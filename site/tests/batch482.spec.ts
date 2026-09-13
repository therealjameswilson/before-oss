import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 482 preserves page 95 rows 30-39 and masks private identifiers", () => {
  const expected = [
    ["df63ca56-4ca7-5897-954d-74bf866dde84", "Charles Coussoule", "4e16d054-fa63-5d3e-af85-169d89e68afd", "••••3214"],
    ["60185ad5-1d94-5b71-8ca6-9854dff73cd5", "G regory J Coutoupis", "f92a6e2e-d250-5d43-9075-5a184a062b5b", "••••2926"],
    ["815eeb9d-3bc5-5d9e-8a3c-912f6a55ac36", "Henry J Couture", "e8035d2b-82e6-5146-8059-f06105f38af7", "••••2431"],
    ["5b978935-3130-5d1f-9d19-8f6f9a7c0305", "Theodore O Couture", "ad6186b8-554f-5c31-8811-23e79bbb349d", "••••3201"],
    ["355eff6b-58cf-5bd4-9232-ad5211ffa967", "Costa G Couvaras", "3db0fa96-adb3-5591-a279-4a9991a12e4d", "••••7180"],
    ["a6c0c9e3-292c-5415-8a28-a387d3b6e08a", "Francis L Covaleski", "1fc02a0a-51d3-5129-aacf-a9f117a168a8", "••••5815"],
    ["41269d6e-aba4-59e4-9899-311d6e7a1800", "Miguel Covarrubias", "20f7229b-32ec-589c-8883-55e62f527a6f", null],
    ["19328a53-b530-533d-a252-834d29027dec", "Richard B Covel", "bc626f6e-2ef6-5571-ac29-def6896265bd", "••••1102"],
    ["34fedf4e-bc72-57d0-8165-5bbe04ce33ba", "James E Covell", "b8279cd8-9fa2-56bd-b9fd-6f9796168bb6", "••••8495"],
    ["05cd9b9c-42c9-5879-8a9e-7d681591e729", "John Covello Jr.", "4c59397e-a79f-5da0-bc2a-0bec1b59bd5b", "••••7014"],
  ];

  for (const [id, name, sourceRecordId, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        box: "149",
        archive_location: "230/86/29/03",
        pdf_page: 95,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 482 records the four exact Army matches without inventing employers", () => {
  const expected = [
    ["815eeb9d-3bc5-5d9e-8a3c-912f6a55ac36", "Student", "student", "1943-06-17"],
    ["5b978935-3130-5d1f-9d19-8f6f9a7c0305", "Nonprocess occupation in manufacturing, not elsewhere classified", "unknown", "1943-06-14"],
    ["05cd9b9c-42c9-5879-8a9e-7d681591e729", "Occupation in automobile manufacturing, not elsewhere classified", "unknown", "1943-08-03"],
  ];

  for (const [id, occupation, relationship, endDate] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        occupation,
        relationship_type: relationship,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        end_date: endDate,
      }),
    );
  }

  expect(profile("355eff6b-58cf-5bd4-9232-ad5211ffa967")).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
});

test("Batch 482 separates Costa Couvaras's Army pathway from his civilian employers", () => {
  const person = profile("355eff6b-58cf-5bd4-9232-ad5211ffa967");
  expect(person.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(person.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "The National Herald",
      role_title: "Assistant to the publisher",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Assyrmatos", role_title: "Correspondent" }),
      expect.objectContaining({
        canonical_organization: "Greek Pavilion, 1939 New York World's Fair",
        role_title: "Public relations staff",
      }),
    ]),
  );
});

test("Batch 482 renders Costa Couvaras's evidence-qualified profile", async ({ page }) => {
  await page.goto("./people/355eff6b-58cf-5bd4-9232-ad5211ffa967/");
  await expect(page.getByRole("heading", { name: "Costa G Couvaras", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("United States Army");
  await expect(page.locator("main")).toContainText("The National Herald");
  await expect(page.locator("main")).toContainText("Assistant to the publisher");
  await expect(page.locator("main")).toContainText("Assyrmatos");
  await expect(page.locator("main")).toContainText("Greek Pavilion");
  await expect(page.locator("main")).toContainText("Ritchie History Museum");
});

test("Batch 482 keeps Miguel Covarrubias's OSS status indeterminate and Vanity Fair non-employment", async ({ page }) => {
  const person = profile("41269d6e-aba4-59e4-9899-311d6e7a1800");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(person.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Vanity Fair",
      role_title: "Contributing caricaturist",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
    }),
  );

  await page.goto("./people/41269d6e-aba4-59e4-9899-311d6e7a1800/");
  await expect(page.getByRole("heading", { name: "Miguel Covarrubias", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Vanity Fair");
  await expect(page.locator("main")).toContainText("Contributing caricaturist");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 482 preserves the Coussoule duplicate boundary and unresolved cohort", () => {
  const box149 = profile("df63ca56-4ca7-5897-954d-74bf866dde84");
  const box140 = profile("e219173b-7125-532f-8601-07e4e222a0df");
  expect(box149.person_id).not.toBe(box140.person_id);
  expect(box149.possible_duplicate_group).toBe(box140.possible_duplicate_group);
  expect(box149).toMatchObject({
    display_name: "Charles Coussoule",
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "needs_identity_review",
    manual_review_required: true,
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
    claims: [],
  });

  for (const id of [
    "60185ad5-1d94-5b71-8ca6-9854dff73cd5",
    "a6c0c9e3-292c-5415-8a28-a387d3b6e08a",
    "19328a53-b530-533d-a252-834d29027dec",
    "34fedf4e-bc72-57d0-8165-5bbe04ce33ba",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});
