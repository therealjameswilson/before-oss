import { expect, test } from "@playwright/test";

test("Louis Dups has a cited earlier Cavalry unit, not an inferred immediate employer", async ({ page }) => {
  await page.goto("./people/2d2ac1c9-b522-54e0-9202-d488968653c2/");
  await expect(page.getByRole("heading", { name: "Louis Dups", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 128" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("101st Cavalry");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card'))
    .toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
    .toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("Annual Report of the Adjutant General");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("Battle Participation Awards");
});

test("Stephen Dunwell's IBM namesake lead remains withheld pending Box 206 linkage", async ({ page }) => {
  await page.goto("./people/07852900-171e-5f02-ba1a-eb43afeeafa3/");
  await expect(page.getByRole("heading", { name: "Stephen W Dunwell", level: 1 })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="research-status"]'))
    .toContainText("Box 206");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
    .toHaveCount(0);
});

test("Virginia A and E Dunlap remain separate possible duplicates", async ({ page }) => {
  let duplicateGroup: string | null = null;
  for (const [id, name] of [
    ["da32c6ed-054c-54b6-9a73-e70b09bb549c", "Virginia E Dunlap"],
    ["f3ffe609-1b06-5cb4-a604-f60a19d68e9b", "Virginia A Dunlap"],
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const group = (await page.locator('dt:has-text("Duplicate group") + dd').textContent())?.trim();
    expect(group).toMatch(/^duplicate-[a-f0-9]{12}$/);
    if (duplicateGroup) expect(group).toBe(duplicateGroup);
    duplicateGroup = group ?? null;
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
      .toHaveCount(0);
  }
});
