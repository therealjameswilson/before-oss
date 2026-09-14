import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 452 confirms four identifier-matched enlisted records without inventing employers", async () => {
  const expected = [
    ["f83974d4-b345-5b59-a600-afa15f861e9e", "Edward A Condon", "student", "Student"],
    ["680a7cd5-df36-549c-b6ae-e92488d17b55", "William A Condon", "unknown", "Operators, construction machinery"],
    ["0e4fffa3-2043-502f-bb32-30f7eeb38c79", "Charles W Cone", "student", "Student"],
    ["bb558e11-f0e8-58ad-ae78-a7e9e6da4aaa", "Edward T Cone", "student", "Undergraduate and graduate student in music"],
  ];

  for (const [id, name, relationship, roleOrOccupation] of expected) {
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
        relationship_type: relationship,
        immediate_pre_oss: false,
        last_civilian_pre_service: false,
        claim_confidence: relationship === "student" && name === "Edward T Cone" ? "high" : "medium",
      }),
    );
    expect(
      person.other_pre_oss_affiliations.some(
        (affiliation: { role_title?: string | null; occupation?: string | null }) =>
          affiliation.role_title === roleOrOccupation || affiliation.occupation === roleOrOccupation,
      ),
    ).toBe(true);
  }
});

test("Batch 452 documents Edward Toner Cone's Princeton study separately from employment", async ({ page }) => {
  const edward = profile("bb558e11-f0e8-58ad-ae78-a7e9e6da4aaa");
  expect(edward.name_variants).toContain("Edward Toner Cone");
  expect(edward.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Princeton University",
      organization_name_as_found: "Princeton",
      role_title: "Undergraduate and graduate student in music",
      relationship_type: "student",
      end_date: "1942",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  );
  expect(edward.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      occupation: "Musicians and teachers of music",
      relationship_type: "unknown",
      end_date: "1942-10-14",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${edward.person_id}/`);
  await expect(page.getByRole("heading", { name: "Edward T Cone", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Edward Toner Cone");
  await expect(page.locator("main")).toContainText("Princeton University");
  await expect(page.locator("main")).toContainText("Undergraduate and graduate student in music");
  await expect(page.locator("main")).toContainText("Musicians and teachers of music");
  await expect(page.locator("main")).toContainText(
    "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 452 preserves all ten printed rows, boxes and masked identifier forms", async () => {
  const expected = [
    ["f83974d4-b345-5b59-a600-afa15f861e9e", "Edward A Condon", "35cef676-1321-508b-8b06-83f36e87b121", "137", true],
    ["988d541b-9b5a-5b6a-889e-a081e7f3ea82", "Jack G Condon", "cd6e766c-5696-579f-8cf9-444475999b32", "137", true],
    ["989e84b8-5283-5652-9e96-7c4bfbd74592", "Richard S Condon", "63b72a24-228c-5082-82d3-21091ec266df", "137", true],
    ["680a7cd5-df36-549c-b6ae-e92488d17b55", "William A Condon", "1dceb812-986a-50a9-b731-e472d636a5a4", "137", true],
    ["0e4fffa3-2043-502f-bb32-30f7eeb38c79", "Charles W Cone", "2b9be4a8-67d4-574c-a3ce-aee05ffa927b", "137", true],
    ["bb558e11-f0e8-58ad-ae78-a7e9e6da4aaa", "Edward T Cone", "863096d0-809f-5d9e-9bbd-65b0ea5235f2", "138", true],
    ["5452b4fa-cffd-5541-b4b1-022ebe48770d", "Alma P Coneby", "1a0537bb-87e0-54d6-978f-55dd83bfd0a7", "138", false],
    ["5e7905c6-6565-5f51-8b37-03e0f57205a1", "Lucien E Conein", "245e5283-d3b7-5d93-b9eb-c85bf836ae81", "138", false],
    ["963d955d-b76a-5694-996e-8afbabe87922", "Leonard R Coneley", "f586980c-43a9-5265-973d-9f278be8f852", "138", false],
    ["2edf51e5-1e6e-5a6b-b45d-18422496dfc1", "William J Coneys", "ebf8b80e-a00a-5403-9e15-8b9cbb02f9b9", "138", false],
  ];

  for (const [id, name, sourceRecordId, box, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      box,
      notes_as_indexed: null,
      archive_location: "230/86/29/01",
      pdf_page: 89,
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

test("Batch 452 leaves five unresolved profiles free of unsupported claims", async ({ page }) => {
  const unresolved = [
    ["988d541b-9b5a-5b6a-889e-a081e7f3ea82", "Jack G Condon", "needs_identity_review"],
    ["989e84b8-5283-5652-9e96-7c4bfbd74592", "Richard S Condon", "needs_identity_review"],
    ["5452b4fa-cffd-5541-b4b1-022ebe48770d", "Alma P Coneby", "requires_archival_review"],
    ["963d955d-b76a-5694-996e-8afbabe87922", "Leonard R Coneley", "requires_archival_review"],
    ["2edf51e5-1e6e-5a6b-b45d-18422496dfc1", "William J Coneys", "needs_identity_review"],
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

  const william = profile("2edf51e5-1e6e-5a6b-b45d-18422496dfc1");
  await page.goto(`./people/${william.person_id}/`);
  await expect(page.getByRole("heading", { name: "William J Coneys", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("damaged");
  await expect(page.locator("main")).toContainText("Review Box 138");
  await expect(page.locator("main")).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed",
  );
});

test("Batch 452 revalidates Lucien Conein without duplicating existing claims", async ({ page }) => {
  const lucien = profile("5e7905c6-6565-5f51-8b37-03e0f57205a1");
  expect(lucien).toMatchObject({
    display_name: "Lucien E Conein",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(lucien.claims).toHaveLength(5);
  expect(lucien.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(lucien.last_civilian_pre_service).toHaveLength(1);
  expect(lucien.other_pre_oss_affiliations).toHaveLength(2);
  expect(lucien.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Unidentified Kansas City printer",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  );

  await page.goto(`./people/${lucien.person_id}/`);
  await expect(page.getByRole("heading", { name: "Lucien E Conein", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Unidentified Kansas City printer");
  await expect(page.locator("main")).toContainText("3rd Student Training Regiment");
});
