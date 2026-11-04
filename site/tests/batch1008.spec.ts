import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page498-werner-to-weston-review_batch-1008_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["06eb2019-df98-55f3-aa79-2ec688eab677", "Marjorie J Werner"],
  ["b5fef31b-68d9-5199-af8f-1ece8d6a0f5b", "Naomi R Werner"],
  ["fbb08b7b-d19b-5400-9e4f-03f08ede11d5", "Neale L Werner"],
  ["25dfc434-480e-5828-a485-a25b303984fa", "Joseph Wernersbach"],
  ["2fc3b6d4-ca0d-5cbb-a150-dcc31255fd67", "Doris M Werntz"],
  ["d82b4b8c-1f51-5901-bd59-abcbf59772f1", "Harold J Wersinger"],
  ["2cfb89ab-e239-5461-9fa9-9fe35fa58836", "Jean B Wertheimer"],
  ["84898965-8e48-52a4-a528-1b7b74b2d676", "Sidney S Wertheimer"],
  ["5eedf409-6844-5209-a463-3f7f24836574", "Theodore A Wertime"],
  ["d100f26a-d14b-5e39-83a2-6fd17154f02a", "Louis M Wertley"],
  ["7de3fdd4-3c90-5e28-81c5-4a92a13ff3aa", "Roland E Weschler"],
  ["187e527d-e0cc-54a5-85d6-c503905ed584", "Frank A Wesley Jr."],
  ["a59e997b-0f4f-5378-98ca-648e324c2369", "Harry N Wessel Jr."],
  ["96ae5806-fdb9-5cf9-a63c-bfba23349722", "Arthur H West"],
  ["5bf2b9ee-8cf1-5500-80cf-9c3d6f018d0d", "Carlin J West"],
  ["90da1136-c456-5f1f-9d02-9c1078a03a7d", "David E West"],
  ["5b4795c9-4006-5d02-944d-e0783803feab", "Edythe M West"],
  ["494eb3fc-5608-56f4-bcea-d248f7d0bb2e", "Eleanor West"],
  ["1f3d2471-f0b0-5cc6-8b57-7e6db06f0841", "Jane V West"],
  ["0925e9ca-9c59-5e23-8fa3-a2f319db53d8", "Joe R West"],
  ["435d0e64-ffb0-50a0-9092-7e5419c40968", "Lee E West"],
  ["856cfba7-fca0-5e24-a272-57c38ed15423", "Marjorie West"],
  ["4bf3fa80-e205-511d-9e23-8ae140993a81", "Mary E West"],
  ["9766cd11-b267-5d63-93f5-ba648aeb1396", "Max E West"],
  ["4d549971-32b4-5f39-9b80-9748d59a9613", "Owen A West"],
  ["b5ae9703-e77e-545b-aaa3-38c7f16b9eeb", "Paul West"],
  ["73d2675c-996f-5eae-96c5-f5e081ecfcd7", "Robert C West"],
  ["e95606dd-9394-51b4-bf17-e25ee9a01c73", "Robert C West"],
  ["5e382a0f-0115-5b66-8dcb-2270cedd78c2", "Thomas M West"],
  ["46722351-0394-5a6e-92fd-97f60c1a6ee1", "William West"],
  ["b31a55fc-175a-52c1-9606-77161626f526", "Richard M Westberry"],
  ["4f0c7e11-dc4c-5127-8690-9b0730267753", "Edwin P Westbrook"],
  ["38e97fef-f6c7-52bc-bbb1-cb64a2cae5a7", "Alwood I Westerdahl"],
  ["5b2245c4-c5e7-5c28-8741-07493c31eba9", "Beatrice H Westerlind"],
  ["164f6285-fe64-5b94-9d7e-8c76ef4c46a2", "Raymond J Western"],
  ["06de1f97-0890-5c94-9fc9-ff6b374c9b94", "Tipton M Westfall"],
  ["6cbe576e-2e56-5ac3-acbd-321b488b1201", "Wallace D Westfall"],
  ["e3f52756-4d35-5387-a8f3-08a015d88f88", "Arthur J Westgard"],
  ["146c2e04-0774-51b4-abef-736949c59f2c", "F K Westlake"],
  ["35befa3e-bc07-553f-ad1f-b1e375f6f44f", "Margaret A Westlake"],
  ["fc9f7331-4067-55f8-ab58-f9f3ac4f96e3", "Guy Westmacott"],
  ["eb846920-1abd-5562-85cc-db31dca30df2", "Cecil R Weston"],
  ["2fc54647-b18e-5c77-943d-0acd3f117498", "Joseph H Weston"],
  ["40729d31-4e16-578b-98f9-ec82a0e38b30", "Logan E Weston"],
  ["dc5a290b-412d-5503-bdc1-7b24532d8d58", "Oscar C Weston"],
  ["b2d63e4c-a599-50df-af87-6865b7b1d247", "T B Weston"],
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

