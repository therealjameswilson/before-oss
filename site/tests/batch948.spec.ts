import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page464-costas-a-theodorou-to-corcoran-thom-review_batch-948_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["7f3c14f8-1069-50e5-a05a-0bc958ba9316", "Costas A Theodorou"],
  ["abafc141-5add-5adc-83dd-98e30147d32c", "Sotiris Theodorou"],
  ["d905ceb1-67b5-561e-b232-080b02cb81fc", "Terry Theodorou"],
  ["698e35ea-2c1b-5ef5-bbc1-0538dbae0ba2", "Adrien W Theriault"],
  ["962f7b23-23aa-5b3b-9257-dbb20201d3e8", "William A Theurer"],
  ["99f5be17-f251-59c3-9fc4-4272a1d96cea", "Ann Thibault"],
  ["c9c58a7a-a4e3-50e5-a0e2-c04202a59622", "John H Thibault"],
  ["6925ac26-afb4-5be7-8617-50269fb4dad6", "Joseph R Thibault"],
  ["d7423224-e9c0-5d09-8b06-43a512defa1c", "Raymond G Thibault"],
  ["52c9f309-7c41-5afa-a0c1-09dd7f99ab69", "Edison P Thibodeaux"],
  ["7e18000b-32d7-5c97-a54f-8bb955fc1eae", "Alphonse P Thiele"],
  ["e336d001-148e-529d-89c5-8f9ac23b9545", "Robert J Thiele"],
  ["6a895d08-e55a-5784-8715-52468002443f", "Charles G Thielicke"],
  ["d870f173-8868-5a38-8215-7fc2d30f3d5d", "Frank W Thielker"],
  ["2ed459bb-34ce-5960-91cb-d26cd4270e1d", "Robert J Thill"],
  ["dfb0fd93-2e00-5236-a792-87275fcb7c5e", "Annie Thinesse"],
  ["0b509df6-b304-5e0a-92b5-fc5086fd1073", "Bernice J Thiry"],
  ["5f3dfaeb-dabc-561c-b889-116698346e31", "Elinor H Thiry"],
  ["25c682d2-ac73-579c-9649-94922301241b", "Richard E Thistle"],
  ["b2a79e77-4935-54dd-9c61-df4ea777464d", "Paul Thole"],
  ["53f5f040-5e44-5067-a8b9-64902fd75d8c", "Lawrence C Tholey"],
  ["84de4a5d-043b-58d6-996a-5d23ff1f77df", "Calvin E Tholson"],
  ["4e994f47-5541-52d0-aba8-3fe93334198e", "Corcoran Thom"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 948 publishes all 23 audited rows with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Sotiris Theodorou separates Army pathway, civilian occupation and student affiliation", async ({ request, page }) => {
  const person = (await peopleShard(request, "s")).find(
    (item: { person_id: string }) => item.person_id === "abafc141-5add-5adc-83dd-98e30147d32c",
  );
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found", commissioned_officer: false });
  expect(person.immediate_pre_oss_affiliations).toEqual([expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment", temporal_basis: "explicit_immediate" })]);
  expect(person.last_civilian_pre_service).toEqual([expect.objectContaining({ canonical_organization: null, occupation: "lawyer and contractor", claim_confidence: "high" })]);
  expect(person.other_pre_oss_affiliations).toEqual([expect.objectContaining({ canonical_organization: "National and Kapodistrian University of Athens", relationship_type: "student" })]);
  await page.goto("./people/abafc141-5add-5adc-83dd-98e30147d32c/");
  await expect(page.locator("main")).toContainText("lawyer and contractor");
});

test("Alphonse Thiele publishes confirmed Camp Mackall pathway and unnamed machinist occupation", async ({ request, page }) => {
  const person = (await peopleShard(request, "a")).find(
    (item: { person_id: string }) => item.person_id === "7e18000b-32d7-5c97-a54f-8bb955fc1eae",
  );
  expect(person).toMatchObject({ identity_status: "confirmed", personnel_category: "commissioned_army_officer", commissioned_officer: true });
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({ canonical_organization: "United States Army", relationship_type: "military_assignment", temporal_basis: "explicit_immediate", claim_confidence: "confirmed" });
  expect(person.last_civilian_pre_service[0]).toMatchObject({ canonical_organization: null, occupation: "machinist", claim_confidence: "confirmed" });
  await page.goto("./people/7e18000b-32d7-5c97-a54f-8bb955fc1eae/");
  const main = page.locator("main");
  await expect(main).toContainText("Camp Mackall");
  await expect(main).toContainText("machinist");
});

test("Corcoran Thom publishes Riggs only as last civilian employer before wartime service", async ({ request }) => {
  const person = (await peopleShard(request, "c")).find(
    (item: { person_id: string }) => item.person_id === "4e994f47-5541-52d0-aba8-3fe93334198e",
  );
  expect(person).toMatchObject({ identity_status: "high_confidence", commissioned_officer: true });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([expect.objectContaining({ canonical_organization: "Riggs National Bank", relationship_type: "employment", start_date: "1928", end_date: null })]);
});

test("Army categories remain qualified and code 993 remains unpublished", async ({ request }) => {
  const cases = [
    ["c", "7f3c14f8-1069-50e5-a05a-0bc958ba9316", "waiter or waitress, except private family"],
    ["t", "d905ceb1-67b5-561e-b232-080b02cb81fc", "accountant or auditor"],
    ["a", "698e35ea-2c1b-5ef5-bbc1-0538dbae0ba2", "machinist"],
    ["r", "e336d001-148e-529d-89c5-8f9ac23b9545", "draftsman"],
    ["l", "53f5f040-5e44-5067-a8b9-64902fd75d8c", "stenographer or typist"],
    ["c", "84de4a5d-043b-58d6-996a-5d23ff1f77df", "farm hand on a general farm"],
  ] as const;
  for (const [letter, id, occupation] of cases) {
    const person = (await peopleShard(request, letter)).find((item: { person_id: string }) => item.person_id === id);
    expect(person.other_pre_oss_affiliations[0]).toMatchObject({ canonical_organization: null, occupation, claim_confidence: "medium" });
  }
  const edison = (await peopleShard(request, "e")).find(
    (item: { person_id: string }) => item.person_id === "52c9f309-7c41-5afa-a0c1-09dd7f99ab69",
  );
  expect(edison.other_pre_oss_affiliations).toHaveLength(0);
  expect(edison.claims).toHaveLength(1);
});

test("Batch 948 evidence excludes secrets and full protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("32525791");
  expect(evidence).not.toContain("01042727");
});

test("Batch 948 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 648,
    research_attempted_people: 14_745,
    verified_affiliation_people: 1_049,
    verified_employer_people: 471,
    archival_review_assessed_people: 13_219,
    published_claims: 9_165,
    public_sources: 6_016,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Riggs National Bank");
});
