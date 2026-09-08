import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const organizations = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/organizations.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 429 separates Army occupations from Egidio Clemente's named employment", async ({ page }) => {
  const kent = profile("2c043090-eefe-5947-ac98-1600a21fb072");
  expect(kent).toMatchObject({
    display_name: "Kent L Clemans",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(kent.immediate_pre_oss_affiliations).toEqual([]);
  expect(kent.last_civilian_pre_service).toEqual([]);
  expect(kent.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Molders",
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  const egidio = profile("233a851f-ae1b-513c-9dba-5ea21bf44103");
  expect(egidio).toMatchObject({
    display_name: "Egidio Clemente",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
  });
  expect(egidio.immediate_pre_oss_affiliations).toEqual([]);
  expect(egidio.last_civilian_pre_service).toEqual([]);
  expect(egidio.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        occupation: "Occupations in printing and publishing, n.e.c.",
        relationship_type: "unknown",
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
      expect.objectContaining({
        canonical_organization: "La Parola del Popolo",
        organization_name_as_found: "La Parola del Popolo",
        role_title: "editor and publisher",
        relationship_type: "employment",
        temporal_basis: "documented_prewar",
        claim_confidence: "high",
      }),
    ]),
  );

  const laParola = organizations.find(
    (organization: { canonical_name: string }) =>
      organization.canonical_name === "La Parola del Popolo",
  );
  expect(laParola).toMatchObject({
    historical_name: "La Parola del Popolo",
    organization_type: "periodical",
    sector: "journalism_and_media",
  });

  await page.goto(`./people/${egidio.person_id}/`);
  await expect(page.getByRole("heading", { name: "Egidio Clemente", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("La Parola del Popolo");
  await expect(page.locator("main")).toContainText("editor and publisher");
  await expect(page.locator("main")).toContainText("documented prewar");
  await expect(page.locator("main")).toContainText("No publishable immediate affiliation or civilian employer is recorded yet");
});

test("Batch 429 preserves Marcel Clemente's unnamed last civilian employer", async ({ page }) => {
  const marcel = profile("473a6680-1fdd-501a-8453-3098e500c34a");
  expect(marcel).toMatchObject({
    display_name: "Marcel J Clemente",
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
  });
  expect(marcel.immediate_pre_oss_affiliations).toEqual([]);
  expect(marcel.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      organization_name_as_found: "a guarantee and trust company in New York",
      role_title: null,
      occupation: null,
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(marcel.claims).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        claim_type: "identity",
        claim_confidence: "confirmed",
      }),
      expect.objectContaining({
        claim_type: "last_civilian_pre_service",
        claim_confidence: "high",
      }),
    ]),
  );

  await page.goto(`./people/${marcel.person_id}/`);
  await expect(page.getByRole("heading", { name: "Marcel J Clemente", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("a guarantee and trust company in New York");
  await expect(page.locator("main")).toContainText("strongly date bounded");
  await expect(page.locator("main")).toContainText("the legal organization name are unknown");
  await expect(page.locator("main")).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(page.getByRole("link", { name: "Foreign Decorations" }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: "Marcel J. Clemente Becomes a Major" }).first()).toBeVisible();
});

