import { expect, test } from "@playwright/test";

const profiles = [
  ["3bba56cc-ed72-5305-8236-afa131e8e952", "Daniel E Murphy"],
  ["0df768fd-3eeb-5b43-94ca-e95d6d429f73", "Dorothy C Murphy"],
  ["5e443cb2-57cb-5004-84eb-6d3fb191285d", "Edward J Murphy"],
  ["ec743fdb-8de5-55b0-8c74-3f383bb857f5", "Gerald R Murphy"],
  ["a4af0bb1-fdf5-5d16-8310-77cfde04bcce", "Ione M Murphy"],
  ["523cba56-b1b7-5eac-8c1e-635a3556b446", "James H Murphy"],
  ["c7f766eb-3d2f-5da9-a9f6-9880cfa0f1db", "James R Murphy"],
  ["de7cdf23-ddc9-520e-b0d1-bf8fa4f38e8d", "John A Murphy"],
  ["2fafa83f-bb32-5e2d-9d18-eac12b5013e3", "John J Murphy"],
  ["f4218c56-5ec6-53ae-8558-bce6b87773a9", "John D Murphy"],
  ["250c1df9-ec52-53ba-9fc3-27f2baa7b4f9", "John R Murphy"],
  ["21cf2b5f-13a2-53f5-adf2-88b7746a8454", "Joseph Murphy"],
  ["93f8417e-3f92-592a-abd0-4aecbb84e879", "Rex R Murphy"],
  ["58585f10-8ca4-5133-83da-7eda533a94d3", "Thomas R Murphy"],
  ["1a149254-702b-5180-966e-e10df38cb557", "Virginia R Murphy"],
  ["5385d453-4e9e-59be-9131-cde48c34a707", "Warren G Murphy"],
  ["f0b796c7-497e-5e7e-895f-5ec041f68b8c", "William B Murphy"],
  ["4b08870e-4487-5c4f-82c3-8d6cd872913b", "Willis A Murphy"],
  ["0a9cfd66-0113-5e2f-afbb-8fd68d9ed037", "Albert E Murray"],
  ["f7f7eb5a-bc82-565c-821b-1c7a23097bf5", "Cathleen Murray"],
  ["ffb7de36-8c56-5258-b2e6-a2d49d5b3773", "Emmett L Murray"],
  ["18c830b0-a43c-5c8c-879d-83a110ab0e92", "Guy E Murray"],
  ["2fe06c19-7390-5708-b875-65a4e7be5e90", "Harry A Murray"],
] as const;

test("Batch 689 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Page 335");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 689 publishes James R Murphy's immediate private practice and last civilian employer", async ({ page }) => {
  await page.goto("./people/c7f766eb-3d2f-5da9-a9f6-9880cfa0f1db/");
  const main = page.locator("main");
  await expect(main).toContainText("James Russell Murphy");
  await expect(main).toContainText("high confidence");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("Self-employed legal practice");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("Self-employed legal practice");
  await expect(main).toContainText("Attorney in private practice");
  await expect(main).toContainText("spring 1941");
  await expect(main.locator('a[href="https://www.dni.gov/files/NCSC/documents/ci/CI_Reader_Vol2.pdf"]')).toHaveCount(2);
  await expect(main.locator('a[href^="https://www.washingtonpost.com/archive/local/1986/10/09/"]')).toHaveCount(2);
  await expect(main).not.toContainText("Cross, Murphy, Smuck and Houston");
});

test("Batch 689 keeps six Army matches as identities without inventing employers", async ({ page }) => {
  for (const id of [
    "21cf2b5f-13a2-53f5-adf2-88b7746a8454",
    "93f8417e-3f92-592a-abd0-4aecbb84e879",
    "58585f10-8ca4-5133-83da-7eda533a94d3",
    "5385d453-4e9e-59be-9131-cde48c34a707",
    "ffb7de36-8c56-5258-b2e6-a2d49d5b3773",
    "2fe06c19-7390-5708-b875-65a4e7be5e90",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 689 preserves Albert E Murray's record conflict and truncated note", async ({ page }) => {
  await page.goto("./people/0a9cfd66-0113-5e2f-afbb-8fd68d9ed037/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("malformed Army record");
  await expect(main).toContainText("Refer to");
  await expect(main).toContainText("truncated");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(main).not.toContainText(/\b\d{8}\b/);
});

test("Batch 689 retains the literal Ione M Murphy note without expanding it", async ({ page }) => {
  await page.goto("./people/a4af0bb1-fdf5-5d16-8310-77cfde04bcce/");
  const main = page.locator("main");
  await expect(main).toContainText("also AS");
  await expect(main).toContainText("truncated");
  await expect(main).not.toContainText("also Army Service");
});

test("Batch 689 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("8,896");
  await expect(body).toContainText("37.16%");
  await expect(body).toContainText("311");
  await expect(body).toContainText("15,038");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
