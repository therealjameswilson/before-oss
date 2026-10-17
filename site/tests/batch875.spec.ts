import { expect, test } from "@playwright/test";

const profiles = [
  ["ed122f8e-b45d-5119-9a5c-1c5e25271834", "Stanley V Sienkiewicz"],
  ["d0c82d84-bdec-5c45-964c-d5ff0c2b64a8", "Warren M Sieverin"],
  ["58dec61a-446e-52a2-bebe-6e383c155fac", "Jeannette K Siewers"],
  ["f5f6a5d2-2953-5528-b1b5-dbda6ede2d6f", "Roger Siffredi"],
  ["1a1d14a6-5e53-5068-955f-6de716f759da", "Louis Sigalas"],
  ["a45f3894-2f9e-5826-a09f-0d729c154d84", "Morris A Sigh"],
  ["f62c2ef6-e77e-5868-87c4-d1850f826c8a", "Section Signal"],
  ["677c33d3-c513-57d4-ad94-24a2e4eae9e2", "Domenico G Signore"],
  ["601c9fb5-0ad3-5419-9a93-d1223b59ba8a", "Joseph V Sika"],
  ["4f59fa28-eeac-5919-9053-d9eaaf0d6d01", "Robert F Sikes"],
  ["1a6b33b8-fa56-5a59-a2a2-1a093972ee33", "Mark A Sikora"],
  ["800fa225-7289-50ab-8138-7713730ef54b", "Mark E Sikora"],
  ["3737c81c-2571-51fa-819d-e3331d8912c7", "Mike Silaghi"],
  ["e52e0a90-bc2e-5ef0-8647-c7bb7a1593e9", "Choon Silasuvan"],
  ["40246ad8-d110-5e94-98fc-a460bd352c75", "Raymond H Silbaugh"],
  ["11f2ce57-1977-571e-ba0a-0b133c5d5c53", "Jack M Silberman"],
  ["27e4eb5d-034d-5039-ab60-f5d7d103acf4", "Anne Silbert"],
  ["e8be247c-8a6b-5266-8de6-e8a5ba6c90f3", "Steve Silianoff"],
  ["57b45288-c488-5666-95c3-1f742b15523c", "Sarah J Sillcocks"],
  ["acefadd5-37b0-5c36-a20e-e21ad04eea6e", "Earl J Silliman"],
  ["d9256c19-8f59-55f6-82c3-5f72d2363ff3", "Chetman W Sillivent"],
  ["c2782124-e5dd-564a-9969-272c693570b2", "Carl Sillman"],
  ["22c0e3bc-5a6a-5236-949c-1b3b5342edd6", "Gerard I Sillman"],
] as const;

test("Batch 875 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 875 distinguishes Sarah Sillcocks's prewar education from employment", async ({ page }) => {
  await page.goto("./people/57b45288-c488-5666-95c3-1f742b15523c/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("Vassar College");
  await expect(main).toContainText("class of 1935");
  await expect(main).toContainText("student");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
  await expect(main).toContainText("Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified");
});

test("Batch 875 qualifies Roger Siffredi without inventing an employer or military unit", async ({ page }) => {
  await page.goto("./people/f5f6a5d2-2953-5528-b1b5-dbda6ede2d6f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Roger Marc Siffredi");
  await expect(main).toContainText("Probable, not confirmed");
  await expect(main).toContainText("do not identify a pre-OSS employer, unit or sequence into OSS");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 875 preserves the Joseph Sika identity conflict", async ({ page }) => {
  await page.goto("./people/601c9fb5-0ad3-5419-9a93-d1223b59ba8a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("EPH V rather than Joseph V Sika");
  await expect(main).toContainText("No employer, occupation or chronology is inferred");
});

test("Batch 875 preserves Signal Section as an ambiguous non-person-form source row", async ({ page }) => {
  await page.goto("./people/f62c2ef6-e77e-5868-87c4-d1850f826c8a/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("non-person-form entry");
  await expect(main).toContainText("No person is asserted");
  await expect(main).toContainText("Box 710");
});

test("Batch 875 keeps Sidianoff and Silianoff separate while exposing the review relationship", async ({ page }) => {
  await page.goto("./people/e8be247c-8a6b-5266-8de6-e8a5ba6c90f3/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("possible spelling variant");
  await expect(main).toContainText("Steve Sidianoff");

  await page.goto("./people/8f249653-ab5e-5f86-920f-f8c5f3e2dea1/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("may be a spelling variant");
  await expect(main).toContainText("Steve Silianoff");
});

test("Batch 875 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 583,
    research_attempted_people: 13_088,
    verified_affiliation_people: 949,
    verified_employer_people: 431,
    archival_review_assessed_people: 11_555,
    published_claims: 7_899,
    public_sources: 5_376,
  });
});
