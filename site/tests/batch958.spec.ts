import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page469-gordon-r-tobin-to-page470-n-s-tokutaro-review_batch-958_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["07e04072-b55c-5389-be3d-3380b27391d3", "Gordon R Tobin"],
  ["31bf8dc1-da43-5fdf-8895-d318f1004945", "Irwin M Tobin"],
  ["0791692f-1f8a-58df-8039-81eb59f48a15", "John D Tobin"],
  ["3bf1f8cb-412a-51d1-b8dc-db4d35062c57", "Robert P Tobin"],
  ["9e5c54a0-ce0e-5216-92d5-5c44212b079b", "Floyd C Tobrocke"],
  ["7266d744-4bba-551f-bd82-c432e8f0e8ee", "Gerard A Toby"],
  ["c7cb1281-ced3-5596-969f-01d3db991c78", "John Tocarsic"],
  ["128b53e8-fb1f-5daf-bdf7-918120fb3430", "Francis Tocci"],
  ["8becc7a0-8fd1-51c8-8810-1d90799619ce", "Honey M Toda"],
  ["464c9397-7c2e-5a4d-9822-c823b5b75910", "Arthur F Todd"],
  ["9dcb4274-c36c-56cc-88bc-33b7720d0458", "Frederick P Todd"],
  ["bf7424eb-dca8-551b-8f2a-e619370bd8a7", "Harvey A Todd"],
  ["85cccea5-b404-540a-b6ec-baab298bdf08", "Howard F Todd"],
  ["92548794-93f5-5dca-af1b-35b2f525a5f5", "Letha M Todd"],
  ["06b1dfe4-e894-51d9-ac0d-46570074ef6f", "Luella A Todd"],
  ["1b3d60c5-adc1-5f23-9122-f560d75bb44a", "Millard H Todd"],
  ["63bf5fdb-dfd5-5bef-ba43-c599b2af1cb8", "Paul H Todd"],
  ["9ec01f9d-7e3e-5949-b3cd-dd0baa9608f2", "Paul H Todd"],
  ["b4eb53ab-f457-5032-a8e3-68ad1c21cff1", "Suzanne Todd"],
  ["108625da-e49b-58e7-be3a-ad169b3911e6", "Borislav J Todorovic"],
  ["0d36d7ab-ff22-5c46-a366-1f499e9784a1", "Stewart T Togans"],
  ["99cbe6e1-6cc3-523b-8465-af3561438325", "Frances J Togliavia"],
  ["e9fbb26c-883f-5f49-af50-c25d256c66d9", "N S Tokutaro"],
] as const;

const unresolvedIds = new Set([
  "07e04072-b55c-5389-be3d-3380b27391d3",
  "0791692f-1f8a-58df-8039-81eb59f48a15",
  "3bf1f8cb-412a-51d1-b8dc-db4d35062c57",
  "c7cb1281-ced3-5596-969f-01d3db991c78",
  "128b53e8-fb1f-5daf-bdf7-918120fb3430",
  "9dcb4274-c36c-56cc-88bc-33b7720d0458",
  "bf7424eb-dca8-551b-8f2a-e619370bd8a7",
  "85cccea5-b404-540a-b6ec-baab298bdf08",
  "92548794-93f5-5dca-af1b-35b2f525a5f5",
  "06b1dfe4-e894-51d9-ac0d-46570074ef6f",
  "1b3d60c5-adc1-5f23-9122-f560d75bb44a",
  "63bf5fdb-dfd5-5bef-ba43-c599b2af1cb8",
  "b4eb53ab-f457-5032-a8e3-68ad1c21cff1",
  "0d36d7ab-ff22-5c46-a366-1f499e9784a1",
  "99cbe6e1-6cc3-523b-8465-af3561438325",
]);

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 958 publishes 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Irwin Tobin preserves the government pathway and separate civilian employer", async ({ request, page }) => {
  const person = await publicPerson(request, "31bf8dc1-da43-5fdf-8895-d318f1004945", "Irwin M Tobin");
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Office of War Information",
      relationship_type: "government_assignment",
      immediate_pre_oss: true,
      last_civilian_pre_service: false,
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Rhode Island State College",
      relationship_type: "employment",
      immediate_pre_oss: false,
      last_civilian_pre_service: true,
    }),
  ]);
  await page.goto("./people/31bf8dc1-da43-5fdf-8895-d318f1004945/");
  await expect(page.locator("main")).toContainText("Office of War Information");
  await expect(page.locator("main")).toContainText("Rhode Island State College");
});

