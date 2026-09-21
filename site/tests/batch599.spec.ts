import { expect, test } from "@playwright/test";

test("Dunderdale's dated SIS role is qualified as earlier, not an immediate OSS transfer", async ({ page }) => {
  await page.goto("./people/51da4744-aece-5630-a1bd-e47bc3356d73/");
  await expect(page.getByRole("heading", { name: "Wilfred A Dunderdale", level: 1 })).toBeVisible();
  await expect(page.getByRole("link", { name: "Page 127" })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("Secret Intelligence Service");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]'))
    .toContainText("medium");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card'))
    .toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
    .toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("La création de l'Équipe 300");
});

test("the printed Dullles spelling remains visible without a famous-namesake employer", async ({ page }) => {
  await page.goto("./people/7fcfdbed-345d-5e4d-8166-edde0efc8ffb/");
  await expect(page.getByRole("heading", { name: "Allen W Dullles", level: 1 })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="index-records"]'))
    .toContainText("Dullles | Allen | W");
  await expect(page.locator('section[aria-labelledby="research-status"]'))
    .toContainText("Box 203");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]'))
    .not.toContainText("Sullivan & Cromwell");
});

test("Clover Todd namesakes and duplicated Duncan rows remain explicit review cases", async ({ page }) => {
  await page.goto("./people/99dd2090-ca2d-5631-af58-fb8e41b34768/");
  await expect(page.locator('section[aria-labelledby="research-status"]'))
    .toContainText("mother and daughter");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
    .toHaveCount(0);

  for (const id of [
    "55a428fa-737c-5315-83fb-725cd3ca7aef",
    "a8892fa2-dcf0-5e0b-a355-7ccef2c6a898",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "Joe B Duncan", level: 1 })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card'))
      .toHaveCount(0);
  }
});

test("the oil-company category remains linked at the top of the home page", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("#oil-companies").getByRole("heading", { name: "People who worked for oil companies" }))
    .toBeVisible();
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(7);
});
