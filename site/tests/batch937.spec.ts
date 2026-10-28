import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page459-dezso-szenes-to-kengo-tajima-review_batch-937_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["56b743a4-535d-5c7f-b33f-f76c35273c76", "Dezso Szenes"],
  ["35d4df75-6035-54c3-a17d-8b4453f74c41", "Stefan Szumowski"],
  ["82cab6f6-dfe2-5f0f-9ff7-761faa99dcf6", "Tadeuss Szumowski"],
  ["9f2ca7dd-d743-5d85-9fa0-7167303fe5e5", "Victor Szymaniak"],
  ["6db3c164-5528-55bf-97d4-e1c8aae920f2", "Anna G Szynal"],
  ["f8342c9f-d29e-5681-86a1-391f44651486", "Harold J Tabb"],
  ["9fbd2204-b28c-502e-bc8b-12b67279f5b4", "Margaret R Taber"],
  ["729c3004-3d2a-519b-b931-a6c807bddf66", "Wilma I Taber"],
  ["f9a70a72-bfcb-5fd1-952a-16adafdb3134", "Tadami Tachino"],
  ["50dca7b8-0dce-5e83-95d4-725c32d666ab", "Nick J Tacko"],
  ["d79e477e-8c47-5618-b6a3-89184f53915d", "Spiros T Taflambas"],
  ["f3fde389-ce3d-575c-aee2-973d893a8408", "Barbara B Taft"],
  ["78b7408c-0017-57ad-ae5f-6799c19c5efc", "Harold J Tager"],
  ["2fdebc68-98c1-536b-b74f-695a1336ffe6", "M F Tager"],
  ["925db9be-d571-538b-941e-f9e81ebba172", "Spencer L Taggart"],
  ["5eeb613e-fb1e-5548-9430-3c5a2c121174", "Daniel T Taglia"],
  ["852c7597-0064-54aa-bc41-dd599f947e1e", "Frances J Tagliavia"],
  ["d371cf0c-6ce7-578f-a8ff-80d23b3ce2fd", "John J Taheny"],
  ["b7cbb373-4019-5fbb-874d-5f2a6b0beba5", "Masami Taiji"],
  ["54c7d1b4-a115-5291-8ee5-487f75f84d83", "Ernest Taikerdanos"],
  ["c053fffe-bfd8-53b1-9dff-3d59b3f54514", "John S Tainter"],
  ["c79aa130-f7a2-5e49-8264-0ac633029daa", "Patricia R Tait"],
  ["872a245a-8318-5425-891a-1d0c89b0f34b", "Kengo Tajima"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 937 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("Tadeuss Szumowski preserves the spelling variant and a qualified Polish Project Eagle pathway", async ({ request, page }) => {
  await page.goto("./people/82cab6f6-dfe2-5f0f-9ff7-761faa99dcf6/");
  const main = page.locator("main");
  await expect(main).toContainText("Tadeusz Szumowski");
  await expect(main).toContainText("Polish Armed Forces in the West");
  await expect(main).toContainText("Project Eagle");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  const people = await peopleShard(request, "t");
  const person = people.find((item: { person_id: string }) => item.person_id === "82cab6f6-dfe2-5f0f-9ff7-761faa99dcf6");
  expect(person.name_variants).toContain("Tadeusz Szumowski");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Polish Armed Forces in the West",
    relationship_type: "military_assignment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "medium",
  });
});

test("Anna Szynal publishes Becker College only as immediate student status", async ({ request, page }) => {
  await page.goto("./people/6db3c164-5528-55bf-97d4-e1c8aae920f2/");
  const main = page.locator("main");
  await expect(main).toContainText("Becker College");
  await expect(main).toContainText("student");
  await expect(main).not.toContainText("Last civilian employer before wartime service");

  const people = await peopleShard(request, "a");
  const person = people.find((item: { person_id: string }) => item.person_id === "6db3c164-5528-55bf-97d4-e1c8aae920f2");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Becker College",
    relationship_type: "student",
    temporal_basis: "explicit_immediate",
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Tadami Tachino keeps Poston translator work qualified and incarceration-aware", async ({ request, page }) => {
  await page.goto("./people/f9a70a72-bfcb-5fd1-952a-16adafdb3134/");
  const main = page.locator("main");
  await expect(main).toContainText("Poston War Relocation Center");
  await expect(main).toContainText("translator");
  await expect(main).toContainText("incarceration");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");

  const people = await peopleShard(request, "t");
  const person = people.find((item: { person_id: string }) => item.person_id === "f9a70a72-bfcb-5fd1-952a-16adafdb3134");
  expect(person.identity_status).toBe("probable");
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Poston War Relocation Center, Camp 3 Adult Education Department",
    occupation: "translator",
    temporal_basis: "documented_prewar",
    claim_confidence: "medium",
  });
});

