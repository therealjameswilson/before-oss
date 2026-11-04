import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page500-wheelock-to-white-review_batch-1010_2026-11-03.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["30d52660-ba6d-5472-84cb-67f1c3e03d39", "Harold J Wheelock"],
  ["d539201d-8bb1-5e19-bc0b-16cfb83b562f", "Mabel Wheelwright"],
  ["805f72e7-99de-5df2-a171-a633a6dcc912", "Alice B Whelan"],
  ["ca1fd474-2b92-5181-bf2f-b013e9f37005", "Donald C Whelan"],
  ["afa40be8-80c1-5593-84c5-f6116b6faecf", "Howard W Whelton"],
  ["fffef6a4-ac22-5320-92a2-6e45e2a59668", "Frederick C Whetzel"],
  ["f1c4fd89-0986-5272-a1a1-651d88b29b8c", "Joshua C Whetzel"],
  ["6d080093-475c-50a9-83bd-96e956d59932", "Theodore M Whicher"],
  ["424704d0-c8e5-57d0-a989-ad7cc52b19b9", "Glenn H Whidden"],
  ["275e103a-656b-5d8b-8074-7e2c56bdca9e", "Dorothy L Whiddon"],
  ["efe128a8-074a-53e5-8cae-430113065aec", "Dana de Peyst Whipple"],
  ["312f49a5-56aa-52aa-87dd-2acc1ceea334", "Dick W Whipple"],
  ["8c4d91c1-0db2-5f73-9543-3672da67eb0d", "Marcel J.A. Whipple"],
  ["5d7cb5c7-4c50-567d-81ec-0744224c3490", "Lafayette Whisonant"],
  ["771e2fbc-b680-5ec2-8bfd-34849dd84f70", "Margaret T Whiston"],
  ["e009fbc1-7482-5aee-b32e-50810b4c329c", "Arthur Whitaker"],
  ["b5a6c93e-da06-56cb-bb8f-20bafd8ece17", "Carl C Whitaker"],
  ["80a06373-a9d5-5f9c-962b-6ba65be60edc", "Charles W Whitaker"],
  ["6f1e41ea-425a-5e21-8820-c30e5c648951", "John T Whitaker"],
  ["7a11fc48-d8ca-518a-af10-415839f693a3", "Marioneth M Whitaker"],
  ["300017f2-ba9a-572a-99f4-3a30c9c7f3c3", "Mary R Whitaker"],
  ["4fb355af-35cb-5af3-9409-b9a6585c0f94", "Nelson B Whitaker"],
  ["70ff245a-55b6-56e7-9975-b40d648b5446", "Raymond Whitaker"],
  ["9eb24883-d0ec-5a5a-aede-3bf6d4f3f09f", "Roland I Whitcomb"],
  ["3eaf4835-68c4-5a01-80a2-0604fc277444", "Alan L White"],
  ["3cb69bce-c0f7-5875-957f-2073a126b894", "Alan Perine White"],
  ["61a3bcef-398d-5993-827c-35e7efe88fec", "Ann H White"],
  ["98a651da-6f35-5437-97eb-75e89aa5420c", "Barbara A White"],
  ["c80c31ba-8731-590f-af43-13c886a9cbbc", "Bennett S White Jr."],
  ["f1e46472-f590-55e0-9c91-9a4edd5701ef", "Bernard H White"],
  ["d584a3b8-75b0-5d05-974d-e62b501f8582", "Beverly C White"],
  ["609a3d78-3ddc-5ac9-b728-2cebcea7454d", "Carl C White"],
  ["1d2b3e94-cd7c-5657-870c-e36185c3e3f2", "Cecil T White"],
  ["d1d7e986-d9d8-5abb-a72c-ad5a45f9b6f6", "Constance White"],
  ["3093115b-ec20-559c-bdd5-545728e6c5c3", "David White"],
  ["fce11e2f-d497-5342-bfa0-efb62fdefc3a", "Dorothy White"],
  ["edcf0f73-3bde-53eb-b71f-a7b26f891e6e", "Edith L White"],
  ["31b5e2d6-2c47-5356-ad1a-9e74f5a20ea4", "Edwin A White"],
  ["f3a0ca54-291e-51b6-9960-41816b6c39dd", "Elizabeth E White"],
  ["4c82dc9e-9fb1-5d5d-b777-999bff271372", "Frances White"],
  ["7b36ce98-e2b7-5507-9896-89f6a02e9346", "Frank M White Jr."],
  ["713428d1-8293-5b31-9649-145819fbeded", "Frederic L.P. White"],
  ["6c066bb5-f2ad-5a1c-a5e6-85de659ea560", "George H White"],
  ["391268b1-7b26-5f7d-900d-bebc44b946ac", "H. Maxine White"],
  ["c65d926a-ef8c-5a5a-acbe-aaf8ef907023", "Hamilton S White"],
  ["143fb26e-764a-5d7f-8f4b-7ed3e1efbf3a", "Harold B White"],
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

