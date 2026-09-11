import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  site: "https://example.github.io/gamewire",
  base: "/gamewire",
  output: "static",
  vite: {
    plugins: [tailwindcss()]
  },
  integrations: [sitemap({
    filter: (page) => !page.includes("/404")
  })]
});