test("qualified student, civilian, military and civic pathways remain distinct", async ({ request }) => {
  const honey = await publicPerson(request, "8becc7a0-8fd1-51c8-8810-1d90799619ce", "Honey M Toda");
  expect(honey.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "University of Maryland", relationship_type: "student" }),
    expect.objectContaining({ canonical_organization: "University of Maryland", relationship_type: "employment" }),
    expect.objectContaining({ canonical_organization: "Manzanar Relocation Center Education Department", relationship_type: "government_assignment" }),
  ]));
  expect(honey.last_civilian_pre_service).toHaveLength(0);

  const paul = await publicPerson(request, "9ec01f9d-7e3e-5949-b3cd-dd0baa9608f2", "Paul H Todd");
  expect(paul.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Cornell University", relationship_type: "student" }),
    expect.objectContaining({ canonical_organization: "United States Army Signal Corps", relationship_type: "military_assignment" }),
  ]));
  expect(paul.last_civilian_pre_service).toHaveLength(0);

  const slocum = await publicPerson(request, "e9fbb26c-883f-5f49-af50-c25d256c66d9", "N S Tokutaro");
  expect(slocum.name_variants).toContain("Tokutaro Nishimura Slocum");
  expect(slocum.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Japanese American Citizens League", relationship_type: "professional_affiliation" }),
    expect.objectContaining({ canonical_organization: "Anti-Axis Committee", relationship_type: "professional_affiliation" }),
  ]));
});

test("Army categories publish as occupations without inventing employers", async ({ request }) => {
  for (const [id, name, variant, occupation] of [
    ["7266d744-4bba-551f-bd82-c432e8f0e8ee", "Gerard A Toby", "Gerald A Toby", "repairmen and mechanics, n. e. c."],
    ["464c9397-7c2e-5a4d-9822-c823b5b75910", "Arthur F Todd", "Arth R F Todd", "bookkeepers and cashiers, except bank cashiers"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
    expect(person.name_variants).toContain(variant);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({ canonical_organization: null, occupation }),
    ]);
  }
});

test("the two Paul H Todd rows remain separate and Hans Tofte is unchanged", async ({ request }) => {
  const unresolved = await publicPerson(request, "63bf5fdb-dfd5-5bef-ba43-c599b2af1cb8", "Paul H Todd");
  const resolved = await publicPerson(request, "9ec01f9d-7e3e-5949-b3cd-dd0baa9608f2", "Paul H Todd");
  expect(unresolved).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
  expect(resolved).toMatchObject({ identity_status: "confirmed", research_status: "completed" });
  expect(unresolved.possible_duplicate_group).toBe(resolved.possible_duplicate_group);
  expect(unresolved.claims).toHaveLength(0);
  const hans = await publicPerson(request, "f28308b3-7c6e-5819-834d-62ec9ef7a65f", "Hans V Tofte");
  expect(hans.research_status).toBe("completed");
});

test("fifteen unresolved people keep archival outcomes without namesake facts", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => unresolvedIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 958 evidence excludes secrets and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 958 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 650,
    research_attempted_people: 14_972,
    verified_affiliation_people: 1_071,
    verified_employer_people: 479,
    archival_review_assessed_people: 13_448,
    published_claims: 9_342,
    public_sources: 6_102,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Rhode Island State College");
});
