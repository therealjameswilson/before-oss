import { expect, test } from "@playwright/test";

const profiles = [
  ["da3cda0f-5cfa-5fa5-a77d-957806008db7", "Thomas J Sheridan"],
  ["3b4ea3ce-1cb4-5b09-834d-66ccaf50d21b", "William B Sheridan"],
  ["c2f02ebb-93b2-54a7-9dca-3c023c1609e0", "William T Sheridan"],
  ["36b08d43-3894-5709-addd-97168128674d", "Arthur Sherman"],
  ["71988779-8020-5131-9736-214d37a567a7", "Carlton A Sherman"],
  ["c453e83b-fb93-53d0-8e2b-6f5f1e6056b7", "David H Sherman"],
  ["f829cb6e-b7ca-5044-87e8-f8175ae5650c", "Eugene Sherman"],
  ["a3f7a944-1eea-5187-a97b-96028ae16f3c", "George H Sherman"],
  ["91e3e442-b31e-5359-9e6e-e87c2a080845", "Irving Sherman"],
  ["4e555325-b107-540b-afc3-64838502e204", "Mabel H Sherman"],
  ["fbc54b79-5c6e-512f-bc7c-bc3c41fbb912", "Miriam R Sherman"],
  ["b072546f-072d-50c1-bf36-9fbbe632a751", "Philip H Sherman"],
  ["e1f99af1-43c9-5738-a2f8-6dd69ac18552", "Richard T Sherman"],
  ["3d7ed0e3-f244-510f-89a4-b8661cf88dfb", "William Sherman"],
  ["50769b2d-82e1-50d4-8ba4-6ae1e2d52f0d", "Victor F Sheronas"],
  ["7f85f1ee-6821-537c-87b3-d892ad5ba07e", "Alfred Sherrard"],
  ["65c9654c-3d56-578c-9dbd-f30b6e5bc6f4", "Florence J Sherriff"],
  ["7e3cf9fa-9583-5657-b644-f321a34d460a", "David D Sherrill"],
  ["e3dd4466-23b1-50fb-bd1e-5de229396d5b", "James R Sherrill"],
  ["a4bd35e9-5c0e-541e-b3a6-e56bbe08c2df", "Lucy Sherrill"],
  ["5acf6ba2-46d2-530f-af69-e07b960859fb", "Margaret S Sherrill"],
  ["5cd1c35e-6d36-5924-b56d-ee9bc4bf5144", "Bowden Sherrod"],
  ["c894e1c9-d2b6-5666-8664-389a0b0d561b", "Byron P Sherry"],
] as const;

test("Batch 868 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 868 publishes Sherman's immediate and last civilian employer", async ({ page }) => {
  await page.goto("./people/91e3e442-b31e-5359-9e6e-e87c2a080845/");
  const main = page.locator("main");
  await expect(main).toContainText("Irving H Sherman");
  await expect(main).toContainText("A. G. Becker & Co.");
  await expect(main).toContainText("Vice-President");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("explicit immediate");
});

test("Batch 868 qualifies Florence Sherriff's three earlier teaching affiliations", async ({ page }) => {
  await page.goto("./people/65c9654c-3d56-578c-9dbd-f30b6e5bc6f4/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Florence Janson Sherriff");
  await expect(main).toContainText("University of Shanghai");
  await expect(main).toContainText("St. John's University, Shanghai");
  await expect(main).toContainText("Shanghai American School");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationA. G. Becker");
});

test("Batch 868 publishes Sheronas's 1934 Moscow assignment only as qualified earlier evidence", async ({ page }) => {
  await page.goto("./people/50769b2d-82e1-50d4-8ba4-6ae1e2d52f0d/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Embassy of the United States, Moscow");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
  await expect(main).toContainText("Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified");
});

test("Batch 868 withholds the unbridged TIME namesake from Eugene Sherman's public profile", async ({ page }) => {
  await page.goto("./people/f829cb6e-b7ca-5044-87e8-f8175ae5650c/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Electronic Army Serial Number Merged File");
  await expect(main).not.toContainText("Honoring the Loyalists");
  await expect(main).not.toContainText("guerrilla base");
});

test("Batch 868 preserves Army matches as identity-only evidence", async ({ page }) => {
  for (const id of [
    "c2f02ebb-93b2-54a7-9dca-3c023c1609e0",
    "f829cb6e-b7ca-5044-87e8-f8175ae5650c",
    "e3dd4466-23b1-50fb-bd1e-5de229396d5b",
    "5cd1c35e-6d36-5924-b56d-ee9bc4bf5144",
    "c894e1c9-d2b6-5666-8664-389a0b0d561b",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("not a named employer or Army-to-OSS chronology");
  }
});

test("Batch 868 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 579,
    research_attempted_people: 12_930,
    verified_affiliation_people: 939,
    verified_employer_people: 427,
    archival_review_assessed_people: 11_397,
    published_claims: 7_809,
    public_sources: 5_327,
  });
});
