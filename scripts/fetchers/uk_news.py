#!/usr/bin/env python3
"""UK health news fetcher.

Fetches health news from UK sources including NHS, BBC Health, and Google News RSS.
"""

import json
import re
import urllib.parse
from datetime import datetime
from pathlib import Path
from typing import Optional
import xml.etree.ElementTree as ET

import requests

# UK health news sources
UK_NEWS_SOURCES = [
    "bbc.co.uk",
    "bbc.com",
    "nhs.uk",
    "theguardian.com",
    "telegraph.co.uk",
    "independent.co.uk",
    "dailymail.co.uk",
    "express.co.uk",
    "mirror.co.uk",
]

# Health-related keywords
HEALTH_KEYWORDS_EN = [
    "health", "medicine", "drug", "treatment", "clinical trial",
    "pharmaceutical", "therapy", "patient", "disease", "hospital",
    "cancer", "diabetes", "heart disease", "research", "MHRA",
    "NHS", "medical", "doctor", "prescription", "NICE",
]


def fetch_google_news_rss(query: str, region: str = "GB") -> list[dict]:
    """Fetch news from Google News RSS.

    Args:
        query: Search query
        region: Country code (GB for United Kingdom)

    Returns:
        List of news items
    """
    encoded_query = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-GB&gl=GB&ceid=GB:en"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        items = []

        for item in root.findall(".//item"):
            title = item.find("title")
            link = item.find("link")
            pub_date = item.find("pubDate")
            source = item.find("source")

            if title is not None and link is not None:
                items.append({
                    "title": title.text,
                    "link": link.text,
                    "pub_date": pub_date.text if pub_date is not None else None,
                    "source": source.text if source is not None else "Unknown",
                })

        return items

    except Exception as e:
        print(f"Error fetching Google News: {e}")
        return []


def fetch_bbc_health_rss() -> list[dict]:
    """Fetch news from BBC Health RSS feed."""
    url = "https://feeds.bbci.co.uk/news/health/rss.xml"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        root = ET.fromstring(response.content)
        items = []

        for item in root.findall(".//item"):
            title = item.find("title")
            link = item.find("link")
            pub_date = item.find("pubDate")

            if title is not None and link is not None:
                items.append({
                    "title": title.text,
                    "link": link.text,
                    "pub_date": pub_date.text if pub_date is not None else None,
                    "source": "BBC Health",
                })

        return items

    except Exception as e:
        print(f"Error fetching BBC Health RSS: {e}")
        return []


def filter_health_news(items: list[dict]) -> list[dict]:
    """Filter news items to health-related only.

    Args:
        items: List of news items

    Returns:
        Filtered list of health news items
    """
    filtered = []

    for item in items:
        title_lower = item.get("title", "").lower()

        # Check for health keywords
        is_health = any(kw.lower() in title_lower for kw in HEALTH_KEYWORDS_EN)

        # Check for UK sources
        link = item.get("link", "")
        is_uk_source = any(src in link for src in UK_NEWS_SOURCES)

        if is_health or is_uk_source:
            filtered.append(item)

    return filtered


def search_drug_disease_news(
    drug_name: str,
    disease_name: Optional[str] = None,
    synonyms: Optional[dict] = None
) -> list[dict]:
    """Search for drug/disease related news.

    Args:
        drug_name: Drug name to search
        disease_name: Optional disease name
        synonyms: Optional synonyms dictionary

    Returns:
        List of relevant news items
    """
    queries = [drug_name]

    if disease_name:
        queries.append(f"{drug_name} {disease_name}")

    # Add synonyms if available
    if synonyms and drug_name in synonyms.get("drug_synonyms", {}):
        for syn in synonyms["drug_synonyms"][drug_name]:
            queries.append(syn)

    all_items = []
    seen_links = set()

    # Fetch from Google News
    for query in queries:
        items = fetch_google_news_rss(query)
        items = filter_health_news(items)

        for item in items:
            link = item.get("link", "")
            if link not in seen_links:
                seen_links.add(link)
                all_items.append(item)

    # Also fetch from BBC Health RSS
    bbc_items = fetch_bbc_health_rss()
    for item in bbc_items:
        link = item.get("link", "")
        if link not in seen_links:
            seen_links.add(link)
            all_items.append(item)

    return all_items


def load_synonyms(base_dir: Path) -> dict:
    """Load synonyms from JSON file.

    Args:
        base_dir: Project base directory

    Returns:
        Synonyms dictionary
    """
    synonyms_file = base_dir / "data" / "news" / "synonyms.json"

    if synonyms_file.exists():
        with open(synonyms_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    return {}


def main():
    """Main function to test news fetching."""
    print("=" * 60)
    print("UkTxGNN - UK Health News Fetcher")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent.parent

    # Load synonyms
    synonyms = load_synonyms(base_dir)

    # Test search
    test_drugs = ["metformin", "aspirin", "ibuprofen"]

    for drug in test_drugs:
        print(f"\nSearching for: {drug}")
        items = search_drug_disease_news(drug, synonyms=synonyms)
        print(f"  Found {len(items)} items")

        for item in items[:3]:
            print(f"  - {item['title'][:60]}...")
            print(f"    Source: {item['source']}")


if __name__ == "__main__":
    main()
