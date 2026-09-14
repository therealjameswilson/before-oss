import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 469 preserves all ten printed rows across the page and box boundary", () => {
  const expected = [
    ["084a3e1f-3df8-5cc2-805d-74ac8f5a183d", "Joseph D Coppock", "50e93b44-2813-588e-bca6-267a31d11d15", null, "143", 92],
    ["6e48723e-f18e-5d50-8590-f45df2537790", "Stephen J Coraleski", "92877376-e849-5e29-885d-232aae728da5", "••••1644", "143", 92],
    ["2825c500-74bd-5261-afd5-f669eb0bfd24", "Eugene P Corbets", "61f1ab34-7f03-555e-8b7d-9d85adffc6e9", null, "143", 92],
    ["d9a90b23-8ac7-5439-be2d-8d4f12c980ab", "Chesley S Corbett", "841a6009-d591-595b-bedc-006c0a79c975", null, "143", 92],
    ["1f95beef-aec9-5e6c-a58b-9c18abb3bb64", "Dorothy L Corbett", "f20ecd83-db40-56ac-b769-d8c7fc78b139", null, "143", 92],
    ["b23d10ce-fc33-5e4c-b1b0-1ee729945820", "Emory T Corbett", "f1bfd094-a077-5094-90a5-9ea012240695", null, "143", 92],
    ["351308d7-1005-5ec2-885b-d7f3703a1754", "George C Corbett Jr.", "20f6982a-36bf-5b3e-9242-7f39aa91d1fa", "••••7637", "143", 92],
    ["a929b4f2-9c2d-5e01-b8bd-b14e6b5ef237", "John M Corbett", "376e286e-2b28-5911-9d74-170fc3023e5b", "••••5480", "143", 92],
    ["0b8f049a-7227-5068-afab-bde32fc1d3c9", "Dolly O Corbin", "93cfbe0e-c5de-54da-925b-1f37cc526ac2", null, "143", 92],
    ["aaf61289-6edb-5a21-af16-0f9a58d2646b", "Robert C Corbin", "e95bc59e-eab1-590b-be66-5744eeb84aa6", "••••5880", "144", 93],
  ];

  for (const [id, name, sourceRecordId, serial, box, page] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: null,
        serial_masked: serial,
        box,
        archive_location: "230/86/29/02",
        pdf_page: page,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 469 publishes Joseph Coppock's explicit OPA-to-OSS pathway without choosing among concurrent civilian affiliations", async ({ page }) => {
  const joseph = profile("084a3e1f-3df8-5cc2-805d-74ac8f5a183d");
  expect(joseph).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
    research_status: "documented_prewar_employer_found",
  });
  expect(joseph.name_variants).toContain("Joseph D. Coppock");
  expect(joseph.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Office of Price Administration",
      role_title: "head",
      relationship_type: "government_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  );
  expect(joseph.last_civilian_pre_service).toEqual([]);
  expect(joseph.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "United States Department of Agriculture", role_title: "economist" }),
      expect.objectContaining({ canonical_organization: "War Production Board", role_title: "special assistant to the vice chairman" }),
      expect.objectContaining({ canonical_organization: "Swarthmore College", relationship_type: "employment" }),
      expect.objectContaining({ canonical_organization: "National Bureau of Economic Research", role_title: "Financial Research Staff member" }),
      expect.objectContaining({ canonical_organization: "University of California", relationship_type: "professional_affiliation" }),
    ]),
  );

  await page.goto("./people/084a3e1f-3df8-5cc2-805d-74ac8f5a183d/");
  await expect(page.getByRole("heading", { name: "Joseph D Coppock", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Office of Price Administration");
  await expect(page.locator("main")).toContainText("Swarthmore College");
  await expect(page.locator("main")).toContainText("A single last civilian employer before wartime or military service has not yet been established");
});

test("Batch 469 publishes only bounded occupations for the two exact Army matches", async ({ page }) => {
  const expected = [
    ["6e48723e-f18e-5d50-8590-f45df2537790", "Stephen J Coraleski", "Buffers, polishers, filers, and grinders (metal)", "1942-09-03", "143"],
    ["aaf61289-6edb-5a21-af16-0f9a58d2646b", "Robert C Corbin", "Engineers, industrial", "1943-02-19", "144"],
  ];
  for (const [id, name, occupation, endDate, box] of expected) {
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
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    );

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: String(name), exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(String(occupation));
    await expect(page.locator("main")).toContainText(`Review Box ${box}`);
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 469 leaves unsupported identities unresolved and exposes archival next actions", async ({ page }) => {
  const unresolved = [
    "2825c500-74bd-5261-afd5-f669eb0bfd24",
    "d9a90b23-8ac7-5439-be2d-8d4f12c980ab",
    "1f95beef-aec9-5e6c-a58b-9c18abb3bb64",
    "b23d10ce-fc33-5e4c-b1b0-1ee729945820",
    "351308d7-1005-5ec2-885b-d7f3703a1754",
    "a929b4f2-9c2d-5e01-b8bd-b14e6b5ef237",
    "0b8f049a-7227-5068-afab-bde32fc1d3c9",
  ];
  for (const id of unresolved) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      personnel_category: "unknown_or_indeterminate",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  await page.goto("./people/a929b4f2-9c2d-5e01-b8bd-b14e6b5ef237/");
  await expect(page.getByRole("heading", { name: "John M Corbett", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Review Box 143");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
