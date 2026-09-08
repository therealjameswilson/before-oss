import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 431 publishes Army occupations without inventing employers", async ({ page }) => {
  const expected = [
    ["b276a591-6e3e-548c-8f56-da7292edb26e", "Howard J Clifton", "Sales clerks"],
    ["32b801a6-fc2f-5445-9c70-1d70d52ed078", "William R Clifton", "Attendants, recreation and amusement, n.e.c."],
    ["7f97dcb9-5681-5df6-9a83-bad9c4c69994", "Sheldon R Cline", "Salesmen, to consumers"],
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

test("Batch 431 keeps Ray Cline's fellowship and government assignment out of employer analytics", async ({ page }) => {
  const ray = profile("d8754b27-3c32-5445-a5fe-063299aa869c");
  expect(ray).toMatchObject({
    display_name: "Ray S Cline",
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    research_attempt_count: 2,
  });
  expect(ray.last_civilian_pre_service).toEqual([]);
  expect(ray.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Department of the Navy",
      role_title: "cryptanalyst",
      relationship_type: "government_assignment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(ray.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Harvard Society of Fellows",
      role_title: "junior fellow",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );

  await page.goto(`./people/${ray.person_id}/`);
  await expect(page.getByRole("heading", { name: "Ray S Cline", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Department of the Navy");
  await expect(page.locator("main")).toContainText("cryptanalyst");
  await expect(page.locator("main")).toContainText("Harvard Society of Fellows");
  await expect(page.locator("main")).toContainText("junior fellow");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 431 preserves Dean Cline's index classification and qualifies DeWitt Clinton", async ({ page }) => {
  const dean = profile("26de762e-5fc9-50c4-90cc-afd85ff52b70");
  expect(dean).toMatchObject({
    display_name: "Dean A Cline",
    identity_status: "unresolved",
    personnel_category: "enlisted_naval_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(dean.source_records[0]).toMatchObject({
    rank_as_indexed: "Sp 2/C",
    notes_as_indexed: "Navy",
  });
  expect(dean.immediate_pre_oss_affiliations).toEqual([]);
  expect(dean.last_civilian_pre_service).toEqual([]);

  await page.goto(`./people/${dean.person_id}/`);
  await expect(page.getByRole("heading", { name: "Dean A Cline", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Sp 2/C");
  await expect(page.locator("main")).toContainText("Navy");

  const dewitt = profile("c2ae1476-e9fe-5555-93eb-2923b3f4a160");
  expect(dewitt).toMatchObject({
    display_name: "DeWitt Clinton",
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    research_status: "requires_archival_review",
  });
  expect(dewitt.immediate_pre_oss_affiliations).toEqual([]);
  expect(dewitt.last_civilian_pre_service).toEqual([]);
  expect(dewitt.other_pre_oss_affiliations).toEqual([]);
  expect(dewitt.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
      match_notes: expect.stringContaining("DeWitt Clinton Poole"),
    }),
  );

  await page.goto(`./people/${dewitt.person_id}/`);
  await expect(page.getByRole("heading", { name: "DeWitt Clinton", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("probably corresponds");
  await expect(page.getByRole("link", { name: "General William J. Donovan: Selected OSS Documents, 1941-1945, Microfilm Roll List and Index" }).first()).toBeVisible();
});

test("Batch 431 preserves every page 84 index row and masks private identifiers", async ({ page }) => {
  const expected = [
    ["b276a591-6e3e-548c-8f56-da7292edb26e", "Howard J Clifton", "1bf44128-3e9b-5f1d-afb1-591d109a80e9", "confirmed", "occupation_only_found", "129"],
    ["bf96d9a0-e636-5e4e-9961-31b4215b58d9", "Mary F Clifton", "c55730d9-c2ed-552f-ab29-4a0554429f80", "unresolved", "requires_archival_review", "129"],
    ["32b801a6-fc2f-5445-9c70-1d70d52ed078", "William R Clifton", "d9289259-3c60-5d95-bfa2-d86794b4a6e8", "confirmed", "occupation_only_found", "129"],
    ["c51e6cb6-3682-511e-9284-b96b4a7435a1", "A C Cline", "f290490c-8d2c-5d1b-823a-155ed158fa3e", "unresolved", "requires_archival_review", "129"],
    ["26de762e-5fc9-50c4-90cc-afd85ff52b70", "Dean A Cline", "b2946e32-f32b-581a-9646-6784d0e62f9d", "unresolved", "requires_archival_review", "129"],
    ["f0f5a717-5280-57da-9279-d73049c3ed9b", "Jeraldine E Cline", "9b27a426-9019-570d-b819-30541001f36e", "unresolved", "requires_archival_review", "129"],
    ["d8754b27-3c32-5445-a5fe-063299aa869c", "Ray S Cline", "17fc1ac6-4676-5e13-9c86-482b85fcc5e7", "high_confidence", "requires_archival_review", "129"],
    ["7f97dcb9-5681-5df6-9a83-bad9c4c69994", "Sheldon R Cline", "afc846a7-d650-5fe9-8576-093480bdf4eb", "confirmed", "occupation_only_found", "130"],
    ["8cc50527-5026-5198-b1b8-0be66dd09be2", "Walter B Cline", "c70553f0-666e-52e1-8e25-c8dff98efb75", "unresolved", "requires_archival_review", "130"],
    ["c2ae1476-e9fe-5555-93eb-2923b3f4a160", "DeWitt Clinton", "fd5d2c75-7d44-540b-9c64-896249047755", "probable", "requires_archival_review", "130"],
  ];

  for (const [id, name, sourceRecordId, identityStatus, researchStatus, box] of expected) {
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
    });
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );

  }

  for (const id of [
    "b276a591-6e3e-548c-8f56-da7292edb26e",
    "32b801a6-fc2f-5445-9c70-1d70d52ed078",
    "7f97dcb9-5681-5df6-9a83-bad9c4c69994",
  ]) {
    expect(profile(id).source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
  }

  await page.goto("./people/?q=Jeraldine%20E%20Cline");
  await expect(page.getByRole("link", { name: "Jeraldine E Cline", exact: true })).toBeVisible();
});
