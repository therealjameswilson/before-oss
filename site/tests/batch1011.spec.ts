import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page501-white-to-whiting-review_batch-1011_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["3525eb07-a84a-5dff-b90d-01a311ecb63f", "Herbert W White"],
  ["3ea7fcb7-5185-5876-b901-cdf71d2c2e88", "Homer White"],
  ["fcf18f90-07bf-573c-9689-a08757e3a84d", "Howard W White"],
  ["3318f77a-9866-51a8-b13a-8032de39a57e", "Jack R White"],
  ["4bf7eb46-7304-5098-92bf-bd85bad63f24", "James White"],
  ["7c6232d6-f7e7-5eac-a80e-70f21a5d22ac", "John A White"],
  ["0e6db06c-e670-5dea-b770-014662862d7c", "John A White"],
  ["57dcc69b-6532-5502-8540-b059412f0998", "John M White"],
  ["b34ee7e1-bcd2-5605-8582-8828aae099bc", "John J White Jr."],
  ["fe64422e-0fcb-5696-8784-3b83423585ae", "Joseph P White"],
  ["0ab334e0-2ef1-5280-9ac8-4acf4272c4f6", "Leland F White"],
  ["a2a82b6d-c71d-5262-88f2-e021ade9579b", "Leslie W White"],
  ["563d47d6-1346-51fe-830e-bd45342ac099", "Lorraine H White"],
  ["ad69e01e-ca14-5fa0-874e-3c8d965d4412", "Martha N White"],
  ["b93ba4f7-9c67-5b04-8a72-4aa7678daeea", "Mary R White"],
  ["dea3f15c-b499-5d44-95c5-4ce1ba2a7f2c", "Max G White"],
  ["a802a3d5-b4f0-515c-807b-c1321908acde", "Michael White"],
  ["0b8e25a7-f668-5c9d-b297-3ed67ad04672", "Nancy M White"],
  ["a5ba7337-917f-502b-bb35-9ee1b643df7f", "Norman White"],
  ["9b4a71ba-9c4e-568f-87c8-f71b38f4f586", "Owen V White"],
  ["52983af1-53bf-534a-9428-63734e5c7539", "Paul R White"],
  ["93bafa90-db19-5c80-8887-feb69e5a934a", "Peregrine White"],
  ["6d82d2ad-f28d-5a3d-bd8f-eb259e1f3ae4", "Peter L White"],
  ["6e67cef4-552e-5444-a754-6105bcb15b4d", "Robert C White"],
  ["52e86f91-5c11-5b7b-bf4a-f5c0f5d7f31c", "Robert G White"],
  ["fc48e936-b465-5542-ab81-685726093cb8", "Robert L White"],
  ["b929db63-545d-5e0e-8a59-12ad8dbcdb3c", "Robert W White"],
  ["2d048789-5b93-5b7a-a3ec-54284adc77e0", "Samuel W White"],
  ["7c787dfa-843e-5451-b467-94d67a14761d", "Shirley White"],
  ["decc2631-c26c-5f5f-a348-ffc12adcc500", "Stanley W White"],
  ["18f47ba1-a677-50f8-94c5-256996182fb3", "Thomas I White"],
  ["9c813e54-093e-524d-9c3a-201a92260e1f", "Thomas J White"],
  ["7d7ec80d-38f5-5454-9212-68599845d9c2", "Wallace B White"],
  ["33aa1fae-efe1-5404-add5-9c28ce490308", "Wilbur C White"],
  ["3c8dfb1e-5f3e-5583-b79f-c423098b8623", "William H White"],
  ["2ab6019b-67fc-5f44-8bc0-888e3d7b439f", "Woodrow W White"],
  ["77207402-d731-50e6-9f67-84aca4567993", "Ralph E Whitecotton"],
  ["8ec54696-4d52-56ef-a1a1-10cb2ebabfd8", "Calvin L Whitehead"],
  ["03eedea4-2f79-53b2-a602-d423dd1243fc", "Charles S Whitehurst"],
  ["57a28eaa-83a3-5c9a-b47e-417146dd7a88", "Fred Whiteing"],
  ["cbd64f27-edec-52f1-b951-676529b0acbe", "Jordan M Whitelaw"],
  ["dffaf32d-50b5-5d9c-90ae-a45f2afc8ce1", "Margery D Whiteley"],
  ["f11c7309-144f-5b7f-81cf-6732191b16ef", "Susan Whiteley"],
  ["2c473d3c-d237-5ad8-adc2-62762035d862", "William A Whitfield"],
  ["acf4c311-f630-53f5-a47a-9a1ffc2661bf", "Ben L Whiting"],
  ["cc976e10-09c9-5f5e-8a31-52eea980cf45", "Herbert Whiting"],
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

