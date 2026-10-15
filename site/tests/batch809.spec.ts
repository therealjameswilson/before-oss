import { expect, test } from "@playwright/test";

const profiles = [
  ["5ec8cf9b-59e7-536c-94bc-69396442fc5a", "Warren D Robbins", "649"],
  ["0c8efaf1-0689-561c-846b-c3c5289f874d", "Felix W Robbio", "649"],
  ["02cd5337-85bc-573a-aa46-d28582e77955", "Cletis L Roberson", "649"],
  ["e29b025c-ca4f-5721-9979-86ecd1764642", "James B Roberson", "649"],
  ["61410d8e-63b0-51f0-920c-daebfbaa59a1", "Fabiola M Robert", "649"],
  ["038f7291-863a-556e-bf20-772582341df5", "H B Robert", "649"],
  ["bf40d8a1-9d08-5f98-ae65-f29218ecad56", "Henry F Robert", "649"],
  ["5b12a72f-8c0f-5c6a-afc8-8a249df82213", "Jacques Robert", "649"],
  ["bfb4eb2d-c8c1-5531-beb3-d035b1f88bda", "Authur P Roberta", "649"],
  ["8ed71a8e-ba56-5c07-880a-a7851ed36fa7", "Joseph M Roberto", "649"],
  ["55bf38f5-a73a-5a11-b07d-4b78d36672b3", "Arthur M Roberts", "649"],
  ["4c7518cb-763d-5673-bf22-1cf12666784d", "Carl E Roberts", "649"],
  ["0a58e4e4-c28c-5660-8044-6bdebd0896c9", "Charles W Roberts", "649"],
  ["0a9e764d-0b3a-52c3-9602-dbe442b1bccf", "Dennis J Roberts", "649"],
  ["8c58186b-31f7-5ede-90b8-b8476650b862", "Donald H Roberts", "649"],
  ["41c53601-083a-57ae-b620-cf8e653cfdcb", "Edythe Roberts", "649"],
  ["8e2560a3-5054-5c9e-bd20-9795c295f8b0", "Eleanor C Roberts", "649"],
  ["76804006-52fe-5cfc-ac14-ee53d366e608", "Eloise Roberts", "649"],
  ["bd182766-48c6-5097-bda0-7eeabb95685a", "Eston J Roberts", "649"],
  ["3f8ff5d8-6f08-511e-b6e1-133792734dcc", "Forrest C Roberts", "649"],
  ["b72d01c2-2014-54f9-926a-141c7f6782b6", "George Roberts", "649"],
  ["fa48e984-628e-51c0-ab5d-71972f0d1d9f", "Glaucia B Roberts", "649"],
  ["3bc15fef-ae64-5d5c-9150-4f091385a85b", "H B Roberts", "650"],
] as const;

test("Batch 809 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText(box);
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Felix Robbio publishes the exact Army identity without inferring an employer", async ({ page }) => {
  await page.goto("./people/0c8efaf1-0689-561c-846b-c3c5289f874d/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("November 1942");
  await expect(main).toContainText("exact private-identifier agreement");
  await expect(main).toContainText("French note is preserved without expansion");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Eston Roberts publishes the exact Army identity without treating coded occupation as employment", async ({ page }) => {
  await page.goto("./people/bd182766-48c6-5097-bda0-7eeabb95685a/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("January 1943");
  await expect(main).toContainText("exact private-identifier agreement");
  await expect(main).toContainText("coded occupation remain private");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Joseph Roberto visibly preserves the post-OSS Army-entry chronology problem", async ({ page }) => {
  await page.goto("./people/8ed71a8e-ba56-5c07-880a-a7851ed36fa7/");
  const main = page.locator("main");
  await expect(main).toContainText("needs temporal review");
  await expect(main).toContainText("June 1946");
  await expect(main).toContainText("after OSS dissolution");
  await expect(main).toContainText("No employment, occupation, or immediate-affiliation claim is made");
});

test("Authur Roberta preserves the printed spelling and labels the search alias", async ({ page }) => {
  await page.goto("./people/bfb4eb2d-c8c1-5531-beb3-d035b1f88bda/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Authur P Roberta", level: 1 })).toBeVisible();
  await expect(main).toContainText("Arthur P Roberta");
  await expect(main).toContainText("source spelling");
  await expect(main).toContainText("requires archival review");
});

test("Jacques Robert withholds the unlinked Robert-Rewez namesake", async ({ page }) => {
  await page.goto("./people/5b12a72f-8c0f-5c6a-afc8-8a249df82213/");
  const main = page.locator("main");
  await expect(main).toContainText("Jacques Robert-Rewez");
  await expect(main).toContainText("no source connects that person to this Box 649 row");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("H B Robert and H B Roberts remain separate unresolved entities", async ({ page }) => {
  await page.goto("./people/038f7291-863a-556e-bf20-772582341df5/");
  await expect(page.getByRole("heading", { name: "H B Robert", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("649");
  await page.goto("./people/3bc15fef-ae64-5d5c-9150-4f091385a85b/");
  await expect(page.getByRole("heading", { name: "H B Roberts", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("650");
  await expect(page.locator("main")).toContainText("remains separate");
});

test("home page exposes the rebuilt Batch 809 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,594");
  await expect(home).toContainText("48.43%");
  await expect(home).toContainText("12,339");
  await expect(home).toContainText("831");
  await expect(home).toContainText("374");
  await expect(home).toContainText("10,057");
});
