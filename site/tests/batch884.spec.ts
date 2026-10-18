import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page432-sliwa-small-review_batch-884_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["30f9c045-dc21-57fc-a80c-d8fa01dc20cc", "Joseph R Sliwa"],
  ["f8dd07c7-1d29-5fcf-80c5-a68192a1605d", "Ruth C Sloan"],
  ["be3046bb-3bb6-5366-afc5-411b7534b56a", "William F Sloan"],
  ["5e503b66-5d23-5bdd-9e84-1d8134b7422e", "Albert J Sloane"],
  ["049b0875-d40b-58c5-aa9e-adacc7f40990", "Lee A Slockbower"],
  ["0faa68e1-b8e5-5f9e-a3eb-26a4b36830c1", "F A Slocum"],
  ["2bf67489-dbaf-53ef-82ba-48f25507cd04", "Tokutaro N Slocum"],
  ["334fcfea-ab27-550d-a15e-2677b2cb6255", "Otto Sloss"],
  ["627f5555-d3bf-5c49-a87b-acd14fc3585d", "Priscilla Sloss"],
  ["d30ecb3c-8afe-5212-a019-6ded91dd4ecd", "A N Slotkin"],
  ["83ff7896-616a-5727-9b41-4ea89251851c", "Harold M Slott"],
  ["bbf39ab1-a5a3-5fb0-b4d6-1900943ddc87", "James J Slovic"],
  ["295a3955-a0d3-564c-be89-9b55a2fd8b26", "Lillian Sluchan"],
  ["60bf4d6b-b09b-56e8-813d-a74abb50f4e0", "Miriam Sluchan"],
  ["29d968b4-8b4e-5964-b760-88aa03d643ba", "Peter Sluiter"],
  ["eac263a1-7e2d-5541-a394-44648062cb99", "Chester A Slupski"],
  ["7d703772-ff26-54e6-bfd6-06aad61462d5", "John M Sluzevich"],
  ["8c35ef6f-00d7-549c-9548-d1a98001f4ed", "Jack F Slyder"],
  ["7f26b878-a2e7-5263-b37b-ead04e9465b7", "Maurice D Slyder"],
  ["055494e6-cf3b-5bfb-a078-506a1f1d9ac9", "Kathryn W Smail"],
  ["05e2e3ff-7485-5a84-9330-a753c571e7f2", "Martha V Smail"],
  ["75ea143e-29fa-59f2-b712-168d3592fae0", "Dorris Smalet"],
  ["124e0b86-9932-5b62-9e7d-20e828a69c4b", "Francis M Small"],
] as const;

test("Batch 884 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
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

test("Batch 884 separates Sluiter's Army pathway from his civilian self-employment", async ({ page }) => {
  await page.goto("./people/29d968b4-8b4e-5964-b760-88aa03d643ba/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  const immediate = main.locator("section[aria-labelledby='immediate-affiliation']");
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("Army cook");
  await expect(immediate).toContainText("explicit immediate");
  const civilian = main.locator("section[aria-labelledby='civilian-employer']");
  await expect(civilian).toContainText("Self-employed meat market");
  await expect(civilian).toContainText("Owner-operator");
  await expect(civilian).toContainText("strongly date bounded");
});

test("Batch 884 publishes Slocum's JACL role as civic affiliation rather than employment", async ({ page }) => {
  await page.goto("./people/2bf67489-dbaf-53ef-82ba-48f25507cd04/");
  const main = page.locator("main");
  await expect(main).toContainText("Tokutaro Nishimura Slocum");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Japanese American Citizens League");
  await expect(earlier).toContainText("professional affiliation");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 884 keeps Slockbower's college and Army evidence qualified", async ({ page }) => {
  await page.goto("./people/049b0875-d40b-58c5-aa9e-adacc7f40990/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Brothers College of Drew University");
  await expect(earlier).toContainText("Assistant battery clerk");
  await expect(earlier).toContainText("medium");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 884 labels Sluchan's Hunter record as student status, not employment", async ({ page }) => {
  await page.goto("./people/60bf4d6b-b09b-56e8-813d-a74abb50f4e0/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Hunter College");
  await expect(earlier).toContainText("A.B. degree candidate");
  await expect(earlier).toContainText("student");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 884 identifies Sluzevich as a commissioned officer without backdating his unit", async ({ page }) => {
  await page.goto("./people/7d703772-ff26-54e6-bfd6-06aad61462d5/");
  const main = page.locator("main");
  await expect(main).toContainText("commissioned army officer");
  await expect(main).toContainText("Commissioned officerYes");
  await expect(main).toContainText("377th Parachute Field Artillery Battalion");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
});

test("Batch 884 evidence bundle excludes private identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 884 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 585,
    research_attempted_people: 13_294,
    verified_affiliation_people: 964,
    verified_employer_people: 435,
    archival_review_assessed_people: 11_761,
    published_claims: 8_045,
    public_sources: 5_442,
  });
});
