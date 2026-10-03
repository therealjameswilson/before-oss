import { expect, test } from "@playwright/test";

const profiles = [
  ["096c796d-fdfd-5e53-89d1-65a8007adb29", "Chalen Mory"],
  ["559293bf-10ad-51b1-9e16-3dea6311feca", "Jacob Mosak"],
  ["a42ccfdb-ebef-5061-b7cc-bfe13ed35d2c", "George Moschinsky"],
  ["1bec1e31-cd74-5b63-8dcd-bf97857bfd5f", "Amos D Moscrip"],
  ["627c4fc2-5d3d-523c-bd89-5dc36cb12d17", "Cornelia N Mose"],
  ["53dd9647-c9ad-5ea8-846c-83cd6d492ffa", "Eric O Mose"],
  ["5ff872fa-49f6-549e-a711-fb6ba542fd9c", "John Moseley"],
  ["baae9246-72b6-517f-b4d1-d10550b43ac6", "Margaret V Moseley"],
  ["b22b3137-5136-54d6-865e-92462d95e5a5", "Rea B Moseley"],
  ["fa153acf-8e4a-5165-a658-e450ac19b3a0", "Herbert G Moselle"],
  ["86d85b71-ed82-5b7f-87dd-0d456d58ff3d", "Philip E Mosely"],
  ["3c56f40b-fb2d-5156-a108-bc4abcb703d0", "Henry B Moses"],
  ["a128ac7b-21b3-517c-b35d-b482c96c92a4", "James R Moses"],
  ["67e93c01-13d1-57d0-82aa-ff6556baf2ef", "McClora Moses"],
  ["f813cd0a-494e-510d-8529-c941a8111579", "Mabelle W Mosher"],
  ["17eb6fff-08f6-53e0-97f0-ee2d4e8e540b", "Robert K Mosher"],
  ["d23c1171-aa67-582f-a29f-51d16bfed825", "Peter M Moshopoulos"],
  ["328e264d-ee5a-5175-81d2-5adb5c38d59d", "Edward A Mosk"],
  ["009304fa-1015-5982-9ca6-ac3866171b7b", "Jerome Moskol"],
  ["73467274-45e9-5d60-aae1-ba2c729416a3", "Theodore Moskowitz"],
  ["a3aa70e6-d560-532a-af7f-d28a39eb7e16", "Mary Moskwa"],
  ["5b235c6b-244b-59a9-9042-26ab4653c0fe", "Ann C Mosleh"],
  ["034deca5-4449-5c0e-8d58-d0936af4b656", "Rosa Mosler"],
] as const;

test("Batch 682 publishes all 23 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 331");
    await expect(page.locator("main")).toContainText("Archive box");
  }
});

test("Batch 682 separates Jacob Mosak's civilian employer from his government assignment", async ({ page }) => {
  await page.goto("./people/559293bf-10ad-51b1-9e16-3dea6311feca/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Chicago");
  await expect(main).toContainText("Office of Price Administration");
  await expect(main).toContainText("economics instructor");
  await expect(main).toContainText("verified employer found");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("University of Chicago");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("Office of Price Administration");
});

test("Batch 682 publishes Amos Moscrip's Army pathway without inventing civilian employment", async ({ page }) => {
  await page.goto("./people/1bec1e31-cd74-5b63-8dcd-bf97857bfd5f/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("101st Anti-Tank Battalion");
  await expect(main).toContainText("military assignment");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("101st Anti-Tank Battalion");
});

test("Batch 682 qualifies Edward Mosk's private legal practice and names no unsupported firm", async ({ page }) => {
  await page.goto("./people/328e264d-ee5a-5175-81d2-5adb5c38d59d/");
  const main = page.locator("main");
  await expect(main).toContainText("private legal practice");
  await expect(main).toContainText("attorney");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("documented prewar employer found");
  await expect(main).toContainText("no prewar firm name has been verified");
});

test("Batch 682 preserves the John Moseley and Philip Mosely conflict without merging profiles", async ({ page }) => {
  await page.goto("./people/5ff872fa-49f6-549e-a711-fb6ba542fd9c/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("probable error for Philip E. Mosely");
  await expect(main).toContainText("separate John Moseley and Philip E. Mosely rows");
  await expect(main).not.toContainText("Cornell University professor");

  await page.goto("./people/86d85b71-ed82-5b7f-87dd-0d456d58ff3d/");
  main = page.locator("main");
  await expect(main).toContainText("Cornell University");
  await expect(main).toContainText("verified employer found");
});

test("Batch 682 preserves both Peter Moshopoulos spellings as an unresolved identifier conflict", async ({ page }) => {
  await page.goto("./people/d23c1171-aa67-582f-a29f-51d16bfed825/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Peter M Moshopoulos");
  await expect(main).toContainText("Peter M Mishopoulos");
  await expect(main).toContainText("Duplicate group");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 682 publishes four identifier-supported Army identities without employer claims", async ({ page }) => {
  const armyIdentities = [
    "a42ccfdb-ebef-5061-b7cc-bfe13ed35d2c",
    "17eb6fff-08f6-53e0-97f0-ee2d4e8e540b",
    "009304fa-1015-5982-9ca6-ac3866171b7b",
    "73467274-45e9-5d60-aae1-ba2c729416a3",
  ];

  for (const id of armyIdentities) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 682 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,736");
  await expect(page.locator("body")).toContainText("36.49%");
  await expect(page.locator("body")).toContainText("307");
  const category = page.locator("#oil-companies");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator(".oil-directory__person")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil companies");

  await page.goto("./people/");
  await expect(page.locator(".featured-directory-category li")).toHaveCount(8);
});
