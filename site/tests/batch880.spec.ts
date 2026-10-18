import { expect, test } from "@playwright/test";

const profiles = [
  ["721fab20-2de2-5ee4-81d6-3a3b29667035", "William A Sincek"],
  ["3e68443e-bc4a-5107-adf3-b8ac76b7cd54", "Howard A Sinclair"],
  ["0aad0985-c734-58ad-8a5a-1d6604d8b6fe", "Marjorie P Sinclair"],
  ["91daf92e-c111-5b75-9b26-56344ded3e06", "Thomas L Sinclair"],
  ["3094f515-3b84-525a-af39-12c7a3828c36", "Nick A Sineveck"],
  ["031d73fe-4d37-55df-adb7-5c3d500df221", "David Sing"],
  ["ce691e6a-7c59-5325-81d5-7f0b41e8b5e4", "Irving Singer"],
  ["18d1122a-e8f5-58e3-a750-42623623b53b", "Loren A Singer"],
  ["4d486875-b4cd-5022-8b7f-10c70fa85d9c", "Martin Singer"],
  ["870b3b00-0069-5735-b785-906e18815fc6", "Martin R Singer"],
  ["e972f0e6-54f0-5b2e-a07c-035c83718850", "John K Singlaub"],
  ["cdbbfdfd-bf0c-5510-ab71-376d132de0c5", "Ada L Singleton"],
  ["4a8151bc-416d-587a-89ef-b4deef45ae07", "Henry E Singleton"],
  ["d45b56e1-5430-54d7-ac6c-0f461f87d992", "Ira C Singleton"],
  ["f724116c-612b-5d4a-a166-a77f7fe74fc9", "Louis J Singleton"],
  ["8eb76c2b-2535-53af-8599-3ac517c4b4b2", "Zella L Singleton"],
  ["0590f648-b516-59bf-b34f-1a73c1edbf3d", "Helene V Sinnott"],
  ["8af2859d-d0c8-59de-a907-4def24490710", "Curt Siodmak"],
  ["1de626ac-9968-5e66-b492-0abda6efa5a6", "Aristole J Sioris"],
  ["424d9dae-4373-51d7-8087-dbeeac7b4a5d", "John J Sipos"],
  ["160da36a-336d-5a93-b592-26e23cf50154", "Sterling E Sippola"],
  ["b81464c0-424e-55b9-b292-77023f621beb", "Charles Siragusa"],
  ["075dac14-a156-5f38-8004-b79f1d48f757", "Angelo Sirico"],
] as const;

test("Batch 880 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 880 publishes Charles Siragusa's government pathway without collapsing the chronology", async ({ page }) => {
  await page.goto("./people/b81464c0-424e-55b9-b292-77023f621beb/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("Federal Bureau of Narcotics");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("strongly date bounded");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("Federal Bureau of Narcotics");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("Immigration and Naturalization Service");
  await expect(main).toContainText("rather than explicit recruited-from evidence");
});

test("Batch 880 keeps Curt Siodmak's RKO work professional rather than inferred employment", async ({ page }) => {
  await page.goto("./people/8af2859d-d0c8-59de-a907-4def24490710/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("occupation only found");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("RKO Radio Pictures, Inc.");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("professional affiliation");
  await expect(main).toContainText("not labeled an employer");
});

test("Batch 880 preserves the unbridged Henry Singleton lead as unresolved", async ({ page }) => {
  await page.goto("./people/4a8151bc-416d-587a-89ef-b4deef45ae07/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("shared name and initials alone do not bridge");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(page.getByRole("link", { name: /Teledyne/i })).toHaveCount(0);
});

test("Batch 880 keeps the two Martin Singer rows distinct", async ({ page }) => {
  await page.goto("./people/4d486875-b4cd-5022-8b7f-10c70fa85d9c/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("separate Martin R Singer row remains distinct");

  await page.goto("./people/870b3b00-0069-5735-b785-906e18815fc6/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("remains separate from the adjacent Martin Singer row");
});

test("Batch 880 exposes reviewed suffix and spelling variants without replacing indexed names", async ({ page }) => {
  await page.goto("./people/3094f515-3b84-525a-af39-12c7a3828c36/");
  let main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Nick A Sineveck", level: 1 })).toBeVisible();
  await expect(main).toContainText("Nick A Sineveck Jr.");
  await expect(main).toContainText("suffix discrepancy remains visible");

  await page.goto("./people/1de626ac-9968-5e66-b492-0abda6efa5a6/");
  main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Aristole J Sioris", level: 1 })).toBeVisible();
  await expect(main).toContainText("Aristotle J Sioris");
  await expect(main).toContainText("spells the first name Aristotle");
});

test("Batch 880 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 584,
    research_attempted_people: 13_202,
    verified_affiliation_people: 956,
    verified_employer_people: 433,
    archival_review_assessed_people: 11_669,
    published_claims: 7_969,
    public_sources: 5_404,
  });
});
