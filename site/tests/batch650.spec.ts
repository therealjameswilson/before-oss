import { expect, test } from "@playwright/test";

test("Batch 650 separates Joseph Mendenhall's military pathway from student status", async ({ page }) => {
  await page.goto("./people/1df747a8-9944-55e9-8272-f3a69893bd66/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Joseph A Mendenhall", level: 1 })).toBeVisible();
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("United States Army Air Forces");
  await expect(main).toContainText("Intelligence officer");
  await expect(main).toContainText("Yuma");
  await expect(main).toContainText("Harvard Law School");
  await expect(main).toContainText("Law student");
  await expect(main).toContainText("student");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Batch 650 publishes Arthur Menken's employers without inventing an immediate predecessor", async ({ page }) => {
  await page.goto("./people/36f4e697-90c8-5677-8bd7-b0e65849526a/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Arthur Menken", level: 1 })).toBeVisible();
  await expect(main).toContainText("No publishable immediate affiliation or civilian employer is recorded yet");
  await expect(main).toContainText("Earlier pre-OSS affiliations");
  await expect(main).toContainText("Paramount News");
  await expect(main).toContainText("United Fruit Company");
  await expect(main).toContainText("Columbia Broadcasting System");
  await expect(main).toContainText("United Press");
  await expect(main).not.toContainText("Explicitly immediate");
});

test("Batch 650 qualifies the Horst Mendershause spelling bridge and employment", async ({ page }) => {
  await page.goto("./people/73d4d683-e3a2-5dcd-9af4-5ffd614fd704/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Horst Mendershause", level: 1 })).toBeVisible();
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Horst Mendershausen");
  await expect(main).toContainText("Bennington College");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("Box 517 confirmation");
});

test("Batch 650 preserves Sir Stewart Menzies as an Allied assignment, not an OSS transfer", async ({ page }) => {
  await page.goto("./people/f2f3310e-2955-537a-855e-520ef81a860b/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Sir Stewart Menzles", level: 1 })).toBeVisible();
  await expect(main).toContainText("Sir Stewart Menzies");
  await expect(main).toContainText("foreign or allied military personnel");
  await expect(main).toContainText("Secret Intelligence Service");
  await expect(main).toContainText("not an OSS employment or transfer claim");
});

test("Batch 650 withholds Helen Mensing's discovery-only affiliation lead", async ({ page }) => {
  await page.goto("./people/de0126a5-3c77-5800-bd1f-425a811801c1/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Helen Mensing", level: 1 })).toBeVisible();
  await expect(main).toContainText("probable");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(main).toContainText("before publishing the Air Transport Command claim");
  await expect(main.locator(".affiliation-card")).toHaveCount(0);
});

test("Batch 650 exposes the Joseph Menengas identifier conflict", async ({ page }) => {
  await page.goto("./people/0ef8dd98-2c6d-534a-a059-1ab4cda0ca74/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Joseph V Menengas", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("Joseph V. Menanga");
  await expect(main).toContainText("records are not merged");
});

test("Batch 650 publishes exact coverage while retaining the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,054");
  await expect(page.locator("body")).toContainText("33.64%");
  await expect(
    page.getByRole("heading", { name: "People who worked for oil companies" }),
  ).toBeVisible();

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Arthur Menken");
});
