import { expect, test } from "@playwright/test";

const profiles = [
  ["96b934f9-7e05-534c-97dd-789e43f8b3b9", "Robert Scott"],
  ["00b75765-8f91-5477-8477-37e63bfb9cb6", "Winston M Scott"],
  ["432d4ea2-8310-5a4c-ae12-3d0b867144b5", "Jean B Scotto"],
  ["b9a25cce-0aa3-539f-97b8-40e5c9aec69d", "Charles B Scovil"],
  ["9981b409-2e68-53f9-a5ec-061caec7e237", "Antonio Sechi"],
  ["fc894859-68dc-5e8e-afd7-60d2438b994f", "Fred R Sechler"],
  ["aa68b100-2d31-5901-8c9f-4a4b855d1da0", "Henry Sechter"],
  ["7fb063e2-ae04-5a2b-996c-8e209a485a32", "Peter A Seckan"],
  ["27512a6f-36ca-53dc-b4ed-3e524228de2e", "Elizabeth D Secrest"],
  ["0c300974-a21d-5078-bc50-3a8c62dcd73f", "James Securanza"],
  ["8efd92ad-8086-5e6d-a1ac-85fe77c89061", "Walter A Seder"],
  ["07b335b3-db24-5184-97da-0f7ba153a2c1", "Wilfred E Sederholm"],
  ["f823a4c6-d0b1-5e09-97b6-372e5cd79342", "Theodora Sedgwick"],
  ["27834dc4-11bd-5c45-bde6-3fb2d5cf857e", "Thomas I Sedgwick"],
  ["650e50d6-8aed-50cf-821f-9de72a5b43f8", "William C Seeger"],
  ["809b2883-304f-54f5-b029-59d1e7d8eb7e", "William J Seeger"],
  ["d27fc85f-451a-57a1-827b-ea0b786a930a", "Caroline H Seeley"],
  ["862684e7-9f70-57fd-b398-709b2743189c", "Jay Seeley"],
  ["ccca912f-af73-54a3-ab3a-c70701c1c992", "Robert G Seeley"],
  ["6bc3f019-62bd-5a17-9d74-8f2d8059f9ef", "Albert L Seely"],
  ["4cc6f9dc-f384-546e-83c5-85d941c85f43", "Jay S Seely"],
  ["150753e4-19dc-51f0-a280-9b7a243259b7", "Dorothea C Seelye"],
  ["db93e2a2-76d3-5bfa-9924-9986c4668170", "Helen Seeman"],
] as const;

test("Batch 856 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("the seven Army matches publish identity bridges but no invented employers", async ({ page }) => {
  const matches = [
    ["9981b409-2e68-53f9-a5ec-061caec7e237", "Antonio Sechi"],
    ["fc894859-68dc-5e8e-afd7-60d2438b994f", "Fred R Sechler"],
    ["7fb063e2-ae04-5a2b-996c-8e209a485a32", "Peter A Seckan"],
    ["8efd92ad-8086-5e6d-a1ac-85fe77c89061", "Walter A Seder"],
    ["07b335b3-db24-5184-97da-0f7ba153a2c1", "Wilfred E Sederholm"],
    ["27834dc4-11bd-5c45-bde6-3fb2d5cf857e", "Thomas I Sedgwick"],
    ["ccca912f-af73-54a3-ab3a-c70701c1c992", "Robert G Seeley"],
  ] as const;

  for (const [id, name] of matches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("requires archival review");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("Identity crosswalk only");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main.getByRole("heading", { name: /Army Serial Number/i })).toHaveCount(0);
    await expect(main).toContainText(name);
  }
});

test("Winston Scott separates immediate government service from the last civilian employer", async ({ page }) => {
  await page.goto("./people/00b75765-8f91-5477-8477-37e63bfb9cb6/");
  const main = page.locator("main");
  await expect(main.getByRole("heading", { name: "Immediate pre-OSS affiliation" })).toBeVisible();
  await expect(main).toContainText("Federal Bureau of Investigation");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("explicit immediate");
  await expect(main.getByRole("heading", { name: "Last civilian employer before service" })).toBeVisible();
  await expect(main).toContainText("University of Alabama");
  await expect(main).toContainText("Teacher of mathematics");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("The Intelligence Officer's Bookshelf");
});

test("documented teaching and education remain qualified by relationship type", async ({ page }) => {
  await page.goto("./people/862684e7-9f70-57fd-b398-709b2743189c/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Anatolia College");
  await expect(main).toContainText("employment");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("A single last civilian employer");

  await page.goto("./people/150753e4-19dc-51f0-a280-9b7a243259b7/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Bryn Mawr College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/f823a4c6-d0b1-5e09-97b6-372e5cd79342/");
  main = page.locator("main");
  await expect(main).toContainText("Radcliffe College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("duplicate and conflict cases remain separate with opaque public labels", async ({ page }) => {
  for (const id of [
    "862684e7-9f70-57fd-b398-709b2743189c",
    "4cc6f9dc-f384-546e-83c5-85d941c85f43",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("Duplicate groupduplicate-12defbf745ca");
  }

  await page.goto("./people/0c300974-a21d-5078-bc50-3a8c62dcd73f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Duplicate groupduplicate-02bf7471aba1");
  await expect(main).toContainText("Compare James Securanza in Box 694 with James P. Sicuranza in Box 709");
  await expect(main).not.toContainText("serial-conflict:");
});
