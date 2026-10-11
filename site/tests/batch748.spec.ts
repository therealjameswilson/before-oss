import { expect, test } from "@playwright/test";

const profiles = [
  ["249b45ef-bd24-533c-b9f7-d238e095d9be", "Harold C or Perry"],
  ["f732a621-5a6f-5646-8300-d83126505d95", "Hart Perry"],
  ["77458b2f-ada9-54e3-87df-8c4b820e42df", "Homer L Perry"],
  ["7200d6d1-9460-5f33-9957-dd960dfedc0f", "James B Perry"],
  ["ed1163b6-873b-58ff-b1ad-256a6059aebf", "James E Perry"],
  ["b2c6f43e-c5c6-5dab-8620-938102ce046b", "John S Perry"],
  ["c040e52a-cc77-551f-8b1c-b3a560fd00e1", "John T Perry"],
  ["9f83b2f4-f13c-5459-99d8-5b2dc828cdb8", "Josephine V Perry"],
  ["46eb9c0b-00af-5047-a367-3cc215e30d6a", "Lizzie Perry"],
  ["6c664959-e91d-5ec7-b35b-536ab4578f92", "Manuel S Perry"],
  ["8768f3dc-7129-5efb-a40b-6fbd03268f25", "Margaret Perry"],
  ["44d836de-8a45-56ef-897f-8cc4b4404452", "Phillip P Perry"],
  ["6f4b22a5-e704-5f3d-a838-8d3e6a89d5c4", "Robert Perry"],
  ["a67b64e1-e2b5-5039-8ca4-9ce765fa8abd", "Robert L Perry"],
  ["a34626aa-c744-5ef5-be5c-82331cb0b31b", "Robert Perry"],
  ["fa6a6f7c-a329-5bc0-a7b8-f185da40f2b8", "Thomas F Perry"],
  ["f1a3dedc-80c3-57d8-afef-724333e57dbc", "William E Perry"],
  ["8972240e-d175-538c-b541-09a9ecd98062", "William R Perry"],
  ["05147dd2-b5d4-5502-b577-0246d8422905", "Albert O. J. Persechino"],
  ["e1ac3273-6a7f-57b0-989f-2a05a53abb1c", "Anthony Perseo"],
  ["0ce35006-2528-5f80-9cbf-c6e5f12ce7c2", "James R Pershall"],
  ["fd1265a7-8efd-5ed5-b718-1174c522cef7", "William R Pershing"],
  ["fdcb0d50-8031-5109-bcb2-660529e5b05c", "Helen Persky"],
] as const;

test("Batch 748 publishes all 23 page-364 profiles with terminal reviewed outcomes", async ({ page }) => {
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

test("Hart Perry publishes Chicago as student status, never as an employer", async ({ page }) => {
  await page.goto("./people/f732a621-5a6f-5646-8300-d83126505d95/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Chicago");
  await expect(main).toContainText("Master of Arts student");
  await expect(main).toContainText("Hart Perry, AM'39");
  await expect(main).toContainText("high documented pre-OSS");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "University of Chicago",
  );
});

test("Batch 748 preserves identity conflicts without exposing full protected identifiers", async ({ page }) => {
  await page.goto("./people/77458b2f-ada9-54e3-87df-8c4b820e42df/");
  await expect(page.locator("main")).toContainText("YAGER MELVIN C");
  await expect(page.locator("main")).toContainText("conflicting");

  await page.goto("./people/7200d6d1-9460-5f33-9957-dd960dfedc0f/");
  const james = page.locator("main");
  await expect(james).toContainText("PEERY JAMES B");
  await expect(james).toContainText("Remove");
  await expect(james).toContainText("Boxes 593 and 597");
  await expect(james).not.toContainText("38091139");
});

test("the two source rows named Robert Perry remain separate profiles", async ({ page }) => {
  await page.goto("./people/6f4b22a5-e704-5f3d-a838-8d3e6a89d5c4/");
  await expect(page.locator("main")).toContainText("Extract fr");
  await expect(page.locator("main")).not.toContainText("Also in B");

  await page.goto("./people/a34626aa-c744-5ef5-be5c-82331cb0b31b/");
  await expect(page.locator("main")).toContainText("Also in B");
  await expect(page.locator("main")).not.toContainText("Extract fr");
});

test("home page exposes the rebuilt Batch 748 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,234");
  await expect(home).toContainText("42.75%");
  await expect(home).toContainText("13,700");
  await expect(home).toContainText("764");
  await expect(home).toContainText("340");
  await expect(home).toContainText("8,693");
});
