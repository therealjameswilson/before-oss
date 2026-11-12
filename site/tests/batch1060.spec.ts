import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const profiles = {
  josephMeegan: ["fc2b05f3-2436-5ae9-b88b-01b7b6080717", "Joseph Meegan"],
  donaldMeehan: ["1e06c56a-6808-58f4-abb1-d7a729d5c810", "Donald J Meehan"],
  williamMeek: ["f44ab699-af7c-5b2d-9d83-440c6e958da5", "William R Meek"],
  leonardMeeker: ["a5ef50b1-f406-5e62-a829-2be84a182538", "Leonard C Meeker"],
  gaudensMegaro: ["7f5823b9-e766-5a55-9e6e-05ec39b5ad1e", "Gaudens Megaro"],
  lincolnMei: ["aabc6afc-6a05-5342-b1c2-4ff5d7b48f55", "Lincoln Mei"],
  henryMeigs: ["203ca089-cf20-53cc-8364-7847b336f171", "Henry H Meigs"],
  johnMeily: ["08962f8b-b560-5ce7-a3fc-ed9817e8f99c", "John J Meily"],
  michaelMeixner: ["33ac230d-0524-5c61-92da-d087da50f79b", "Michael S Meixner"],
  leifMeland: ["24a68ddd-d4f3-5d05-a9fb-7f3b382b52a9", "Leif E Meland"],
  iJMelchior: ["09119446-f015-5b6e-b512-e2ad4104d5dc", "I J Melchior"],
  michaelMelehes: ["0b87149d-b1f9-542d-b53d-dbd99d2772bd", "Michael Melehes"],
  kostaMelinkoff: ["e81bf272-edef-5a3a-94f7-87ac7a542d9c", "Kosta Melinkoff"],
  michaelMelkonian: ["2c99f3a1-3b85-543b-b2e0-0cb69b197ded", "Michael Melkonian"],
  charlesMeledonis: ["0941bebf-43dd-5cfa-b669-1fdfa3c6e161", "Charles S Meledonis"],
  bertMellgren: ["1ae517c5-847f-5f78-a4c8-8dba7635158a", "Bert E Mellgren"],
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

test("Batch 1060 publishes all 46 page-315 rows through 45 terminal profiles", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(
      ...(await response.json()).filter(
        (person: { source_records: { pdf_page: number }[] }) =>
          person.source_records.some((row) => row.pdf_page === 315),
      ),
    );
  }
  expect(people).toHaveLength(45);
  expect(
    people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.filter((row) => row.pdf_page === 315),
    ),
  ).toHaveLength(46);
  for (const person of people) {
    expect(["not_started", "in_progress", "candidate_found"]).not.toContain(
      person.research_status,
    );
  }
});

test("Batch 1060 Army-entry occupations remain qualified and organization-free", async ({ request, page }) => {
  for (const [profile, occupation] of [
    [profiles.donaldMeehan, "file clerk"],
    [profiles.williamMeek, "construction occupation, n.e.c."],
    [profiles.michaelMeixner, "pressman or plate printer in printing"],
    [profiles.charlesMeledonis, "electrical engineer"],
    [profiles.bertMellgren, "showman"],
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
  await page.goto(`./people/${profiles.charlesMeledonis[0]}/`);
  await expect(page.locator("main")).toContainText("electrical engineer");
  await expect(page.locator("main")).toContainText("temporal relation uncertain");
});

test("Page-315 verified employer and documented-prewar profiles retain stronger chronology", async ({ request }) => {
  const leonard = await publicPerson(request, profiles.leonardMeeker);
  expect(leonard).toMatchObject({ research_status: "verified_employer_found" });
  expect(leonard.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army" }),
  ]);
  expect(leonard.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Office of the Solicitor General" }),
  ]);

  const gaudens = await publicPerson(request, profiles.gaudensMegaro);
  expect(gaudens).toMatchObject({ research_status: "verified_employer_found" });
  expect(gaudens.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Coordinator of Information" }),
  ]);
  expect(gaudens.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Queens College" }),
  ]);

  const ib = await publicPerson(request, profiles.iJMelchior);
  expect(ib).toMatchObject({ research_status: "verified_employer_found" });
  expect(ib.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Radio City Music Hall" }),
  ]);

  const leif = await publicPerson(request, profiles.leifMeland);
  expect(leif).toMatchObject({ research_status: "documented_prewar_employer_found" });
  expect(leif.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "99th Infantry Battalion (Separate)" }),
  ]);
  expect(leif.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({ occupation: "sailor or deckhand, except U.S. Navy" }),
  );
});

test("Page-315 duplicate and identity-conflict boundaries remain visible", async ({ request }) => {
  const michael = await publicPerson(request, profiles.michaelMelkonian);
  expect(michael).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(
    michael.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 315),
  ).toHaveLength(2);
  expect(michael.other_pre_oss_affiliations).toHaveLength(0);

  for (const profile of [profiles.johnMeily, profiles.kostaMelinkoff]) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({
      identity_status: "conflicting",
      research_status: "conflicting_sources",
    });
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
  const lincoln = await publicPerson(request, profiles.lincolnMei);
  expect(lincoln).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
  });
});

test("Undecodable code 992 and OSS-only identity evidence stay qualified", async ({ request }) => {
  const henry = await publicPerson(request, profiles.henryMeigs);
  expect(henry).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(henry.other_pre_oss_affiliations).toHaveLength(0);
  expect(JSON.stringify(henry)).not.toContain("code 992");

  const michael = await publicPerson(request, profiles.michaelMelehes);
  expect(michael).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(michael.other_pre_oss_affiliations).toHaveLength(0);
});

test("Joseph Meegan uses the visually printed name while preserving the raw variant", async ({ request, page }) => {
  const joseph = await publicPerson(request, profiles.josephMeegan);
  expect(joseph).toMatchObject({
    display_name: "Joseph Meegan",
    research_status: "requires_archival_review",
  });
  expect(joseph.name_variants).toContain("Jospeh Meegan");
  expect(joseph.name_variants).toContain("Joseph Meegan");
  expect(joseph.source_records).toContainEqual(
    expect.objectContaining({
      indexed_last_name: "Meegan",
      indexed_first_name: "Joseph",
      pdf_page: 315,
    }),
  );
  await page.goto(`./people/${profiles.josephMeegan[0]}/`);
  await expect(page.locator("main")).toContainText("Joseph Meegan");
  await expect(page.locator("main")).toContainText("Jospeh Meegan");
});

test("Batch 1060 public data omits private identity-crosswalk fields", async ({ request }) => {
  for (const profile of Object.values(profiles)) {
    const person = await publicPerson(request, profile);
    const serialized = JSON.stringify(person);
    expect(serialized).not.toContain("candidate_identifier");
    expect(serialized).not.toContain("bulk_record_ordinal");
    expect(serialized).not.toContain("private_identifier");
    expect(serialized).not.toContain("service_number_normalized");
  }
});
