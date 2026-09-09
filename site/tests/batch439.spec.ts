import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 439 keeps three identifier-backed Army occupations separate from employers", async ({ page }) => {
  const expected = [
    ["e710e105-a184-50ca-8e06-133274b460ca", "Noah J Cohen", "Sales clerks", "1941-06-03"],
    ["73105eec-b393-5333-b8ec-da5f0832486a", "Sidney L Cohen", "Food products producing occupations, miscellaneous", "1942-10-24"],
    ["96bb4e98-fef0-5d31-a5fd-2fa21875f742", "Carl M Cohn", "Foremen, n.e.c.", "1942-11-03"],
  ];

  for (const [id, name, occupation, endDate] of expected) {
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
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "temporal_relation_uncertain",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );
  }

  const sidney = profile("73105eec-b393-5333-b8ec-da5f0832486a");
  await page.goto(`./people/${sidney.person_id}/`);
  await expect(page.getByRole("heading", { name: "Sidney L Cohen", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Food products producing occupations, miscellaneous");
  await expect(page.locator("main")).toContainText("no employer or exact trade is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 439 qualifies Mabel and Robert Cohen rather than promoting common-name matches", async ({ page }) => {
  const mabel = profile("d52905c0-3de5-5cd0-b015-fa4ec9398766");
  expect(mabel).toMatchObject({
    display_name: "Mabel Cohen",
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
  });
  expect(mabel.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Chestnut Lodge Sanitarium",
      organization_name_as_found: "Chestnut Lodge Sanitarium, Rockville, Md.",
      occupation: "physician and psychiatrist",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );
  expect(mabel.last_civilian_pre_service[0].affiliation_id).toBe(
    mabel.immediate_pre_oss_affiliations[0].affiliation_id,
  );

  const robert = profile("10e8e445-dd65-59e6-8a13-a0c4f7e4cf28");
  expect(robert).toMatchObject({
    display_name: "Robert A Cohen",
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "documented_prewar_employer_found",
  });
  expect(robert.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Sheppard-Pratt Hospital",
      organization_name_as_found: "Sheppard-Pratt Hospital, Towson, Md.",
      role_title: "physician",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      identity_confidence: "probable",
      claim_confidence: "medium",
    }),
  );
  expect(robert.last_civilian_pre_service[0].affiliation_id).toBe(
    robert.immediate_pre_oss_affiliations[0].affiliation_id,
  );

  await page.goto(`./people/${mabel.person_id}/`);
  await expect(page.getByRole("heading", { name: "Mabel Cohen", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Mabel Blake Cohen");
  await expect(page.locator("main")).toContainText("Chestnut Lodge Sanitarium");
  await expect(page.locator("main")).toContainText("medium explicit immediate");

  await page.goto(`./people/${robert.person_id}/`);
  await expect(page.getByRole("heading", { name: "Robert A Cohen", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Sheppard-Pratt Hospital");
  await expect(page.locator("main")).toContainText("physician");
  await expect(page.locator("main")).toContainText("probable");
});

test("Batch 439 separates Theodore Cohen's employer from Marcel Cohen's temporal-uncertain occupation", async ({ page }) => {
  const theodore = profile("05c008ff-79b7-58e8-99ca-4528a39b5f54");
  expect(theodore).toMatchObject({
    display_name: "Theodore Cohen",
    identity_status: "probable",
    research_status: "documented_prewar_employer_found",
  });
  expect(theodore.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "City College of New York",
      role_title: "history teacher",
      relationship_type: "employment",
      start_date: "1939",
      end_date: "1940",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "probable",
      claim_confidence: "medium",
    }),
  );
  expect(theodore.last_civilian_pre_service[0].affiliation_id).toBe(
    theodore.immediate_pre_oss_affiliations[0].affiliation_id,
  );

  const marcel = profile("200fc5df-df5e-5898-962e-63c49a825356");
  expect(marcel).toMatchObject({
    display_name: "Marcel Cohen",
    identity_status: "probable",
    research_status: "occupation_only_found",
  });
  expect(marcel.immediate_pre_oss_affiliations).toEqual([]);
  expect(marcel.last_civilian_pre_service).toEqual([]);
  expect(marcel.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "film editor and director",
      relationship_type: "unknown",
      start_date: "1943",
      end_date: "1944",
      temporal_basis: "temporal_relation_uncertain",
      identity_confidence: "probable",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${theodore.person_id}/`);
  await expect(page.getByRole("heading", { name: "Theodore Cohen", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("City College of New York");
  await expect(page.locator("main")).toContainText("history teacher");

  await page.goto(`./people/${marcel.person_id}/`);
  await expect(page.getByRole("heading", { name: "Marcel Cohen", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Marcel Cravenne");
  await expect(page.locator("main")).toContainText("film editor and director");
  await expect(page.locator("main")).toContainText("temporal relation uncertain");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 439 preserves all ten rows, masks identifiers and keeps unresolved namesakes visible", async ({ page }) => {
  const expected = [
    ["17ca80e8-cf1a-59e0-b414-e4b748013fa3", "Louise D Cohen", "b8aafbac-1336-529e-ab04-388f2c9bf298", "133", true],
    ["d52905c0-3de5-5cd0-b015-fa4ec9398766", "Mabel Cohen", "f1f38720-1e60-5711-870b-8dfce4985f3b", "133", false],
    ["200fc5df-df5e-5898-962e-63c49a825356", "Marcel Cohen", "de72abd5-e9b3-5d60-9758-5caf0d7d9b35", "133", false],
    ["e710e105-a184-50ca-8e06-133274b460ca", "Noah J Cohen", "5d3a28e3-2a51-5017-baae-98313237aa4d", "133", true],
    ["10e8e445-dd65-59e6-8a13-a0c4f7e4cf28", "Robert A Cohen", "1d1ab263-7c2d-542e-b2ee-e1becf3bb313", "133", false],
    ["e7f8bbbe-71e9-572e-abf9-fbf3581e041d", "Sarah Cohen", "e9f260fc-a34d-5e8a-ae6d-060e5839949c", "133", false],
    ["73105eec-b393-5333-b8ec-da5f0832486a", "Sidney L Cohen", "bfb8b281-0798-5349-86b7-8014bc67575b", "133", true],
    ["05c008ff-79b7-58e8-99ca-4528a39b5f54", "Theodore Cohen", "57cd7be0-4a9f-5e1d-ba51-662c4fd33328", "133", false],
    ["96bb4e98-fef0-5d31-a5fd-2fa21875f742", "Carl M Cohn", "fa92459b-748b-542f-ad53-a7f64c20a2be", "133", true],
    ["1c16dedd-1629-558f-8ddf-1821808ecb1e", "Edwin J Cohn Jr.", "1318cfa6-44b3-5f7b-8ce0-4435be8227e2", "132", false],
  ];

  for (const [id, name, sourceRecordId, box, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 86,
      rank_as_indexed: null,
      box,
      archive_location: "230/86/28/07",
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

  for (const id of [
    "17ca80e8-cf1a-59e0-b414-e4b748013fa3",
    "e7f8bbbe-71e9-572e-abf9-fbf3581e041d",
    "1c16dedd-1629-558f-8ddf-1821808ecb1e",
  ]) {
    const person = profile(id);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const louise = profile("17ca80e8-cf1a-59e0-b414-e4b748013fa3");
  expect(louise.identity_status).toBe("ambiguous");
  await page.goto(`./people/${louise.person_id}/`);
  await expect(page.getByRole("heading", { name: "Louise D Cohen", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Louis or Lewis Cohen");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  const edwin = profile("1c16dedd-1629-558f-8ddf-1821808ecb1e");
  await page.goto(`./people/${edwin.person_id}/`);
  await expect(page.getByRole("heading", { name: "Edwin J Cohn Jr.", exact: true })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("Harvard biochemist");
});
