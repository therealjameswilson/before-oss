import { expect, test } from "@playwright/test";

const profiles = [
  ["74f0a45e-f63e-5773-b2c3-cb9dc9159837", "Arpad J Nevada"],
  ["1ccf262c-5a41-501c-a87a-b4f57431eef3", "Louis W Neve"],
  ["a99668c8-57ae-56f1-a6c6-4d8039efc1d7", "Francis M Nevils"],
  ["365606ff-aef4-5a25-9d0f-ea057d79cda6", "John F Nevins"],
  ["8c0768be-1486-527c-97ad-7f8f4a1725d6", "Charles H New"],
  ["375aeeec-dcaf-5008-a43b-18579912fa54", "Ilhan New"],
  ["25fc3e86-41ac-56dd-9b32-ba5daa4ad8d0", "Victor M Newberg"],
  ["979dc34e-ee2b-5a37-a72d-3e1870bbcef1", "Truman H Newberry II"],
  ["71a8bb62-41ce-521a-9881-fb8692c08a1d", "Max J Newcomb"],
  ["c0796ba1-9ef7-5f16-b1ab-cf13075f5df7", "Patricia B Newcomb"],
  ["2e26dc88-c522-5f09-8d0f-a4ee6ad0cd9f", "Thelma V Newcomb"],
  ["ca884707-ee7d-58aa-bb04-78736c04af8f", "Theodore M Newcomb"],
  ["13a58c79-f698-58d6-8700-f5a6ceedc5d0", "Dorothea Newell"],
  ["7986ffc5-dc66-5582-a59b-2ba10904d8e3", "John W Newett"],
  ["c08eee15-9623-5047-b4bd-5fc257ba2fa4", "Wilhelmina Newfield"],
  ["1f0eb167-73f1-5b2a-8f56-225ac0ed36f4", "Norman N Newhouse"],
  ["f1826568-cc5e-5df7-8d46-02b31ad073c2", "John G Newitt"],
  ["58fa8d43-f909-50a3-b044-15c3bd7deb01", "Raymond F Newkirk"],
  ["5f75e958-e405-59bb-80b4-1b9766916e60", "Winton H Newkirk"],
  ["ca9dd2a2-d1df-5445-9e34-923a20c2bfaf", "Edwin S Newman"],
  ["0712d49d-f222-5cdd-adf3-c878e3a3dc1c", "Elizabeth E Newman"],
  ["29719ffc-dbc2-5dbd-a255-996f93e7ace6", "Howard L Newman"],
  ["59bcd221-a84a-513b-af5d-777ebeab2a88", "John R Newman"],
] as const;

test("Batch 701 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{7,8}$/);
  }
});

test("Batch 701 separates Ilhan New's immediate affiliation, civilian employer, and student status", async ({ page }) => {
  await page.goto("./people/375aeeec-dcaf-5008-a43b-18579912fa54/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Overseas Korean Congress");
  await expect(main).toContainText("Yuhan Corporation");
  await expect(main).toContainText("La Choy Food Products Inc.");
  await expect(main).toContainText("University of Southern California");
  await expect(main).toContainText("USC is not counted as an employer");
  await expect(main).toContainText("Dr. Ilhan New: Road of Life");
});

test("Batch 701 publishes the Newcomb, Newett, Newhouse, and Newkirk pathways with qualifications", async ({ page }) => {
  await page.goto("./people/ca884707-ee7d-58aa-bb04-78736c04af8f/");
  let main = page.locator("main");
  await expect(main).toContainText("Theodore Mead Newcomb");
  await expect(main).toContainText("University of Michigan");
  await expect(main).toContainText("strongly date bounded");

  await page.goto("./people/7986ffc5-dc66-5582-a59b-2ba10904d8e3/");
  main = page.locator("main");
  await expect(main).toContainText("Naval Air Corps");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);

  await page.goto("./people/1f0eb167-73f1-5b2a-8f56-225ac0ed36f4/");
  main = page.locator("main");
  await expect(main).toContainText("Long Island Press");
  await expect(main).toContainText("medium probable immediate");
  await expect(main).toContainText("exact military leave date is not stated");

  await page.goto("./people/58fa8d43-f909-50a3-b044-15c3bd7deb01/");
  main = page.locator("main");
  await expect(main).toContainText("Federal Bureau of Investigation");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("exact transfer date remains unlocated");
});

test("Batch 701 keeps Army identity-only records and identifier conflicts honest", async ({ page }) => {
  for (const id of [
    "1ccf262c-5a41-501c-a87a-b4f57431eef3",
    "8c0768be-1486-527c-97ad-7f8f4a1725d6",
    "25fc3e86-41ac-56dd-9b32-ba5daa4ad8d0",
    "979dc34e-ee2b-5a37-a72d-3e1870bbcef1",
    "ca9dd2a2-d1df-5445-9e34-923a20c2bfaf",
    "59bcd221-a84a-513b-af5d-777ebeab2a88",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }

  for (const [id, conflictingName] of [
    ["5f75e958-e405-59bb-80b4-1b9766916e60", "WUNSCH HERMAN F"],
    ["29719ffc-dbc2-5dbd-a255-996f93e7ace6", "NICHOLSON CLYDE A"],
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText(conflictingName);
  }
});

test("Batch 701 updates exact coverage while retaining the oil-company directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,165");
  await expect(main).toContainText("38.28%");
  await expect(main).toContainText("319");
  await expect(main).toContainText("14,769");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
