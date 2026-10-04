import { expect, test } from "@playwright/test";

const profiles = [
  ["e34b2e5c-21b4-5bb3-9eb1-e3b0f8304974", "Willard P Norberg"],
  ["5aa67c35-393d-5d55-a59c-6eb56acccc44", "Guy E Norbert"],
  ["8feff3e9-c0f0-55f7-a0f2-368409127930", "Christopher S Norborg"],
  ["fc20fcec-9ec1-5946-a008-575f960cf541", "Phyllis Norbury"],
  ["d0db0770-8fb0-54ed-a106-eacc572e8393", "Albert Nordang"],
  ["166850e8-6505-5239-88ca-9a2c1b946b1d", "Harold E Nordblom"],
  ["349ff874-fa17-5c61-b0ce-774f0ddb9a5d", "Albert Norden"],
  ["c3503298-8ec3-566f-a737-f4c239ffb185", "Vivian E Nordenstam"],
  ["5bdc3002-150c-5a85-ab95-b4fe9357cd9d", "Johan Nordentoft"],
  ["3c26f2a2-98c8-5a66-9455-ee7e70de8f83", "Jackson E Nordin"],
  ["2bccfeab-63b9-515b-a49d-0232c95c4093", "Jens H Nordlie"],
  ["513063d8-461e-505f-a7c3-4ceb2d8cc19f", "John B Nordmann"],
  ["1e6ce64f-7660-5290-9e04-76dda9ce07b0", "Carl W Nordsiek"],
  ["0562d0f0-e9da-5ff2-95fe-f220c65a613d", "Frederick C Nordsiek"],
  ["0d9c879c-d34e-5b82-98e7-8378eb10b8e6", "Robert W Nordstrom"],
  ["11bc2ae5-b430-573a-b0c1-6b35a78f1144", "Kenneth R Nordwall"],
  ["d295de39-bd24-5c78-aefe-6c420e606689", "Karl H Noris"],
  ["2c77e6cf-f75f-57c2-8f6a-86f72290be2c", "John Norman"],
  ["0a1b0e06-7bc1-597c-b473-4e839e13f4e6", "John F Norman"],
  ["1ae048a4-3d9d-500c-ad94-e18b0855f635", "Brunnon C Normand"],
  ["2067f122-eb6e-5aed-9d0d-21ca1ddf9abe", "Maurice O Normandin"],
  ["e40c168a-b89e-5219-af2c-8ad57487d77f", "Ira E Norrell"],
  ["7b95bb86-dbe1-5a34-8195-7e31a845ce5d", "John Norris"],
  ["6fc82ff9-6ccd-57aa-b711-9134b266b151", "Karl H Norris"],
] as const;

test("Batch 708 publishes all 24 direct profile routes with terminal outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{5,8}$/);
  }
});

test("Batch 708 publishes Christopher Norborg's dated university employment without claiming immediacy", async ({ page }) => {
  await page.goto("./people/8feff3e9-c0f0-55f7-a0f2-368409127930/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("University of Minnesota");
  await expect(main).toContainText("Assistant Professor of Philosophy");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("no source explicitly calls it the immediate predecessor");
});

test("Batch 708 keeps Harold Nordblom's Cyprus duty separate from employer evidence", async ({ page }) => {
  await page.goto("./people/166850e8-6505-5239-88ca-9a2c1b946b1d/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("GI mess at Cyprus");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 708 distinguishes Johan Nordentoft's military pathway from civilian employment", async ({ page }) => {
  await page.goto("./people/5bdc3002-150c-5a85-ab95-b4fe9357cd9d/");
  const main = page.locator("main");
  await expect(main).toContainText("Danish Army - Zealand Division");
  await expect(main).toContainText("Chief of staff");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).not.toContainText("documented prewar employer found");
});

test("Batch 708 publishes Jens Nordlie's strongly date-bounded last civilian employer", async ({ page }) => {
  await page.goto("./people/2bccfeab-63b9-515b-a49d-0232c95c4093/");
  const main = page.locator("main");
  await expect(main).toContainText("Jens Henrik Throne Nordlie");
  await expect(main).toContainText("Narvesens Kioskkompani");
  await expect(main).toContainText("Office manager");
  await expect(main).toContainText("strongly date bounded");
});

test("Batch 708 preserves name conflicts and duplicate rows instead of silently merging", async ({ page }) => {
  await page.goto("./people/5aa67c35-393d-5d55-a59c-6eb56acccc44/");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");
  await expect(page.locator("main")).toContainText("Norbert C Guy");

  await page.goto("./people/1e6ce64f-7660-5290-9e04-76dda9ce07b0/");
  await expect(page.locator("main")).toContainText("Carl W Nordsieck");
  await expect(page.locator("main")).toContainText("Identity statusconflicting");

  for (const id of ["d295de39-bd24-5c78-aefe-6c420e606689", "6fc82ff9-6ccd-57aa-b711-9134b266b151"]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("Identity statusprobable");
    await expect(page.locator("main")).toContainText("Serial••••8088");
    await expect(page.locator("main")).toContainText("Duplicate groupduplicate-1bb444528063");
  }
});

test("Batch 708 updates exact coverage while preserving the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,323");
  await expect(main).toContainText("38.94%");
  await expect(main).toContainText("322");
  await expect(main).toContainText("14,611");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
