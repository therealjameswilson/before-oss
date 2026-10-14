import { expect, test } from "@playwright/test";

const profiles = [
  ["0d2c95a4-3738-5c5e-a838-93b86ba81e63", "Francis R. M. Rea"],
  ["6a846dd9-b29a-5b8d-b4de-b54d826ff669", "Leo M Rea"],
  ["8fa007c3-d683-5a1b-80c6-7d8948ad1076", "Barbara H Read"],
  ["d1b224f9-97fc-5bc8-8aac-088a4f139d48", "Conyers Read"],
  ["6aa99e81-b2c4-58c9-a650-3a1e0ab27cd2", "Mary J Read"],
  ["a6459847-e0fe-5ea4-a104-af1de30c122d", "Norman W Read"],
  ["48821174-0258-58a0-937d-f80682eecc34", "Roby C Read"],
  ["1c06fd03-36b4-5fcf-ac84-f5990122cf1f", "Douglas K Reading"],
  ["05a4ebef-2e21-5ce0-97dc-ce180b3d0b81", "Betty B Ready"],
  ["b057a874-02bb-5ac5-972a-e8a6f124f4a4", "Louis M Ream"],
  ["eabdd3d6-7bd4-54c8-9f73-f45cc3c280e9", "Robert C Ream"],
  ["4ff51e76-c5b9-5bbd-90a2-8ed35eb039fa", "Arthur A Reams"],
  ["43b7dfc1-ec29-5f9d-9a19-f462dc332880", "Elinor P Reams"],
  ["bde91a47-4ee4-50e2-87b2-2e35821c377b", "Francis J Reardon"],
  ["8fc7717e-a0a9-59ed-ba43-575f99f19da0", "Hugh K Reardon"],
  ["4b0e2df8-3a5b-5b14-a380-a24a9235fbbf", "William A Reardon"],
  ["2361d7c7-edbb-57be-86bc-db0840a4b5ce", "Daniel R Reason"],
  ["fa0b23fa-7a26-5f62-b743-2b10fc463a99", "Bettie E Reasoner"],
  ["4fad4ac1-553f-52e2-860c-a2380b58ec40", "Ellis R Reasor"],
  ["c2a86d60-21ab-54cd-9160-170f901bf564", "Vincent Rebar"],
  ["b0d55f47-0fc1-57ba-966c-121599072195", "Robert R Reber"],
  ["f591b9c2-b6cb-5305-8125-4d54615467c4", "Constantino Reboa"],
  ["958d72e3-5e28-5845-bce1-470854a818ac", "Cornelia Reck"],
] as const;

test("Batch 791 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 791 publishes Reboa's last civilian affiliation without calling it immediate", async ({ page }) => {
  await page.goto("./people/f591b9c2-b6cb-5305-8125-4d54615467c4/");
  const main = page.locator("main");
  await expect(main).toContainText("Constantino Reboa");
  await expect(main).toContainText("confirmed");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Italian Merchant Marine");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Radio officer");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText("Italian Merchant Marine");
  await expect(main).toContainText("internment camp");
  await expect(main).toContainText("Hoover Institution Library & Archives");
  await expect(main).toContainText("photogra");
});

test("Batch 791 resolves Ream's OSS identity without inventing a pre-OSS employer", async ({ page }) => {
  await page.goto("./people/b057a874-02bb-5ac5-972a-e8a6f124f4a4/");
  const main = page.locator("main");
  await expect(main).toContainText("Louis M Ream");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("deputy director for administrative services");
  await expect(main).toContainText("National Park Service");
  await expect(main).toContainText("archival review");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText("New York Trust");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText("Princeton");
});

test("Batch 791 preserves the page 385 clipped index notes", async ({ page }) => {
  for (const [id, note] of [
    ["0d2c95a4-3738-5c5e-a838-93b86ba81e63", "Record"],
    ["6a846dd9-b29a-5b8d-b4de-b54d826ff669", "Dental Id"],
    ["4ff51e76-c5b9-5bbd-90a2-8ed35eb039fa", "Name pl"],
    ["958d72e3-5e28-5845-bce1-470854a818ac", "photogra"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText(note);
  }
});

test("home page exposes the rebuilt Batch 791 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,189");
  await expect(home).toContainText("46.74%");
  await expect(home).toContainText("12,745");
  await expect(home).toContainText("808");
  await expect(home).toContainText("362");
  await expect(home).toContainText("9,649");
});
