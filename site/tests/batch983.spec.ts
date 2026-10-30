import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page482-edward-c-veigel-to-m-p-veran-review_batch-983_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["25b4ded1-d287-5680-9e77-072ccadf2f03", "Edward C Veigel"],
  ["3b8b4299-8dc4-5b1e-aff3-d8abe1363965", "Rock G Veilleux"],
  ["033b3adc-b3f2-525a-802f-6d438bcf8bc9", "Evelyn M Veith"],
  ["1124fde4-d031-5cc1-8b89-217722a1e6cc", "Paul Velay"],
  ["45dc42eb-8c1c-52ba-91a1-1ac1da7909e4", "Hermes Velez"],
  ["8b6fe7b1-ce53-5cc3-895f-724988f74fcd", "Anthony J Vella"],
  ["404f2fd6-b353-581f-8ba8-57b953916e94", "Anthony J Vella"],
  ["ca775866-fb72-5226-8b75-71447d09d156", "Walter F Vella"],
  ["9a81eee3-9800-507c-b604-ef49aafc3da3", "Arthur H Velleman"],
  ["833cab1f-839d-5766-baf2-4bebff78cada", "Moritz Velleman"],
  ["899455b1-64c6-5a77-8c65-29b2447b86a9", "Guss Vellios"],
  ["5a0538fa-0b0c-5f45-bbbc-4094c81f9736", "Alex L Vellis"],
  ["28d4ca4f-e3c6-5322-a519-d2f03ee5c6fd", "Lawson R Venable"],
  ["73d65c5b-56b8-5e0d-bf76-055753173f4a", "Theodore Venard"],
  ["982f70ae-b035-5658-9369-decacad2e92b", "Malcolm Vendrick"],
  ["5cd94b1a-0c3b-5fbc-8750-5946f8b482d8", "Anthony A Veneruso"],
  ["ba6f0b53-a64c-567b-a673-b02fc77e71b0", "Irene A Venit"],
  ["2f8a9780-0748-5d48-92f7-de31c48cba54", "Claude H Venon"],
  ["7f0f46d5-0bad-5d45-92a6-5bbe9bfd9057", "Atta B Venson"],
  ["3a7fc3e4-e455-57dc-b944-8b992a31a505", "Annina Ventrella"],
  ["bdd660b0-ca6b-54fa-81a7-cd22b108476e", "Jose Ventura"],
  ["bf74d86c-94cf-5191-92d5-f60b97c64d37", "Lauro Venturi"],
  ["432ad6dd-0b72-5c7c-b104-2ea7721abd74", "M P Veran"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 983 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Army bridges publish qualified categories rather than invented employers", async ({ request }) => {
  const expected = [
    ["3b8b4299-8dc4-5b1e-aff3-d8abe1363965", "Rock G Veilleux", "paper-goods manufacturing occupation"],
    ["8b6fe7b1-ce53-5cc3-895f-724988f74fcd", "Anthony J Vella", "warehousing, storekeeping, handling, loading or unloading occupation, not elsewhere classified"],
    ["899455b1-64c6-5a77-8c65-29b2447b86a9", "Guss Vellios", "decorator or window dresser"],
    ["28d4ca4f-e3c6-5322-a519-d2f03ee5c6fd", "Lawson R Venable", "laboratory technician or assistant"],
    ["5cd94b1a-0c3b-5fbc-8750-5946f8b482d8", "Anthony A Veneruso", "semiskilled automobile-manufacturing occupation, not elsewhere classified"],
    ["2f8a9780-0748-5d48-92f7-de31c48cba54", "Claude H Venon", "student"],
    ["bdd660b0-ca6b-54fa-81a7-cd22b108476e", "Jose Ventura", "kitchen worker in a hotel, restaurant, railroad, steamship or related establishment, not elsewhere classified"],
    ["bf74d86c-94cf-5191-92d5-f60b97c64d37", "Lauro Venturi", "student"],
  ] as const;
  for (const [id, name, occupation] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person.identity_status).toBe("high_confidence");
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("Walter Vella separates Berkeley student status from the immediate Army pathway", async ({ request }) => {
  const person = await publicPerson(request, "ca775866-fb72-5226-8b75-71447d09d156", "Walter F Vella");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "completed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Army Specialized Training Program",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "University of California, Berkeley",
      role_title: "student",
      relationship_type: "student",
      claim_confidence: "high",
    }),
  ]));
});

test("Alex Vellis is an identity finding without a fabricated occupation", async ({ request }) => {
  const person = await publicPerson(request, "5a0538fa-0b0c-5f45-bbbc-4094c81f9736", "Alex L Vellis");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "enlisted_army_personnel",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
});

test("shared-identifier and same-name rows remain visibly separate", async ({ request }) => {
  const veigel = await publicPerson(request, "25b4ded1-d287-5680-9e77-072ccadf2f03", "Edward C Veigel");
  const viegel = await publicPerson(request, "6d9ca923-aed1-5972-8936-ceed76854a23", "Edward C Viegel");
  expect(veigel).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(veigel.possible_duplicate_group).toMatch(/^duplicate-[a-f0-9]{12}$/);
  expect(viegel.possible_duplicate_group).toBe(veigel.possible_duplicate_group);
  expect(veigel.possible_duplicate_group).not.toMatch(/\d{8}/);

  const anthonyWithIdentifier = await publicPerson(request, "8b6fe7b1-ce53-5cc3-895f-724988f74fcd", "Anthony J Vella");
  const anthonyWithoutIdentifier = await publicPerson(request, "404f2fd6-b353-581f-8ba8-57b953916e94", "Anthony J Vella");
  expect(anthonyWithIdentifier.person_id).not.toBe(anthonyWithoutIdentifier.person_id);
  expect(anthonyWithIdentifier.possible_duplicate_group).toBe(anthonyWithoutIdentifier.possible_duplicate_group);
  expect(anthonyWithoutIdentifier).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
});

test("the nine newly unbridged people remain affiliation-free archival cases", async ({ request }) => {
  const names = new Set([
    "Evelyn M Veith", "Paul Velay", "Hermes Velez", "Theodore Venard", "Malcolm Vendrick",
    "Irene A Venit", "Atta B Venson", "Annina Ventrella", "M P Veran",
  ]);
  for (const [id, name] of profiles.filter(([, name]) => names.has(name))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Batch 983 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 983 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 669,
    research_attempted_people: 15_542,
    verified_affiliation_people: 1_120,
    verified_employer_people: 504,
    archival_review_assessed_people: 14_018,
    published_claims: 9_898,
    public_sources: 6_393,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
