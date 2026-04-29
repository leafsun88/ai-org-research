"""
播客转录脚本 — Groq优先 + DashScope兜底 (v4: RSS刷新+本地OSS兜底)
============================================================
核心改进:
  - 转录前先用RSS feed刷新音频URL（解决anchor.fm签名过期问题）
  - 对失败URL自动重试一次（用刷新后的URL）
  - 优先用Groq Whisper转录RSS/metadata音频URL（更快、更轻）
  - Groq失败或额度不足时，再提交百炼/千问Paraformer-v2
  - 远程URL百炼拉取失败时，本地下载音频并上传百炼OSS兜底
  - URL预检失败时也不直接放弃，继续尝试本地下载/OSS转录

流程:
  1. 读取播客元数据JSON
  2. 用RSS feed刷新过期的音频URL
  3. 验证URL可达性
  4. 提交Groq Whisper URL转录
  5. Groq失败时提交百炼Paraformer-v2 URL转录
  6. 百炼URL失败时尝试本地_audio_cache + 百炼OSS上传
  7. 保存transcript为.md文件
"""

import os
import sys
import json
import time
import re
import shutil
import subprocess
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from http import HTTPStatus
from datetime import datetime
from typing import Optional

try:
    from target_config import load_target, target_key, target_script_root
except ImportError:
    load_target = None
    target_script_root = None

try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

from dashscope.audio.asr import Transcription
from dashscope.utils.oss_utils import OssUtils

