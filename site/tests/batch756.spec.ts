import { expect, test } from "@playwright/test";

const profiles = [
  ["e3879067-defa-5601-9be7-65297b362875", "Austin T Piazza"],
  ["ca1f14e0-84ac-5dc2-9a7f-69ea1f8b8abc", "Jean Piazza"],
  ["21f70504-3248-5d25-b27b-602da603f787", "Santo Piazza"],
  ["52f2095b-c836-5ae5-b561-93821d7e5dbb", "Marius J. R. Piberes"],
  ["327bf393-8839-542a-a27d-089b8fc81b40", "Eugene O Picard"],
  ["c464e2ae-a0db-57a0-b216-b630e1d942d2", "Joel J Picard"],
  ["027142f4-5206-5f03-98bf-b2760e8f9c61", "Lucian L Picard"],
  ["06d49479-0090-5cf1-bc7d-a34d303338ee", "Raymond N Picard"],
  ["fbfbf753-f951-5930-bdf2-246a1f9c2b7b", "George Piccardi"],
  ["48b02686-04de-5540-884c-881aa59b790c", "Constanzo Picco"],
  ["5c6064a3-f87c-584c-9fb4-7f84b0864d6a", "Edward Pichette"],
  ["bb305292-eeb0-5004-949a-ad50b6628155", "Germain V Pichon"],
  ["bf994ac1-300e-58e8-827f-a5a7dbcf4663", "Steve Picinich"],
  ["47cf6749-b0f2-5dbd-aa2c-faa5e876373e", "George Pick"],
  ["1345f27c-1414-5743-9a78-12e91b3e0377", "Robert G Pick"],
  ["70d8694d-1020-574c-8f1e-490402b4f24e", "Lawrence Pickard"],
  ["1958b1df-7a26-56c1-ad45-cf40f2dc2855", "Naomi Pickerel"],
  ["4951c6ee-1fd1-5d43-aaa7-934d557f1936", "Adrian Pickering"],
  ["c5a530a9-791b-586e-baec-678753f81d0d", "Arthur A Pickett"],
  ["3daa20f5-71fe-57e1-a7c5-6195873e1959", "India Pickett"],
  ["6829a5d6-9964-58cd-8c3e-0ad78254d214", "William F Pickles"],
  ["3fd04b2d-1380-5f23-b3b6-7b10e6bf2c02", "Lydia I Pickup"],
  ["df877230-34df-54b8-85a9-e9c75f9c45bf", "Sidney R Pickus"],
] as const;

test("Batch 756 publishes all 23 page-368 profiles with terminal outcomes", async ({ page }) => {
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

test("Batch 756 distinguishes Pickard's last civilian employer from immediate affiliation", async ({ page }) => {
  await page.goto("./people/70d8694d-1020-574c-8f1e-490402b4f24e/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "The Herald Statesman",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Before Army service",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main).toContainText("Broadcasting, February 25, 1946");
  await expect(main).toContainText("Before entering the Army");
  await expect(main).toContainText("82nd Airborne");
});

test("Batch 756 publishes the Herald Statesman organization page", async ({ page }) => {
  await page.goto("./organizations/484da27f-f1a9-55b1-a088-4e43fadc1ab3/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "The Herald Statesman", level: 1 })).toBeVisible();
  await expect(main).toContainText("Yonkers Herald-Statesman");
  await expect(main).toContainText("Lawrence Pickard");
  await expect(main).toContainText("journalism and media");
});

test("Batch 756 keeps both Sidney Pickus source rows visible", async ({ page }) => {
  await page.goto("./people/df877230-34df-54b8-85a9-e9c75f9c45bf/");
  const main = page.locator("main");
  await expect(main).toContainText("Both preserved Sidney R Pickus index rows");
  await expect(main).toContainText("Page 368");
  await expect(main).toContainText("Page 369");
});

test("home page exposes the rebuilt Batch 756 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,417");
  await expect(home).toContainText("43.51%");
  await expect(home).toContainText("13,517");
  await expect(home).toContainText("775");
  await expect(home).toContainText("345");
  await expect(home).toContainText("8,876");
});
