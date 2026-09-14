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
  ["187cefeb-92c1-5785-ad92-1d564af0f4ec", "Mary W Cutler", "192c2ff1-720a-5c55-89ef-46d2c1e4cd06", 102, null, false],
  ["80c6025c-e24b-58f4-b6c0-e9eafb0c7bc9", "Richard W Cutler", "bbdb92db-97b7-50bb-81fa-d8fa81a826f1", 102, null, true],
  ["5221df7f-a75a-5c69-bca8-db1c6a9edf55", "Stuart G Cutler", "30f4f8bf-eb54-587f-9398-c7610c9ebd0c", 102, null, true],
  ["7d3046ec-50e8-55d1-8ef1-c0deabc6bc8d", "Charles S Cutting", "0b5fd82d-b733-52ee-82b0-d79e6c11ff45", 102, "Lt Col", true],
  ["a43197dc-7b75-51d4-a4f8-e73c6ff1d003", "Grace M Cutting", "e1ebc039-be88-52b1-a109-7b84db803a12", 102, null, false],
  ["2ac9fab1-3fb7-5d56-a547-525bbdce8ebb", "Robert F Cutting", "a3912040-8d32-53e0-bb51-8625e91c38fc", 102, null, true],
  ["0728e884-3799-5510-ad92-1c2009c652e4", "Theodore S Cutting", "cec936b0-a173-59b8-ae5f-59137a6866ac", 102, null, true],
  ["113627b3-b313-52b3-ba1a-1317ef143624", "Claire H Cyr", "fda2ef41-9133-5b23-a6f6-971d7499349f", 102, null, false],
  ["d7ecf94b-665a-56d5-977b-4608440d4fb7", "Paul Cyr", "317a620e-3e7e-5086-ad22-d76f04a8b242", 102, null, true],
  ["d30d7fcf-2d57-5c1e-8c0b-c770daa5d034", "Louise L Czako", "672d7e50-472b-5143-858f-9e1ffd1e3ed8", 103, null, true],
] as const;

test("Batch 515 preserves ten Box 162 rows, Lieutenant Colonel rank, and seven masked private fields", () => {
  for (const [id, name, sourceRecordId, page, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "162",
      archive_location: "230/86/29/05",
      pdf_page: page,
      rank_as_indexed: rank,
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

test("Batch 515 separates Richard Cutler's last civilian employer from his immediate military pathway", () => {
  const richard = profile("80c6025c-e24b-58f4-b6c0-e9eafb0c7bc9");
  expect(richard).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(richard.last_civilian_pre_service).toHaveLength(1);
  expect(richard.last_civilian_pre_service[0]).toMatchObject({
    canonical_organization: "Donovan, Leisure, Newton & Lumbard",
    role_title: "lawyer",
    relationship_type: "employment",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "high_confidence",
    claim_confidence: "high",
  });
  expect(richard.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(richard.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army Air Forces",
    role_title: "second lieutenant",
    relationship_type: "military_assignment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(richard.claims).toHaveLength(3);
});

test("Batch 515 publishes Paul Cyr only as a qualified occupation at Army entry", () => {
  const paul = profile("d7ecf94b-665a-56d5-977b-4608440d4fb7");
  expect(paul).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "occupation_only_found",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(paul.other_pre_oss_affiliations).toHaveLength(1);
  expect(paul.other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "Actor",
    relationship_type: "unknown",
    end_date: "1941-02-24",
    temporal_basis: "strongly_date_bounded",
    identity_confidence: "high_confidence",
    claim_confidence: "medium",
    organization_id: null,
  });
  expect(paul.claims).toHaveLength(2);
});

test("Batch 515 publishes Charles Cutting's name-and-rank match without inventing an affiliation", () => {
  const charles = profile("7d3046ec-50e8-55d1-8ef1-c0deabc6bc8d");
  expect(charles).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(charles.claims).toHaveLength(1);
  expect(charles.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "high",
    publication_status: "published",
  });
});

test("Batch 515 exposes Louise Czako's name conflict and withholds the Army occupation", () => {
  const louise = profile("d30d7fcf-2d57-5c1e-8c0b-c770daa5d034");
  expect(louise).toMatchObject({
    display_name: "Louise L Czako",
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(louise.claims).toHaveLength(1);
  expect(louise.claims[0]).toMatchObject({
    claim_type: "identity",
    claim_confidence: "conflicting",
    publication_status: "conflicting",
  });
  expect(louise.claims[0].claim_text).toContain("Louise L. Czako");
  expect(louise.claims[0].claim_text).toContain("Louis L. Czako");
});

test("Batch 515 preserves six unresolved or ambiguous profiles without speculative claims", () => {
  for (const id of [
    "5221df7f-a75a-5c69-bca8-db1c6a9edf55",
    "a43197dc-7b75-51d4-a4f8-e73c6ff1d003",
    "0728e884-3799-5510-ad92-1c2009c652e4",
    "113627b3-b313-52b3-ba1a-1317ef143624",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      claims: [],
    });
  }
  for (const id of [
    "187cefeb-92c1-5785-ad92-1d564af0f4ec",
    "2ac9fab1-3fb7-5d56-a547-525bbdce8ebb",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      research_status: "needs_identity_review",
      claims: [],
    });
  }
});

test("Batch 515 advances attempted, verified-employer, and archival coverage", () => {
  expect(stats.research_attempted_people).toBe(4918);
  expect(stats.verified_affiliation_people).toBe(558);
  expect(stats.verified_employer_people).toBe(249);
  expect(stats.archival_review_assessed_people).toBe(4873);
});

test("Batch 515 direct routes expose evidence, distinctions, conflict, and archival guidance", async ({ page }) => {
  await page.goto("./people/80c6025c-e24b-58f4-b6c0-e9eafb0c7bc9/");
  await expect(page.getByRole("heading", { name: "Richard W Cutler", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Donovan, Leisure, Newton & Lumbard");
  await expect(page.locator("main")).toContainText("United States Army Air Forces");
  await expect(page.locator("main")).toContainText("Last civilian employer");

  await page.goto("./people/d7ecf94b-665a-56d5-977b-4608440d4fb7/");
  await expect(page.getByRole("heading", { name: "Paul Cyr", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Actor");
  await expect(page.locator("main")).toContainText("Actors and actresses");
  await expect(page.locator("main")).not.toContainText("Immediate pre-OSS affiliation\nActor");

  await page.goto("./people/d30d7fcf-2d57-5c1e-8c0b-c770daa5d034/");
  await expect(page.getByRole("heading", { name: "Louise L Czako", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("source-name conflict");
  await expect(page.locator("main")).toContainText("Louis L. Czako");
  await expect(page.locator("main")).toContainText("Review Box 162");
});
