import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 445 publishes identifier-supported occupations without inventing employers", async ({ page }) => {
  const expected = [
    [
      "10a113c8-e185-5ef7-a2a3-c73b3615bbb2",
      "Henry D Collette",
      "Henry D Collette",
      "Chauffeurs and drivers, bus, taxi, truck, and tractor",
      "1943-02-01",
    ],
    [
      "7e707cf1-72be-56f4-abad-5fba832aef1c",
      "L J Collier",
      "Langdon J Collier",
      "Clerk, general office",
      "1942-08-22",
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

  const henry = profile("10a113c8-e185-5ef7-a2a3-c73b3615bbb2");
  await page.goto(`./people/${henry.person_id}/`);
  await expect(page.getByRole("heading", { name: "Henry D Collette", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Chauffeurs and drivers");
  await expect(page.locator("main")).toContainText("no employer or vehicle is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  const langdon = profile("7e707cf1-72be-56f4-abad-5fba832aef1c");
  await page.goto(`./people/${langdon.person_id}/`);
  await expect(page.getByRole("heading", { name: "L J Collier", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Langdon J Collier");
  await expect(page.locator("main")).toContainText("Clerk, general office");
  await expect(page.locator("main")).toContainText("no employer or office is identified");
});

test("Batch 445 keeps civilian employment, self-employment, candidate evidence and military assignment distinct", async ({ page }) => {
  const miles = profile("d1b020df-b909-566f-a3d6-3afe9f547ebd");
  expect(miles).toMatchObject({
    display_name: "Miles Collier",
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(miles.immediate_pre_oss_affiliations).toEqual([]);
  expect(miles.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Collier Company",
      relationship_type: "employment",
      identity_confidence: "high_confidence",
      claim_confidence: "high",
    }),
  );
  expect(miles.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Motor Sport, Inc.",
      relationship_type: "self_employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  );

  const sam = profile("4c8a470f-b646-55ab-9123-3f312aef5a92");
  expect(sam).toMatchObject({
    display_name: "Sam A Collier",
    identity_status: "probable",
    research_status: "requires_archival_review",
  });
  expect(sam.last_civilian_pre_service).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Collier Company",
      identity_confidence: "probable",
      claim_confidence: "medium",
    }),
  );
  expect(sam.identity_evidence).toContain("printed A conflicts");

  const john = profile("d9b8c0b9-08f5-58e5-8952-bdfcf5d74528");
  expect(john).toMatchObject({
    display_name: "John G Colling",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "occupation_only_found",
  });
  expect(john.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  );
  expect(john.last_civilian_pre_service).toEqual([]);
  expect(john.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({ occupation: "Draftsman", relationship_type: "unknown" }),
  );

  await page.goto(`./people/${miles.person_id}/`);
  await expect(page.getByRole("heading", { name: "Miles Collier", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Collier Company");
  await expect(page.locator("main")).toContainText("Motor Sport, Inc.");

  await page.goto(`./people/${sam.person_id}/`);
  await expect(page.locator("main")).toContainText("probably, but not conclusively");
  await expect(page.locator("main")).toContainText("printed A conflicts");

  await page.goto(`./people/${john.person_id}/`);
  await expect(page.locator("main")).toContainText("United States Army");
  await expect(page.locator("main")).toContainText("Draftsman");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 445 preserves all ten printed rows, masks identifiers and publishes unresolved profiles", async ({ page }) => {
  const expected = [
    ["10a113c8-e185-5ef7-a2a3-c73b3615bbb2", "Henry D Collette", "9ad65c03-23d5-5445-81d1-022932b43cce", "135", true],
    ["8ae1962f-1269-5a97-8fea-0d128bea3370", "Joseph H Collette", "805d3de0-82dd-5382-83be-2bf6f8438f28", "135", false],
    ["35f21edb-a69a-56df-8d02-37afa0d0ec36", "Penelope E Colley", "3e6aa888-ebcd-54ce-951b-7e7d10fd6765", "135", false],
    ["7e707cf1-72be-56f4-abad-5fba832aef1c", "L J Collier", "9fa494d6-484e-57d7-b1b6-99c3e3e5d207", "136", true],
    ["c68fcd1d-1405-52d0-ad7e-c4cb6aa72f59", "Mildred Collier", "76728d78-d023-507d-8b2a-8ec536b5bce5", "135", false],
    ["d1b020df-b909-566f-a3d6-3afe9f547ebd", "Miles Collier", "e525882f-b87f-5975-93b7-125aae1ce0f7", "135", false],
    ["4c8a470f-b646-55ab-9123-3f312aef5a92", "Sam A Collier", "d7a1bafc-8b17-5193-848f-3d74d2fb660d", "135", false],
    ["d9b8c0b9-08f5-58e5-8952-bdfcf5d74528", "John G Colling", "826698e4-2639-547e-9503-108713e53baa", "135", true],
    ["a60422b0-3cb0-5b18-a1fe-91fac1e026c4", "Agnes B Collins", "edfe849f-911d-54bb-bb1f-d2189ea0ea35", "135", false],
    ["053a3c8e-36da-54d6-883d-079377bf9ee4", "Charles A Collins", "31773baf-0403-568a-abe4-aa93a1775b2b", "135", false],
  ];

  for (const [id, name, sourceRecordId, box, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      box,
      archive_location: "230/86/29/01",
      pdf_page: 87,
    });
    if (hasSerial) {
      expect(person.source_records[0].serial_masked).toMatch(/^••••.{3,4}$/u);
    } else {
      expect(person.source_records[0].serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  for (const id of [
    "8ae1962f-1269-5a97-8fea-0d128bea3370",
    "35f21edb-a69a-56df-8d02-37afa0d0ec36",
    "c68fcd1d-1405-52d0-ad7e-c4cb6aa72f59",
    "a60422b0-3cb0-5b18-a1fe-91fac1e026c4",
    "053a3c8e-36da-54d6-883d-079377bf9ee4",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const joseph = profile("8ae1962f-1269-5a97-8fea-0d128bea3370");
  await page.goto(`./people/${joseph.person_id}/`);
  await expect(page.getByRole("heading", { name: "Joseph H Collette", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Seaman Second Class");
  await expect(page.locator("main")).toContainText("Review Box 135");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");

  const charles = profile("053a3c8e-36da-54d6-883d-079377bf9ee4");
  await page.goto(`./people/${charles.person_id}/`);
  await expect(page.locator("main")).toContainText("Twenty-three exact-name Army rows");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
