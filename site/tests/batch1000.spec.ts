import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page490-ward-to-warfield-review_batch-1000_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["8dbec3ac-780d-537e-b275-15eb457ebb1a", "Betty Lou Ward"],
  ["acf77d4c-cdde-5187-8840-c018ac689b1d", "Charles D Ward"],
  ["b5f31ff9-2798-59f1-aa28-1999599622cc", "Francis R Ward"],
  ["3bb338fc-74b8-5158-85cb-446b5997af69", "Hugh C Ward Jr."],
  ["00d4faca-822d-50e9-a3be-749c7bf0370a", "James R Ward"],
  ["9687c2b9-417a-5123-adb8-3a1f90046c95", "Jean E Ward"],
  ["733e8b24-040a-5e54-8d01-7c63ec5c1bed", "Kathryn Ward"],
  ["e6847ed1-5bf3-510d-8713-3f67c0025b77", "Luther B Ward"],
  ["1fc82c30-5734-5011-83e3-04d47578ec25", "M. Eugene Ward"],
  ["5dcf386e-3a45-5ba9-97aa-76eaf81a9a43", "Mabel T Ward"],
  ["0047c86d-d525-502b-b9af-dfd5ce252870", "Malcolm C Ward"],
  ["7b7a2502-afcd-5d38-919e-f14455be282e", "Mary B Ward"],
  ["b9fc6164-4765-52dc-bd65-9422318bca73", "Paul L Ward"],
  ["4cdfb92a-831d-51d6-a6e3-c0223f07ed5b", "Philip S Ward"],
  ["778665c4-757e-598a-bbe3-e4bc98ddadf2", "Robert L Ward"],
  ["03030a9c-ebef-5dd2-8ddd-a9f7709d36e6", "Thomas N Ward"],
  ["7ab1af89-8ef5-58b1-a40f-437f78e56126", "Edythe C Warden"],
  ["c808443d-d646-5233-8851-7017c717ed80", "Philip Wardner"],
  ["2ce5dcd0-29f7-52f6-ada6-fae6349d8d6b", "Edmund D Wardrop"],
  ["0c292d66-d569-56d6-981a-02988e793fe5", "Tom Karr Ware Jr."],
  ["b88028d0-754f-5590-8a00-bb9a9aab0f70", "Roscoe H Wareham"],
  ["c945176d-c547-5ce4-8c54-c397ce14b890", "Peter P Warenzak"],
  ["3d88483a-88a7-5d92-b263-b8a0ee44cf0d", "Gaither P Warfield"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1000 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("seven Army bridges publish qualified categories without invented employers", async ({ request }) => {
  const expected = new Map([
    [profiles[1][0], ["automobile-manufacturing occupation, not elsewhere classified", "unknown"]],
    [profiles[3][0], ["actor", "unknown"]],
    [profiles[7][0], ["student", "student"]],
    [profiles[13][0], ["student", "student"]],
    [profiles[14][0], ["weigher", "unknown"]],
    [profiles[20][0], ["electrician", "unknown"]],
    [profiles[21][0], ["nonprocess manufacturing occupation, not elsewhere classified", "unknown"]],
  ]);
  for (const [id, [occupation, relationship]] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Hugh Ward preserves the printed civilian OSS status", async ({ request }) => {
  const person = await publicPerson(request, profiles[3][0], profiles[3][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(person.source_records[0]).toMatchObject({
    indexed_first_name: "Hugh, Jr.",
    indexed_middle: "C",
    rank_as_indexed: "Civ.",
    box: "816",
    pdf_page: 490,
  });
});

test("Paul Ward publishes three bounded teaching roles, not an immediate employer", async ({ request }) => {
  const person = await publicPerson(request, profiles[12][0], profiles[12][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Harvard University", relationship_type: "employment", temporal_basis: "documented_prewar", claim_confidence: "medium" }),
      expect.objectContaining({ canonical_organization: "Radcliffe College", relationship_type: "employment", temporal_basis: "documented_prewar", claim_confidence: "medium" }),
      expect.objectContaining({ canonical_organization: "Russell Sage College", role_title: "assistant professor of history", claim_confidence: "medium" }),
    ]),
  );
  expect(person.other_pre_oss_affiliations).toHaveLength(3);
  expect(person.claims).toHaveLength(4);
});

test("Gaither Warfield publishes dated church affiliations with the wartime overlap qualified", async ({ request }) => {
  const person = await publicPerson(request, profiles[22][0], profiles[22][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "Methodist mission in Poland",
        relationship_type: "professional_affiliation",
        start_date: "1924",
        end_date: "1942",
        temporal_basis: "documented_prewar",
        claim_confidence: "high",
        publication_status: "published",
      }),
      expect.objectContaining({
        canonical_organization: "Board of Missions of the Methodist Church",
        start_date: "1942",
        end_date: "1946",
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]),
  );
});

test("Edmund Wardrop remains probable and Princeton is student status only", async ({ request }) => {
  const person = await publicPerson(request, profiles[18][0], profiles[18][1]);
  expect(person).toMatchObject({
    identity_status: "probable",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Princeton University",
      relationship_type: "student",
      end_date: "1934",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("Jean Ward conflict transfers no Army biography", async ({ request }) => {
  const person = await publicPerson(request, profiles[5][0], profiles[5][1]);
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting" }),
  ]);
});

test("unbridged James Ward and Philip Wardner leads remain unresolved", async ({ request }) => {
  for (const index of [4, 17] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 1000 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1000 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [1, 3, 5, 7, 12, 13, 14, 18, 20, 21, 22] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person.claims.length).toBeGreaterThan(0);
    for (const item of person.claims) {
      expect(item.sources.length).toBeGreaterThan(0);
      for (const link of item.sources) {
        expect(link.source.stable_url || link.source.archival_identifier).toBeTruthy();
        const excerpt = link.excerpt_override ?? item.evidence_excerpt ?? "";
        expect(excerpt.trim() ? excerpt.trim().split(/\s+/).length : 0).toBeLessThanOrEqual(25);
      }
    }
  }
});

test("Batch 1000 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_932,
    verified_affiliation_people: 1_147,
    verified_employer_people: 519,
    archival_review_assessed_people: 14_407,
    published_claims: 10_208,
    public_sources: 6_542,
  });
});
