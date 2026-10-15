import { expect, test } from "@playwright/test";

const profiles = [
  ["da78d8b9-b841-532e-b272-53dc070d5c22", "Roy K Rickerson", "643"],
  ["efc8f9b6-41d7-559d-8ae7-5aa08d0f759c", "August Richman", "643"],
  ["88c18f17-cf0f-5d64-90fa-78b80af39d74", "Bennett B Richman", "643"],
  ["6cadc59c-b911-519e-8c14-347d9988ad65", "Nathan L Richman", "643"],
  ["c7a455ab-3738-5954-b15f-3505badec140", "G N Richmond", "643"],
  ["9f4c35f2-0f0b-51f9-9937-5c8c840ba6f8", "Allen R Richter", "643"],
  ["e9b09887-896d-5005-96a8-56c315ca09c5", "Allen R Richter", "643"],
  ["6b94d400-9240-5634-8766-b70ed08513a5", "Dorothy V Richter", "643"],
  ["32218440-8c69-5186-b635-771aca652361", "Frederick K Richter", "643"],
  ["b6fb870e-d198-5dae-8bad-480318f53882", "Jon C Richter", "643"],
  ["7993ed19-ca2a-58e1-8215-993c6f4a1b3e", "Melvin Richter", "643"],
  ["4bc2f78c-edec-5784-a36f-8c590b34ca6a", "Leonal D Rickard", "643"],
  ["03308f98-f203-5ab7-bef8-fc5fca958478", "Mildred Ricker", "643"],
  ["d481fa5d-dbae-555c-8ffb-b7765b7f0aa8", "Robert R Ricker", "643"],
  ["aee8bdd1-4c58-50f6-8d46-dd72309a6d87", "Ethel A Rickers", "643"],
  ["46661a18-5dd9-52d9-8b02-6110781bb880", "Peirson Ricks", "644"],
  ["23a62dde-19c1-5fe0-95d9-f5a4cc65a9d0", "John G Riddell", "644"],
  ["ef33905c-178a-59f7-8850-9965ce91b110", "Richard J Riddell", "644"],
  ["d3611d10-9d87-5e7a-b1b5-b7ceb6fbb2ab", "John Gatlin Riddick", "644"],
  ["24a4d7e7-03a4-5117-8f2b-9b663b8c6974", "James H Riddle", "644"],
  ["2315ad65-f510-52e8-aed6-6cb086425dbc", "Sigrid F Riddle", "644"],
  ["55df5b70-d8f4-5850-9370-c9ad3e01b782", "Harry C Riddle Jr.", "644"],
] as const;

test("Batch 803 publishes all 22 active profiles with terminal attempted outcomes", async ({ page }) => {
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
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Roy Rickerson profile preserves both index rows and the reviewed spelling resolution", async ({
  page,
}) => {
  await page.goto("./people/da78d8b9-b841-532e-b272-53dc070d5c22/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Roy K Richerson");
  await expect(main).toContainText("Roy K Rickerson");
  await expect(main).toContainText("Capt");
  await expect(main).toContainText("1st Lt");
  await expect(main).toContainText("Pfc. Weiss Begins His Adventure in Southern France");
  await expect(main).toContainText("OSS in Action: The Pacific and the Far East");
});

test("Allen Richter publishes qualified communications work without a named employer", async ({
  page,
}) => {
  await page.goto("./people/9f4c35f2-0f0b-51f9-9937-5c8c840ba6f8/");
  const main = page.locator("main");
  await expect(main).toContainText("communications industry");
  await expect(main).toContainText("medium documented pre-OSS");
  await expect(main).toContainText("not a named employer claim");
  await expect(main).toContainText("Duplicate group");
});

test("Melvin Richter distinguishes Harvard student status from employment", async ({ page }) => {
  await page.goto("./people/7993ed19-ca2a-58e1-8215-993c6f4a1b3e/");
  const main = page.locator("main");
  await expect(main).toContainText("Harvard College");
  await expect(main).toContainText("Student");
  await expect(main).toContainText("not treated as an employer");
  await expect(main).toContainText("Operation MAGPIE");
});

test("Peirson Ricks exposes the unnamed immediate employer and earlier work", async ({ page }) => {
  await page.goto("./people/46661a18-5dd9-52d9-8b02-6110781bb880/");
  const main = page.locator("main");
  await expect(main).toContainText("a technical school");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("a Philadelphia advertising firm");
  await expect(main).toContainText("a Winston-Salem cotton mill");
  await expect(main).toContainText("Ricks, (David) Peirson");
});

test("Batch 803 preserves clipped notes without silent expansion", async ({ page }) => {
  await page.goto("./people/88c18f17-cf0f-5d64-90fa-78b80af39d74/");
  await expect(page.locator("main")).toContainText("photogra");

  await page.goto("./people/6cadc59c-b911-519e-8c14-347d9988ad65/");
  await expect(page.locator("main")).toContainText("French c");

  await page.goto("./people/03308f98-f203-5ab7-bef8-fc5fca958478/");
  await expect(page.locator("main")).toContainText("Charged");

  await page.goto("./people/24a4d7e7-03a4-5117-8f2b-9b663b8c6974/");
  await expect(page.locator("main")).toContainText("Record");
});

test("home page exposes the rebuilt Batch 803 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,456");
  await expect(home).toContainText("47.86%");
  await expect(home).toContainText("12,477");
  await expect(home).toContainText("822");
  await expect(home).toContainText("371");
  await expect(home).toContainText("9,919");
});
