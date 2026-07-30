#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UI/UX Pro Max Search - BM25 search engine for UI/UX style guides.

Usage:
    python3 search.py "<query>" [--domain <domain>] [--stack <stack>]
    python3 search.py "<query>" --design-system [-p "Project Name"]
    python3 search.py "<query>" --design-system --persist [-p "Project Name"] [--page "homepage"]
"""

import argparse
import json

from core import AVAILABLE_STACKS, CSV_CONFIG, MAX_RESULTS, search, search_stack
from design_system import (
    DesignSystemGenerator,
    format_ascii_box,
    format_markdown,
    persist_design_system,
)


def format_output(result):
    """Format results for Claude consumption (token-optimized)."""
    if "error" in result:
        return f"Error: {result['error']}"

    output = []
    if result.get("stack"):
        output.append("## UI Pro Max Stack Guidelines")
        output.append(f"**Stack:** {result['stack']} | **Query:** {result['query']}")
    else:
        output.append("## UI Pro Max Search Results")
        output.append(f"**Domain:** {result['domain']} | **Query:** {result['query']}")
    output.append(f"**Source:** {result['file']} | **Found:** {result['count']} results\n")

    for index, row in enumerate(result["results"], 1):
        output.append(f"### Result {index}")
        for key, value in row.items():
            value_str = str(value)
            if len(value_str) > 300:
                value_str = value_str[:300] + "..."
            output.append(f"- **{key}:** {value_str}")
        output.append("")

    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(description="UI Pro Max Search")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--domain", "-d", choices=list(CSV_CONFIG.keys()), help="Search domain")
    parser.add_argument(
        "--stack",
        "-s",
        choices=AVAILABLE_STACKS,
        help=f"Stack-specific search ({', '.join(AVAILABLE_STACKS)})",
    )
    parser.add_argument("--max-results", "-n", type=int, default=MAX_RESULTS, help="Max results (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--design-system", "-ds", action="store_true", help="Generate a complete design system recommendation")
    parser.add_argument("--project-name", "-p", type=str, default=None, help="Project name for design system output")
    parser.add_argument("--format", "-f", choices=["ascii", "markdown"], default="ascii", help="Design system output format")
    parser.add_argument("--persist", action="store_true", help="Save into design-system/<project>/")
    parser.add_argument("--page", type=str, default=None, help="Create a page-specific override; requires --persist")
    parser.add_argument("--output-dir", "-o", type=str, default=None, help="Persistence root (default: current directory)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing generated files; requires --persist")

    args = parser.parse_args()

    if args.page and not args.persist:
        parser.error("--page requires --persist")
    if args.force and not args.persist:
        parser.error("--force requires --persist")
    if args.persist and not args.design_system:
        parser.error("--persist requires --design-system")

    if args.design_system:
        design_system = DesignSystemGenerator().generate(args.query, args.project_name)
        formatter = format_markdown if args.format == "markdown" else format_ascii_box
        print(formatter(design_system))

        if args.persist:
            result = persist_design_system(
                design_system,
                page=args.page,
                output_dir=args.output_dir,
                page_query=args.query,
                overwrite=args.force,
            )
            print("\nDesign system persisted:")
            print(f"  Master: {result['master_file']}")
            if result["page_file"]:
                print(f"  Page override: {result['page_file']}")
            print("\nUsage: check the page override first, then fall back to MASTER.md.")
        return

    if args.stack:
        result = search_stack(args.query, args.stack, args.max_results)
    else:
        result = search(args.query, args.domain, args.max_results)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_output(result))


if __name__ == "__main__":
    main()
