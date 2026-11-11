#!/usr/bin/env python3
"""Fetch YouTube transcripts into resources/videos/NN.md for concept indexing.

Usage:
    pip install yt-dlp
    python3 tools/fetch_videos.py URL [URL ...] [--out resources/videos] [--lang en] [--first 1]

Each URL may be a video or a playlist. Videos are numbered in order starting
at --first (01, 02, ...). Each output file has the video's title, link,
chapters (if the uploader added any), an empty concept-index table for the
agent to fill in, and the timestamped transcript. Existing files are skipped
unless --force is given, so the script is safe to re-run.
"""
import argparse
import html
import os
import re
import sys
import tempfile

try:
    import yt_dlp
except ImportError:
    sys.exit("yt-dlp is not installed. Run: pip install yt-dlp")


def fmt(sec):
    sec = int(sec)
    h, m, s = sec // 3600, sec % 3600 // 60, sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def parse_ts(ts):
    parts = ts.replace(",", ".").split(":")
    parts = [float(p) for p in parts]
    while len(parts) < 3:
        parts.insert(0, 0.0)
    return parts[0] * 3600 + parts[1] * 60 + parts[2]


def parse_vtt(text):
    """Return [(start_sec, line)], de-duplicating rolling auto-caption lines."""
    out, last = [], None
    for block in re.split(r"\n\s*\n", text):
        lines = block.strip().splitlines()
        idx = next((i for i, l in enumerate(lines) if "-->" in l), None)
        if idx is None:
            continue
        start = parse_ts(lines[idx].split("-->")[0].strip())
        for raw in lines[idx + 1:]:
            line = html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()
            line = re.sub(r"^[A-Z][A-Z .'-]{1,30}:\s+", "", line)  # "SPEAKER: "
            if not line or line == last:
                continue
            out.append((start, line))
            last = line
    # Merge very short consecutive lines into ~one line per cue start.
    merged = []
    for start, line in out:
        if merged and int(merged[-1][0]) == int(start):
            merged[-1] = (merged[-1][0], merged[-1][1] + " " + line)
        else:
            merged.append((start, line))
    return merged


def expand(urls):
    """Yield video URLs, expanding playlists in order."""
    opts = {"quiet": True, "extract_flat": "in_playlist", "skip_download": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        for url in urls:
            info = ydl.extract_info(url, download=False)
            if info.get("_type") == "playlist":
                for e in info.get("entries") or []:
                    if e and e.get("id"):
                        yield f"https://www.youtube.com/watch?v={e['id']}"
            else:
                yield url


def fetch(url, lang, tmp):
    opts = {
        "quiet": True, "no_warnings": True, "noprogress": True, "skip_download": True,
        "writesubtitles": True, "writeautomaticsub": True,
        "subtitleslangs": [lang, f"{lang}-orig", f"{lang}.*"],
        "subtitlesformat": "vtt", "outtmpl": os.path.join(tmp, "%(id)s.%(ext)s"),
    }
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url, download=True)
    vid = info["id"]
    manual = bool(info.get("subtitles"))
    vtts = sorted(f for f in os.listdir(tmp) if f.startswith(vid) and f.endswith(".vtt"))
    text = open(os.path.join(tmp, vtts[0]), encoding="utf-8").read() if vtts else ""
    return info, parse_vtt(text), manual


def render(n, info, cues, manual):
    vid, title = info["id"], info.get("title", "")
    lines = [f"# {n:02d}: {title}", "",
             f"Video: https://youtu.be/{vid}  ",
             f"Channel: {info.get('channel') or info.get('uploader') or '?'}  ",
             f"Length: {fmt(info.get('duration') or 0)}  ",
             f"Transcript: {'uploaded captions' if manual else 'auto-generated captions' if cues else 'none available'}",
             ""]
    chapters = info.get("chapters") or []
    if chapters:
        lines += ["## Chapters (from the uploader)", "", "| Start | End | Chapter |", "|---|---|---|"]
        lines += [f"| {fmt(c['start_time'])} | {fmt(c['end_time'])} | {c.get('title', '')} |" for c in chapters]
        lines.append("")
    lines += [
        "## Concept index", "",
        "<!-- Agent: fill one row per concept segment, using times from the",
        "transcript below (never guessed). Lesson = syllabus lesson number(s),",
        "comma-separated, or — for off-topic segments. Then run",
        "tools/build_clips.py to regenerate resources/clips.md. -->", "",
        "| Start | End | Lesson | Concept |", "|---|---|---|---|", "",
        "## Transcript", "",
    ]
    if not cues:
        lines.append("_No transcript available. Index from chapters, or link the whole video._")
    for start, text in cues:
        lines.append(f"[{fmt(start)}](https://youtu.be/{vid}?t={int(start)}) {text}  ")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--out", default="resources/videos")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--first", type=int, default=1, help="number for the first video")
    ap.add_argument("--force", action="store_true", help="overwrite existing files")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    failed = []
    for n, url in enumerate(expand(a.urls), start=a.first):
        path = os.path.join(a.out, f"{n:02d}.md")
        if os.path.exists(path) and not a.force:
            print(f"skip   {path} (exists)")
            continue
        try:
            with tempfile.TemporaryDirectory() as tmp:
                info, cues, manual = fetch(url, a.lang, tmp)
        except Exception as e:  # keep going; report at the end
            failed.append((url, str(e).splitlines()[0]))
            print(f"FAIL   {url}: {failed[-1][1]}")
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(n, info, cues, manual))
        kind = "captions" if manual else "auto-captions" if cues else "NO transcript"
        print(f"wrote  {path}  {info.get('title', '')[:60]}  [{kind}, {len(info.get('chapters') or [])} chapters]")
    if failed:
        print(f"\n{len(failed)} failed. If YouTube asks to 'sign in to confirm you're not a bot',"
              " run this script on your own computer and commit the output.")
        sys.exit(1)


if __name__ == "__main__":
    main()
