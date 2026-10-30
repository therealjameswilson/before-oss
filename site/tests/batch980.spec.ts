import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page480-charles-vanda-to-martha-vandiver-review_batch-980_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["2a85f187-98b0-58de-beab-522352408edc", "Charles Vanda"],
  ["0f666d7f-d608-5049-8bf5-5b04e9e5fbd2", "Clarence H Vandellen"],
  ["add9eae0-db60-5d85-8936-ac4e094d404d", "Hoyt S Vandenberg"],
  ["30c22d38-7915-5f57-8585-292943753050", "John Vandenberg"],
  ["700a7d7e-7517-521b-879d-fa1a15c9ae12", "Louis W Vandenboom"],
  ["474d0397-9a79-50a6-80d2-223567f30d8a", "Amry Vandenbosch"],
  ["a1146a1f-3102-5b31-8565-c93ccc980831", "Paul VanDenstricht"],
  ["c540901c-dce9-5947-b7a7-adda0862a5cc", "John L Vander"],
  ["54cfb556-48df-5b54-a8e5-a1046de51372", "Charles S Vanderblue"],
  ["aeeb28b1-d39c-5902-9069-0b7a8ec59850", "John Vanderleith"],
  ["b333225b-f27a-5e52-8f02-5ba3f178bd43", "Elmer Vanderploeg"],
  ["4497dbbc-43c3-50b9-b0fa-738142ea95f8", "Vivian R Vanderpool"],
  ["b1a6fccf-f0fc-54ed-9659-7626fbcc472d", "John L Vandersys"],
  ["92e98d0c-a0c1-572b-a375-d1291257e81b", "Richard J Vandertie"],
  ["4c7e2eab-b7da-5572-95f5-51866b0da48a", "Arnold Vandervalk"],
  ["2e9ea2cb-128d-55e1-a33d-10c76fd5bf9d", "Rollin N Vandervart"],
  ["afe4e251-3894-5d87-be68-894289c9b3ca", "Ollie R Vandervender"],
  ["faf6f135-3749-5acf-a7ef-e544c2e2b0c5", "Benjamin H Vandervoort"],
  ["63af3f89-4040-5005-8e8d-fdfb323c93bb", "John R Vandervoort"],
  ["a9c9f92d-a305-5d98-a4a6-940de93eb2c8", "John R Vandervoort"],
  ["78af1878-86e8-5ea2-a87a-1ad2f9d18b3f", "Dale S Vandervort"],
  ["b442e752-398e-5eda-b0bf-ed057c6b04d2", "William H Vanderwege"],
  ["c83c2dae-c1eb-5d94-b5cb-124e4b7f0501", "Martha V Vandiver"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 980 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Vanda publishes CBS only as last civilian employer", async ({ request }) => {
  const person = await publicPerson(request, "2a85f187-98b0-58de-beab-522352408edc", "Charles Vanda");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Columbia Broadcasting System",
      role_title: "program manager overseeing Hollywood radio originations",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
    }),
  ]);
});

test("Vandenbosch keeps university employment distinct from State and OSS service", async ({ request }) => {
  const person = await publicPerson(request, "474d0397-9a79-50a6-80d2-223567f30d8a", "Amry Vandenbosch");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Kentucky",
      role_title: "department head and professor of political science",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
    }),
  ]);
});

test("official Army bridges publish occupations or student status, never employers", async ({ request }) => {
  const expected = [
    ["30c22d38-7915-5f57-8585-292943753050", "John Vandenberg", "actor or actress", "unknown"],
    ["a9c9f92d-a305-5d98-a4a6-940de93eb2c8", "John R Vandervoort", "student", "student"],
    ["78af1878-86e8-5ea2-a87a-1ad2f9d18b3f", "Dale S Vandervort", "paymaster, payroll clerk, or timekeeper", "unknown"],
  ] as const;
  for (const [id, name, occupation, relationship] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("official identity and OSS-role findings do not invent pre-OSS affiliations", async ({ request }) => {
  const expected = [
    ["add9eae0-db60-5d85-8936-ac4e094d404d", "Hoyt S Vandenberg", "confirmed"],
    ["54cfb556-48df-5b54-a8e5-a1046de51372", "Charles S Vanderblue", "high_confidence"],
    ["4c7e2eab-b7da-5572-95f5-51866b0da48a", "Arnold Vandervalk", "high_confidence"],
    ["b442e752-398e-5eda-b0bf-ed057c6b04d2", "William H Vanderwege", "confirmed"],
  ] as const;
  for (const [id, name, identityStatus] of expected) {
    const person = await publicPerson(request, id, name);
    expect(person.identity_status).toBe(identityStatus);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("duplicate candidates and unbridged namesakes remain separate and affiliation-free", async ({ request }) => {
  const noIdentifierJohn = await publicPerson(request, "63af3f89-4040-5005-8e8d-fdfb323c93bb", "John R Vandervoort");
  const identifiedJohn = await publicPerson(request, "a9c9f92d-a305-5d98-a4a6-940de93eb2c8", "John R Vandervoort");
  expect(noIdentifierJohn).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(identifiedJohn).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(noIdentifierJohn.other_pre_oss_affiliations).toHaveLength(0);
  expect(identifiedJohn.other_pre_oss_affiliations).toHaveLength(1);

  for (const [id, name] of [
    ["a1146a1f-3102-5b31-8565-c93ccc980831", "Paul VanDenstricht"],
    ["faf6f135-3749-5acf-a7ef-e544c2e2b0c5", "Benjamin H Vandervoort"],
    ["c83c2dae-c1eb-5d94-b5cb-124e4b7f0501", "Martha V Vandiver"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person.identity_status).toBe("ambiguous");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Batch 980 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 980 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 668,
    research_attempted_people: 15_475,
    verified_affiliation_people: 1_117,
    verified_employer_people: 503,
    archival_review_assessed_people: 13_951,
    published_claims: 9_835,
    public_sources: 6_367,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
