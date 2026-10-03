import { expect, test } from "@playwright/test";

const thomasMoonId = "bc5ab263-1086-5109-9553-91ba2780445f";

test("Batch 672 publishes Thomas N Moon's direct profile route", async ({ page }) => {
  await page.goto(`./people/${thomasMoonId}/`);
  await expect(page.getByRole("heading", { name: "Thomas N Moon", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("PDF page 326");
  await expect(page.locator("main")).toContainText("Box 534");
});

test("Batch 672 publishes the Engineer Corps as an immediate military assignment", async ({ page }) => {
  await page.goto(`./people/${thomasMoonId}/`);
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const lastCivilian = page.locator('section[aria-labelledby="civilian-employer"]');

  await expect(immediate.locator(".affiliation-card")).toHaveCount(1);
  await expect(immediate).toContainText("United States Army Corps of Engineers");
  await expect(immediate).toContainText("Draftee assigned to the Engineer Corps");
  await expect(immediate).toContainText("military assignment");
  await expect(immediate).toContainText("explicit immediate");
  await expect(lastCivilian).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(lastCivilian).not.toContainText("Army Corps of Engineers");
});

test("Batch 672 exposes the evidence chain and preserves the rank limitation", async ({ page }) => {
  await page.goto(`./people/${thomasMoonId}/`);
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("nonshared protected identifier");
  await expect(main).toContainText("A Special Forces Model");
  await expect(main).toContainText("A 'Game' Without Rules");
  await expect(main).toContainText("index prints T-3");
  await expect(main).toContainText("T/5 in early 1944");
  await expect(main).toContainText("OH 2395");
  await expect(main).not.toContainText("Verified employer");
  await expect(main).not.toContainText("PRIVATE/DO NOT USE");
});

test("Batch 672 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,511");
  await expect(page.locator("body")).toContainText("35.55%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  await expect(oilList).not.toContainText("Thomas N Moon");
});
