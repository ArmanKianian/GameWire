import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwind from "@astrojs/tailwind";

export default defineConfig({
  site: "https://armankianian.github.io/GameWire",
  base: "/gamewire",
  output: "static",
  integrations: [sitemap({
    filter: (page) => !page.includes("/404")
  }), tailwind()]
});
