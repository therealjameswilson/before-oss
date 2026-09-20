import { expect, test } from "@playwright/test";

const cohort = [
  ["2a4986cb-3d6d-56b9-9610-1b566a8cebba", "Louis Dilworth", "Box 187"],
  ["98bb1194-1928-5134-a8dc-aaedbb81bd32", "Luigi DiMaggio", "Box 187"],
  ["7b01cdcb-4928-5813-9e1a-55291339fda5", "Nick L DiMarco", "Box 187"],
  ["9d0631ee-c5d7-5902-8c52-bd7b5aae2542", "Charles DiMary", "Box 187"],
  ["cb0b4bd4-dd0a-59c2-8187-6cf5269c9041", "Jim Dimas", "Box 187"],
  ["058410c0-0ffd-5a38-9c8b-a00608a19af7", "Salvatore DiMattino", "Box 188"],
  ["53cfdc24-1461-5d1c-ae43-076b810b473d", "Orlando F Dimenna", "Box 188"],
  ["4dc5ec08-d157-54ef-aeab-0061112e5e56", "John M Dimick", "Box 188"],
  ["6ec07f7d-6597-5cd5-b0b8-b2fb2b1adec5", "Gaetano Dimille", "Box 188"],
  ["156efb97-35cf-5c84-906d-6ef5850814ae", "Victor Dimitrijevich", "Box 188"],
  ["c98622d7-70a9-592a-bc28-be5f47c293f9", "D M Dimond", "Box 188"],
  ["ea4e4cde-ec70-5e86-8067-70a4454bcc0c", "Vito Dinanno", "Box 188"],
  ["d313ecc6-073d-526b-82af-d5d7565b519f", "Peter DiNatale", "Box 188"],
  ["fe3efa4e-21a3-533b-a2e3-e94744aa0407", "Eugene A Dinet Jr.", "Box 188"],
  ["3c9ee495-cc45-598a-9872-93298281d77a", "Martin Dinga", "Box 188"],
  ["c332b1ff-219e-55f8-aec3-660607cea289", "Richard S Dinner", "Box 188"],
] as const;

test("batch 586 preserves all sixteen printed-row profiles and archival boxes", async ({ page }) => {
  for (const [id, name, box] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText(box, { exact: false }).first()).toBeVisible();
  }
});

test("Dinga has a cited immediate Red Cross affiliation without national-society expansion", async ({ page }) => {
  await page.goto(`./people/${cohort[14][0]}/`, { waitUntil: "domcontentloaded" });
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(immediate.locator(".affiliation-card")).toHaveCount(1);
  await expect(civilian.locator(".affiliation-card")).toHaveCount(1);
  await expect(immediate.getByRole("link", { name: "Red Cross (society unspecified)" })).toBeVisible();
  await expect(immediate.locator(".affiliation-card")).not.toContainText("social-work role");
  await expect(page.getByRole("link", { name: /OSS Cairo field-board personnel interviews/ }).first()).toBeVisible();
  await expect(page.locator("body")).not.toContainText("American Red Cross");
});

test("a surname-only newspaper hit and postwar teaching do not become employers", async ({ page }) => {
  for (const index of [7, 10, 13]) {
    await page.goto(`./people/${cohort[index][0]}/`, { waitUntil: "domcontentloaded" });
    await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  }
});
