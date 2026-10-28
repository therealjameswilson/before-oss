import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page463-henry-w-terrett-to-erika-teutsch-review_batch-946_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["aebe55ca-6471-5529-b9b9-ce7502b1716d", "Henry W Terrett"],
  ["a8575c75-1395-56ae-aa75-e3682156d30e", "Walter L Terrill"],
  ["6db6bbce-c97a-5977-8231-5829a9fbef86", "Rocco E Terrone"],
  ["1c07bfe7-a8a8-5284-b4b4-d215442105c0", "James R Terry"],
  ["c573aa1d-646b-57bb-ad7c-53ec81567d04", "Rollin E Terry"],
  ["57e4222f-297e-5302-91fc-d1d74bb686cf", "Harry J Terwilliger"],
  ["398cf0e8-557c-5b10-b853-a764d32cc4be", "Alexander J Terzaghi"],
  ["20c04d14-0e5d-589d-ad9d-98992fae8d8e", "Adrian Terzian"],
  ["b7be437e-2360-530e-bdaa-151f5216328f", "Fred Teschner"],
  ["deba6c6c-275b-5696-8b18-72647305e4df", "Edward Tesdorff"],
  ["845073eb-17ca-51a2-89fd-3cd4d606e5f9", "William G Tesi"],
  ["b14d12d5-bc9c-5762-bfce-36ec79eccf78", "John R Teske"],
  ["59c899f0-ea9b-5d4f-9947-415764b54940", "John R Teske"],
  ["cc4b077b-540a-55a1-9008-a89c84d07356", "Joseph J Tesoriere"],
  ["f49a8bb6-17bd-57cc-a6b5-8ca0bead42f3", "Emil Tessari"],
  ["e3e63998-895a-5043-8aff-584c6b2ee42e", "John Tessitore"],
  ["bf398b17-a0bb-593a-b1b2-39602a310499", "Frank C Test"],
  ["58ced547-179f-5c8d-b880-480fa680ddfc", "Janet Testerman"],
  ["ba92e4c7-4f0f-57c4-a9a5-1b8a7df2b1c8", "* Testi"],
  ["dc16580f-e943-5e38-a78c-e1b02a7985c0", "Joseph Testo"],
  ["26b0c21c-c39d-5c2d-b1ac-1cc2ca6c5a7f", "Leo P Tetrault"],
  ["c27c77fc-f69a-562d-912b-e3df7f1547df", "Leo P Tetrealt"],
  ["436a8686-43bb-5463-a073-1bd851b02d04", "Erika Teutsch"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 946 publishes all 23 indexed-row entities with reviewed outcomes", async ({ page }) => {
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

test("Henry Terrett preserves the middle-initial conflict and transfers no Army occupation", async ({ request, page }) => {
  const person = (await peopleShard(request, "h")).find(
    (item: { person_id: string }) => item.person_id === "aebe55ca-6471-5529-b9b9-ce7502b1716d",
  );
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  ]);
  await page.goto("./people/aebe55ca-6471-5529-b9b9-ce7502b1716d/");
  await expect(page.locator("main")).toContainText("Conflicting identity");
  await expect(page.locator("main")).toContainText("Henry M. Terrett");
});

