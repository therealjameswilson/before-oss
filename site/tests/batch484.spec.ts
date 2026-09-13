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
  ["e22e73ce-92e3-511c-a522-e0f384616a9a", "Katehrine M Cowen", "abcbe86f-429d-5661-8832-fe4bcda63cd1", "149", null],
  ["53e57106-492b-5127-8255-2cd49f9d8201", "Wilbur A Cowett", "d93a234f-5f24-5ee1-b54b-58f501cc7206", "150", "••••7598"],
  ["2dda6c0d-38cc-5c34-b02f-bd04dd9edcab", "Lawrence L Cowger", "e31b6aed-aec2-5c69-9015-08703f19f8b4", "150", "••••8363"],
  ["bb5381dd-be46-51c8-a794-5d1bbda8f328", "John F Cowgill", "f8b4428d-a65d-51a7-931f-8c3277fc50b4", "150", null],
  ["008775a2-a334-54ae-9e0c-13baaf1d3b4e", "David O Cowles", "47f57cd0-1d80-572c-912f-8f0e4fda5e04", "150", "••••8279"],
  ["f6ed20c2-57d2-5eb5-b16e-eef3653d4755", "Alfred T Cox", "3567ce30-3502-58d0-8e33-149e348d5d1e", "150", null],
  ["6909bd17-a5b5-59c2-b81e-47cebee1b893", "Arthur M Cox", "4bc115c8-7881-5fe6-9887-20b0ca05908d", "150", null],
  ["8580a6aa-0113-52cf-8e8c-83156673ad99", "Charles W Cox", "2f07cbc5-5cd6-5f83-85df-460a313c4e19", "150", "••••1395"],
  ["7f2dd2e8-7842-5083-9244-72d3d5989eb6", "Clarence R Cox", "25b32529-fb4c-5b85-9d50-7257cbd5793c", "150", "••••6040"],
  ["d3f9beb5-abf3-58a9-917c-6ae1c3be4d4f", "Donald J Cox", "6969ca59-f6da-5bc9-808e-9178d9d10208", "150", "••••2766"],
] as const;

test("Batch 484 preserves the ten page 96 rows and masks private identifiers", () => {
  for (const [id, name, sourceRecordId, box, serial] of cohort) {
    const person = profile(id);
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        box,
        archive_location: "230/86/29/03",
        pdf_page: 96,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 484 publishes only supported exact-identifier Army occupations", () => {
  const cases = [
    ["008775a2-a334-54ae-9e0c-13baaf1d3b4e", "Occupation in manufacture of radios and phonographs"],
    ["7f2dd2e8-7842-5083-9244-72d3d5989eb6", "Farm hand, animal and livestock"],
    ["d3f9beb5-abf3-58a9-917c-6ae1c3be4d4f", "Photographic process occupation"],
  ] as const;

  for (const [id, occupation] of cases) {
    const person = profile(id);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
    });
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        occupation,
        relationship_type: "unknown",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    );
    expect(person.claims).toEqual(
      expect.arrayContaining([
        expect.objectContaining({ claim_type: "identity", claim_confidence: "confirmed" }),
        expect.objectContaining({ claim_type: "occupation", claim_confidence: "medium" }),
      ]),
    );
  }

  const lawrence = profile("2dda6c0d-38cc-5c34-b02f-bd04dd9edcab");
  expect(lawrence).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(lawrence.claims).toHaveLength(1);
  expect(lawrence.claims[0]).toMatchObject({ claim_type: "identity" });
});

test("Batch 484 keeps unresolved common-name and Allied candidates unassigned", () => {
  for (const id of [
    "e22e73ce-92e3-511c-a522-e0f384616a9a",
    "53e57106-492b-5127-8255-2cd49f9d8201",
    "bb5381dd-be46-51c8-a794-5d1bbda8f328",
    "6909bd17-a5b5-59c2-b81e-47cebee1b893",
    "8580a6aa-0113-52cf-8e8c-83156673ad99",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  expect(profile("bb5381dd-be46-51c8-a794-5d1bbda8f328")).toMatchObject({
    personnel_category: "foreign_or_allied_military_personnel",
    allied_or_foreign_personnel: true,
    commissioned_officer: null,
  });
});

test("Batch 484 separates Alfred Cox's military predecessor from Lehigh student status", () => {
  const alfred = profile("f6ed20c2-57d2-5eb5-b16e-eef3653d4755");
  expect(alfred).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "completed",
    last_civilian_pre_service: [],
  });
  expect(alfred.immediate_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "U.S. Army Infantry School",
      relationship_type: "military_assignment",
      immediate_pre_oss: true,
      claim_confidence: "high",
    }),
  );
  expect(alfred.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Lehigh University",
      relationship_type: "student",
      immediate_pre_oss: false,
      claim_confidence: "high",
    }),
  );
  expect(alfred.claims).toHaveLength(3);
});

test("Batch 484 profile and coverage data render the reviewed outcome", async ({ page }) => {
  expect(stats.research_attempted_people).toBe(4609);
  expect(stats.verified_affiliation_people).toBe(530);
  expect(stats.verified_employer_people).toBe(235);

  await page.goto("./people/f6ed20c2-57d2-5eb5-b16e-eef3653d4755/");
  await expect(page.getByRole("heading", { name: "Alfred T Cox", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("U.S. Army Infantry School");
  await expect(page.locator("main")).toContainText("Captain and guerrilla-warfare instructor");
  await expect(page.locator("main")).toContainText("Lehigh University");
  await expect(page.locator("main")).toContainText("Civil engineering student");
  await expect(page.locator("main")).toContainText("Daily Life in Camp Park and Town");
  await expect(page.locator("main")).toContainText("Alfred Cox - Roger S. Penske/Lehigh Athletics Hall of Fame");
});
