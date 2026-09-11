# GameWire

A static, self-updating gaming news portal built with Astro + GitHub Pages + GitHub Actions.

## Local development

```bash
npm install
npm run dev
```

## Automatic updates

Edit `scripts/update_news.py` and add RSS feeds to `FEEDS`.

The `update-news.yml` workflow runs hourly, updates `src/data/articles.json`, commits changes, and the deployment workflow rebuilds the Astro site.

## Before deploying

1. Change `site` and `base` in `astro.config.mjs`.
2. Replace the demo articles.
3. Add your RSS sources.
4. Configure GitHub Pages to use **GitHub Actions**.
5. Add proper attribution/source links for every feed.

## Planned upgrades

- RSS/Atom parser with `feedparser`
- duplicate detection using canonical URLs
- source-specific parsers
- game/entity detection
- article importance scoring
- generated article pages
- sitemap + RSS output
- JSON-LD NewsArticle
- Open Graph images
- search
- trending games
- optional AI classification/summarization
