import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page475-joseph-turcotte-to-mildred-turner-review_batch-970_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["a2f22323-2d3a-50fe-a2b2-b67b8d3a6253", "Joseph E Turcotte"],
  ["5029cf18-6843-58b3-a9d5-bd89a2ffccf4", "John Turean"],
  ["cae8ee63-77b7-5b6f-933c-577360d0a0fb", "Leonard S Turkowski"],
  ["98c38d68-3fee-5c00-9cb7-fb7dc7a48249", "August A Turlano"],
  ["43d20da9-2ff9-5732-8e6c-126abbcb0b40", "Carl W Turley"],
  ["2f9c3116-ab53-51b0-8618-b04abf056627", "Grady V Turley"],
  ["4ff7bce1-cef9-5c40-b79a-fc4493625ec3", "Dennis H Turnbull"],
  ["f59b7664-3c11-533c-827f-6cc6f742efc4", "Douglas H Turnbull"],
  ["cb434056-7a1e-54c1-8239-a141caa85f96", "Fredrick Turnbull"],
  ["e406630e-c5da-5d8e-826d-463e8c577e6b", "Robert L Turnbull"],
  ["415f3a77-a884-51c3-b9fa-05d7b0575d5e", "Robert T Turnbull"],
  ["3fe00325-5ead-586f-8f25-337bd56c685f", "Ronald B Turnbull"],
  ["cb43dd8f-a17c-50ea-8ddb-0bddefb6f932", "William Turnbull"],
  ["d20803ab-67c1-5afe-bde2-f11ea7cb0a02", "Campbell Turner"],
  ["8f4710f2-9061-58c3-b539-b794eb783096", "Charles N Turner"],
  ["e87a0151-6edd-5cf4-8686-0937b4e0ae80", "Dora Turner"],
  ["aa8a566b-5fb0-5694-a270-f56909e7e083", "Gladys Turner"],
  ["e2aea350-195f-5aab-b91f-eecee44b996f", "Hugh W Turner"],
  ["9a83dca7-ea84-5abb-9139-fb7448ee5dde", "John L Turner"],
  ["e695bb1b-ee87-56e8-af3b-5cf51377eed3", "John M Turner"],
  ["c7fed2e6-f649-5059-98cc-56d7be89ccdc", "Marden S Turner"],
  ["cea7eb07-203b-5308-acc3-8f074a9c52be", "Margaret H Turner"],
  ["6e04f465-6968-56dc-8252-26dbf33beec3", "Mildred M Turner"],
] as const;

const occupationProfiles = [
  ["a2f22323-2d3a-50fe-a2b2-b67b8d3a6253", "Joseph E Turcotte", "semiskilled machine-shop or related worker, not elsewhere classified", "unknown", "documented_prewar"],
  ["5029cf18-6843-58b3-a9d5-bd89a2ffccf4", "John Turean", "student", "student", "documented_prewar"],
  ["98c38d68-3fee-5c00-9cb7-fb7dc7a48249", "August A Turlano", "lawyer or judge", "unknown", "documented_prewar"],
  ["f59b7664-3c11-533c-827f-6cc6f742efc4", "Douglas H Turnbull", "chauffeur or driver of a bus, taxi, truck or tractor", "unknown", "documented_prewar"],
  ["415f3a77-a884-51c3-b9fa-05d7b0575d5e", "Robert T Turnbull", "recreation or amusement attendant, not elsewhere classified", "unknown", "documented_prewar"],
  ["e2aea350-195f-5aab-b91f-eecee44b996f", "Hugh W Turner", "general-industry clerk", "unknown", "documented_prewar"],
  ["9a83dca7-ea84-5abb-9139-fb7448ee5dde", "John L Turner", "student", "student", "temporal_relation_uncertain"],
  ["e695bb1b-ee87-56e8-af3b-5cf51377eed3", "John M Turner", "student", "student", "documented_prewar"],
  ["c7fed2e6-f649-5059-98cc-56d7be89ccdc", "Marden S Turner", "manufacturing foreman", "unknown", "documented_prewar"],
] as const;

