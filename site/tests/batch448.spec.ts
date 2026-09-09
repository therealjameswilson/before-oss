import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 448 publishes two named employers with distinct temporal meanings", async ({ page }) => {
  const frances = profile("7aebe016-265f-59d0-8d94-211d9ec878af");
  expect(frances).toMatchObject({
    display_name: "Frances R Colosimo",
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "documented_prewar_employer_found",
  });
  expect(frances.immediate_pre_oss_affiliations).toEqual([]);
  expect(frances.last_civilian_pre_service).toEqual([]);
  expect(frances.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "American Bottlers of Carbonated Beverages",
      organization_name_as_found: "American Bottlers of Carbonated Beverages",
      role_title: "research technician",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      identity_confidence: "high_confidence",
      claim_confidence: "high",
    }),
  );

  await page.goto(`./people/${frances.person_id}/`);
  await expect(page.getByRole("heading", { name: "Frances R Colosimo", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("American Bottlers of Carbonated Beverages");
  await expect(page.locator("main")).toContainText("research technician");
  await expect(page.locator("main")).toContainText("does not explicitly call it her immediately preceding OSS role");

  const constance = profile("580abbf6-f2f9-506f-b091-1c075d5ba8ef");
  expect(constance).toMatchObject({
    display_name: "Constance Colt",
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(constance.name_variants).toContain("Constance Colt Bassett");
  expect(constance.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Free French",
      organization_name_as_found: "the Free French",
      role_title: null,
      occupation: null,
      relationship_type: "employment",
      immediate_pre_oss: true,
      last_civilian_pre_service: true,
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  );
  expect(constance.last_civilian_pre_service).toHaveLength(1);

  await page.goto(`./people/${constance.person_id}/`);
  await expect(page.getByRole("heading", { name: "Constance Colt", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Free French");
  await expect(page.locator("main")).toContainText("Immediately before moving to Washington for OSS");
  await expect(page.locator("main")).toContainText("exact dates and a formal title are not given");
});

test("Batch 448 confirms Joseph Comastra's Army-entry occupation without inventing an employer", async ({ page }) => {
  const joseph = profile("f00238d0-f2f2-5dfd-9aa4-a4b91b177b35");
  expect(joseph).toMatchObject({
    display_name: "Joseph S Comastra",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(joseph.immediate_pre_oss_affiliations).toEqual([]);
  expect(joseph.last_civilian_pre_service).toEqual([]);
  expect(joseph.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Chauffeurs and drivers, bus, taxi, truck, and tractor",
      relationship_type: "unknown",
      end_date: "1941-01-16",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${joseph.person_id}/`);
  await expect(page.getByRole("heading", { name: "Joseph S Comastra", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Chauffeurs and drivers, bus, taxi, truck, and tractor");
  await expect(page.locator("main")).toContainText("no employer");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 448 keeps Harold's identity qualified and preserves all printed records safely", async ({ page }) => {
  const expected = [
    ["dd6ce9da-5a46-5a47-b9a1-7d34ea7db1a3", "Lola Colonel", "be870590-0195-55a1-ba99-c6982c1a174a", "136", 0],
    ["7aebe016-265f-59d0-8d94-211d9ec878af", "Frances R Colosimo", "938624bc-fa08-58bd-9c6c-202d796dc474", "136", 0],
    ["00fe1d19-198f-598b-830a-dfd37a46a12f", "Edward A Colson", "bff407da-6fcd-5b45-b7ad-d3093c2a59d7", "136", 0],
    ["596946e0-162f-5dc8-93b8-ce1df6df2f3e", "Robert C Colson", "f7fe717f-0066-50e9-b178-d6472efa695f", "136", 7],
    ["580abbf6-f2f9-506f-b091-1c075d5ba8ef", "Constance Colt", "66d526fe-83ec-5d2e-bc51-5e5b7becace7", "136", 0],
    ["46062dcb-0685-58df-bd51-74e7f87a7699", "Elizabeth V Colt", "6b732d3b-a98d-58b1-855d-ae2890628653", "136", 0],
    ["222d3d9a-a206-5f42-92fe-d9c4e5db6232", "Gertrude L Colvin", "5b05f090-5d8f-578e-a0f1-d141965469d5", "136", 0],
    ["e2d88789-b88b-54cd-9475-dcb74148a638", "Harold L Colvocoresses", "f0eb828a-d80d-5ba4-bc8f-442444434537", "136", 0],
    ["f00238d0-f2f2-5dfd-9aa4-a4b91b177b35", "Joseph S Comastra", "60e87d63-3897-5ec4-beb1-258844791b77", "136", 8],
    ["bec3acf5-804f-59bc-9013-5f7893a7462e", "Don P Combe", "bc3037ec-73c8-58c0-b861-1ccaea97f9d7", "141", 7],
  ];

  for (const [id, name, sourceRecordId, box, serialLength] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      box,
      archive_location: "230/86/29/01",
      pdf_page: 88,
    });
    if (serialLength) {
      expect(person.source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
    } else {
      expect(person.source_records[0].serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  const harold = profile("e2d88789-b88b-54cd-9475-dcb74148a638");
  expect(harold).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
  });
  expect(harold.name_variants).toContain("Harold Lee Colvocoresses");
  expect(harold.immediate_pre_oss_affiliations).toEqual([]);
  expect(harold.last_civilian_pre_service).toEqual([]);
  expect(harold.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${harold.person_id}/`);
  await expect(page.locator("main")).toContainText("probably, but not conclusively");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.locator("main")).toContainText("Review Box 136");

  for (const id of [
    "dd6ce9da-5a46-5a47-b9a1-7d34ea7db1a3",
    "00fe1d19-198f-598b-830a-dfd37a46a12f",
    "596946e0-162f-5dc8-93b8-ce1df6df2f3e",
    "46062dcb-0685-58df-bd51-74e7f87a7699",
    "222d3d9a-a206-5f42-92fe-d9c4e5db6232",
    "bec3acf5-804f-59bc-9013-5f7893a7462e",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const robert = profile("596946e0-162f-5dc8-93b8-ce1df6df2f3e");
  await page.goto(`./people/${robert.person_id}/`);
  await expect(page.locator("main")).toContainText("seven-digit printed value");
  await expect(page.locator("main")).toContainText("Four exact-name Army rows");

  const don = profile("bec3acf5-804f-59bc-9013-5f7893a7462e");
  await page.goto(`./people/${don.person_id}/`);
  await expect(page.locator("main")).toContainText("seven-digit printed value");
  await expect(page.locator("main")).toContainText("Review Box 141");
});
