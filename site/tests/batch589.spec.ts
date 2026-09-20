import { expect, test } from "@playwright/test";

const cohort = [
  ["7715d962-f6dd-5c67-a597-685a6f49de39", "Theodore D'Luski", "Box 189"],
  ["519e9442-eab6-5a1a-a5de-0b493610c3c5", "Albert Dobberstein, J", "Box 190"],
  ["dc50f0ae-a540-5ee0-bcdf-a0f3be37c387", "Paul Dobbs", "Box 190"],
  ["40a22ed3-336e-573d-bce4-e0d48cd1eb1c", "John F Dobes", "Box 190"],
  ["b30b979f-da30-573a-a406-cd305894879c", "Francis Dobo", "Box 190"],
  ["b978a1d0-495c-5b46-877f-066dda68850a", "John Dobo", "Box 190"],
] as const;

test("batch 589 retains all six distinct page-119 rows and no invented employers", async ({ page }) => {
  for (const [id, name, box] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText(box, { exact: false }).first()).toBeVisible();
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  }
});

test("Francis Dobo's unbridged career candidate is not published as an employer", async ({ page }) => {
  await page.goto(`./people/${cohort[4][0]}/`);
  await expect(page.getByText(/employment history is withheld pending file review/)).toBeVisible();
  await expect(page.getByText("Opera Mundi")).toHaveCount(0);
  await expect(page.getByText("Office of War Information")).toHaveCount(0);
});

test("John Dobo's official identity crosswalk does not become an employer", async ({ page }) => {
  await page.goto(`./people/${cohort[5][0]}/`);
  await expect(page.getByText(/official Army bulk file/).first()).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
});
