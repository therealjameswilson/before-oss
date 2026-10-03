import { expect, test } from "@playwright/test";

const profiles = [
  ["ee48651b-0a41-525f-b101-ddcee05d1250", "Charlotte Morrill"],
  ["6557df06-a8b5-5b19-9fbd-4666a96c0f88", "Daniel E Morris"],
  ["59f173b7-14e6-5d24-84d8-1d0ff4a0cd05", "Ethel V Morris"],
  ["ef082d99-61c0-5832-abc3-f61f415af2ca", "Jacquelyn P Morris"],
  ["a51c279b-f60f-5a25-acd2-d69fb1258da7", "John E Morris"],
  ["8e651acd-1a9e-569d-b63d-3f8446683604", "John F Morris"],
  ["714fdb95-6b2b-5e13-a6e5-901d7340790f", "John P Morris"],
  ["c7fa01df-ec55-59c4-a800-eb79624065b4", "John T Morris"],
  ["e95a8794-b5f3-5715-a549-7bd0d1ba7ae7", "Leland C Morris"],
  ["eba9f0e6-f7cb-5492-943a-f210e9fee0af", "Louise P Morris"],
  ["ad6bfc7f-5479-558c-be0f-e981596bc25f", "Sara N Morris"],
  ["6d029516-fb8d-51b4-beec-e85ef406ad1c", "Thomas E Morris"],
  ["59674a03-df58-5599-897c-bf60bb7e5e1d", "Virginia L Morris"],
  ["a6cc2f60-4833-503a-af18-e8478650e319", "Donald J Morrisey"],
  ["09766766-15bc-5bd1-acbb-0396be657f79", "Donald F Morrison"],
  ["e9196030-2f7b-5c6a-b880-b2da7338f973", "Edward S Morrison"],
  ["3d8e8919-d041-5659-a838-28f389a64a38", "Elbie E Morrison"],
  ["f51002b8-e7b4-527e-8539-051ddbb64b7a", "Frances C Morrison"],
  ["a33a0a5c-83c1-5731-8007-4628e162af41", "H. G Morrison Jr."],
  ["27b1c1cb-c448-5bfd-8bd0-e0610a34ecb8", "Hubert G Morrison"],
  ["57d00854-be39-5521-8e7a-cc16cfa1e5de", "Hugh P Morrison"],
  ["ce2a9689-aef0-5a11-845e-3a5d6facbc4e", "Phoebe Morrison"],
  ["228f10b9-ca71-5d01-ab38-f40aeb4c2133", "Robert S Morrison"],
] as const;

const highConfidenceArmyMatches = [
  ["a51c279b-f60f-5a25-acd2-d69fb1258da7", "John E Morris"],
  ["8e651acd-1a9e-569d-b63d-3f8446683604", "John F Morris"],
  ["714fdb95-6b2b-5e13-a6e5-901d7340790f", "John P Morris"],
  ["6d029516-fb8d-51b4-beec-e85ef406ad1c", "Thomas E Morris"],
  ["a6cc2f60-4833-503a-af18-e8478650e319", "Donald J Morrisey"],
  ["e9196030-2f7b-5c6a-b880-b2da7338f973", "Edward S Morrison"],
  ["57d00854-be39-5521-8e7a-cc16cfa1e5de", "Hugh P Morrison"],
  ["228f10b9-ca71-5d01-ab38-f40aeb4c2133", "Robert S Morrison"],
] as const;

test("Batch 680 publishes all 23 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 330");
    await expect(page.locator("main")).toContainText("Archive box");
    await expect(page.locator("main")).toContainText("539");
  }
});

test("Batch 680 publishes eight high-confidence Army identities without employer inference", async ({ page }) => {
  for (const [id, name] of highConfidenceArmyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("coded occupation remain private");
  }
});

test("Batch 680 publishes Phoebe Morrison's qualified Yale employment", async ({ page }) => {
  await page.goto("./people/ce2a9689-aef0-5a11-845e-3a5d6facbc4e/");
  const main = page.locator("main");
  const immediateAffiliation = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilianEmployer = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Yale Law School");
  await expect(main).toContainText("Research Associate in International Law");
  await expect(main).toContainText("assistant professor");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("Oral History Interview: Mary Gardiner Jones");
  await expect(main).toContainText("Legal Problems in the Far Eastern Conflict");
  await expect(immediateAffiliation).not.toContainText("Yale Law School");
  await expect(civilianEmployer).not.toContainText("Yale Law School");
});

test("Batch 680 preserves the Hubert and H. G. Morrison conflict without merging", async ({ page }) => {
  await page.goto("./people/27b1c1cb-c448-5bfd-8bd0-e0610a34ecb8/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("H G Morrison Junior");
  await expect(main).toContainText("adjacent");
  await expect(main).toContainText("Box 539");
  await expect(main).not.toContainText("Verified employer");

  await page.goto("./people/a33a0a5c-83c1-5731-8007-4628e162af41/");
  main = page.locator("main");
  await expect(main).toContainText("ambiguous");
  await expect(main).toContainText("Hubert G Morrison");
  await expect(main).toContainText("do not merge");
  await expect(main).toContainText("requires archival review");
});

test("Batch 680 records terminal no-result outcomes without implying no prior employment", async ({ page }) => {
  for (const id of [
    "ee48651b-0a41-525f-b101-ddcee05d1250",
    "6557df06-a8b5-5b19-9fbd-4666a96c0f88",
    "59f173b7-14e6-5d24-84d8-1d0ff4a0cd05",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("no reliable result after protocol");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText("539");
  }
});

test("Batch 680 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,692");
  await expect(page.locator("body")).toContainText("36.31%");
  await expect(page.locator("body")).toContainText("306");
  const category = page.locator("#oil-companies");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator(".oil-directory__person")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil companies");

  await page.goto("./people/");
  const directoryCategory = page.locator(".featured-directory-category");
  await expect(directoryCategory.locator("li")).toHaveCount(8);
});
