import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page481-e-l-vanduesen-to-thomas-a-varnson-review_batch-981_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["95480abb-10c7-5e64-86a1-2d47edb5637e", "E L Vanduesen"],
  ["791fbd05-3b8c-5f79-b29e-80d5886abab5", "Delbert E Vangampleare"],
  ["34190b8b-4744-50ec-8155-762be392e07e", "Vito Vangi"],
  ["837f23b5-5159-52e9-a811-1fcf59e9f569", "Raymond VanHoven"],
  ["cc145a7a-d0ec-59d5-ac75-b2d4803beb18", "Nicholas A Vanikiotis"],
  ["09a4a886-06b6-5156-b4f1-d88ed8723f39", "Harvey T Vann"],
  ["380abb97-902d-5951-a1d8-6bd6eb32ffa5", "Leslie J Vanoncini"],
  ["ddc13795-1aed-514d-8d8e-0577a0e70c39", "Ida W Van't Hooft"],
  ["177435e9-1e16-5a09-a1ff-8a03541111c1", "Francis E Vantimmeren"],
  ["872fd96b-01dd-5c08-a89e-750b02488fc5", "Riccardo Vanzetti"],
  ["cbacfe58-f834-5547-a2ad-978d4cd2a3c9", "Anne M Varacalli"],
  ["f4e69784-6ef4-5a55-b00e-9e185ae2676c", "Francis R Varacalli"],
  ["b43fa505-c460-52ad-9e03-30ad478e12d6", "Theodore S Varalyay"],
  ["035cd9e5-a925-5452-ba91-94c9c7d93f19", "Ernest J Vardales"],
  ["25db07f4-cf35-5db2-9dab-b70cf2a4a523", "Nicholas J Vardales"],
  ["4f7b6da3-c8bd-53c9-ad9c-8b5580843a18", "Mary Vardoulakis"],
  ["8ddc329b-5166-58be-a81b-05c9de8a832f", "George S Varga"],
  ["f60d655c-d626-561d-8975-05062679d8ec", "Michael S Vargo"],
  ["92b42abf-a44e-5d43-a297-059b899b5601", "Walter P Vargo"],
  ["51f8ab95-fc49-5670-b757-ba89db8b5657", "Peter G Varlan"],
  ["f56c93f0-5f47-5259-9a4f-d1902526e795", "Dimitry V Varley"],
  ["de861165-a156-510b-8259-e9462adb0184", "Herbert W Varner"],
  ["93b0a921-de70-5a2a-b10b-72c9b3e3dde9", "Thomas A Varnson"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 981 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Army bridges publish seven qualified occupations or student statuses, never employers", async ({ request }) => {
  const expected = [
    ["791fbd05-3b8c-5f79-b29e-80d5886abab5", "Delbert E Vangampleare", "general farm hand", "unknown"],
    ["34190b8b-4744-50ec-8155-762be392e07e", "Vito Vangi", "sailor or deckhand outside the U.S. Navy", "unknown"],
    ["cc145a7a-d0ec-59d5-ac75-b2d4803beb18", "Nicholas A Vanikiotis", "student", "student"],
    ["f4e69784-6ef4-5a55-b00e-9e185ae2676c", "Francis R Varacalli", "engraver", "unknown"],
    ["035cd9e5-a925-5452-ba91-94c9c7d93f19", "Ernest J Vardales", "bootblack", "unknown"],
    ["92b42abf-a44e-5d43-a297-059b899b5601", "Walter P Vargo", "metal filer, grinder, buffer, or polisher", "unknown"],
    ["f56c93f0-5f47-5259-9a4f-d1902526e795", "Dimitry V Varley", "professional occupation, not elsewhere classified", "unknown"],
  ] as const;
  for (const [id, name, occupation, relationship] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person.research_status).toBe("occupation_only_found");
    expect(person.personnel_category).toBe("enlisted_army_personnel");
    expect(person.commissioned_officer).toBe(false);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("undefined Army codes remain identity-only and do not create occupations", async ({ request }) => {
  for (const [id, name] of [
    ["25db07f4-cf35-5db2-9dab-b70cf2a4a523", "Nicholas J Vardales"],
    ["8ddc329b-5166-58be-a81b-05c9de8a832f", "George S Varga"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "requires_archival_review",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Vanzetti publishes a prior military assignment without inventing a civilian employer", async ({ request }) => {
  const person = await publicPerson(request, "872fd96b-01dd-5c08-a89e-750b02488fc5", "Riccardo Vanzetti");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "foreign_or_allied_military_personnel",
    allied_or_foreign_personnel: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Italian Air Force (service not further specified)",
      organization_name_as_found: "Air Force",
      occupation: "Air Force engineer",
      relationship_type: "military_assignment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
});

test("Vardoulakis keeps probable student status separate from employment and chronology", async ({ request }) => {
  const person = await publicPerson(request, "4f7b6da3-c8bd-53c9-ad9c-8b5580843a18", "Mary Vardoulakis");
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Wellesley College",
      relationship_type: "student",
      temporal_basis: "temporal_relation_uncertain",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
});

test("Vanikiotis and Vanoncini identity findings do not invent earlier employers", async ({ request }) => {
  const vanikiotis = await publicPerson(request, "cc145a7a-d0ec-59d5-ac75-b2d4803beb18", "Nicholas A Vanikiotis");
  expect(vanikiotis.identity_status).toBe("confirmed");
  expect(vanikiotis.last_civilian_pre_service).toHaveLength(0);
  expect(vanikiotis.other_pre_oss_affiliations).toHaveLength(1);
  expect(vanikiotis.other_pre_oss_affiliations[0].relationship_type).toBe("student");

  const vanoncini = await publicPerson(request, "380abb97-902d-5951-a1d8-6bd6eb32ffa5", "Leslie J Vanoncini");
  expect(vanoncini).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(vanoncini.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(vanoncini.last_civilian_pre_service).toHaveLength(0);
  expect(vanoncini.other_pre_oss_affiliations).toHaveLength(0);
});

test("unbridged people remain affiliation-free and indexed officer status stays visible", async ({ request }) => {
  for (const [id, name] of [
    ["95480abb-10c7-5e64-86a1-2d47edb5637e", "E L Vanduesen"],
    ["837f23b5-5159-52e9-a811-1fcf59e9f569", "Raymond VanHoven"],
    ["09a4a886-06b6-5156-b4f1-d88ed8723f39", "Harvey T Vann"],
    ["ddc13795-1aed-514d-8d8e-0577a0e70c39", "Ida W Van't Hooft"],
    ["177435e9-1e16-5a09-a1ff-8a03541111c1", "Francis E Vantimmeren"],
    ["cbacfe58-f834-5547-a2ad-978d4cd2a3c9", "Anne M Varacalli"],
    ["b43fa505-c460-52ad-9e03-30ad478e12d6", "Theodore S Varalyay"],
    ["f60d655c-d626-561d-8975-05062679d8ec", "Michael S Vargo"],
    ["51f8ab95-fc49-5670-b757-ba89db8b5657", "Peter G Varlan"],
    ["de861165-a156-510b-8259-e9462adb0184", "Herbert W Varner"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }

  const varnson = await publicPerson(request, "93b0a921-de70-5a2a-b10b-72c9b3e3dde9", "Thomas A Varnson");
  expect(varnson).toMatchObject({
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(varnson.other_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 981 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 981 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 668,
    research_attempted_people: 15_498,
    verified_affiliation_people: 1_118,
    verified_employer_people: 503,
    archival_review_assessed_people: 13_974,
    published_claims: 9_857,
    public_sources: 6_375,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
