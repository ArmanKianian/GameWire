"""
Generate lots of realistic demo articles for testing Astro's static page generation.

Usage:
  python scripts/generate_pages.py --count 1000
  python scripts/generate_pages.py --count 500 --seed 42

This changes src/data/articles.json and creates lightweight local SVG artwork.
It does NOT scrape copyrighted articles. Replace the generated demo data with
your own licensed/allowed feed ingestion before production.
"""
from pathlib import Path
from datetime import datetime, timedelta, timezone
import argparse, json, random, re

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"src/data/articles.json"
IMG=ROOT/"public/images/news"

GAMES=[
("Elden Ring","RPG","FromSoftware"),("Grand Theft Auto VI","Open World","Rockstar Games"),
("Resident Evil Requiem","Horror","Capcom"),("Cyberpunk 2077","RPG","CD PROJEKT RED"),
("The Witcher 4","RPG","CD PROJEKT RED"),("Monster Hunter Wilds","Action RPG","Capcom"),
("Minecraft","Sandbox","Mojang"),("Hades II","Roguelike","Supergiant Games"),
("Final Fantasy VII Rebirth","RPG","Square Enix"),("Death Stranding 2","Action","Kojima Productions")
]
PLATFORMS=["PC","PlayStation 5","Xbox Series X|S","Nintendo Switch 2"]
CATS=["Gaming","RPG","Action","Horror","Open World","Hardware","PC","PlayStation","Xbox","Nintendo"]
VERBS=["gets a major new update","reveals fresh details","has players talking again","adds a new reason to return","gets another big announcement"]
TOPICS=["new update","latest announcement","upcoming release","developer reveal","major patch"]

def slug(s):
    return re.sub(r"[^a-z0-9]+","-",s.lower()).strip("-")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--count",type=int,default=500)
    ap.add_argument("--seed",type=int,default=42)
    args=ap.parse_args()
    random.seed(args.seed)
    now=datetime.now(timezone.utc)
    articles=[]
    for i in range(args.count):
        game,genre,studio=random.choice(GAMES)
        verb=random.choice(VERBS)
        topic=random.choice(TOPICS)
        title=f"{game} {verb} as {topic} sparks a new wave of discussion"
        published=now-timedelta(hours=i*3+random.randint(0,20))
        s=slug(title)+f"-{i+1}"
        articles.append({
            "id":f"generated-{i+1:06d}","slug":s,"title":title,
            "excerpt":f"Here is what players should know about the latest {game} {topic}.",
            "category":random.choice(CATS),"game":game,"studio":studio,
            "platforms=random.sample(PLATFORMS,k=2)": None
        })
        articles[-1]["platforms"]=random.sample(PLATFORMS,k=2)
        articles[-1]["tags"]=[slug(game),slug(genre),"gaming-news",slug(topic)]
        articles[-1]["author"]="GameWire Staff"
        articles[-1]["publishedAt"]=published.isoformat()
        articles[-1]["updatedAt"]=(published+timedelta(hours=1)).isoformat()
        articles[-1]["source"]={"name":studio,"url":"https://example.com/"}
        articles[-1]["image"]=f"/gamewire/images/news/{s}.svg"
        articles[-1]["content"]=[
            f"{game} is at the center of the latest gaming discussion.",
            f"The new {topic} gives players another reason to keep an eye on {game}.",
            "This generated article exists to test the site's page architecture, internal links and SEO at scale.",
            "For production, replace this demo copy with original reporting or properly licensed/allowed source summaries."
        ]
        IMG.mkdir(parents=True,exist_ok=True)
        (IMG/f"{s}.svg").write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900"><rect width="1600" height="900" fill="#0d0d0d"/><circle cx="1200" cy="200" r="300" fill="#4a2b12" opacity=".35"/><text x="100" y="690" fill="#f1b86a" font-family="Arial" font-size="36" font-weight="700">GAMEWIRE</text><text x="100" y="770" fill="#fff" font-family="Arial" font-size="60" font-weight="800">{game[:30]}</text></svg>',
            encoding="utf-8")
    OUT.write_text(json.dumps(articles,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"Generated {len(articles)} articles.")

if __name__=="__main__":
    main()
