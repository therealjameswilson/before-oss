import { expect, test } from "@playwright/test";

const profiles = [
  ["8d283782-a513-5230-bdc0-364108032904", "Grover C Moran", "536"],
  ["45216897-b9ce-59ee-bb1e-0cd8f74e7a81", "James H Moran", "536"],
  ["dc3deaad-90fc-5dac-a12d-9668a2004f11", "James P Moran", "536"],
  ["4f081029-3fe9-5fad-b4f2-d3507619b966", "James R Moran", "536"],
  ["8e9fd923-844e-5085-97e6-a0470f789d02", "Lawrence J Moran", "536"],
  ["06d1c901-10f9-57b1-adad-87aaf6c99d95", "Lester W Moran", "536"],
  ["43ea30c9-0f94-50ca-9693-52f076f5c04d", "Vincent P Moran", "536"],
  ["3e2b7fe2-2c93-5061-97bf-6ff8e7611539", "William S Moran", "536"],
  ["af795873-3f55-5684-b8c0-97ea7cc9bff9", "William E Moran", "536"],
  ["2bcbe463-e458-5fb4-85a9-0b71409c4ee9", "William J Moran", "536"],
  ["24223730-0694-556e-9011-f8814a07757c", "William J Moravansky", "537"],
  ["514b026b-79f4-5f38-8030-ff2db7e80f2b", "Frantisek Moravec", "537"],
  ["166373e3-7e6d-53b8-9338-d5827d97e9d7", "Edwin J Morby", "537"],
  ["d2c2dae0-c529-5e82-9c6d-6aa81f51339e", "Paul Morch", "537"],
  ["a1a84ce0-5053-5f29-9196-c2095378e810", "Wesley C Morck", "537"],
  ["51d58faa-c950-5c23-9b15-e5a3e3ff57e0", "William M Morcock", "537"],
  ["79e4357d-a18b-548e-963c-4984a5e8991f", "Herbert T Morcom", "537"],
  ["a13de9e5-a321-57cb-b821-0c448f3a1c5f", "Theodore A Morde", "537"],
  ["3dbf9882-0ca2-5014-8279-2f113db5efab", "Robert W More", "537"],
  ["c74fe740-5b07-57e0-869f-07e5c73d03df", "Daniel A Morea", "537"],
  ["54c3b26f-f14f-5d83-94a7-5b0961294507", "Gregory L Moreau", "537"],
  ["124e850d-0794-5705-949f-2998c93d4fec", "Pierre Moreau", "537"],
] as const;

const armyMatches = [
  ["dc3deaad-90fc-5dac-a12d-9668a2004f11", "James P Moran", "048"],
  ["06d1c901-10f9-57b1-adad-87aaf6c99d95", "Lester W Moran", "788"],
  ["24223730-0694-556e-9011-f8814a07757c", "William J Moravansky", "794"],
  ["51d58faa-c950-5c23-9b15-e5a3e3ff57e0", "William M Morcock", "992"],
  ["c74fe740-5b07-57e0-869f-07e5c73d03df", "Daniel A Morea", "340"],
  ["54c3b26f-f14f-5d83-94a7-5b0961294507", "Gregory L Moreau", "175"],
] as const;

const duplicateConflicts = [
  ["45216897-b9ce-59ee-bb1e-0cd8f74e7a81", "James H Moran"],
  ["4f081029-3fe9-5fad-b4f2-d3507619b966", "James R Moran"],
  ["3e2b7fe2-2c93-5061-97bf-6ff8e7611539", "William S Moran"],
  ["2bcbe463-e458-5fb4-85a9-0b71409c4ee9", "William J Moran"],
] as const;

const unresolved = [
  ["8d283782-a513-5230-bdc0-364108032904", "Grover C Moran"],
  ["8e9fd923-844e-5085-97e6-a0470f789d02", "Lawrence J Moran"],
  ["43ea30c9-0f94-50ca-9693-52f076f5c04d", "Vincent P Moran"],
  ["af795873-3f55-5684-b8c0-97ea7cc9bff9", "William E Moran"],
  ["166373e3-7e6d-53b8-9338-d5827d97e9d7", "Edwin J Morby"],
  ["d2c2dae0-c529-5e82-9c6d-6aa81f51339e", "Paul Morch"],
  ["3dbf9882-0ca2-5014-8279-2f113db5efab", "Robert W More"],
  ["124e850d-0794-5705-949f-2998c93d4fec", "Pierre Moreau"],
] as const;

test("Batch 676 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 328");
    await expect(page.locator("main")).toContainText(`Archive box${box}`);
  }
});

test("Batch 676 publishes six protected-identifier identities without employer inference", async ({ page }) => {
  for (const [id, name, privateOccupationCode] of armyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText(`occupation code ${privateOccupationCode}`);
    await expect(main).not.toContainText(`civilian_occupation_code=${privateOccupationCode}`);
  }
});

test("Batch 676 keeps both protected-identifier pairs separate and conflicting", async ({ page }) => {
  for (const [id, name] of duplicateConflicts) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("conflicting sources");
    await expect(main).toContainText("protected identifier");
    await expect(main).not.toContainText("Verified employer");
  }
});

test("Batch 676 preserves Herbert Morcom's Army conflict without publishing the wrong person", async ({ page }) => {
  await page.goto("./people/79e4357d-a18b-548e-963c-4984a5e8991f/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("official Army record under a different name");
  await expect(main).toContainText("Box 537");
  await expect(main).not.toContainText("civilian_occupation_code=736");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 676 documents Moravec's military-intelligence pathway without calling it civilian employment", async ({ page }) => {
  await page.goto("./people/514b026b-79f4-5f38-8030-ff2db7e80f2b/");
  const main = page.locator("main");
  await expect(main).toContainText("František Moravec");
  await expect(main).toContainText("Czechoslovak General Staff, Second Directorate");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 676 keeps Morck's oil interest out of the employee category", async ({ page }) => {
  await page.goto("./people/a1a84ce0-5053-5f29-9196-c2095378e810/");
  const main = page.locator("main");
  await expect(main).toContainText("Brinton & Co.");
  await expect(main).toContainText("Clinton Oil Company");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("does not qualify Morck for the oil-company employee category");

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  await expect(oilList).not.toContainText("Wesley C Morck");
});

test("Batch 676 documents Morde's prewar occupation without inventing an employer", async ({ page }) => {
  await page.goto("./people/a13de9e5-a321-57cb-b821-0c448f3a1c5f/");
  const main = page.locator("main");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("explorer");
  await expect(main).toContainText("American Intelligence and the German Resistance to Hitler");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 676 gives all eight unresolved people terminal research pages", async ({ page }) => {
  for (const [id, name] of unresolved) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("Archival-review priorityhigh");
    await expect(main).not.toContainText("Verified employer");
  }
});

test("Batch 676 publishes exact coverage and preserves the evidence-scoped oil category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,602");
  await expect(page.locator("body")).toContainText("35.93%");
  const category = page.locator("#oil-companies");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator(".oil-directory__person")).toHaveCount(8);
  await expect(category).not.toContainText("Wesley C Morck");

  await page.goto("./people/");
  const directoryCategory = page.locator(".featured-directory-category");
  await expect(directoryCategory.locator("li")).toHaveCount(8);
  await expect(directoryCategory).toContainText("10 historically named oil, petroleum, refining, or exploration companies");
  await expect(directoryCategory).not.toContainText("Wesley C Morck");
});
