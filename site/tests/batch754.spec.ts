import { expect, test } from "@playwright/test";

const profiles = [
  ["b9779493-18f0-5771-9a91-992b08658189", "Agnes G Phelan"],
  ["ff22f73a-03ec-5cd1-811a-1faa5b139199", "Charles E Phelps"],
  ["c11c0a26-3124-5372-ace2-edb43456236d", "Flora L Phelps"],
  ["0710a8ff-887f-5165-a253-6d2f7479cd20", "Julia G Phelps"],
  ["1f389fd8-012b-5c3c-b061-27bd3355aeea", "Reginald H Phelps"],
  ["88bed4b5-c2f7-59bc-b32a-f76dfb802bc2", "William L Phelps"],
  ["82a95c9e-559d-5c31-b577-c46efc24cc7d", "William R Phelps"],
  ["f7f657b5-27c5-585a-8049-f93d9876079c", "Elizabeth Q Phenix"],
  ["a3f926c6-d13d-588a-af01-dd3996d143c5", "Richard Phenix"],
  ["119c9d09-b590-5439-b8c4-1aff574c75e4", "Albert J Phiebig"],
  ["105f93d6-e3c7-5feb-8e80-d31d0ed3c4e7", "George F Philip"],
  ["9983706b-352a-59be-8ee2-374f571e5c58", "Hallie L Philippi"],
  ["fa19cb0a-fb2c-5c23-b2b8-7d9ff235ee39", "Karl Philippi"],
  ["46ac8731-354f-5472-a80f-15341aea2637", "Stephanos J Philippides"],
  ["a261de56-3f4d-5405-b89d-d7b796e34e81", "Jacques L Philippot"],
  ["c9949871-bc62-5639-bb3d-a93c3705997f", "Alexander P Phillips"],
  ["56255a53-016a-52ea-846d-deabda4e026f", "Beatrice Phillips"],
  ["1efafd71-6387-5ba5-b731-469586069bd1", "Earl L Phillips"],
  ["7f52a572-3194-5d82-a503-27c6007eb25d", "Frederick L Phillips"],
  ["8f5250c8-2556-5305-8ce3-5b6c763fb74a", "George C Phillips"],
  ["8e20a25c-4582-5388-9166-b4c9c46a74dd", "Harry P Phillips"],
  ["ab0ca33f-84bc-50f0-8fb9-0f44d399c9d8", "John M Phillips"],
  ["497fd6ab-0158-5158-990b-62087a760631", "John S Phillips"],
] as const;

test("Batch 754 publishes all 23 page-367 profiles with reviewed outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 754 publishes Reginald Phelps's strongly bounded Harvard employment", async ({ page }) => {
  await page.goto("./people/1f389fd8-012b-5c3c-b061-27bd3355aeea/");
  const main = page.locator("main");
  await expect(main).toContainText("Harvard");
  await expect(main).toContainText("German instructor and administrator");
  await expect(main).toContainText("strongly date bounded");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Harvard",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Harvard",
  );
});

test("Batch 754 keeps Julia Phelps's student status separate from employment", async ({ page }) => {
  await page.goto("./people/0710a8ff-887f-5165-a253-6d2f7479cd20/");
  const main = page.locator("main");
  await expect(main).toContainText("Radcliffe");
  await expect(main).toContainText("undergraduate student");
  await expect(main).toContainText("student");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 754 preserves the Jacques Philippot identity conflict", async ({ page }) => {
  await page.goto("./people/a261de56-3f4d-5405-b89d-d7b796e34e81/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("completely different name");
  await expect(main).toContainText("records remain separate");
  await expect(main).not.toContainText("Army occupation");
});

test("home page exposes the rebuilt Batch 754 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,371");
  await expect(home).toContainText("43.32%");
  await expect(home).toContainText("13,563");
  await expect(home).toContainText("774");
  await expect(home).toContainText("344");
  await expect(home).toContainText("8,830");
});
