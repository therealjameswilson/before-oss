import { spawn } from "node:child_process";
import { copyFile, mkdir, readdir, stat } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import process from "node:process";

const ROOT = process.cwd();
const PUBLIC_DIR = path.join(ROOT, "public");
const DIST_DIR = path.resolve(ROOT, process.env.BEFORE_OSS_DIST_DIR || "dist");
const EMPTY_PUBLIC_DIR = path.join(os.tmpdir(), "before-oss-empty-public");
const TRANSIENT_CODES = new Set(["EBUSY", "EIO", "EMFILE", "ENFILE", "ETIMEDOUT"]);
const MAX_ATTEMPTS = 6;

const sleep = (milliseconds) =>
  new Promise((resolve) => setTimeout(resolve, milliseconds));

async function copyWithRetry(source, destination) {
  await mkdir(path.dirname(destination), { recursive: true });
  for (let attempt = 1; attempt <= MAX_ATTEMPTS; attempt += 1) {
    try {
      await copyFile(source, destination);
      const [sourceStat, destinationStat] = await Promise.all([
        stat(source),
        stat(destination),
      ]);
      if (sourceStat.size !== destinationStat.size) {
        const error = new Error(
          `Size mismatch after copying ${source}: ${sourceStat.size} != ${destinationStat.size}`,
        );
        error.code = "EIO";
        throw error;
      }
      return sourceStat.size;
    } catch (error) {
      if (!TRANSIENT_CODES.has(error?.code) || attempt === MAX_ATTEMPTS) {
        throw error;
      }
      const delay = 250 * 2 ** (attempt - 1);
      console.warn(
        `Public asset copy retry ${attempt}/${MAX_ATTEMPTS} for ${path.relative(ROOT, source)} after ${error.code}; waiting ${delay}ms`,
      );
      await sleep(delay);
    }
  }
  throw new Error(`Unable to copy ${source}`);
}

async function copyTree(sourceDir, destinationDir) {
  let files = 0;
  let bytes = 0;
  const entries = await readdir(sourceDir, { withFileTypes: true });
  entries.sort((left, right) => left.name.localeCompare(right.name));
  for (const entry of entries) {
    const source = path.join(sourceDir, entry.name);
    const destination = path.join(destinationDir, entry.name);
    if (entry.isDirectory()) {
      const child = await copyTree(source, destination);
      files += child.files;
      bytes += child.bytes;
    } else if (entry.isFile()) {
      bytes += await copyWithRetry(source, destination);
      files += 1;
    }
  }
  return { files, bytes };
}

function runAstroBuild() {
  const executable = path.join(ROOT, "node_modules", ".bin", "astro");
  return new Promise((resolve, reject) => {
    const child = spawn(executable, ["build"], {
      cwd: ROOT,
      env: { ...process.env, BEFORE_OSS_PUBLIC_DIR: EMPTY_PUBLIC_DIR },
      stdio: "inherit",
    });
    child.once("error", reject);
    child.once("exit", (code, signal) => {
      if (code === 0) {
        resolve();
      } else {
        reject(
          new Error(
            `Astro build failed with ${signal ? `signal ${signal}` : `exit code ${code}`}`,
          ),
        );
      }
    });
  });
}

await mkdir(EMPTY_PUBLIC_DIR, { recursive: true });
await runAstroBuild();
const copied = await copyTree(PUBLIC_DIR, DIST_DIR);
console.log(
  `Copied and size-verified ${copied.files.toLocaleString("en-US")} public assets (${copied.bytes.toLocaleString("en-US")} bytes) into ${path.relative(ROOT, DIST_DIR) || "."}.`,
);
