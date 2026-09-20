import { expect, test } from "@playwright/test";

const major = "1105c04b-ece7-557c-b84a-230d6fb00977";
const unnumbered = "04e1481b-c471-5892-9d61-579a7b2d2971";
const cohort = [
  ["475b54bf-2ece-59ab-817c-291ef46d22d2", "Ismael E Diaz"],
  ["d3b54bf8-250b-52cc-a85c-14888c14f056", "Joseph Diaz"],
  ["904ce055-2020-59ba-acba-88193ca7484f", "Marino Dibari"],
  [major, "George C Dibert"],
  [unnumbered, "George C Dibert"],
  ["ec72c2c9-5279-5c03-bbc3-468b937e7ebb", "Dominick N Diblasi"],
  ["e813de5e-63a0-5dec-915f-4acb48c91ec9", "John S Diblasi"],
  ["80aee59d-e7b4-5c90-a6fc-e8d3c1da20fc", "Charles Dibner"],
  ["61569c53-9c8c-5c06-96e2-d26affb2ccb5", "Susan W Dichter"],
  ["54f1e052-dfc1-5f30-a8dd-9a654e46b80a", "Louis D DiCicco"],
] as const;

test("batch 581 preserves ten direct Box 185 profiles with terminal online reviews", async ({ page }) => {
  for (const [id, name] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText("Box 185", { exact: false }).first()).toBeVisible();
    await expect(page.getByText(
      id === major ? "verified employer found" : "requires archival review",
      { exact: true },
    ).first()).toBeVisible();
  }
});

test("Major Dibert has cited last civilian employment, not an immediate OSS predecessor", async ({ page }) => {
  await page.goto(`./people/${major}/`, { waitUntil: "domcontentloaded" });
  const lastCivilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(lastCivilian.getByRole("link", { name: "J. Walter Thompson Co." })).toBeVisible();
  await expect(lastCivilian.getByText("high", { exact: true })).toBeVisible();
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate.getByText("No reviewed claim currently meets the publication threshold.")).toBeVisible();
  await expect(page.getByRole("link", { name: "Radio Warfare: OSS and CIA Subversive Propaganda" }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: "Agencies: George C. Dibert commissioned in the Army Specialist Corps" }).first()).toBeVisible();
});

test("adjacent unnumbered Dibert stays separate and receives no borrowed employer", async ({ page }) => {
  await page.goto(`./people/${unnumbered}/`, { waitUntil: "domcontentloaded" });
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.getByText(/may duplicate the indexed major/)).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.getByRole("link", { name: "J. Walter Thompson Co." })).toHaveCount(0);
  await expect(page.getByText(/Compare both George C Dibert Box 185 files/)).toBeVisible();
});

test("five official Army identity crosswalks do not become employer claims", async ({ page }) => {
  for (const id of [cohort[0][0], cohort[5][0], cohort[6][0], cohort[7][0], cohort[9][0]]) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
    await expect(page.getByText("No publishable pre-OSS affiliation is recorded yet")).toBeVisible();
  }
});
