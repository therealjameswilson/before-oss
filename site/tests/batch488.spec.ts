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
  ["05134457-f13a-5ccc-9534-ee07888b9495", "Pierre Crabites", "de845ba0-b24b-550c-8d68-91630725206c", 96, false],
  ["3978aaaa-68fc-5569-9c7a-dff184d191c8", "Sam Crabtree", "dd52cbde-338c-5a3f-9351-44c7d9ef3d2b", 96, true],
  ["ee767ef8-bf5a-5b41-80ff-4990c3684aed", "Pauline G Craft", "5fe15e8f-36f3-5857-bd87-f002d0ae8368", 96, true],
  ["81486989-3d69-50dd-8edd-da4bf9d34842", "William S Craft", "3c3d2c75-4fb6-504f-a2b6-15dc61ff9608", 97, true],
  ["16259c86-c7c3-5c78-bcfb-411e2558ca65", "Cecilia A Crafts", "dec78d89-2e86-5c91-8ae6-1e66a9ae8450", 97, true],
  ["d6f34acd-8b24-5894-963d-39a0f17e3009", "Alan B Cragin", "55e5d011-fcb4-5b77-a87e-63ee71cda79e", 97, true],
  ["05da8907-ae2d-5027-ba78-3723f19e1aaa", "Martha N Cragin", "ff3c0bb2-adee-52f1-b6e1-df9174fd6fcb", 97, false],
  ["5aae898a-174c-557e-99c1-321e76d314aa", "Dorothy P Craig", "18869e2f-32ca-5d2d-a95f-8bc7bd4cc145", 97, false],
  ["fb9b02f9-9dfb-5965-8514-fa5b73e3b2c9", "Gordon A Craig", "8047f9e3-425a-52d3-bc5b-5d3e1c6d5ea7", 97, false],
  ["425dd323-dc16-5cb9-a89f-8aba4448e86c", "Margaret Craig", "f9b79815-93ed-56b1-a491-cac9e0547074", 97, false],
] as const;

test("Batch 488 preserves all ten rows across pages 96 and 97 and masks identifiers", () => {
  for (const [id, name, sourceRecordId, pdfPage, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    const sourceRecord = person.source_records.find(
      (record: { source_record_id: string }) => record.source_record_id === sourceRecordId,
    );
    expect(sourceRecord).toMatchObject({
      box: "151",
      archive_location: "230/86/29/03",
      pdf_page: pdfPage,
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

test("Batch 488 publishes Pierre Crabites's court service only as earlier prewar affiliation", () => {
  const pierre = profile("05134457-f13a-5ccc-9534-ee07888b9495");
  expect(pierre).toMatchObject({
    display_name: "Pierre Crabites",
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
  });
  expect(pierre.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Mixed Courts of Egypt",
      role_title: "American judge and member",
      relationship_type: "government_assignment",
      start_date: "1911",
      end_date: "1936",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );
  expect(pierre.claims).toHaveLength(2);
});

test("Batch 488 confirms William Craft and Alan Cragin without inventing occupations", () => {
  for (const id of [
    "81486989-3d69-50dd-8edd-da4bf9d34842",
    "d6f34acd-8b24-5894-963d-39a0f17e3009",
  ]) {
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
    expect(person.claims).toHaveLength(1);
    expect(person.claims[0].claim_type).toBe("identity");
  }
});

test("Batch 488 exposes Pauline Craft's identifier conflict without transferring Army attributes", () => {
  const pauline = profile("ee767ef8-bf5a-5b41-80ff-4990c3684aed");
  expect(pauline).toMatchObject({
    display_name: "Pauline G Craft",
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(pauline.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  );
});

test("Batch 488 retains five unsupported people as unresolved archival cases", () => {
  for (const id of [
    "3978aaaa-68fc-5569-9c7a-dff184d191c8",
    "16259c86-c7c3-5c78-bcfb-411e2558ca65",
    "05da8907-ae2d-5027-ba78-3723f19e1aaa",
    "5aae898a-174c-557e-99c1-321e76d314aa",
    "425dd323-dc16-5cb9-a89f-8aba4448e86c",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }
});

test("Batch 488 profiles and coverage render the reviewed outcomes", async ({ page }) => {
  expect(stats.research_attempted_people).toBe(4648);
  expect(stats.verified_affiliation_people).toBe(533);
  expect(stats.verified_employer_people).toBe(236);
  expect(stats.archival_review_assessed_people).toBe(4603);

  const gordon = profile("fb9b02f9-9dfb-5965-8514-fa5b73e3b2c9");
  expect(gordon).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(gordon.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Princeton University",
      relationship_type: "student",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/05134457-f13a-5ccc-9534-ee07888b9495/");
  await expect(page.getByRole("heading", { name: "Pierre Crabites", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Mixed Courts of Egypt");
  await expect(page.locator("main")).toContainText("American judge and member");
  await expect(page.locator("main")).toContainText("Foreign Service Journal");

  await page.goto("./people/ee767ef8-bf5a-5b41-80ff-4990c3684aed/");
  await expect(page.getByRole("heading", { name: "Pauline G Craft", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("conflict");
  await expect(page.locator("main")).toContainText("Paul G Craft");
});
