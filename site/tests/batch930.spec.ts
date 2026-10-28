import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page455-john-l-sullivan-to-elinor-h-summers-review_batch-930_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["cca2cffa-2270-5b47-9ef6-666706057b05", "John L Sullivan"],
  ["1bf7a6a5-b2b8-575c-98c7-2c2dabd79a48", "John L Sullivan"],
  ["4de5a14f-5ca1-5267-b56e-eab157fe4939", "John W Sullivan"],
  ["3c6e6e5c-59a3-541b-8acd-51204243227c", "Leo E Sullivan"],
  ["69aae1f4-cc49-5b26-86ba-5782f9ce687c", "Leslie F Sullivan"],
  ["6f6c6933-ea91-574f-afde-93c02d04e065", "Mary L Sullivan"],
  ["bd96d822-ef30-5b41-b9a7-830974f0dedf", "Phillip B Sullivan"],
  ["46808238-ddda-5ac1-9686-48515565caec", "Phyllis A Sullivan"],
  ["f8fd70de-0878-51c3-a901-66c5f8104788", "Richard E Sullivan"],
  ["4efe4157-32eb-5ae0-a682-0a9219a23dd3", "Richard P Sullivan"],
  ["7c49fa2c-9da6-5134-8f26-c1e2dcbeb631", "Thomas J Sullivan"],
  ["aa513060-bc48-57e7-8260-caaa874a3bee", "Thomas V Sullivan"],
  ["4c81aa01-870e-501f-ae9f-c54de01297c2", "William H Sullivan"],
  ["eb928c89-4472-5038-98f9-78343042b846", "Alvah W Sulloway"],
  ["ceff069a-9287-5cf2-8109-339aeda1ed7a", "Leonard Sultan"],
  ["0ce88b2f-5413-5a46-b5f4-bccf37837d22", "Alfred F Sumabat"],
  ["80542357-a72c-57b3-a590-b452b2827ba5", "Mercedes Sumi"],
  ["1b764b72-6166-56ed-8896-cea761979131", "Shingo Sumi"],
  ["79541560-3d33-5b65-8458-aa01f9d3e4b5", "Helen P Summerlin"],
  ["f726cb2f-798c-56a5-9112-cd287137b5d4", "Roy C Summerlin"],
  ["d9b876f4-34ba-5f11-907a-a645936912db", "Charnelle H Summers"],
  ["a466c051-eb38-5c1c-a190-eb1d19f29c28", "Donald B Summers"],
  ["ed415c3b-04a3-5806-9aea-33973ab8a08a", "Elinor H Summers"],
] as const;

test("Batch 930 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Sulloway publishes Sulloway and Hollis in both required employment categories", async ({ page }) => {
  await page.goto("./people/eb928c89-4472-5038-98f9-78343042b846/");
  const main = page.locator("main");
  await expect(main).toContainText("Alvah Woodbury Sulloway");
  await expect(main).toContainText("Sulloway & Hollis");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("lawyer");
  await expect(main).toContainText("1941");
  await expect(main).toContainText("1942");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("verified employer found");
});

test("the Sumi profiles preserve incarceration and the explicit transition to OSS", async ({ page }) => {
  for (const [id, name] of [
    ["80542357-a72c-57b3-a590-b452b2827ba5", "Mercedes Sumi"],
    ["1b764b72-6166-56ed-8896-cea761979131", "Shingo Sumi"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(name);
    await expect(main).toContainText("Granada Relocation Center (Amache)");
    await expect(main).toContainText("incarcerated resident granted indefinite leave");
    await expect(main).toContainText("1944-07-22");
    await expect(main).toContainText("Employer to be Office of Strategic Services");
    await expect(main).toContainText("involuntary confinement");
    await expect(main).not.toContainText("Last civilian employer before wartime service\nGranada");
  }
});

test("three Army categories remain occupation-only and employer-free", async ({ page }) => {
  for (const [id, occupation] of [
    ["69aae1f4-cc49-5b26-86ba-5782f9ce687c", "Occupations in the manufacture of leather"],
    ["7c49fa2c-9da6-5134-8f26-c1e2dcbeb631", "Brick and stone masons, and tile setters"],
    ["aa513060-bc48-57e7-8260-caaa874a3bee", "Occupations in the manufacture of automobiles"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("no employer or workplace");
    await expect(main).toContainText("occupation only found");
  }

  await page.goto("./people/3c6e6e5c-59a3-541b-8acd-51204243227c/");
  const leo = page.locator("main");
  await expect(leo).toContainText("1946-01-31");
  await expect(leo).toContainText("after OSS dissolution");
  await expect(leo).not.toContainText("Sheet metal workers");
});

test("Richard E and Richard P remain separate with the initial conflict visible", async ({ page, request }) => {
  const response = await request.get("./data/people/r.json");
  const people = await response.json();
  const richards = people.filter((item: { person_id: string }) => [
    "f8fd70de-0878-51c3-a901-66c5f8104788",
    "4efe4157-32eb-5ae0-a682-0a9219a23dd3",
  ].includes(item.person_id));
  expect(richards).toHaveLength(2);
  expect(richards[0].possible_duplicate_group).toBeTruthy();
  expect(richards[0].possible_duplicate_group).toBe(richards[1].possible_duplicate_group);
  expect(richards.every((item: {
    immediate_pre_oss_affiliations: unknown[];
    last_civilian_pre_service: unknown[];
    other_pre_oss_affiliations: unknown[];
  }) =>
    item.immediate_pre_oss_affiliations.length === 0 &&
    item.last_civilian_pre_service.length === 0 &&
    item.other_pre_oss_affiliations.length === 0
  )).toBeTruthy();

  await page.goto("./people/f8fd70de-0878-51c3-a901-66c5f8104788/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Richard P Sullivan");
  await expect(main).toContainText("middle-initial conflict");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");

  await page.goto("./people/4efe4157-32eb-5ae0-a682-0a9219a23dd3/");
  main = page.locator("main");
  await expect(main).toContainText("Possible duplicate group");
  await expect(main).toContainText("Review both Box 757 Richard Sullivan files");
});

test("all three John L Sullivan rows share one review group and terminal status", async ({ request }) => {
  const response = await request.get("./data/people/j.json");
  const people = await response.json();
  const johns = people.filter((item: { display_name: string }) => item.display_name === "John L Sullivan");
  expect(johns).toHaveLength(3);
  expect(new Set(johns.map((item: { possible_duplicate_group: string }) => item.possible_duplicate_group)).size).toBe(1);
  expect(johns.every((item: { research_status: string }) => item.research_status === "requires_archival_review")).toBeTruthy();
});

test("Roy Summerlin retains direct commissioned classification without an invented employer", async ({ page }) => {
  await page.goto("./people/f726cb2f-798c-56a5-9112-cd287137b5d4/");
  const main = page.locator("main");
  await expect(main).toContainText("2nd Lt");
  await expect(main).toContainText("commissioned army officer");
  await expect(main).toContainText("Commissioned officer");
  await expect(main).toContainText("No reliable pre-OSS employer");
});

test("Batch 930 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Sulloway & Hollis");
  await expect(main).not.toContainText("Granada Relocation Center");
});

test("Batch 930 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 930 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 630,
    research_attempted_people: 14_337,
    verified_affiliation_people: 1_017,
    verified_employer_people: 459,
    archival_review_assessed_people: 12_810,
    published_claims: 8_803,
    public_sources: 5_827,
  });
});
