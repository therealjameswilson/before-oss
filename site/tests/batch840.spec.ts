import { expect, test } from "@playwright/test";

const profiles = [
  ["60b4bb3a-f3f7-56a8-b0a2-ac6b5d60e38f", "Jacquelyn Saunders"],
  ["60d00e34-9dc8-5f57-8aec-f32cbe9f0b67", "Joan R Saunders"],
  ["d81b4b0f-b2f6-5930-a2c5-070402c4cd4a", "Merle L Saunders"],
  ["25d65df9-ab5f-5518-bf8e-0d05c64f7220", "Russell Saunders"],
  ["2fd649f1-035b-5203-939d-6e890283e97f", "Tuth T Saunders"],
  ["eefb0a86-eaf1-5795-91af-5a52d034008b", "William B Saunders"],
  ["c925c096-39b6-59b8-b317-352d5d64e0c1", "Francis A Saur"],
  ["1e5f34f1-f4c6-59a4-9e48-11271cb21fc8", "Peter Sauro"],
  ["9d09d671-cd5c-59a0-ac07-94fa40bb6643", "Frank Sauter"],
  ["ca32d904-b569-5a5e-bb78-8e16a5cd3f2b", "Mary E Sauter"],
  ["17e39884-ee7e-59c7-a8b1-c69913b895c9", "Lucien A Sauvage"],
  ["78df631a-e425-533b-b28c-f3cd43a29952", "Carleton N Savage"],
  ["1c2170de-232e-5e84-84fe-4e39bdda2891", "Dorothy E Savage"],
  ["4f1116f8-00a9-5b07-98bc-385e4a5b4bc7", "John W Savage"],
  ["2369875b-7054-58d1-81ec-0beae02a9890", "Lamar H Savage"],
  ["1d8fe536-b22c-5f29-ac4b-4d7650153111", "Richard R Savage"],
  ["4a99103b-b985-5420-ae20-d1740bb98732", "Russell W Savage"],
  ["69a1cad0-11ef-5391-9489-751d74f28539", "Harry M Savaides"],
  ["114aeded-3191-513e-9f73-18a8c275bced", "Charles V Savarese"],
  ["cd7cf9c4-69cd-5c37-9874-9cf3c1a392ca", "George A Savelli"],
  ["d0492a68-b649-572f-941e-75793e83fbfd", "Geraldine L Saville"],
  ["5845269d-e7f2-5460-bf85-6b23e3d86dc4", "Robert L Saville"],
  ["2cfcaead-58fb-5f7e-bd2d-ba8e2bfc230e", "Anthony Savino"],
] as const;

test("Batch 840 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
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

test("Peter Sauro separates Army, last civilian employment, and earlier self-employment", async ({ page }) => {
  await page.goto("./people/1e5f34f1-f4c6-59a4-9e48-11271cb21fc8/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("U.S. Army");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("Essex County Park Commission");
  await expect(main).toContainText("tree surgeon");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("self-employed in gardening and tree work");
  await expect(main).toContainText("NAID 2185127");
});

test("Carleton Savage publishes a qualified Colby College pathway", async ({ page }) => {
  await page.goto("./people/78df631a-e425-533b-b28c-f3cd43a29952/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Colby College");
  await expect(main).toContainText("instructor");
  await expect(main).toContainText("1943–1944");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("best-supported immediate pre-OSS affiliation");
  await expect(main).toContainText("personnel file has not yet been reviewed directly");
});

test("accepted Batch 840 Army crosswalks publish identity but no coded occupation", async ({ page }) => {
  for (const id of [
    "eefb0a86-eaf1-5795-91af-5a52d034008b",
    "1d8fe536-b22c-5f29-ac4b-4d7650153111",
    "4a99103b-b985-5420-ae20-d1740bb98732",
    "cd7cf9c4-69cd-5c37-9874-9cf3c1a392ca",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("protected identifier");
    await expect(main).not.toContainText("Army occupation code");
  }
});

test("Savarese conflict is visible without leaking the alternate candidate", async ({ page }) => {
  await page.goto("./people/114aeded-3191-513e-9f73-18a8c275bced/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("materially different surname");
  await expect(main).toContainText("alternate private name and protected identifier are withheld");
  await expect(main).not.toContainText("Army occupation code");
});

test("Tuth spelling and Anthony Savino note stay exactly as indexed", async ({ page }) => {
  await page.goto("./people/2fd649f1-035b-5203-939d-6e890283e97f/");
  let main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Tuth T Saunders", level: 1 })).toBeVisible();
  await expect(main).toContainText("unusual printed forename Tuth was visually confirmed");
  await expect(main).toContainText("critical");

  await page.goto("./people/2cfcaead-58fb-5f7e-bd2d-ba8e2bfc230e/");
  main = page.locator("main");
  await expect(main).toContainText("Hollas");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("Review Box 679");
});

test("unresolved Batch 840 profiles retain dignified archival guidance", async ({ page }) => {
  for (const id of [
    "60b4bb3a-f3f7-56a8-b0a2-ac6b5d60e38f",
    "60d00e34-9dc8-5f57-8aec-f32cbe9f0b67",
    "d81b4b0f-b2f6-5930-a2c5-070402c4cd4a",
    "25d65df9-ab5f-5518-bf8e-0d05c64f7220",
    "2fd649f1-035b-5203-939d-6e890283e97f",
    "c925c096-39b6-59b8-b317-352d5d64e0c1",
    "9d09d671-cd5c-59a0-ac07-94fa40bb6643",
    "ca32d904-b569-5a5e-bb78-8e16a5cd3f2b",
    "17e39884-ee7e-59c7-a8b1-c69913b895c9",
    "1c2170de-232e-5e84-84fe-4e39bdda2891",
    "4f1116f8-00a9-5b07-98bc-385e4a5b4bc7",
    "2369875b-7054-58d1-81ec-0beae02a9890",
    "69a1cad0-11ef-5391-9489-751d74f28539",
    "d0492a68-b649-572f-941e-75793e83fbfd",
    "5845269d-e7f2-5460-bf85-6b23e3d86dc4",
    "2cfcaead-58fb-5f7e-bd2d-ba8e2bfc230e",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusunresolved");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("Review Box 679");
  }
});
