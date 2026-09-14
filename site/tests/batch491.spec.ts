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
  ["db3c624d-7dee-52c3-9db5-d03c585998ca", "Virginia Crate", "3962b676-50fc-507d-98a0-3ba3df8b84d8", false],
  ["8b13f39b-28a1-5dec-b1c2-a94bc65a4b2d", "John H Craven", "31ea175d-65c5-5bce-bf8f-2573cf5c54f9", true],
  ["ddb91f00-acd8-56e7-9905-b79393540907", "William C Craven", "f9564fe3-32cb-596b-bf5b-d764450222b0", true],
  ["0f51260d-7a48-5849-9740-5220e0d7f9fa", "William M Cravener", "6bdecefd-608a-5a61-928c-73b65dd4ffe9", true],
  ["ce10d4ed-b5e1-52f1-9f42-7ee6769ba198", "Kenneth W Craver", "9768c77f-9a61-51a3-a4ee-e7b55e9b4a02", true],
  ["487ca004-c9a3-584f-8fbb-701dc70a614c", "Alexander L Crawford", "9aed6245-a23e-59a7-ba21-541d6af1d27a", true],
  ["fd855d4a-79ca-5eac-8aa3-710aacf84f37", "Alice M Crawford", "7fbbce2d-2b53-5853-b9f9-ede567389938", false],
  ["30f03ca7-5eb2-58ff-abf8-2bbd4dbe6114", "Archibald S Crawford", "928a9b76-8152-5bbf-bfce-cc6429bb8c26", false],
  ["a38a8f20-185c-51b5-81de-c1ad492e924a", "Chester H Crawford", "6304d627-cbaf-5f38-8928-f591d291fa75", true],
  ["72d10d6e-782c-53f2-b04e-7d7307e33634", "Eugene E Crawford", "521814bd-c0d7-5535-b37c-d704e829bb0e", false],
] as const;

test("Batch 491 preserves all ten page 97 rows and masks every printed identifier", () => {
  for (const [id, name, sourceRecordId, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "152",
      archive_location: "230/86/29/03",
      pdf_page: 97,
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

test("Batch 491 publishes two qualified identifier-supported occupations", () => {
  const expected = [
    [
      "8b13f39b-28a1-5dec-b1c2-a94bc65a4b2d",
      "high_confidence",
      "Managers and officials, not elsewhere classified",
      "1943-04-21",
    ],
    [
      "0f51260d-7a48-5849-9740-5220e0d7f9fa",
      "confirmed",
      "Welders and flame cutters",
      "1942-12-08",
    ],
  ] as const;

  for (const [id, identityStatus, occupation, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: identityStatus,
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        occupation,
        end_date: endDate,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    );
    expect(person.claims).toContainEqual(
      expect.objectContaining({
        claim_type: "occupation",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
  }
});

test("Batch 491 confirms two enlisted identities without unsafe occupation decoding", () => {
  const expected = [
    ["ddb91f00-acd8-56e7-9905-b79393540907", "417"],
    ["487ca004-c9a3-584f-8fbb-701dc70a614c", "668"],
  ] as const;

  for (const [id, withheldCode] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
    });
    expect(person.claims).toContainEqual(
      expect.objectContaining({
        claim_type: "identity",
        claim_confidence: "confirmed",
        match_notes: expect.stringContaining(`${withheldCode} is deliberately withheld`),
      }),
    );
  }
});

test("Batch 491 preserves unresolved, ambiguous, alias, and short-identifier cases", () => {
  const unresolved = [
    "db3c624d-7dee-52c3-9db5-d03c585998ca",
    "30f03ca7-5eb2-58ff-abf8-2bbd4dbe6114",
  ];
  const ambiguous = [
    "ce10d4ed-b5e1-52f1-9f42-7ee6769ba198",
    "fd855d4a-79ca-5eac-8aa3-710aacf84f37",
    "a38a8f20-185c-51b5-81de-c1ad492e924a",
    "72d10d6e-782c-53f2-b04e-7d7307e33634",
  ];

  for (const id of unresolved) {
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
  for (const id of ambiguous) {
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
  expect(profile("30f03ca7-5eb2-58ff-abf8-2bbd4dbe6114").source_records).toContainEqual(
    expect.objectContaining({ notes_as_indexed: "aka Arch" }),
  );
});

test("Batch 491 direct routes expose qualifications and archival guidance", async ({ page }) => {
  expect(stats.research_attempted_people).toBeGreaterThanOrEqual(4678);
  expect(stats.verified_affiliation_people).toBeGreaterThanOrEqual(534);
  expect(stats.verified_employer_people).toBeGreaterThanOrEqual(237);
  expect(stats.archival_review_assessed_people).toBeGreaterThanOrEqual(4633);

  await page.goto("./people/8b13f39b-28a1-5dec-b1c2-a94bc65a4b2d/");
  await expect(page.getByRole("heading", { name: "John H Craven", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Managers and officials, not elsewhere classified");
  await expect(page.locator("main")).toContainText("GRAVEN JOHN H");
  await expect(page.locator("main")).toContainText("no employer is named");

  await page.goto("./people/0f51260d-7a48-5849-9740-5220e0d7f9fa/");
  await expect(page.getByRole("heading", { name: "William M Cravener", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Welders and flame cutters");

  await page.goto("./people/ddb91f00-acd8-56e7-9905-b79393540907/");
  await expect(page.getByRole("heading", { name: "William C Craven", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("do not decode value 417");

  await page.goto("./people/30f03ca7-5eb2-58ff-abf8-2bbd4dbe6114/");
  await expect(page.getByRole("heading", { name: "Archibald S Crawford", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("aka Arch");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
