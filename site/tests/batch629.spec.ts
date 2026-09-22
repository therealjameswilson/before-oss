import { expect, test } from "@playwright/test";

test("Donald McCarthy receives only the supported Army identity crosswalk", async ({ page }) => {
  await page.goto("./people/4c805025-19d5-5ea8-984b-fa3aa71e7461/");
  await expect(page.getByRole("heading", { name: "Donald K McCarthy", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("high confidence");
  await expect(page.locator("main")).toContainText("nonshared protected identifier");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("the two John F McCarthy rows remain separate and evidence-distinct", async ({ page }) => {
  await page.goto("./people/98b57dae-121f-52b2-810c-165e26f3751a/");
  await expect(page.getByRole("heading", { name: "John F McCarthy", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("high confidence");
  await expect(page.locator("main")).toContainText("staff-sergeant John F. McCarthy row");
  await expect(page.locator("main")).toContainText("adjacent same-name index row");

  await page.goto("./people/d5db343c-7209-505d-b40b-f777f67cf63c/");
  await expect(page.getByRole("heading", { name: "John F McCarthy", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("ambiguous");
  await expect(page.locator("main")).toContainText("a protected identifier different from the staff-sergeant row");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("the McCarary-McCrary pair remains separate and unresolved", async ({ page }) => {
  await page.goto("./people/1aa37e74-b066-54a9-b781-89500217fb27/");
  await expect(page.getByRole("heading", { name: "Jack L McCarary", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("probable duplicate");
  await expect(page.locator("main")).toContainText("original-jacket confirmation");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");

  await page.goto("./people/4960f431-455c-5d03-a23d-90159edbc153/");
  await expect(page.getByRole("heading", { name: "Jack L McCrary", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("probable duplicate");
  await expect(page.locator("main")).toContainText("original-jacket confirmation");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 629 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,580");
  await expect(page.locator("body")).toContainText("31.66%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Donald K McCarthy");
});