test("Batch 1011 publishes all 46 reviewed people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("all 46 page 501 rows remain separately recoverable", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    sourceRows += person.source_records.filter(
      (row: { pdf_page: number }) => row.pdf_page === 501,
    ).length;
  }
  expect(sourceRows).toBe(46);
});

test("thirteen Army categories remain qualified and never invent employers", async ({ request }) => {
  const expected = new Map([
    [profiles[4][0], "semiskilled brick and stone mason or tile setter"],
    [profiles[5][0], "actor"],
    [profiles[6][0], "boarding-house or lodging-house keeper"],
    [profiles[11][0], "bookkeeping-machine operator"],
    [profiles[18][0], "skilled pattern or model maker, except paper"],
    [profiles[19][0], "cook, except private family"],
    [profiles[22][0], "student"],
    [profiles[23][0], "credit man"],
    [profiles[27][0], "draftsman"],
    [profiles[29][0], "stenographer or typist"],
    [profiles[31][0], "general farm hand"],
    [profiles[32][0], "author, editor, or reporter"],
    [profiles[33][0], "chemical engineer"],
  ]);
  for (const [id, occupation] of expected) {
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
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("the two John A White identities remain distinct", async ({ request }) => {
  const sergeant = await publicPerson(request, profiles[5][0], profiles[5][1]);
  const jedburgh = await publicPerson(request, profiles[6][0], profiles[6][1]);
  expect(sergeant.person_id).not.toBe(jedburgh.person_id);
  expect(sergeant.source_records[0].rank_as_indexed).toBe("1/Sgt.");
  expect(sergeant.other_pre_oss_affiliations[0].occupation).toBe("actor");
  expect(jedburgh.source_records[0].rank_as_indexed).toBeNull();
  expect(jedburgh.other_pre_oss_affiliations[0].occupation).toBe(
    "boarding-house or lodging-house keeper",
  );
  expect(JSON.stringify(jedburgh.claims)).toContain("Jedburgh");
});

test("Jordan Whitelaw keeps student and production-committee affiliations out of employment", async ({ request }) => {
  const person = await publicPerson(request, profiles[40][0], profiles[40][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "completed",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "Phillips Academy",
        relationship_type: "student",
      }),
      expect.objectContaining({
        canonical_organization: "Lowell House Musical Society",
        relationship_type: "professional_affiliation",
      }),
    ]),
  );
});

test("unresolved and post-OSS leads remain withheld", async ({ request }) => {
  const homer = await publicPerson(request, profiles[1][0], profiles[1][1]);
  expect(homer).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(JSON.stringify(homer.claims)).not.toContain("Operation Medusa");

  const ralph = await publicPerson(request, profiles[36][0], profiles[36][1]);
  expect(ralph).toMatchObject({
    identity_status: "confirmed",
    research_status: "requires_archival_review",
  });
  expect(ralph.other_pre_oss_affiliations).toHaveLength(0);
  expect(JSON.stringify(ralph.claims)).toContain("after OSS dissolution");
});

test("Batch 1011 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1011 public claims retain inspectable short citations", async ({ request }) => {
  const claimIndexes = [4, 5, 6, 9, 11, 18, 19, 22, 23, 27, 29, 31, 32, 33, 36, 40] as const;
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