test("Batch 429 classifies Georges Clement without inventing a predecessor", async ({ page }) => {
  const georges = profile("47425d8d-4099-5f1b-9655-2882ee2ffc4c");
  expect(georges).toMatchObject({
    display_name: "Georges Clement",
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
  });
  expect(georges.immediate_pre_oss_affiliations).toEqual([]);
  expect(georges.last_civilian_pre_service).toEqual([]);
  expect(georges.other_pre_oss_affiliations).toEqual([]);
  expect(georges.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "high",
      publication_status: "published",
    }),
  );

  await page.goto(`./people/${georges.person_id}/`);
  await expect(page.getByRole("heading", { name: "Georges Clement", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("French sous-lieutenant attached to the Office of Strategic Services");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("Review Box 128");
  await expect(page.getByRole("link", { name: "Georges Clement" }).first()).toBeVisible();
});

test("Batch 429 keeps unresolved candidates private while preserving every index row", async ({ page }) => {
  const expected = [
    ["fbe4cd0f-da86-5c6c-9265-77cacddc0211", "Alice B Clem", "84ef483b-0472-5239-8dd2-1cbb5067e9c9", "128", null, "unresolved", "requires_archival_review"],
    ["2c043090-eefe-5947-ac98-1600a21fb072", "Kent L Clemans", "ec80b158-189e-5d3f-a85f-08bbcd2469f2", "128", null, "confirmed", "occupation_only_found"],
    ["f9033b86-3f4b-5622-b9ac-6bf79886dd94", "Robert E Clemens", "c7047f33-01ea-55a1-ad9f-90ea6c2ceb03", "128", null, "ambiguous", "needs_identity_review"],
    ["86fedb3c-a7b5-55c1-8cbc-f395f1fc7664", "Catherine A Clement", "2d4ee581-a52b-551d-83d5-68ae07bba87b", "128", null, "unresolved", "requires_archival_review"],
    ["47425d8d-4099-5f1b-9655-2882ee2ffc4c", "Georges Clement", "847502c9-1175-5c6c-b80c-570950f3be70", "128", "S/Lt", "high_confidence", "requires_archival_review"],
    ["0a2d1f90-4d6a-52aa-b99a-0887e7e0c8b7", "Geraldine Clement", "cae8ca68-1b28-50e4-be15-1f26776bc205", "128", null, "unresolved", "requires_archival_review"],
    ["233a851f-ae1b-513c-9dba-5ea21bf44103", "Egidio Clemente", "04f94369-90e8-57e3-8e00-13b2dd459852", "128", "Cpl", "confirmed", "documented_prewar_employer_found"],
    ["473a6680-1fdd-501a-8453-3098e500c34a", "Marcel J Clemente", "fa97d1d4-cf19-5836-816d-d9a4f73de86e", "129", null, "confirmed", "documented_prewar_employer_found"],
    ["429fcf99-b09c-550c-9ece-97747fa884f6", "Claras B Clements", "dd85dba0-75a2-5318-a989-1b0e884c5dd6", "129", null, "unresolved", "requires_archival_review"],
    ["a08954d1-eab1-59dc-9b2e-cef9888bdb6a", "Ira L Clements", "4622e108-c7d6-5dc8-9e09-01fff3a77925", "129", null, "ambiguous", "needs_identity_review"],
  ];

  for (const [id, name, sourceRecordId, box, rank, identityStatus, researchStatus] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({
      display_name: name,
      identity_status: identityStatus,
      research_status: researchStatus,
    });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 84,
      box,
      archive_location: "230/86/28/07",
      rank_as_indexed: rank,
    });
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );

    await page.goto(`./people/?q=${encodeURIComponent(String(name))}`);
    await expect(page.getByRole("link", { name: String(name), exact: true })).toBeVisible();
  }

  for (const id of [
    "2c043090-eefe-5947-ac98-1600a21fb072",
    "f9033b86-3f4b-5622-b9ac-6bf79886dd94",
    "0a2d1f90-4d6a-52aa-b99a-0887e7e0c8b7",
    "233a851f-ae1b-513c-9dba-5ea21bf44103",
    "a08954d1-eab1-59dc-9b2e-cef9888bdb6a",
  ]) {
    expect(profile(id).source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
  }

  for (const id of [
    "fbe4cd0f-da86-5c6c-9265-77cacddc0211",
    "f9033b86-3f4b-5622-b9ac-6bf79886dd94",
    "86fedb3c-a7b5-55c1-8cbc-f395f1fc7664",
    "0a2d1f90-4d6a-52aa-b99a-0887e7e0c8b7",
    "429fcf99-b09c-550c-9ece-97747fa884f6",
    "a08954d1-eab1-59dc-9b2e-cef9888bdb6a",
  ]) {
    const person = profile(id);
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }
});
