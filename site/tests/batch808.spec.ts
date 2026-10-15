import { expect, test } from "@playwright/test";

const profiles = [
  ["95ba9bbd-9b2f-5267-8ddf-9506e071fc81", "Antolino Rivera", "648"],
  ["f5a5e02f-d532-58d1-b717-4a24163633cf", "Ishmael Rivera", "648"],
  ["7352e8f9-f6b6-5176-90b2-1d9a5ae61c4d", "Michael A Rivera", "648"],
  ["e0e2dbcf-294c-5767-98b9-1b89bcbdf0d2", "David Rivers", "648"],
  ["06577906-160d-54b2-a89e-11f50f748c9b", "Francis B Rives", "648"],
  ["da45f1c9-db00-5500-9ff9-d8987947c7b0", "Benjamin Rivlin", "648"],
  ["39b18cbd-81ea-5cee-8794-f49580b49dfc", "Alphonse Rizzo", "648"],
  ["ac5f7e34-29b1-5189-9f0f-25ec2aa5b33a", "Antonio A Rizzo", "648"],
  ["d2a4aa6a-9134-5e42-81e6-35b4335cb89a", "Ovid Rizzolo", "648"],
  ["162f95e0-7e6e-551a-b057-11619d8887db", "James R Roach", "649"],
  ["4b44ec53-cbdc-5e96-b758-6e037e0bc589", "William E Roach", "649"],
  ["4256c2ec-1a64-593f-b9e2-9b79622555d2", "James Roaden", "649"],
  ["b73a6e4f-f5fa-5c8a-9cee-bda516da74df", "Chester F Robards", "649"],
  ["b7c90057-c562-5286-8c90-45cc52f99ed0", "Janice Robarge", "649"],
  ["16c0bf61-5a6e-50df-8f9c-a9a438b38523", "Woodrow W Robarge", "649"],
  ["adbf4169-083c-53b7-83d5-2c77f54eb832", "Cornelia T Robb", "649"],
  ["d720d668-0d0b-5424-8392-fe4bd22d4a07", "George W Robb", "649"],
  ["6644471c-28b4-5342-8646-94ff75c4a920", "Roberta H Robb", "649"],
  ["7fd2df90-8f0a-5177-8cac-da63dbe1f43d", "Billy A Robbins", "649"],
  ["7d872408-fc20-55fb-af29-fddceeb61fb1", "Clyde C Robbins Jr.", "649"],
  ["d60c28cc-2f5c-5ab3-ba84-64d8a0e7ace6", "Edgar S Robbins", "649"],
  ["250c9c1e-b3fb-5573-b2e2-f14b9a1b7371", "Gene A Robbins", "649"],
  ["af5858df-bc1b-5144-9ba8-f281174a57b6", "Hilton W Robbins", "649"],
] as const;

test("Batch 808 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText(box);
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Benjamin Rivlin separates an immediate Army assignment from student status", async ({ page }) => {
  await page.goto("./people/da45f1c9-db00-5500-9ff9-d8987947c7b0/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Soldier-student in the Army Specialized Training Program");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Brooklyn College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("not a civilian-employer claim");
});

test("Ovid Rizzolo publishes a documented 1940 Guard affiliation without overstating sequence", async ({ page }) => {
  await page.goto("./people/d2a4aa6a-9134-5e42-81e6-35b4335cb89a/");
  const main = page.locator("main");
  await expect(main).toContainText("Company C, 113th Infantry");
  await expect(main).toContainText("New Jersey National Guard");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("high");
  await expect(main).toContainText("not shown to be the immediate predecessor");
});

test("Francis Rives remains a qualified probable identity with no employer claim", async ({ page }) => {
  await page.goto("./people/06577906-160d-54b2-a89e-11f50f748c9b/");
  const main = page.locator("main");
  await expect(main).toContainText("probably Francis Bayard Rives");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("qualified identity");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("James Roaden visibly preserves the post-OSS temporal problem", async ({ page }) => {
  await page.goto("./people/4256c2ec-1a64-593f-b9e2-9b79622555d2/");
  const main = page.locator("main");
  await expect(main).toContainText("needs temporal review");
  await expect(main).toContainText("December 1945");
  await expect(main).toContainText("after OSS dissolution");
  await expect(main).toContainText("no employment or immediate-affiliation claim is made");
});

test("Ishmael Rivera preserves the Ismael spelling conflict", async ({ page }) => {
  await page.goto("./people/f5a5e02f-d532-58d1-b717-4a24163633cf/");
  const main = page.locator("main");
  await expect(main).toContainText("needs identity review");
  await expect(main).toContainText("Ismael");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("different first-name spelling");
});

test("Edgar Robbins withholds the unlinked Gulf Oil directory candidate", async ({ page }) => {
  await page.goto("./people/d60c28cc-2f5c-5ab3-ba84-64d8a0e7ace6/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("Gulf Oil products distributor");
  await expect(main).toContainText("no indexed identifier or OSS bridge");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main.getByRole("heading", { name: "Immediate pre-OSS affiliation" })).toBeVisible();
  await expect(main.getByRole("heading", { name: "Last civilian employer before service" })).toBeVisible();
});

test("home page exposes the rebuilt Batch 808 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,571");
  await expect(home).toContainText("48.34%");
  await expect(home).toContainText("12,362");
  await expect(home).toContainText("831");
  await expect(home).toContainText("374");
  await expect(home).toContainText("10,034");
});
