import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const profiles = {
  francisMcVarish: ["a3b30365-2a1f-5f2e-8e9c-a7a1a2987551", "Francis C McVarish"],
  charlesMcVey: ["28c74028-bb9f-585e-8afa-521e14a920c3", "Charles F McVey"],
  rMcVickerst: ["51318818-d94a-5cd1-ab8d-5500883da0ea", "R McVickerst"],
  chastainMcWilliams: ["71e6a694-3a2a-5b6f-a615-60a3630cc05f", "Chastain McWilliams"],
  juliaMcWilliams: ["a417086c-3c99-5b5a-a198-35e1dc27f553", "Julia C McWilliams"],
  robertMcWilliams: ["05b64e26-6fd7-52b4-b44d-b55381b7ac15", "Robert H McWilliams"],
  georgeMead: ["636ecf8a-9eca-553f-9335-fba09f37be6a", "George G Mead"],
  maryMeadeOne: ["948cd939-1937-5ccb-b3e2-fd58bf08434b", "Mary P Meade"],
  maryMeadeTwo: ["5745d57e-cc7f-57c1-9a11-3673f61baa9e", "Mary P Meade"],
  edwinMeader: ["cd2a9ff7-13d3-5386-9652-c47686c756cb", "Edwin E Meader"],
  lorraineMeader: ["e1d3612e-1ec2-5438-8a7f-8768cad5816d", "Lorraine M Meader"],
  lorraineMeador: ["87534337-8145-51b8-bd77-c4748c6de875", "Lorraine M Meador"],
  francisMeadowcraft: ["73fa35b0-22b5-538e-98d4-e484b27132fa", "Francis Meadowcraft"],
  josephMedagliant: ["382588a9-b2e3-50ad-89fa-1c91994f3511", "Joseph B Medagliant"],
  donnMedalie: ["e4f06177-71b0-59d9-b72d-9f36f3377345", "Donn P Medalie"],
  henryMedieros: ["22a22416-ca55-57e6-9d6d-859bf9eed047", "Henry J Medieros"],
  aneoMediler: ["2c23d961-72ee-5252-99a1-a4e466598994", "Aneo Mediler"],
  thomasMedlicott: ["c2f1a32f-db57-537f-91d3-e21198ed9dbd", "Thomas O Medlicott"],
  herbertMedric: ["fd951697-8d83-5c30-a37d-9799b02da010", "Herbert G Medric"],
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

test("Batch 1059 publishes all 46 page-314 rows as separate terminal profiles", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(
      ...(await response.json()).filter(
        (person: { source_records: { pdf_page: number }[] }) =>
          person.source_records.some((row) => row.pdf_page === 314),
      ),
    );
  }
  expect(people).toHaveLength(46);
  expect(
    people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.filter((row) => row.pdf_page === 314),
    ),
  ).toHaveLength(46);
  for (const person of people) {
    expect(["not_started", "in_progress", "candidate_found"]).not.toContain(
      person.research_status,
    );
  }
});

test("Batch 1059 Army-entry occupations remain qualified and organization-free", async ({ request, page }) => {
  for (const [profile, occupation] of [
    [profiles.francisMcVarish, "author, editor, or reporter"],
    [profiles.charlesMcVey, "sailor or deckhand, except U.S. Navy"],
    [profiles.chastainMcWilliams, "packing, filling, labeling, marking, bottling, or related occupation, n.e.c."],
    [profiles.georgeMead, "civil engineer"],
    [profiles.francisMeadowcraft, "stock clerk"],
    [profiles.henryMedieros, "retail manager"],
    [profiles.herbertMedric, "sales clerk"],
  ] as const) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    ]);
  }
  await page.goto(`./people/${profiles.charlesMcVey[0]}/`);
  await expect(page.locator("main")).toContainText("sailor or deckhand, except U.S. Navy");
  await expect(page.locator("main")).toContainText("medium");
  await expect(page.locator("main")).toContainText("temporal relation uncertain");
});

test("Page-314 verified employer profiles retain stronger cited chronology", async ({ request }) => {
  const julia = await publicPerson(request, profiles.juliaMcWilliams);
  expect(julia).toMatchObject({
    identity_status: "confirmed",
    research_status: "verified_employer_found",
  });
  expect(julia.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Office of War Information" }),
  ]);
  expect(julia.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "W. & J. Sloane" }),
  ]);

  const robert = await publicPerson(request, profiles.robertMcWilliams);
  expect(robert).toMatchObject({ research_status: "verified_employer_found" });
  expect(robert.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Office of Naval Intelligence" }),
  ]);
  expect(robert.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Denver District Attorney's Office" }),
  ]);
  expect(robert.other_pre_oss_affiliations).toHaveLength(0);

  const edwin = await publicPerson(request, profiles.edwinMeader);
  expect(edwin).toMatchObject({ research_status: "verified_employer_found" });
  expect(edwin.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Kalamazoo Vegetable Parchment Company" }),
  ]);
  expect(edwin.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      occupation: "manager or official, n.e.c.",
      claim_confidence: "medium",
    }),
  );
});

test("Page-314 duplicate and identity-conflict boundaries remain visible", async ({ request }) => {
  for (const [leftProfile, rightProfile] of [
    [profiles.maryMeadeOne, profiles.maryMeadeTwo],
    [profiles.lorraineMeader, profiles.lorraineMeador],
  ] as const) {
    const left = await publicPerson(request, leftProfile);
    const right = await publicPerson(request, rightProfile);
    expect(left.person_id).not.toBe(right.person_id);
    for (const person of [left, right]) {
      expect(person).toMatchObject({
        identity_status: "probable",
        research_status: "needs_identity_review",
      });
      expect(person.possible_duplicate_group).toBeTruthy();
      expect(person.other_pre_oss_affiliations).toHaveLength(0);
    }
  }
  for (const profile of [profiles.rMcVickerst, profiles.aneoMediler]) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({
      identity_status: "conflicting",
      research_status: "needs_identity_review",
    });
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
  const joseph = await publicPerson(request, profiles.josephMedagliant);
  expect(joseph).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(joseph.other_pre_oss_affiliations).toHaveLength(0);
});

test("Documented government and military pathways remain distinct from employers", async ({ request, page }) => {
  const donn = await publicPerson(request, profiles.donnMedalie);
  expect(donn).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
  });
  expect(donn.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(donn.last_civilian_pre_service).toHaveLength(0);
  expect(donn.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of State",
      relationship_type: "government_assignment",
    }),
  ]);

  const thomas = await publicPerson(request, profiles.thomasMedlicott);
  expect(thomas).toMatchObject({ research_status: "completed" });
  expect(thomas.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Coast Guard",
      relationship_type: "military_assignment",
    }),
  ]);
  expect(thomas.last_civilian_pre_service).toHaveLength(0);
  await page.goto(`./people/${profiles.thomasMedlicott[0]}/`);
  await expect(page.locator("main")).toContainText("United States Coast Guard");
  await expect(page.locator("main")).toContainText("immediate");
});

test("Batch 1059 public data omits private identity-crosswalk fields", async ({ request }) => {
  for (const profile of Object.values(profiles)) {
    const person = await publicPerson(request, profile);
    const serialized = JSON.stringify(person);
    expect(serialized).not.toContain("candidate_identifier");
    expect(serialized).not.toContain("bulk_record_ordinal");
    expect(serialized).not.toContain("private_identifier");
    expect(serialized).not.toContain("service_number_normalized");
  }
});
