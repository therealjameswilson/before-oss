import { expect, test } from "@playwright/test";

const profiles = [
  ["c37af33b-f26d-53cd-ad74-904f893ee7f3", "Raymond G Rocca"],
  ["b1252f4f-7a4a-5578-990f-78356402d831", "Vincent M Rocca"],
  ["e8798a28-1817-50b6-9f2a-12f70b9fbbbc", "Anthony A Rocco"],
  ["af594ec0-b763-5a8b-bb66-bb184154881b", "Alfred Roch"],
  ["37c12214-d227-5b04-9ac4-41a23910a322", "Robert Rochard"],
  ["3f5080ed-13fb-5a36-b84c-434b19b9075a", "Gerald E Roche"],
  ["098ea03a-20ad-58fc-9642-2d8d12e7723e", "Thomas J Roche"],
  ["7cd44b2c-4f80-5cba-b96a-13409a99449a", "William H Roche Jr."],
  ["811758f6-16a9-56c9-96d1-be5e7856e970", "John H Rochelle"],
  ["1d4c9770-e173-5681-856e-647760868a5f", "Jacob A Rock"],
  ["40eb3237-8bd7-514a-9d72-073c49b6786d", "Merle W Rock"],
  ["8c64fe2a-fbb5-5ca0-8010-d603cf51f7d1", "Steve A Rock"],
  ["f3044bc6-8792-5768-9f12-35e59b5de3d6", "Willy H Rocker"],
  ["13c65b3b-14bc-5430-9fda-6a8e97a61728", "Alice E Rockett"],
  ["3b9d4c8a-db21-590e-8805-9589c29c0f7d", "Abraham H Rockman"],
  ["598f0234-1f43-5e74-9bbb-81e1ef7513f7", "Sverre B Rockne"],
  ["384aa29e-7632-5e4a-9883-5a43cbeecb10", "Lee C Rocksien"],
  ["694da818-9834-5ca0-b8b0-c09b17afea3b", "Cornelia Rockwell"],
  ["45589faf-ac1f-58e7-9e0f-83e62b86fad5", "Dorothy Rockwell"],
  ["3d0e2f53-182e-5d2c-80d3-256e6dc33c5a", "Stuart W Rockwell"],
  ["856d7f45-13d5-556e-9a63-7897d4f2ee52", "Laura W Rockwood"],
  ["228ac0cd-808e-5be8-844a-60a278da1333", "Oscar Rodbell"],
  ["5745b23b-62fe-5556-954f-4c0ea8c8a4c1", "John B Rodd"],
] as const;

test("Batch 813 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Stuart Rockwell separates the Foreign Service, Army, and Harvard relationships", async ({ page }) => {
  await page.goto("./people/3d0e2f53-182e-5d2c-80d3-256e6dc33c5a/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("immediate pre-OSS");
  await expect(main).toContainText("United States Department of State");
  await expect(main).toContainText("last civilian");
  await expect(main).toContainText("Harvard University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("Stuart W. Rockwell Oral History Interview");
});

test("Vincent Rocca exposes the official Team Dormouse evidence", async ({ page }) => {
  await page.goto("./people/b1252f4f-7a4a-5578-990f-78356402d831/");
  const main = page.locator("main");
  await expect(main).toContainText("Team Dormouse");
  await expect(main).toContainText("National Park Service");
  await expect(main).toContainText("confirmed");
});

test("Anthony Rocco preserves the Rocca source variant", async ({ page }) => {
  await page.goto("./people/e8798a28-1817-50b6-9f2a-12f70b9fbbbc/");
  const main = page.locator("main");
  await expect(main.getByRole("heading", { name: "Anthony A Rocco", level: 1 })).toBeVisible();
  await expect(main).toContainText("Anthony A Rocca");
  await expect(main).toContainText("surname");
});

test("John Rodd remains separate and publishes the Rudd identifier conflict", async ({ page }) => {
  await page.goto("./people/5745b23b-62fe-5556-954f-4c0ea8c8a4c1/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("John B. Rudd");
  await expect(main).toContainText("Boxes 653 and 665");
});

test("home page exposes the rebuilt Batch 813 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,684");
  await expect(home).toContainText("48.81%");
  await expect(home).toContainText("12,249");
  await expect(home).toContainText("834");
  await expect(home).toContainText("374");
  await expect(home).toContainText("10,147");
});
