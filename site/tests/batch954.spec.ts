import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page467-george-thornton-to-walter-h-thurn-review_batch-954_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["3eaee07c-ad1f-5aac-9067-80b288358223", "George Thornton"],
  ["9813058e-948f-54a1-b531-830fd57520f7", "George D Thornton"],
  ["28de3ad1-ac3d-5166-9252-718f74ee763d", "Homer A Thornton"],
  ["13adbaaa-c9f4-5a34-9dc7-bec1b035473f", "J R Thornton"],
  ["ff67f7bb-616f-595b-aa02-b384b2b07b34", "Steve W Thornton"],
  ["6aca7beb-46ce-5804-b46e-fba2731d0582", "Claude G Thorpe"],
  ["1329c519-a0c3-5f86-9c7c-77f6d1aaa0f9", "George H Thorpe"],
  ["c0ad88ce-8efc-5642-94aa-0b737b50eb48", "Wilbur Thorpe"],
  ["50c61c2d-b77b-59c9-b09a-bdb215f5c10b", "Arthur C Thorsen"],
  ["3f226327-04e9-5dfd-812d-b00883aabbae", "Randell A Thorsen"],
  ["a0872503-1a26-598e-b496-20a238fb327d", "Kent D Thorup"],
  ["4313fff7-d9d1-5ac0-9683-f1669e8e4509", "Martin C Thraikill"],
  ["997e7660-49ed-5566-988a-aff5457c1624", "Donald S Thrall"],
  ["a0498cde-de76-5b25-94b3-c1bfabac856a", "Rastus W Thrasher"],
  ["c80601a9-cc7c-5c78-9e4d-e97621314899", "John E Throwbridge"],
  ["a943f5da-0fbb-5f23-98ff-3731251fdf9b", "Clellan C Thrower"],
  ["8b4a9cd3-97aa-5dc7-92ff-719ace44183c", "Fredrick M Thrower"],
  ["6b3ee250-ca60-58ce-8990-e481afd8c743", "Robert Thrun"],
  ["73b4c7d4-b77b-50de-aec6-08bea9efcd3d", "Paul H Thunnissen"],
  ["eca8027a-3642-5f8f-a3d5-34d14d72805c", "Francis B Thurber"],
  ["59151c96-04d4-50f4-ae2e-c8830d29ef03", "John W Thurlow"],
  ["3b177db3-fa9f-5558-ac1f-32ed57cf2f2a", "Edwin B Thurman"],
  ["ab0cb3f1-9652-57c4-9768-bc6d0d95e43a", "Walter H Thurn"],
] as const;

const armyCategories = [
  ["3eaee07c-ad1f-5aac-9067-80b288358223", "George Thornton", "student", "student", "1942-12-10"],
  ["9813058e-948f-54a1-b531-830fd57520f7", "George D Thornton", "purchasing agents and buyers, n. e. c.", "employment", "1945-02-16"],
  ["28de3ad1-ac3d-5166-9252-718f74ee763d", "Homer A Thornton", "architects", "employment", "1943-10-05"],
  ["1329c519-a0c3-5f86-9c7c-77f6d1aaa0f9", "George H Thorpe", "occupations in manufacture of boots and shoes", "employment", "1942-11-21"],
  ["c0ad88ce-8efc-5642-94aa-0b737b50eb48", "Wilbur Thorpe", "construction occupations, n. e. c.", "employment", "1942-09-21"],
  ["50c61c2d-b77b-59c9-b09a-bdb215f5c10b", "Arthur C Thorsen", "machine shop and related occupations, n. e. c.", "employment", "1941-03-11"],
  ["997e7660-49ed-5566-988a-aff5457c1624", "Donald S Thrall", "construction occupations, n. e. c.", "employment", "1942-12-03"],
  ["a0498cde-de76-5b25-94b3-c1bfabac856a", "Rastus W Thrasher", "general farmers", "employment", "1942-12-16"],
  ["6b3ee250-ca60-58ce-8990-e481afd8c743", "Robert Thrun", "lawyers and judges", "employment", "1943-06-15"],
  ["3b177db3-fa9f-5558-ac1f-32ed57cf2f2a", "Edwin B Thurman", "salesmen, insurance", "employment", "1942-09-28"],
  ["ab0cb3f1-9652-57c4-9768-bc6d0d95e43a", "Walter H Thurn", "mechanics and repairmen, motor vehicle", "employment", "1942-07-01"],
] as const;

const unresolvedIds = [
  "13adbaaa-c9f4-5a34-9dc7-bec1b035473f",
  "ff67f7bb-616f-595b-aa02-b384b2b07b34",
  "6aca7beb-46ce-5804-b46e-fba2731d0582",
  "3f226327-04e9-5dfd-812d-b00883aabbae",
  "a0872503-1a26-598e-b496-20a238fb327d",
  "4313fff7-d9d1-5ac0-9683-f1669e8e4509",
  "c80601a9-cc7c-5c78-9e4d-e97621314899",
  "a943f5da-0fbb-5f23-98ff-3731251fdf9b",
  "8b4a9cd3-97aa-5dc7-92ff-719ace44183c",
  "73b4c7d4-b77b-50de-aec6-08bea9efcd3d",
  "eca8027a-3642-5f8f-a3d5-34d14d72805c",
  "59151c96-04d4-50f4-ae2e-c8830d29ef03",
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

async function publicPerson(
  request: APIRequestContext,
  id: string,
  displayName: string,
) {
  const shard = await peopleShard(request, displayName[0].toLowerCase());
  return shard.find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 954 publishes all 23 audited rows with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) {
      expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
    }
  }
});

test("eleven Army matches publish only qualified dated historical categories", async ({ request }) => {
  for (const [id, name, occupation, relationship, endDate] of armyCategories) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("George Thornton keeps student status separate from employment", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "3eaee07c-ad1f-5aac-9067-80b288358223",
    "George Thornton",
  );
  expect(person.name_variants).toContain("George C Thornton");
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    occupation: "student",
    relationship_type: "student",
    end_date: "1942-12-10",
  });
  await page.goto("./people/3eaee07c-ad1f-5aac-9067-80b288358223/");
  const main = page.locator("main");
  await expect(main).toContainText("student");
  await expect(main).toContainText("no school or employer is identified");
  await expect(main).not.toContainText("Student — employer");
});

test("Walter H Thurn publishes the sourced Jr variant without changing the indexed name", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "ab0cb3f1-9652-57c4-9768-bc6d0d95e43a",
    "Walter H Thurn",
  );
  expect(person.display_name).toBe("Walter H Thurn");
  expect(person.name_variants).toContain("Walter H Thurn Jr");
  await page.goto("./people/ab0cb3f1-9652-57c4-9768-bc6d0d95e43a/");
  await expect(page.getByRole("heading", { name: "Walter H Thurn", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Walter H Thurn Jr");
});

test("twelve unresolved people keep archival-review outcomes without transferred facts", async ({ request }) => {
  for (const id of unresolvedIds) {
    const profile = profiles.find(([profileId]) => profileId === id);
    expect(profile).toBeTruthy();
    const person = await publicPerson(request, id, profile![1]);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      personnel_category: "unknown_or_indeterminate",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 954 evidence excludes secrets and protected-identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 954 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 648,
    research_attempted_people: 14_881,
    verified_affiliation_people: 1_053,
    verified_employer_people: 472,
    archival_review_assessed_people: 13_357,
    published_claims: 9_243,
    public_sources: 6_052,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("student category");
});
