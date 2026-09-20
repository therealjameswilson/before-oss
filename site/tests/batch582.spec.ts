import { expect, test } from "@playwright/test";

const cohort = [
  ["4f720acb-3589-5ea2-887c-975af2e002a9", "Ann J Dick", 185],
  ["ca30a4a5-e1aa-5490-b6a7-e5b08cfd59dc", "Doris R Dick", 185],
  ["5d21d605-2eab-56f1-8d52-7a95a8c41ae7", "David H Dickason", 185],
  ["76d8b004-fdff-5747-88ef-2c74edddd985", "Frederick G Dickason", 186],
  ["e3e5aed7-e9be-5ceb-8b3b-ead0c9e9d3c6", "Samuel Dicken", 186],
  ["cfec3f26-d75a-53e9-9126-e1c9456c16f5", "Roger H Dickens", 186],
  ["8f2b63e7-4749-52b6-8744-98a3875fb741", "William B Dickens", 186],
  ["776f68d5-9f3d-58fd-b8dd-0c75d18570f3", "Thelma W Dickerman", 186],
  ["76dc4560-6f0a-5b02-a3a2-d4815e0e0419", "Gelnn O Dickerson", 186],
  ["069e0379-3fd1-5002-802b-7ed37128e5e4", "Harold E Dickerson", 186],
] as const;

test("batch 582 retains all ten direct profiles and archival next steps", async ({ page }) => {
  for (const [id, name, box] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText(`Box ${box}`, { exact: false }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  }
});

test("three Army identity matches are cited without becoming employers", async ({ page }) => {
  for (const id of [cohort[5][0], cohort[8][0], cohort[9][0]]) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" })).toBeVisible();
    await expect(page.getByText("No publishable pre-OSS affiliation is recorded yet")).toBeVisible();
  }
});

test("original Gelnn spelling is displayed with documented Glenn variant", async ({ page }) => {
  await page.goto(`./people/${cohort[8][0]}/`, { waitUntil: "domcontentloaded" });
  await expect(page.getByRole("heading", { name: "Gelnn O Dickerson", exact: true })).toBeVisible();
  await expect(page.getByText("Glenn O Dickerson", { exact: false }).first()).toBeVisible();
});
