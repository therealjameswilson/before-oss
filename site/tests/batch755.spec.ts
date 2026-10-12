import { expect, test } from "@playwright/test";

const profiles = [
  ["dd652d06-032b-5e4a-8851-e3a5d791fde7", "Kenneth H Phillips"],
  ["2069b215-2161-55ea-a02a-ef33949909b3", "Margaret K Phillips"],
  ["e8ceef98-bd3c-5b8f-8d18-911345715faf", "Marion E Phillips"],
  ["9d891299-cffb-5459-8ce3-3345970a08ef", "Paul A Phillips"],
  ["75324529-d0bb-5770-af3b-93cce98c7497", "Perecles P Phillips"],
  ["4afb2052-2862-5ccb-9f25-fe51a2c7952a", "Richard B Phillips"],
  ["a40da12d-6c8f-56c4-a381-5fdde3a98433", "Robert S Phillips"],
  ["cf726735-916c-5f68-9189-3c58aafaf4c8", "Ruth M Phillips"],
  ["69b617a9-aed9-55b8-9441-798e4f100ca8", "Sally Phillips"],
  ["86d6dd84-3459-5696-aa6d-a8b16f7e8575", "Sam B Phillips"],
  ["d845d2ba-7c3a-585f-acfc-16178981ce40", "Ulva J Phillips"],
  ["7499f0e1-eb1a-57d3-8051-a0b214032d6f", "Wallace B Phillips"],
  ["97647744-820b-5544-9428-c01540d1c71c", "Wayman F Phillips"],
  ["e8b3dda2-5d71-56c6-823a-898a5e8f6436", "William Phillips"],
  ["888ba408-6781-5296-a7f9-979b73b59c72", "William R Phillips"],
  ["dd60bd38-8733-5f4e-91d8-d9c81bf238d6", "Robert L Philpot"],
  ["a76b834b-4022-5a7c-b591-df5a6247c2b7", "Charles H Phipps"],
  ["ca0c9320-f7d7-5032-b6f1-60432d91ca90", "Edward A Phipps"],
  ["5260f46c-2b07-5509-bc4a-e858d83e2697", "Amnuay Phoonphiphut"],
  ["f50fb8de-3aa7-5b29-8e72-8f8a73de8823", "Peter C Photis"],
  ["ee7618c2-d0ee-59d8-a117-d4b5506457a9", "John U Physioc"],
  ["a75265a2-8500-5af0-9321-593cf52cf008", "Arthur R Piantadosi"],
  ["dd059ef0-ded2-5514-9343-3480d3ffe8b7", "Louis Piantadosi"],
] as const;

test("Batch 755 publishes all 23 page-368 profiles with reviewed outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 755 corroborates Perecles Phillips without inventing an employer", async ({ page }) => {
  await page.goto("./people/75324529-d0bb-5770-af3b-93cce98c7497/");
  const main = page.locator("main");
  await expect(main).toContainText("Perecles Peter Phillips");
  await expect(main).toContainText("Perry Phillips");
  await expect(main).toContainText("Greek Operational Group");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 755 publishes Peter Photis's corroborated OSS identity only", async ({ page }) => {
  await page.goto("./people/f50fb8de-3aa7-5b29-8e72-8f8a73de8823/");
  const main = page.locator("main");
  await expect(main).toContainText("OSS commando");
  await expect(main).toContainText("Greek-U.S. Operational Group");
  await expect(main).toContainText("Charles F. Snyder Funeral Homes");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 755 keeps Robert Phillips's inaccessible official lead qualified", async ({ page }) => {
  await page.goto("./people/a40da12d-6c8f-56c4-a381-5fdde3a98433/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("could not be directly inspected");
  await expect(main).toContainText("Inspect Box 603");
});

test("home page exposes the rebuilt Batch 755 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,394");
  await expect(home).toContainText("43.42%");
  await expect(home).toContainText("13,540");
  await expect(home).toContainText("774");
  await expect(home).toContainText("344");
  await expect(home).toContainText("8,853");
});
