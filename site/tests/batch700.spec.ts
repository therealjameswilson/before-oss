import { expect, test } from "@playwright/test";

const profiles = [
  ["ce3ad396-6246-5a4c-bfdf-05ae9f4b3245", "Frank B Nesbitt"],
  ["90010d13-b6b9-55cb-99dd-56db58ad4234", "Paul H Nesbitt"],
  ["884e9c2b-08ec-5362-8236-a89efb456bb8", "John E Nesline Jr."],
  ["2e2ff5fc-1fdd-54ee-8a93-2bcfd87d1eea", "Harriet J Nespodzany"],
  ["82499773-7f9d-545f-9f05-1c413f676afb", "Ervin T Ness"],
  ["c578afbc-3450-57b9-bd7e-3efa24bd6e39", "Harold E Ness"],
  ["bccb6020-2491-54b8-b558-89bdfd8e1017", "Mae L Ness"],
  ["1f439d78-f75a-5004-95f3-e4af8a0c292e", "Rudolph W Ness"],
  ["a99fed25-fd16-5035-944d-d23c3650086b", "Eileen A Nester"],
  ["2c0f1aa1-993c-5cbe-b9a7-fa3b2f689f09", "John C Nester"],
  ["5c006189-ed2c-5c8a-a275-6e7f48cf03c0", "Gladys R Nettles"],
  ["091ee5dc-82d8-5075-bd9a-15dcf4c82097", "Thomas E Nettles"],
  ["e63a0d61-5443-5b0d-b347-3c183b0aab63", "Arthur A Netzley"],
  ["cc6364ef-e750-55a5-82fb-e28445e46c53", "Arthur J Neu Jr."],
  ["220d340d-43b6-5f01-a57c-d87528bf3ab5", "Stanley P Neugebauer"],
  ["073bb3de-dcd8-5129-9b6d-802503aaf5a5", "Mary I Neuland"],
  ["1ebf1355-4c93-5569-9c5b-b37c6fe9666e", "Ernestine K Neumann"],
  ["9d917a08-06a5-5ec3-bebf-5c43b422a5aa", "Franz L Neumann"],
  ["9df2718f-34c1-56cb-930d-cd49392bc13d", "Gerhardt Neumann"],
  ["7e514818-c3d4-5231-a2bc-65c6761f62e4", "Otto Neumann"],
  ["317f54ac-1e67-567a-9030-8e6a4efda87b", "Robert G Neumann"],
  ["e5d55cc5-e295-5092-9100-c8a4b14e76d0", "Robert G Neumann"],
  ["4ebb85b3-0542-5281-b254-b36e810242bb", "Sigmund Neumann"],
] as const;

test("Batch 700 publishes all 23 direct profile routes with terminal or review outcomes", async ({ page }) => {
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

test("Batch 700 publishes identity-only decisions without inventing employers", async ({ page }) => {
  for (const id of [
    "ce3ad396-6246-5a4c-bfdf-05ae9f4b3245",
    "1f439d78-f75a-5004-95f3-e4af8a0c292e",
    "091ee5dc-82d8-5075-bd9a-15dcf4c82097",
    "cc6364ef-e750-55a5-82fb-e28445e46c53",
    "220d340d-43b6-5f01-a57c-d87528bf3ab5",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  }
});

test("Batch 700 documents Gerhard Neumann while preserving the indexed spelling", async ({ page }) => {
  await page.goto("./people/9df2718f-34c1-56cb-930d-cd49392bc13d/");
  const main = page.locator("main");
  await expect(main).toContainText("Gerhardt Neumann");
  await expect(main).toContainText("Gerhard Neumann");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("U.S. Army Air Corps");
  await expect(main).toContainText("American Volunteer Group");
  await expect(main).toContainText("Chinese Nationalist Air Force");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("Herman the German");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 700 keeps conflicts and the Robert G Neumann duplicate review visible", async ({ page }) => {
  await page.goto("./people/884e9c2b-08ec-5362-8236-a89efb456bb8/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("middle initial conflicts");

  await page.goto("./people/c578afbc-3450-57b9-bd7e-3efa24bd6e39/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("VINEYARD DELMAR I");

  for (const id of [
    "317f54ac-1e67-567a-9030-8e6a4efda87b",
    "e5d55cc5-e295-5092-9100-c8a4b14e76d0",
  ]) {
    await page.goto(`./people/${id}/`);
    main = page.locator("main");
    await expect(main).toContainText("Identity statusambiguous");
    await expect(main).toContainText("different protected identifiers");
    await expect(main).toContainText("Compare both Box 557 files");
  }
});

test("Batch 700 qualifies the Paul H Nesbitt lead and updates exact coverage", async ({ page }) => {
  await page.goto("./people/90010d13-b6b9-55cb-99dd-56db58ad4234/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Paul Homer Nesbitt");
  await expect(main).toContainText("no accessible source ties his life record to the indexed captain");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);

  await page.goto("./");
  main = page.locator("main");
  await expect(main).toContainText("9,142");
  await expect(main).toContainText("38.19%");
  await expect(main).toContainText("317");
  await expect(main).toContainText("14,792");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