test("Batch 1010 publishes all 46 reviewed people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("all 46 page 500 rows remain separately recoverable", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    sourceRows += person.source_records.filter(
      (row: { pdf_page: number }) => row.pdf_page === 500,
    ).length;
  }
  expect(sourceRows).toBe(46);
});

test("seven Army categories remain qualified and never invent employers", async ({ request }) => {
  const expected = new Map([
    [profiles[11][0], ["surveyor", "unknown"]],
    [profiles[12][0], ["skilled general woodworking worker, not elsewhere classified", "unknown"]],
    [profiles[16][0], ["carpenter", "unknown"]],
    [profiles[21][0], ["student", "student"]],
    [profiles[31][0], ["public official, not elsewhere classified", "unknown"]],
    [profiles[32][0], ["professional occupation, not elsewhere classified", "unknown"]],
    [profiles[45][0], ["loom fixer", "unknown"]],
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

test("Theodore Whicher separates Morningside student status from Coast Artillery service", async ({ request }) => {
  const person = await publicPerson(request, profiles[7][0], profiles[7][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Morningside College", relationship_type: "student" }),
      expect.objectContaining({ canonical_organization: "United States Army Coast Artillery Corps", relationship_type: "military_assignment" }),
    ]),
  );
});

test("John Whitaker keeps the last civilian employer separate from earlier newspapers", async ({ request }) => {
  const person = await publicPerson(request, profiles[18][0], profiles[18][1]);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Chicago Daily News", relationship_type: "employment", temporal_basis: "strongly_date_bounded" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Chattanooga News" }),
      expect.objectContaining({ canonical_organization: "New York Herald Tribune" }),
    ]),
  );
});

test("Alan Perine White keeps education and military service out of employer analytics", async ({ request }) => {
  const person = await publicPerson(request, profiles[25][0], profiles[25][1]);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Princeton University", relationship_type: "student" }),
      expect.objectContaining({ canonical_organization: "81st Infantry Division", relationship_type: "military_assignment", temporal_basis: "temporal_relation_uncertain" }),
    ]),
  );
});

test("Bennett White's University of Kentucky lead remains qualified and non-employment", async ({ request }) => {
  const person = await publicPerson(request, profiles[28][0], profiles[28][1]);
  expect(person.identity_status).toBe("probable");
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Kentucky",
      relationship_type: "professional_affiliation",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("George Hunter White gains a documented last civilian assignment without losing immediate-affiliation uncertainty", async ({ request }) => {
  const person = await publicPerson(request, profiles[42][0], profiles[42][1]);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Federal Bureau of Narcotics", temporal_basis: "probable_immediate" }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Federal Bureau of Narcotics", relationship_type: "government_assignment" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "United States Border Patrol" }),
      expect.objectContaining({ relationship_type: "self_employment", occupation: "private investigator" }),
    ]),
  );
});

test("Charles Whitaker's protected-identifier collision remains explicit", async ({ request }) => {
  const person = await publicPerson(request, profiles[17][0], profiles[17][1]);
  const namesake = await publicPerson(
    request,
    "227bcffa-5ff0-5f4d-99a3-e8ab46383f9a",
    "Charles W Whittaker",
  );
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(person.possible_duplicate_group).toMatch(/^duplicate-[0-9a-f]{12}$/);
  expect(namesake.possible_duplicate_group).toBe(person.possible_duplicate_group);
  expect(JSON.stringify([person, namesake])).not.toContain("42030227");
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims.some((claim: { claim_confidence: string }) => claim.claim_confidence === "conflicting")).toBe(true);
});

test("Batch 1010 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1010 public claims retain inspectable short citations", async ({ request }) => {
  const claimIndexes = [7, 11, 12, 16, 17, 18, 21, 25, 28, 31, 32, 42, 45] as const;
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
