import { defineConfig } from "astro/config";

const base = process.env.PUBLIC_BASE_PATH || "/before-oss";
const site = process.env.PUBLIC_SITE_URL || "https://example.invalid";
const outDir = process.env.BEFORE_OSS_DIST_DIR || "./dist";
const publicDir = process.env.BEFORE_OSS_PUBLIC_DIR || "./public";

export default defineConfig({
  site,
  base,
  publicDir,
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
