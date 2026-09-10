import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 459 preserves all ten printed rows and masks every private identifier", () => {
  const expected = [
    ["a5d06a7b-dd43-5653-b6cd-3c9e847ddd0b", "Louise A Consiglio", "a4414123-6f5d-5ae4-97d2-0624c37f59f7", null, "••••4771"],
    ["e219173b-7125-532f-8601-07e4e222a0df", "Charles Conssoule", "cef1baa8-9c8f-593f-9833-a9ef475dfa4e", "Capt", null],
    ["3d0c1324-2887-5768-8c3c-e4f13a6a0bb2", "Claude K Constable", "8db5a0cc-5ea8-5e70-8cd9-7e83466e2357", null, "••••3162"],
    ["6b0ada79-5326-5dd8-9a12-e716517ec384", "Lincoln Constance", "9573e1a1-fe9d-51a1-9d64-7ddfa4359999", null, null],
    ["e196af88-045b-5b66-9884-a69ae4134e7f", "Fanny Contaras", "c1e0dfed-c5ca-58f0-ac6a-aebdcf0428c4", null, null],
    ["ce8e3c7e-e91e-572e-9352-a26f9e5f0636", "John P Conte", "0d004921-2a1c-52b1-a1c1-07653d386d6c", null, "••••4654"],
    ["d2a4346e-9e6b-504f-8b50-d66bec6f1d8b", "Carlo Conti", "d632ccda-922d-53c1-880f-178080a8e6a6", null, null],
    ["8e737e38-e569-5b20-9b2b-e3c5dec94ad8", "Thomas Conti", "46e80085-cac6-5c76-954f-f0b4345bcd61", null, "••••0616"],
    ["9fe95939-01a2-51be-b55a-4286bcfbacac", "Nicholas Continisio", "c5426744-db30-588a-ad8f-ea222826ba35", null, "••••1581"],
    ["bc6c3c4a-3f57-59d3-824c-5b0b13b9077f", "Michael C Contrastino", "39f91103-55c6-500b-9c44-a8ab53ca7a60", null, "••••4084"],
  ];

  for (const [id, name, sourceRecordId, rank, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: rank,
        serial_masked: serial,
        box: "140",
        archive_location: "230/86/29/01",
        pdf_page: 90,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 459 publishes Lincoln Constance's Berkeley pathway without conflating earlier employment", async ({ page }) => {
  const lincoln = profile("6b0ada79-5326-5dd8-9a12-e716517ec384");
  expect(lincoln).toMatchObject({
    display_name: "Lincoln Constance",
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(lincoln.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "University of California, Berkeley",
      role_title: "Assistant professor of botany",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(lincoln.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "University of California, Berkeley",
      role_title: "Assistant professor of botany",
    }),
  );
  expect(lincoln.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Washington State College",
      role_title: "Director of the herbarium and instructor in taxonomy and ecology",
      start_date: "1934",
      end_date: "1937",
      temporal_basis: "documented_prewar",
    }),
  );

  await page.goto("./people/" + lincoln.person_id + "/");
  await expect(page.getByRole("heading", { name: "Lincoln Constance", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("University of California, Berkeley");
  await expect(page.locator("main")).toContainText("Washington State College");
  await expect(page.locator("main")).toContainText("Assistant professor of botany");
  await expect(page.locator("main")).toContainText("explicit immediate");
});

test("Batch 459 links but does not merge the Conssoule and Coussoule rows", async ({ page }) => {
  const conssoule = profile("e219173b-7125-532f-8601-07e4e222a0df");
  const coussoule = profile("df63ca56-4ca7-5897-954d-74bf866dde84");
  expect(conssoule).toMatchObject({
    display_name: "Charles Conssoule",
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    manual_review_required: true,
  });
  expect(coussoule).toMatchObject({
    display_name: "Charles Coussoule",
    identity_status: "unresolved",
    research_status: "not_started",
    manual_review_required: true,
  });
  expect(conssoule.person_id).not.toBe(coussoule.person_id);
  expect(conssoule.possible_duplicate_group).toBeTruthy();
  expect(conssoule.possible_duplicate_group).toBe(coussoule.possible_duplicate_group);
  expect(conssoule.claims).toContainEqual(
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
  );
  expect(conssoule.immediate_pre_oss_affiliations).toEqual([]);
  expect(conssoule.last_civilian_pre_service).toEqual([]);

  await page.goto("./people/" + conssoule.person_id + "/");
  await expect(page.getByRole("heading", { name: "Charles Conssoule", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Charles Coussoule");
  await expect(page.locator("main")).toContainText("The two index rows remain separate");
  await expect(page.locator("main")).toContainText("Duplicate group");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 459 publishes three confirmed Army occupation observations without employers", async ({ page }) => {
  const expected = [
    ["8e737e38-e569-5b20-9b2b-e3c5dec94ad8", "Thomas Conti", "Warehousing, storekeeping, handling, loading, unloading, and related occupations, n.e.c.", "1943-03-02"],
    ["9fe95939-01a2-51be-b55a-4286bcfbacac", "Nicholas Continisio", "Construction occupations, n.e.c.", "1942-02-02"],
    ["bc6c3c4a-3f57-59d3-824c-5b0b13b9077f", "Michael C Contrastino", "Welders and flame cutters", "1943-05-21"],
  ];

  for (const [id, name, occupation, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        occupation,
        end_date: endDate,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );

    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(occupation);
    await expect(page.locator("main")).toContainText(
      "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 459 exposes Louise Consiglio's first-name conflict without transferring Army facts", async ({ page }) => {
  const louise = profile("a5d06a7b-dd43-5653-b6cd-3c9e847ddd0b");
  expect(louise).toMatchObject({
    display_name: "Louise A Consiglio",
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    manual_review_required: true,
  });
  expect(louise.other_pre_oss_affiliations).toEqual([]);
  expect(louise.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  );
  expect(JSON.stringify(louise)).not.toContain("32904771");

  await page.goto("./people/" + louise.person_id + "/");
  await expect(page.getByRole("heading", { name: "Louise A Consiglio", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("first-name conflict");
  await expect(page.locator("main")).toContainText("Box 140");
});

test("Batch 459 keeps unresolved and ambiguous people claim-free", () => {
  const expected = [
    ["3d0c1324-2887-5768-8c3c-e4f13a6a0bb2", "ambiguous", "needs_identity_review"],
    ["e196af88-045b-5b66-9884-a69ae4134e7f", "unresolved", "requires_archival_review"],
    ["ce8e3c7e-e91e-572e-9352-a26f9e5f0636", "ambiguous", "needs_identity_review"],
    ["d2a4346e-9e6b-504f-8b50-d66bec6f1d8b", "ambiguous", "needs_identity_review"],
  ];

  for (const [id, identityStatus, researchStatus] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      research_status: researchStatus,
      manual_review_required: true,
    });
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.next_action).toContain("Box 140");
  }
});
