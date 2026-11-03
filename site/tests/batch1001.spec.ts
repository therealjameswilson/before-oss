import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page491-wargo-to-waters-review_batch-1001_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["a8016077-f892-598d-b293-e7f46dcdecfd", "Stephen J Wargo"],
  ["d9572d34-1f9d-5650-821a-412223e6f362", "Waldo W Waring"],
  ["0be00d1d-21ca-569c-a32d-90e74fea3836", "Joseph J Warman"],
  ["33c4d214-2cad-5297-a566-5c3580dfc49b", "Adolphe J Warner"],
  ["34fe30da-78f4-5535-9b36-55267c69e1ef", "Arthur C Warner"],
  ["1f8b79b4-0d38-558f-b3cb-d8f8bfb97aeb", "Edwin E Warner"],
  ["404b95d9-57bb-5ec7-9e32-b7467e75c600", "Eugene P Warner"],
  ["cc98d8f8-ae18-52be-8f96-c560af5dae31", "J C Warner"],
  ["911ff8bb-d5d9-5a83-a676-83444e861b60", "John S Warner"],
  ["98e1a775-897d-5d07-a044-83624f91a0de", "Margaret Warner"],
  ["8f9d31f3-56d5-5838-9bf5-019c35ab5e9f", "Marion A Warner"],
  ["ff8d47e4-635f-59e1-b5e7-b2e4fa11a179", "Ralph P Warner"],
  ["efb61a4e-cf44-5022-8b4e-7cb7fb995f0c", "Sam B Warner"],
  ["813dbe56-56ea-511f-a41c-1a3d9169874c", "W. Lloyd Warner"],
  ["ad9ae311-9c12-544f-bb91-f230050d9e74", "Aaron D Warnock"],
  ["c858e5fe-1609-5798-8f79-53eca3937c9c", "John C Warnock"],
  ["8b775eea-a03b-543d-98ed-40be4c602792", "* Warren"],
  ["b326361e-4098-553d-8f5b-d5b4b490ecb7", "Charles H Warren"],
  ["eb5f4e5d-9208-589c-b4f5-02e4274b7711", "Charlie J Warren"],
  ["57a43dbf-1a33-534b-955a-aab3b7633fbc", "Darrell F Warren"],
  ["dcf0b482-ab8e-5a0e-b0cb-df66645a1504", "Frank Miles Warren"],
  ["c2438c9f-b1b8-592d-9468-747d3ed002cb", "George E Warren"],
  ["c13d0727-a63f-52e1-89f1-d573971dfa58", "Janet Carolyn Warren"],
  ["5ae50702-aae8-56a9-afe3-db1f3ebe690d", "Northam Warren Jr."],
  ["a1319427-adda-50e6-bbb4-73717cd45432", "Paul L Warren"],
  ["c798347f-5ddf-5442-a80c-caf48cff5455", "Ralph F Warren"],
  ["537beed5-76d8-5bd9-ad54-040e0cc3290b", "Helga Rose Warrens"],
  ["e9faa646-d4ac-5adc-9c01-4d15da7dec68", "Salomon J Warszawski"],
  ["c87c2938-ead3-58f7-8a78-932704b681bb", "George Wartenbert"],
  ["1e5c0e34-d68a-52e6-b1f9-cb644b8cccc4", "Anna M Warters"],
  ["f4890abc-e000-5bdf-9eb6-e197ced081ab", "John William Waser"],
  ["8c491ced-1cd9-5e63-9fd0-0cb81588e02b", "Abbott Washburn"],
  ["ec3a1750-f61f-56c5-9742-98c9f2326e0e", "Emlen D Washburn"],
  ["88c0e9e9-dd30-521c-beb1-92e5c862f92d", "Arthur Washington"],
  ["f6bb3b94-048f-531c-a0c1-f62134849fe8", "Bushrod C Washington"],
  ["00b472e6-1caf-594b-bbed-29b903030aea", "Wilbert Washington"],
  ["8ac64ad3-5cea-574e-aaca-aa290ad404f8", "John J Wask"],
  ["8bb70dd9-0143-5ab0-bbe3-a5cf1c9766d6", "Frank S Watanabe"],
  ["1c940876-93a6-5e82-a6f7-0efe4c7a8d92", "Howard T Watanabe"],
  ["5d1a383f-2578-5076-9e92-0452cbfa5e5a", "Kazumi Watanabe"],
  ["84b75ea2-9eac-5961-887c-1a3f41470449", "Lucy E Waterman"],
  ["9f2c0364-363a-56a9-b48c-9c977039b1a5", "Richard E Waterman"],
  ["88879c6b-b450-5195-9c97-37ff0c25779c", "Robert W Waterman"],
  ["41976ddf-1fc5-5600-95eb-52fcfc4dd71b", "Robert P Waterman"],
  ["6be568c2-1fab-5868-be5f-6e11b6d3bf03", "Alexander Waters"],
  ["b36e432f-89da-55ae-931d-211f2cd4f2d1", "Arthur R Waters"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find(
    (item: { person_id: string }) => item.person_id === id,
  );
}

