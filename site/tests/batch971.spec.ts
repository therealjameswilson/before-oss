import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page476-olive-turner-to-edgar-twamley-review_batch-971_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["29257549-20a2-519d-858e-65d3eb00ddc2", "Olive J Turner"],
  ["0eebd349-e415-5ab5-ae7a-c417e0d35a0e", "Oscar Turner"],
  ["ece51c24-29cf-55ea-a9c2-dc04418d82fa", "Robert A Turner"],
  ["361649a6-a65b-54fe-885d-cd221d8ddf0d", "Robert E Turner"],
  ["ca63ec77-3678-579d-b108-0c42339f3618", "Vernon R Turner"],
  ["76723c8e-f874-5f8d-99c5-c49b694f053c", "Wilmore J Turner"],
  ["18814fea-530b-54a0-b9b9-95796b9c7e5b", "Willison H Turney"],
  ["0de56684-395c-5d73-9852-dd5badbae081", "Norman R Turpin"],
  ["496bbce6-47da-55c9-aeed-65f4617ff538", "Robert G Turpin"],
  ["eeb98a02-d488-5656-9ebd-bcd1888908dd", "Sara Turpin"],
  ["91d98415-0ab9-5ae7-ad47-eb25417b9efa", "Pierre M Turquet"],
  ["30a89768-a52e-545c-8ec8-a5c450017a3e", "William A Turrell"],
  ["92055f33-0141-56b2-bd86-56f59bddfcc2", "Cipriano E Turri"],
  ["3f2a6b2e-dcf5-515a-94f3-a1ae05e54772", "Carl F Turvey"],
  ["052bcbc9-333c-58c7-a951-397c3184ada3", "Wladyslaw Turzecki"],
  ["63e62b1e-f409-5fbc-9c2f-d35a61acab50", "Everett D Tutor"],
  ["75832d36-db7c-5fc4-a832-7c6d46963459", "Hiram D Tuttle"],
  ["e731c885-b01a-5dc9-8732-01ed4f9d6bc2", "Kenneth D Tuttle"],
  ["07162a59-8b5f-5c63-9f05-5d4159a63090", "Shirley R Tutun"],
  ["3c67dcdf-554f-56fa-b1ff-0c60867058a9", "Catherine B Tuvo"],
  ["552d5697-fe1f-5db4-9650-fcbeefc6ea7b", "Albert Tversky"],
  ["3f8f78f8-9de6-577e-a77e-f983172f1c1e", "Arnold E Tvinnerain"],
  ["3b47a877-c697-51bb-ba4b-6d5a2e688501", "Edgar H Twamley"],
] as const;

const occupationProfiles = [
  ["ca63ec77-3678-579d-b108-0c42339f3618", "Vernon R Turner", "manager or official, not elsewhere classified"],
  ["18814fea-530b-54a0-b9b9-95796b9c7e5b", "Willison H Turney", "semiskilled printing or publishing worker, not elsewhere classified"],
  ["e731c885-b01a-5dc9-8732-01ed4f9d6bc2", "Kenneth D Tuttle", "lumberman, raftsman or woodchopper"],
  ["552d5697-fe1f-5db4-9650-fcbeefc6ea7b", "Albert Tversky", "general-office clerk"],
] as const;

const unresolvedProfiles = [
  ["29257549-20a2-519d-858e-65d3eb00ddc2", "Olive J Turner"],
  ["0eebd349-e415-5ab5-ae7a-c417e0d35a0e", "Oscar Turner"],
  ["ece51c24-29cf-55ea-a9c2-dc04418d82fa", "Robert A Turner"],
  ["361649a6-a65b-54fe-885d-cd221d8ddf0d", "Robert E Turner"],
  ["0de56684-395c-5d73-9852-dd5badbae081", "Norman R Turpin"],
  ["496bbce6-47da-55c9-aeed-65f4617ff538", "Robert G Turpin"],
  ["eeb98a02-d488-5656-9ebd-bcd1888908dd", "Sara Turpin"],
  ["30a89768-a52e-545c-8ec8-a5c450017a3e", "William A Turrell"],
  ["3f2a6b2e-dcf5-515a-94f3-a1ae05e54772", "Carl F Turvey"],
  ["052bcbc9-333c-58c7-a951-397c3184ada3", "Wladyslaw Turzecki"],
  ["07162a59-8b5f-5c63-9f05-5d4159a63090", "Shirley R Tutun"],
  ["3c67dcdf-554f-56fa-b1ff-0c60867058a9", "Catherine B Tuvo"],
  ["3f8f78f8-9de6-577e-a77e-f983172f1c1e", "Arnold E Tvinnerain"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 971 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("four Army categories remain qualified occupations without named employers", async ({ request }) => {
  for (const [id, name, occupation] of occupationProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: "unknown",
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
      }),
    ]));
  }
});

