import { expect, test } from "@playwright/test";

const profiles = [
  ["0e73e29c-d957-5860-8495-5010cedecbbf", "Joseph Orefice"],
  ["13a387ee-6cc7-59de-b6d9-f61999dbbace", "Edward Ordynowicz"],
  ["17b58857-a1c3-5080-a05a-1397161d2a55", "John Orisek"],
  ["1ef96ff0-c33a-5e78-b5f1-3bc2e0851a1f", "Edward M Orler"],
  ["323c2405-bb58-5d49-9d7a-8447bd15748a", "Marjorie H Oreilly"],
  ["3c47f06a-2731-5736-8551-afd363f9fe5e", "John Orban"],
  ["41da9570-412e-5a50-ac93-b12270bdc169", "Zygmunt Orlowicz"],
  ["45d865da-2ae1-5b26-9367-278da73e2882", "Peter C Orlich"],
  ["4f6ebe80-9fee-591b-a613-ee34f213297c", "Carmel V Orlando"],
  ["52b43c13-5bf3-5706-b162-92ac6bed2ddc", "Pampeil Orlando"],
  ["5dc2d83e-1c1b-5eea-99c5-ddda312cdcf5", "David Ormiston"],
  ["706ea654-2b09-57fb-be4b-2183b2fe28b1", "Joseph J Orlan"],
  ["759b91ad-0591-5abd-b43f-928442b710b3", "Melvin E Orchard"],
  ["7cba9b92-4ad2-5e3a-82df-f65985501261", "John T Orlandi"],
  ["858fa1d5-24db-5c06-8f65-0a9801b19063", "Joseph S Orlowski"],
  ["951aa690-d22b-5e92-a360-0211eeab7d49", "Julien A Orgeron"],
  ["a0416fee-bea4-5c2b-a6ba-ee54e9b81241", "Jesse M Orme"],
  ["b39c17d4-cda4-5342-9e37-41c72aa3ec33", "Liberio Orlando"],
  ["ce51cfd3-7880-521f-bc0f-d503c5547794", "John Orlowsci"],
  ["d83acd15-3919-51b5-a29e-eafdcba0cced", "John Oriniak"],
  ["d84ffc67-1b57-5daa-8b0d-b17e71f30839", "Samuel G Oregan"],
  ["e3277f61-c842-562d-ae40-a98cfbd6428f", "Alekos X Orkoulas"],
  ["fb8cab26-a314-5f91-b63f-1fadcb2a4647", "Ruth J Oreckovsky"],
] as const;

test("Batch 722 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 722 publishes Joseph Orlan's qualified radio and Signal Corps pathway", async ({ page }) => {
  await page.goto("./people/706ea654-2b09-57fb-be4b-2183b2fe28b1/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("amateur radio work");
  await expect(main).toContainText("United States Army Signal Corps");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("The Ukrainian Weekly");
  await expect(main).toContainText("occupation only found");
});

test("Batch 722 publishes official identity evidence without inventing employers", async ({ page }) => {
  await page.goto("./people/e3277f61-c842-562d-ae40-a98cfbd6428f/");
  const orkoulas = page.locator("main");
  await expect(orkoulas).toContainText("Identity statusconfirmed");
  await expect(orkoulas).toContainText("Tec 5 Alekos X Orkoulas");
  await expect(orkoulas).toContainText("also AS");
  await expect(orkoulas).toContainText("requires archival review");

  await page.goto("./people/17b58857-a1c3-5080-a05a-1397161d2a55/");
  const orisek = page.locator("main");
  await expect(orisek).toContainText("Identity statusconfirmed");
  await expect(orisek).toContainText("Special Orders No. 9");
  await expect(orisek).toContainText("requires archival review");

  await page.goto("./people/45d865da-2ae1-5b26-9367-278da73e2882/");
  const orlich = page.locator("main");
  await expect(orlich).toContainText("Identity statushigh confidence");
  await expect(orlich).toContainText("radio operator");
  await expect(orlich).toContainText("requires archival review");
});

test("Batch 722 preserves protected-identifier name conflicts", async ({ page }) => {
  await page.goto("./people/b39c17d4-cda4-5342-9e37-41c72aa3ec33/");
  const liberio = page.locator("main");
  await expect(liberio).toContainText("Identity statusconflicting");
  await expect(liberio).toContainText("ORLANDO LIBORIO");

  await page.goto("./people/ce51cfd3-7880-521f-bc0f-d503c5547794/");
  const orlowsci = page.locator("main");
  await expect(orlowsci).toContainText("Identity statusconflicting");
  await expect(orlowsci).toContainText("ORLOWSKI JOHN");
});

test("Batch 722 publishes David Ormiston's supported name variant", async ({ page }) => {
  await page.goto("./people/5dc2d83e-1c1b-5eea-99c5-ddda312cdcf5/");
  const main = page.locator("main");
  await expect(main).toContainText("David K Ormiston");
  await expect(main).toContainText("no reliable result after protocol");
});

test("Batch 722 publishes exact rebuilt coverage without changing the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,644");
  await expect(main).toContainText("40.29%");
  await expect(main).toContainText("14,290");
  await expect(main).toContainText("732");
  await expect(main).toContainText("328");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Joseph Orlan");
});
