import { expect, test } from "@playwright/test";

const profiles = [
  ["7d86b8f5-09fa-55fd-81c0-939cb86a0473", "William H Schmagel"],
  ["a8812c32-0a9a-5e07-a7f1-ed6b1ee3e4c7", "Horace W Schmahl"],
  ["4e13fda2-6782-5529-b898-268199101539", "George P Schmaling"],
  ["7dd68572-ec0d-5ee4-8946-45c1d8e4d121", "Alexander P Schmalz"],
  ["22997adf-905c-5bb4-bf62-59c19bdd311a", "Alice H Schmid"],
  ["d4b44bec-b748-5880-b074-a6397ea53302", "Joseph L Schmid"],
  ["01b3ff04-ab44-5d89-b773-5bc9bcd1a4da", "Robert C Schmid"],
  ["5b9db8ec-1bc3-5fd2-9b71-d965b5c376b7", "Adolph W Schmidt"],
  ["fd43d47d-554d-5abc-b2f8-22713877ab30", "Dorothy K Schmidt"],
  ["e9977e95-8e44-550e-9ed4-7bd5fa6d492b", "Edward C Schmidt"],
  ["c1b39fb6-9e5a-55a7-be27-654ad7b13c29", "Edwin Schmidt"],
  ["b31e4b71-0e86-58a7-91f0-6566f7eeda71", "Erich F Schmidt"],
  ["ad153284-af7e-528c-9830-35a9daefb07f", "Erling P Schmidt"],
  ["f29318da-08da-5d12-bab2-f34c4edfe329", "Ervin W Schmidt"],
  ["c52e6d9d-17a2-5a93-9e06-186d5be7b225", "Eugene V Schmidt"],
  ["c8469224-b635-5a2b-b629-cbfd72a568f5", "Everett G Schmidt"],
  ["3e5ccbb2-c18a-56c6-a9b8-fed692eaca5c", "Frank Schmidt"],
  ["c0716168-0009-5f17-9f73-539516fd76b8", "George Schmidt"],
  ["7aa1e2ad-2163-5652-82ca-032e610176c4", "Jack C Schmidt"],
  ["ddf0488c-07db-58e6-9637-9eb1d51eec0e", "Oswald A Schmidt"],
  ["93fbdd8f-dc7f-5d90-853d-309e1fb29fba", "Robert C Schmidt"],
  ["a0668707-52bc-51d6-b548-d39a3396ee2a", "Robert E Schmidt"],
  ["bd62af97-ba71-5608-9b8e-aa23e0579979", "William J Schmidt"],
] as const;

test("Batch 846 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
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

test("William Schmagel keeps the Air Corps pathway distinct from civilian employment", async ({ page }) => {
  await page.goto("./people/7d86b8f5-09fa-55fd-81c0-939cb86a0473/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("William Herman Schmagel");
  await expect(main).toContainText("United States Army Air Corps");
  await expect(main).toContainText("Radio and code instructor");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("United States Army Signal Corps");
  await expect(main).toContainText("qualified pending personnel-file confirmation");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Horace Schmahl publishes qualified federal work without expanding the index note", async ({ page }) => {
  await page.goto("./people/a8812c32-0a9a-5e07-a7f1-ed6b1ee3e4c7/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("ASN is n");
  await expect(main).toContainText("United States Attorney's Office for the Southern District of New York");
  await expect(main).toContainText("Independent contractor and translator");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("overlapping Army and federal assignments prevent treating it as immediately prior");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Adolph Schmidt separates the last civilian employer from corporate board affiliations", async ({ page }) => {
  await page.goto("./people/5b9db8ec-1bc3-5fd2-9b71-d965b5c376b7/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Adolph William Schmidt");
  await expect(main).toContainText("Mellon National Bank");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("1929–1942");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Columbia Radiator Company");
  await expect(main).toContainText("Pittsburgh Coal Company");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("the exact immediate military assignment remains unknown");
});

test("Batch 846 Army crosswalks publish variants without exposing protected identifiers", async ({ page }) => {
  await page.goto("./people/d4b44bec-b748-5880-b074-a6397ea53302/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Joseph L Schmid Jr");
  await expect(main).toContainText("suffix is a documented variant");
  await expect(main).not.toContainText("occupation code:");

  await page.goto("./people/7aa1e2ad-2163-5652-82ca-032e610176c4/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Jack Schmidt");
  await expect(main).toContainText("middle-initial omission is retained as a variant");
  await expect(main).not.toContainText("occupation code:");
});

test("Erich Schmidt preserves the visibly truncated note and requires archival review", async ({ page }) => {
  await page.goto("./people/b31e4b71-0e86-58a7-91f0-6566f7eeda71/");
  const main = page.locator("main");
  await expect(main).toContainText("Consulta");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("remains unexpanded");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});
