import { expect, test } from "@playwright/test";

test("Batch 649 separates Amos Melton's civilian employer and military pathway", async ({ page }) => {
  await page.goto("./people/3e77de23-01c3-5189-9548-fee8eb208fea/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Amos W Melton", level: 1 })).toBeVisible();
  await expect(main).toContainText("Fort Worth Star-Telegram");
  await expect(main).toContainText("Reporter; assistant financial editor; sportswriter");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("United States Army Air Forces");
  await expect(main).toContainText("Intelligence officer");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Texas State Historical Association");
});

test("Batch 649 keeps Dolores Mencke's post-OSS OPA lead out of affiliation facts", async ({ page }) => {
  await page.goto("./people/68c64125-a750-5390-ab6c-0f6fe43e3a39/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Dolores J Mencke", level: 1 })).toBeVisible();
  await expect(main).toContainText("November 6, 1945");
  await expect(main).toContainText("postdates OSS dissolution");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(main).not.toContainText("Last civilian employer before wartime service");
});

test("Batch 649 preserves the Joseph Menanga and Menengas identity conflict", async ({ page }) => {
  await page.goto("./people/bfb08429-94e7-5d76-a9d3-3fd8ab8de509/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Joseph V Menanga", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Menengas");
  await expect(main).toContainText("surname conflict prevents a merge");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 649 qualifies Oleg Melnikoff's spelling and suffix differences", async ({ page }) => {
  await page.goto("./people/f5a3f46d-4a2e-582d-a01f-dfeb02893310/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Oleg Melnikoff II", level: 1 })).toBeVisible();
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Oleg I. Melnikof");
  await expect(main).toContainText("spelling and Roman numeral differ");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 649 publishes exact coverage while retaining the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,032");
  await expect(page.locator("body")).toContainText("33.55%");
  await expect(
    page.getByRole("heading", { name: "People who worked for oil companies" }),
  ).toBeVisible();

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Amos W Melton");
});
