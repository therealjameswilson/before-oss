import { expect, test } from "@playwright/test";

test("Batch 651 separates Benjamin Meritt's predecessor assignment from his civilian employer", async ({ page }) => {
  await page.goto("./people/e17a5828-bc9e-545b-a356-8dc73b73e5a5/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Benjamin D Meritt", level: 1 })).toBeVisible();
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Foreign Nationalities Branch");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("Institute for Advanced Study");
  await expect(main).toContainText("Professor of Greek epigraphy");
  await expect(main).toContainText("Bulletin No. 12");
});

test("Batch 651 publishes Gordon Merrick's ordered newspaper chronology", async ({ page }) => {
  await page.goto("./people/cea6c22b-a0dc-53e9-a302-66fdc0ab499f/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Gordon Merrick", level: 1 })).toBeVisible();
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("New York Post");
  await expect(main).toContainText("Earlier pre-OSS affiliations");
  await expect(main).toContainText("Washington Star");
  await expect(main).toContainText("Baltimore Sun");
  await expect(main).toContainText("Gordon Merrick Papers");
});

test("Batch 651 visibly qualifies the Guillermo and Guillaume Mercader bridge", async ({ page }) => {
  await page.goto("./people/82081189-078b-5a00-8fc0-6f5bb819de1b/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Guillermo Mercader", level: 1 })).toBeVisible();
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Guillaume Mercader");
  await expect(main).toContainText("cycle, motor, and sporting-goods shop");
  await expect(main).toContainText("Organisation civile et militaire");
  await expect(main).toContainText("not necessarily immediately before OSS");
  await expect(main).toContainText("Inspect Box 518");
  await expect(main).not.toContainText("Explicitly immediate");
});

test("Batch 651 exposes David Merrell's protected-identifier conflict", async ({ page }) => {
  await page.goto("./people/d739762b-0c18-50a0-9839-0a81f5b85e13/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "David J Merrell", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("Russell Franklyn H");
  await expect(main).toContainText("Army record is not accepted");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 651 preserves three William Meritts spellings without merging", async ({ page }) => {
  await page.goto("./people/7b5cf14b-f5b5-58b4-bab2-a6ff99802643/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "William L Meritts", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("William L Marritts");
  await expect(main).toContainText("William L Merritts");
  await expect(main).toContainText("no merge is made");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 651 accepts Rene Mermet's Army identity without inventing an employer", async ({ page }) => {
  await page.goto("./people/d762b661-3182-5f04-8ef3-8ae8a21db10d/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Rene J Mermet", level: 1 })).toBeVisible();
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Rene J E Mermet");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(main).toContainText("Army codes do not establish a named predecessor employer");
});

test("Batch 651 publishes the new coverage while retaining the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,075");
  await expect(page.locator("body")).toContainText("33.73%");
  await expect(
    page.getByRole("heading", { name: "People who worked for oil companies" }),
  ).toBeVisible();

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Benjamin D Meritt");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Gordon Merrick");
});
