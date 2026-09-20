import { expect, test } from "@playwright/test";

const cohort = [
  ["5fc002c3-cd84-5c72-85c1-6622c44d8b03", "Edward T Dickerson Jr."],
  ["0f04fce9-444b-55c8-9c35-b10ab5c2543b", "Ruth M Dickey"],
  ["12b5d513-213e-5bd2-b7ed-14576c675947", "Thomas S Dickey Jr."],
  ["68941ec5-39d1-5062-8f28-15f268c84387", "Edward T Dickinson"],
  ["b3664234-c305-59dd-8067-2648bce19e77", "Philip C Dickinson"],
  ["68544af4-c5dc-51b5-9ecf-041676fee2d1", "Scott R Dickinson"],
  ["61398370-af32-581c-9800-fd86dbf31441", "William S Dickinson"],
  ["3c68add8-c3b0-5a33-9e28-cb133acb07d1", "William J Dickman"],
  ["e6474d0a-a47e-5081-9e39-1ec0906aee0d", "Byron R Dickson"],
  ["c10af0a4-a3c6-5fec-83a5-ac20ce03b49f", "Doyle E Dickson"],
  ["816217f8-3d25-59e0-8f4a-80a6261fb61e", "Edward T Dickson"],
  ["80b2f491-82be-57f8-ac7e-3fec68b8489a", "Frances A Dickson"],
  ["e72690fd-17f1-5ddc-9206-b71dd83fb41f", "Martin Dickson"],
  ["8c320001-bda3-54e5-9d84-fdf46b770a11", "William L Dickson"],
  ["8811876d-c7dc-5d5f-b779-e37d47df0576", "Angelo DiDomenico"],
  ["d312d6af-94a7-51cb-8140-767acc5c38f6", "William Diebod Jr."],
] as const;

test("batch 583 retains sixteen direct profiles and unresolved civilian employers", async ({ page }) => {
  for (const [id, name] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText("Box 186", { exact: false }).first()).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  }
});

test("Martin Dickson's Army pathway is qualified and not a civilian employer", async ({ page }) => {
  await page.goto(`./people/${cohort[12][0]}/`, { waitUntil: "domcontentloaded" });
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate.locator(".affiliation-card")).toHaveCount(1);
  await expect(immediate.getByText("United States Army")).toBeVisible();
  await expect(immediate.getByText("medium", { exact: true })).toBeVisible();
  await expect(page.getByRole("link", { name: "In Memoriam: Martin Dickson" }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: "Dickson, Martin Bernard" }).first()).toBeVisible();
});

test("Army name variants are preserved without assigning a civilian employer", async ({ page }) => {
  for (const [id, variant] of [
    [cohort[9][0], "Doyle E Diclson"],
    [cohort[14][0], "Angelo Di Domenico"],
  ] as const) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByText(variant, { exact: false }).first()).toBeVisible();
    await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  }
});
