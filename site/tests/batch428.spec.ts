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

test("Batch 428 keeps occupations, student status, and employers distinct", async ({ page }) => {
  for (const [id, name, occupation, relationship, temporalBasis] of [
    [
      "b76676ac-c0d0-5e16-a9fd-78f6a068f3fd",
      "George L Clayton",
      "Cooks, except private family",
      "unknown",
      "temporal_relation_uncertain",
    ],
    [
      "2a98d8c4-2887-55a5-91d1-f9565a177708",
      "Vernon H Clear",
      "Chauffeurs and drivers, bus, taxi, truck, and tractor",
      "unknown",
      "temporal_relation_uncertain",
    ],
    [
      "1b58c43b-3102-5134-928e-c4f93bc8547b",
      "Malachy F Cleary",
      "Students",
      "student",
      "strongly_date_bounded",
    ],
    [
      "069c5b11-7359-58f5-95c6-6547eaa80397",
      "Michael L Cleffi",
      "Machine shop and related occupations, n.e.c.",
      "unknown",
      "temporal_relation_uncertain",
    ],
  ]) {
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
        relationship_type: relationship,
        temporal_basis: temporalBasis,
        claim_confidence: "medium",
      }),
    );

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: String(name), exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(String(occupation));
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
    await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 428 qualifies Gerard P Cleisz's Ohio State employment", async ({ page }) => {
  const gerard = profile("35b048ba-b360-5167-9b82-c3c06aaad2c0");
  expect(gerard).toMatchObject({
    display_name: "Gerard P Cleisz",
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
  });
  expect(gerard.immediate_pre_oss_affiliations).toEqual([]);
  expect(gerard.last_civilian_pre_service).toEqual([]);
  expect(gerard.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "The Ohio State University",
      organization_name_as_found: "Ohio State University",
      role_title: "Assistant, Romance Languages",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      identity_confidence: "probable",
      claim_confidence: "medium",
    }),
  );
  expect(gerard.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "other_pre_oss_affiliation",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );

  const ohioState = organizations.find(
    (organization: { canonical_name: string }) =>
      organization.canonical_name === "The Ohio State University",
  );
  expect(ohioState).toMatchObject({
    historical_name: "Ohio State University",
    sector: "academia_and_research",
  });

  await page.goto(`./people/${gerard.person_id}/`);
  await expect(
    page.getByRole("heading", { name: "Gerard P Cleisz", exact: true }),
  ).toBeVisible();
  await expect(page.locator("main")).toContainText("The Ohio State University");
  await expect(page.locator("main")).toContainText("Assistant, Romance Languages");
  await expect(page.locator("main")).toContainText("probable");
  await expect(page.locator("main")).toContainText("medium");
  await expect(page.locator("main")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );
});

test("Batch 428 keeps unresolved and rejected candidates out of public facts", async ({ page }) => {
  for (const [id, name, identityStatus, researchStatus, evidence] of [
    [
      "3e7906f8-9da0-5ffa-925c-9f37e99b4735",
      "Charlotte Clayton",
      "unresolved",
      "requires_archival_review",
      "no exact-name Charlotte Clayton row",
    ],
    [
      "5ebfb18e-6149-5fed-be21-47991c6daf52",
      "Zola A Clear",
      "unresolved",
      "requires_archival_review",
      "no exact-name Zola A Clear row",
    ],
    [
      "4be4e8dc-5089-5a8d-b46d-68c61b78cc31",
      "Joseph P Cleary",
      "ambiguous",
      "needs_identity_review",
      "Five exact-name Joseph P Cleary Army rows",
    ],
    [
      "e7f29d6e-1b46-53aa-9436-73eba069ef8f",
      "Alice B Cleaveland",
      "unresolved",
      "requires_archival_review",
      "no exact-name Alice B Cleaveland row",
    ],
    [
      "43fd883f-9fad-55bc-a3f1-75aeef606fd6",
      "Dewey Cleek",
      "unresolved",
      "requires_archival_review",
      "no exact-name Dewey Cleek row",
    ],
  ]) {
    const person = profile(String(id));
    expect(person).toMatchObject({
      display_name: name,
      identity_status: identityStatus,
      research_status: researchStatus,
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
    });
    expect(person.claims).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: String(name), exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(String(evidence));
    await expect(page.locator("main")).toContainText("Review Box 128");
    await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 428 preserves source rows, citations, search, and masking", async ({ page }) => {
  const expected = [
    ["3e7906f8-9da0-5ffa-925c-9f37e99b4735", "Charlotte Clayton", "ebc5e01d-2e6e-5dd0-82bc-2a865c1a1fe1", 83],
    ["b76676ac-c0d0-5e16-a9fd-78f6a068f3fd", "George L Clayton", "f4557922-2bb1-59fb-86a5-dc647550c306", 83],
    ["2a98d8c4-2887-55a5-91d1-f9565a177708", "Vernon H Clear", "03f9a3f4-d765-5056-b84a-a317c35618ab", 83],
    ["5ebfb18e-6149-5fed-be21-47991c6daf52", "Zola A Clear", "e6512ba0-208a-5ae6-a4ac-a99a2ffb9179", 83],
    ["4be4e8dc-5089-5a8d-b46d-68c61b78cc31", "Joseph P Cleary", "aa1c755e-7c28-5e4e-b4a8-e75c427e0022", 83],
    ["1b58c43b-3102-5134-928e-c4f93bc8547b", "Malachy F Cleary", "5a475710-9485-5ee9-8913-c4ef8a02df57", 84],
    ["e7f29d6e-1b46-53aa-9436-73eba069ef8f", "Alice B Cleaveland", "1e0ef715-6112-5fe0-a7fd-d906217f8a95", 84],
    ["43fd883f-9fad-55bc-a3f1-75aeef606fd6", "Dewey Cleek", "cc516418-9ac7-544e-a276-d60eb03c561a", 84],
    ["069c5b11-7359-58f5-95c6-6547eaa80397", "Michael L Cleffi", "f629ca29-fb02-5459-8843-854230f13933", 84],
    ["35b048ba-b360-5167-9b82-c3c06aaad2c0", "Gerard P Cleisz", "6a401929-7024-51c4-97c2-90466eb389a8", 84],
  ];

  for (const [id, name, sourceRecordId, pdfPage] of expected) {
    const person = profile(String(id));
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: pdfPage,
      box: "128",
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
    "b76676ac-c0d0-5e16-a9fd-78f6a068f3fd",
    "2a98d8c4-2887-55a5-91d1-f9565a177708",
    "1b58c43b-3102-5134-928e-c4f93bc8547b",
    "069c5b11-7359-58f5-95c6-6547eaa80397",
  ]) {
    expect(profile(id).source_records[0].serial_masked).toMatch(/^••••\d{4}$/);
  }

  await page.goto("./people/069c5b11-7359-58f5-95c6-6547eaa80397/");
  await expect(
    page.getByRole("link", { name: "Michael L. Cleffi obituary" }).first(),
  ).toBeVisible();
  await expect(
    page.getByRole("link", {
      name: "NARA Compiled Code Lists for the Electronic Army Serial Number Merged File",
    }),
  ).toBeVisible();

  await page.goto("./people/35b048ba-b360-5167-9b82-c3c06aaad2c0/");
  await expect(
    page
      .getByRole("link", {
        name: "Record of Proceedings of the Board of Trustees of the Ohio State University, 1940-1943",
      })
      .first(),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "The Hi-Po, September 25, 1959" }).first(),
  ).toBeVisible();
});
