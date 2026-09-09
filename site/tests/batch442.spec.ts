import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 442 preserves identifier-supported Army occupations without inventing employers", async ({ page }) => {
  const expected = [
    [
      "fa8fa6cc-d96d-5f4b-82fd-f9f39d977f2c",
      "Manny Cole",
      "Mjnny Cole",
      "Newsboy",
      "1944-01-27",
    ],
    [
      "b16cf49b-b509-5383-8b31-b03ba885dbeb",
      "Raymond T Cole",
      "Raymond T Cole",
      "Accountant or auditor",
      "1944-02-29",
    ],
  ];

  for (const [id, indexedName, documentedVariant, occupation, endDate] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: indexedName,
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.name_variants).toContain(documentedVariant);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        organization_id: null,
        occupation,
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
      }),
    );
  }

  const manny = profile("fa8fa6cc-d96d-5f4b-82fd-f9f39d977f2c");
  await page.goto(`./people/${manny.person_id}/`);
  await expect(page.getByRole("heading", { name: "Manny Cole", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Mjnny Cole");
  await expect(page.locator("main")).toContainText("Newsboy");
  await expect(page.locator("main")).toContainText("no newspaper, route or employer is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 442 publishes Remsen Cole's documented-prewar firm without overstating chronology", async ({ page }) => {
  const remsen = profile("48a1eb2f-7da0-5757-a839-913057a727bd");
  expect(remsen).toMatchObject({
    display_name: "Remsen J Cole",
    identity_status: "high_confidence",
    personnel_category: "commissioned_marine_corps_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
  });
  expect(remsen.name_variants).toContain("Remsen J. Cole");
  expect(remsen.immediate_pre_oss_affiliations).toEqual([]);
  expect(remsen.last_civilian_pre_service).toEqual([]);
  expect(remsen.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Remsen J. Cole and Associates",
      role_title: "Head",
      occupation: "Public relations counsel",
      relationship_type: "self_employment",
      temporal_basis: "documented_prewar",
      identity_confidence: "high_confidence",
      claim_confidence: "high",
      sector: "advertising_and_public_relations",
    }),
  );

  const affiliationClaim = remsen.claims.find(
    (claim: { claim_type: string }) => claim.claim_type === "other_pre_oss_affiliation",
  );
  expect(affiliationClaim).toMatchObject({
    claim_confidence: "high",
    publication_status: "published",
  });
  expect(
    affiliationClaim.sources.some(
      (link: { source: { stable_url: string } }) =>
        link.source.stable_url === "https://doi.org/10.1086/265428",
    ),
  ).toBe(true);

  await page.goto(`./people/${remsen.person_id}/`);
  await expect(page.getByRole("heading", { name: "Remsen J Cole", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Remsen J. Cole and Associates");
  await expect(page.locator("main")).toContainText("public relations counsel of Philadelphia");
  await expect(page.locator("main")).toContainText("documented prewar");
  await expect(page.locator("main")).toContainText("No publishable immediate affiliation or civilian employer is recorded yet");
  await expect(page.locator("main")).toContainText("Lieutenant Colonels");
});

test("Batch 442 preserves every source row, masks identifiers and keeps unresolved people visible", async ({ page }) => {
  const expected = [
    ["348ecda7-5f56-5838-8893-142847ee805c", "Frederic W Cole", "ea52b2a4-a2c1-5357-9d81-3f8636b27c41", 86, true],
    ["01695f9a-1467-50d8-a77d-77d24f71d10d", "Gordon H Cole", "78975813-d0b1-5f0b-96a9-ca7d11e249eb", 86, false],
    ["9ef2a574-ef20-5c06-9eed-58cc0783defc", "Joe Cole", "887bb884-4c0b-57e7-b3b3-b0c8a6053481", 86, false],
    ["36b48c6c-7087-5ee9-82f5-49f900e06062", "John O Cole", "6fe4de29-c1b4-574c-935f-7654a74727d7", 87, true],
    ["8eafdcf1-0310-53f5-b8bb-ff60b4729c07", "Joseph G Cole", "ef59874d-7207-5c1f-a437-2e41dc801e70", 87, false],
    ["874bbb80-f03f-5c50-8b69-392782bbd18e", "Kathryn B Cole", "0819b2f1-9d52-51cc-8754-cfd90f9d71d6", 87, false],
    ["fa8fa6cc-d96d-5f4b-82fd-f9f39d977f2c", "Manny Cole", "29bc641b-a728-580e-bf6f-3c0bf258bc87", 87, true],
    ["f35d0663-fd6a-5886-8353-e82a59cd39d5", "Nathan L Cole", "1c970f80-ec19-56b3-8f93-4a69a6ea07eb", 87, true],
    ["b16cf49b-b509-5383-8b31-b03ba885dbeb", "Raymond T Cole", "de19a06d-fd55-5aee-9bed-a54f3c8eed52", 87, true],
    ["48a1eb2f-7da0-5757-a839-913057a727bd", "Remsen J Cole", "30caf269-abf0-5b3f-86e1-aca758ed7a09", 87, false],
  ];

  for (const [id, name, sourceRecordId, pdfPage, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: pdfPage,
      rank_as_indexed: null,
      box: "134",
      archive_location: "230/86/29/01",
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
    "348ecda7-5f56-5838-8893-142847ee805c",
    "01695f9a-1467-50d8-a77d-77d24f71d10d",
    "9ef2a574-ef20-5c06-9eed-58cc0783defc",
    "36b48c6c-7087-5ee9-82f5-49f900e06062",
    "8eafdcf1-0310-53f5-b8bb-ff60b4729c07",
    "874bbb80-f03f-5c50-8b69-392782bbd18e",
    "f35d0663-fd6a-5886-8353-e82a59cd39d5",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const frederic = profile("348ecda7-5f56-5838-8893-142847ee805c");
  await page.goto(`./people/${frederic.person_id}/`);
  await expect(page.getByRole("heading", { name: "Frederic W Cole", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("short six-digit identifier");
  await expect(page.locator("main")).toContainText("was not padded");
  await expect(page.locator("main")).toContainText("Review Box 134");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
