import { expect, test } from "@playwright/test";

const profiles = [
  ["86cab551-d9c2-593b-ad8b-363e01a3b88f", "James G Nelligan"],
  ["05a852f2-a003-521e-b637-f8cddfd0740c", "Adeline M Nelson"],
  ["d63a0190-43c2-5855-9102-e3179e3356c2", "Andrew E Nelson"],
  ["f863d315-95a5-59ff-88b3-09889ff0d610", "Aubrey W Nelson"],
  ["5d66834d-80cb-5ac2-9e90-7f1609c6befc", "B M Nelson"],
  ["524a02a4-33c6-5645-bf25-ab1d86c8b178", "Carl G Nelson"],
  ["1b18f78c-aaf3-5693-a899-edeb5533fc54", "Carl W Nelson"],
  ["994ab371-0b3d-529d-a88f-8c0a11cb5ff7", "Charles H Nelson"],
  ["d0ff415b-5cf5-57a2-8055-8182021f4625", "Charles W Nelson"],
  ["dc7bbdc1-9433-5570-bf8c-1d4023e4780e", "Charles R Nelson"],
  ["f16c16f2-556d-56de-a3a8-a41d45313538", "Clifford R Nelson"],
  ["e46d7412-66ca-5b25-a9c3-c037fbf6a2bb", "Donald S Nelson"],
  ["77b61c17-a3a5-50b2-a2c3-e23f29805807", "Edward Nelson"],
  ["eec63e89-f798-5e97-a467-7c53f5c25ec5", "Florence V Nelson"],
  ["d212f11d-df04-5581-a2d9-c7d770597ff1", "Frank G Nelson"],
  ["f344723a-f9bd-5a06-89f4-7d1c5f5a8d90", "Franklin Nelson"],
  ["dd7ee40f-24e4-5302-a9ae-09407f13025a", "Gilmer H Nelson"],
  ["28ba6048-8675-5295-b65e-789b552098bd", "Gladys E Nelson"],
  ["9b1de10b-3695-5649-8bd3-a9018680bd70", "Harold G Nelson"],
  ["a044bf3c-65dc-54d1-b089-50f483ffff3e", "Herman Nelson"],
  ["56168bc1-46e8-5a16-8d27-942e1c170f52", "Ingolv Nelson"],
  ["d96ca83a-99dd-5526-808b-710aa72f0323", "Irene R Nelson"],
  ["04f30f74-d102-59cb-bc23-aaa435d669cf", "Isadore Nelson"],
] as const;

test("Batch 698 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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

test("Batch 698 publishes official OSS-role evidence without inventing employment", async ({ page }) => {
  await page.goto("./people/9b1de10b-3695-5649-8bd3-a9018680bd70/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Operational Group Command Special Orders Number 9");
  await expect(main).toContainText("Special Reconnaissance Battalion");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);

  await page.goto("./people/56168bc1-46e8-5a16-8d27-942e1c170f52/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Operation BOSTON");
  await expect(main).toContainText("P-101 crew");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 698 keeps both protected-identifier conflicts visible", async ({ page }) => {
  await page.goto("./people/994ab371-0b3d-529d-a88f-8c0a11cb5ff7/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Evidence conflict");
  await expect(main).toContainText("THOMALLA EMANUEL V");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);

  await page.goto("./people/d0ff415b-5cf5-57a2-8055-8182021f4625/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Evidence conflict");
  await expect(main).toContainText("NELSENJCHARLES W");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 698 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("9,098");
  await expect(body).toContainText("38.00%");
  await expect(body).toContainText("317");
  await expect(body).toContainText("14,836");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