const unresolvedProfiles = [
  ["cae8ee63-77b7-5b6f-933c-577360d0a0fb", "Leonard S Turkowski"],
  ["4ff7bce1-cef9-5c40-b79a-fc4493625ec3", "Dennis H Turnbull"],
  ["cb434056-7a1e-54c1-8239-a141caa85f96", "Fredrick Turnbull"],
  ["e406630e-c5da-5d8e-826d-463e8c577e6b", "Robert L Turnbull"],
  ["3fe00325-5ead-586f-8f25-337bd56c685f", "Ronald B Turnbull"],
  ["cb43dd8f-a17c-50ea-8ddb-0bddefb6f932", "William Turnbull"],
  ["8f4710f2-9061-58c3-b539-b794eb783096", "Charles N Turner"],
  ["e87a0151-6edd-5cf4-8686-0937b4e0ae80", "Dora Turner"],
  ["aa8a566b-5fb0-5694-a270-f56909e7e083", "Gladys Turner"],
  ["cea7eb07-203b-5308-acc3-8f074a9c52be", "Margaret H Turner"],
  ["6e04f465-6968-56dc-8252-26dbf33beec3", "Mildred M Turner"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 970 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("nine Army categories stay qualified and separate from immediate or named-employer claims", async ({ request }) => {
  for (const [id, name, occupation, relationship, temporalBasis] of occupationProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        temporal_basis: temporalBasis,
        claim_confidence: "medium",
      }),
    ]));
  }
});

test("August Turlano preserves the Iurlano variant and special archive location", async ({ request }) => {
  const person = await publicPerson(request, "98c38d68-3fee-5c00-9cb7-fb7dc7a48249", "August A Turlano");
  expect(person.name_variants).toEqual(expect.arrayContaining(["August A Iurlano"]));
  expect(person.source_records).toEqual(expect.arrayContaining([
    expect.objectContaining({ box: "365", archive_location: "230/86/33/06", rank_as_indexed: "Cpl." }),
  ]));
  expect(person.identity_evidence).toContain("surname conflict remains visible");
});

test("Campbell Turner has one qualified school affiliation, not an immediate employer", async ({ request, page }) => {
  const person = await publicPerson(request, "d20803ab-67c1-5afe-bde2-f11ea7cb0a02", "Campbell Turner");
  expect(person).toMatchObject({ identity_status: "probable", research_status: "requires_archival_review" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Turner's Diplomatic School",
      role_title: "director",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
      identity_confidence: "probable",
      claim_confidence: "medium",
    }),
  ]);
  expect(person.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "medium", publication_status: "publish_qualified" }),
    expect.objectContaining({ claim_type: "other_pre_oss_affiliation", claim_confidence: "medium", publication_status: "publish_qualified" }),
  ]));
  await page.goto("./organizations/f24ecbc7-450d-5c41-8fdf-a2e2286b41f2/");
  await expect(page.getByRole("heading", { name: "Turner's Diplomatic School", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Campbell Turner");
});

test("eleven unresolved profiles remain dignified archival-review cases", async ({ request }) => {
  for (const [id, name] of unresolvedProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Carl and Grady Turley retain identity evidence without invented occupations", async ({ request }) => {
  for (const [id, name] of [
    ["43d20da9-2ff9-5732-8e6c-126abbcb0b40", "Carl W Turley"],
    ["2f9c3116-ab53-51b0-8618-b04abf056627", "Grady V Turley"],
  ]) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
    ]);
  }
});

test("Batch 970 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 970 publishes exact coverage counters without changing verified-employer or oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 664,
    research_attempted_people: 15_246,
    verified_affiliation_people: 1_094,
    verified_employer_people: 488,
    archival_review_assessed_people: 13_722,
    published_claims: 9_641,
    public_sources: 6_245,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
