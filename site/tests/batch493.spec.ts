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
  ["ef0de5ff-c499-5763-b8a9-998215c5a4e7", "Robert N Creadick", "ab3cc6ce-d905-5cb2-a40a-be488ac3d15a", true],
  ["a7c6f86e-9a57-59df-a246-277ccc4a24a7", "Charles C Creamer", "b18cfb70-ef47-586e-bb86-9e184fb24779", false],
  ["95cf3e41-ddb2-589b-9a9d-c65a545a0008", "Robert D Creaven", "78926a83-0b5e-584d-a911-bf51340212d8", true],
  ["1d43ed61-dd97-57e6-9e01-4209f5861f9a", "Eugene A Creech Jr.", "f33f130e-0c62-5e10-9a76-9e75914db84f", true],
  ["d512db94-dcb2-56e7-9383-ad639d2fe45b", "John W Creech", "7378c066-0cef-5d4b-839a-8b7e27e5c83e", true],
  ["efd18232-4ba7-5ca8-869f-0dc55765cc3a", "Emma L Creed", "fe2c248f-9a60-530d-9bb1-aee86e60d907", false],
  ["b0703f3f-ee62-5535-8c1a-fc3eb1282eff", "John A Creedy", "e0ff2c67-2b84-5987-bbb1-2c4c8582040d", true],
  ["e359488c-4462-50f2-bb29-7954c00d2ae6", "James A Creel", "6f8a3171-e69a-5a0a-95f4-78e6024dacba", false],
  ["3e0a9e89-de06-502c-8ca9-fced6a71ecab", "Wilhelmine S Creel", "86f23466-d63d-5f4d-bd18-7d899b95c86e", false],
  ["22a38666-b2cf-5656-a1b5-b05645817f83", "Albert M Creighton Jr.", "52da279f-e33c-540d-bd58-af488f4e8c4f", false],
] as const;

test("Batch 493 preserves all ten page 98 source rows and masks printed identifiers", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "153",
      archive_location: "230/86/29/03",
      pdf_page: 98,
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
});

test("Batch 493 publishes only Creaven's accessible identifier-supported occupation", () => {
  const person = profile("95cf3e41-ddb2-589b-9a9d-c65a545a0008");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "blocked_by_source_access",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(person.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      occupation: "Carpenters",
      end_date: "1941-02-17",
      relationship_type: "unknown",
      temporal_basis: "documented_prewar",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
    }),
  );
  expect(person.claims).toHaveLength(1);
  expect(person.claims[0]).toMatchObject({
    claim_type: "occupation",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(JSON.stringify(person)).not.toContain("When did you come into the Army");
  expect(JSON.stringify(person)).not.toContain("May 1941");
});

test("Batch 493 qualifies probable John A Creedy journalism and does not label it immediate", () => {
  const person = profile("b0703f3f-ee62-5535-8c1a-fc3eb1282eff");
  expect(person).toMatchObject({
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        organization_name_as_found: "Durham Herald Sun",
        role_title: "Reporter",
        relationship_type: "employment",
        temporal_basis: "documented_prewar",
        identity_confidence: "probable",
        claim_confidence: "medium",
      }),
      expect.objectContaining({
        organization_name_as_found:
          "a union newspaper for tobacco, hosiery and cotton workers",
        role_title: "Editor",
        relationship_type: "employment",
        temporal_basis: "documented_prewar",
        identity_confidence: "probable",
        claim_confidence: "medium",
      }),
    ]),
  );
  expect(person.claims).toHaveLength(2);
});

test("Batch 493 preserves three unresolved and five ambiguous cases", () => {
  for (const id of [
    "a7c6f86e-9a57-59df-a246-277ccc4a24a7",
    "efd18232-4ba7-5ca8-869f-0dc55765cc3a",
    "3e0a9e89-de06-502c-8ca9-fced6a71ecab",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
  for (const id of [
    "ef0de5ff-c499-5763-b8a9-998215c5a4e7",
    "1d43ed61-dd97-57e6-9e01-4209f5861f9a",
    "d512db94-dcb2-56e7-9383-ad639d2fe45b",
    "e359488c-4462-50f2-bb29-7954c00d2ae6",
    "22a38666-b2cf-5656-a1b5-b05645817f83",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "needs_identity_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});

test("Batch 493 direct routes expose qualifications and archival next actions", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4698);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(534);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(237);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4653);

  await page.goto("./people/95cf3e41-ddb2-589b-9a9d-c65a545a0008/");
  await expect(page.getByRole("heading", { name: "Robert D Creaven", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Carpenters");
  await expect(page.locator("main")).toContainText("blocked by source access");
  await expect(page.locator("main")).toContainText("Hoover item 69085.159");

  await page.goto("./people/b0703f3f-ee62-5535-8c1a-fc3eb1282eff/");
  await expect(page.getByRole("heading", { name: "John A Creedy", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Durham Herald Sun");
  await expect(page.locator("main")).toContainText("union newspaper");
  await expect(page.locator("main")).toContainText("Probable");
  await expect(page.locator("main")).toContainText("neither proves it was the immediate pre-OSS affiliation");

  await page.goto("./people/ef0de5ff-c499-5763-b8a9-998215c5a4e7/");
  await expect(page.getByRole("heading", { name: "Robert N Creadick", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("literal six-digit value");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
