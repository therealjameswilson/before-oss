import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const profiles = {
  emmettMcNamara: ["6422367f-34a3-5c72-9130-5af24fd15e02", "Emmett F McNamara"],
  jamesMcLuskey: ["f69ec40e-d619-5c5d-bb6e-ec35e0240443", "James A McLuskey"],
  johnMcLaughlin: ["c3e47113-2f34-5958-8f4f-2915a2e0ee16", "John J McLaughlin"],
  cyrilMcLeod: ["bb31e319-1344-5907-9f92-f6b72ab50caf", "Cyril McLeod"],
  robertMcManamy: ["0f222fe3-db20-59bf-b347-07392f886149", "Robert C McManamy"],
  walterMcMillan: ["6f81d270-10fe-5cb4-ae38-304d848a6699", "Walter F McMillan"],
  williamMcMahon: ["8453c16a-1c36-5cbc-8433-8f30fd990e50", "William J McMahon"],
  georgeMcNally: ["19d26b79-9ae5-5b19-b43d-83cd71a0d7ab", "George E McNally"],
  lawrenceMcNally: ["228becf6-8f84-5dc3-97bb-25ebc221d819", "Lawerence D McNally"],
  georgeMcNamara: ["1c956fdc-ddf9-5d13-b528-23c32fb51fea", "George T McNamara"],
} as const;

async function publicPerson(
  request: APIRequestContext,
  [id, name]: readonly [string, string],
) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find(
    (item: { person_id: string }) => item.person_id === id,
  );
}

test("Batch 1057 publishes all 46 page-312 rows as 45 terminal profiles", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(
      ...(await response.json()).filter(
        (person: { source_records: { pdf_page: number }[] }) =>
          person.source_records.some((row) => row.pdf_page === 312),
      ),
    );
  }
  expect(people).toHaveLength(45);
  expect(
    people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.filter((row) => row.pdf_page === 312),
    ),
  ).toHaveLength(46);
  for (const person of people) {
    expect(["not_started", "in_progress", "candidate_found"]).not.toContain(
      person.research_status,
    );
  }
});

test("Emmett McNamara publishes an explicit Signal Corps-to-OSS transition without inventing an employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.emmettMcNamara);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Signal Corps",
      organization_name_as_found: "Army's Signal Corps school at Fort Monmouth",
      occupation: "radio operator",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
      immediate_pre_oss: true,
      last_civilian_pre_service: false,
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "retail manager",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.emmettMcNamara[0]}/`);
  await expect(page.locator("main")).toContainText("United States Army Signal Corps");
  await expect(page.locator("main")).toContainText("explicit immediate");
  await expect(page.locator("main")).toContainText("retail manager");
});

test("James McLuskey's post-OSS Army entry is identity evidence only", async ({ request }) => {
  const person = await publicPerson(request, profiles.jamesMcLuskey);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims.length).toBeGreaterThanOrEqual(1);
  expect(person.claims.every((claim: { claim_type: string }) => claim.claim_type === "identity")).toBeTruthy();
  expect(
    person.claims.some((claim: { temporal_assessment: string }) =>
      claim.temporal_assessment.includes("1946"),
    ),
  ).toBeTruthy();
});

test("Page-312 duplicate, parser-warning, and military-record conflicts remain visible", async ({ request }) => {
  const john = await publicPerson(request, profiles.johnMcLaughlin);
  expect(john.source_records).toHaveLength(2);
  expect(john.possible_duplicate_group).toBeTruthy();
  expect(john.identity_status).toBe("high_confidence");

  const cyril = await publicPerson(request, profiles.cyrilMcLeod);
  expect(cyril).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(cyril.identity_evidence).toContain("middle-initial column");
  expect(cyril.source_records[0].rank_as_indexed).toBeNull();

  const robert = await publicPerson(request, profiles.robertMcManamy);
  expect(robert).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(robert.other_pre_oss_affiliations).toHaveLength(0);

  const walter = await publicPerson(request, profiles.walterMcMillan);
  expect(walter).toMatchObject({
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
  });
  expect(walter.other_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 1057 Army-entry occupations remain qualified and organization-free", async ({ request }) => {
  for (const [profile, occupation] of [
    [profiles.williamMcMahon, "policeman or detective in public service"],
    [profiles.georgeMcNally, "student"],
    [profiles.lawrenceMcNally, "midwife or practical nurse"],
    [profiles.georgeMcNamara, "housekeeper, steward, or hostess"],
  ] as const) {
    const person = await publicPerson(request, profile);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("Batch 1057 public data omits private identity-crosswalk fields", async ({ request }) => {
  for (const profile of Object.values(profiles)) {
    const person = await publicPerson(request, profile);
    const serialized = JSON.stringify(person);
    expect(serialized).not.toContain("candidate_identifier");
    expect(serialized).not.toContain("bulk_record_ordinal");
    expect(serialized).not.toContain("private_identifier");
    expect(serialized).not.toContain("service_number_normalized");
  }
});
