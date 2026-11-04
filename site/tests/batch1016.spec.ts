import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page506-lansing-williams-to-lawrence-j-willinger-review_batch-1016_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["9c00e055-1c02-5eda-967c-3732586a8a87", "Lansing Williams"],
  ["ab0d962e-4482-543b-bd0d-f00c08786a12", "Lauri A Williams"],
  ["868ac8d2-4681-5cfc-b8d5-f3a1eea717e7", "Layton R Williams"],
  ["d95e19f3-f8d8-5c16-99af-b3d01c359a66", "Malcolm J Williams"],
  ["54eea12e-cef2-5b4e-ad4b-a22ee0504a8d", "Margaret C Williams"],
  ["f23a2cd6-373a-51b5-8eed-0cf13f6f18a7", "Mary C Williams"],
  ["9ad42d6a-3d3b-5b73-a070-49ffc5286952", "Mary E Williams"],
  ["552f2500-37cb-560c-bbef-c02888ef8d45", "Melvin Williams"],
  ["bcdd1801-9e44-5309-9092-6a00c948fff9", "Milton D Williams"],
  ["4bec75e2-b1c0-5e76-bcb8-5cb595f1da81", "Morris S Williams"],
  ["3c3fccfc-f30f-5927-b2e9-886bceb5b1a4", "Nathaniel Williams"],
  ["704c9bb8-e7d6-5d8e-b9fe-024055783508", "Norman Williams"],
  ["9fbc584e-e6a7-5708-9e8d-8cea1401cc9a", "Oscar C Williams"],
  ["c13d658f-31cb-5212-816e-d7f4ce551675", "Payne Williams II"],
  ["40209512-a9e1-5c12-bbd1-579ddb6b221b", "Peter W Williams"],
  ["46c59f1d-3db7-5691-af89-81306e245ca0", "Randolph A Williams"],
  ["ab653302-9bef-56bc-b3d2-a5a27973c224", "Robert G Williams"],
  ["2df9a0b5-f465-5c87-a6d1-67ff06724783", "Robert L Williams"],
  ["c00580fa-3ff9-59a3-8129-6076523c2c53", "Roy L Williams"],
  ["917e5bcb-35c7-55d6-bfbf-d28518c6ae6c", "Roy N Williams Jr."],
  ["5c5c1754-5cb9-540c-8fbc-5c1b856076e1", "Violet R Williams"],
  ["f10b2a0f-a1a6-562d-bf30-90ee9126bb63", "Walker F Williams"],
  ["7c2800ca-c8d3-5c70-8fb5-8195119f381a", "William O Williams"],
  ["b1f21268-2fc0-5310-ac57-e14e17668182", "William Williams"],
  ["8b4b90bb-2a25-5a34-9913-721ff076a07d", "William A Williams"],
  ["1160b5a5-704f-53b8-9e14-2d215b324998", "William B Williams"],
  ["2dbd2cd4-f1f5-5ff3-83fe-2827933c577d", "William C Williams"],
  ["5a53e687-e1e9-50b3-9ab1-a7508a84d0ff", "William E Williams Jr."],
  ["0729999c-f1e1-54d7-b52f-e8639740c653", "Wyman Williams"],
  ["c94d0247-bd4d-5fcf-80f7-9280b94a7c62", "Barbara A Williamson"],
  ["fda8c002-7cd2-5aca-a8e2-97f0101ba96a", "Benjamin E Williamson"],
  ["31120da9-ecca-53d8-8853-76af0acf0588", "David Williamson"],
  ["484cc607-e764-596f-95b0-2b4ec476c1ef", "Elizabeth C Williamson"],
  ["a7611fff-cc66-5b19-9764-3189a7a192a7", "Emmy Lou Williamson"],
  ["bf2193a9-c716-5245-9168-e0cc9647d6dc", "Florence Williamson"],
  ["32cb5ae6-a2e8-5d14-afbe-569ce8538033", "Francis T Williamson"],
  ["82a8bc6b-a73c-5371-9ac8-0722b0407d98", "Jayo Williamson"],
  ["0ae3193f-ee6c-5284-9b6b-41a6d88adff3", "Lyman O Williamson"],
  ["17e644f0-841f-5ef5-bbe3-c7045b5ae8cb", "Margaret W Williamson"],
  ["85775a46-c409-5b9c-b184-c961815bd292", "Mary F Williamson"],
  ["db029202-c913-5084-9858-7ffa277f265f", "Zetha Williamson"],
  ["57845e9a-5fa4-56c0-b634-adcaa992d19b", "Buck M Williford"],
  ["b1d5cd65-0bf2-506a-83d6-c93cca2a9dc0", "Colleen G Williford"],
  ["ccb6a192-6bbd-551c-a113-ee964f028c39", "Edna E Williford"],
  ["7d303a23-1a5e-550e-886d-f81a22d372d8", "Robert H Williford"],
  ["d1576e97-4d34-575b-a909-1d9f69060c65", "Lawrence J Willinger"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find(
    (item: { person_id: string }) => item.person_id === id,
  );
}

