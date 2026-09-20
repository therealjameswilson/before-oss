import { expect, test } from "@playwright/test";

const cohort = [
  ["3a435f4b-3d5d-55d9-b80a-c195bdb3d0fd", "E A Dieckman", "Box 186"],
  ["9b8fe388-dc42-5509-9e31-629ac6624145", "Lee A Diehl", "Box 186"],
  ["a5568b42-b051-5187-bfc6-6c405aee10a7", "Arne Diesen", "Box 186"],
  ["e2b3f386-a853-578f-a056-05a837e15d1a", "Sigismond Diettrich", "Box 186"],
  ["29a6c452-934b-54cd-b09d-4afb7e354a46", "Glenwood A Dietz", "Box 186"],
  ["7392604d-a90d-5351-9b90-7b73cd170091", "John D Diffenbaugh", "Box 186"],
  ["dc0b2c6b-9c8b-5372-b319-a4ec5354cbdd", "Pierre Digeon", "Box 186"],
  ["d86ca689-e8cf-5972-a7fd-fe657d5d8997", "Reardon Dight", "Box 186"],
  ["6578105b-ef7d-5360-818e-992f76dca21b", "Augustine M Digiovanni", "Box 186"],
  ["78e5f873-6613-51e1-a2ac-b79280fe3d6c", "Gregory A Digiovanni", "Box 187"],
] as const;

test("batch 584 retains ten direct profiles and separates immediate from earlier employment", async ({ page }) => {
  for (const [id, name, box] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText(box, { exact: false }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  }
});

test("Diettrich's documented Florida employment is cited without claiming it immediately preceded OSS", async ({ page }) => {
  await page.goto(`./people/${cohort[3][0]}/`, { waitUntil: "domcontentloaded" });
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(earlier.locator(".affiliation-card")).toHaveCount(1);
  await expect(earlier.getByRole("link", { name: "University of Florida" })).toBeVisible();
  await expect(earlier.getByText("documented pre-OSS", { exact: true })).toBeVisible();
  await expect(page.getByRole("link", { name: "A Guide to the Sigismond deRudesheim Diettrich Papers" }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: "The Deltasig, March 1933" }).first()).toBeVisible();
});

test("Army identity variants appear without invented employers or unmasked serials", async ({ page }) => {
  for (const [id, variant] of [
    [cohort[7][0], "Reardon E Dight"],
    [cohort[8][0], "Augustine M Di Giovanni"],
  ] as const) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByText(variant, { exact: false }).first()).toBeVisible();
    await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" })).toBeVisible();
  }
  await expect(page.locator("body")).not.toContainText("33098797");
});

test("the source index's truncated note stays literal", async ({ page }) => {
  await page.goto(`./people/${cohort[2][0]}/`, { waitUntil: "domcontentloaded" });
  await expect(page.getByText("Norwegi", { exact: true })).toBeVisible();
});
