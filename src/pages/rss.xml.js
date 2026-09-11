import rss from "@astrojs/rss";
import articles from "../data/articles.json";
export function GET(context) {
  return rss({
    title: "GameWire — Gaming News",
    description: "The latest gaming news and stories.",
    site: context.site,
    items: articles.slice(0, 50).map(a => ({
      title: a.title,
      pubDate: new Date(a.publishedAt),
      description: a.excerpt,
      link: `/news/${a.slug}/`
    }))
  });
}