test("Batch 1001 publishes all 46 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("nine Army bridges publish bounded categories without invented institutions", async ({ request }) => {
  const expected = new Map([
    [profiles[2][0], ["jeweler, watchmaker, goldsmith, or silversmith", "unknown"]],
    [profiles[3][0], ["salesman or sales agent, except to consumers", "unknown"]],
    [profiles[11][0], ["blacksmith, forgerman, or hammerman", "unknown"]],
    [profiles[15][0], ["student", "student"]],
    [profiles[18][0], ["general farmer", "unknown"]],
    [profiles[19][0], ["electrician", "unknown"]],
    [profiles[37][0], ["sales clerk", "unknown"]],
    [profiles[38][0], ["general clerk", "unknown"]],
    [profiles[41][0], ["student", "student"]],
  ]);
  for (const [id, [occupation, relationship]] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Eugene Warner preserves civilian status and an occupation-only result", async ({ request }) => {
  const person = await publicPerson(request, profiles[6][0], profiles[6][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(person.source_records[0]).toMatchObject({
    rank_as_indexed: "Civilian",
    box: "817",
    pdf_page: 491,
  });
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "reporter and writer",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  ]);
});

test("Charles Warren is classified from the printed USNR note", async ({ request }) => {
  const person = await publicPerson(request, profiles[17][0], profiles[17][1]);
  expect(person).toMatchObject({
    identity_status: "unresolved",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(person.source_records[0]).toMatchObject({
    rank_as_indexed: "Capt.",
    notes_as_indexed: "USNR",
  });
});

test("John Warner separates the immediate military assignment from the last civilian employer", async ({ request }) => {
  const person = await publicPerson(request, profiles[8][0], profiles[8][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "390th Bombardment Group (Heavy)",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Union Trust Company",
      role_title: "Assistant Trust Investment Officer",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
});

test("Sam Warner keeps Harvard and War Production Board chronology qualified", async ({ request }) => {
  const person = await publicPerson(request, profiles[12][0], profiles[12][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "Harvard University",
        relationship_type: "employment",
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
      }),
      expect.objectContaining({
        canonical_organization: "War Production Board",
        relationship_type: "government_assignment",
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    ]),
  );
});

test("W. Lloyd Warner publishes only documented prewar university employment", async ({ request }) => {
  const person = await publicPerson(request, profiles[13][0], profiles[13][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Chicago",
      role_title: "professor of anthropology and sociology",
      start_date: "1935",
      end_date: "1959",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
});

test("Northam Warren publishes Army service without reusing a postwar employer", async ({ request }) => {
  const person = await publicPerson(request, profiles[23][0], profiles[23][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  expect(JSON.stringify(person)).not.toContain("Chesebrough-Ponds");
});

test("Abbott Washburn separates Navy assignment from General Mills employment", async ({ request }) => {
  const person = await publicPerson(request, profiles[31][0], profiles[31][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Navy",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "General Mills, Inc.",
      relationship_type: "employment",
      start_date: "1937",
      end_date: null,
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
});

test("Stephen Wargo conflict transfers no Army occupation", async ({ request }) => {
  const person = await publicPerson(request, profiles[0][0], profiles[0][1]);
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
    }),
  ]);
});

test("incomplete and unbridged rows retain dignified archival outcomes", async ({ request }) => {
  for (const index of [16, 27, 28, 34, 42, 45] as const) {
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

test("Batch 1001 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1001 public claims retain inspectable citations", async ({ request }) => {
  for (const index of [0, 2, 3, 6, 8, 11, 12, 13, 15, 18, 19, 23, 31, 37, 38, 41] as const) {
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

test("Batch 1001 publishes exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 679,
    research_attempted_people: 15_978,
    verified_affiliation_people: 1_149,
    verified_employer_people: 521,
    archival_review_assessed_people: 14_453,
    published_claims: 10_242,
    public_sources: 6_554,
  });
});
