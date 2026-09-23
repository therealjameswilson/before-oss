import { expect, test } from "@playwright/test";

const profiles = [
  ["676b8b61-1cf2-565e-8c15-a0b14ff07a03", "Christie E Mileff"],
  ["1a174064-70d3-5d20-bb00-7f1cccce9ae3", "Newton Miler"],
  ["3d9b9e37-9fac-5be8-aea9-38c0f3e722e6", "Dorothy Miles"],
  ["fc8319bd-814c-54e2-ba26-a03515a2cfbe", "Joseph M Miles"],
  ["2be2dd5f-e176-50be-ba08-b2fde0610d38", "Margaret G Miles"],
  ["9161e0f7-2e4f-55b5-b0ed-5d4aab49fd44", "Milton E Miles"],
  ["ad205fd3-2497-577c-b2be-93699bb7e0c9", "William H Miley"],
  ["9bb17d01-0400-58e5-b6d4-4d0446ab6108", "Anthony J Milikas"],
  ["0fb2c024-6193-595f-bb22-d7092dc05fb4", "George Milkovich"],
  ["511f9726-782f-5792-acaf-9d2bfcc9a96b", "Edward W Mill"],
  ["897e73eb-105f-502a-b7be-ce96cb410474", "Harris R Mill"],
  ["18429ce1-9c9c-52d7-9a4a-fa6d7b2f5de3", "Robert R Millar"],
  ["088444f5-97de-56eb-9a57-1cc8204f172a", "Irene Millard"],
  ["209f7b79-fe05-5b3f-9718-39eae5efa965", "John B Millas"],
  ["f686e2f2-3ee7-5fe4-93a9-4708986ca5c5", "Lloyd S Millegan"],
  ["2ea67f87-442d-59e8-98d4-b910c6eaa572", "Jean A Millen"],
  ["28336b2f-5308-5847-b4c0-ac1479421b89", "Murdo J Millen"],
  ["f839f97e-1e85-58bc-add0-27c07203892c", "Niles J Millen"],
  ["5cf71dae-e2c6-548e-b2de-64805466a270", "Walter E Millen"],
  ["040c41a2-3e1f-57f1-828c-baafb4610055", "Aaron H Miller"],
  ["6b939642-8217-59f7-bc86-fd6527e00d4f", "Adah D Miller"],
  ["14422e95-2182-5bae-b098-a60692d4b96f", "Alice E Miller"],
] as const;

test("Batch 658 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 658 distinguishes Newton Miler's 1946 SSU status", async ({ page }) => {
  await page.goto("./people/1a174064-70d3-5d20-bb00-7f1cccce9ae3/");
  const main = page.locator("main");

  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("student at Dartmouth College");
  await expect(main).toContainText("1946 SSU candidacy");
  await expect(main).toContainText("unemployed while still attending school");
  await expect(main).toContainText("104-10219-10000");
});

test("Batch 658 publishes Milton Miles as a naval pathway, not a civilian employer", async ({ page }) => {
  await page.goto("./people/9161e0f7-2e4f-55b5-b0ed-5d4aab49fd44/");
  const main = page.locator("main");

  await expect(main).toContainText("commissioned naval officer");
  await expect(main).toContainText("Navy Department Interior Control Board");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("does not state an OSS transfer date");
});

test("Batch 658 publishes Lloyd Millegan's bounded Library of Congress employment", async ({ page }) => {
  await page.goto("./people/f686e2f2-3ee7-5fe4-93a9-4708986ca5c5/");
  const main = page.locator("main");

  await expect(main).toContainText("Library of Congress");
  await expect(main).toContainText("last civilian employer");
  await expect(main).toContainText("immediate OSS succession is not proven");
  await expect(main).toContainText("The Journal of Asian Studies");
});

test("Batch 658 publishes George Milkovich's direct Army-to-OSS chronology", async ({ page }) => {
  await page.goto("./people/0fb2c024-6193-595f-bb22-d7092dc05fb4/");
  const main = page.locator("main");

  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("assigned to OSS on 10 August 1943");
  await expect(main).toContainText("mechanical engineer");
  await expect(main).toContainText("names the occupation but no company");
});

test("Batch 658 keeps Walter Millen separate from Walter Miller", async ({ page }) => {
  await page.goto("./people/5cf71dae-e2c6-548e-b2de-64805466a270/");
  const main = page.locator("main");

  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("separate Walter Miller");
  await expect(main).toContainText("Box 524");
  await expect(main).toContainText("Box 526");
});

test("Batch 658 updates exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,228");
  await expect(page.locator("body")).toContainText("34.37%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
