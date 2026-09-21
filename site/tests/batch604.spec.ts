import { expect, test } from "@playwright/test";

test("English's OSS identity crosswalk does not invent a pre-OSS employer", async ({ page }) => {
  await page.goto("./people/a1b5cb3b-8221-5bf4-ac6a-2cdf45dbab56/");
  await expect(page.getByRole("heading", { name: "Van Harvey English", level: 1 }))
    .toBeVisible();
  await expect(page.getByRole("link", { name: "Page 136" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("With the Faculty");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .not.toContainText("Dartmouth");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("Dartmouth");
});

test("same-name Enders candidate does not acquire Smithsonian career", async ({ page }) => {
  await page.goto("./people/8ec38c0a-bbba-5f1b-870b-d68064f8e5d5/");
  await expect(page.getByRole("heading", { name: "Robert K Enders", level: 1 }))
    .toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("Missouri Valley College");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]'))
    .not.toContainText("Missouri Valley College");
});

test("Paul Endacott's Phillips career is excluded from John Endacott and the oil list", async ({ page }) => {
  await page.goto("./people/426e86a1-a152-50d5-b7fa-0ed0e75e636b/");
  await expect(page.getByRole("heading", { name: "John L Endacott", level: 1 }))
    .toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("Phillips Petroleum");
  await page.goto("./oil-companies/");
  const list = page.getByRole("region", { name: "Oil company work list" });
  await expect(list.locator(".oil-directory__person")).toHaveCount(7);
  await expect(list).not.toContainText("John L Endacott");
});

test("page 136 spelling pairs remain separate public people", async ({ page }) => {
  await page.goto("./people/d4d89487-a8f1-5a61-98d8-7bcd8a064c9c/");
  await expect(page.getByRole("heading", { name: "Rudolphe J Emond", level: 1 }))
    .toBeVisible();
  await page.goto("./people/2752a201-e638-5c92-8f43-879847ec43ca/");
  await expect(page.getByRole("heading", { name: "Rudolphe J Enond", level: 1 }))
    .toBeVisible();
  await page.goto("./people/54052f1b-2a7a-51d8-8a17-0c105f509f3b/");
  await expect(page.getByRole("heading", { name: "George W Engl", level: 1 }))
    .toBeVisible();
  await page.goto("./people/10ad95f6-d07e-5590-9b31-c7561d6d0542/");
  await expect(page.getByRole("heading", { name: "George W England", level: 1 }))
    .toBeVisible();
});
