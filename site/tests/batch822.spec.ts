import { expect, test } from "@playwright/test";

const profiles = [
  ["49a4a27d-2da8-5150-90b4-7f6d0000b17f", "E P Ross"],
  ["d7e8bdeb-cad6-5b23-8d33-3e6fdbf37e30", "Edward J Ross"],
  ["91711b75-29f9-5a40-b3d6-557168ed4aaf", "Harlow N Ross"],
  ["4bfed8ea-9c2c-5ae3-b320-c368aa4c69ba", "Henry H Ross"],
  ["d54aba0a-9afc-52e9-88e8-fe2a2d9faf7f", "James E Ross"],
  ["f750af6c-8824-5387-ac13-af8b78833a73", "Lonella B Ross"],
  ["d9371bd0-8175-53dc-b7c2-7a492464e59b", "Martin B Ross"],
  ["3109dbb0-00d4-5875-803a-0e7304130404", "Michael J Ross"],
  ["d1e9d23f-1bf8-5d7e-a16a-e2791fdf19aa", "Muriel I Ross"],
  ["1b2f94b4-925f-5cec-8acf-2f13b6ccc754", "Murray Ross"],
  ["c75ad316-c527-5880-8d1e-71c3e992ac58", "Otto H Ross"],
  ["1a4f7539-3aef-53fd-9511-da68ddf74797", "Robert T Ross"],
  ["a8391786-a95c-5114-83c8-6448ee75966e", "Stanley Ross"],
  ["58d75375-cb03-5af7-b4a7-6af19e6e6989", "Victor H Ross"],
  ["95a2c567-2004-5899-8028-832670ec9bff", "Walter M Ross"],
  ["5b0bb232-ad3c-5907-ae88-ae5fdb4cdf5c", "Peter S Rossello"],
  ["d2200214-683e-55ec-9172-d3a8d6d1aabb", "Clarence B Rosser Jr."],
  ["2e9b8aa5-4ed1-5673-982e-69828c9d2b72", "Garnet L Rosset"],
  ["ac8aecbf-2feb-5de1-a40f-4e664b8ee757", "Guiseppe Rossetti"],
  ["30e03df1-a3df-52af-b43a-333c3dc1355a", "Stephen O Rossetti"],
  ["61c52c2c-4105-55b5-ba1c-a0b764357bb0", "Lawrence F Rossi"],
  ["348e5eb8-7baf-53a9-b1d1-e2811c2ffd32", "Thomas G Rossi"],
  ["daaa336d-552e-5404-83c1-f72b6bf90304", "Harold T Rossman"],
] as const;

test("Batch 822 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Army identity-only matches do not become employer claims", async ({ page }) => {
  for (const id of [
    "4bfed8ea-9c2c-5ae3-b320-c368aa4c69ba",
    "3109dbb0-00d4-5875-803a-0e7304130404",
    "c75ad316-c527-5880-8d1e-71c3e992ac58",
    "1a4f7539-3aef-53fd-9511-da68ddf74797",
    "58d75375-cb03-5af7-b4a7-6af19e6e6989",
    "5b0bb232-ad3c-5907-ae88-ae5fdb4cdf5c",
    "348e5eb8-7baf-53a9-b1d1-e2811c2ffd32",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("official Army bulk record");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Stephen Rossetti profile visibly qualifies the VA identity match", async ({ page }) => {
  await page.goto("./people/30e03df1-a3df-52af-b43a-333c3dc1355a/");
  const main = page.locator("main");
  await expect(main).toContainText("Veterans Legacy Memorial");
  await expect(main).toContainText("probable identity match");
  await expect(main).toContainText("does not establish the pre-OSS chronology");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Lawrence Rossi conflict is rejected without changing the indexed identity", async ({ page }) => {
  await page.goto("./people/61c52c2c-4105-55b5-ba1c-a0b764357bb0/");
  const main = page.locator("main");
  await expect(main).toContainText("Lawrence F Rossi");
  await expect(main).toContainText("Jesse A. Carvalho");
  await expect(main).toContainText("was rejected");
  await expect(main).toContainText("requires archival review");
});

test("Murray Ross profile keeps the economist lead unassigned", async ({ page }) => {
  await page.goto("./people/1b2f94b4-925f-5cec-8acf-2f13b6ccc754/");
  const main = page.locator("main");
  await expect(main).toContainText("Brooklyn College");
  await expect(main).toContainText("no source connected him to the indexed OSS captain");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("printed Guiseppe spelling remains primary while Giuseppe is a search alias", async ({ page }) => {
  await page.goto("./people/ac8aecbf-2feb-5de1-a40f-4e664b8ee757/");
  await expect(page.getByRole("heading", { name: "Guiseppe Rossetti", level: 1 })).toBeVisible();
  const main = page.locator("main");
  await expect(main).toContainText("Giuseppe Rossetti");
  await expect(main).toContainText("tested Giuseppe as an alias");
});
