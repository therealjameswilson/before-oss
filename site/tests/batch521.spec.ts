import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["aee33554-653a-5f5c-a81b-b95c7f4b900c", "Amando Dalisay", "edc97d66-a9e1-586b-9437-d4fdb08ce8ff", false],
  ["c38ae3c4-c561-5384-b97f-56c08970c017", "James W Dallas", "6faa494c-ade5-5b5c-9b1e-524c2088fc9c", false],
  ["4c362695-a623-550e-bf18-aa19fe9bc4be", "John E Dally", "f48c1b1f-9cf6-5048-b265-90ed7baf15fd", true],
  ["771dbfa8-6c54-553c-b81b-0f7a044a9e0a", "Miguel S Dalmau", "0a4c0d60-3836-59e6-9192-366964934e55", true],
  ["99e21774-5b37-5d7a-b71c-9d2a0714e56d", "Ronald E Dalrymple", "8c012f4e-15cb-5dc6-8ad2-a1de0c1c3acb", true],
  ["60f10b8b-9ded-51e7-ae67-780fae66155a", "Robert A Dalton", "0378c412-b66a-5aec-a190-e9cdb6e24b54", true],
  ["5c15eb85-52eb-59fa-8a02-86f1979c1a9d", "Dennis D Daly", "5eae9537-c962-5b3e-bc53-66c91279d180", true],
  ["921d760b-83ed-5bba-b5c9-e3d72449f47a", "Donald D Daly", "d12687fa-7d28-547f-8ec6-fc54c324ebbe", false],
  ["3f163c26-669a-5976-850a-67dc3c2ee9f5", "Earle J Daly", "2285b75e-9167-5523-a360-0866289e79ef", false],
  ["3452c4e3-ac1e-5549-a637-6cb49aa85e7f", "Edward F Daly", "628836c7-75b2-5915-b783-511d7ac417a5", true],
] as const;

test("Batch 521 preserves all eleven printed page 104 rows and masks seven private fields", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      archive_location: "230/86/29/05",
      pdf_page: 104,
    });
    if (hasPrivateIdentifier) {
      expect(sourceRecord.serial_masked).toMatch(/^••••\d{4}$/);
    } else {
      expect(sourceRecord.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  const edward = profile("3452c4e3-ac1e-5549-a637-6cb49aa85e7f");
  expect(edward.source_records).toHaveLength(2);
  expect(edward.source_records).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ box: "165", rank_as_indexed: "T-4" }),
      expect.objectContaining({ box: "164", rank_as_indexed: "Cpl" }),
    ]),
  );
});

test("Batch 521 keeps Amando Dalisay's probable student affiliations distinct from employment", () => {
  const amando = profile("aee33554-653a-5f5c-a81b-b95c7f4b900c");
  expect(amando).toMatchObject({
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(amando.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "Harvard University",
        occupation: "Student",
        relationship_type: "student",
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
      }),
      expect.objectContaining({
        canonical_organization: "University of the Philippines",
        occupation: "Student",
        relationship_type: "student",
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
      }),
    ]),
  );
  expect(amando.claims).toHaveLength(3);
});

test("Batch 521 publishes only bounded occupation evidence for five identifier-confirmed people", () => {
  const expected = new Map([
    ["4c362695-a623-550e-bf18-aa19fe9bc4be", ["Student", "student"]],
    ["99e21774-5b37-5d7a-b71c-9d2a0714e56d", ["Chauffeur or driver of a bus, taxi, truck, or tractor", "unknown"]],
    ["60f10b8b-9ded-51e7-ae67-780fae66155a", ["Construction occupations, not elsewhere classified", "unknown"]],
    ["5c15eb85-52eb-59fa-8a02-86f1979c1a9d", ["Lawyers and judges", "unknown"]],
    ["3452c4e3-ac1e-5549-a637-6cb49aa85e7f", ["Actor", "unknown"]],
  ]);

  for (const [id, [occupation, relationshipType]] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      organization_id: null,
      occupation,
      relationship_type: relationshipType,
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    });
    expect(person.claims).toHaveLength(2);
  }
});

test("Batch 521 leaves four unsupported identities without affiliation claims", () => {
  const expected = new Map([
    ["c38ae3c4-c561-5384-b97f-56c08970c017", ["ambiguous", "needs_identity_review"]],
    ["771dbfa8-6c54-553c-b81b-0f7a044a9e0a", ["unresolved", "requires_archival_review"]],
    ["921d760b-83ed-5bba-b5c9-e3d72449f47a", ["ambiguous", "needs_identity_review"]],
    ["3f163c26-669a-5976-850a-67dc3c2ee9f5", ["unresolved", "requires_archival_review"]],
  ]);
  for (const [id, [identityStatus, researchStatus]] of expected) {
    expect(profile(id)).toMatchObject({
      identity_status: identityStatus,
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: researchStatus,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 521 advances exact aggregate coverage without changing the index denominator", () => {
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    research_attempted_people: 4977,
    research_attempt_percent: 20.7895,
    verified_affiliation_people: 566,
    verified_affiliation_percent: 2.3642,
    verified_employer_people: 252,
    verified_employer_percent: 1.0526,
    archival_review_assessed_people: 4932,
    archival_review_percent: 20.6015,
    published_claims: 3936,
    public_sources: 3367,
  });
  expect(stats.research_status_counts).toMatchObject({
    completed: 143,
    needs_identity_review: 276,
    not_started: 18963,
    occupation_only_found: 909,
    requires_archival_review: 3068,
    verified_employer_found: 237,
  });
});

test("Batch 521 creates direct Harvard and University of the Philippines routes", async ({ page }) => {
  await page.goto("./organizations/45ddf347-21c6-59f5-a8ae-517418adf941/");
  await expect(page.locator("h1")).toContainText("Harvard University");
  await expect(page.locator("body")).toContainText("Amando Dalisay");

  await page.goto("./organizations/a0d4db9d-8485-5d1c-801c-c8423a15b417/");
  await expect(page.locator("h1")).toContainText("University of the Philippines");
  await expect(page.locator("body")).toContainText("Amando Dalisay");
});

test.describe("Batch 521 direct profile routes", () => {
  for (const [id, name] of cohort) {
    test(`${name} renders from a direct route`, async ({ page }) => {
      await page.goto(`./people/${id}/`);
      await expect(page.locator("h1")).toContainText(name);
      await expect(page.locator("body")).toContainText("Box 164");
    });
  }
});
