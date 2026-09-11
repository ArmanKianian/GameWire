import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwind from "@astrojs/tailwind";

export default defineConfig({
  site: "https://example.github.io/gamewire",
  base: "/gamewire",
  output: "static",
  integrations: [sitemap({
    filter: (page) => !page.includes("/404")
  }), tailwind()]
});