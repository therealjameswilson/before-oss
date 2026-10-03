import { expect, test } from "@playwright/test";

const profiles = [
  ["6c6d1465-c1bb-5819-a3b0-c3de320e9d76", "Springs R Moore", "535"],
  ["34883c78-0b17-507e-92ee-d688a478de61", "Wallace J Moore", "535"],
  ["694be9e5-ca0d-51b2-8c94-b9eea9b7c98a", "Walter A Moore", "536"],
  ["5b531fb4-ac69-5a3a-bca4-c5b9d8acf619", "Wayne E Moore", "536"],
  ["833e896b-4ee4-5279-a3a1-ed071ea82e29", "William B Moore", "536"],
  ["6e1ea084-e722-5431-b9ed-28cf0f023918", "William C Moore", "536"],
  ["06ab8ad7-a135-53a3-bf9c-df5ffc0a350f", "William R Moore", "536"],
  ["71b62b49-026e-5c80-9af2-7053d56f99a4", "Wilson H Moore", "536"],
  ["1c6d98f2-9a13-5448-a594-3502a97e27c1", "Ethel H Moorhead", "536"],
  ["8d473190-979f-539e-9e0d-960503420de6", "Tommie J Moorman", "536"],
  ["66f196e5-b5a5-572c-8f39-7c5ff87118b2", "Joseph L Moortgat", "536"],
  ["83b285b4-c6da-566c-b9dc-d0f37376bf5e", "Gordon A Moote", "536"],
  ["06c27b18-42da-5250-9a3c-be7b91054615", "Domenic J Morabito", "536"],
  ["ad3d9f60-98ab-576e-8f57-77f0c3ce95f6", "Edward J Moraghan", "536"],
  ["55c2480c-fb3e-5546-9149-1c9f852576b8", "Victor M Morales", "536"],
  ["580d34ef-3911-5dba-a493-f137ef4cb85d", "Alfred B Moran", "536"],
  ["7a15a4ca-9cb2-5fef-8bc0-1ab242aab6c3", "Avis M Moran", "536"],
  ["48b5cf53-54d6-5da2-8abc-eadb10b5fd69", "Cecilia A Moran", "536"],
  ["742bea6b-8d99-5e02-b4ea-793a712b3af0", "Charles Moran", "536"],
  ["2dfd41c8-3312-5d24-9906-87502fca38fe", "Clarence Moran", "536"],
  ["fb606f68-9b21-5079-808e-fe8cb4ca1e2a", "Daniel J Moran", "536"],
  ["82ab157c-0f23-5ff9-9e6d-bb79e308df99", "Finis G Moran", "536"],
  ["dc4e984d-4335-5e1d-956b-4329775a97c3", "Frank W Moran", "536"],
  ["85a8e7b1-167f-5232-8b20-5730808c701a", "George B Moran", "536"],
] as const;

const armyMatches = [
  ["34883c78-0b17-507e-92ee-d688a478de61", "Wallace J Moore", "768"],
  ["694be9e5-ca0d-51b2-8c94-b9eea9b7c98a", "Walter A Moore", "992"],
  ["83b285b4-c6da-566c-b9dc-d0f37376bf5e", "Gordon A Moote", "992"],
  ["06c27b18-42da-5250-9a3c-be7b91054615", "Domenic J Morabito", "157"],
  ["fb606f68-9b21-5079-808e-fe8cb4ca1e2a", "Daniel J Moran", "992"],
  ["85a8e7b1-167f-5232-8b20-5730808c701a", "George B Moran", "097"],
] as const;

