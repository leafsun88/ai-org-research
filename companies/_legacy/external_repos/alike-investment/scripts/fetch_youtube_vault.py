#!/usr/bin/env python3
"""Fetch YouTube transcripts into vault structure.
Uses yt-dlp for search, youtube-transcript-api for transcripts."""

import sys
import os
import re
import json
import subprocess
import shutil
from pathlib import Path
from datetime import datetime

# Find yt-dlp (still needed for search)
YTDLP = None
for p in [
    os.path.expanduser("~/Library/Python/3.9/bin/yt-dlp"),
    os.path.expanduser("~/bin/yt-dlp"),
    "/usr/local/bin/yt-dlp",
    "/opt/homebrew/bin/yt-dlp",
]:
    if os.path.isfile(p):
        YTDLP = p
        break
if not YTDLP:
    YTDLP = shutil.which("yt-dlp")
if not YTDLP:
    print("ERROR: yt-dlp not found. Install with: pip3 install yt-dlp")
    sys.exit(1)

# youtube-transcript-api for actual transcripts
try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    print("ERROR: youtube-transcript-api not found. Install with: pip3 install youtube-transcript-api")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).parent.parent
VAULT_DIR = PROJECT_ROOT / "vault"
INDEX_PATH = VAULT_DIR / "_index.json"


def load_slug(ticker):
    with open(INDEX_PATH) as f:
        index = json.load(f)
    return index.get("ticker_map", {}).get(ticker)


def search_videos(query, max_results=5):
    """Use yt-dlp for search (no PO token needed for search)."""
    cmd = [YTDLP, f'ytsearch{max_results}:{query}', '--flat-playlist',
           '--print', '%(id)s\t%(title)s\t%(upload_date)s\t%(channel)s\t%(duration)s']
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        videos = []
        for line in result.stdout.strip().split('\n'):
            if not line.strip():
                continue
            parts = line.split('\t')
            if len(parts) >= 2:
                videos.append({
                    'id': parts[0], 'title': parts[1],
                    'date': parts[2] if len(parts) > 2 else '',
                    'channel': parts[3] if len(parts) > 3 else '',
                    'duration': parts[4] if len(parts) > 4 else '',
                })
        return videos
    except Exception as e:
        print(f"    Search failed: {e}")
        return []


def get_transcript(video_id):
    """Use youtube-transcript-api to get transcript (no PO token needed)."""
    try:
        ytt_api = YouTubeTranscriptApi()
        # Try English first, then any available language
        for lang in [['en'], ['en-US'], ['zh-Hans', 'zh-CN', 'zh'], None]:
            try:
                if lang:
                    transcript = ytt_api.fetch(video_id, languages=lang)
                else:
                    # Get whatever is available
                    transcript = ytt_api.fetch(video_id)
                text = ' '.join([entry.text for entry in transcript.snippets])
                if len(text) > 100:
                    return text
            except Exception:
                continue
    except Exception as e:
        pass
    return None


def safe_filename(title, max_len=60):
    clean = re.sub(r'[^\w\s-]', '', title)
    clean = re.sub(r'\s+', '-', clean.strip())
    return clean[:max_len]


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 fetch_youtube_vault.py TICKER CompanyName [max_videos]")
        sys.exit(1)

    ticker = sys.argv[1]
    company = sys.argv[2]
    max_videos = int(sys.argv[3]) if len(sys.argv) > 3 else 20

    slug = load_slug(ticker)
    if not slug:
        print(f"ERROR: {ticker} not in _index.json")
        sys.exit(1)

    out_dir = VAULT_DIR / "companies" / slug / "discovery" / "sources" / "youtube"
    out_dir.mkdir(parents=True, exist_ok=True)

    queries = [
        f"{company} earnings analysis",
        f"{company} CEO interview",
        f"{company} stock analysis 2025",
        f"{ticker} stock deep dive",
    ]

    all_videos = {}
    for q in queries:
        print(f"  Searching: {q}")
        results = search_videos(q, max_results=5)
        for v in results:
            if v['id'] not in all_videos:
                all_videos[v['id']] = v
        print(f"    Found {len(results)} videos")

    videos = list(all_videos.values())[:max_videos]
    print(f"\n  Total unique videos: {len(videos)}, downloading transcripts...")

    success = 0
    for i, v in enumerate(videos):
        print(f"  [{i+1}/{len(videos)}] {v['title'][:50]}...", end=" ", flush=True)
        text = get_transcript(v['id'])
        if text:
            date_str = v.get('date', '')
            if len(date_str) == 8:
                date_fmt = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
            else:
                date_fmt = datetime.now().strftime('%Y-%m-%d')

            fname = f"{date_fmt}_{safe_filename(v['title'])}.md"
            filepath = out_dir / fname

            with open(filepath, 'w') as f:
                f.write("---\n")
                f.write(f"type: youtube_transcript\n")
                f.write(f"ticker: {ticker}\n")
                f.write(f"title: \"{v['title']}\"\n")
                f.write(f"channel: \"{v.get('channel', '')}\"\n")
                f.write(f"date: {date_fmt}\n")
                f.write(f"video_id: {v['id']}\n")
                f.write(f"url: https://www.youtube.com/watch?v={v['id']}\n")
                f.write(f"transcript_method: youtube-transcript-api\n")
                f.write(f"credibility: S2\n")
                f.write(f"evidence: E2\n")
                f.write("---\n\n")
                f.write(f"# {v['title']}\n\n")
                f.write(f"**Channel**: {v.get('channel', 'N/A')}  \n")
                f.write(f"**Date**: {date_fmt}  \n")
                f.write(f"**URL**: https://www.youtube.com/watch?v={v['id']}\n\n")
                f.write("## Transcript\n\n")
                f.write(text + "\n")

            success += 1
            print(f"✅ ({len(text)} chars)")
        else:
            print("❌ no transcript")

    print(f"\n  Done: {success}/{len(videos)} transcripts saved to vault/companies/{slug}/discovery/sources/youtube/")


if __name__ == "__main__":
    main()
