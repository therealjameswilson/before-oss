import { expect, test } from "@playwright/test";

const profiles = [
  ["087699de-9b55-5d2e-8031-10ed75cdbac5", "James P Osbourn"],
  ["1290a078-6636-5c18-a7b3-ecc4ecbbaf55", "Harry T Oshima"],
  ["20f9e573-e051-5620-bcb4-940516999c2d", "Takashi G Osaki"],
  ["2e493979-dc51-557f-b9a9-7e0335c45e88", "Dorothy P Osfield"],
  ["4b449859-ca9b-56c5-811f-e33aa45cbb05", "Lithgow Osborne"],
  ["5094a0a5-e278-5726-bc62-75945e10bd47", "Helen Osmun"],
  ["733059a8-b49b-5b50-a0a3-ef2ca11e62a2", "Birginia Osborn"],
  ["75964751-419e-529e-9fbf-4c755aa42091", "Peter J Ortiz"],
  ["7ebebebb-2871-5b0a-ba84-fb86130dcce9", "Justin J Oshea"],
  ["89cab667-b2ab-5c33-814c-b022135e8cff", "Robert Orwin"],
  ["a6888720-579c-5a46-9682-3a65a601bbd0", "Robert J Orwin"],
  ["afc92e80-f697-5c67-9b04-c100b5b6dd2a", "Robert L Osgood"],
  ["b32e1cbd-41d9-5df5-b648-f274181c0438", "Frank C Osment"],
  ["b89982d2-996c-5cf9-8341-3327ac1cdf31", "John G Ortlepp"],
  ["c42b98c1-fb68-5024-9257-94d097ccfbf4", "Marguerite G Osborne"],
  ["c4f9a5ca-2a30-52de-bb77-ebde21026b52", "Robert G Osborne"],
  ["d1e9fde9-93c5-50dd-a69d-01b1241f9a0f", "Gilbert Ortiz"],
  ["d284d88d-093a-5d91-be5d-43b527d365fe", "Harold Ossman"],
  ["d5853588-f387-54eb-9312-3d87b1d993c4", "Stanley Oscar"],
  ["d6c5603e-3afe-588f-83c9-344a27d3302e", "Leonard Oshrain"],
  ["e54dc05a-0fab-5f8d-9c1d-6edc85e5c203", "Francis J Osinskie"],
  ["e7560303-162f-571e-99b9-f84888e11d7c", "Frederic C Osgood"],
  ["f7b024bd-f546-54bf-bb10-97205c6e5781", "Edward A Osowski"],
] as const;

test("Batch 724 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^\d{4,8}$/);
  }
});

test("Batch 724 publishes Lithgow Osborne's explicit state-to-OSS transition", async ({ page }) => {
  await page.goto("./people/4b449859-ca9b-56c5-811f-e33aa45cbb05/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("New York State Conservation Department");
  await expect(main).toContainText("Conservation Commissioner");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("verified employer found");
  await expect(main).toContainText("Congressional Record");
  await expect(main).toContainText("Thirty-Second Annual Report");
});

test("Batch 724 keeps Helen Osmun's college attendance separate from employment", async ({ page }) => {
  await page.goto("./people/5094a0a5-e278-5726-bc62-75945e10bd47/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Swarthmore College");
  await expect(main).toContainText("student");
    await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("Helen Parker Obituary");
});

test("Batch 724 preserves both protected-identifier conflicts", async ({ page }) => {
  await page.goto("./people/e7560303-162f-571e-99b9-f84888e11d7c/");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");
  await expect(page.locator("main")).toContainText("Shinohara Jasaku");

  await page.goto("./people/d284d88d-093a-5d91-be5d-43b527d365fe/");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");
  await expect(page.locator("main")).toContainText("Koken Lee R");
});

test("Batch 724 retains Peter Ortiz's existing evidence without duplicating it", async ({ page }) => {
  await page.goto("./people/75964751-419e-529e-9fbf-4c755aa42091/");
  const main = page.locator("main");
  await expect(main).toContainText("US Marine Corps");
  await expect(main).toContainText("French Foreign Legion");
  await expect(main).toContainText("verified employer found");
  await expect(main.getByText("French Foreign Legion", { exact: true })).toHaveCount(1);
});

test("Batch 724 publishes exact rebuilt coverage without changing the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,689");
  await expect(main).toContainText("40.47%");
  await expect(main).toContainText("14,245");
  await expect(main).toContainText("736");
  await expect(main).toContainText("329");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Lithgow Osborne");
  await expect(page.locator("#oil-companies")).not.toContainText("Helen Osmun");
});
