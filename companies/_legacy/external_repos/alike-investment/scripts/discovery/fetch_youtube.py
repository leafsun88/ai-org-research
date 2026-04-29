"""
Phase 3: YouTube采集
- yt-dlp搜索视频
- yt-dlp下载字幕 (auto-generated or manual)
- 清洗VTT → 纯文本
- 保存到 {TICKER}/sources/youtube/
"""

import os
import sys
import re
import os
import json
import subprocess
import tempfile
import shutil
from pathlib import Path
from datetime import datetime

DB_DIR = Path(os.environ.get('ALIKE_DB_DIR', str(Path(__file__).parent.parent)))
YTDLP_CANDIDATES = [
    os.environ.get("YT_DLP_PATH"),
    shutil.which("yt-dlp"),
    os.path.expanduser("~/Library/Python/3.9/bin/yt-dlp"),
    os.path.expanduser("~/Library/Python/3.10/bin/yt-dlp"),
    os.path.expanduser("~/Library/Python/3.11/bin/yt-dlp"),
    os.path.expanduser("~/Library/Python/3.12/bin/yt-dlp"),
    os.path.expanduser("~/bin/yt-dlp"),
    "/opt/homebrew/bin/yt-dlp",
    "/usr/local/bin/yt-dlp",
]


def resolve_ytdlp():
    """Resolve yt-dlp from PATH or common install locations."""
    for candidate in YTDLP_CANDIDATES:
        if candidate and Path(candidate).exists():
            return candidate
    return None


def clean_vtt(vtt_text):
    """Convert VTT subtitle to clean text, removing duplicates and timestamps."""
    lines = vtt_text.split('\n')
    text_lines = []
    seen = set()

    for line in lines:
        # Skip WEBVTT header, timestamps, empty lines
        if line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:'):
            continue
        if '-->' in line:
            continue
        if not line.strip():
            continue
        if line.strip().startswith('align:') or line.strip().startswith('position:'):
            continue

        # Remove VTT tags like <c>, </c>, <00:00:00.000>
        clean = re.sub(r'<[^>]+>', '', line).strip()
        if not clean:
            continue

        # Deduplicate (VTT often has duplicate lines)
        if clean not in seen:
            seen.add(clean)
            text_lines.append(clean)

    return ' '.join(text_lines)


