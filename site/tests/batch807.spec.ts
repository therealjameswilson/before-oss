import { expect, test } from "@playwright/test";

const profiles = [
  ["39c270e4-8b8c-5562-87ee-31985bf33e8c", "Ove A Rise", "647"],
  ["91cd3d48-1c71-5882-8bd9-43eed288f190", "Stanley E Rise", "647"],
  ["ad2860fd-2064-5d1a-a6df-2b1304dbf55f", "John C Risher", "647"],
  ["5ef02020-15f2-54ef-ac0e-9b756a55b450", "Edith F Rising", "647"],
  ["8f07376b-fa97-5c14-ad21-b9440010e348", "Sarah L Rising", "647"],
  ["11679283-7b53-560e-8929-65deca1f668c", "Elizabeth Risler", "647"],
  ["a1ccf976-7c5d-5a3b-8a67-91605ae641e8", "Jack R Risler", "647"],
  ["d5e2a0ca-cdc7-56b8-b469-d7a664adfaf5", "Herschel G Rismiller", "647"],
  ["b5cc3ba4-22b2-55f4-a49f-f28d4bce577d", "Oskar Rismondo", "647"],
  ["2ea39824-5203-58e9-aa51-bb73a23a670e", "Pauline D Ritchey", "648"],
  ["75fed872-e40a-50b3-8104-37d551ee9f0b", "Alexander Ritchie", "647"],
  ["a479d0d4-ae10-5ca4-a5dd-5becd2cfd3d1", "Dolan S Ritchie", "647"],
  ["0514c9f6-c2a1-5c02-a7fb-3524af187a82", "Doris N Ritchie", "647"],
  ["62430081-0ae5-537b-a122-0ea362680e44", "Haiden Ritchie", "647"],
  ["e8465e3e-97ca-5484-8525-9129562cc3f6", "Andre J Rittener", "648"],
  ["8ed13c7a-9518-5d75-b84d-9afbab823aa3", "Alvis Ritter", "648"],
  ["de34ec47-6be6-5241-bb5c-64b9719a4fe2", "Betty H Ritter", "648"],
  ["eb14a2de-e4f1-5a7c-b900-367b60647c3d", "Mabel Ritter", "648"],
  ["7c11531d-4598-5833-8ac3-23bbb4e3180b", "Walter T Ritter Jr.", "648"],
  ["f8a65eaa-55ee-53e1-9115-89d85a586607", "Albert Ritzenberg", "648"],
  ["9359611b-81d9-580a-a214-b4cc342364da", "Simone B Riulina", "648"],
  ["d6b4ed0f-d283-5940-8f7f-fbb385066248", "William Rivchin", "648"],
  ["0a31f8b7-8300-5fc0-b0f9-2f306ceab783", "Fred R Riveglia", "648"],
] as const;

test("Batch 807 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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

test("Jack Risler has a qualified Marine-instructor-to-OSS sequence", async ({ page }) => {
  await page.goto("./people/a1ccf976-7c5d-5a3b-8a67-91605ae641e8/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Marine Corps");
  await expect(main).toContainText("Parachute instructor at New River");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("enlisted marine corps personnel");
  await expect(main).toContainText("not a civilian-employer claim");
});

test("Oskar Rismondo separates NYU student status from uncertain Army chronology", async ({ page }) => {
  await page.goto("./people/b5cc3ba4-22b2-55f4-a49f-f28d4bce577d/");
  const main = page.locator("main");
  await expect(main).toContainText("New York University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Haiden Ritchie publishes Dartmouth student status immediately before OSS", async ({ page }) => {
  await page.goto("./people/62430081-0ae5-537b-a122-0ea362680e44/");
  const main = page.locator("main");
  await expect(main).toContainText("Dartmouth College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("following graduation from Dartmouth");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Fred Riveglia publishes Army and OSS evidence without backdating postwar work", async ({ page }) => {
  await page.goto("./people/0a31f8b7-8300-5fc0-b0f9-2f306ceab783/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Paratrooper and OSS group member");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("Brown education and Pratt & Whitney employment occurred after wartime service");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("home page exposes the rebuilt Batch 807 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,548");
  await expect(home).toContainText("48.24%");
  await expect(home).toContainText("12,385");
  await expect(home).toContainText("829");
  await expect(home).toContainText("374");
  await expect(home).toContainText("10,011");
});
