import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";

export default defineConfig({
  site: "https://armankianian.github.io/GameWire",
  base: "/GameWire",
  output: "static",
  integrations: [sitemap({
    filter: (page) => !page.includes("/404")
  })]
});
