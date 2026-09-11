# GameWire Ultimate

A static-first gaming news website template built for **SEO + scale + GitHub Pages + GitHub Actions + Astro**.

## What is included

- Home page
- News archive
- 180 demo article pages
- Individual game pages
- Category pages
- Platform pages
- Search
- About / Contact / Privacy
- 404
- RSS feed
- Automatic sitemap
- Canonical URLs
- robots directives
- Open Graph + Twitter cards
- `NewsArticle` JSON-LD
- `WebSite` + `SearchAction` JSON-LD
- Breadcrumb navigation
- Local lightweight SVG article images
- Responsive dark editorial design
- Hourly GitHub Actions news-update pipeline
- Separate deployment pipeline
- Python bulk-content generator for load/page testing

## Run locally

```bash
npm install
npm run dev
```

Build:

```bash
npm run build
```

## Generate lots of pages

```bash
python scripts/generate_pages.py --count 1000
npm run build
```

This creates 1,000 article records and local lightweight SVG images. Astro will generate a large number of static pages, letting you test the architecture and SEO output.

## Before production

Change these:

- `site` in `astro.config.mjs`
- `site` in `src/layouts/Layout.astro`
- `base` if the repository is not `/gamewire`
- `public/robots.txt` if you add one
- real contact/privacy information
- real RSS sources
- real source attribution
- licensed/owned images

## SEO philosophy

The important part is not simply adding meta keywords. The template focuses on:

1. Crawlable HTML
2. Unique URLs
3. Unique titles/descriptions
4. Canonical URLs
5. XML sitemap
6. RSS discovery
7. `NewsArticle` structured data
8. Breadcrumb structured navigation
9. Descriptive image alt text
10. Fast static output
11. Internal links between news → games → categories → platforms
12. Mobile-friendly responsive pages
13. No JavaScript requirement for core content
14. Clean URL hierarchy

## Important

Do not publish copied articles. Use RSS for discovery/metadata and link to the original source, or publish original/licensed summaries and reporting.
