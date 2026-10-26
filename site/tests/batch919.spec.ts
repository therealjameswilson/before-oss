import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page450-stites-to-henry-stokes-review_batch-919_2026-10-26.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["1225ef83-5bed-5c7f-b230-cc8db024471f", "Louis E Stites"],
  ["e76a74b1-2a05-5dfb-bfb2-c15893dc5238", "Michael L Stiver"],
  ["6e2df8db-7754-5854-bc73-f0063ba9bc5a", "Frederick Stix"],
  ["6f5a6c85-9821-5226-a925-69fe6ae2bc22", "Tom Stix"],
  ["bbe9712d-6c59-574f-b72a-7ebd960c6587", "Albert B Stock"],
  ["e021e1ca-fe8a-55e7-b3cb-192fee4fd9bd", "Grace K Stock"],
  ["f0ca1cba-263b-517e-8f0d-2ab49e8747b8", "George J Stocker"],
  ["91d19978-8e48-5131-9827-abe34b8f7be3", "Louise T Stockly"],
  ["4491ad4a-2a29-5085-b9d8-710c98a1e2ed", "Robert A Stockton"],
  ["240b615e-7100-59fa-9ce8-818859b653b2", "Stanley Stockwitz"],
  ["b711ede2-6b15-5517-a69e-8761c4e9f479", "Gertrude Stoddard"],
  ["37fb3056-d41f-5837-b028-2a66df481322", "Louis Stoddard"],
  ["78e79875-9404-5857-8c86-3e67a5e4d999", "Janie E Stodghill"],
  ["6df27dbc-aa29-5425-9493-4d692ab3246f", "Clemence F Stodolka"],
  ["84be9c37-cc0a-549e-9008-0c046112b1bb", "Graham D Stoessel"],
  ["fc0375ab-d463-51fd-be42-d2a7cbfc7c74", "Joan M Stoffel"],
  ["241e2792-2f46-5e38-b648-722518ac7dd5", "Margaret B Stoffle"],
  ["a3c55561-db1d-5f3c-b1ea-e9dbc06cff0e", "Lloyd K Stogdill"],
  ["a46f0afb-ff51-5246-b412-84c462915d9d", "Andrew W Stohl"],
  ["1f87fe7e-8d81-5ddf-9a3d-35c608729e35", "Adolph Stojak"],
  ["7ab32b46-1116-5cca-9e4f-0af79b160a28", "Alexander C Stokes"],
  ["7905888a-9ace-5607-a756-d56d0ee75653", "Fraser R Stokes"],
  ["9c0927d4-6279-52fd-9e0e-2a8afe47203b", "Henry C Stokes"],
] as const;

test("Batch 919 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Fraser Stokes keeps the Army code as an occupation rather than an employer", async ({ page }) => {
  await page.goto("./people/7905888a-9ace-5607-a756-d56d0ee75653/");
  const main = page.locator("main");
  await expect(main).toContainText("Bookkeepers and cashiers, except bank cashiers");
  await expect(main).toContainText("no employer is identified");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("1943-06-07");
});

test("Michael Stiver shows a qualified COI affiliation without claiming immediacy", async ({ page }) => {
  await page.goto("./people/e76a74b1-2a05-5dfb-bfb2-c15893dc5238/");
  const main = page.locator("main");
  await expect(main).toContainText("Coordinator of Information");
  await expect(main).toContainText("probably identifies");
  await expect(main).toContainText("neither individual dates nor immediate transition into OSS are established");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Tom Stix exposes the mission identity bridge without inventing a prior employer", async ({ page }) => {
  await page.goto("./people/6f5a6c85-9821-5226-a925-69fe6ae2bc22/");
  const main = page.locator("main");
  await expect(main).toContainText("Operation Stygia");
  await expect(main).toContainText("high-confidence match");
  await expect(main).toContainText("provide no pre-OSS employer or predecessor affiliation");
  await expect(main).not.toContainText("America's Grub Street Speaks");
});

test("Stanley Stockwitz displays the probable identity and the chronology conflict", async ({ page }) => {
  await page.goto("./people/240b615e-7100-59fa-9ce8-818859b653b2/");
  const main = page.locator("main");
  await expect(main).toContainText("Stanley Stephen Stokwitz");
  await expect(main).toContainText("Stokwisz");
  await expect(main).toContainText("chronologically inconsistent");
  await expect(main).toContainText("OSS created 1942-06-13");
  await expect(main).toContainText("No pre-OSS employer is stated");
});

test("rejected LoC newspaper candidates do not leak into the public profiles", async ({ page }) => {
  await page.goto("./people/e021e1ca-fe8a-55e7-b3cb-192fee4fd9bd/");
  await expect(page.locator("main")).not.toContainText("Redwood Gazette");

  await page.goto("./people/f0ca1cba-263b-517e-8f0d-2ab49e8747b8/");
  await expect(page.locator("main")).not.toContainText("George R. Stocker");

  await page.goto("./people/37fb3056-d41f-5837-b028-2a66df481322/");
  await expect(page.locator("main")).not.toContainText("Blackcock");

  await page.goto("./people/9c0927d4-6279-52fd-9e0e-2a8afe47203b/");
  await expect(page.locator("main")).not.toContainText("Birmingham age-herald");
});

test("Batch 919 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 919 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 617,
    research_attempted_people: 14_086,
    verified_affiliation_people: 1_003,
    verified_employer_people: 451,
    archival_review_assessed_people: 12_559,
    published_claims: 8_627,
    public_sources: 5_736,
  });
});
