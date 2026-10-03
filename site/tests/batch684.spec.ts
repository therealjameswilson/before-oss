import { expect, test } from "@playwright/test";

const profiles = [
  ["dc0d05b5-98dc-590a-ac4f-301bdf2e795d", "Albert Moulton"],
  ["49664a9e-3fb2-5677-81d2-c5b5fd993bb6", "Ruth N Moulton"],
  ["99cf4545-e9d7-500f-8524-b5e3d6b78ff6", "Thomas T Moulton"],
  ["832ac295-99ba-5899-b841-78264d9ff394", "Andre G Mourqet"],
  ["e38b7ca7-7043-5e50-a045-83279d234d22", "Cleo C Mouser"],
  ["a4270213-f53d-5479-8944-7d4e8264dbac", "Leonidas Mousetis"],
  ["0adc9202-0cb1-5ecb-b6cc-cfa14f8ca913", "Andrew S Mousilinas"],
  ["4498c60c-abbd-5c9f-8e28-56159bd7d5c1", "Fernand F Mousis"],
  ["dcb0e404-3457-51f0-93f3-fd63db70c463", "Gaston Mousis"],
  ["2a27781a-4c74-50c5-8ffd-a9d0551b7d79", "Frederick O Moussean"],
  ["d2b82375-a4b9-5a56-9d96-185b99791242", "Chris G Moustakis"],
  ["6bb57757-f7a3-5276-a2e9-a23ffd233929", "Therese Mouzon"],
  ["d6caa166-febb-5212-9cf7-6418bea8dac6", "Chin M Mow"],
  ["efc9a046-5234-5024-8f40-39772b821937", "Betty J Mowery"],
  ["e772314b-dca8-5952-9e9c-5185264b68c1", "John A Mowinckel"],
  ["055d95d7-8745-5dfd-82ec-f30575f729e5", "John W Mowinckel"],
  ["0ac453d8-2b63-5d38-a573-ea42f578a568", "Frank Mowinski"],
  ["962cbbf4-5f63-5153-8b6f-7f4fb4efb064", "Arno D Mowitz Jr."],
  ["ea849814-12a1-5d15-b640-78d9efbff2ce", "Edgar A Mowrer"],
  ["21726b44-4cab-54f6-8460-a81a3934fc71", "Orval H Mowser"],
  ["bebf9fe5-7985-57a3-989b-66ed9cc32f03", "Clarence Moy"],
  ["871a830a-051e-5056-9298-66c205a2d79d", "James T Moy"],
  ["29e36d44-64eb-5e3c-a21a-200471da491a", "Leon L Moye"],
] as const;

test("Batch 684 publishes all 23 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 332");
    await expect(page.locator("main")).toContainText("Archive box");
  }
});

test("Batch 684 adds John A Mowinckel to the oil category without overstating immediacy", async ({ page }) => {
  await page.goto("./people/e772314b-dca8-5952-9e9c-5185264b68c1/");
  const main = page.locator("main");
  await expect(main).toContainText("Standard Oil Company of New Jersey");
  await expect(main).toContainText("Head of European operations");
  await expect(main).toContainText("documented prewar");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("Standard Oil");

  await page.goto("./");
  const homeCategory = page.locator("#oil-companies");
  await expect(homeCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(homeCategory).toContainText("11 historically named oil companies");
  await expect(homeCategory).toContainText("John A Mowinckel");

  await page.goto("./people/");
  await expect(page.locator(".featured-directory-category li")).toHaveCount(9);
  await expect(page.locator(".featured-directory-category")).toContainText("John A Mowinckel");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(9);
  await expect(page.locator("main")).toContainText("John A Mowinckel");
  await expect(page.locator("main")).toContainText("Standard Oil Company of New Jersey");
});

test("Batch 684 keeps John W Mowinckel's military and student pathways separate from his father", async ({ page }) => {
  await page.goto("./people/055d95d7-8745-5dfd-82ec-f30575f729e5/");
  const main = page.locator("main");
  await expect(main).toContainText("John Wallendahl Mowinckel");
  await expect(main).toContainText("United States Marine Corps Reserve");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("Princeton University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("commissioned marine corps officer");
  await expect(main).not.toContainText("Standard Oil Company of New Jersey");
});

test("Batch 684 preserves the Mourqet-Mourquet conflict without exposing full identifiers", async ({ page }) => {
  await page.goto("./people/832ac295-99ba-5899-b841-78264d9ff394/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Andre G Mourqet");
  await expect(main).toContainText("Andre G Mourquet");
  await expect(main).toContainText("one-digit-different");
  await expect(main).not.toContainText(/\b\d{8}\b/);
});

test("Batch 684 preserves four official-record name conflicts", async ({ page }) => {
  const conflicts = [
    ["0adc9202-0cb1-5ecb-b6cc-cfa14f8ca913", "Andrew S Mousilinas", "Andrew S Mousalimas"],
    ["2a27781a-4c74-50c5-8ffd-a9d0551b7d79", "Frederick O Moussean", "Frederick O Mousseau"],
    ["0ac453d8-2b63-5d38-a573-ea42f578a568", "Frank Mowinski", "Clyde E White"],
    ["962cbbf4-5f63-5153-8b6f-7f4fb4efb064", "Arno D Mowitz Jr.", "Arno P Mowitz Jr."],
  ] as const;

  for (const [id, indexed, variant] of conflicts) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("conflicting");
    await expect(main).toContainText(indexed);
    await expect(main).toContainText(variant);
  }
});

test("Batch 684 publishes bounded identity findings without inventing employers", async ({ page }) => {
  for (const id of [
    "d6caa166-febb-5212-9cf7-6418bea8dac6",
    "871a830a-051e-5056-9298-66c205a2d79d",
    "ea849814-12a1-5d15-b640-78d9efbff2ce",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 684 publishes Therese Mouzon's variants but no employer", async ({ page }) => {
  await page.goto("./people/6bb57757-f7a3-5276-a2e9-a23ffd233929/");
  const main = page.locator("main");
  await expect(main).toContainText("Thérèse Joséphine Mouzon");
  await expect(main).toContainText("Thérèse André");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 684 qualifies Clarence Moy's Army pathway and civilian employer", async ({ page }) => {
  await page.goto("./people/bebf9fe5-7985-57a3-989b-66ed9cc32f03/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Territory of Hawaii Department of Institutions");
  await expect(main).toContainText("Social worker");
  await expect(main).toContainText("medium confidence");
});

test("Batch 684 keeps Leon Moye's Atlanta Gas Light lead out of public affiliations", async ({ page }) => {
  await page.goto("./people/29e36d44-64eb-5e3c-a21a-200471da491a/");
  const main = page.locator("main");
  await expect(main).toContainText("unresolved");
  await expect(main).toContainText("exact-name lead");
  await expect(main).toContainText("Atlanta Gas Light Company");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("Atlanta Gas Light");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("Atlanta Gas Light");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 684 updates exact coverage counts", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("8,781");
  await expect(body).toContainText("36.68%");
  await expect(body).toContainText("308");
  await expect(body).toContainText("15,153");
});
