import { expect, test } from "@playwright/test";

const profiles = [
  ["59c07578-ea9f-5a68-bafa-14c853a7e6b1", "Gustave A Mueller"],
  ["2e04fc10-f5a7-5229-b266-3f436b802920", "Johanna B Mueller"],
  ["7230fd63-18fd-58f3-86d9-d696786aaa80", "Walter J Mueller"],
  ["22c9d34f-9213-5249-9edc-08fcc010ebba", "William A Mueller"],
  ["cfb11d4f-1c01-5521-b23c-a6df00b8acea", "William L Mueller"],
  ["e58c8be6-1451-506a-8328-1588b4f71cc8", "William M Mueller"],
  ["75f36574-3b8a-5c01-82ed-a8cc3798ae01", "John P Muench"],
  ["fa7486b4-cb4b-5f4f-a0b3-890479cd2545", "Elinor L Muenster"],
  ["483ede05-cfab-5456-8524-250d64b6a5f8", "Armando J Muglia"],
  ["52477369-a91f-5141-9b04-f0488864eaf9", "Edward E Muhs"],
  ["975e428b-9bbc-58f7-87e8-8979e84898a6", "Wallace S Mukai"],
  ["08492c71-dd10-56c4-af0c-e89f93de1fb8", "Gust Mukanos"],
  ["2377892d-5cba-5ec6-a791-129426c303f2", "Stanley L Mulare"],
  ["c43ce51d-19bb-515e-b356-16b526f8234c", "Donald V Mulcahy"],
  ["fa2dfee3-8be7-58f3-90e0-fa237f26d3ba", "Francis J Mulcahy"],
  ["fb1dd164-0ace-51a0-9d66-302c1bc13203", "William L Mulcahy"],
  ["ce3eed28-b672-56ba-9b90-689ab9881292", "Cornelius A Mulder"],
  ["a56422d9-b962-53f0-ac31-cf3b4e17968a", "John L Mulford"],
  ["e4c77aa0-ddf6-57cd-924b-c2d88a3b98c7", "Mary J Mulford"],
  ["4f7f8728-2cc8-564b-9de0-9bfc1499fd40", "James L Mulhen"],
  ["0bca3d05-d716-5948-94a2-bd6b2393f9b2", "Joseph J Mulhern"],
  ["2811fd0e-bc4c-5eef-a726-b02a9600dcb1", "Jean A Mull"],
  ["73ee8649-cc5e-5db5-a966-e91777ca6dcb", "George E Mullaney"],
] as const;

const armyIdentities = [
  "75f36574-3b8a-5c01-82ed-a8cc3798ae01",
  "483ede05-cfab-5456-8524-250d64b6a5f8",
  "975e428b-9bbc-58f7-87e8-8979e84898a6",
  "08492c71-dd10-56c4-af0c-e89f93de1fb8",
  "fb1dd164-0ace-51a0-9d66-302c1bc13203",
  "ce3eed28-b672-56ba-9b90-689ab9881292",
  "a56422d9-b962-53f0-ac31-cf3b4e17968a",
  "73ee8649-cc5e-5db5-a966-e91777ca6dcb",
] as const;

test("Batch 686 publishes all 23 direct profile routes with terminal research outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Page 333");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 686 publishes eight bounded Army identities without inventing employers", async ({ page }) => {
  for (const id of armyIdentities) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 686 identifies John Louis Mulford but excludes his postwar tire company", async ({ page }) => {
  await page.goto("./people/a56422d9-b962-53f0-ac31-cf3b4e17968a/");
  const main = page.locator("main");
  await expect(main).toContainText("John Louis Mulford");
  await expect(main).toContainText("South Jersey Times");
  await expect(main).toContainText("Mulford Tire Company");
  await expect(main).toContainText("postwar");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("Mulford Tire");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("Mulford Tire");
});

test("Batch 686 keeps Gust Mukanos's OSS unit context out of the pre-OSS affiliation sections", async ({ page }) => {
  await page.goto("./people/08492c71-dd10-56c4-af0c-e89f93de1fb8/");
  const main = page.locator("main");
  await expect(main).toContainText("Greek Operational Group V");
  await expect(main).toContainText("OSS service context");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("Greek Operational Group V");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("Greek Operational Group V");
});

test("Batch 686 updates exact coverage while preserving the evidence-scoped oil category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("8,827");
  await expect(body).toContainText("36.87%");
  await expect(body).toContainText("308");
  await expect(body).toContainText("15,107");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