test("Wilmore Turner keeps the protected-identifier name conflict visible", async ({ request, page }) => {
  const person = await publicPerson(request, "76723c8e-f874-5f8d-99c5-c49b694f053c", "Wilmore J Turner");
  expect(person).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting", publication_status: "conflicting" }),
  ]);
  await page.goto("./people/76723c8e-f874-5f8d-99c5-c49b694f053c/");
  await expect(page.locator("main")).toContainText("Turner J W");
});

test("Pierre Turquet publishes a qualified Allied military assignment, not an immediate employer", async ({ request, page }) => {
  const person = await publicPerson(request, "91d98415-0ab9-5ae7-ad47-eb25417b9efa", "Pierre M Turquet");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "foreign_or_allied_military_personnel",
    commissioned_officer: true,
    allied_or_foreign_personnel: true,
    research_status: "requires_archival_review",
  });
  expect(person.name_variants).toEqual(expect.arrayContaining(["Pierre Maurice Turquet"]));
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Royal Army Medical Corps",
      role_title: "Major",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(person.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
    expect.objectContaining({ claim_type: "other_pre_oss_affiliation", claim_confidence: "medium" }),
  ]));
  await page.goto("./organizations/cbd4a40c-a104-5ad2-acc0-172be0f45a02/");
  await expect(page.getByRole("heading", { name: "Royal Army Medical Corps", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Pierre M Turquet");
});

test("Edgar Twamley separates immediate, last-civilian and earlier employers", async ({ request, page }) => {
  const person = await publicPerson(request, "3b47a877-c697-51bb-ba4b-6d5a2e688501", "Edgar H Twamley");
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "WBEN Inc.",
      role_title: "station director",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "WBEN Inc.", last_civilian_pre_service: true }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "National Broadcasting Company",
      role_title: "station relations staff",
      temporal_basis: "documented_prewar",
    }),
  ]);
  expect(person.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
    expect.objectContaining({ claim_type: "immediate_pre_oss_affiliation", claim_confidence: "high" }),
    expect.objectContaining({ claim_type: "last_civilian_pre_service", claim_confidence: "high" }),
    expect.objectContaining({ claim_type: "other_pre_oss_affiliation", claim_confidence: "high" }),
  ]));
  await page.goto("./organizations/e98c6f24-1230-5dd5-82f2-fcf37a13b64b/");
  await expect(page.getByRole("heading", { name: "WBEN Inc.", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Edgar H Twamley");
});

test("thirteen unresolved profiles remain dignified archival-review cases", async ({ request }) => {
  for (const [id, name] of unresolvedProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("three exact Army identities do not gain undecoded occupations", async ({ request }) => {
  for (const [id, name] of [
    ["92055f33-0141-56b2-bd86-56f59bddfcc2", "Cipriano E Turri"],
    ["63e62b1e-f409-5fbc-9c2f-d35a61acab50", "Everett D Tutor"],
    ["75832d36-db7c-5fc4-a832-7c6d46963459", "Hiram D Tuttle"],
  ]) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual([
      expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
    ]);
  }
});

test("Batch 971 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 971 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 664,
    research_attempted_people: 15_269,
    verified_affiliation_people: 1_095,
    verified_employer_people: 489,
    archival_review_assessed_people: 13_745,
    published_claims: 9_659,
    public_sources: 6_253,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
