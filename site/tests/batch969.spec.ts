import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page475-gaston-tuggle-to-euclide-turcotte-review_batch-969_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["56ba9eee-1bb0-5054-a45e-4699f644e0d8", "Gaston E Tuggle"],
  ["5d842394-776f-549a-a6cf-d8c4c3037525", "Donald G Tuinstra"],
  ["a5bf76a7-2699-51ba-af14-6e2d1aa572c3", "Nicholas Tukalo"],
  ["e1bb7d16-57bd-5199-8a64-744c85b4f691", "Sam Tularak"],
  ["4d0ce179-3d73-55b5-b97c-9cf938f35f1c", "Murray A Tulis"],
  ["a48648cb-bc3b-5fcc-9123-b7e9ff3feddf", "Charles O Tulka"],
  ["a0badc47-6594-5946-8e5a-a01e23d0f246", "Robt E Tullen"],
  ["1649ead5-2a9a-5f10-86fe-00dd4b3474bd", "Robert E Tulley"],
  ["0b414d74-66f8-550d-a466-dad5b793fa9f", "Dorothy G Tully"],
  ["26b244ae-83c3-5a4d-8c8b-df1b31174f7a", "Jack A Tully"],
  ["ec8827c8-9bcd-5dbb-89ca-df454bd11cf6", "Joseph J Tully"],
  ["d28301f9-8700-5685-8cbc-6f08462b0663", "Susan Tully"],
  ["93e7815f-bcb2-5a0e-88a2-da7233aab883", "Barney R Tumbiolo"],
  ["384228de-0f41-53e7-8405-f4fbe2000c17", "John W Tumbridge"],
  ["b2afe78f-52cc-56de-88f7-87f6014ba057", "Harry T Tun"],
  ["5bef741a-256e-5848-b824-0147cb9c6653", "Chen Dao Tung"],
  ["4fbbb540-7cbd-5a56-884c-679d4a06c62b", "Annis L Tunis"],
  ["39fcc188-1258-510e-b442-d0cb0828d3b0", "Bill K Tunnel"],
  ["1a7c8fa9-a745-57e2-8fcf-367d049b5318", "Edwin D Tunnell"],
  ["3cfe62b7-af17-5849-b5d9-0e966470945d", "Frederick H Tunnell"],
  ["cdde1d60-e611-5f8b-83c3-b6cb604755c5", "Anthony Turano"],
  ["cdd69d6f-4836-54d4-ad47-bb2001257b3d", "Carmen Turco"],
  ["f58e7cd0-d5c2-57b8-b186-31809a186ffc", "Euclide Turcotte"],
] as const;

const occupationProfiles = [
  ["56ba9eee-1bb0-5054-a45e-4699f644e0d8", "Gaston E Tuggle", "semiskilled worker in dairy-products processing", "unknown", "documented_prewar"],
  ["5d842394-776f-549a-a6cf-d8c4c3037525", "Donald G Tuinstra", "warehousing, storekeeping, handling, loading or unloading worker", "unknown", "documented_prewar"],
  ["1649ead5-2a9a-5f10-86fe-00dd4b3474bd", "Robert E Tulley", "chauffeur or driver of a bus, taxi, truck or tractor", "unknown", "documented_prewar"],
  ["ec8827c8-9bcd-5dbb-89ca-df454bd11cf6", "Joseph J Tully", "student", "student", "documented_prewar"],
  ["93e7815f-bcb2-5a0e-88a2-da7233aab883", "Barney R Tumbiolo", "laundering, cleaning, dyeing or apparel-pressing worker", "unknown", "documented_prewar"],
  ["3cfe62b7-af17-5849-b5d9-0e966470945d", "Frederick H Tunnell", "statistical clerk or compiler", "unknown", "temporal_relation_uncertain"],
  ["cdde1d60-e611-5f8b-83c3-b6cb604755c5", "Anthony Turano", "commercial photographer", "unknown", "documented_prewar"],
  ["f58e7cd0-d5c2-57b8-b186-31809a186ffc", "Euclide Turcotte", "semiskilled textile-manufacturing worker, not elsewhere classified", "unknown", "documented_prewar"],
] as const;