test("Spiros Taflambas separates the last civilian occupation from the earlier job and invents no employer", async ({ request, page }) => {
  await page.goto("./people/d79e477e-8c47-5618-b6a3-89184f53915d/");
  const main = page.locator("main");
  await expect(main).toContainText("waiter");
  await expect(main).toContainText("grocery delivery boy");
  await expect(main).toContainText("Greek Operational Group II");

  const people = await peopleShard(request, "s");
  const person = people.find((item: { person_id: string }) => item.person_id === "d79e477e-8c47-5618-b6a3-89184f53915d");
  expect(person.last_civilian_pre_service[0].occupation).toBe("waiter");
  expect(person.last_civilian_pre_service[0].canonical_organization).toBeNull();
  expect(person.other_pre_oss_affiliations[0].occupation).toBe("grocery delivery");
  expect(person.other_pre_oss_affiliations[0].canonical_organization).toBeNull();
});

test("Spencer Taggart publishes the explicit Justice Department-to-OSS sequence", async ({ request, page }) => {
  await page.goto("./people/925db9be-d571-538b-941e-f9e81ebba172/");
  const main = page.locator("main");
  await expect(main).toContainText("U.S. Department of Justice");
  await expect(main).toContainText("Special War Policies Unit");
  await expect(main).toContainText("Foreign Agents Registration Section");
  await expect(main).toContainText("Spencer Laird Taggart");

  const people = await peopleShard(request, "s");
  const person = people.find((item: { person_id: string }) => item.person_id === "925db9be-d571-538b-941e-f9e81ebba172");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "U.S. Department of Justice",
    relationship_type: "government_assignment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Masami Taiji publishes MISLS assignment while leaving the undefined occupation code uninterpreted", async ({ request, page }) => {
  await page.goto("./people/b7cbb373-4019-5fbb-874d-5f2a6b0beba5/");
  const main = page.locator("main");
  await expect(main).toContainText("Military Intelligence Service Language School");
  await expect(main).toContainText("Headquarters Company");
  await expect(main).toContainText("Undefined Army code 352 remains uninterpreted");

  const people = await peopleShard(request, "m");
  const person = people.find((item: { person_id: string }) => item.person_id === "b7cbb373-4019-5fbb-874d-5f2a6b0beba5");
  expect(person.identity_status).toBe("confirmed");
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Military Intelligence Service Language School",
    relationship_type: "military_assignment",
    temporal_basis: "temporal_relation_uncertain",
  });
});

test("Daniel Taglia and John Tainter remain occupation-only and employer-free", async ({ page }) => {
  for (const [id, phrase] of [
    ["5eeb613e-fb1e-5548-9430-3c5a2c121174", "Stock clerks"],
    ["c053fffe-bfd8-53b1-9dff-3d59b3f54514", "Machine shop and related occupations, n.e.c."],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(phrase);
    await expect(main).toContainText("no employer or workplace");
    await expect(main).not.toContainText("Last civilian employer before wartime service");
  }
});

test("Kengo Tajima remains an unresolved archival case and receives no pastor claim", async ({ request, page }) => {
  await page.goto("./people/872a245a-8318-5425-891a-1d0c89b0f34b/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("same-name West Coast pastor");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");

  const people = await peopleShard(request, "k");
  const person = people.find((item: { person_id: string }) => item.person_id === "872a245a-8318-5425-891a-1d0c89b0f34b");
  expect(person.identity_status).toBe("ambiguous");
  expect(person.claims).toHaveLength(0);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 937 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Becker College");
  await expect(main).not.toContainText("U.S. Department of Justice");
});

test("Batch 937 evidence excludes credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("36316994");
  expect(evidence).not.toContain("37772334");
  expect(evidence).not.toContain("11018199");
  expect(evidence).not.toContain("301953");
  expect(evidence).not.toContain("542013");
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 937 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 634,
    research_attempted_people: 14_495,
    verified_affiliation_people: 1_025,
    verified_employer_people: 463,
    archival_review_assessed_people: 12_968,
    published_claims: 8_934,
    public_sources: 5_896,
  });
});
