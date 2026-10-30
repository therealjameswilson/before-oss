import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page482-william-verback-to-frederick-vetlesen-review_batch-984_2026-10-31.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["2dac46d2-9b5d-5730-acb6-23290829a089", "William Verback"],
  ["001e9673-0fc6-5dce-8429-abcf0e475057", "Madeline Verga"],
  ["f130b15b-0575-58cc-8929-9fa5bea41b7e", "Francis C Verger"],
  ["7d7ba9de-cab0-5a67-bd1b-582ad1123eac", "George W Verghis"],
  ["4b0ba62d-83e4-552e-8adc-0330ebce47ee", "Henri L Vergon"],
  ["e29bb927-f990-5078-ac90-68fcb0e38634", "George M Verhaeghe"],
  ["97ba01a2-5b0c-5d2b-9b34-a62d709313d6", "Joseph P Verkamp"],
  ["fb8792f6-08ec-586f-99b9-9790913e5ff4", "Robert L Verlin"],
  ["d147ce88-5433-52e2-a501-9cf351a625a5", "Robert J Vermillion"],
  ["359d97f4-5f6d-58ed-b8fa-f11f6ed4bef0", "Frank Vernon"],
  ["eddd5dcf-bf46-54cb-b9e7-3f681a4ad351", "Robert L Vernon"],
  ["342a327e-add8-548f-b7fa-10a3a1c18940", "Joseph R Verreault"],
  ["cda23c4c-3ae2-585f-9b79-f597967a8f66", "Robinson Verrill"],
  ["6847cada-7512-51e5-a133-c7cd6a13c3d7", "Margaret Verrnay"],
  ["b435df81-7601-52f3-a167-211173b83f8e", "Irving A Verschoor"],
  ["cf546e55-06b5-5eb2-82a7-9f264e930744", "Marcel Verzeano"],
  ["55337c5f-4136-5242-b58d-ba8372a9f01c", "Joseph Veselinovich"],
  ["3ca4b213-c8ba-56c1-807e-0296b80429fe", "Erik J Vesely"],
  ["cc7777d3-a62d-5a6f-9243-6a726dda4fba", "John W Vest"],
  ["b9932397-4c76-5442-bcfd-9875324e5c76", "James O Vestal"],
  ["f632036c-0896-5d74-bc26-a7e2c699d503", "Carolyn B Vester"],
  ["ab78876d-899a-55db-98f8-03ff916bf315", "Eliot N Vestner"],
  ["aa2df4e4-b97f-51cf-999d-d600620f6366", "Frederick Vetlesen"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 984 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Army bridges publish broad occupations without inventing employers", async ({ request }) => {
  const expected = [
    ["fb8792f6-08ec-586f-99b9-9790913e5ff4", "Robert L Verlin", "photographer"],
    ["d147ce88-5433-52e2-a501-9cf351a625a5", "Robert J Vermillion", "checker"],
    ["eddd5dcf-bf46-54cb-b9e7-3f681a4ad351", "Robert L Vernon", "salesperson"],
    ["cf546e55-06b5-5eb2-82a7-9f264e930744", "Marcel Verzeano", "physician or surgeon"],
    ["cc7777d3-a62d-5a6f-9243-6a726dda4fba", "John W Vest", "textile-manufacturing occupation, not elsewhere classified"],
    ["b9932397-4c76-5442-bcfd-9875324e5c76", "James O Vestal", "cook, except in a private family"],
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

test("Verkamp and Verzeano preserve distinct student, occupation and rescue affiliations", async ({ request }) => {
  const verkamp = await publicPerson(request, "97ba01a2-5b0c-5d2b-9b34-a62d709313d6", "Joseph P Verkamp");
  expect(verkamp).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(verkamp.last_civilian_pre_service).toHaveLength(0);
  expect(verkamp.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "University of Cincinnati",
      role_title: "engineering student",
      relationship_type: "student",
      claim_confidence: "high",
    }),
  ]));

  const verzeano = await publicPerson(request, "cf546e55-06b5-5eb2-82a7-9f264e930744", "Marcel Verzeano");
  expect(verzeano.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Centre américain de secours", relationship_type: "professional_affiliation" }),
    expect.objectContaining({ canonical_organization: null, occupation: "physician or surgeon", publication_status: "publish_qualified" }),
  ]));
});

test("Verrill, Vestner and Vetlesen keep their confidence and temporal limits visible", async ({ request }) => {
  const verrill = await publicPerson(request, "cda23c4c-3ae2-585f-9b79-f597967a8f66", "Robinson Verrill");
  expect(verrill).toMatchObject({ identity_status: "probable", research_status: "documented_prewar_employer_found" });
  expect(verrill.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Verrill, Hale, Booth & Ives", claim_confidence: "medium", temporal_basis: "documented_prewar" }),
  ]));

  const vestner = await publicPerson(request, "ab78876d-899a-55db-98f8-03ff916bf315", "Eliot N Vestner");
  expect(vestner).toMatchObject({ identity_status: "high_confidence", research_status: "completed", commissioned_officer: true });
  expect(vestner.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment", temporal_basis: "probable_immediate", claim_confidence: "medium" }),
  ]);

  const vetlesen = await publicPerson(request, "aa2df4e4-b97f-51cf-999d-d600620f6366", "Frederick Vetlesen");
  expect(vetlesen).toMatchObject({ identity_status: "confirmed", research_status: "requires_archival_review", commissioned_officer: true });
  expect(vetlesen.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(vetlesen.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "confirmed", publication_status: "published" }),
    expect.objectContaining({ claim_type: "occupation", claim_confidence: "medium", publication_status: "publish_qualified" }),
  ]));
});

test("the protected-identifier conflict remains separate and public-safe", async ({ request }) => {
  const veselinovich = await publicPerson(request, "55337c5f-4136-5242-b58d-ba8372a9f01c", "Joseph Veselinovich");
  expect(veselinovich).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources", commissioned_officer: true });
  expect(veselinovich.possible_duplicate_group).toMatch(/^duplicate-[a-f0-9]{12}$/);
  expect(veselinovich.possible_duplicate_group).not.toMatch(/\d{7,9}/);
  expect(veselinovich.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(veselinovich.last_civilian_pre_service).toHaveLength(0);
  expect(veselinovich.other_pre_oss_affiliations).toHaveLength(0);
});

test("unbridged Batch 984 people remain affiliation-free archival cases", async ({ request }) => {
  const names = new Set([
    "William Verback", "Madeline Verga", "Francis C Verger", "Henri L Vergon", "George M Verhaeghe",
    "Frank Vernon", "Joseph R Verreault", "Margaret Verrnay", "Irving A Verschoor", "Erik J Vesely", "Carolyn B Vester",
  ]);
  for (const [id, name] of profiles.filter(([, name]) => names.has(name))) {
    const person = await publicPerson(request, id, name);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Batch 984 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 984 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 670,
    research_attempted_people: 15_565,
    verified_affiliation_people: 1_122,
    verified_employer_people: 504,
    archival_review_assessed_people: 14_041,
    published_claims: 9_919,
    public_sources: 6_405,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
