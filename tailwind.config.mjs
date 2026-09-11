/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    fontFamily: {
      sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
    },
    colors: {
      gold: '#f1b86a',
      muted: '#8b8b8b',
      line: '#242424',
      'bg-dark': '#090909',
      'bg-card': '#111',
      'bg-hover': '#171717',
    },
  },
  plugins: [],
}