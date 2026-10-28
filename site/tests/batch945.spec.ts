import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page463-kenneth-s-templeton-to-william-b-terrell-review_batch-945_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["38fea3f1-6703-5843-a83a-e9c248895241", "Kenneth S Templeton"],
  ["10858a8f-fd6f-5c5d-92ad-fe20908f14c0", "Richard Temposky"],
  ["acb250e2-712f-5117-b4e7-6e89a2978fa2", "Edward A Tenenbaum"],
  ["800216a6-97b8-593d-b6ea-f339050a035c", "Gerritt J TenHoor"],
  ["c07e7248-2a98-5259-8bd3-469c0015de5f", "Calvin Tenne"],
  ["136f7d9d-c513-5977-bd5b-81d03c93f2b9", "George E Tenny"],
  ["9c06eb20-7990-5b72-bc6c-4b65c48a9c2b", "Helen B Tenny"],
  ["7cb36e99-9fc4-5677-9211-6250c6e69a2e", "Lloyd S Tenny"],
  ["d8d95892-3f69-510d-aec4-432a43575061", "William W Tennyson"],
  ["265712f9-7f19-5589-8d6b-ceadd8044671", "Bertha H Teper"],
  ["fc4e3ffe-f90f-54c1-bd2d-8a12346960df", "Lazare Teper"],
  ["44a21b4e-d171-557b-bab6-252f31ce8f6e", "Lazare Teper"],
  ["ff8e4a0a-f694-50e0-be9f-98a722feae73", "Douglas Tepper"],
  ["e8090daa-f5cd-53ad-9efb-4d5b3c5b0af6", "Gabriel R Terek"],
  ["23f7873e-68ac-5360-992b-988999c9e6c4", "Ethel M Terhaar"],
  ["22eb9e85-2d7a-53d9-94a0-63b762e5a63f", "Frank J Terhorst"],
  ["3063897d-55a8-59e6-a61a-216167e64d9a", "Virginia H Terhune"],
  ["9f4ca781-6b4d-5eba-b165-b1e7c1cc4612", "Dorothy N Terney"],
  ["6de3f649-54a5-5737-87b9-2f0a1bcf5e20", "Anneilo A Terracciano"],
  ["43bd4912-1519-56ad-93b0-5d990d61e757", "Edwin M Terrell"],
  ["b008145c-0a58-5d63-8cb2-b26439f13726", "Virgil E Terrell"],
  ["f238d457-78c8-5960-985c-b84c7b7586e0", "Walter L Terrell"],
  ["72386b20-f9db-5aa6-80f2-48aad95e24ce", "William B Terrell"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 945 publishes all 23 indexed-row entities with terminal reviewed outcomes", async ({ page }) => {
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

test("Edward Tenenbaum distinguishes education and military service from a civilian employer", async ({ request, page }) => {
  const person = (await peopleShard(request, "e")).find(
    (item: { person_id: string }) => item.person_id === "acb250e2-712f-5117-b4e7-6e89a2978fa2",
  );
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.name_variants).toContain("Edward Adam Tenenbaum");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Yale University", relationship_type: "student" }),
    expect.objectContaining({ canonical_organization: "United States Army Air Forces", relationship_type: "military_assignment" }),
  ]));
  await page.goto("./people/acb250e2-712f-5117-b4e7-6e89a2978fa2/");
  await expect(page.locator("main")).toContainText("Edward Adam Tenenbaum");
});

test("Helen Tenny publishes the Tenny-Tenney and Short Wave Research finding only as qualified", async ({ request, page }) => {
  const person = (await peopleShard(request, "h")).find(
    (item: { person_id: string }) => item.person_id === "9c06eb20-7990-5b72-bc6c-4b65c48a9c2b",
  );
  expect(person.identity_status).toBe("probable");
  expect(person.name_variants).toContain("Helen B. Tenney");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Short Wave Research, Inc.",
    relationship_type: "employment",
    temporal_basis: "explicit_immediate",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
  expect(person.last_civilian_pre_service).toHaveLength(1);
  await page.goto("./people/9c06eb20-7990-5b72-bc6c-4b65c48a9c2b/");
  await expect(page.locator("main")).toContainText("Probable identity");
  await expect(page.locator("main")).toContainText("Short Wave Research");
});

test("the two Lazare Teper rows remain separate and evidence is not transferred", async ({ request }) => {
  const people = await peopleShard(request, "l");
  const identified = people.find(
    (item: { person_id: string }) => item.person_id === "fc4e3ffe-f90f-54c1-bd2d-8a12346960df",
  );
  const unresolved = people.find(
    (item: { person_id: string }) => item.person_id === "44a21b4e-d171-557b-bab6-252f31ce8f6e",
  );
  expect(identified.possible_duplicate_group).toBe(unresolved.possible_duplicate_group);
  expect(identified.identity_status).toBe("high_confidence");
  expect(identified.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "International Ladies' Garment Workers' Union",
      role_title: "founding director of the Research Department",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
    }),
  ]));
  expect(identified.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(unresolved.identity_status).toBe("ambiguous");
  expect(unresolved.research_status).toBe("needs_identity_review");
  expect(unresolved.other_pre_oss_affiliations).toHaveLength(0);
  expect(unresolved.claims).toHaveLength(0);
});

test("Ethel Terhaar remains a probable earlier-employment finding", async ({ request }) => {
  const person = (await peopleShard(request, "e")).find(
    (item: { person_id: string }) => item.person_id === "23f7873e-68ac-5360-992b-988999c9e6c4",
  );
  expect(person.identity_status).toBe("probable");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "University of Minnesota",
    role_title: "clerk-stenographer",
    temporal_basis: "documented_prewar",
    identity_confidence: "probable",
    claim_confidence: "medium",
    publication_status: "publish_qualified",
  });
});

test("reviewed Army occupation categories remain unnamed and are not employers", async ({ request }) => {
  const cases = [
    ["g", "e8090daa-f5cd-53ad-9efb-4d5b3c5b0af6", "skilled occupation in the manufacture of miscellaneous products"],
    ["a", "6de3f649-54a5-5737-87b9-2f0a1bcf5e20", "semiskilled occupation in mechanical treatment of metals"],
    ["w", "72386b20-f9db-5aa6-80f2-48aad95e24ce", "secondary-school teacher or principal"],
  ] as const;
  for (const [letter, id, occupation] of cases) {
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
      claim_confidence: "medium",
    });
  }
});

test("Batch 945 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Short Wave Research");
});

test("Batch 945 evidence excludes credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 945 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 642,
    research_attempted_people: 14_676,
    verified_affiliation_people: 1_044,
    verified_employer_people: 470,
    archival_review_assessed_people: 13_150,
    published_claims: 9_096,
    public_sources: 5_990,
  });
});
