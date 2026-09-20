import { expect, test } from "@playwright/test";

const cohort = [
  ["5d6b32b8-8a79-53cd-95c7-5977e7c9b589", "Romeo P Digiulian", "Box 186"],
  ["16bfb398-23e4-54e7-a415-ecea34bff33e", "Armand Digliani", "Box 187"],
  ["2ddc4dfb-270d-540c-986f-d0eb9c333161", "Grant Dignall", "Box 187"],
  ["5d68ee52-811d-5916-af0e-460d4814c440", "Alfred Dilello", "Box 187"],
  ["4f5bfca0-620b-5753-9b64-cd52aa9b38d9", "Josephine Dilibertok", "Box 187"],
  ["659fcc55-f4eb-5a08-87ad-794ffdf93929", "George Dill", "Box 187"],
  ["923fa1dc-9cab-5ea1-861f-80667dfd563c", "Chester A Dillahunt", "Box 187"],
  ["77330187-3f50-5a2b-87d3-89d6d164610a", "John R Dillard", "Box 187"],
  ["ab7802ef-09f4-5a3c-bfca-92b27d9df36f", "Andrew Diller", "Box 187"],
  ["cfbb2674-ea02-5f87-ac86-0ea33bee8e96", "Donald D Diller", "Box 187"],
  ["f555e18e-34df-539e-a68f-0006bc3d4765", "Clair F Dillman", "Box 187"],
  ["41e2aaab-fe3a-566a-88d1-3b2ca695e6e8", "E P Dillon", "Box 187"],
  ["c9102e4f-6843-56f8-95b9-0446e50c04ba", "Robert G Dillon", "Box 187"],
  ["66712c7d-cf9d-56cc-b218-66fcc2860e04", "Trefon J Dillon", "Box 187"],
  ["2bdf400e-1ac7-5613-89fb-c8898155472a", "William J Dillon", "Box 187"],
  ["a28936e3-5a81-5809-87aa-f5b369764c33", "William F Dillon", "Box 187"],
  ["5c4b0cd6-8f61-5cc7-8523-0ec57281950b", "John B Dillon Jr.", "Box 187"],
  ["ede6d2cb-cd90-5104-bc1b-2d9a23c14c9f", "Konrad C Dillow", "Box 187"],
  ["25745a0c-2b3c-5216-8fb2-8a5d8e149fd6", "Alfred H Diloreto", "Box 187"],
  ["4cd23e6e-1b17-5904-9268-44fdc306746e", "Elizabeth S Dilworth", "Box 187"],
] as const;

test("batch 585 preserves twenty distinct direct profiles and no invented employer", async ({ page }) => {
  for (const [id, name, box] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText(box, { exact: false }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  }
});

test("Dillow's cited graduate fellowship is student affiliation, not a university employer", async ({ page }) => {
  await page.goto(`./people/${cohort[17][0]}/`, { waitUntil: "domcontentloaded" });
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(earlier.locator(".affiliation-card")).toHaveCount(1);
  await expect(earlier.getByRole("link", { name: "University of Illinois" })).toBeVisible();
  await expect(earlier.getByText("Graduate fellow in Education")).toBeVisible();
  await expect(earlier.getByText(/student/)).toBeVisible();
  await expect(page.getByRole("link", { name: /Minutes of the Board of Trustees, University of Illinois, April 14, 1937/ }).first()).toBeVisible();
  await expect(page.locator("body")).not.toContainText("University of Illinois employer");
});

test("namesake employers and clipped notes do not become assertions", async ({ page }) => {
  await page.goto(`./people/${cohort[16][0]}/`, { waitUntil: "domcontentloaded" });
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
  await page.goto(`./people/${cohort[10][0]}/`, { waitUntil: "domcontentloaded" });
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
  await page.goto(`./people/${cohort[11][0]}/`, { waitUntil: "domcontentloaded" });
  await expect(page.getByText("British A", { exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
});
