import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page505-asa-e-williams-to-june-williams-review_batch-1015_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["bdba50c5-59f7-5c45-a904-e65dd6e17b07", "Asa E Williams"],
  ["d8f56989-c60b-51d7-80a1-c8bd2a0566bc", "Barbara A Williams"],
  ["4ac09478-6b60-5974-a844-8751fd36a6f3", "Charles H Williams"],
  ["1422bbac-edac-5309-ae0d-8570a8eeab38", "Charles L.L. Williams"],
  ["c59f4cc0-b134-5742-9788-5d45d971c868", "Charles S Williams"],
  ["3533a80c-b5f8-53d7-935c-203c5fef544c", "Charles W Williams"],
  ["ecb1c016-bd61-5fa4-b1c4-a62db863a7a1", "Clarence D Williams"],
  ["7552eb7c-1dc3-5abd-a038-f79e160db03e", "Clyde L Williams"],
  ["0e50678d-f6ec-5c0d-bef4-3d2cafda7dc4", "Clyde O Williams"],
  ["c59ad468-4ba8-51b3-b162-57ca140e008d", "Corinne T Williams"],
  ["760bed35-b9f5-5cd7-afd0-45ca2f3ef473", "Dudley W Williams"],
  ["4c052102-d332-5d36-9bff-186d60b57917", "Dwight C Williams"],
  ["44d83f03-995a-5ecb-9b0a-fd7d6736c0d7", "E. Fay Williams"],
  ["131ccfe5-82aa-559c-9f9c-4a35df0f36f9", "Earl L Williams"],
  ["facafc12-4e42-5947-a29f-81623241009b", "Edith B Williams"],
  ["0ccc15c8-0f13-5d66-b45c-872ec8eb5991", "Edward J Williams"],
  ["13dfaf37-e124-5ee4-9ab8-604d2201a4b1", "Edwin A Williams"],
  ["a94f917b-d897-56bb-9610-b648aabeb3cc", "Eric J Williams"],
  ["408ef0ee-24f9-5bb1-b938-ace14123bd33", "Eric Williams"],
  ["9dc0d436-428c-5df8-9b7a-2acd4d8594d6", "Ernestine O Williams"],
  ["bdcb1945-38dd-5d6a-9cd6-fbb32da1d4f6", "Evelyn M Williams"],
  ["a332579e-12a8-5f81-bc6a-035a1dfc8db0", "Franklin R Williams"],
  ["44b8750a-ffbf-5aeb-9327-4d4740c456fc", "Fred R Williams"],
  ["015e318b-8dc6-536c-a271-bc1d0a52de11", "Frederick Williams"],
  ["f5311b42-cde7-55de-97d2-4528e23ea1d3", "Garland H Williams"],
  ["6549ef85-0fc0-5493-8db9-5f1ac0f6d4a0", "George C Williams"],
  ["449bdf3b-2834-552e-a5c5-89cb90aa8238", "George W Williams"],
  ["577d27da-d414-5cf4-8ab9-936cd2bc443c", "Guy R Williams"],
  ["a63100b2-fe31-5c4e-85db-7feaf5b853bf", "Harold A Williams"],
  ["05746991-eb18-528a-8127-d1728b9a6023", "Harold D Williams"],
  ["6463028d-6a8e-5db7-aed6-26e00518c69d", "Harold P Williams"],
  ["703bcddd-da0a-5194-9467-c6a01653f783", "Harold W Williams"],
  ["f61f6888-b097-5935-95fd-093650630049", "Helen M Williams"],
  ["c8cc718d-e9b8-5245-8f4d-443f757f7127", "Herbert H Williams"],
  ["8939b9f8-5a77-52c6-a667-e9ca3c99accf", "Herbert J Williams"],
  ["167ec58c-8ae1-54fa-8374-f6d69ec50094", "Houston Hiatt Williams"],
  ["2fedeed8-effe-5ddf-af4f-5ed739446f5c", "Ian Wythe Williams"],
  ["0616d9ef-3866-5674-b6ca-c148f55ed084", "Irene Ellen Williams"],
  ["6c4d0fdc-1316-5233-8af6-b80c72be1f80", "Jack R Williams"],
  ["e21ffbf4-7f4b-5e67-9664-e17fa7d82920", "Jacklyn Williams"],
  ["2900d56d-8aff-5b2b-9d02-cf172a45389e", "James C Williams"],
  ["ca25aa31-3a3b-5f03-b6c7-303dcf4c2e5d", "James J Williams"],
  ["948c0add-14e9-5195-9374-d0f3609fad10", "Jeannette R Williams"],
  ["6b138798-7790-594e-84b5-f7de0f58eee5", "John Williams"],
  ["85f05a48-9e95-501a-9273-3b405d7e6ac3", "John W Williams"],
  ["f4e20212-f1f7-5e09-be06-9f8ee873d387", "June Williams"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const shard = name[0].toLowerCase();
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find(
    (item: { person_id: string }) => item.person_id === id,
  );
}

