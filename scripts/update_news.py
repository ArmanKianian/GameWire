"""
Production-oriented RSS ingestion starter.

Install:
  python -m pip install feedparser

Then put allowed RSS/Atom URLs in FEEDS.

The script stores metadata/excerpts and canonical source links. Do not copy
full copyrighted articles. Add your own rules for source attribution,
deduplication, filtering and any licensed images.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

FEEDS = [
    # "https://example.com/feed.xml",
]
OUT=Path("src/data/articles.json")

def stable_id(url):
    return hashlib.sha256(url.encode()).hexdigest()[:16]

def main():
    try:
        import feedparser
    except ImportError:
        raise SystemExit("Install feedparser first: python -m pip install feedparser")
    existing=json.loads(OUT.read_text()) if OUT.exists() else []
    by_url={a.get("sourceUrl"):a for a in existing if a.get("sourceUrl")}
    for feed_url in FEEDS:
        feed=feedparser.parse(feed_url)
        for e in feed.entries[:50]:
            url=e.get("link")
            title=e.get("title","Untitled").strip()
            if not url or not title: continue
            published=e.get("published") or e.get("updated") or datetime.now(timezone.utc).isoformat()
            article={
                "id":stable_id(url),"slug":stable_id(url)+"-"+title.lower().replace(" ","-")[:50],
                "title":title,"excerpt":e.get("summary","")[:280],
                "category":"Gaming","game":"Gaming","studio":feed.feed.get("title","Source"),
                "platforms":[],"tags":["gaming-news"],"author":"GameWire Staff",
                "publishedAt":published,"updatedAt":datetime.now(timezone.utc).isoformat(),
                "source":{"name":feed.feed.get("title","Original source"),"url":url},
                "sourceUrl":url,"image":"/GameWire/images/og.svg",
                "content":[e.get("summary",""),"Read the original source for the complete story."]
            }
            by_url[url]=article
    articles=sorted(by_url.values(),key=lambda a:a.get("publishedAt",""),reverse=True)[:2000]
    OUT.write_text(json.dumps(articles,indent=2,ensure_ascii=False)+"\n")
    print(f"Saved {len(articles)} stories.")

if __name__=="__main__":
    main()
