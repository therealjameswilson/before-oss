import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page459-john-t-takach-to-max-v-talbot-review_batch-938_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["047fda06-9304-53c6-9437-d5cb32fbb542", "John T Takach"],
  ["3baa382a-8c60-5637-9e0f-7cd71386eda3", "Alfred J Takacs"],
  ["317f3ad9-e305-56f0-bea0-e34a6dd96ca1", "Kuniyasu Takahashi"],
  ["3bbd01d0-97fb-504c-b6d2-62cfa9328e17", "Minekichi Takahashi"],
  ["fb335f1e-9687-586f-b536-a50c132cb3b2", "Shigeharu Takahashi"],
  ["77cd3c5d-3f74-5f1a-adef-db289f4037af", "Robert S Takakuwa"],
  ["880de019-0520-5181-81d2-51aca3ae2365", "William A Takala"],
  ["95e3497e-b8db-5e19-99ed-6d006a651eed", "William A Takala"],
  ["c27ff5cf-2087-5fb6-957d-db545b5b69e5", "Sakichi Takao"],
  ["fa42ca9a-8f36-5778-a2e9-5b9377acc783", "Tadao T Takayanagi"],
  ["05108fc5-e7da-5ba3-b52c-ea14c04fd66b", "Tokutaro Takayanagi"],
  ["44f1c17b-ad29-5fef-a08a-6d9210fca5d6", "Seiichi Takeda"],
  ["5914a559-6eae-5e54-a54b-e32cd04c33c2", "Shiro Takeda"],
  ["817240da-d0ea-5603-9ed3-d9074ca881f4", "Gene M Takei"],
  ["f984cbc5-1d0a-5a35-8936-bf36d85f1f8f", "Roy M Takeno"],
  ["8960fc28-a865-5389-b2a0-0a492e2d84f0", "Haga Takeshi"],
  ["0b02acc1-b885-5352-8023-57ec3bbf95a2", "John Tako"],
  ["36c9a385-88ce-5b27-8440-500dd6a07976", "Josef Talarek"],
  ["37c01a7e-2c83-5edb-bdc6-e7ab29819871", "Hampton Talbot"],
  ["f6038c58-22f8-571c-95a3-96f048f958e2", "James F Talbot"],
  ["7aadf0d0-3879-50a9-ada4-26e643ff4e29", "Janice Talbot"],
  ["44a3dee4-42a3-5bfb-b8a5-9a2c681b0c48", "Jerree Lee S Talbot"],
  ["298d6c95-4287-5df1-a39e-f2f38c7dc946", "Max V Talbot"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 938 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("Tadao Takayanagi separates the immediate hospital employer from earlier roles", async ({ request, page }) => {
  await page.goto("./people/fa42ca9a-8f36-5778-a2e9-5b9377acc783/");
  const main = page.locator("main");
  await expect(main).toContainText("University Hospital (Ann Arbor)");
  await expect(main).toContainText("Butcher");
  await expect(main).toContainText("Hotel Utah");
  await expect(main).toContainText("Weber's Tavern");
  await expect(main).toContainText("University of California, Berkeley");
  await expect(main).toContainText("Topaz");
  await expect(main).toContainText("incarceration");

  const people = await peopleShard(request, "t");
  const person = people.find((item: { person_id: string }) => item.person_id === "fa42ca9a-8f36-5778-a2e9-5b9377acc783");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "University Hospital (Ann Arbor)",
    occupation: "butcher",
    relationship_type: "employment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "medium",
  });
  expect(person.last_civilian_pre_service[0].affiliation_id)
    .toBe(person.immediate_pre_oss_affiliations[0].affiliation_id);
  expect(person.other_pre_oss_affiliations.map((item: { canonical_organization: string }) => item.canonical_organization))
    .toEqual(expect.arrayContaining(["Hotel Utah", "Weber's Tavern", "University of California, Berkeley", "War Relocation Authority"]));
});

test("the two William Takala rows stay separate and only the reviewed row receives an occupation", async ({ request, page }) => {
  const people = await peopleShard(request, "w");
  const first = people.find((item: { person_id: string }) => item.person_id === "880de019-0520-5181-81d2-51aca3ae2365");
  const second = people.find((item: { person_id: string }) => item.person_id === "95e3497e-b8db-5e19-99ed-6d006a651eed");
  expect(first.possible_duplicate_group).toBeTruthy();
  expect(second.possible_duplicate_group).toBe(first.possible_duplicate_group);
  expect(first.claims).toHaveLength(0);
  expect(second.claims.some((claim: { claim_text: string }) => claim.claim_text.includes("Correspondence clerks"))).toBe(true);

  await page.goto("./people/95e3497e-b8db-5e19-99ed-6d006a651eed/");
  const main = page.locator("main");
  await expect(main).toContainText("Correspondence clerks");
  await expect(main).toContainText("no employer or workplace");
  await expect(main).not.toContainText("Last civilian employer before wartime service");
});