test("the Terrell-Terrill and Teske duplicate candidates remain separate", async ({ request }) => {
  const walters = await peopleShard(request, "w");
  const walterTerrell = walters.find(
    (item: { person_id: string }) => item.person_id === "f238d457-78c8-5960-985c-b84c7b7586e0",
  );
  const walterTerrill = walters.find(
    (item: { person_id: string }) => item.person_id === "a8575c75-1395-56ae-aa75-e3682156d30e",
  );
  expect(walterTerrell.possible_duplicate_group).toBe(walterTerrill.possible_duplicate_group);
  expect(walterTerrell.person_id).not.toBe(walterTerrill.person_id);
  expect(walterTerrell.claims).toHaveLength(0);
  expect(walterTerrill.claims).toHaveLength(0);

  const johns = (await peopleShard(request, "j")).filter(
    (item: { person_id: string }) => [
      "b14d12d5-bc9c-5762-bfce-36ec79eccf78",
      "59c899f0-ea9b-5d4f-9947-415764b54940",
    ].includes(item.person_id),
  );
  expect(johns).toHaveLength(2);
  expect(johns[0].possible_duplicate_group).toBe(johns[1].possible_duplicate_group);
  for (const person of johns) {
    expect(person.identity_status).toBe("ambiguous");
    expect(person.research_status).toBe("needs_identity_review");
    expect(person.claims).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Leo Tetrault and Tetrealt remain separate and only the protected row receives evidence", async ({ request }) => {
  const people = await peopleShard(request, "l");
  const unbridged = people.find(
    (item: { person_id: string }) => item.person_id === "26b0c21c-c39d-5c2d-b1ac-1cc2ca6c5a7f",
  );
  const identified = people.find(
    (item: { person_id: string }) => item.person_id === "c27c77fc-f69a-562d-912b-e3df7f1547df",
  );
  expect(unbridged.possible_duplicate_group).toBe(identified.possible_duplicate_group);
  expect(unbridged.identity_status).toBe("ambiguous");
  expect(unbridged.claims).toHaveLength(0);
  expect(unbridged.other_pre_oss_affiliations).toHaveLength(0);
  expect(identified.identity_status).toBe("high_confidence");
  expect(identified.name_variants).toEqual(expect.arrayContaining(["Leo P Tetrault", "Leo P Tetreault"]));
  expect(identified.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: null,
    organization_name_as_found: null,
    occupation: "stock clerk",
    claim_confidence: "medium",
  });
});

test("Erika Teutsch publishes Swarthmore only as a qualified student pathway", async ({ request, page }) => {
  const person = (await peopleShard(request, "e")).find(
    (item: { person_id: string }) => item.person_id === "436a8686-43bb-5463-a073-1bd851b02d04",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "needs_temporal_review",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Swarthmore College",
      relationship_type: "student",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  await page.goto("./people/436a8686-43bb-5463-a073-1bd851b02d04/");
  const main = page.locator("main");
  await expect(main).toContainText("Swarthmore College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("Probable immediate");
  await expect(main).not.toContainText("Last civilian employer before service\nSwarthmore");
});

test("reviewed Army categories remain unnamed and student status is not employment", async ({ request }) => {
  const cases = [
    ["r", "6db6bbce-c97a-5977-8231-5829a9fbef86", "musician or music teacher", "employment"],
    ["j", "1c07bfe7-a8a8-5284-b4b4-d215442105c0", "student", "student"],
    ["w", "845073eb-17ca-51a2-89fd-3cd4d606e5f9", "semiskilled construction occupation, not elsewhere classified", "employment"],
    ["j", "e3e63998-895a-5043-8aff-584c6b2ee42e", "semiskilled textile-manufacturing occupation, not elsewhere classified", "employment"],
    ["j", "dc16580f-e943-5e38-a78c-e1b02a7985c0", "student", "student"],
  ] as const;
  for (const [letter, id, occupation, relationshipType] of cases) {
    const person = (await peopleShard(request, letter)).find(
      (item: { person_id: string }) => item.person_id === id,
    );
    expect(person.personnel_category).toBe("enlisted_army_personnel");
    expect(person.commissioned_officer).toBe(false);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({
      canonical_organization: null,
      organization_name_as_found: null,
      occupation,
      relationship_type: relationshipType,
      claim_confidence: "medium",
    });
  }
});

test("Batch 946 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Swarthmore College");
});

test("Batch 946 evidence excludes credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 946 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 645,
    research_attempted_people: 14_699,
    verified_affiliation_people: 1_044,
    verified_employer_people: 470,
    archival_review_assessed_people: 13_173,
    published_claims: 9_121,
    public_sources: 5_998,
  });
});
