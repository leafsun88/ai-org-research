"""
播客转录脚本 — DashScope Paraformer-v2 (v2: RSS刷新+重试)
============================================================
核心改进:
  - 转录前先用RSS feed刷新音频URL（解决anchor.fm签名过期问题）
  - 对失败URL自动重试一次（用刷新后的URL）
  - 先验证URL可达性再提交百炼（避免浪费API调用）
  - 支持并发提交（百炼batch API一次100个）

流程:
  1. 读取播客元数据JSON
  2. 用RSS feed刷新过期的音频URL
  3. 验证URL可达性
  4. 提交百炼Paraformer-v2转录
  5. 保存transcript为.md文件
"""

import os
import sys
import json
import time
import re
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from http import HTTPStatus

from dashscope.audio.asr import Transcription

DB_DIR = Path(__file__).parent.parent
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': '*/*',
}

# ── RSS Feed缓存 ──
_RSS_CACHE = {}  # feed_url -> {title: audio_url}


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
    podcast_id = ep.get('collectionId', ep.get('podcast_id', ''))
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
    feed_url = ep.get('feedUrl', '')
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


def transcribe_url(audio_url: str, language: str = 'auto') -> dict:
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

    try:
        task_response = Transcription.async_call(**call_kwargs)

        if task_response.status_code != HTTPStatus.OK:
            return {'success': False, 'error': f'Submit failed: {task_response.message}'}

        task_id = task_response.output.get('task_id')
        if not task_id:
            return {'success': False, 'error': 'No task_id returned'}

        result = Transcription.wait(task=task_id)

        if result.status_code != HTTPStatus.OK:
            return {'success': False, 'error': f'Transcription failed: {result.message}'}

        results = result.output.get('results', [])
        if not results:
            return {'success': False, 'error': 'No results returned'}

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
        }

    except Exception as e:
        return {'success': False, 'error': str(e)}


def process_podcast_episodes(ticker: str, max_episodes: int = 10, language: str = 'auto'):
    """Process podcast episodes with RSS refresh + verify + transcribe."""
    episodes_file = DB_DIR / ticker / '_podcast_episodes.json'
    if not episodes_file.exists():
        print(f"No podcast episodes file found: {episodes_file}")
        return

    with open(episodes_file) as f:
        episodes = json.load(f)

    print(f"\n{'='*60}")
    print(f"  Podcast Transcription v2 (RSS Refresh): {ticker}")
    print(f"  Episodes: {len(episodes)} available, processing max {max_episodes}")
    print(f"  Language: {language}")
    print(f"{'='*60}\n")

    output_dir = DB_DIR / ticker / 'sources' / 'podcasts_transcripts'
    output_dir.mkdir(parents=True, exist_ok=True)

    # Filter: skip already transcribed, skip short episodes (<30 min)
    MIN_DURATION_MIN = 30
    to_process = []
    skipped_short = 0
    for ep in episodes:
        audio_url = ep.get('audio_url', ep.get('url', ''))
        if not audio_url or not audio_url.startswith('http'):
            continue

        # Duration filter: skip episodes shorter than 30 minutes
        duration = ep.get('duration_min', ep.get('trackTimeMillis', 0))
        if isinstance(duration, (int, float)) and duration > 1000:
            # trackTimeMillis is in ms, convert to minutes
            duration = duration / 60000
        if isinstance(duration, (int, float)) and 0 < duration < MIN_DURATION_MIN:
            skipped_short += 1
            continue

        title = ep.get('title', '')
        safe_title = ''.join(c if c.isalnum() or c in ' -_' else '' for c in title)[:60].strip().replace(' ', '_')
        if safe_title and list(output_dir.glob(f'*{safe_title[:20]}*')):
            continue
        to_process.append(ep)

    to_process = to_process[:max_episodes]
    if skipped_short:
        print(f"  Skipped {skipped_short} episodes shorter than {MIN_DURATION_MIN} minutes")
    print(f"  Processing {len(to_process)} episodes...\n")

    success_count = 0
    fail_reasons = {}

    for i, ep in enumerate(to_process, 1):
        title = ep.get('title', f'Episode {i}')
        audio_url = ep.get('audio_url', ep.get('url', ''))
        date = ep.get('date', ep.get('releaseDate', ''))[:10]
        podcast_name = ep.get('podcast', ep.get('collectionName', ''))

        print(f"  [{i}/{len(to_process)}] {title[:60]}...")

        # Step 1: Verify original URL
        ok, resolved_url, reason = verify_audio_url(audio_url)

        if not ok:
            print(f"    ⚠ Original URL failed: {reason}")

            # Step 2: Try RSS refresh
            print(f"    🔄 Trying RSS feed refresh...")
            fresh_url = refresh_audio_url(ep)

            if fresh_url and fresh_url != audio_url:
                print(f"    📡 Got fresh URL from RSS")
                ok2, resolved_url, reason2 = verify_audio_url(fresh_url)
                if ok2:
                    print(f"    ✅ Fresh URL works!")
                    audio_url = fresh_url
                    ok = True
                else:
                    print(f"    ❌ Fresh URL also failed: {reason2}")
            else:
                print(f"    ❌ No RSS feed available or title not matched")

            if not ok:
                # Step 3: Try resolve redirect anyway (sometimes百炼can handle it)
                resolved_url = resolve_audio_url(audio_url)
                if resolved_url != audio_url:
                    print(f"    🔗 Trying resolved URL anyway: {resolved_url[:60]}")
                else:
                    fail_reasons[reason] = fail_reasons.get(reason, 0) + 1
                    print(f"    ⏭ Skipping")
                    continue

        else:
            resolved_url = resolve_audio_url(audio_url)

        # Step 4: Transcribe
        print(f"    🎙 Transcribing...")
        result = transcribe_url(resolved_url, language=language)

        if not result['success'] and 'FILE_403' in result.get('error', ''):
            # One more retry: try original URL without resolve
            print(f"    🔄 403 from百炼, retrying with original URL...")
            result = transcribe_url(audio_url, language=language)

        if result['success']:
            safe_title = ''.join(c if c.isalnum() or c in ' -_' else '' for c in title)[:60].strip().replace(' ', '-')
            filename = f"{date}_{safe_title}.md"

            md = f"""---
ticker: {ticker}
type: podcast_transcript
title: "{title}"
podcast: "{podcast_name}"
date: {date}
audio_url: {audio_url}
language: {language}
chars: {result['chars']}
credibility: S2-S3
evidence: E2
transcription_engine: dashscope_paraformer_v2
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
            print(f"    ✅ {result['chars']:,} chars → {filename}")
            success_count += 1
        else:
            err = result['error']
            fail_reasons[err[:50]] = fail_reasons.get(err[:50], 0) + 1
            print(f"    ❌ {err}")

        time.sleep(1)

    # Summary
    print(f"\n{'='*60}")
    print(f"  Done: {success_count}/{len(to_process)} succeeded")
    if fail_reasons:
        print(f"  Failure reasons:")
        for reason, count in sorted(fail_reasons.items(), key=lambda x: -x[1]):
            print(f"    {count}x — {reason}")
    print(f"  Output: {output_dir}")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python fetch_podcast_transcript.py TICKER [max_episodes] [language]")
        print("Example: python fetch_podcast_transcript.py APP 50 en")
        print("Example: python fetch_podcast_transcript.py POP 64 zh,en")
        sys.exit(1)

    ticker = sys.argv[1]
    max_eps = int(sys.argv[2]) if len(sys.argv) > 2 else 50
    lang = sys.argv[3] if len(sys.argv) > 3 else 'auto'

    process_podcast_episodes(ticker, max_episodes=max_eps, language=lang)
