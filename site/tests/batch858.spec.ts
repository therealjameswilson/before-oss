import { expect, test } from "@playwright/test";

const profiles = [
  ["b5a64790-b6b4-5dfd-8ef5-0ad5b2da59de", "Albert B Seitz"],
  ["abfbe8f9-19ce-500a-82df-8d1845dc6366", "Marguerite Seitzer"],
  ["09607ef5-092a-58ae-8e2d-ee4aa5833ec2", "John Sekela"],
  ["6435a349-610e-584b-b864-ecf61b315a13", "David S Seki"],
  ["78f6b72a-10f2-5baa-a0ae-7a01cb1d8966", "Carl A Selby"],
  ["e8bc3899-b9a6-54ec-b1fc-4c4465e5d504", "George R Selby"],
  ["6e69c934-13e0-5c9e-aab5-0a77411ac2db", "Harvey T Selee"],
  ["0b6c4490-5343-5749-88fe-da2bb4a01301", "George J Seleno"],
  ["a66a82af-226b-546c-bd4e-ea5cf9ac2d1a", "Joseph M Self"],
  ["8de6c3f4-15da-565b-b27c-a6e8bf46f0d0", "Phoehem Selig"],
  ["19595c75-4f72-5eef-af7f-cc6a8e07acd5", "Harold S Seligmann"],
  ["78d5edc6-776f-51a1-9212-ca3516d80caa", "Herbert Seligmann"],
  ["2e859538-333a-5824-aa08-4cef6aedbab8", "Bernice F Seligson"],
  ["8da481a5-3fab-55ba-a97b-b49449678e31", "Joseph P Seliquini"],
  ["19d363c0-a12c-54f1-9ae0-71e9af77ec04", "Lyle E Selix"],
  ["de7b9b61-3fe2-5f6e-b57f-e264aeac56ff", "Anthony B Sella"],
  ["fa2c14f4-8445-5f89-9116-2665219d234b", "Melvin J Sellers"],
  ["7b91d4bf-8645-5401-9d1f-b4861cd0eda3", "Donald C Sellman"],
  ["cccc7bc3-bd4d-5550-925d-0d6805f69b05", "Harry G Sells"],
  ["c7233241-c593-5db1-984f-4f6106d7b087", "Margaret A Sells"],
  ["64ee4c4c-7d96-5f8b-887d-e4c7e47cf498", "Conrad G Selvig"],
  ["38b3465a-4d37-5c05-b0a7-c3586f98e50e", "George C Selvig"],
  ["0ca4a0cf-bc3b-57e9-b116-c56b49bce632", "Helen M Selvig"],
] as const;

test("Batch 858 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Marguerite Seitzer keeps the State Department pathway distinct from civilian employment", async ({ page }) => {
  await page.goto("./people/abfbe8f9-19ce-500a-82df-8d1845dc6366/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Marguerite Osborne Seitzer");
  await expect(main).toContainText("Immediate pre-OSS affiliationUnited States Department of State");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("Marguerite 'Red' Seitzer; Arlington Resident");
  await expect(main).not.toContainText("Last civilian employer before serviceUnited States Department of State");
});

test("Joseph Seliquini has an official OSS identity without an invented employer", async ({ page }) => {
  await page.goto("./people/8da481a5-3fab-55ba-a97b-b49449678e31/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("enlisted army personnel");
  await expect(main).toContainText("OSS Italian Operational Group radio operator");
  await expect(main).toContainText("OSS in Action: The Mediterranean and European Theaters");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("George and Conrad Selvig remain separate under one opaque duplicate label", async ({ page }) => {
  for (const id of [
    "64ee4c4c-7d96-5f8b-887d-e4c7e47cf498",
    "38b3465a-4d37-5c05-b0a7-c3586f98e50e",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Duplicate groupduplicate-33ede72ab1d9");
    await expect(main).not.toContainText("variant-review:conrad-george-selvig");
  }

  await page.goto("./people/38b3465a-4d37-5c05-b0a7-c3586f98e50e/");
  const main = page.locator("main");
  await expect(main).toContainText("commissioned army officer");
  await expect(main).toContainText("Herringbone Cloak--GI Dagger: Marines of the OSS");
  await expect(main).toContainText("Yugoslav");
});

test("Helen Selvig's university evidence is student status, not employment", async ({ page }) => {
  await page.goto("./people/0ca4a0cf-bc3b-57e9-b116-c56b49bce632/");
  const main = page.locator("main");
  await expect(main).toContainText("Helen Marion Selvig");
  await expect(main).toContainText("University of Minnesota");
  await expect(main).toContainText("Student, class of 1926");
  await expect(main).toContainText("student");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).not.toContainText("Last civilian employer before serviceUniversity of Minnesota");
});

test("Army crosswalks remain identity-only and the Selee collision stays public", async ({ page }) => {
  for (const id of [
    "e8bc3899-b9a6-54ec-b1fc-4c4465e5d504",
    "0b6c4490-5343-5749-88fe-da2bb4a01301",
    "a66a82af-226b-546c-bd4e-ea5cf9ac2d1a",
    "19595c75-4f72-5eef-af7f-cc6a8e07acd5",
    "19d363c0-a12c-54f1-9ae0-71e9af77ec04",
    "7b91d4bf-8645-5401-9d1f-b4861cd0eda3",
    "cccc7bc3-bd4d-5550-925d-0d6805f69b05",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  await page.goto("./people/6e69c934-13e0-5c9e-aab5-0a77411ac2db/");
  const conflict = page.locator("main");
  await expect(conflict).toContainText("Identity statusconflicting");
  await expect(conflict).toContainText("Duplicate groupduplicate-8934959fe3b1");
  await expect(conflict).not.toContainText("serial-conflict");
});

test("Herbert Seligmann keeps the journalist lead unresolved", async ({ page }) => {
  await page.goto("./people/78d5edc6-776f-51a1-9212-ca3516d80caa/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("Review Box 695");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationOverseas News Agency");
  await expect(main).not.toContainText("Last civilian employer before serviceJewish Telegraphic Agency");
});
