import { expect, test } from "@playwright/test";

test("Kingman Dong's WPA job is earlier employment, not an immediate or last-civilian assignment", async ({ page }) => {
  await page.goto("./people/684fe187-b576-5042-8ea3-1301b58ff4c5/");
  await expect(page.getByRole("heading", { name: "Kingman M Dong Sr.", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 121" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')
    .getByRole("link", { name: "Works Progress Administration" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.getByRole("link", { name: "Dong Kingman: Watercolor Master" }).first())
    .toHaveAttribute("href", "https://unwritten-record.blogs.archives.gov/2023/05/23/dong-kingman-watercolor-master/");
});

test("Jocelyn Donaldson's Clark student status is not published as employment", async ({ page }) => {
  await page.goto("./people/db6acb5b-ef68-5c32-a029-d6b87a655dac/");
  await expect(page.getByRole("heading", { name: "Jocelyn Donaldson", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "The Monadnock Volume 19, Number 2, May 1945" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator("main")).toContainText("not a paid employer");
});

test("same-name pairs stay separate and an Army name conflict remains qualified", async ({ page }) => {
  await page.goto("./people/ea68739d-bfe9-56b3-889f-b64b5d3b10c8/");
  await expect(page.getByRole("heading", { name: "George J Donish", level: 1 })).toBeVisible();
  const firstGroup = await page.getByText(/^duplicate-[a-f0-9]{12}$/).textContent();
  expect(firstGroup).toMatch(/^duplicate-[a-f0-9]{12}$/);

  await page.goto("./people/3237419b-7fee-5183-a635-00c50210d224/");
  await expect(page.getByRole("heading", { name: "George J Donish", level: 1 })).toBeVisible();
  await expect(page.getByText(firstGroup ?? "missing duplicate group", { exact: true })).toBeVisible();

  await page.goto("./people/2d6ce766-6f15-5170-8ec8-0f947b9a071a/");
  await expect(page.getByRole("heading", { name: "Ivan H Doman", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("different full name");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator("main")).not.toContainText("Harmon Robinson");
});