const unresolved = [
  ["6c6d1465-c1bb-5819-a3b0-c3de320e9d76", "Springs R Moore"],
  ["833e896b-4ee4-5279-a3a1-ed071ea82e29", "William B Moore"],
  ["6e1ea084-e722-5431-b9ed-28cf0f023918", "William C Moore"],
  ["06ab8ad7-a135-53a3-bf9c-df5ffc0a350f", "William R Moore"],
  ["71b62b49-026e-5c80-9af2-7053d56f99a4", "Wilson H Moore"],
  ["1c6d98f2-9a13-5448-a594-3502a97e27c1", "Ethel H Moorhead"],
  ["8d473190-979f-539e-9e0d-960503420de6", "Tommie J Moorman"],
  ["66f196e5-b5a5-572c-8f39-7c5ff87118b2", "Joseph L Moortgat"],
  ["ad3d9f60-98ab-576e-8f57-77f0c3ce95f6", "Edward J Moraghan"],
  ["55c2480c-fb3e-5546-9149-1c9f852576b8", "Victor M Morales"],
  ["580d34ef-3911-5dba-a493-f137ef4cb85d", "Alfred B Moran"],
  ["7a15a4ca-9cb2-5fef-8bc0-1ab242aab6c3", "Avis M Moran"],
  ["48b5cf53-54d6-5da2-8abc-eadb10b5fd69", "Cecilia A Moran"],
  ["742bea6b-8d99-5e02-b4ea-793a712b3af0", "Charles Moran"],
  ["82ab157c-0f23-5ff9-9e6d-bb79e308df99", "Finis G Moran"],
  ["dc4e984d-4335-5e1d-956b-4329775a97c3", "Frank W Moran"],
] as const;

test("Batch 675 publishes all 24 direct profile routes", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 328");
    await expect(page.locator("main")).toContainText(`Archive box${box}`);
  }
});

test("Batch 675 publishes six protected-identifier identities without employer inference", async ({ page }) => {
  for (const [id, name, privateOccupationCode] of armyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("Verified employer");
    await expect(main).not.toContainText(`occupation code ${privateOccupationCode}`);
    await expect(main).not.toContainText(`civilian_occupation_code=${privateOccupationCode}`);
  }
});

test("Batch 675 preserves Walter Moore's documented suffix without forcing the grade code", async ({ page }) => {
  await page.goto("./people/694be9e5-ca0d-51b2-8c94-b9eea9b7c98a/");
  const main = page.locator("main");
  await expect(main).toContainText("Walter A Moore Jr");
  await expect(main).toContainText("Jr. suffix absent from the index");
  await expect(main).toContainText("preserved without forced interpretation");
  await expect(main).not.toContainText("entry grade private");
});

test("Batch 675 publishes Clarence Moran's official Field Photo Branch bridge", async ({ page }) => {
  await page.goto("./people/2dfd41c8-3312-5d24-9906-87502fca38fe/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Field Photo Branch");
  await expect(main).toContainText("CHSP(P)");
  await expect(main).toContainText("WN#08587");
  await expect(main).toContainText("not Clarence Moran's pre-OSS employer");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 675 preserves Wayne Moore's identity conflict without misidentifying him", async ({ page }) => {
  await page.goto("./people/5b531fb4-ac69-5a3a-bca4-c5b9d8acf619/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("official Army record under a different name");
  await expect(main).toContainText("Box 536");
  await expect(main).not.toContainText("Nelson Albert O");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 675 gives all sixteen unresolved people terminal research pages", async ({ page }) => {
  for (const [id, name] of unresolved) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("Archival-review priorityhigh");
    await expect(main).not.toContainText("Verified employer");
  }
});

test("Batch 675 preserves truncated index notes as indexed", async ({ page }) => {
  await page.goto("./people/06ab8ad7-a135-53a3-bf9c-df5ffc0a350f/");
  await expect(page.locator("main")).toContainText("file is ch");
  await page.goto("./people/71b62b49-026e-5c80-9af2-7053d56f99a4/");
  await expect(page.locator("main")).toContainText("docume");
});

test("Batch 675 updates exact coverage and does not add an oil-company member", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,580");
  await expect(page.locator("body")).toContainText("35.84%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  for (const [, name] of profiles) {
    await expect(oilList).not.toContainText(name);
  }
});
