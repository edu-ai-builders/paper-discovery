"""
search_arxiv.py
arXiv 论文搜索 + PDF 直链获取

用法：
  python search_arxiv.py "AI tutoring system education"
  python search_arxiv.py "formative feedback learning" --max-results 5 --category cs.AI
  python search_arxiv.py "metacognition" --sort-by relevance

依赖：
  pip install arxiv
"""

import argparse
import sys

try:
    import arxiv
except ImportError:
    print("[ERROR] Missing dependency. Run: pip install arxiv")
    sys.exit(1)


CATEGORY_HINTS = {
    "cs.AI": "Artificial Intelligence",
    "cs.HC": "Human-Computer Interaction",
    "cs.CY": "Computers and Society",
    "cs.LG": "Machine Learning",
    "stat.ML": "Machine Learning (Stats)",
}

SORT_OPTIONS = {
    "relevance": arxiv.SortCriterion.Relevance,
    "latest": arxiv.SortCriterion.SubmittedDate,
    "citations": arxiv.SortCriterion.Relevance,  # arXiv doesn't have citation sort
}


def search_arxiv(
    query: str,
    max_results: int = 5,
    category: str = None,
    sort_by: str = "relevance",
) -> list:
    if category:
        full_query = f"({query}) AND cat:{category}"
    else:
        full_query = query

    sort_criterion = SORT_OPTIONS.get(sort_by, arxiv.SortCriterion.Relevance)

    client = arxiv.Client()
    search = arxiv.Search(
        query=full_query,
        max_results=max_results,
        sort_by=sort_criterion,
        sort_order=arxiv.SortOrder.Descending,
    )

    results = []
    for result in client.results(search):
        results.append(result)

    return results


def format_result(result, index: int) -> str:
    authors = ", ".join(str(a) for a in result.authors[:3])
    if len(result.authors) > 3:
        authors += " et al."

    year = result.published.year if result.published else "n/a"
    categories = ", ".join(result.categories[:3])

    abstract = result.summary or ""
    abstract_short = abstract[:200] + "..." if len(abstract) > 200 else abstract

    pdf_url = result.pdf_url or f"https://arxiv.org/pdf/{result.get_short_id()}"
    abs_url = result.entry_id

    return (
        f"[{index}] {result.title}\n"
        f"    Authors   : {authors}\n"
        f"    Year      : {year}  |  Categories: {categories}\n"
        f"    Abstract  : {abstract_short}\n"
        f"    ✅ PDF    : {pdf_url}\n"
        f"    Abstract  : {abs_url}\n"
    )


def main():
    parser = argparse.ArgumentParser(description="Search arXiv for papers (always free PDF)")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--max-results", type=int, default=5, help="Number of results (default: 5)")
    parser.add_argument(
        "--category",
        type=str,
        help=f"arXiv category filter. Options: {', '.join(CATEGORY_HINTS.keys())}",
    )
    parser.add_argument(
        "--sort-by",
        choices=["relevance", "latest"],
        default="relevance",
        help="Sort order (default: relevance)",
    )
    args = parser.parse_args()

    print(f"\n🔍 Searching arXiv: '{args.query}'")
    if args.category:
        print(f"   Category: {args.category} ({CATEGORY_HINTS.get(args.category, 'custom')})")
    print("─" * 60)

    results = search_arxiv(
        query=args.query,
        max_results=args.max_results,
        category=args.category,
        sort_by=args.sort_by,
    )

    if not results:
        print("No results found.")
        return

    for i, result in enumerate(results, 1):
        print(format_result(result, i))

    print("─" * 60)
    print(f"Found {len(results)} paper(s). All arXiv papers have free PDF links (✅).")
    print("\nNote: arXiv is best for CS/AI papers. For education empirical research,")
    print("      use search_semantic_scholar.py for broader coverage.")


if __name__ == "__main__":
    main()
