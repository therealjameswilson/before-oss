import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page467-william-j-thompson-to-ronald-h-thornley-review_batch-953_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["e80c56d4-d024-5b0c-9cac-33eac8268924", "William J Thompson"],
  ["9e6312c7-2f9a-5521-a32e-be3236e2cc74", "William K Thompson"],
  ["68011b7b-c0c4-5c7a-bd5c-b4a9b917687d", "William T Thompson"],
  ["7b75a41b-3260-5644-bbe7-4e2115fc28c5", "Adeline V Thoms"],
  ["b610a51d-477f-5600-97ca-c5b898435199", "Hans Peter A Thomsen"],
  ["f16981e3-6361-5ec1-9d95-249027dde163", "Archibald G Thomson"],
  ["875f2b0d-2f9d-52cc-93a5-8689c7ac8b84", "Archibald R Thomson"],
  ["551ae1bd-d271-5a8e-88ea-965f0780c8f7", "George G Thomson"],
  ["4940db74-777c-50d6-9067-bd2a32c5f3d3", "James C Thomson"],
  ["a399210a-e1bb-55ad-bf4b-1c6f7778d971", "John S Thomson"],
  ["d048558b-b5c8-5ebc-8c6f-09a751cdf82a", "Robert D Thomson"],
  ["f9ce2aa6-4dae-506c-81b8-bf43212190f9", "Stanley J Thomson"],
  ["bb58f59a-8263-5672-847a-f219dc941904", "Conrad J Thoren"],
  ["2456daf1-03f3-5a6c-9007-e8d330b093ab", "Gordon P Thorigal"],
  ["4d30ffd0-43d2-5611-9cd7-7ea559fcb604", "Reginald Thorlin"],
  ["dfafe96f-62dd-5348-bfe6-d652b36f3422", "Betsy A Thorn"],
  ["7e2b7ced-c34d-5840-821a-1d51657abb78", "Edwin W Thorn"],
  ["04c4b7c0-765e-5cd9-9a59-9cbc54e62177", "Elmers Thornburg"],
  ["1eb0eaa7-9a35-585d-a672-c7f2f61f960f", "Ethel M Thornbury"],
  ["df0d68ba-4870-554d-b2c0-4bb94869670d", "George O Thorne"],
  ["e87dd833-7c90-577a-9a43-3722decf88a9", "Sevia B Thorne"],
  ["7e44bfee-9729-501a-8903-5ce8eeda77fb", "Stewart Thorne"],
  ["adb5a82e-e191-5679-87ee-616cffd41c1a", "Ronald H Thornley"],
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

test("Batch 953 publishes all 23 audited rows with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("four Army matches publish only qualified occupation categories", async ({ request }) => {
  const expected = [
    ["68011b7b-c0c4-5c7a-bd5c-b4a9b917687d", "William T Thompson", "actors and actresses"],
    ["f9ce2aa6-4dae-506c-81b8-bf43212190f9", "Stanley J Thomson", "accountants and auditors"],
    ["e87dd833-7c90-577a-9a43-3722decf88a9", "Sevia B Thorne", "general industry clerks"],
    ["7e44bfee-9729-501a-8903-5ce8eeda77fb", "Stewart Thorne", "paint and varnish producing occupations"],
  ] as const;
  for (const [id, name, occupation] of expected) {
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
        relationship_type: "employment",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    ]);
  }
  const williamJ = await publicPerson(
    request,
    "e80c56d4-d024-5b0c-9cac-33eac8268924",
    "William J Thompson",
  );
  expect(williamJ).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "enlisted_army_personnel",
  });
  expect(williamJ.other_pre_oss_affiliations).toHaveLength(0);
});

test("Ethel M Thornbury publishes two earlier academic employers without claiming immediacy", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "1eb0eaa7-9a35-585d-a672-c7f2f61f960f",
    "Ethel M Thornbury",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(person.name_variants).toContain("Ethel Margaret Thornbury");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Wisconsin-Madison",
      historical_organization: "University of Wisconsin",
      role_title: "associate professor of English",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
    expect.objectContaining({
      canonical_organization: "Barnard College",
      role_title: "visiting associate professor of English",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]);
  await page.goto("./people/1eb0eaa7-9a35-585d-a672-c7f2f61f960f/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Wisconsin");
  await expect(main).toContainText("Barnard College");
  await expect(main).toContainText("no source yet establishes it as immediately before OSS");
});

test("Reginald Thorlin retains student status and an explicit identifier discrepancy", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "4d30ffd0-43d2-5611-9cd7-7ea559fcb604",
    "Reginald Thorlin",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Naval Academy",
      relationship_type: "student",
      end_date: "1937-03-15",
      temporal_basis: "documented_prewar",
    }),
  ]);
  await page.goto("./people/4d30ffd0-43d2-5611-9cd7-7ea559fcb604/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Naval Academy");
  await expect(main).toContainText("protected identifier");
  await expect(main).toContainText("Box 776");
});

test("Gordon P Thorigal publishes a Coast Guard military pathway, not a civilian employer", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "2456daf1-03f3-5a6c-9007-e8d330b093ab",
    "Gordon P Thorigal",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "completed",
    personnel_category: "enlisted_coast_guard_personnel",
    commissioned_officer: false,
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Coast Guard",
      historical_organization: "United States Coast Guard Reserve",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  await page.goto("./people/2456daf1-03f3-5a6c-9007-e8d330b093ab/");
  const main = page.locator("main");
  await expect(main).toContainText("United States Coast Guard Reserve");
  await expect(main).toContainText("military assignment");
  await expect(main).not.toContainText("United States Coast Guard — employer");
});

test("James C Thomson preserves the protected-identifier conflict without transferred facts", async ({ request, page }) => {
  const person = await publicPerson(
    request,
    "4940db74-777c-50d6-9067-bd2a32c5f3d3",
    "James C Thomson",
  );
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
    personnel_category: "unknown_or_indeterminate",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toHaveLength(0);
  await page.goto("./people/4940db74-777c-50d6-9067-bd2a32c5f3d3/");
  await expect(page.locator("main")).toContainText("directly with James C Thomson");
});

test("Batch 953 evidence excludes secrets and protected-identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 953 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 648,
    research_attempted_people: 14_858,
    verified_affiliation_people: 1_053,
    verified_employer_people: 472,
    archival_review_assessed_people: 13_334,
    published_claims: 9_221,
    public_sources: 6_048,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("United States Coast Guard");
});
