import fs from "node:fs";
import path from "node:path";

const dist = path.resolve("dist");
const base = "/before-oss/";
const htmlFiles = [];
const external = new Set();

function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    const full = path.join(directory, entry.name);
    if (entry.isDirectory()) walk(full);
    else if (entry.name.endsWith(".html")) htmlFiles.push(full);
  }
}

function targetFor(href) {
  const pathname = href.split(/[?#]/, 1)[0];
  if (!pathname || pathname === "/") return path.join(dist, "index.html");
  const relative = pathname.startsWith(base)
    ? pathname.slice(base.length)
    : pathname.replace(/^\/+/, "");
  const direct = path.join(dist, relative);
  if (path.extname(direct)) return direct;
  return path.join(direct, "index.html");
}

walk(dist);
const missing = [];
for (const file of htmlFiles) {
  const html = fs.readFileSync(file, "utf8");
  for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    const href = match[1];
    if (/^(?:mailto:|tel:|data:|#)/.test(href)) continue;
    if (/^https?:\/\//.test(href)) {
      external.add(href.split("#", 1)[0]);
      continue;
    }
    if (!fs.existsSync(targetFor(href))) {
      missing.push(`${path.relative(dist, file)} -> ${href}`);
    }
  }
}

if (missing.length) {
  console.error(`Missing internal targets (${missing.length}):`);
  console.error(missing.slice(0, 100).join("\n"));
  process.exit(1);
}
console.log(
  `Checked ${htmlFiles.length.toLocaleString()} HTML files; all internal links resolve. ` +
  `${external.size} unique external URLs were inventoried for the separate live check.`,
);