test("Josef Talarek publishes a high-confidence Polish military pathway and alias", async ({ request, page }) => {
  await page.goto("./people/36c9a385-88ce-5b27-8440-500dd6a07976/");
  const main = page.locator("main");
  await expect(main).toContainText("Józef Herzyk");
  await expect(main).toContainText("Polish Armed Forces in the West");
  await expect(main).toContainText("Project Eagle");
  await expect(main).toContainText("wireless operator");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  const people = await peopleShard(request, "j");
  const person = people.find((item: { person_id: string }) => item.person_id === "36c9a385-88ce-5b27-8440-500dd6a07976");
  expect(person.name_variants).toEqual(expect.arrayContaining(["Józef Talarek", "Józef Herzyk"]));
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Polish Armed Forces in the West",
    relationship_type: "military_assignment",
    claim_confidence: "high",
  });
});

test("Gene Takei publishes the Army-to-OSS pathway without inventing a civilian employer", async ({ request, page }) => {
  await page.goto("./people/817240da-d0ea-5603-9ed3-d9074ca881f4/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Private First Class");
  await expect(main).toContainText("Fort Leonard Wood");
  await expect(main).toContainText("Burma");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  const people = await peopleShard(request, "g");
  const person = people.find((item: { person_id: string }) => item.person_id === "817240da-d0ea-5603-9ed3-d9074ca881f4");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    relationship_type: "military_assignment",
    temporal_basis: "strongly_date_bounded",
  });
});

test("Roy Takeno keeps three newspaper roles qualified and incarceration-aware", async ({ request, page }) => {
  await page.goto("./people/f984cbc5-1d0a-5a35-8936-bf36d85f1f8f/");
  const main = page.locator("main");
  await expect(main).toContainText("Japan-California Daily News");
  await expect(main).toContainText("Manzanar Free Press");
  await expect(main).toContainText("Rocky Shimpo");
  await expect(main).toContainText("incarceration");

  const people = await peopleShard(request, "r");
  const person = people.find((item: { person_id: string }) => item.person_id === "f984cbc5-1d0a-5a35-8936-bf36d85f1f8f");
  expect(person.identity_status).toBe("probable");
  expect(person.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "Rocky Shimpo",
    claim_confidence: "medium",
  });
  expect(person.other_pre_oss_affiliations).toHaveLength(2);
});

test("qualified institutional leads remain qualified rather than silently promoted", async ({ request }) => {
  const people = await peopleShard(request, "s");
  const sakichi = people.find((item: { person_id: string }) => item.person_id === "c27ff5cf-2087-5fb6-957d-db545b5b69e5");
  const shiro = people.find((item: { person_id: string }) => item.person_id === "5914a559-6eae-5e54-a54b-e32cd04c33c2");
  expect(sakichi.identity_status).toBe("probable");
  expect(sakichi.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Amache Consumer Enterprises, Inc.",
    temporal_basis: "temporal_relation_uncertain",
    claim_confidence: "medium",
  });
  expect(shiro.identity_status).toBe("probable");
  expect(shiro.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Military Intelligence Service Language School",
    role_title: "Civilian faculty member",
    temporal_basis: "temporal_relation_uncertain",
  });
});

test("Jerree Talbot preserves the surname-order uncertainty", async ({ request, page }) => {
  await page.goto("./people/44a3dee4-42a3-5bfb-b8a5-9a2c681b0c48/");
  const main = page.locator("main");
  await expect(main).toContainText("Jerree Lee Talbot Smith");
  await expect(main).toContainText("U.S. Office of Censorship");
  await expect(main).toContainText("surname ordering");

  const people = await peopleShard(request, "j");
  const person = people.find((item: { person_id: string }) => item.person_id === "44a3dee4-42a3-5bfb-b8a5-9a2c681b0c48");
  expect(person.identity_status).toBe("probable");
  expect(person.other_pre_oss_affiliations[0].claim_confidence).toBe("medium");
});

test("ambiguous same-name cases receive no borrowed affiliation", async ({ request, page }) => {
  await page.goto("./people/fb335f1e-9687-586f-b536-a50c132cb3b2/");
  const main = page.locator("main");
  await expect(main).toContainText("Two incompatible same-name wartime biographies");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");

  const people = await peopleShard(request, "s");
  const person = people.find((item: { person_id: string }) => item.person_id === "fb335f1e-9687-586f-b536-a50c132cb3b2");
  expect(person.identity_status).toBe("ambiguous");
  expect(person.claims).toHaveLength(0);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 938 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("University Hospital");
  await expect(main).not.toContainText("Rocky Shimpo");
});

test("Batch 938 evidence excludes credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("2139654");
  expect(evidence).not.toContain("33451327");
  expect(evidence).not.toContain("190464461");
  expect(evidence).not.toContain("37553062");
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 938 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 635,
    research_attempted_people: 14_518,
    verified_affiliation_people: 1_026,
    verified_employer_people: 463,
    archival_review_assessed_people: 12_991,
    published_claims: 8_959,
    public_sources: 5_912,
  });
});