test("Batch 1016 publishes all 46 reviewed profiles and preserves page 506 rows", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    expect(person, name).toBeTruthy();
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
    sourceRows += person.source_records.filter(
      (row: { pdf_page: number }) => row.pdf_page === 506,
    ).length;
    expect(JSON.stringify(person)).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
  }
  expect(sourceRows).toBe(46);
});

test("six Army categories remain qualified and never become employers", async ({ request }) => {
  const expected = new Map([
    [profiles[9][0], "apprentice to another trade"],
    [profiles[13][0], "student"],
    [profiles[21][0], "stenographer or typist"],
    [profiles[25][0], "photoengraver"],
    [profiles[30][0], "skilled mechanic or repairman"],
    [profiles[44][0], "semiskilled construction occupation"],
  ]);
  for (const [id, label] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(JSON.stringify(person.other_pre_oss_affiliations)).toContain(label);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: null,
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
  }
});

test("David Williamson keeps the Foreign Service as probable immediate government service", async ({ request, page }) => {
  const person = await publicPerson(request, profiles[31][0], profiles[31][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of State",
      role_title: "Foreign Service Officer, class V",
      relationship_type: "government_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto(`./people/${profiles[31][0]}/`);
  await expect(page.getByRole("heading", { name: "David Williamson", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Department of State");
  await expect(page.locator("main")).toContainText("Probable immediate");
});

test("Jayo Williamson is a qualified Ball State student, not an employee", async ({ request, page }) => {
  const person = await publicPerson(request, profiles[36][0], profiles[36][1]);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Ball State Teachers College",
      role_title: "assistant copy editor, The Easterner",
      relationship_type: "student",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  await page.goto(`./people/${profiles[36][0]}/`);
  await expect(page.getByRole("heading", { name: "Jayo Williamson", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Ball State Teachers College");
});

test("post-OSS and undefined Army rows confirm identity only", async ({ request }) => {
  for (const index of [8, 14] as const) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Norman Williams conflict transfers no Army data", async ({ request }) => {
  const person = await publicPerson(request, profiles[11][0], profiles[11][1]);
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
      publication_status: "conflicting",
    }),
  ]);
});

test("Batch 1016 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1016 claims retain inspectable short citations", async ({ request }) => {
  const indexes = [8, 9, 11, 13, 14, 21, 25, 30, 31, 36, 44] as const;
  for (const index of indexes) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person.claims.length).toBeGreaterThan(0);
    for (const claim of person.claims) {
      expect(claim.sources.length).toBeGreaterThan(0);
      for (const link of claim.sources) {
        expect(link.source.stable_url || link.source.archival_identifier).toBeTruthy();
        const excerpt = link.excerpt_override ?? claim.evidence_excerpt ?? "";
        expect(excerpt.trim() ? excerpt.trim().split(/\s+/).length : 0).toBeLessThanOrEqual(25);
      }
    }
  }
});

test("Batch 1016 coverage totals are public", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23935,
    research_attempted_people: 16661,
    verified_affiliation_people: 1176,
    verified_employer_people: 538,
    archival_review_assessed_people: 15140,
  });
});
