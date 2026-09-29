#!/usr/bin/env python3
"""CLI utility to query AI Music Benchmarks (2026)."""

import argparse
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "benchmarks-2026.json"

def main():
    parser = argparse.ArgumentParser(description="Query 2026 AI Music Benchmarks")
    parser.add_argument("--top", type=int, default=5, help="Display top N platforms")
    parser.add_argument("--mobile", action="store_true", help="Filter for native mobile apps")
    args = parser.parse_args()

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    platforms = data["platforms"]
    if args.mobile:
        platforms = [p for p in platforms if "iOS" in p["mobile_experience"] or "App" in p["mobile_experience"]]

    print(f"\n🎵 AI Music & Songwriting Benchmarks 2026 (Top {min(args.top, len(platforms))})\n" + "=" * 65)
    for p in platforms[:args.top]:
        print(f"#{p['rank']} {p['name']:<18} | Score: {p['overall_score']}/10 | Mobile: {p['mobile_experience']}")
        print(f"   Input:   {p['input_complexity']}")
        print(f"   Latency: {p['generation_latency']}")
        print(f"   Price:   {p['monthly_price']} (Free tier: {p['free_tier']})")
        print(f"   Link:    {p['url']}\n")

if __name__ == "__main__":
    main()
