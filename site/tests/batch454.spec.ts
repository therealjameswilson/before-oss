import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 454 preserves all ten printed rows and masks every private identifier", async () => {
  const expected = [
    ["c4e92baf-05f9-5ea9-91ce-a4681aa117bf", "Hugh R Conklin", "2d5aeea1-e8e1-58c0-808c-3db30c1d8b2e", null, "••••3730"],
    ["602399be-ce74-51e1-bd22-05405f522c49", "Mary P Conklin", "9a940ee0-2a2d-5e02-a93f-ef027f2f2621", null, null],
    ["7a99258e-5297-5731-b0c7-7b62d71a7184", "Arthur P Conkling", "07867254-d38c-518f-88c2-5a07573968c8", null, "••••0892"],
    ["3b9e5807-1db0-53cb-88da-30c3403a74f5", "Edward J Conley", "3617d1e0-8d52-558c-aad5-4fffb67ef879", null, "••••4101"],
    ["dfad9c2b-d359-580e-94af-0cd9f6e85087", "John H Conley", "3e27c506-6318-5638-8f4a-80976d633115", null, "••••4750"],
    ["319d208e-df7b-58c9-884f-8af8d46c4d6a", "Leonard R Conley", "d9403e7d-0ec2-5561-977a-a3b4919071a8", null, "••••9859"],
    ["4b513cf8-07ce-52aa-9bdd-ffe9202c7048", "Lloyd B Conley", "f2c43cc8-9bf3-5d8b-8bde-a216b9ffd137", null, "••••0403"],
    ["570630cb-4d24-56ab-91f5-700d25b4247a", "Phillip J Conley", "4a6f7579-7875-5c33-b28c-ca92cf0980d7", "Lt Comd", null],
    ["f0598703-31dd-50b1-ad92-46e9c02d70dd", "Robert M Conley", "46ab2769-3195-5ee1-8514-97fa48222c8b", null, "••••5479"],
    ["8af35ff9-a371-5db6-9bf2-fe76a4c83bb0", "Charles J Conlon", "a365f24d-bf24-55e6-93d7-52e00931709c", null, "••••3617"],
  ];

  for (const [id, name, sourceRecordId, rank, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      rank_as_indexed: rank,
      serial_masked: serial,
      box: "138",
      archive_location: "230/86/29/01",
      pdf_page: 89,
    });
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 454 publishes Lloyd B Conley's date-bounded category without inventing an employer", async ({ page }) => {
  const lloyd = profile("4b513cf8-07ce-52aa-9bdd-ffe9202c7048");
  expect(lloyd).toMatchObject({
    display_name: "Lloyd B Conley",
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(lloyd.immediate_pre_oss_affiliations).toEqual([]);
  expect(lloyd.last_civilian_pre_service).toEqual([]);
  expect(lloyd.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      occupation: "Salesmen and sales agents, except to consumers",
      relationship_type: "unknown",
      end_date: "1943-01-14",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
      immediate_pre_oss: false,
      last_civilian_pre_service: false,
    }),
  );
  expect(lloyd.claims).toHaveLength(2);

  await page.goto(`./people/${lloyd.person_id}/`);
  await expect(page.getByRole("heading", { name: "Lloyd B Conley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Salesmen and sales agents, except to consumers");
  await expect(page.locator("main")).toContainText(/no employer or product is identified/i);
  await expect(page.locator("main")).toContainText(
    "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 454 keeps Robert M Conley's student status separate from employment", async ({ page }) => {
  const robert = profile("f0598703-31dd-50b1-ad92-46e9c02d70dd");
  expect(robert).toMatchObject({
    display_name: "Robert M Conley",
    identity_status: "confirmed",
    research_status: "occupation_only_found",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(robert.immediate_pre_oss_affiliations).toEqual([]);
  expect(robert.last_civilian_pre_service).toEqual([]);
  expect(robert.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: null,
      role_title: "Student",
      occupation: "Students",
      relationship_type: "student",
      end_date: "1943-07-06",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${robert.person_id}/`);
  await expect(page.getByRole("heading", { name: "Robert M Conley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("student status on 6 July 1943");
  await expect(page.locator("main")).toContainText(/no school or employer is identified/i);
  await expect(page.locator("main")).toContainText(
    "Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 454 exposes both identifier conflicts without assigning Army occupations", async ({ page }) => {
  const expected = [
    ["319d208e-df7b-58c9-884f-8af8d46c4d6a", "Leonard R Conley"],
    ["8af35ff9-a371-5db6-9bf2-fe76a4c83bb0", "Charles J Conlon"],
  ];

  for (const [id, name] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "conflicting",
      research_status: "conflicting_sources",
    });
    expect(person.claims).toHaveLength(1);
    expect(person.claims[0]).toMatchObject({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);

    await page.goto(`./people/${person.person_id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(
      "resolves to an official Army record for a different person",
    );
    await expect(page.locator("main")).toContainText("conflicting");
  }
});

test("Batch 454 preserves Phillip J Conley's spelling and naval rank while leaving unresolved people claim-free", async ({ page }) => {
  const phillip = profile("570630cb-4d24-56ab-91f5-700d25b4247a");
  expect(phillip).toMatchObject({
    display_name: "Phillip J Conley",
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
  });
  expect(phillip.source_records[0].rank_as_indexed).toBe("Lt Comd");

  const unresolved = [
    "c4e92baf-05f9-5ea9-91ce-a4681aa117bf",
    "602399be-ce74-51e1-bd22-05405f522c49",
    "7a99258e-5297-5731-b0c7-7b62d71a7184",
    "3b9e5807-1db0-53cb-88da-30c3403a74f5",
    "dfad9c2b-d359-580e-94af-0cd9f6e85087",
    "570630cb-4d24-56ab-91f5-700d25b4247a",
  ];
  for (const id of unresolved) {
    const person = profile(id);
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.next_action).toContain("Box 138");
  }

  await page.goto(`./people/${phillip.person_id}/`);
  await expect(page.getByRole("heading", { name: "Phillip J Conley", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Lt Comd");
  await expect(page.locator("main")).toContainText(/commissioned naval officer/i);
  await expect(page.locator("main")).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed",
  );
});