def search_youtube(query, max_results=10):
    """Search YouTube using yt-dlp, return video metadata."""
    ytdlp = resolve_ytdlp()
    if not ytdlp:
        print("  搜索跳过: yt-dlp 未安装")
        return []

    cmd = [
        ytdlp,
        f'ytsearch{max_results}:{query}',
        '--flat-playlist',
        '--print', '%(id)s\t%(title)s\t%(channel)s\t%(upload_date)s\t%(duration)s',
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        videos = []
        for line in result.stdout.strip().split('\n'):
            if not line.strip():
                continue
            parts = line.split('\t')
            if len(parts) >= 5:
                videos.append({
                    'id': parts[0],
                    'title': parts[1],
                    'channel': parts[2],
                    'date': parts[3] if parts[3] != 'NA' else '',
                    'duration': float(parts[4]) if parts[4] != 'NA' else 0,
                })
        return videos
    except Exception as e:
        print(f"  搜索失败: {e}")
        return []


def download_subtitle(video_id, lang='en'):
    """Download subtitle for a video using yt-dlp. Returns clean text or None."""
    ytdlp = resolve_ytdlp()
    if not ytdlp:
        return None

    with tempfile.TemporaryDirectory() as tmpdir:
        out_template = os.path.join(tmpdir, f'sub_{video_id}')

        # Try auto-generated subtitles first, then manual
        for sub_flag in ['--write-auto-sub', '--write-sub']:
            cmd = [
                ytdlp,
                sub_flag,
                '--skip-download',
                '--sub-lang', lang,
                '-o', out_template,
                f'https://www.youtube.com/watch?v={video_id}',
            ]
            try:
                subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            except subprocess.TimeoutExpired:
                continue

            # Check for downloaded file
            for f in Path(tmpdir).glob(f'sub_{video_id}*.vtt'):
                vtt_text = f.read_text(encoding='utf-8')
                clean_text = clean_vtt(vtt_text)
                if len(clean_text) > 100:  # Minimum viable transcript
                    return clean_text

            # Also try .srt
            for f in Path(tmpdir).glob(f'sub_{video_id}*.srt'):
                srt_text = f.read_text(encoding='utf-8')
                # Simple SRT cleaning
                clean = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n', '', srt_text)
                clean = re.sub(r'<[^>]+>', '', clean)
                clean = ' '.join(clean.split())
                if len(clean) > 100:
                    return clean

        # Try Chinese subtitles if English failed
        if lang == 'en':
            return download_subtitle(video_id, lang='zh-Hans')

    return None


def save_youtube_transcript(ticker, video_id, title, channel, date_str, transcript, language='en'):
    """Save a YouTube transcript as markdown."""
    sources_dir = DB_DIR / ticker / "sources" / "youtube"
    sources_dir.mkdir(parents=True, exist_ok=True)

    safe_title = re.sub(r'[^\w\s-]', '', title)[:50].strip().replace(' ', '-')
    if not date_str or date_str == 'NA':
        date_str = datetime.now().strftime('%Y-%m-%d')
    elif len(date_str) == 8:  # YYYYMMDD format from yt-dlp
        date_str = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"

    filename = f"{date_str}_{safe_title}.md"

    content = f"""---
ticker: {ticker}
type: youtube
title: "{title}"
channel: "{channel}"
date: {date_str}
url: https://www.youtube.com/watch?v={video_id}
transcript_method: yt-dlp_subtitle
language: {language}
chars: {len(transcript)}
---

# {title}

## 视频信息
- **频道**: {channel}
- **日期**: {date_str}
- **链接**: https://www.youtube.com/watch?v={video_id}

## 转录全文

{transcript}
"""

    filepath = sources_dir / filename
    filepath.write_text(content, encoding="utf-8")
    return filepath


def fetch_youtube_for_company(ticker, company_name, max_videos=15):
    """Full pipeline: search → download subtitles → save."""
    print(f"[YouTube] Researching {ticker} ({company_name})...")
    ytdlp = resolve_ytdlp()
    if not ytdlp:
        print("  ⚠️  yt-dlp 未安装，跳过 YouTube 采集。可运行: pip3 install --user yt-dlp")
        return []

    # Search queries
    queries = [
        f"{company_name} earnings analysis",
        f"{company_name} CEO interview",
        f"{company_name} stock analysis 2025",
        f"{ticker} stock deep dive",
    ]

    all_videos = []
    seen_ids = set()

    for query in queries:
        print(f"  搜索: {query}")
        videos = search_youtube(query, max_results=5)
        for v in videos:
            if v['id'] not in seen_ids:
                seen_ids.add(v['id'])
                all_videos.append(v)
        print(f"    找到 {len(videos)} 个视频")

    # Sort by duration (prefer longer, more substantive videos) but cap at max
    all_videos.sort(key=lambda v: v.get('duration', 0), reverse=True)
    all_videos = all_videos[:max_videos]

    print(f"\n  共 {len(all_videos)} 个独立视频, 开始提取字幕...")

    results = []
    for i, video in enumerate(all_videos):
        vid = video['id']
        title = video.get('title', f'Video_{vid}')
        channel = video.get('channel', 'Unknown')
        date_str = video.get('date', '')

        print(f"  [{i+1}/{len(all_videos)}] {title[:60]}...")

        transcript = download_subtitle(vid)
        if transcript:
            filepath = save_youtube_transcript(
                ticker, vid, title, channel, date_str, transcript
            )
            print(f"    ✓ {len(transcript):,} chars → {filepath.name}")
            results.append({
                'id': vid, 'title': title, 'chars': len(transcript),
                'file': str(filepath),
            })
        else:
            print(f"    ✗ 无字幕")
            results.append({'id': vid, 'title': title, 'error': 'no subtitle'})

    success = sum(1 for r in results if r.get('chars'))
    total_chars = sum(r.get('chars', 0) for r in results)
    print(f"\n  完成: {success}/{len(all_videos)} 成功, 共 {total_chars:,} 字符")

    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_youtube.py TICKER [COMPANY_NAME]")
        sys.exit(1)

    ticker = sys.argv[1]
    company_name = sys.argv[2] if len(sys.argv) > 2 else ticker
    fetch_youtube_for_company(ticker, company_name)
