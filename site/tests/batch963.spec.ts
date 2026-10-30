import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page472-harry-trainosky-to-william-treat-review_batch-963_2026-10-29.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["b1cfbbc5-6503-554d-a4a0-ce2de319f5b5", "Harry Trainosky"],
  ["d4d935e2-f749-585e-a087-6195e37b7cd9", "Athenesios P Traintos"],
  ["c4049a48-3c09-5c37-a934-14fc0b2104a1", "Fannie M Tramantano"],
  ["f9e08d73-0e00-5ab2-b46f-0ee7aa4e5c63", "Albert Tramonti"],
  ["9211fdc5-2eed-5089-b58f-267735773d09", "Kurt E Trampel"],
  ["ca5871a0-fa0d-5074-b8fd-479ab1d94a32", "Anthony Tramuta"],
  ["95f03c8b-794a-5d5d-a27d-78745588690d", "Jack Tranes"],
  ["83412f4c-4834-50aa-8a36-6eadd50cc2a5", "Lillian Trangott"],
  ["5443535b-811d-52b5-b22a-c1ecebf95ac7", "F W Trapwell"],
  ["ca9be871-b625-5062-b435-0b2bca887810", "George M Trate"],
  ["2f3399a1-d162-51b3-967f-d04e5db13d51", "Alvin W Traub"],
  ["fd434428-30e6-5a00-8110-22429c5aa2dd", "Lillian Traugott"],
  ["3aae401a-368a-54f0-99b0-94054a258037", "Ralph C Traunecker"],
  ["f1c861af-67f0-58e3-9723-ecf7bb570960", "Marcella M Traut"],
  ["627fe0bd-a41b-577c-bbe2-da49b5dc3b46", "Vincent D Travaglini"],
  ["3aa9d2e9-6ce3-5dd7-9b59-87a7fff7e36d", "Helen E Travers"],
  ["6816b766-c089-5688-8d1e-e06141ba4af1", "Thomas J Travers"],
  ["e9ec8843-c86e-551d-95a7-4f4d33ccc4ed", "George Travis"],
  ["802721f2-ad68-56db-acd3-6c7cc6c0b545", "James Travis"],
  ["461c6ca0-13b8-573a-a1b3-b3769821399e", "Leo M Traynor"],
  ["5f06d6a6-99ce-50f5-a14f-58bf750abe74", "Emerson Treacy"],
  ["0e9f2d7d-8b3f-54bd-ab7d-c08dabebf820", "Owen E Treanor"],
  ["34047313-8092-56ca-a1a2-f2963e964eb3", "William W Treat"],
] as const;

const unresolvedIds = new Set([
  "b1cfbbc5-6503-554d-a4a0-ce2de319f5b5",
  "c4049a48-3c09-5c37-a934-14fc0b2104a1",
  "f9e08d73-0e00-5ab2-b46f-0ee7aa4e5c63",
  "9211fdc5-2eed-5089-b58f-267735773d09",
  "95f03c8b-794a-5d5d-a27d-78745588690d",
  "5443535b-811d-52b5-b22a-c1ecebf95ac7",
  "f1c861af-67f0-58e3-9723-ecf7bb570960",
  "627fe0bd-a41b-577c-bbe2-da49b5dc3b46",
  "3aa9d2e9-6ce3-5dd7-9b59-87a7fff7e36d",
  "6816b766-c089-5688-8d1e-e06141ba4af1",
  "802721f2-ad68-56db-acd3-6c7cc6c0b545",
  "461c6ca0-13b8-573a-a1b3-b3769821399e",
  "5f06d6a6-99ce-50f5-a14f-58bf750abe74",
  "34047313-8092-56ca-a1a2-f2963e964eb3",
]);

const occupationProfiles = [
  ["d4d935e2-f749-585e-a087-6195e37b7cd9", "Athenesios P Traintos", "student", "student"],
  ["ca5871a0-fa0d-5074-b8fd-479ab1d94a32", "Anthony Tramuta", "general office clerk", "employment"],
  ["ca9be871-b625-5062-b435-0b2bca887810", "George M Trate", "insurance clerk, not elsewhere classified", "employment"],
  ["2f3399a1-d162-51b3-967f-d04e5db13d51", "Alvin W Traub", "student", "student"],
  ["3aae401a-368a-54f0-99b0-94054a258037", "Ralph C Traunecker", "craneman, derrickman, hoistman, or shovelman", "employment"],
  ["e9ec8843-c86e-551d-95a7-4f4d33ccc4ed", "George Travis", "salesperson", "employment"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 963 publishes 23 audited people with terminal outcomes", async ({ page }) => {
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

test("six Army matches publish only qualified occupation or student status", async ({ request }) => {
  for (const [id, name, occupation, relationshipType] of occupationProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationshipType,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]);
  }
});

test("student categories do not become employers or named schools", async ({ request }) => {
  for (const [id, name] of occupationProfiles.filter((item) => item[3] === "student")) {
    const person = await publicPerson(request, id, name);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      organization_id: null,
      canonical_organization: null,
      relationship_type: "student",
      occupation: "student",
    });
  }
});

test("Owen Treanor is a commissioned officer without an invented prior affiliation", async ({ request }) => {
  const person = await publicPerson(request, "0e9f2d7d-8b3f-54bd-ab7d-c08dabebf820", "Owen E Treanor");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
  ]);
});

test("Lillian Trangott and Lillian Traugott remain separate ambiguous profiles", async ({ request }) => {
  const first = await publicPerson(request, "83412f4c-4834-50aa-8a36-6eadd50cc2a5", "Lillian Trangott");
  const second = await publicPerson(request, "fd434428-30e6-5a00-8110-22429c5aa2dd", "Lillian Traugott");
  expect(first).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(second).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(first.person_id).not.toBe(second.person_id);
  expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
  expect(first.claims).toHaveLength(0);
  expect(second.claims).toHaveLength(0);
});

test("unresolved people retain archival outcomes without transferred namesake facts", async ({ request }) => {
  for (const [id, name] of profiles.filter(([id]) => unresolvedIds.has(id))) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 963 evidence excludes secrets and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 963 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 663,
    research_attempted_people: 15_087,
    verified_affiliation_people: 1_084,
    verified_employer_people: 486,
    archival_review_assessed_people: 13_563,
    published_claims: 9_462,
    public_sources: 6_164,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Students");
});
