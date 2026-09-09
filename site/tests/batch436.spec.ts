import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 436 publishes John Coddington's earlier Harvard employment without calling it immediate", async ({ page }) => {
  const john = profile("a2066c13-67d5-5418-8b75-6ab93f10e8d1");
  expect(john).toMatchObject({
    display_name: "John I Coddington",
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
  });
  expect(john.immediate_pre_oss_affiliations).toEqual([]);
  expect(john.last_civilian_pre_service).toEqual([]);
  expect(john.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Harvard University",
      organization_name_as_found: "Harvard History Department",
      relationship_type: "employment",
      start_date: "1930",
      end_date: "1936",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${john.person_id}/`);
  await expect(page.getByRole("heading", { name: "John I Coddington", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Harvard History Department");
  await expect(page.locator("main")).toContainText("Research Specialist");
  await expect(page.locator("main")).toContainText("not the immediate predecessor");
});

test("Batch 436 keeps four identifier-backed Army categories separate from employers", async ({ page }) => {
  const expected = [
    ["ff9dec18-709a-5d03-b1a8-cdbc0fc88762", "Nick J Cocoris", "General industry clerks", "1942-04-04", "unknown"],
    ["db3ab994-11d4-5b6c-b8d4-e2ee06e75dca", "Avery L Coddens", "Students", "1943-04-26", "student"],
    ["94612448-1e57-544c-a26a-524b6a20d4b4", "Ernest J Codekas", "Foremen, manufacturing", "1942-12-04", "unknown"],
    ["ce8949bf-8356-5ea6-9505-f0d9717506c1", "George N Codino", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "1943-03-13", "unknown"],
  ];

  for (const [id, name, occupation, endDate, relationshipType] of expected) {
    const person = profile(id);
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
        relationship_type: relationshipType,
        end_date: endDate,
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    );
  }

  const avery = profile("db3ab994-11d4-5b6c-b8d4-e2ee06e75dca");
  await page.goto(`./people/${avery.person_id}/`);
  await expect(page.getByRole("heading", { name: "Avery L Coddens", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("student");
  await expect(page.locator("main")).toContainText("no school or employer is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 436 preserves duplicate clusters and rejects Chester Cody's leading-zero Army candidate", async ({ page }) => {
  const williamOne = profile("d1c51632-4aca-5d19-af0c-487ce2feedc0");
  const williamTwo = profile("bd36d4ff-c5f7-574e-adfc-20454703ace2");
  expect(williamOne.person_id).not.toBe(williamTwo.person_id);
  expect(williamOne.possible_duplicate_group).toMatch(/^duplicate-[a-f0-9]{12}$/);
  expect(williamTwo.possible_duplicate_group).toBe(williamOne.possible_duplicate_group);
  expect(williamOne.research_status).toBe("requires_archival_review");
  expect(williamTwo.research_status).toBe("requires_archival_review");

  const ernestConfirmed = profile("94612448-1e57-544c-a26a-524b6a20d4b4");
  const ernestUnresolved = profile("c4599e01-733d-53c8-8cdd-182d80e90998");
  expect(ernestConfirmed.person_id).not.toBe(ernestUnresolved.person_id);
  expect(ernestConfirmed.possible_duplicate_group).toMatch(/^duplicate-[a-f0-9]{12}$/);
  expect(ernestUnresolved.possible_duplicate_group).toBe(ernestConfirmed.possible_duplicate_group);
  expect(ernestUnresolved.identity_status).toBe("unresolved");
  expect(ernestUnresolved.other_pre_oss_affiliations).toEqual([]);

  const chester = profile("fd97d7d6-3846-5b92-9db4-54cbc22d4a48");
  expect(chester).toMatchObject({
    display_name: "Chester Cody",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(chester.immediate_pre_oss_affiliations).toEqual([]);
  expect(chester.last_civilian_pre_service).toEqual([]);
  expect(chester.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${chester.person_id}/`);
  await expect(page.getByRole("heading", { name: "Chester Cody", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Kachin Rangers");
  await expect(page.locator("main")).toContainText("not padded to select a zero-prefixed Army row");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 436 preserves all ten source rows while masking private identifiers", async () => {
  const expected = [
    ["ff9dec18-709a-5d03-b1a8-cdbc0fc88762", "Nick J Cocoris", "966bc9c1-8048-5009-9c16-f3458d5f7245", null, "131", true],
    ["d1c51632-4aca-5d19-af0c-487ce2feedc0", "William S Codd", "0dd4c33c-3da6-599f-a555-bb4587eb6c8b", null, "131", false],
    ["bd36d4ff-c5f7-574e-adfc-20454703ace2", "William S Codd", "c8d48359-d673-5394-8d2b-aabf91f8f079", null, "131", false],
    ["db3ab994-11d4-5b6c-b8d4-e2ee06e75dca", "Avery L Coddens", "b8fc23a6-c595-58c2-9bea-be401f2a1ff7", null, "131", true],
    ["a2066c13-67d5-5418-8b75-6ab93f10e8d1", "John I Coddington", "c46417dc-2833-58c3-9fc5-37d9eae68f5f", null, "132", false],
    ["94612448-1e57-544c-a26a-524b6a20d4b4", "Ernest J Codekas", "582cf4a8-16e7-5f65-8beb-3fd9988bdd53", null, "132", true],
    ["c4599e01-733d-53c8-8cdd-182d80e90998", "Ernest J Codekas", "95bd4df7-cd7d-5850-9043-d657a771987a", null, "131", false],
    ["ce8949bf-8356-5ea6-9505-f0d9717506c1", "George N Codino", "02254c20-f517-53b7-b041-97db9571ad69", null, "132", true],
    ["ac733f29-73c7-5ee1-957e-f52f9ffb7538", "Eliot Codman", "b6be7396-4219-59a3-bdb8-3ffa02a30e86", null, "132", false],
    ["fd97d7d6-3846-5b92-9db4-54cbc22d4a48", "Chester Cody", "3ebd9078-8f23-52b2-98eb-ed452f00ffc7", "Sgt", "132", true],
  ];

  for (const [id, name, sourceRecordId, rank, box, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 85,
      box,
      archive_location: "230/86/28/07",
      rank_as_indexed: rank,
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
