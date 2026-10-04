import { expect, test } from "@playwright/test";

const profiles = [
  ["74c973f1-c6ae-58ca-b381-d82e769241e3", "Raye Palmer"],
  ["e91d5afb-1a97-56f8-8fcd-a70cc3e0239b", "Theodore P Palmer"],
  ["670647ea-b359-52e7-8e26-1e5d37635c8a", "Theodore D Palmer Jr."],
  ["52a9f02a-fb78-5d3d-a17e-09998cc1b418", "William H Palmer"],
  ["14f08802-a1da-502b-9ac6-ec1c37822819", "William A Palmer"],
  ["a486f8d0-3f3a-59c8-8638-62f79e062c72", "Joseph L Palosky"],
  ["b0547021-142c-5a93-a765-6b905e0f61c1", "Phyllis M Palson"],
  ["b4d8a525-eb98-5be2-b15f-c493c597486b", "Leo J Pampalone"],
  ["6832f904-4c3f-51c8-8564-1cde3599a155", "Francis Pamplin"],
  ["d0ceb5cc-d30c-55a0-a642-c9579a09c069", "Hiram C Pamplin"],
  ["8793d915-402d-5f2c-9d8b-7d045a84c6bc", "Jack C Pamplin"],
  ["0d1fac30-5aad-5d02-b996-ec2e7f51da84", "Peter M Panagakos"],
  ["a31ba4da-4afc-5f32-9cce-55c8a1bd167b", "Sotirios Panagiotareas"],
  ["02f1aa3e-c7de-5ccb-9040-9f601177e408", "Arthur J Panagiotopoul"],
  ["ce6e6c8f-d0e9-5d54-ac3e-d63ed2cc85dd", "Anthony Panaro"],
  ["c09fb374-7ebb-5e9c-8cd3-07420da9fe64", "Pietro Panaro"],
  ["731d83de-8dd7-5278-9679-7a350fc06e63", "Joseph P Pando"],
  ["056e221a-f507-5e05-b6b7-a9c4330a6a90", "John C Pangborn Jr."],
  ["9c4e3e04-f6bd-5b08-a286-b66d351aa604", "Peter N Panos"],
  ["5ed02812-53c1-5d56-8ef8-e8b54eb7280a", "Guido Pantaleoni"],
  ["2abf2b6c-6b57-55f0-84e7-9a2b081ffefc", "Nicholas G Pantelias"],
  ["2c115c6f-3cc4-5607-8691-fb88af43ecc7", "Kusa Panyarjun"],
  ["a66ae0a3-5131-5c27-b9c9-671f793b1d2e", "Giacomo Panza"],
] as const;

test("Batch 731 publishes all 23 direct profile routes with reviewed outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^\d{4,8}$/);
  }
});

test("Batch 731 publishes Guido Pantaleoni's strongly bounded law-firm chronology", async ({ page }) => {
  await page.goto("./people/5ed02812-53c1-5d56-8ef8-e8b54eb7280a/");
  const main = page.locator("main");
  await expect(main).toContainText("Reavis & Pantaleoni");
  await expect(main).toContainText("Co-founder and lawyer");
  await expect(main).toContainText("1935");
  await expect(main).toContainText("1943");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("2677 Company");
  await expect(main).toContainText("AfterWords, July 2004");
  await expect(main).not.toContainText("Last civilian employer before serviceWhite & Case");
});

test("Batch 731 presents Kusa Panyarjun's Penn link as student status, not employment", async ({ page }) => {
  await page.goto("./people/2c115c6f-3cc4-5607-8691-fb88af43ecc7/");
  const main = page.locator("main");
  await expect(main).toContainText("Kusa Panyarachun");
  await expect(main).toContainText("University of Pennsylvania");
  await expect(main).toContainText("Student");
  await expect(main).toContainText("freshman crew candidate");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationUniversity of Pennsylvania");
  await expect(main).not.toContainText("Last civilian employer before serviceUniversity of Pennsylvania");
  await expect(main).toContainText("postwar World Travel Service role is excluded");
});

test("Batch 731 keeps Theodore D Palmer Jr.'s wartime assignment visibly qualified", async ({ page }) => {
  await page.goto("./people/670647ea-b359-52e7-8e26-1e5d37635c8a/");
  const main = page.locator("main");
  await expect(main).toContainText("Army Specialized Training Division");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("sequence relative to OSS service is not established");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");
});

test("Batch 731 corroborates Peter Panagakos and Anthony Panaro without inventing employers", async ({ page }) => {
  await page.goto("./people/0d1fac30-5aad-5d02-b996-ec2e7f51da84/");
  await expect(page.locator("main")).toContainText("Greek Group VII");
  await expect(page.locator("main")).toContainText("high confidence");
  await expect(page.locator("main")).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/ce6e6c8f-d0e9-5d54-ac3e-d63ed2cc85dd/");
  await expect(page.locator("main")).toContainText("Peedee mission roster");
  await expect(page.locator("main")).toContainText("high confidence");
  await expect(page.locator("main")).toContainText("No reviewed claim currently meets the publication threshold.");
});

test("Batch 731 rebuilds exact coverage and verified-employer totals", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,849");
  await expect(main).toContainText("41.14%");
  await expect(main).toContainText("14,085");
  await expect(main).toContainText("743");
  await expect(main).toContainText("333");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
