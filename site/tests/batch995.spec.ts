import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page488-walk-to-walker-review_batch-995_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["fab5ef20-f001-5dea-ada9-27184f1b7f86", "Richard D Walk"],
  ["e9cdf34e-9e6b-5fbe-91da-bbaf5cb9a283", "Albert Walker"],
  ["c4f2769f-aeec-59d5-ba0f-f94f88af5ec2", "Alvin Walker"],
  ["a5b7d8d3-810d-517e-bc61-87a0359a0dfa", "Ann C Walker"],
  ["e642b0c8-a5fa-533d-b208-cfe63fecbf54", "Ann Walker"],
  ["2842489c-2541-56bf-9ba2-be9594be05c9", "Anna G Walker"],
  ["f752f636-d84d-58ca-aae7-578d4a7ea918", "Bette B Walker"],
  ["7cef39d0-6022-5e0d-957b-d2ff21b82978", "Burdeau Walker"],
  ["bbb69569-76d8-53dd-95df-4110d86d285a", "Charles S Walker Jr."],
  ["5380b9b7-7cc7-5ed7-9ee4-e5a6eb58dc23", "Charlotte F Walker"],
  ["606124e8-7690-5a13-b93c-8e4994173bfd", "Doyle E Walker"],
  ["79bdb544-7b3d-51bb-bab0-dd3ee917fe0f", "Earl E Walker"],
  ["afa5978b-65fc-53cb-97f2-eaa95400c45a", "Eleanor Louise Walker"],
  ["e4b38c8f-5816-57e6-bb45-ab6e99af193d", "Fred W Walker"],
  ["25de06bd-bc37-5d02-8963-df108cbd026a", "Fred L Walker Jr."],
  ["bc6c83a9-6eda-5135-ac73-e2ee63bc9a42", "Gordon A Walker"],
  ["82d9e346-f0d1-50d8-926a-18aeadc153bc", "Herman Walker Jr."],
  ["629282c2-60ad-5e4f-a80d-e446f35ec92e", "James Edward Walker"],
  ["3b209b39-4b2e-5d5f-85aa-446afa5b1a07", "John C Walker"],
  ["02336424-ef94-5ca7-8e83-31d3f52e1983", "John W Walker"],
  ["76b5fb40-2b7d-57c0-906b-7ce0b78350f6", "Joseph W Walker"],
  ["66f9c5f9-2f77-5dcf-a5a5-97920f0e17dd", "Lucy B Walker"],
  ["44e05623-d961-5aa5-87e9-1ccbfce38cc8", "Marjorie K Walker"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 995 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("four Army bridges publish only qualified historical occupations", async ({ request }) => {
  const expected = new Map([
    [profiles[0][0], "architect"],
    [profiles[10][0], "chainman, rodman, or axman in surveying"],
    [profiles[13][0], "farm hand on a general farm"],
    [profiles[16][0], "professional occupation, not elsewhere classified"],
  ]);

  for (const [id, occupation] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person.research_status).toBe("occupation_only_found");
    expect(person.personnel_category).toBe("enlisted_army_personnel");
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Richard Walk preserves the transcription uncertainty", async ({ request }) => {
  const person = await publicPerson(request, profiles[0][0], profiles[0][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
  });
  expect(person.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
    expect.objectContaining({ claim_type: "occupation", claim_confidence: "medium" }),
  ]));
});

test("the three printed officers retain officer classification without invented biographies", async ({ request }) => {
  for (const index of [8, 11, 14] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      personnel_category: "commissioned_army_officer",
      commissioned_officer: true,
    });
    expect(person.claims).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Fred L Walker Jr remains unresolved despite a compatible 36th Division namesake", async ({ request }) => {
  const person = await publicPerson(request, profiles[14][0], profiles[14][1]);
  expect(person).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(person.next_action).toContain("No reliable pre-OSS employer has yet been identified");
  expect(person.claims).toHaveLength(0);
});

test("Gordon Walker exposes the Army-name conflict without transferring fields", async ({ request }) => {
  const person = await publicPerson(request, profiles[15][0], profiles[15][1]);
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.archival_file.review_priority).toBe("critical");
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting" }),
  ]);
});

test("Batch 995 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 995 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [0, 10, 13, 15, 16] as const) {
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

test("Batch 995 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_817,
    verified_affiliation_people: 1_143,
    verified_employer_people: 517,
    archival_review_assessed_people: 14_292,
    published_claims: 10_131,
    public_sources: 6_510,
  });
});