test("Batch 1008 publishes all 46 reviewed people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("all 46 page 498 rows remain separately recoverable", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    sourceRows += person.source_records.filter(
      (row: { pdf_page: number }) => row.pdf_page === 498,
    ).length;
  }
  expect(sourceRows).toBe(46);
});

test("eleven Army categories remain qualified and never invent employers", async ({ request }) => {
  const expected = new Map([
    [profiles[2][0], ["student", "student"]],
    [profiles[3][0], ["shipping and receiving clerk", "unknown"]],
    [profiles[7][0], ["routeman", "unknown"]],
    [profiles[8][0], ["professional occupation, not elsewhere classified", "unknown"]],
    [profiles[12][0], ["student", "student"]],
    [profiles[14][0], ["machine-shop and related occupation, not elsewhere classified", "unknown"]],
    [profiles[15][0], ["student", "student"]],
    [profiles[23][0], ["police officer or detective, public service", "unknown"]],
    [profiles[30][0], ["checker", "unknown"]],
    [profiles[31][0], ["actor or actress", "unknown"]],
    [profiles[32][0], ["mechanic or repairman, not elsewhere classified", "unknown"]],
  ]);
  for (const [id, [occupation, relationship]] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
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

test("Doris Werntz keeps the Firestone lead qualified and non-immediate", async ({ request }) => {
  const person = await publicPerson(request, profiles[4][0], profiles[4][1]);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Firestone",
      role_title: "Accountant",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("identity and rank conflicts remain explicit", async ({ request }) => {
  const weschler = await publicPerson(request, profiles[10][0], profiles[10][1]);
  expect(weschler).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(weschler.claims.some((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toBe(true);

  const westgard = await publicPerson(request, profiles[37][0], profiles[37][1]);
  expect(westgard).toMatchObject({
    identity_status: "confirmed",
    research_status: "conflicting_sources",
  });
  expect(westgard.claims.some((claim: { claim_text: string }) => claim.claim_text.includes("disagree on grade"))).toBe(true);
});

test("Paul West, Guy Westmacott, and Logan Weston retain bounded identity conclusions", async ({ request }) => {
  const paul = await publicPerson(request, profiles[25][0], profiles[25][1]);
  expect(paul).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(paul.immediate_pre_oss_affiliations).toHaveLength(0);

  const guy = await publicPerson(request, profiles[40][0], profiles[40][1]);
  expect(guy).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    allied_or_foreign_personnel: true,
  });
  expect(guy.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Grenadier Guards",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);

  const logan = await publicPerson(request, profiles[43][0], profiles[43][1]);
  expect(logan).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
  });
  expect(logan.other_pre_oss_affiliations).toHaveLength(0);
});

test("same-name Robert C West rows remain separate cautious entities", async ({ request }) => {
  const left = await publicPerson(request, profiles[26][0], profiles[26][1]);
  const right = await publicPerson(request, profiles[27][0], profiles[27][1]);
  expect(left.person_id).not.toBe(right.person_id);
  expect(left.possible_duplicate_group).toBeTruthy();
  expect(right.possible_duplicate_group).toBe(left.possible_duplicate_group);
  expect(left.identity_status).toBe("unresolved");
  expect(right.identity_status).toBe("unresolved");
});

test("Batch 1008 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1008 public claims retain inspectable short citations", async ({ request }) => {
  const claimIndexes = [2, 3, 4, 7, 8, 10, 12, 14, 15, 23, 25, 30, 31, 32, 37, 40, 43] as const;
  for (const index of claimIndexes) {
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
