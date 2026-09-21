import { expect, test } from "@playwright/test";

test("Eifler's Army, COI, and Customs roles remain distinct", async ({ page }) => {
  await page.goto("./people/a0f164c7-505d-5cb9-88e1-0c3c1f1be22f/");
  await expect(page.getByRole("heading", { name: "Carl F Eifler", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 133" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .toContainText("Coordinator of Information");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .not.toContainText("K Company");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .toContainText("United States Customs Service");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("K Company, 35th Infantry Regiment");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("military police unit guarding enemy alien detainees in Hawaii");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("OSS in Action: The Pacific and the Far East");
});

test("the featured oil category excludes Eifler's father's oil-field work", async ({ page }) => {
  await page.goto("./oil-companies/");
  const list = page.getByRole("region", { name: "Oil company work list" });
  await expect(list.locator(".oil-directory__person")).toHaveCount(7);
  await expect(list).not.toContainText("Carl F Eifler");
});
