import { expect, test } from "@playwright/test";

const profiles = [
  ["58b33c15-31ea-5166-b549-30be0e004b92", "Julian A Oflaherty"],
  ["69fe4ea3-dfc2-5d79-91ec-325f2b6432e9", "Douglas N Ogan"],
  ["87b4e66f-86a1-5699-ad82-6465b760be4a", "Dorothy T Ogata"],
  ["1f5dd951-1ba3-5b4e-838d-faad8208cd27", "Edward Ogden"],
  ["c365d76b-f880-5e41-89ff-b4d77af9be79", "Marcus R Ogden"],
  ["0bc4cc82-4bac-5d01-94f2-3241189aa7fb", "Thomas A Ogden"],
  ["93ffbe19-b195-5336-9a98-24b1d47d7960", "William L Ogden"],
  ["4eb5d817-6141-5eff-b10d-406fd0497543", "Robert E Ogg"],
  ["7eb5508f-edce-5ce6-9743-5e2b2f05452e", "Martha C Ogilvie"],
  ["982b8c68-565d-5739-a15e-71691572c593", "Carla Ogle"],
  ["21fc0746-dd8c-51b9-8b93-33ccf747b163", "Lairo M Ogle"],
  ["eb1f55e1-c295-53d3-b476-8e9cd0ac7ba9", "Marbury B Ogle"],
  ["9230aff7-aafc-5b94-ad4a-6040b286028a", "Mildred E Ogle"],
  ["06a807ce-3b19-59d9-9860-c1d657622371", "Ezra G Ogletree"],
  ["329cecba-b627-5f37-a4d2-08593ca5fba1", "John F Oglevee"],
  ["2356b15c-9b3d-513e-a350-b11c314da867", "Phyllis Ogrean"],
  ["2b2525d3-9adc-5e42-af3c-baa9d125ddcf", "Shirley D Ogren"],
  ["47fb69d3-a0b2-5719-818f-7417d1f379c0", "Warren A Ogren"],
  ["c628754b-a341-515a-93db-ef93b040d660", "Louis Oguss"],
  ["16976be7-cfc0-5b4b-bb9d-18d0e8c53d02", "Patrick Ohanlon"],
  ["90b8f7f2-f3fd-5aac-a3d0-c8208b8ce0ac", "Edward C Ohara"],
  ["1a9f2a73-b2a2-5926-9a96-d0978dff7048", "James F Ohara"],
  ["65cfac05-eef6-52ff-a167-68e71c6d89c1", "James W Ohara"],
] as const;

test("Batch 715 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 715 distinguishes Marbury Ogle's three pre-OSS relationships", async ({ page }) => {
  await page.goto("./people/eb1f55e1-c295-53d3-b476-8e9cd0ac7ba9/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Marbury Bladen Ogle Jr.");
  await expect(main).toContainText("U.S. Department of Justice, Special War Policy Unit");
  await expect(main).toContainText("immediate pre-OSS");
  await expect(main).toContainText("Western Reserve University");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("Instructor of political science");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("possibly");
});

test("Batch 715 qualifies John Oglevee's Ohio State role", async ({ page }) => {
  await page.goto("./people/329cecba-b627-5f37-a4d2-08593ca5fba1/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("The Ohio State University");
  await expect(main).toContainText("Reader in History");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("medium A direct official");
  await expect(main).toContainText("needs temporal review");
});

test("Batch 715 visibly qualifies Dorothy Ogata's scholarly OSS context", async ({ page }) => {
  await page.goto("./people/87b4e66f-86a1-5699-ad82-6465b760be4a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("probably the Dorothy Ogata");
  await expect(main).toContainText("Asian American Mata Hari");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 715 preserves the Ogden and OGDEE identity conflict", async ({ page }) => {
  await page.goto("./people/1f5dd951-1ba3-5b4e-838d-faad8208cd27/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("OGDEE EDWARD");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("neither spelling replaces the other");
});

test("Batch 715 publishes Patrick O'Hanlon's qualified official identity", async ({ page }) => {
  await page.goto("./people/16976be7-cfc0-5b4b-bb9d-18d0e8c53d02/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Patrick Hudson O'Hanlon");
  await expect(main).toContainText("Intelligence Corps");
  await expect(main).toContainText("Medal of Freedom with Bronze Palm");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 715 publishes accepted Army identities without inventing employment", async ({ page }) => {
  for (const id of [
    "0bc4cc82-4bac-5d01-94f2-3241189aa7fb",
    "06a807ce-3b19-59d9-9860-c1d657622371",
    "47fb69d3-a0b2-5719-818f-7417d1f379c0",
    "c628754b-a341-515a-93db-ef93b040d660",
    "90b8f7f2-f3fd-5aac-a3d0-c8208b8ce0ac",
    "1a9f2a73-b2a2-5926-9a96-d0978dff7048",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 715 publishes exact rebuilt coverage and preserves the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,483");
  await expect(main).toContainText("39.61%");
  await expect(main).toContainText("14,451");
  await expect(main).toContainText("722");
  await expect(main).toContainText("326");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
