import { defineConfig } from "astro/config";

const base = process.env.PUBLIC_BASE_PATH || "/before-oss";
const site = process.env.PUBLIC_SITE_URL || "https://example.invalid";
const outDir = process.env.BEFORE_OSS_DIST_DIR || "./dist";

export default defineConfig({
  site,
  base,
  output: "static",
  outDir,
  trailingSlash: "always",
  build: {
    format: "directory",
    concurrency: 4
  },
  vite: {
    build: {
      sourcemap: false
    }
  }
});
