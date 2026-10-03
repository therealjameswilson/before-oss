import { expect, test } from "@playwright/test";

const profiles = [
  ["6d471627-1326-5ffd-9a8f-ad1d17b05b2f", "Susan C Millett"],
  ["1250e77e-2563-56ce-9cb6-e91b115ea61c", "Cary B Millholland"],
  ["160175cf-d8f2-5163-a74e-8a3e42a059da", "Clayton G Milligan"],
  ["7820e901-e755-5d9d-8df0-b6b148070087", "John C Milligan"],
  ["045cc89c-7b5a-56b8-8988-82bb360d1a29", "Lloyd S Milligan"],
  ["3c5e48db-490e-5f97-a925-7e3882fdcbc2", "Vincent Milligan"],
  ["10de766d-b07c-5f42-88fd-50340cc23cb2", "Wayne A Milligan"],
  ["5e682b8a-5283-5032-848f-9b76152178d3", "Anne Milliken"],
  ["682dbf24-f379-5aa6-ad3c-59a8466e4a9b", "Gerrish H Milliken"],
  ["6166eb99-461b-598a-98f1-30bf768c33db", "Donald D Millikin"],
  ["097c48d7-93ed-5940-ac3d-352388da2a62", "Spiro H Millios"],
  ["bf86ccb3-d10e-53fc-bc11-1a6e7998c318", "Charles H.C. Mills"],
  ["68357b20-8c78-50a1-9b2f-2b0ce5d13f31", "Donald A Mills"],
  ["f1ac21cb-8fb1-5861-bbe0-ce92314ef25b", "Francis B Mills"],
  ["e0ec7e3c-5d93-5b9f-997d-da49f670774c", "Henry E Mills"],
  ["7a0caa5b-1f08-5f9a-b11d-8b8a482deaa1", "Hiram J Mills"],
  ["47c0fdcc-a515-50cb-91ae-ff13f308a507", "Myrtle B Mills"],
  ["2dd803c4-287e-5355-8a7b-64bd62ff3434", "Mary M Millspaugh"],
  ["7620ac59-94ba-5a07-8b26-0f43d7f0534c", "Ian I Milne"],
  ["d94464a3-6ddd-51c0-8b4e-fc0e93cc8d5c", "John R Milodragovich"],
  ["fa251faf-1643-5e11-bf89-035ee27c3747", "George T Milstein"],
  ["a85453a9-5d61-5b89-9dbc-cf57fbfe6793", "Billy G Milton"],
] as const;

test("Batch 663 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 663 separates Cary Millholland's private practice from her professional office", async ({ page }) => {
  await page.goto("./people/1250e77e-2563-56ce-9cb6-e91b115ea61c/");
  const main = page.locator("main");

  await expect(main).toContainText("Self-employed");
  await expect(main).toContainText("Landscape architect");
  await expect(main).toContainText("1937");
  await expect(main).toContainText("1942");
  await expect(main).toContainText("American Horticultural Society");
  await expect(main).toContainText("Secretary");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("professional affiliation, not an employer claim");
});

test("Batch 663 publishes John Milodragovich's prewar Forest Service chronology", async ({ page }) => {
  await page.goto("./people/d94464a3-6ddd-51c0-8b4e-fc0e93cc8d5c/");
  const main = page.locator("main");

  await expect(main).toContainText("United States Forest Service");
  await expect(main).toContainText("Forester");
  await expect(main).toContainText("Deerlodge and Kootenai National Forests");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("not immediate pre-OSS");
  await expect(main).toContainText("Forestry News");
});

test("Batch 663 qualifies Donald Millikin's NYU affiliation without calling it employment", async ({ page }) => {
  await page.goto("./people/6166eb99-461b-598a-98f1-30bf768c33db/");
  const main = page.locator("main");

  await expect(main).toContainText("probable");
  await expect(main).toContainText("New York University");
  await expect(main).toContainText("Cryptography instructor");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("professional affiliation");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 663 keeps Anne Milliken's family company out of employer claims", async ({ page }) => {
  await page.goto("./people/5e682b8a-5283-5032-848f-9b76152178d3/");
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("OSS Rome");
  await expect(main).toContainText("British ar");
  await expect(main).toContainText("does not establish a reliable pre-OSS employer");
  await expect(main).not.toContainText("Milliken and Company");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 663 keeps the Clayton Milligan-Millikan conflict visible", async ({ page }) => {
  await page.goto("./people/160175cf-d8f2-5163-a74e-8a3e42a059da/");
  const main = page.locator("main");

  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Clayton G. Millikan");
  await expect(main).toContainText("Box 527");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 663 publishes Francis Mills identity without inventing an employer", async ({ page }) => {
  await page.goto("./people/f1ac21cb-8fb1-5861-bbe0-ce92314ef25b/");
  const main = page.locator("main");

  await expect(main).toContainText("Francis Byron Mills");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("northern China");
  await expect(main).toContainText("not a named pre-OSS civilian employer");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 663 updates exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,336");
  await expect(page.locator("body")).toContainText("34.82%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil, petroleum, refining, or exploration companies");

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
