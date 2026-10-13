import { expect, test } from "@playwright/test";

const profiles = [
  ["43dbed37-7e56-5645-85e1-7d1f04ba9279", "George L Piday"],
  ["60b85b90-9779-5082-8586-94c87af93e7d", "Edward J Piekanski"],
  ["d354f911-cca0-5a98-a887-911ea1825fa8", "Frank W Piekarczyk"],
  ["4cd22f0c-3d9a-5393-b446-8f77f3d34310", "Rosemond M Pielke"],
  ["1cf55845-ec2e-5bc4-aaaf-b5c4d77a8b2c", "Kenneth M Pier"],
  ["c7276c33-f457-573d-b8bc-9d2730be76b6", "Spiros D Pieratos"],
  ["ff6d6d2a-31af-5a12-9ef6-e413ea94e8e9", "Christian J Pierce"],
  ["567ade6d-718a-5244-a55b-461a26448c08", "Donald S Pierce"],
  ["35088b49-20f5-5259-80f0-dcea1f5d4963", "Frederick S Pierce"],
  ["a4d0d342-4d4d-544b-8c5f-371aee29f703", "George W Pierce"],
  ["11b65116-afa0-5feb-b007-5c7250fb2971", "Guy R Pierce"],
  ["9897a524-bbfe-536c-bf27-f48df65031ac", "Hubert B Pierce"],
  ["8fd4d85c-804c-5316-bbbb-bd2a277e927a", "W Ruth Pierce"],
  ["312aeb6c-9f16-57d1-a6c9-dcd364d8a266", "Roger L Pierre"],
  ["acdb754c-da44-51b4-98d3-5616303399fe", "Gilbert Pierrel"],
  ["b9419cee-247e-56d6-9b7d-735abae167f5", "Esther Pierson"],
  ["e9430935-ce25-5cf4-a88d-bdb151cf5084", "Glen Pierson"],
  ["247c1b7b-a8ca-57e7-8f2c-12a07db18d4c", "Robert C Pierson"],
  ["5ac5eca1-a440-5d4b-b984-8aa933c5f9d6", "Walter R Pierson"],
  ["0b627837-9fe2-5bdd-a708-832ade849f96", "Anna V Pietri"],
  ["af984cb1-71cc-5416-9e81-893067f9a431", "Emmanuel Pietromartire"],
  ["1539d17f-4a77-52cf-8554-049e4b306131", "Bernard M Pietrowiak"],
  ["a9b80f7f-8285-5170-8106-8ee19150f6fd", "William H Pietsch"],
  ["01e210c8-374a-5564-b330-5aecbd56e0b3", "William H Pietsch"],
  ["96ae9209-72b9-5a07-a49f-55513004edb8", "Guido Pignatelli"],
  ["5f8b1dda-289c-570e-ac37-3065d20b6bf1", "Joseph W Pignatelli"],
  ["096dbd4b-4b7c-5f82-a1aa-507f93312857", "Edward J Pikanski"],
] as const;

test("Batch 757 publishes all 27 page-369 profiles with terminal outcomes", async ({ page }) => {
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

test("Batch 757 publishes Kenneth Pier's pre-OSS Navy assignment", async ({ page }) => {
  await page.goto("./people/1cf55845-ec2e-5bc4-aaaf-b5c4d77a8b2c/");
  const main = page.locator("main");
  const immediate = main.locator("section[aria-labelledby='immediate-affiliation']");
  await expect(immediate).toContainText("U.S. Navy Field Photographic Office");
  await expect(immediate).toContainText("Before July 1944");
  await expect(immediate).toContainText("military assignment");
  await expect(main).toContainText("The Office of Strategic Services (OSS) Maritime Unit on the Arakan Coast of Burma");
  await expect(main).toContainText("assigned to the Navy's Field Photographic Office");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 757 separates Robert Pierson's Army pathway from student status", async ({ page }) => {
  await page.goto("./people/247c1b7b-a8ca-57e7-8f2c-12a07db18d4c/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "United States Army",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Immediately before OSS assignment",
  );
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText(
    "West Virginia University",
  );
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText(
    "student",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "West Virginia University",
  );
  await expect(main).toContainText("The army assigned him to the Office of Strategic Services");
});

test("Batch 757 preserves both Pietsch rows and the Piekanski-Pikanski conflict", async ({ page }) => {
  for (const id of [
    "a9b80f7f-8285-5170-8106-8ee19150f6fd",
    "01e210c8-374a-5564-b330-5aecbd56e0b3",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("adjacent duplicate row");
    await expect(main).toContainText("probable");
    await expect(main).toContainText("Uniform of OSS Col. William H. Pietsch, Jr.");
  }

  await page.goto("./people/60b85b90-9779-5082-8586-94c87af93e7d/");
  await expect(page.locator("main")).toContainText("Edward J Pikanski");
  await expect(page.locator("main")).toContainText("conflict");

  await page.goto("./people/096dbd4b-4b7c-5f82-a1aa-507f93312857/");
  await expect(page.locator("main")).toContainText("Edward J Piekanski");
  await expect(page.locator("main")).toContainText("conflict");
});

test("Batch 757 publishes the Field Photographic Office organization page", async ({ page }) => {
  await page.goto("./organizations/ce2efa5c-9d4e-5586-83d6-68f1081e16df/");
  const main = page.locator("main");
  await expect(
    page.getByRole("heading", { name: "U.S. Navy Field Photographic Office", level: 1 }),
  ).toBeVisible();
  await expect(main).toContainText("Navy's Field Photographic Office");
  await expect(main).toContainText("Kenneth M Pier");
  await expect(main).toContainText("military");
});

test("home page exposes the rebuilt Batch 757 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,444");
  await expect(home).toContainText("43.63%");
  await expect(home).toContainText("13,490");
  await expect(home).toContainText("777");
  await expect(home).toContainText("345");
  await expect(home).toContainText("8,903");
});
