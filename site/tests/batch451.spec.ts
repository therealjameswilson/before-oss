import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 451 qualifies Condakes's Army-to-OSS pathway and keeps student status separate", async ({ page }) => {
  const george = profile("8343ccd8-4dff-529f-9814-ba9c5b91e09b");
  expect(george).toMatchObject({
    display_name: "George P Condakes",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "completed",
  });
  expect(george.name_variants).toContain("George Peter Condakes");
  expect(george.last_civilian_pre_service).toEqual([]);
  expect(george.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "100th Infantry Division, United States Army",
      organization_name_as_found: "100th Infantry Division",
      relationship_type: "military_assignment",
      immediate_pre_oss: true,
      last_civilian_pre_service: false,
      temporal_basis: "explicit_immediate",
      claim_confidence: "medium",
    }),
  );
  expect(george.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Northeastern University",
      relationship_type: "student",
      immediate_pre_oss: false,
      last_civilian_pre_service: false,
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${george.person_id}/`);
  await expect(page.getByRole("heading", { name: "George P Condakes", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("George Peter Condakes");
  await expect(page.locator("main")).toContainText("100th Infantry Division");
  await expect(page.locator("main")).toContainText("Northeastern University");
  await expect(page.locator("main")).toContainText("student");
  await expect(page.locator("main")).toContainText("medium");
  await expect(page.locator("main")).toContainText(
    "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 451 confirms Condayan without inventing a pre-OSS employer", async ({ page }) => {
  const vahram = profile("2b9ac394-0947-5ff1-887d-7bc1e3668029");
  expect(vahram).toMatchObject({
    display_name: "Vahram H Condayan",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(vahram.immediate_pre_oss_affiliations).toEqual([]);
  expect(vahram.last_civilian_pre_service).toEqual([]);
  expect(vahram.other_pre_oss_affiliations).toEqual([]);
  expect(vahram.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "confirmed",
      publication_status: "published",
    }),
  );

  await page.goto(`./people/${vahram.person_id}/`);
  await expect(page.getByRole("heading", { name: "Vahram H Condayan", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("WN#27076");
  await expect(page.locator("main")).toContainText("French Somali Coast");
  await expect(page.locator("main")).toContainText("Review Box 137");
  await expect(page.locator("main")).toContainText(
    "Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold",
  );
});

test("Batch 451 publishes Condict's UVM study without turning it into employment", async ({ page }) => {
  const trimble = profile("7a23a917-1275-5007-a704-f8a39fec8a90");
  expect(trimble).toMatchObject({
    display_name: "Trimble C Condict",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(trimble.name_variants).toContain("Trimble Chubb Condict");
  expect(trimble.immediate_pre_oss_affiliations).toEqual([]);
  expect(trimble.last_civilian_pre_service).toEqual([]);
  expect(trimble.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "University of Vermont and State Agricultural College",
      organization_name_as_found: "University of Vermont",
      role_title: "Graduate student in education",
      relationship_type: "student",
      start_date: "1941",
      end_date: "1942",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${trimble.person_id}/`);
  await expect(page.getByRole("heading", { name: "Trimble C Condict", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Trimble Chubb Condict");
  await expect(page.locator("main")).toContainText("University of Vermont");
  await expect(page.locator("main")).toContainText("Graduate student in education");
  await expect(page.locator("main")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );
});

test("Batch 451 preserves all ten printed rows, page split and masked identifiers", async () => {
  const expected = [
    ["780ba410-69bc-5177-b602-c558ce06034e", "Charles L Conaughty", "cf33645e-59f4-5c86-8816-db48a5622381", 88, false],
    ["2d5f6cfa-672a-50f9-8678-27b78f974d4c", "Anthony E Concordia", "3e48e60a-a653-5a15-a29d-51f71c8bfc6a", 88, true],
    ["8c2420c1-82f1-5083-88a0-54270576dfc5", "Marie L Concordia", "42c1c198-2412-5733-b0f6-ae4da96ddce8", 88, false],
    ["8343ccd8-4dff-529f-9814-ba9c5b91e09b", "George P Condakes", "fc85a7ae-2315-5e12-ba37-7557b6641432", 88, false],
    ["2b9ac394-0947-5ff1-887d-7bc1e3668029", "Vahram H Condayan", "616bb5a8-24a1-5f29-97b5-14fe0821dccd", 88, true],
    ["ba42401c-de76-5ea2-85ae-bdbf3a67a43a", "Josephthine M Conde", "70006a38-8b5a-57e7-a31a-7479cb783104", 89, false],
    ["7a23a917-1275-5007-a704-f8a39fec8a90", "Trimble C Condict", "0c82661d-594c-533c-bbf8-7857652bd0e4", 89, true],
    ["6b108f0f-5b8f-5f61-b124-7c801d8bf43f", "Robert S Condie", "21ee3836-e57c-558b-8292-f9bbf00e98bd", 89, true],
    ["f16ee2f2-158a-5256-8b48-960b81d55951", "E C Condit", "d9eaf2d8-e3aa-5ba1-a965-21f2a77a6730", 89, false],
    ["686502ab-4d52-59e3-94f2-50392d15ee8f", "Jean O Condit", "96cb07b5-acc3-5d24-ad30-9b6e4b270261", 89, false],
  ];

  for (const [id, name, sourceRecordId, pdfPage, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      box: "137",
      notes_as_indexed: null,
      archive_location: "230/86/29/01",
      pdf_page: pdfPage,
    });
    if (hasSerial) {
      expect(person.source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
    } else {
      expect(person.source_records[0].serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 451 leaves seven unresolved profiles free of unsupported affiliations", async ({ page }) => {
  const unresolved = [
    ["780ba410-69bc-5177-b602-c558ce06034e", "Charles L Conaughty", "requires_archival_review"],
    ["2d5f6cfa-672a-50f9-8678-27b78f974d4c", "Anthony E Concordia", "needs_identity_review"],
    ["8c2420c1-82f1-5083-88a0-54270576dfc5", "Marie L Concordia", "requires_archival_review"],
    ["ba42401c-de76-5ea2-85ae-bdbf3a67a43a", "Josephthine M Conde", "needs_identity_review"],
    ["6b108f0f-5b8f-5f61-b124-7c801d8bf43f", "Robert S Condie", "needs_identity_review"],
    ["f16ee2f2-158a-5256-8b48-960b81d55951", "E C Condit", "needs_identity_review"],
    ["686502ab-4d52-59e3-94f2-50392d15ee8f", "Jean O Condit", "requires_archival_review"],
  ];

  for (const [id, name, status] of unresolved) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: status,
    });
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }

  const josephthine = profile("ba42401c-de76-5ea2-85ae-bdbf3a67a43a");
  await page.goto(`./people/${josephthine.person_id}/`);
  await expect(page.getByRole("heading", { name: "Josephthine M Conde", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Josephthine");
  await expect(page.locator("main")).toContainText("not adopted as corrections");
  await expect(page.locator("main")).toContainText("Review Box 137");
});
