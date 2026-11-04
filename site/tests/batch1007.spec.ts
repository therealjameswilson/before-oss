import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page497-wells-to-werner-review_batch-1007_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["7660dc05-b932-5947-8a11-bd697c70fdb1", "Dorson S Wells"],
  ["666ce936-2052-5880-b3ae-6df492bbfe7c", "Edward O Wells"],
  ["198c0f14-b3bc-5e5a-9d52-9503cef85ef7", "Frances J Wells"],
  ["fbe6bb8d-88c5-59b7-84ec-da59a00725d5", "George K Wells Jr."],
  ["d0c82f62-3687-5630-aa68-08193eb7274d", "John W Wells"],
  ["f2e7ae70-cdd8-5aa6-bae4-24a99269358d", "Kenneth E Wells"],
  ["b8ded288-581c-5deb-8de8-c14e6e6d2ed3", "Lydia F Wells"],
  ["b89754a9-ed43-53ef-94c7-5c00b8a957de", "Lyman C Wells"],
  ["c3e5d490-25f2-52af-8dba-3a6744bd3e4c", "Marion O Wells"],
  ["c06be51c-8294-5d38-90a0-c321153fb607", "Ralph J Wells"],
  ["8b6b5d22-c121-58d5-bcb4-f317b3c88152", "Richard S Wells"],
  ["5e06c406-a711-5604-8aa9-eb36eb919c8d", "Robert J Wells"],
  ["98e8f4ad-841a-54b3-9d00-b2eddfcd3bd5", "Staring Wells"],
  ["7659df98-b645-504b-a2f8-cf32fcd507f3", "Warren R Wells"],
  ["9f6be017-c897-5886-84f7-ee7531110081", "Winifred G Wells"],
  ["3373c334-5112-519f-9cd5-da94b1e2537e", "Vivian Wellwood"],
  ["9e224a36-2f9d-552d-8844-e1b6aa782205", "Jerome H Welo"],
  ["99d9d8a5-9f99-50b7-bc4a-fd3b31d1b3ad", "Eva B Wels"],
  ["45dc201b-9b7c-5f57-82df-23bb7cc2dacd", "Paul J Welsh"],
  ["1558bf32-3a55-5c16-b9a6-cf22fa86183a", "Luida Wendell"],
  ["65d263fe-859d-5e0a-9cf5-fb398582510c", "Saly Wengel"],
  ["87a69f19-f285-558a-bc27-9c155a08a89b", "Irving Wenger"],
  ["c6b9e65d-b194-57ee-9ee2-32313dd628c2", "John H Wennberg"],
  ["4b69a7f5-b17b-5ed8-92f7-95af6a06e777", "Carl G Wenner"],
  ["1ff415e5-57da-50e7-8af1-e6fb6bbb52e9", "Luther J.G. Wenner"],
  ["35310cb1-996d-5dbd-92c2-09d33e4ad6bc", "Robert K Wensley"],
  ["9db7a686-99df-58d6-855a-b07dff245bdf", "George Wentler"],
  ["82c94e31-3810-5a88-8723-86fe24f3cf6a", "Dorothy E Wentworth"],
  ["96cfe5ac-0557-5a09-b35f-0cb206603f38", "Nathan H Wentworth"],
  ["1650d9e8-4f2d-5f5c-802f-1e4189fd5a94", "Paul T Wentworth"],
  ["d3ea8fb7-808e-5b83-8c05-9098f6244f2a", "Robert J Wentworth"],
  ["ae4af2b2-505b-5913-afd3-9161ba7d93a3", "Robert J Wentworth"],
  ["0f6a0e59-a521-5f32-8902-8dadd70e872f", "Russell A Wentworth"],
  ["f0aed3c5-2440-5e45-b8ec-38d607586214", "Donald B Wentzel"],
  ["58e485fe-9fcd-5b1c-b229-be0b27d10570", "Francis G Wenzel"],
  ["2a3e9061-b725-5382-8361-57923cbb4ae8", "Peter Wenzel"],
  ["2627680a-afa9-509d-9332-a0f2fa29213c", "Charlotte L Wepf"],
  ["86661c77-6a2f-59b8-9a2e-ce1b3797d9e8", "Mitchell L Wer-Bell"],
  ["8289cc71-1234-5008-936d-c0fcc9565a41", "Wilford J Werber"],
  ["935fbe7a-3882-5ad8-972f-da066a935ea9", "Leon I Werbin"],
  ["a3400fd4-a057-5ebf-84d6-f0d217e4aab6", "Wallace Werble Sr."],
  ["727ff070-594f-562a-820b-2f288f921782", "Thomas F Werkich"],
  ["44094644-6fc0-5896-8ddd-1436b103b431", "Frank W Werley"],
  ["1aa11e0f-bcaa-589e-85ea-6ee3d9a08143", "Daniel S Werner"],
  ["7dba3b2a-5e3f-53b9-a387-cfe55fef0581", "Louis B Werner"],
  ["3ae20377-34d3-5050-8225-bb4b217b5087", "Louis Werner Jr."],
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