DB_DIR = Path(__file__).parent.parent
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': '*/*',
}

# ── RSS Feed缓存 ──
_RSS_CACHE = {}  # feed_url -> {title: audio_url}
_TARGET_CACHE = {}
GROQ_TRANSCRIPTIONS_ENDPOINT = 'https://api.groq.com/openai/v1/audio/transcriptions'
DASHSCOPE_REST_TRANSCRIPTION_ENDPOINT = 'https://dashscope.aliyuncs.com/api/v1/services/audio/asr/transcription'
DASHSCOPE_REST_TASK_ENDPOINT = 'https://dashscope.aliyuncs.com/api/v1/tasks/'


def staging_root_for_ticker(ticker: str) -> Path:
    """Return company-local staging root when ticker is a configured target."""
    if load_target and target_script_root:
        try:
            return target_script_root(load_target(ticker))
        except Exception:
            pass
    return DB_DIR / ticker


def default_episodes_file(ticker: str) -> Path:
    root = staging_root_for_ticker(ticker)
    candidates = [
        root / 'sources' / 'podcasts' / 'metadata' / '_podcast_episodes.json',
        root / '_podcast_episodes.json',
        DB_DIR / ticker / '_podcast_episodes.json',
    ]
    for path in candidates:
        if path.exists():
            return path
    return candidates[0]


def load_project_env():
    """Load local .env without adding python-dotenv as a dependency."""
    for env_path in [
        Path.cwd() / '.env',
        Path(__file__).resolve().parents[2] / '.env',
        Path(__file__).resolve().parents[1] / '.env',
    ]:
        if not env_path.exists():
            continue
        try:
            for raw_line in env_path.read_text(encoding='utf-8').splitlines():
                line = raw_line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value
        except Exception:
            pass


load_project_env()


def target_frontmatter(ticker: str) -> str:
    """Return target manifest frontmatter if this ticker is configured."""
    if not load_target:
        return ""
    key = ticker.upper()
    if key not in _TARGET_CACHE:
        try:
            _TARGET_CACHE[key] = load_target(key)
        except Exception:
            _TARGET_CACHE[key] = None
    target = _TARGET_CACHE.get(key)
    if not target:
        return ""
    return (
        f"company: {json.dumps(target.get('company_name', ''))}\n"
        f"research_key: {target_key(target)}\n"
        f"fetched_at: {datetime.now().isoformat(timespec='seconds')}\n"
    )


def fetch_rss_audio_urls(feed_url: str) -> dict:
    """从RSS feed获取所有episode的音频URL映射 {title_prefix: audio_url}"""
    if feed_url in _RSS_CACHE:
        return _RSS_CACHE[feed_url]

    result = {}
    try:
        r = requests.get(feed_url, headers=HEADERS, timeout=30)
        if r.status_code != 200:
            return result
        root = ET.fromstring(r.content)
        for item in root.findall('.//item'):
            title_el = item.find('title')
            enclosure = item.find('enclosure')
            if title_el is not None and enclosure is not None:
                title = (title_el.text or '')[:40].lower().strip()
                audio_url = enclosure.get('url', '')
                if title and audio_url:
                    result[title] = audio_url
    except Exception:
        pass

    _RSS_CACHE[feed_url] = result
    return result


def get_rss_feed_url(podcast_id: str) -> str:
    """通过iTunes lookup获取podcast的RSS feed URL"""
    if not podcast_id:
        return ''
    try:
        r = requests.get('https://itunes.apple.com/lookup',
                         params={'id': podcast_id}, timeout=15)
        if r.status_code == 200:
            results = r.json().get('results', [])
            if results:
                return results[0].get('feedUrl', '')
    except Exception:
        pass
    return ''


def refresh_audio_url(ep: dict) -> str:
    """尝试通过RSS feed获取最新的音频URL"""
    # 如果有podcast_id，用它获取RSS
    podcast_id = ep.get('collectionId', ep.get('collection_id', ep.get('podcast_id', '')))
    if podcast_id:
        feed_url = get_rss_feed_url(str(podcast_id))
        if feed_url:
            rss_urls = fetch_rss_audio_urls(feed_url)
            title_prefix = ep.get('title', '')[:40].lower().strip()
            if title_prefix in rss_urls:
                return rss_urls[title_prefix]
            # Fuzzy match: check if any RSS title contains our title prefix
            for rss_title, rss_url in rss_urls.items():
                if title_prefix[:20] in rss_title or rss_title[:20] in title_prefix:
                    return rss_url

    # 如果有feedUrl直接用
    feed_url = ep.get('feedUrl', ep.get('feed_url', ''))
    if feed_url:
        rss_urls = fetch_rss_audio_urls(feed_url)
        title_prefix = ep.get('title', '')[:40].lower().strip()
        if title_prefix in rss_urls:
            return rss_urls[title_prefix]
        for rss_title, rss_url in rss_urls.items():
            if title_prefix[:20] in rss_title or rss_title[:20] in title_prefix:
                return rss_url

    return ''


def verify_audio_url(url: str, timeout: int = 10) -> tuple:
    """验证URL是否可达且是音频文件。返回 (ok, final_url, reason)"""
    try:
        r = requests.head(url, allow_redirects=True, headers=HEADERS, timeout=timeout)
        final_url = r.url
        ct = r.headers.get('Content-Type', '')

        if r.status_code == 403:
            return False, final_url, 'HTTP 403 Forbidden (签名过期)'
        if r.status_code != 200:
            return False, final_url, f'HTTP {r.status_code}'
        if 'html' in ct and 'audio' not in ct:
            return False, final_url, f'HTML page, not audio ({ct})'

        return True, final_url, 'OK'
    except requests.exceptions.SSLError:
        return False, url, 'SSL Error'
    except requests.exceptions.Timeout:
        return False, url, 'Timeout'
    except Exception as e:
        return False, url, str(e)


def resolve_audio_url(url: str, timeout: int = 15) -> str:
    """Resolve redirect chains to get the final audio URL."""
    try:
        r = requests.head(url, allow_redirects=True, headers=HEADERS, timeout=timeout)
        return r.url
    except Exception:
        try:
            r = requests.get(url, allow_redirects=True, headers=HEADERS,
                             timeout=timeout, stream=True)
            final_url = r.url
            r.close()
            return final_url
        except Exception:
            return url


def transcribe_groq_url(audio_url: str, language: str = 'auto') -> dict:
    """Transcribe a single audio URL using Groq Whisper.

    Groq accepts the `url` field, but the request still needs to be
    multipart/form-data. Plain form-urlencoded requests return 400.
    """
    api_key = os.environ.get('GROQ_API_KEY', '').strip()
    if not api_key:
        return {'success': False, 'error': 'GROQ_API_KEY not set', 'provider': 'groq'}

    model = os.environ.get('GROQ_STT_MODEL', 'whisper-large-v3-turbo')
    files = {
        'model': (None, model),
        'url': (None, audio_url),
        'response_format': (None, 'verbose_json'),
        'temperature': (None, '0'),
    }
    if language != 'auto' and ',' not in language:
        files['language'] = (None, language)

    try:
        r = requests.post(
            GROQ_TRANSCRIPTIONS_ENDPOINT,
            headers={'Authorization': f'Bearer {api_key}'},
            files=files,
            timeout=int(os.environ.get('GROQ_TRANSCRIBE_TIMEOUT_SECONDS', '180')),
        )
        try:
            payload = r.json()
        except Exception:
            payload = {'raw': r.text[:1000]}

        if r.status_code == 429:
            return {
                'success': False,
                'error': 'Groq rate limit or quota exceeded',
                'provider': 'groq',
                'retryable': True,
                'raw': payload,
            }
        if not r.ok:
            message = payload.get('error', {}).get('message') if isinstance(payload, dict) else ''
            return {
                'success': False,
                'error': f"Groq failed: {message or r.status_code}",
                'provider': 'groq',
                'raw': payload,
            }

        full_text = (payload.get('text') or '').strip()
        if not full_text:
            return {
                'success': False,
                'error': 'Groq empty transcript',
                'provider': 'groq',
                'raw': payload,
            }

        return {
            'success': True,
            'text': full_text,
            'chars': len(full_text),
            'provider': 'groq',
            'engine': f'groq_{model}',
            'model': model,
            'duration': payload.get('duration'),
            'segments': len(payload.get('segments', []) or []),
        }
    except requests.exceptions.RequestException as e:
        return {'success': False, 'error': f'Groq request failed: {e}', 'provider': 'groq'}
    except Exception as e:
        return {'success': False, 'error': f'Groq unexpected error: {e}', 'provider': 'groq'}


def transcribe_dashscope_url(audio_url: str, language: str = 'auto') -> dict:
    """Transcribe a single audio URL using DashScope Paraformer-v2.
    language='auto' lets the model auto-detect (best for mixed zh/en content).
    """
    call_kwargs = {
        'model': 'paraformer-v2',
        'file_urls': [audio_url],
    }
    # 只在明确指定语言时传language_hints，auto模式让模型自动检测
    if language != 'auto':
        lang_hints = language.split(',') if ',' in language else [language]
        call_kwargs['language_hints'] = lang_hints

    retries = 3
    max_poll_seconds = int(os.environ.get('PODCAST_MAX_POLL_SECONDS', '900'))
    poll_interval = 5
    last_error = None

    for attempt in range(1, retries + 1):
        try:
            task_response = Transcription.async_call(**call_kwargs)

            if task_response.status_code != HTTPStatus.OK:
                return {'success': False, 'error': f'Submit failed: {task_response.message}'}

            task_id = task_response.output.get('task_id')
            if not task_id:
                return {'success': False, 'error': 'No task_id returned'}

            result = None
            started = time.time()
            while time.time() - started < max_poll_seconds:
                result = Transcription.fetch(task=task_id)
                if result.status_code != HTTPStatus.OK:
                    return {'success': False, 'error': f'Transcription fetch failed: {result.message}'}

                task_status = result.output.get('task_status')
                if task_status in ('SUCCEEDED', 'FAILED'):
                    break
                time.sleep(poll_interval)

            if result is None:
                return {'success': False, 'error': 'No result returned from polling'}

            task_status = result.output.get('task_status')
            if task_status not in ('SUCCEEDED', 'FAILED'):
                return {'success': False, 'error': f'Transcription polling timeout after {max_poll_seconds}s'}

            results = result.output.get('results', [])
            if not results:
                return {'success': False, 'error': f'No results returned (task_status={task_status})'}

            # Check subtask status
            subtask = results[0]
            if subtask.get('subtask_status') == 'FAILED':
                code = subtask.get('code', '')
                return {'success': False, 'error': f'Subtask failed: {code}'}

            trans_url = subtask.get('transcription_url')
            if not trans_url:
                return {'success': False, 'error': 'No transcription_url'}

            tr = requests.get(trans_url, timeout=30)
            tr_data = tr.json()

            transcripts = tr_data.get('transcripts', [])
            if not transcripts:
                return {'success': False, 'error': 'Empty transcript', 'raw': tr_data}

            full_text = '\n'.join(t.get('text', '') for t in transcripts).strip()

            return {
                'success': True,
                'text': full_text,
                'chars': len(full_text),
                'task_id': task_id,
                'provider': 'dashscope',
                'engine': 'dashscope_paraformer_v2',
            }

        except requests.exceptions.RequestException as e:
            last_error = str(e)
            if attempt < retries:
                time.sleep(attempt * 2)
                continue
            return {'success': False, 'error': last_error}
        except Exception as e:
            last_error = str(e)
            if ('SSLError' in last_error or 'RemoteDisconnected' in last_error or 'EOF occurred' in last_error) and attempt < retries:
                time.sleep(attempt * 2)
                continue
            return {'success': False, 'error': last_error}

    return {'success': False, 'error': last_error or 'Unknown transcription error', 'provider': 'dashscope'}


def standardize_audio_for_rest(local_path: Path, standard_dir: Path, title: str, date: str) -> Optional[Path]:
    """Convert a downloaded audio file into a stable WAV container for REST fallback."""
    standard_dir.mkdir(parents=True, exist_ok=True)
    target_path = standard_dir / f"{date}_{safe_title(title)}.wav"
    if target_path.exists() and target_path.stat().st_size > 0:
        return target_path

    afconvert = shutil.which('afconvert')
    if not afconvert:
        print("    Standardize fallback unavailable: afconvert not found")
        return None

    cmd = [
        afconvert,
        str(local_path),
        str(target_path),
        '-f', 'WAVE',
        '-d', 'LEI16@16000',
        '-c', '1',
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if proc.returncode != 0:
            err = (proc.stderr or proc.stdout or '').strip()
            print(f"    Standardize fallback failed: {err[:160]}")
            if target_path.exists():
                target_path.unlink(missing_ok=True)
            return None
        if not target_path.exists() or target_path.stat().st_size == 0:
            print("    Standardize fallback failed: empty output")
            target_path.unlink(missing_ok=True)
            return None
        print(f"    Standardized audio: {target_path.name} ({target_path.stat().st_size/1024/1024:.1f} MB)")
        return target_path
    except Exception as e:
        print(f"    Standardize fallback failed: {str(e)[:160]}")
        if target_path.exists():
            target_path.unlink(missing_ok=True)
        return None


def transcribe_dashscope_rest(file_url: str, language: str = 'auto') -> dict:
    """Transcribe a single audio URL using DashScope RESTful API."""
    api_key = os.environ.get('DASHSCOPE_API_KEY', '').strip()
    if not api_key:
        return {'success': False, 'error': 'DASHSCOPE_API_KEY not set', 'provider': 'dashscope_rest'}

    payload = {
        'model': 'paraformer-v2',
        'input': {
            'file_urls': [file_url],
        },
    }
    if language != 'auto':
        payload['parameters'] = {
            'language_hints': language.split(',') if ',' in language else [language],
        }

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
        'X-DashScope-Async': 'enable',
    }
    if file_url.startswith('oss://'):
        headers['X-DashScope-OssResourceResolve'] = 'enable'

    try:
        submit = requests.post(
            DASHSCOPE_REST_TRANSCRIPTION_ENDPOINT,
            headers=headers,
            data=json.dumps(payload, ensure_ascii=False),
            timeout=int(os.environ.get('DASHSCOPE_REST_SUBMIT_TIMEOUT_SECONDS', '60')),
        )
        try:
            submit_data = submit.json()
        except Exception:
            submit_data = {'raw': submit.text[:1000]}

        if not submit.ok:
            message = submit_data.get('message') if isinstance(submit_data, dict) else ''
            return {
                'success': False,
                'error': f"DashScope REST submit failed: {message or submit.status_code}",
                'provider': 'dashscope_rest',
                'raw': submit_data,
            }

        task_id = submit_data.get('output', {}).get('task_id') or submit_data.get('task_id')
        if not task_id:
            return {
                'success': False,
                'error': 'DashScope REST submit returned no task_id',
                'provider': 'dashscope_rest',
                'raw': submit_data,
            }

        retries = 3
        max_poll_seconds = int(os.environ.get('PODCAST_MAX_POLL_SECONDS', '900'))
        poll_interval = 5
        last_error = None
        result = None
        for attempt in range(1, retries + 1):
            started = time.time()
            while time.time() - started < max_poll_seconds:
                poll = requests.post(
                    f"{DASHSCOPE_REST_TASK_ENDPOINT}{task_id}",
                    headers={'Authorization': f'Bearer {api_key}'},
                    timeout=int(os.environ.get('DASHSCOPE_REST_POLL_TIMEOUT_SECONDS', '30')),
                )
                try:
                    poll_data = poll.json()
                except Exception:
                    poll_data = {'raw': poll.text[:1000]}

                if not poll.ok:
                    last_error = f"DashScope REST poll failed: {poll_data.get('message') if isinstance(poll_data, dict) else poll.status_code}"
                    break

                result = poll_data.get('output', poll_data)
                task_status = result.get('task_status')
                if task_status in ('SUCCEEDED', 'FAILED'):
                    break
                time.sleep(poll_interval)

            if result is None:
                last_error = 'DashScope REST produced no polling result'
            else:
                task_status = result.get('task_status')
                if task_status not in ('SUCCEEDED', 'FAILED'):
                    last_error = f'DashScope REST polling timeout after {max_poll_seconds}s'
                else:
                    results = result.get('results', [])
                    if not results:
                        last_error = f'No results returned (task_status={task_status})'
                    else:
                        subtask = results[0]
                        if subtask.get('subtask_status') == 'FAILED':
                            code = subtask.get('code', '')
                            message = subtask.get('message', '')
                            last_error = f'Subtask failed: {code or message or "unknown"}'
                        else:
                            trans_url = subtask.get('transcription_url')
                            if not trans_url:
                                last_error = 'No transcription_url'
                            else:
                                tr = requests.get(trans_url, timeout=30)
                                tr_data = tr.json()
                                transcripts = tr_data.get('transcripts', [])
                                if not transcripts:
                                    last_error = 'Empty transcript'
                                else:
                                    full_text = '\n'.join(t.get('text', '') for t in transcripts).strip()
                                    if not full_text:
                                        last_error = 'Empty transcript'
                                    else:
                                        return {
                                            'success': True,
                                            'text': full_text,
                                            'chars': len(full_text),
                                            'task_id': task_id,
                                            'provider': 'dashscope_rest',
                                            'engine': 'dashscope_paraformer_v2_rest',
                                        }

            if last_error and attempt < retries and ('SSLError' in last_error or 'RemoteDisconnected' in last_error or 'EOF occurred' in last_error):
                time.sleep(attempt * 2)
                continue
            break

        return {
            'success': False,
            'error': last_error or 'Unknown transcription error',
            'provider': 'dashscope_rest',
            'task_id': task_id,
        }
    except requests.exceptions.RequestException as e:
        return {'success': False, 'error': f'DashScope REST request failed: {e}', 'provider': 'dashscope_rest'}
    except Exception as e:
        return {'success': False, 'error': f'DashScope REST unexpected error: {e}', 'provider': 'dashscope_rest'}


def download_audio_to_cache(audio_url: str, cache_dir: Path, title: str, date: str) -> Optional[Path]:
    """Download an audio URL locally so DashScope can ingest it via OSS upload."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    ext = Path(urlparse_path(audio_url)).suffix
    if not ext or len(ext) > 8:
        ext = '.mp3'
    filename = f"{date}_{safe_title(title)}{ext}"
    filepath = cache_dir / filename
    if filepath.exists() and filepath.stat().st_size > 0:
        return filepath

    try:
        with requests.get(audio_url, headers=HEADERS, timeout=(15, 300), stream=True, allow_redirects=True) as r:
            if r.status_code != 200:
                print(f"    Local download failed: HTTP {r.status_code}")
                return None
            with filepath.open('wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
        if filepath.stat().st_size == 0:
            filepath.unlink(missing_ok=True)
            return None
        print(f"    Downloaded audio cache: {filepath.name} ({filepath.stat().st_size/1024/1024:.1f} MB)")
        return filepath
    except Exception as e:
        print(f"    Local download failed: {str(e)[:120]}")
        return None


def urlparse_path(url: str) -> str:
    try:
        from urllib.parse import urlparse
        return urlparse(url).path
    except Exception:
        return ''


def upload_local_audio_to_oss(local_path: Path) -> str:
    file_url, _ = OssUtils.upload(
        model='paraformer-v2',
        file_path=str(local_path),
        api_key=os.environ.get('DASHSCOPE_API_KEY'),
    )
    return file_url


def episode_key(ep: dict) -> str:
    title = ep.get('title', ep.get('trackName', '')).strip()
    date = ep.get('date', ep.get('releaseDate', ''))[:10]
    return f"{date}|{title}"


def safe_title(title: str, sep: str = '-') -> str:
    return ''.join(c if c.isalnum() or c in ' -_' else '' for c in title)[:60].strip().replace(' ', sep)


def existing_transcript_path(output_dir: Path, ep: dict) -> str:
    title = ep.get('title', ep.get('trackName', ''))
    date = ep.get('date', ep.get('releaseDate', ''))[:10]
    normalized = normalize_identity_text(title)
    if not normalized or not date:
        return ''
    for path in output_dir.glob('*.md'):
        try:
            text = path.read_text(encoding='utf-8', errors='ignore')[:4000]
        except Exception:
            continue
        file_title = parse_frontmatter_value(text, 'title')
        file_date = parse_frontmatter_value(text, 'date')
        if file_date == date and normalize_identity_text(file_title) == normalized:
            return str(path)
    return ''


def normalize_identity_text(value: str) -> str:
    return re.sub(r'[^a-z0-9]+', '', (value or '').lower())


def parse_frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf'^{re.escape(key)}:\s*(.+)$', text, re.MULTILINE)
    if not match:
        return ''
    raw = match.group(1).strip()
    if raw in {'', 'null'}:
        return ''
    try:
        parsed = json.loads(raw)
        return str(parsed)
    except Exception:
        return raw.strip('"').strip("'")


def write_status_files(
    output_dir: Path,
    ticker: str,
    status_by_key: dict,
    retry_rounds: int,
    min_duration_min: int,
    status_suffix: str = '',
):
    statuses = list(status_by_key.values())
    non_failure_statuses = {
        'success',
        'existing_success',
        'skipped_short',
        'deferred_max_limit',
    }
    failures = [
        item for item in statuses
        if item.get('status') not in non_failure_statuses
    ]
    skipped = [
        item for item in statuses
        if item.get('status') in ('skipped_short', 'deferred_max_limit')
    ]
    status_doc = {
        'ticker': ticker,
        'generated_at': datetime.now().isoformat(timespec='seconds'),
        'retry_rounds': retry_rounds,
        'min_duration_min': min_duration_min,
        'total_records': len(statuses),
        'success_records': sum(1 for item in statuses if item.get('status') in ('success', 'existing_success')),
        'skipped_records': len(skipped),
        'failure_records': len(failures),
        'statuses': statuses,
    }
    suffix = status_suffix or ''
    (output_dir / f'_podcast_transcription_status{suffix}.json').write_text(
        json.dumps(status_doc, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )
    (output_dir / f'_podcast_transcription_failures{suffix}.json').write_text(
        json.dumps(failures, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )
    return failures


def transcribe_episode(ep: dict, ticker: str, output_dir: Path, language: str, attempt_round: int, index: int, total: int) -> dict:
    title = ep.get('title', f'Episode {index}')
    audio_url = ep.get('audio_url', ep.get('url', ''))
    date = ep.get('date', ep.get('releaseDate', ''))[:10]
    podcast_name = ep.get('podcast', ep.get('show', ep.get('collectionName', '')))

    print(f"  [round {attempt_round} | {index}/{total}] {title[:60]}...")

    fresh_url = ''

    # Step 1: Verify original URL
    ok, resolved_url, reason = verify_audio_url(audio_url)

    if not ok:
        print(f"    Original URL failed: {reason}")

        # Step 2: Try RSS refresh
        print(f"    Trying RSS feed refresh...")
        fresh_url = refresh_audio_url(ep)

        if fresh_url and fresh_url != audio_url:
            print(f"    Got fresh URL from RSS")
            ok2, resolved_url, reason2 = verify_audio_url(fresh_url)
            if ok2:
                print(f"    Fresh URL works")
                audio_url = fresh_url
                ok = True
            else:
                print(f"    Fresh URL also failed: {reason2}")
        else:
            print(f"    No RSS feed available or title not matched")

        if not ok:
            # Step 3: Try resolve redirect anyway, then continue to local
            # fallback instead of dropping the episode before we try a download.
            resolved_url = resolve_audio_url(audio_url)
            if resolved_url != audio_url:
                print(f"    Trying resolved URL anyway: {resolved_url[:60]}")
            else:
                print(f"    URL not verified; will still try DashScope/local fallback")
    else:
        resolved_url = resolve_audio_url(audio_url)

    # Step 4: Transcribe with multiple candidate URLs.
    # Provider order is deliberate:
    #   1) Groq URL transcription: fastest and no OSS ceremony.
    #   2) DashScope URL transcription: second provider / quota fallback.
    #   3) Local download + DashScope OSS: only after remote URL ingestion fails.
    candidate_urls = []
    for candidate in [resolved_url, audio_url, fresh_url]:
        if candidate and candidate not in candidate_urls:
            candidate_urls.append(candidate)

    result = {'success': False, 'error': 'No candidate URL available'}
    tried_urls = []
    provider_attempts = []
    local_fallback_path = ''
    standard_audio_path = ''
    original_audio_url = audio_url

    for idx, candidate_url in enumerate(candidate_urls, 1):
        tried_urls.append(f'groq:{candidate_url}')
        print(f"    Groq transcribing URL... ({idx}/{len(candidate_urls)})")
        result = transcribe_groq_url(candidate_url, language=language)
        provider_attempts.append({
            'provider': 'groq',
            'url': candidate_url,
            'success': result.get('success', False),
            'error': result.get('error', ''),
        })
        if result['success']:
            audio_url = candidate_url
            break

        error_text = result.get('error', '')
        print(f"    Groq candidate failed: {error_text[:120]}")

    if not result['success']:
        for idx, candidate_url in enumerate(candidate_urls, 1):
            tried_urls.append(f'dashscope:{candidate_url}')
            print(f"    DashScope transcribing URL... ({idx}/{len(candidate_urls)})")
            result = transcribe_dashscope_url(candidate_url, language=language)
            provider_attempts.append({
                'provider': 'dashscope',
                'url': candidate_url,
                'success': result.get('success', False),
                'error': result.get('error', ''),
            })
            if result['success']:
                audio_url = candidate_url
                break

            error_text = result.get('error', '')
            if 'FILE_403' in error_text or 'FILE_DOWNLOAD_FAILED' in error_text:
                print(f"    DashScope could not fetch candidate URL")
                continue
            if 'HTTPSConnectionPool' in error_text or 'RemoteDisconnected' in error_text or 'EOF occurred' in error_text:
                print(f"    Transient network error, trying next candidate...")
                continue
            print(f"    DashScope candidate failed: {error_text[:120]}")

    if not result['success'] and candidate_urls:
        print(f"    Trying local download + DashScope OSS upload fallback...")
        cache_dir = output_dir / '_audio_cache'
        for candidate_url in candidate_urls:
            local_path = download_audio_to_cache(candidate_url, cache_dir, title, date)
            if not local_path:
                continue
            local_fallback_path = str(local_path)
            try:
                oss_url = upload_local_audio_to_oss(local_path)
                tried_urls.append(f'dashscope_oss:{oss_url}')
                print(f"    Uploaded local audio to OSS; transcribing cached audio...")
                result = transcribe_dashscope_url(oss_url, language=language)
                provider_attempts.append({
                    'provider': 'dashscope_oss',
                    'url': oss_url,
                    'source_url': candidate_url,
                    'success': result.get('success', False),
                    'error': result.get('error', ''),
                })
                if result['success']:
                    audio_url = oss_url
                    break
                print(f"    Cached audio transcription failed: {result.get('error', '')[:120]}")
            except Exception as e:
                result = {'success': False, 'error': f'Local OSS fallback failed: {e}'}
                print(f"    Local OSS fallback failed: {str(e)[:120]}")

    if not result['success'] and candidate_urls:
        print(f"    Trying standard audio + DashScope REST fallback...")
        cache_dir = output_dir / '_audio_cache'
        standard_dir = output_dir / '_standard_audio'
        for candidate_url in candidate_urls:
            raw_local_path = download_audio_to_cache(candidate_url, cache_dir, title, date)
            if not raw_local_path:
                continue
            local_fallback_path = str(raw_local_path)
            standard_path = standardize_audio_for_rest(raw_local_path, standard_dir, title, date)
            provider_attempts.append({
                'provider': 'standard_audio',
                'url': candidate_url,
                'local_audio_path': str(raw_local_path),
                'standard_audio_path': str(standard_path) if standard_path else '',
                'success': bool(standard_path),
                'error': '' if standard_path else 'standardization_failed',
            })
            if not standard_path:
                continue
            standard_audio_path = str(standard_path)
            try:
                oss_url = upload_local_audio_to_oss(standard_path)
                tried_urls.append(f'dashscope_rest:{oss_url}')
                print(f"    Uploaded standardized audio to OSS; transcribing via REST...")
                result = transcribe_dashscope_rest(oss_url, language=language)
                provider_attempts.append({
                    'provider': 'dashscope_rest',
                    'url': oss_url,
                    'source_url': candidate_url,
                    'local_audio_path': str(raw_local_path),
                    'standard_audio_path': str(standard_path),
                    'success': result.get('success', False),
                    'error': result.get('error', ''),
                })
                if result['success']:
                    audio_url = oss_url
                    break
                print(f"    Standard audio REST transcription failed: {result.get('error', '')[:120]}")
            except Exception as e:
                result = {'success': False, 'error': f'Standard audio REST fallback failed: {e}'}
                print(f"    Standard audio REST fallback failed: {str(e)[:120]}")

    if result['success']:
        filename = f"{date}_{safe_title(title)}.md"
        md = f"""---
ticker: {ticker}
type: podcast_transcript
title: {json.dumps(title)}
podcast: {json.dumps(podcast_name)}
date: {date}
audio_url: {json.dumps(audio_url)}
source_audio_url: {json.dumps(original_audio_url)}
local_audio_path: {json.dumps(local_fallback_path)}
standard_audio_path: {json.dumps(standard_audio_path)}
{target_frontmatter(ticker)}source: podcast_audio
language: {language}
chars: {result['chars']}
credibility: S2-S3
evidence: E2
transcription_provider: {result.get('provider', '')}
transcription_engine: {result.get('engine', '')}
---

# {title}

**Podcast**: {podcast_name}
**Date**: {date}

---

## Transcript

{result['text']}
"""
        filepath = output_dir / filename
        filepath.write_text(md, encoding='utf-8')
        print(f"    {result['chars']:,} chars -> {filename}")
        if local_fallback_path:
            try:
                Path(local_fallback_path).unlink(missing_ok=True)
            except Exception:
                pass
        return {
            'status': 'success',
            'title': title,
            'date': date,
            'podcast': podcast_name,
            'audio_url': audio_url,
            'source_audio_url': original_audio_url,
            'local_audio_path': local_fallback_path,
            'standard_audio_path': standard_audio_path,
            'transcript_path': str(filepath),
            'chars': result['chars'],
            'task_id': result.get('task_id', ''),
            'attempt_round': attempt_round,
            'tried_urls': tried_urls,
            'provider_attempts': provider_attempts,
            'transcription_provider': result.get('provider', ''),
            'transcription_engine': result.get('engine', ''),
        }

    err = result['error']
    print(f"    Failed: {err}")
    return {
        'status': 'failed',
        'title': title,
        'date': date,
        'podcast': podcast_name,
        'audio_url': audio_url,
        'attempt_round': attempt_round,
        'error': err,
        'stage': 'asr_transcription',
        'tried_urls': tried_urls,
        'provider_attempts': provider_attempts,
        'local_audio_path': local_fallback_path,
        'standard_audio_path': standard_audio_path,
    }


def process_podcast_episodes(ticker: str, max_episodes: int = 10, language: str = 'auto', episodes_path: str = ''):
    """Process podcast episodes with RSS refresh + verify + transcribe."""
    episodes_file = Path(episodes_path) if episodes_path else default_episodes_file(ticker)
    if not episodes_file.exists():
        print(f"No podcast episodes file found: {episodes_file}")
        return False

    with open(episodes_file) as f:
        episodes = json.load(f)

    print(f"\n{'='*60}")
    print(f"  Podcast Transcription v4 (Groq -> DashScope -> local OSS): {ticker}")
    print(f"  Episodes file: {episodes_file}")
    print(f"  Episodes: {len(episodes)} available, processing max {max_episodes}")
    print(f"  Language: {language}")
    print(f"{'='*60}\n")

    output_dir = staging_root_for_ticker(ticker) / 'sources' / 'podcasts' / 'transcripts'
    output_dir.mkdir(parents=True, exist_ok=True)
    status_suffix = os.environ.get('PODCAST_STATUS_SUFFIX', '').strip()

    # Default: skip known short clips; unknown duration is still processed.
    min_duration_min = int(os.environ.get('PODCAST_MIN_DURATION_MIN', '10'))
    retry_rounds = int(os.environ.get('PODCAST_RETRY_ROUNDS', '3'))
    to_process = []
    status_by_key = {}
    for ep in episodes:
        key = episode_key(ep)
        title = ep.get('title', ep.get('trackName', ''))
        date = ep.get('date', ep.get('releaseDate', ''))[:10]
        podcast_name = ep.get('podcast', ep.get('show', ep.get('collectionName', '')))
        audio_url = ep.get('audio_url', ep.get('url', ''))
        if not audio_url or not audio_url.startswith('http'):
            status_by_key[key] = {
                'status': 'failed',
                'title': title,
                'date': date,
                'podcast': podcast_name,
                'audio_url': audio_url,
                'error': 'missing_audio_url',
                'stage': 'metadata_validation',
            }
            continue

        existing_path = existing_transcript_path(output_dir, ep)
        if existing_path:
            status_by_key[key] = {
                'status': 'existing_success',
                'title': title,
                'date': date,
                'podcast': podcast_name,
                'audio_url': audio_url,
                'transcript_path': existing_path,
            }
            continue

        duration = ep.get('duration_min', ep.get('trackTimeMillis', 0))
        if isinstance(duration, (int, float)) and duration > 1000:
            # trackTimeMillis is in ms, convert to minutes
            duration = duration / 60000
        if min_duration_min and isinstance(duration, (int, float)) and 0 < duration < min_duration_min:
            status_by_key[key] = {
                'status': 'skipped_short',
                'title': title,
                'date': date,
                'podcast': podcast_name,
                'audio_url': audio_url,
                'duration_min': duration,
                'error': f'shorter_than_{min_duration_min}_minutes',
                'stage': 'duration_filter',
            }
            continue

        to_process.append(ep)

    limit = len(to_process) if max_episodes <= 0 else max_episodes
    selected = to_process[:limit]
    deferred = to_process[limit:]
    for ep in deferred:
        key = episode_key(ep)
        status_by_key[key] = {
            'status': 'deferred_max_limit',
            'title': ep.get('title', ep.get('trackName', '')),
            'date': ep.get('date', ep.get('releaseDate', ''))[:10],
            'podcast': ep.get('podcast', ep.get('show', ep.get('collectionName', ''))),
            'audio_url': ep.get('audio_url', ep.get('url', '')),
            'error': f'max_episodes_limit_{max_episodes}',
            'stage': 'selection',
        }

    print(f"  Existing transcripts: {sum(1 for v in status_by_key.values() if v.get('status') == 'existing_success')}")
    print(f"  Processing {len(selected)} episodes, retry rounds {retry_rounds}...\n")

    pending = selected
    for attempt_round in range(1, retry_rounds + 1):
        if not pending:
            break
        next_pending = []
        total = len(pending)
        for i, ep in enumerate(pending, 1):
            status_by_key[episode_key(ep)] = {
                'status': 'running',
                'title': ep.get('title', ep.get('trackName', '')),
                'date': ep.get('date', ep.get('releaseDate', ''))[:10],
                'podcast': ep.get('podcast', ep.get('show', ep.get('collectionName', ''))),
                'audio_url': ep.get('audio_url', ep.get('url', '')),
                'attempt_round': attempt_round,
                'stage': 'asr_transcription',
                'started_at': datetime.now().isoformat(timespec='seconds'),
            }
            write_status_files(output_dir, ticker, status_by_key, retry_rounds, min_duration_min, status_suffix=status_suffix)
            result = transcribe_episode(ep, ticker, output_dir, language, attempt_round, i, total)
            status_by_key[episode_key(ep)] = result
            write_status_files(output_dir, ticker, status_by_key, retry_rounds, min_duration_min, status_suffix=status_suffix)
            if result.get('status') != 'success':
                next_pending.append(ep)
            time.sleep(1)
        pending = next_pending
        if pending and attempt_round < retry_rounds:
            print(f"\n  Retrying {len(pending)} failed episodes after script-level retry round {attempt_round}...\n")
            time.sleep(3)

    # Summary
    failures = write_status_files(output_dir, ticker, status_by_key, retry_rounds, min_duration_min, status_suffix=status_suffix)
    fail_reasons = {}
    for item in failures:
        reason = item.get('error', 'unknown')[:80]
        fail_reasons[reason] = fail_reasons.get(reason, 0) + 1
    success_count = len(status_by_key) - len(failures)

    print(f"\n{'='*60}")
    print(f"  Done: {success_count}/{len(status_by_key)} succeeded")
    if fail_reasons:
        print(f"  Failure reasons:")
        for reason, count in sorted(fail_reasons.items(), key=lambda x: -x[1]):
            print(f"    {count}x - {reason}")
        print(f"  Failure file: {output_dir / f'_podcast_transcription_failures{status_suffix}.json'}")
    print(f"  Status file: {output_dir / f'_podcast_transcription_status{status_suffix}.json'}")
    print(f"  Output: {output_dir}")
    print(f"{'='*60}\n")

    return len(failures) == 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python fetch_podcast_transcript.py TICKER [max_episodes] [language] [episodes_json_path]")
        print("Example: python fetch_podcast_transcript.py APP 50 en")
        print("Example: python fetch_podcast_transcript.py POP 64 zh,en")
        sys.exit(1)

    ticker = sys.argv[1]
    max_eps = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    lang = sys.argv[3] if len(sys.argv) > 3 else 'auto'
    episodes_path = sys.argv[4] if len(sys.argv) > 4 else ''

    ok = process_podcast_episodes(ticker, max_episodes=max_eps, language=lang, episodes_path=episodes_path)
    if not ok:
        sys.exit(2)
