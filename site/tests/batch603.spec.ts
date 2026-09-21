import { expect, test } from "@playwright/test";

test("Elisseeff's documented academic roles do not become an immediate OSS employer", async ({ page }) => {
  await page.goto("./people/8829fd35-280c-54c2-8348-ca57b8befb3d/");
  await expect(page.getByRole("heading", { name: "Sergei Elisseeff", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 134" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("Harvard University");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("Harvard-Yenching Institute");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .not.toContainText("Harvard University");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("Harvard University");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("New Book Published on former HYI Director Serge Elisseeff");
});

test("Eitner's Princeton enrollment is visible as study, not an employer", async ({ page }) => {
  await page.goto("./people/31a9a6d6-7414-5e2c-887d-214d6e723ea7/");
  await expect(page.getByRole("heading", { name: "Lorenz E.A. Eitner", level: 1 })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("Princeton University");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("student");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("Princeton University");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("Lorenz E. A. Eitner *52");
});

test("Embree's Toronto chronology is marked probable rather than date-bounded", async ({ page }) => {
  await page.goto("./people/ae597b0c-6982-5c47-8b87-f74cfb29b92c/");
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate).toContainText("University of Toronto");
  await expect(immediate).toContainText("probable immediate");
  await expect(immediate).toContainText("medium");
  await expect(immediate).not.toContainText("strongly date bounded");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("University of Hawaii");
});

test("Ellmann's Navy transfer and last civilian employer stay separate from the unresolved same-name row", async ({ page }) => {
  await page.goto("./people/572c9c93-f927-5f68-8344-4a76fe5ff959/");
  await expect(page.getByRole("link", { name: "Page 135" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .toContainText("United States Navy");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .toContainText("Harvard University");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("Richard Ellmann, 1918–1987");
  await page.goto("./people/bd8aca8d-045b-5d58-88f6-531291f982e3/");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("Harvard University");
});
