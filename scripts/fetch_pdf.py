"""
fetch_pdf.py
拿到 PDF 链接后下载到本地

用法：
  python fetch_pdf.py "https://arxiv.org/pdf/2301.00001"
  python fetch_pdf.py "https://..." --output ./papers/
  python fetch_pdf.py --from-json results.json --output ./papers/   # 批量下载

输入 JSON 格式（来自 search_semantic_scholar.py --json 或手动整理）：
  [
    {"title": "Paper Title", "pdf_url": "https://..."},
    ...
  ]
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; skill-paper-discovery/1.0; "
        "+https://github.com/edu-ai-builders)"
    )
}

MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds


def sanitize_filename(name: str, max_len: int = 80) -> str:
    """把标题转成合法文件名"""
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    name = re.sub(r"\s+", "_", name.strip())
    return name[:max_len]


def download_pdf(url: str, output_dir: Path, filename: str = None) -> Path | None:
    """下载单个 PDF，返回保存路径，失败返回 None"""
    output_dir.mkdir(parents=True, exist_ok=True)

    if not filename:
        # 从 URL 推断文件名
        url_path = url.rstrip("/").split("/")[-1]
        filename = url_path if url_path.endswith(".pdf") else url_path + ".pdf"

    if not filename.endswith(".pdf"):
        filename += ".pdf"

    output_path = output_dir / filename

    if output_path.exists():
        print(f"  ⏭  Already exists: {output_path}")
        return output_path

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                content_type = resp.headers.get("Content-Type", "")
                if "pdf" not in content_type and attempt == MAX_RETRIES:
                    print(f"  ⚠  Warning: Content-Type is '{content_type}', may not be a PDF")

                data = resp.read()
                output_path.write_bytes(data)
                size_kb = len(data) // 1024
                print(f"  ✅ Downloaded ({size_kb} KB): {output_path}")
                return output_path

        except urllib.error.HTTPError as e:
            if e.code == 403:
                print(f"  🔒 Access denied (403) — this paper may be behind a paywall: {url}")
                return None
            elif e.code == 404:
                print(f"  ❌ Not found (404): {url}")
                return None
            else:
                print(f"  ⚠  HTTP {e.code} on attempt {attempt}/{MAX_RETRIES}")
                if attempt < MAX_RETRIES:
                    time.sleep(RETRY_DELAY)

        except Exception as e:
            print(f"  ⚠  Error on attempt {attempt}/{MAX_RETRIES}: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)

    print(f"  ❌ Failed after {MAX_RETRIES} attempts: {url}")
    return None


def extract_pdf_url(paper: dict) -> str | None:
    """从 Semantic Scholar JSON 或手动 dict 中提取 PDF URL"""
    # Semantic Scholar 格式
    if "openAccessPdf" in paper:
        pdf_info = paper["openAccessPdf"]
        if pdf_info and pdf_info.get("url"):
            return pdf_info["url"]

    # 简化格式
    if "pdf_url" in paper:
        return paper["pdf_url"]

    # arXiv ID fallback
    ext_ids = paper.get("externalIds", {})
    arxiv_id = ext_ids.get("ArXiv")
    if arxiv_id:
        return f"https://arxiv.org/pdf/{arxiv_id}"

    return None


def main():
    parser = argparse.ArgumentParser(description="Download PDF(s) from URL or JSON list")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("url", nargs="?", help="Single PDF URL to download")
    group.add_argument("--from-json", type=str, help="Path to JSON file with paper list")

    parser.add_argument(
        "--output", type=str, default="./papers", help="Output directory (default: ./papers)"
    )
    parser.add_argument("--filename", type=str, help="Custom filename (single URL mode only)")
    args = parser.parse_args()

    output_dir = Path(args.output)

    # 单个 URL 模式
    if args.url:
        print(f"\n📥 Downloading PDF...")
        filename = args.filename or None
        result = download_pdf(args.url, output_dir, filename)
        if result:
            print(f"\nSaved to: {result.resolve()}")
        else:
            sys.exit(1)
        return

    # 批量 JSON 模式
    json_path = Path(args.from_json)
    if not json_path.exists():
        print(f"[ERROR] File not found: {json_path}")
        sys.exit(1)

    with open(json_path, encoding="utf-8") as f:
        papers = json.load(f)

    print(f"\n📥 Batch downloading {len(papers)} paper(s) to '{output_dir}'...\n")

    success, skipped, failed = 0, 0, 0

    for i, paper in enumerate(papers, 1):
        title = paper.get("title", f"paper_{i}")
        pdf_url = extract_pdf_url(paper)

        print(f"[{i}/{len(papers)}] {title[:70]}")

        if not pdf_url:
            print(f"  ⚠  No open-access PDF available — skipping")
            skipped += 1
            continue

        filename = sanitize_filename(title) + ".pdf"
        result = download_pdf(pdf_url, output_dir, filename)

        if result:
            success += 1
        else:
            failed += 1

        time.sleep(1)  # 礼貌性延迟，避免触发限流

    print(f"\n{'─'*60}")
    print(f"Results: ✅ {success} downloaded  ⏭  {skipped} skipped (no PDF)  ❌ {failed} failed")
    print(f"Output directory: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