test("Batch 1007 publishes all 46 reviewed people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("all 46 page 497 source rows remain separately recoverable", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    sourceRows += person.source_records.filter(
      (row: { pdf_page: number }) => row.pdf_page === 497,
    ).length;
  }
  expect(sourceRows).toBe(46);
});

test("nine Army categories remain qualified and never invent employers", async ({ request }) => {
  const expected = new Map([
    [profiles[8][0], ["telegraph, telephone, or power lineman or serviceman", "unknown"]],
    [profiles[10][0], ["financial institution clerk", "unknown"]],
    [profiles[21][0], ["student", "student"]],
    [profiles[22][0], ["mechanic or repairman, not elsewhere classified", "unknown"]],
    [profiles[23][0], ["secondary-school teacher or principal", "unknown"]],
    [profiles[39][0], ["commercial artist", "unknown"]],
    [profiles[40][0], ["author, editor, or reporter", "unknown"]],
    [profiles[41][0], ["worker in manufacture of miscellaneous finished lumber products", "unknown"]],
    [profiles[42][0], ["chauffeur or driver", "unknown"]],
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

test("damaged code 990 and undefined code 999 remain identity evidence only", async ({ request }) => {
  for (const index of [24, 38] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("John W Wells keeps the Ohio State lead visibly qualified", async ({ request }) => {
  const person = await publicPerson(request, profiles[4][0], profiles[4][1]);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
  });
  for (const affiliation of [
    ...person.immediate_pre_oss_affiliations,
    ...person.last_civilian_pre_service,
  ]) {
    expect(affiliation).toMatchObject({
      canonical_organization: "The Ohio State University",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
  }
});

test("Mitchell WerBell separates Army, last civilian employer, earlier work, and study", async ({ request }) => {
  const person = await publicPerson(request, profiles[37][0], profiles[37][1]);
  expect(person).toMatchObject({
    display_name: "Mitchell L Wer-Bell",
    identity_status: "confirmed",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Palmer Radar Development Laboratories",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "L'Artisan", relationship_type: "employment" }),
      expect.objectContaining({ canonical_organization: "Strawbridge & Clothier", role_title: "Assistant advertising manager" }),
      expect.objectContaining({ canonical_organization: "Charles Morris Price School", relationship_type: "student" }),
    ]),
  );
});

test("same-name Robert J Wentworth rows remain separate cautious entities", async ({ request }) => {
  const left = await publicPerson(request, profiles[30][0], profiles[30][1]);
  const right = await publicPerson(request, profiles[31][0], profiles[31][1]);
  expect(left.person_id).not.toBe(right.person_id);
  expect(left.possible_duplicate_group).toBeTruthy();
  expect(right.possible_duplicate_group).toBe(left.possible_duplicate_group);
  expect(left.identity_status).toBe("unresolved");
  expect(right.identity_status).toBe("unresolved");
});

test("printed Coast Guard and commissioned categories remain distinct", async ({ request }) => {
  const coastGuard = await publicPerson(request, profiles[7][0], profiles[7][1]);
  expect(coastGuard).toMatchObject({
    personnel_category: "enlisted_coast_guard_personnel",
    commissioned_officer: false,
  });
  for (const index of [43, 45] as const) {
    const captain = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(captain).toMatchObject({
      personnel_category: "commissioned_army_officer",
      commissioned_officer: true,
    });
  }
});

test("Batch 1007 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1007 public claims retain inspectable short citations", async ({ request }) => {
  const claimIndexes = [4, 8, 10, 21, 22, 23, 37, 39, 40, 41, 42] as const;
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
