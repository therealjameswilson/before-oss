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

test("Batch 430 keeps David Clift's civilian and military pathways distinct", async ({ page }) => {
  const david = profile("c5830e41-50e0-549d-af0f-4b02a6f3e6f9");
  expect(david).toMatchObject({
    display_name: "David H Clift",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(david.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      organization_name_as_found: "Army",
      role_title: "hospital orderly",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(david.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Columbia University Library",
      role_title: "assistant to the director",
      relationship_type: "employment",
      start_date: "1937",
      end_date: "1942",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(david.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "New York Public Library",
      role_title: "reference work",
      relationship_type: "employment",
      start_date: "1931",
      end_date: "1937",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
  expect(david.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Librarians",
      relationship_type: "unknown",
      claim_confidence: "medium",
    }),
  );

  const columbia = organizations.find(
    (organization: { canonical_name: string }) =>
      organization.canonical_name === "Columbia University Library",
  );
  expect(columbia).toMatchObject({
    historical_name: "Columbia University Library",
    organization_type: "university library",
    sector: "academia_and_research",
  });

  await page.goto(`./people/${david.person_id}/`);
  await expect(page.getByRole("heading", { name: "David H Clift", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Columbia University Library");
  await expect(page.locator("main")).toContainText("assistant to the director");
  await expect(page.locator("main")).toContainText("Army");
  await expect(page.locator("main")).toContainText("hospital orderly");
  await expect(page.locator("main")).toContainText("New York Public Library");
  await expect(page.locator("main")).toContainText("Librarians");
  await expect(page.getByRole("link", { name: "Clift, David H. (1907-1973)" }).first()).toBeVisible();
});

test("Batch 430 publishes Army occupations without inventing employers", async ({ page }) => {
  const expected = [
    ["a87e1264-62b8-5ad4-a5dc-88e0b38acd61", "Harold V Cleveland", "Advertising agents"],
    ["fc53423e-0e2f-54af-a780-68d2fa1cd43f", "Elizabeth A Clifford", "Clerks, general"],
  ];

  for (const [id, name, occupation] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        organization_id: null,
        occupation,
        relationship_type: "unknown",
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    );

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: String(name), exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(String(occupation));
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 430 qualifies Margaret Cleveland and preserves Acice Clifford", async ({ page }) => {
  const margaret = profile("fabdd442-a242-55c4-bad9-393330cf5f87");
  expect(margaret).toMatchObject({
    display_name: "Margaret L Cleveland",
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    research_status: "requires_archival_review",
  });
  expect(margaret.immediate_pre_oss_affiliations).toEqual([]);
  expect(margaret.last_civilian_pre_service).toEqual([]);
  expect(margaret.other_pre_oss_affiliations).toEqual([]);
  expect(margaret.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );

  await page.goto(`./people/${margaret.person_id}/`);
  await expect(page.getByRole("heading", { name: "Margaret L Cleveland", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("probably corresponds");
  await expect(page.locator("main")).toContainText("vouchered civilians");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(page.getByRole("link", { name: "War Department Strategic Services Unit dispatch on civilian personnel assigned to war crimes" }).first()).toBeVisible();

  const acice = profile("09371392-dc10-505c-9d47-5c6613f5179d");
  expect(acice).toMatchObject({
    display_name: "Acice C Clifford",
    identity_status: "unresolved",
    research_status: "requires_archival_review",
  });
  expect(acice.name_variants).not.toContain("Alice C Clifford");
  expect(acice.claims).toEqual([]);

  await page.goto("./people/?q=Acice%20C%20Clifford");
  await expect(page.getByRole("link", { name: "Acice C Clifford", exact: true })).toBeVisible();
  await expect(page.getByRole("link", { name: "Alice C Clifford", exact: true })).toHaveCount(0);
});

test("Batch 430 preserves every page 84 index row and masks private identifiers", async ({ page }) => {
  const expected = [
    ["bcc80989-3047-5a3e-98be-e8634b8a6c72", "Joseph E Clements", "4ecbe085-50f0-59a2-b2e5-f179c35a767e", "ambiguous", "needs_identity_review"],
    ["f882b39b-5397-5e32-891e-81da27f0fde6", "Ysobel Clements", "00a93296-c33b-5168-8739-9e36dae4664a", "unresolved", "requires_archival_review"],
    ["69f5ff96-d546-5aad-b6e1-2e6909228cde", "Edmund C Cleveland", "5da07601-1e0e-5e95-a20b-19a221f0393c", "unresolved", "requires_archival_review"],
    ["5f502899-e592-5395-9f02-d52a290e8157", "Eleanor E Cleveland", "fc4557d3-8150-591b-a81b-83cc2ba4f1a3", "unresolved", "requires_archival_review"],
    ["a87e1264-62b8-5ad4-a5dc-88e0b38acd61", "Harold V Cleveland", "4db52eca-0fbf-5d63-9456-ce06b24f4f98", "confirmed", "occupation_only_found"],
    ["fabdd442-a242-55c4-bad9-393330cf5f87", "Margaret L Cleveland", "e672f507-fd35-59f3-8b4d-34a5a21e5a04", "probable", "requires_archival_review"],
    ["0685bf56-fa83-56f3-9de4-ff7f54250156", "Zito Cleveland", "f44be0d9-8000-53b0-9335-9fb7a394ba69", "unresolved", "requires_archival_review"],
    ["09371392-dc10-505c-9d47-5c6613f5179d", "Acice C Clifford", "87ad4a87-4868-5abc-bbe1-bb8852f79342", "unresolved", "requires_archival_review"],
    ["fc53423e-0e2f-54af-a780-68d2fa1cd43f", "Elizabeth A Clifford", "5af91073-d94c-59dd-910b-63600e6401cc", "confirmed", "occupation_only_found"],
    ["c5830e41-50e0-549d-af0f-4b02a6f3e6f9", "David H Clift", "9ad2c14c-6cb5-5a0a-8438-6d41881d1556", "confirmed", "verified_employer_found"],
  ];

  for (const [id, name, sourceRecordId, identityStatus, researchStatus] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({
      display_name: name,
      identity_status: identityStatus,
      research_status: researchStatus,
    });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 84,
      box: "129",
      archive_location: "230/86/28/07",
      rank_as_indexed: null,
    });
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );

    await page.goto(`./people/?q=${encodeURIComponent(String(name))}`);
    await expect(page.getByRole("link", { name: String(name), exact: true })).toBeVisible();
  }

  for (const id of [
    "69f5ff96-d546-5aad-b6e1-2e6909228cde",
    "a87e1264-62b8-5ad4-a5dc-88e0b38acd61",
    "fc53423e-0e2f-54af-a780-68d2fa1cd43f",
    "c5830e41-50e0-549d-af0f-4b02a6f3e6f9",
  ]) {
    expect(profile(id).source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
  }
});
