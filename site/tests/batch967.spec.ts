import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page474-robert-true-to-ernest-tsikerdanos-review_batch-967_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["1f3f2f86-1131-5c89-afa0-4584b27e1f66", "Robert E True"],
  ["a597dda4-f3f2-5810-b6a9-b64c36c3a35f", "Svend Truelsen"],
  ["d3e1dd89-72b7-50c4-ae48-5d35b7c412df", "Ralph J Truex"],
  ["ca3e1a33-98bc-5e87-8111-5854761e079a", "Jerry Truhlar"],
  ["06f87d98-2b77-5cc7-9201-187642246fd2", "Jerry Truhler"],
  ["32803515-8f02-5e84-b5e8-7070b27bcc53", "William D Truland"],
  ["a9084a8e-b3c8-5693-a4ea-e7b1d10636ec", "Robert Truman"],
  ["979cc12a-a410-51fe-baf0-df2fa24f98aa", "Carl J Trumm"],
  ["8ad7fbdb-a037-59e3-a49d-f650195d497d", "Shirly R Trumps"],
  ["d2405232-fb46-5186-bdf1-21943702ef2b", "Margaret M Trun"],
  ["3464bec3-da6a-5f1a-848f-6ce2fc249ed0", "Joseph Trunecek"],
  ["262eb5f7-5878-5754-ace3-cd794c08888e", "Charles V Trupia"],
  ["4ad3f882-8c87-5f79-80f5-f747a692788e", "John F Trutza"],
  ["f0ed9496-997a-5d53-b06f-1ba768443d37", "Nicholas Tryforos"],
  ["ac8023d9-1343-57d2-b7e1-3b20feaedfea", "Bernard H Trygstad"],
  ["0aaf902d-ab7a-5157-8f85-606a5bdd7ec0", "Frieda B Tryon"],
  ["fd420531-2b35-5def-bec9-c2c195d0c421", "Robert C Tryon"],
  ["f71cf73f-d6a4-572a-989d-c2817e211b99", "Yueh C Tsai"],
  ["31dbb69d-f3fc-5f4e-a8d7-8ed1806f9911", "Ioannis Tsankaris"],
  ["80e11206-f295-5b89-a9b9-56d41c5a08e2", "Eleftherius Tsantes"],
  ["46c805e8-c8de-5fd5-9f26-8ccfb50d76e3", "Ernest C Tschonis"],
  ["42b9c424-c2f9-5881-ae1c-1d2677b0b01b", "Cheng K Tseng"],
  ["307cecc3-b3f5-5f4c-98e7-f1aede79589c", "Ernest Tsikerdanos"],
] as const;

const occupationProfiles = [
  ["32803515-8f02-5e84-b5e8-7070b27bcc53", "William D Truland", "probable", "radio operator"],
  ["979cc12a-a410-51fe-baf0-df2fa24f98aa", "Carl J Trumm", "probable", "actor or actress"],
  ["3464bec3-da6a-5f1a-848f-6ce2fc249ed0", "Joseph Trunecek", "high_confidence", "secretary"],
  ["4ad3f882-8c87-5f79-80f5-f747a692788e", "John F Trutza", "high_confidence", "millwright"],
  ["f71cf73f-d6a4-572a-989d-c2817e211b99", "Yueh C Tsai", "high_confidence", "private-family domestic-service occupation"],
  ["31dbb69d-f3fc-5f4e-a8d7-8ed1806f9911", "Ioannis Tsankaris", "high_confidence", "construction or maintenance painter"],
  ["80e11206-f295-5b89-a9b9-56d41c5a08e2", "Eleftherius Tsantes", "confirmed", "primary-school or kindergarten teacher"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 967 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("seven Army categories remain qualified occupations without fabricated employers", async ({ request }) => {
  for (const [id, name, identity, occupation] of occupationProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: identity,
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]));
  }
});

test("Svend Truelsen separates last civilian employer from intelligence and government assignments", async ({ request }) => {
  const person = await publicPerson(request, "a597dda4-f3f2-5810-b6a9-b64c36c3a35f", "Svend Truelsen");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Danish General Staff Intelligence Service",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Danish Agricultural Council",
      occupation: "agricultural-council secretary",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Danish Ministry of Agriculture",
      relationship_type: "government_assignment",
      claim_confidence: "medium",
    }),
  ]);
});