test("Batch 1015 publishes all 46 terminal profiles and preserves page 505 rows", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    expect(person, name).toBeTruthy();
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
    sourceRows += person.source_records.filter(
      (row: { pdf_page: number }) => row.pdf_page === 505,
    ).length;
    expect(JSON.stringify(person)).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
  }
  expect(sourceRows).toBe(46);
});

test("ten Army categories remain qualified occupations or student statuses", async ({ request }) => {
  const expected = new Map([
    [profiles[2][0], "student"],
    [profiles[5][0], "textile-product fabrication"],
    [profiles[6][0], "student"],
    [profiles[7][0], "welder or flame cutter"],
    [profiles[8][0], "carpenter"],
    [profiles[13][0], "architect"],
    [profiles[25][0], "clerk in trade"],
    [profiles[26][0], "pressman or plate printer"],
    [profiles[27][0], "hotel or restaurant manager"],
    [profiles[38][0], "chauffeur or bus, taxi, truck, or tractor driver"],
  ]);
  for (const [id, label] of expected) {
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
    expect(JSON.stringify(person.other_pre_oss_affiliations)).toContain(label);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: null,
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    });
  }
});

test("Eric Williams publishes Howard evidence without claiming immediacy", async ({ request, page }) => {
  const person = await publicPerson(request, profiles[18][0], profiles[18][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Howard University",
      role_title: "Assistant Professor of Political and Social Science",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
  await page.goto(`./people/${profiles[18][0]}/`);
  await expect(page.getByRole("heading", { name: "Eric Williams", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Howard University");
});

test("Ian Wythe Williams keeps NBC and Embassy roles separate and non-immediate", async ({ request, page }) => {
  const person = await publicPerson(request, profiles[36][0], profiles[36][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations.map(
    (item: { canonical_organization: string }) => item.canonical_organization,
  )).toEqual(expect.arrayContaining([
    "National Broadcasting Company",
    "United States Embassy in Paris",
  ]));
  await page.goto(`./people/${profiles[36][0]}/`);
  await expect(page.getByRole("heading", { name: "Ian Wythe Williams", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("National Broadcasting Company");
  await expect(page.locator("main")).toContainText("United States Embassy in Paris");
});

test("uninterpreted and conflicting Army records transfer no occupation", async ({ request }) => {
  const unknownCode = await publicPerson(request, profiles[30][0], profiles[30][1]);
  expect(unknownCode).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    research_status: "requires_archival_review",
  });
  expect(unknownCode.other_pre_oss_affiliations).toHaveLength(0);

  const conflict = await publicPerson(request, profiles[29][0], profiles[29][1]);
  expect(conflict).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(conflict.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(conflict.last_civilian_pre_service).toHaveLength(0);
  expect(conflict.other_pre_oss_affiliations).toHaveLength(0);
  expect(conflict.claims).toEqual([
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  ]);
});

test("Garland Williams remains a qualified identity lead, not an employer claim", async ({ request }) => {
  const person = await publicPerson(request, profiles[24][0], profiles[24][1]);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("Batch 1015 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1015 claims retain inspectable short citations", async ({ request }) => {
  const indexes = [2, 5, 6, 7, 8, 13, 18, 24, 25, 26, 27, 29, 30, 36, 38] as const;
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

test("Batch 1015 coverage totals are public", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23935,
    research_attempted_people: 16617,
    verified_affiliation_people: 1175,
    verified_employer_people: 538,
    archival_review_assessed_people: 15094,
  });
});
