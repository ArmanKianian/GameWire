"""
Starter news updater.

Replace FEEDS with RSS feeds you are permitted to use.
The script intentionally keeps the first version simple:
RSS -> normalized JSON -> Git commit -> Astro deploy.
"""
from pathlib import Path
import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

FEEDS = [
    # Add RSS URLs here.
    # "https://example.com/feed.xml",
]

OUT = Path("src/data/articles.json")

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "GameWire/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read()

def main():
    existing = json.loads(OUT.read_text())
    by_id = {a["id"]: a for a in existing}

    for feed_url in FEEDS:
        try:
            root = ET.fromstring(fetch(feed_url))
        except Exception as exc:
            print(f"Skipping {feed_url}: {exc}")
            continue

        for item in root.findall(".//item")[:20]:
            title = item.findtext("title") or "Untitled"
            link = item.findtext("link") or "#"
            description = item.findtext("description") or ""
            guid = item.findtext("guid") or link
            article_id = str(abs(hash(guid)))

            by_id[article_id] = {
                "id": article_id,
                "title": title.strip(),
                "description": description.strip(),
                "category": "Gaming",
                "game": "Gaming",
                "source": feed_url,
                "publishedAt": datetime.now(timezone.utc).isoformat(),
                "url": link.strip(),
                "image": ""
            }

    articles = sorted(by_id.values(), key=lambda x: x["publishedAt"], reverse=True)[:500]
    OUT.write_text(json.dumps(articles, ensure_ascii=False, indent=2) + "\n")
    print(f"Saved {len(articles)} articles")

if __name__ == "__main__":
    main()
