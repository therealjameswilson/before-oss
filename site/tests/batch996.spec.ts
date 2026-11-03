import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page488-walker-to-wallace-review_batch-996_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["466b5612-1274-5490-a2db-e8df9e243b13", "Mary Virginia Walker"],
  ["f1ee22dc-e66e-5954-bb75-ffffe5d1f7c0", "Morley Walker"],
  ["45ff3de0-3a9b-50a3-8f19-1c53b6a649bf", "Nora Walker"],
  ["9ee3948c-3dee-5078-9bd0-e5595bede27e", "Philip G Walker"],
  ["c1845772-6df0-53bb-84b0-60fb88d41b80", "Raymond E Walker"],
  ["084a2157-d631-51ee-bd61-ec09efb64202", "Reinhold Walker"],
  ["36343c8d-ea8b-54bf-b6f2-555f9506b595", "Richard J Walker"],
  ["5c303c26-d46d-5481-bdac-f9cbcc737083", "Robert N Walker"],
  ["ba8c8f52-f4be-5af6-a3c5-2683ee52cd80", "Robert M Walker"],
  ["40b7f95c-8c3e-5b7e-bc55-9dff49bf847f", "Robert M Walker"],
  ["2e8b3586-7976-57f5-a9ce-5f1ee04e7917", "Roy L Walker"],
  ["ba6c677b-1da9-569c-9561-91b6ed996182", "Sinclair C Walker"],
  ["3fdb6199-8323-5e87-a7b1-85d23ac514ba", "T.E. Walker"],
  ["32855ded-c355-56f8-98bb-e140410da6cf", "Vincent Walker"],
  ["b55b188c-7264-50b4-9295-9174ebd72054", "Wesley E Walker"],
  ["252a6f06-c8e6-5184-9f1b-6ac4f9428ebd", "William E Walker"],
  ["08b751b5-8153-5b80-aba2-234d85a7e1af", "Philip Walkley"],
  ["a1174b10-b91a-5ce6-8796-75d331c2d091", "Fred Wall Jr."],
  ["b9ef16f7-ea2c-5a27-a95a-1df21e528219", "Robert B Wall"],
  ["8bd20855-5dac-5616-bdc6-be3c48394139", "Temple A Wall Jr."],
  ["3b7644de-050b-5216-ab0c-44e83b010f92", "Curt M Wallace"],
  ["c1d97c2b-84f9-5b2f-9f80-b4eb06948d33", "Dudley R Wallace"],
  ["dfb5ff48-b259-575b-bea2-e4f319b3da68", "Elery P Wallace"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 996 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("six Army bridges publish only qualified occupation or student categories", async ({ request }) => {
  const expected = new Map([
    [profiles[1][0], ["student", "student"]],
    [profiles[9][0], ["secondary-school teacher or principal", "employment"]],
    [profiles[10][0], ["farm hand on a general farm", "employment"]],
    [profiles[11][0], ["actor", "employment"]],
    [profiles[18][0], ["student", "student"]],
    [profiles[20][0], ["photographer", "employment"]],
  ]);

  for (const [id, [occupation, relationship]] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person.research_status).toBe("occupation_only_found");
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

test("Sinclair Walker and Curt Wallace retain documented name uncertainty", async ({ request }) => {
  for (const index of [11, 20] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
    });
    expect(person.claims).toEqual(expect.arrayContaining([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
      expect.objectContaining({ claim_type: "occupation", claim_confidence: "medium" }),
    ]));
  }
});

test("the two printed officers retain officer classification without invented biographies", async ({ request }) => {
  for (const index of [3, 15] as const) {
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

test("the adjacent Robert M Walker rows remain separate", async ({ request }) => {
  const unresolved = await publicPerson(request, profiles[8][0], profiles[8][1]);
  const armyMatch = await publicPerson(request, profiles[9][0], profiles[9][1]);
  expect(unresolved).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(unresolved.claims).toHaveLength(0);
  expect(armyMatch).toMatchObject({
    identity_status: "confirmed",
    research_status: "occupation_only_found",
  });
  expect(armyMatch.other_pre_oss_affiliations[0].occupation).toBe(
    "secondary-school teacher or principal",
  );
});

test("Raymond Walker exposes the Army-name conflict without transferring fields", async ({ request }) => {
  const person = await publicPerson(request, profiles[4][0], profiles[4][1]);
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

test("Robert N Walker remains blocked rather than publishing an inaccessible-source claim", async ({ request }) => {
  const person = await publicPerson(request, profiles[7][0], profiles[7][1]);
  expect(person).toMatchObject({
    identity_status: "unresolved",
    research_status: "blocked_by_source_access",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.archival_file.review_priority).toBe("critical");
  expect(person.claims).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.next_action).toContain("Verify the source pages before accepting");
});

test("Batch 996 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 996 public claims retain inspectable source citations", async ({ request }) => {
  for (const index of [1, 4, 9, 10, 11, 18, 20] as const) {
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

test("Batch 996 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_840,
    verified_affiliation_people: 1_143,
    verified_employer_people: 517,
    archival_review_assessed_people: 14_315,
    published_claims: 10_144,
    public_sources: 6_514,
  });
});
