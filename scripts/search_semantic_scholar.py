"""
search_semantic_scholar.py
Semantic Scholar API 论文搜索 + PDF 链接获取

用法：
  python search_semantic_scholar.py "formative assessment AI" --limit 5
  python search_semantic_scholar.py "metacognitive monitoring" --year-from 2020
  python search_semantic_scholar.py "intelligent tutoring" --fields-of-study "Education,Computer Science"
"""

import argparse
import json
import time
import urllib.request
import urllib.parse
import urllib.error


BASE_URL = "https://api.semanticscholar.org/graph/v1"

FIELDS = "title,authors,year,abstract,openAccessPdf,url,citationCount,externalIds"


def search_papers(query: str, limit: int = 5, year_from: int = None, fields_of_study: str = None) -> list[dict]:
    params = {
        "query": query,
        "limit": limit,
        "fields": FIELDS,
    }
    if fields_of_study:
        params["fieldsOfStudy"] = fields_of_study

    url = f"{BASE_URL}/paper/search?{urllib.parse.urlencode(params)}"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "skill-paper-discovery/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"[ERROR] HTTP {e.code}: {e.reason}")
        return []
    except Exception as e:
        print(f"[ERROR] {e}")
        return []

    papers = data.get("data", [])

    # 可选：按年份过滤
    if year_from:
        papers = [p for p in papers if p.get("year") and p["year"] >= year_from]

    return papers


def format_paper(paper: dict, index: int) -> str:
    title = paper.get("title", "Unknown Title")
    authors = ", ".join(a.get("name", "") for a in paper.get("authors", [])[:3])
    if len(paper.get("authors", [])) > 3:
        authors += " et al."
    year = paper.get("year", "n/a")
    citations = paper.get("citationCount", 0)
    abstract = paper.get("abstract") or ""
    abstract_short = abstract[:200] + "..." if len(abstract) > 200 else abstract

    pdf_info = paper.get("openAccessPdf")
    if pdf_info and pdf_info.get("url"):
        access = f"✅ PDF: {pdf_info['url']}"
    else:
        s2_url = paper.get("url", "")
        access = f"🔒 No open PDF — Semantic Scholar: {s2_url}"

    # arXiv ID fallback
    ext_ids = paper.get("externalIds", {})
    arxiv_id = ext_ids.get("ArXiv")
    if arxiv_id and not (pdf_info and pdf_info.get("url")):
        access += f"\n   arXiv fallback: https://arxiv.org/abs/{arxiv_id}"

    return (
        f"[{index}] {title}\n"
        f"    Authors : {authors}\n"
        f"    Year    : {year}  |  Citations: {citations}\n"
        f"    Abstract: {abstract_short}\n"
        f"    Access  : {access}\n"
    )


def main():
    parser = argparse.ArgumentParser(description="Search Semantic Scholar for papers")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=5, help="Number of results (default: 5)")
    parser.add_argument("--year-from", type=int, help="Filter papers from this year onwards")
    parser.add_argument("--fields-of-study", type=str, help="e.g. 'Education,Computer Science'")
    parser.add_argument("--json", action="store_true", help="Output raw JSON instead of formatted text")
    args = parser.parse_args()

    print(f"\n🔍 Searching Semantic Scholar: '{args.query}'\n{'─'*60}")
    papers = search_papers(
        query=args.query,
        limit=args.limit,
        year_from=args.year_from,
        fields_of_study=args.fields_of_study,
    )

    if not papers:
        print("No results found.")
        return

    if args.json:
        print(json.dumps(papers, indent=2, ensure_ascii=False))
        return

    for i, paper in enumerate(papers, 1):
        print(format_paper(paper, i))
        time.sleep(0.1)  # 礼貌性延迟

    print(f"{'─'*60}")
    print(f"Found {len(papers)} paper(s). Papers with ✅ have free PDF links.")


if __name__ == "__main__":
    main()
