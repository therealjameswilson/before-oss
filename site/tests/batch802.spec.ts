import { expect, test } from "@playwright/test";

const profiles = [
  ["d6b3fc7e-5763-527a-a822-9df54ceae60e", "Joseph V Richards", "642"],
  ["7c3997b1-fc44-51b5-bcd5-06b19eb6e9b2", "Louise Richards", "643"],
  ["202f284c-1df6-50ee-b290-3e739f18339f", "Richard K Richards", "643"],
  ["26be9ea1-21e7-5df9-8684-6bfb2dc9d3b4", "Robert W Richards", "643"],
  ["af8deeb6-e6c6-5d16-8f8f-47a76143a454", "Rudolph A Richards", "643"],
  ["cb0f9c7e-b4d0-53b3-8b56-64eef189ec3e", "William W Richards", "643"],
  ["9caad58c-3367-5cd4-9d9a-2663fed94eef", "Don C Richardson", "643"],
  ["89e469e2-17ae-50dc-bffb-dfc78514a45b", "Earl E Richardson", "643"],
  ["b80fdd23-1392-5c79-8ddb-4820752f7d39", "Evelyn R Richardson", "643"],
  ["385dab26-bfd6-509d-8954-ca7087976b0f", "Frank D Richardson", "643"],
  ["d9e5a0aa-2d66-5983-8d2a-e0ea66bfe9a5", "John H Richardson", "643"],
  ["8347f5d5-c63d-579b-b261-27a08bab10e5", "John L Richardson", "643"],
  ["36da48f0-9ac6-5691-9b0f-bf7c66ccc581", "Joseph M Richardson", "643"],
  ["49074a93-000f-5f45-ba46-c235e6eb28e5", "Reuben L Richardson", "643"],
  ["0a736e81-5d69-582d-82a1-8affc7e13713", "Wayne H Richardson", "643"],
  ["3fd2451a-c8c6-5b8c-bc3a-888926774907", "Wesley E Richardson", "643"],
  ["a1d63dc2-27c3-5197-b2ec-dabef2452fee", "William Richardson", "643"],
  ["c7b65b8d-a0d0-5c20-99da-266c5a534fb0", "Clayton H Richardson Jr.", "643"],
  ["09f71f2c-29f9-5102-992c-433a9ca6028b", "Louis Richardson Jr.", "643"],
  ["be8d131e-0212-58da-a859-24dfc1a81214", "William Richardson-Be", "643"],
  ["2e657989-7488-5bcd-8833-906bf2425a16", "Mark W Richcreek", "643"],
  ["5bb0cfcb-cc2e-5339-bcb8-34821e46ea3e", "Donald H Richer", "643"],
  ["a16ecdbc-3391-5456-8423-b6ce43f5d7e6", "Edmond R Richer", "643"],
] as const;

test("Batch 802 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText(box);
    await expect(main).not.toContainText("not started");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 802 publishes six high-confidence Army identities without employer inference", async ({
  page,
}) => {
  for (const [id] of [
    ["d6b3fc7e-5763-527a-a822-9df54ceae60e"],
    ["202f284c-1df6-50ee-b290-3e739f18339f"],
    ["9caad58c-3367-5cd4-9d9a-2663fed94eef"],
    ["89e469e2-17ae-50dc-bffb-dfc78514a45b"],
    ["c7b65b8d-a0d0-5c20-99da-266c5a534fb0"],
    ["09f71f2c-29f9-5102-992c-433a9ca6028b"],
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("requires archival review");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
  }
});

test("William Richardson exposes the protected-identifier name conflict", async ({ page }) => {
  await page.goto("./people/a1d63dc2-27c3-5197-b2ec-dabef2452fee/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Charles W. Richardson");
  await expect(main).toContainText("Electronic Army Serial Number Merged File");
});

test("Batch 802 preserves raw notes and the clipped surname", async ({ page }) => {
  await page.goto("./people/89e469e2-17ae-50dc-bffb-dfc78514a45b/");
  await expect(page.locator("main")).toContainText("Record");

  await page.goto("./people/5bb0cfcb-cc2e-5339-bcb8-34821e46ea3e/");
  await expect(page.locator("main")).toContainText("Danish");
  await expect(page.locator("main")).toContainText("MM2/c");

  await page.goto("./people/be8d131e-0212-58da-a859-24dfc1a81214/");
  await expect(page.getByRole("heading", { name: "William Richardson-Be", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("clipped surname");
});

test("home page exposes the rebuilt Batch 802 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,434");
  await expect(home).toContainText("47.76%");
  await expect(home).toContainText("12,500");
  await expect(home).toContainText("820");
  await expect(home).toContainText("370");
  await expect(home).toContainText("9,897");
});