test("Robert C Tryon has a verified Berkeley employer and Frieda B Tryon does not", async ({ request }) => {
  const robert = await publicPerson(request, "fd420531-2b35-5def-bec9-c2c195d0c421", "Robert C Tryon");
  expect(robert).toMatchObject({ identity_status: "confirmed", research_status: "verified_employer_found" });
  expect(robert.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "University of California, Berkeley", relationship_type: "employment", claim_confidence: "high" }),
  ]);
  expect(robert.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "University of California, Berkeley", relationship_type: "employment", claim_confidence: "high" }),
  ]);

  const frieda = await publicPerson(request, "0aaf902d-ab7a-5157-8f85-606a5bdd7ec0", "Frieda B Tryon");
  expect(frieda).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(frieda.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(frieda.last_civilian_pre_service).toHaveLength(0);
  expect(frieda.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "University of North Carolina at Chapel Hill", relationship_type: "professional_affiliation", claim_confidence: "medium" }),
  ]);
});

test("Army pathways remain distinct from civilian employment", async ({ request }) => {
  const truex = await publicPerson(request, "d3e1dd89-72b7-50c4-ae48-5d35b7c412df", "Ralph J Truex");
  expect(truex.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment" }),
  ]);
  expect(truex.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Military Academy", relationship_type: "student" }),
  ]);
  expect(truex.last_civilian_pre_service).toHaveLength(0);

  const trumps = await publicPerson(request, "8ad7fbdb-a037-59e3-a49d-f650195d497d", "Shirly R Trumps");
  expect(trumps.name_variants).toEqual(expect.arrayContaining(["Shirly Ray Trumps", "Shirley R. Trumps"]));
  expect(trumps.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment" }),
  ]);
  expect(trumps.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Louisiana National Guard", relationship_type: "military_assignment" }),
  ]);

  const tsikerdanos = await publicPerson(request, "307cecc3-b3f5-5f4c-98e7-f1aede79589c", "Ernest Tsikerdanos");
  expect(tsikerdanos.name_variants).toEqual(expect.arrayContaining(["Ernest John Tsikerdanos", "Chick Tsikerdanos"]));
  expect(tsikerdanos.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "82nd Airborne Division", relationship_type: "military_assignment", claim_confidence: "high" }),
  ]);
  expect(tsikerdanos.last_civilian_pre_service).toHaveLength(0);
});

test("ambiguous, duplicate and conflicting records remain visible without namesake transfer", async ({ request }) => {
  const truePerson = await publicPerson(request, "1f3f2f86-1131-5c89-afa0-4584b27e1f66", "Robert E True");
  expect(truePerson).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(truePerson.claims).toHaveLength(0);

  const duplicateProfiles: Array<{ person_id: string; possible_duplicate_group: string }> = [];
  for (const [id, name] of [
    ["ca3e1a33-98bc-5e87-8111-5854761e079a", "Jerry Truhlar"],
    ["06f87d98-2b77-5cc7-9201-187642246fd2", "Jerry Truhler"],
  ]) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
    });
    expect(person.possible_duplicate_group).toMatch(/^duplicate-/);
    expect(person.claims).toHaveLength(0);
    duplicateProfiles.push(person);
  }
  expect(duplicateProfiles[0].person_id).not.toBe(duplicateProfiles[1].person_id);
  expect(duplicateProfiles[0].possible_duplicate_group).toBe(duplicateProfiles[1].possible_duplicate_group);

  const trupia = await publicPerson(request, "262eb5f7-5878-5754-ace3-cd794c08888e", "Charles V Trupia");
  expect(trupia).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(trupia.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(trupia.last_civilian_pre_service).toHaveLength(0);
  expect(trupia.other_pre_oss_affiliations).toHaveLength(0);
  expect(trupia.claims).toHaveLength(0);
});

test("direct identity evidence does not become an unsupported employer", async ({ request }) => {
  const tryforos = await publicPerson(request, "f0ed9496-997a-5d53-b06f-1ba768443d37", "Nicholas Tryforos");
  expect(tryforos).toMatchObject({ identity_status: "confirmed", commissioned_officer: true, research_status: "requires_archival_review" });
  expect(tryforos.name_variants).toContain("Nicholas J. P. Tryforos");
  expect(tryforos.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(tryforos.last_civilian_pre_service).toHaveLength(0);
  expect(tryforos.other_pre_oss_affiliations).toHaveLength(0);

  const trygstad = await publicPerson(request, "ac8023d9-1343-57d2-b7e1-3b20feaedfea", "Bernard H Trygstad");
  expect(trygstad).toMatchObject({ identity_status: "probable", commissioned_officer: true });
  expect(trygstad.last_civilian_pre_service).toHaveLength(0);
  expect(trygstad.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Navy", relationship_type: "military_assignment", claim_confidence: "medium" }),
  ]);
});

test("Batch 967 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toContain("Max Margolies");
});

test("Batch 967 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 664,
    research_attempted_people: 15_177,
    verified_affiliation_people: 1_092,
    verified_employer_people: 488,
    archival_review_assessed_people: 13_653,
    published_claims: 9_573,
    public_sources: 6_216,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Students");
});
