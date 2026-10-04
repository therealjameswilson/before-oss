import { expect, test } from "@playwright/test";

const profiles = [
  ["d95fe6b3-1129-5bea-b1af-dacaea755ec0", "Robert E Parent"],
  ["c6ecdd1c-7241-533c-949b-09e2f9a6705d", "Dominick F Parenta"],
  ["da00ca96-e018-5e45-b1d3-20ef3dad124b", "Aurelius Parenti"],
  ["2129e85b-bd54-5f82-875e-bb7e7fc55732", "Rufus S Paret"],
  ["2e16caca-06fa-5a26-971c-7ee0401bc667", "Ernest L Paris"],
  ["9a4d9cf7-7e92-5c66-8d9e-44adeb5b1998", "Jesse Paris"],
  ["fa26ee39-1e10-5373-99ce-1f9b991bc13d", "Nelson B Paris"],
  ["c4d22d8b-b55f-5303-a521-09a22d842841", "Johnny E Parish"],
  ["04518ec0-84ed-573a-9f8b-7b0a5e49259f", "Bernard H Parisky"],
  ["d112c0c6-0dbf-50bd-bf73-11c3c45cb740", "Ki B Park"],
  ["3be57eb6-2f96-5bf4-a73f-5488f2deb8e8", "Susan B Park"],
  ["6aa16dc4-b198-55fd-8732-c48c4a1705cc", "Alton B Parker"],
  ["b0e2bf61-27b9-56c7-bd9c-fba915061adf", "Ann M Parker"],
  ["a90836a6-c62d-58e4-9130-16900a3ca45e", "Barbara B Parker"],
  ["ee3e85ab-12cc-5270-ac4c-84c540299de6", "Blanche V Parker"],
  ["3e283de6-e29a-5439-bb29-342e3accf790", "Charles S Parker"],
  ["d92b2998-72af-5f44-bbb2-66878b854b42", "Dema Parker"],
  ["0ef8fbe7-f19c-510c-8072-05ebc9d34900", "Evan J Parker Jr."],
  ["c4affa7e-9e45-5583-b998-373ac6d4642e", "Frank B Parker"],
  ["a7eeb5ae-cfe6-53a1-b99d-97b290fbd2c2", "Franklin P Parker"],
  ["f9ebe2fa-00c1-5367-b1ca-88b25823d08b", "Harold K Parker"],
  ["c6a29ecf-a8ef-5f1c-89d6-f4c5c825d609", "Henry S Parker"],
  ["3d5ca3cd-75c9-526e-8f77-624cbabaeffc", "Hilda B Parker"],
] as const;

test("Batch 734 publishes all 23 page-357 profiles with terminal dispositions", async ({ page }) => {
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

test("Batch 734 publishes Parker's Cornell relationship as student status only", async ({ page }) => {
  await page.goto("./people/0ef8fbe7-f19c-510c-8072-05ebc9d34900/");
  await expect(page.getByRole("heading", { name: "Evan J Parker Jr.", level: 1 })).toBeVisible();
  const main = page.locator("main");
  const immediate = page.locator("section[aria-labelledby='immediate-affiliation']");
  const civilian = page.locator("section[aria-labelledby='civilian-employer']");
  const earlier = page.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(immediate).not.toContainText("Cornell University");
  await expect(civilian).not.toContainText("Cornell University");
  await expect(earlier).toContainText("Cornell University");
  await expect(earlier).toContainText("student");
  await expect(earlier).toContainText("Class of 1941");
  await expect(main).toContainText("Cornell is not counted as an employer");
  await expect(main).toContainText("Evan J Parker, Jr., Interview");
});

test("Batch 734 confirms Nelson Paris without inventing a predecessor affiliation", async ({ page }) => {
  await page.goto("./people/fa26ee39-1e10-5373-99ce-1f9b991bc13d/");
  await expect(page.getByRole("heading", { name: "Nelson B Paris", level: 1 })).toBeVisible();
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("naval photographer");
  await expect(main).toContainText("Dawes Mission");
  await expect(main).toContainText("not the affiliation immediately before OSS service");
  await expect(page.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(page.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 734 exposes the Jesse Paris official-name conflict", async ({ page }) => {
  await page.goto("./people/9a4d9cf7-7e92-5c66-8d9e-44adeb5b1998/");
  await expect(page.getByRole("heading", { name: "Jesse Paris", level: 1 })).toBeVisible();
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("TRUITT GEORGE S");
  await expect(main).toContainText("no Army identity is accepted");
  await expect(main).toContainText("Box 585");
  await expect(main).toContainText("critical");
});

test("Batch 734 rebuilds exact coverage without changing verified-employer coverage", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,918");
  await expect(main).toContainText("41.43%");
  await expect(main).toContainText("14,016");
  await expect(main).toContainText("745");
  await expect(main).toContainText("334");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
