import { expect, test } from "@playwright/test";

const profiles = [
  ["a578c96b-7546-5e0b-92ed-e7517aecd9f1", "Donald Nicholson"],
  ["b1e59c69-37cf-53d9-9857-18e7bfa5d57f", "Earl J Nicholson"],
  ["1b9d4b46-d06c-5f55-a075-6ba1e32f5294", "Emrich Nicholson"],
  ["77244e29-632e-5877-97f8-a2a5decb9fb6", "Guy H Nicholson"],
  ["04c6eb5a-05a2-504c-afeb-026e778dcdb9", "Kathleen J Nicholson"],
  ["e14b3fcc-508c-5f9e-9edc-e7bc9a4acee5", "R M Nicholson"],
  ["015c8153-ad2f-50fe-b8a1-0a9100e0e47d", "Mary L Nickel"],
  ["a2bfdc41-bd20-5c3e-99af-c9d1c1569566", "Linda A Nickl"],
  ["d24bbe98-d5f3-5197-83fd-adb49352eabb", "Cornelia E Nicklas"],
  ["efc51e6b-07ed-5930-985b-487eb8faa3e6", "Harry G Nickles"],
  ["d5edf4fa-d3e6-5fd4-ba9a-b91b72d2edf7", "Peter G Nickles"],
  ["d8280b6c-ed0c-5643-b091-36efe67b148b", "Miriam D Nicklin"],
  ["c0bd475d-6254-5558-93a4-c2f5e75d984b", "Nick J Nickolas"],
  ["c58c3b3a-3d50-5cd4-ada3-31b1f9d60c49", "George A Nickolodoulos"],
  ["4d2bc504-3b27-5aca-9bf4-8522dbfc8362", "Meredith Z Nicodemus"],
  ["7eb70f5c-ff35-5a3b-94e3-f5df592a28b6", "Helen O Nicol"],
  ["64f73d8d-4372-59f0-b43b-669dc00eb833", "Frederick B Nicola"],
  ["fbf9d525-7852-5027-8e9e-7d05990ac84c", "Eugene B Nicolaisen"],
  ["c8dbf165-7169-54aa-99e7-98d55a4c7228", "John M Nicolich"],
  ["929edc5e-97f6-5a0b-81ed-476548ecb527", "George K Nicolopoulos"],
  ["bec4d5c2-bdf9-5dd1-b2be-c911023b32e3", "Franko M Nicotri"],
  ["5eb2a538-66e6-58b5-97f4-2b3adef7e32e", "Gaspare Nicotri"],
  ["48ec0479-5f93-5b8a-99f7-c4d5dcb655f7", "Jack B Niedner"],
] as const;

test("Batch 704 publishes all 23 direct profile routes with reviewed outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{6,8}$/);
  }
});

test("Batch 704 qualifies Emrich Nicholson's documented prewar design work", async ({ page }) => {
  await page.goto("./people/1b9d4b46-d06c-5f55-a075-6ba1e32f5294/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Otto Kuhler's design office");
  await expect(main).toContainText("Chief designer");
  await expect(main).toContainText("Emrich Nicholson's freelance design practice");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 704 confirms Harry Nickles without turning his OSS assignment into prehistory", async ({ page }) => {
  await page.goto("./people/efc51e6b-07ed-5930-985b-487eb8faa3e6/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("commissioned naval officer");
  await expect(main).toContainText("USNR");
  await expect(main).toContainText("Security Officer for Istanbul");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 704 separates Gaspare Nicotri's occupation and authorship from employment", async ({ page }) => {
  await page.goto("./people/5eb2a538-66e6-58b5-97f4-2b3adef7e32e/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("lawyer, educator, and writer");
  await expect(main).toContainText("La Parola");
  await expect(main).toContainText("Contributing author");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 704 keeps duplicate and spelling conflicts visible", async ({ page }) => {
  await page.goto("./people/b1e59c69-37cf-53d9-9857-18e7bfa5d57f/");
  await expect(page.locator("main")).toContainText("Identity statusambiguous");
  await expect(page.locator("main")).toContainText("Earl J Nichelson");

  await page.goto("./people/c8dbf165-7169-54aa-99e7-98d55a4c7228/");
  await expect(page.locator("main")).toContainText("Identity statusambiguous");
  await expect(page.locator("main")).toContainText("Nicolich or Nicholich rows");

  await page.goto("./people/c58c3b3a-3d50-5cd4-ada3-31b1f9d60c49/");
  await expect(page.locator("main")).toContainText("George A Nickolopoulos");

  await page.goto("./people/bec4d5c2-bdf9-5dd1-b2be-c911023b32e3/");
  await expect(page.locator("main")).toContainText("Franco Mario Nicotri");
});

test("Batch 704 updates exact coverage while preserving the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,231");
  await expect(main).toContainText("38.56%");
  await expect(main).toContainText("319");
  await expect(main).toContainText("14,703");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