const unresolvedProfiles = [
  ["4d0ce179-3d73-55b5-b97c-9cf938f35f1c", "Murray A Tulis"],
  ["0b414d74-66f8-550d-a466-dad5b793fa9f", "Dorothy G Tully"],
  ["26b244ae-83c3-5a4d-8c8b-df1b31174f7a", "Jack A Tully"],
  ["d28301f9-8700-5685-8cbc-6f08462b0663", "Susan Tully"],
  ["384228de-0f41-53e7-8405-f4fbe2000c17", "John W Tumbridge"],
  ["b2afe78f-52cc-56de-88f7-87f6014ba057", "Harry T Tun"],
  ["5bef741a-256e-5848-b824-0147cb9c6653", "Chen Dao Tung"],
  ["4fbbb540-7cbd-5a56-884c-679d4a06c62b", "Annis L Tunis"],
  ["39fcc188-1258-510e-b442-d0cb0828d3b0", "Bill K Tunnel"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 969 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("eight qualified statuses remain separate from immediate and named-employer claims", async ({ request }) => {
  for (const [id, name, occupation, relationship, temporalBasis] of occupationProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person.research_status).toBe("occupation_only_found");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationship,
        temporal_basis: temporalBasis,
        claim_confidence: "medium",
      }),
    ]));
  }
});

test("Tullen and Tulley remain separate despite the protected-identifier collision", async ({ request }) => {
  const tullen = await publicPerson(request, "a0badc47-6594-5946-8e5a-a01e23d0f246", "Robt E Tullen");
  const tulley = await publicPerson(request, "1649ead5-2a9a-5f10-86fe-00dd4b3474bd", "Robert E Tulley");
  expect(tullen.person_id).not.toBe(tulley.person_id);
  expect(tullen.possible_duplicate_group).toBeTruthy();
  expect(tullen.possible_duplicate_group).toBe(tulley.possible_duplicate_group);
  expect(tullen).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(tullen.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting", publication_status: "conflicting" }),
  ]));
  expect(tulley).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
});

test("Gaston Tuggle has a confirmed Detachment 101 identity without publishing a full identifier", async ({ request }) => {
  const person = await publicPerson(request, "56ba9eee-1bb0-5054-a45e-4699f644e0d8", "Gaston E Tuggle");
  expect(person).toMatchObject({ identity_status: "confirmed", commissioned_officer: false });
  const identityClaim = person.claims.find((claim: { claim_type: string }) => claim.claim_type === "identity");
  expect(identityClaim).toMatchObject({ claim_confidence: "confirmed", publication_status: "published" });
  expect(identityClaim.sources).toEqual(expect.arrayContaining([
    expect.objectContaining({
      source: expect.objectContaining({ stable_url: expect.stringContaining("Detachment%20101") }),
    }),
  ]));
});

test("Anthony Turano is a qualified commercial photographer, not assigned an invented studio employer", async ({ request }) => {
  const person = await publicPerson(request, "cdde1d60-e611-5f8b-83c3-b6cb604755c5", "Anthony Turano");
  expect(person).toMatchObject({ identity_status: "high_confidence", commissioned_officer: true });
  expect(person.name_variants).toEqual(expect.arrayContaining(["Anthony (Tony) Turano", "Tony Turano"]));
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "commercial photographer",
      relationship_type: "unknown",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
});

test("Carmen Turco remains a qualified probable Peedee-team identity", async ({ request }) => {
  const person = await publicPerson(request, "cdd69d6f-4836-54d4-ad47-bb2001257b3d", "Carmen Turco");
  expect(person).toMatchObject({
    identity_status: "probable",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual(expect.arrayContaining([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "medium", publication_status: "publish_qualified" }),
  ]));
});

test("nine unresolved profiles remain dignified archival-review cases", async ({ request }) => {
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

test("the Sam-Sanguan Tularak lead stays withheld pending an identity bridge", async ({ request }) => {
  const person = await publicPerson(request, "e1bb7d16-57bd-5199-8a64-744c85b4f691", "Sam Tularak");
  expect(person).toMatchObject({ identity_status: "ambiguous", research_status: "requires_archival_review" });
  expect(person.claims).toHaveLength(0);
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 969 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 969 publishes exact coverage counters without changing the oil category", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 664,
    research_attempted_people: 15_223,
    verified_affiliation_people: 1_094,
    verified_employer_people: 488,
    archival_review_assessed_people: 13_699,
    published_claims: 9_619,
    public_sources: 6_239,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
