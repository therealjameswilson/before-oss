import { expect, test } from "@playwright/test";

const profiles = [
  ["2be4cd30-69a7-52ad-877c-6ea8c8226c4b", "Arthur J Parry"],
  ["cc5a259c-b5f4-5464-8796-eec57f8a343e", "George G Parry"],
  ["08726339-45a4-543d-843b-e2d5c5e2bdd7", "Richard Parry"],
  ["cd417b85-a1c5-59ac-987d-10de32ad61b3", "William E Parry"],
  ["c08b2012-ce37-58df-9155-4314bc554f8e", "Edward M Parsen"],
  ["d8655c37-f95b-5520-976d-908229e4354b", "Edward D Parsons"],
  ["1ee99623-479e-5efb-96bd-bb45fae47a65", "Edwin O Parsons"],
  ["307410fb-a218-5c63-9853-96724d627fb1", "Gustav A Parsons"],
  ["4d290966-e6db-565a-870b-0f708178e7fe", "Harvey Parsons"],
  ["60668860-890c-52fa-b35a-a59c2dd22ce0", "Ira H Parsons"],
  ["ac843848-e217-5b90-a9f8-f0a346949865", "Mimi Parsons"],
  ["7d9c1e22-2bcc-5c60-9b29-1dfab1cfe08f", "James I Partain"],
  ["cfbb437e-b3de-526c-9036-c727a8ca83fe", "Marvin F Partain"],
  ["3f39a037-7d05-593a-8af9-c61dde232586", "Joe M Partin"],
  ["642e6ea1-27b5-500b-86df-15a04c703dd9", "Allen V Partington"],
  ["5c8089ad-74c0-5fd8-aa41-b45700e0358d", "Yvette A Partington"],
  ["8079dba3-d014-5410-b581-01adb44ee6c0", "Herman H Partnon"],
  ["00739bc1-093a-5699-96ca-d88e3b13a9b5", "Dominggus Pasalbessy"],
  ["97fbe94e-09b6-57e3-bb08-5166b862746d", "Jacintha Pascal"],
  ["31e184a6-485e-5c10-8df3-f416d6dc6db5", "Norman S Pascal"],
  ["1bb66f7c-fda1-56f6-b305-fc16f10f32d4", "Paul A Pasco"],
  ["f73b8021-c972-5247-8858-d6f7a3f71bff", "John J Pascoe"],
  ["0205dfb9-117e-5744-a3fa-83b37aef7966", "John Pascone"],
] as const;

test("Batch 736 publishes all 23 page-358 profiles with terminal dispositions", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
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

test("Batch 736 exposes both official protected-identifier conflicts", async ({ page }) => {
  await page.goto("./people/cd417b85-a1c5-59ac-987d-10de32ad61b3/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("WILSON DEMPSEY F");
  await expect(main).toContainText("critical");

  await page.goto("./people/cfbb437e-b3de-526c-9036-c727a8ca83fe/");
  main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("SIMPSON ARVEL J");
  await expect(main).toContainText("LYANCDALE F");
  await expect(main).toContainText("critical");
});

test("Batch 736 preserves printed foreign and incomplete notes", async ({ page }) => {
  await page.goto("./people/c08b2012-ce37-58df-9155-4314bc554f8e/");
  await expect(page.locator("main")).toContainText("Belgian");

  await page.goto("./people/4d290966-e6db-565a-870b-0f708178e7fe/");
  await expect(page.locator("main")).toContainText("Norwegi");

  await page.goto("./people/1bb66f7c-fda1-56f6-b305-fc16f10f32d4/");
  await expect(page.locator("main")).toContainText("French");
  await expect(page.locator("main")).toContainText("S/Lt");

  await page.goto("./people/0205dfb9-117e-5744-a3fa-83b37aef7966/");
  await expect(page.locator("main")).toContainText("Refer to");
  await expect(page.locator("main")).toContainText("Box 588");
});

test("Batch 736 keeps Army identity evidence separate from employer evidence", async ({ page }) => {
  for (const id of [
    "2be4cd30-69a7-52ad-877c-6ea8c8226c4b",
    "c08b2012-ce37-58df-9155-4314bc554f8e",
    "1ee99623-479e-5efb-96bd-bb45fae47a65",
    "60668860-890c-52fa-b35a-a59c2dd22ce0",
    "642e6ea1-27b5-500b-86df-15a04c703dd9",
    "31e184a6-485e-5c10-8df3-f416d6dc6db5",
    "0205dfb9-117e-5744-a3fa-83b37aef7966",
  ]) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 736 rebuilds exact coverage without changing employer or affiliation totals", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,962");
  await expect(main).toContainText("41.61%");
  await expect(main).toContainText("13,972");
  await expect(main).toContainText("745");
  await expect(main).toContainText("334");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
