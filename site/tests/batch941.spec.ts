import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page461-ray-l-tarbox-to-jack-h-tattersall-review_batch-941_2026-10-28.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["a32c26eb-45b9-5881-98c3-251ce3e8ef9d", "Ray L Tarbox"],
  ["5fbf8900-7004-5c7e-a45b-e3836c407c1c", "Laurier R Tardiff"],
  ["72293415-151b-59ef-a265-187a0142a5d2", "John Targakis"],
  ["486a3afa-aa1c-57ff-9741-24860b997a7c", "John Targakis"],
  ["b2496d1b-8659-59c1-aec5-e161411e8658", "Louis Tarmina"],
  ["546541b8-c26f-5c09-ac26-0944ef1e2bf6", "Louis Tarnrinn"],
  ["bc607451-320d-5b9d-be1d-6f83a66b5c00", "Warren J Tarrant"],
  ["1a938ab2-b735-56c3-a1fb-6978403a6f9e", "Frank Tartaro"],
  ["2fc76078-f789-57e7-94a2-48874feb2e51", "Lewis S Taschler"],
  ["7f2e7c76-8491-5d90-8a2b-51142cb65c5a", "Louis J Taschler"],
  ["f61bcdd1-53e6-5a24-9513-90f54c99587c", "Esther Tash"],
  ["dfbbbfd1-a918-5fcc-87d8-82738ce676cf", "Yukio Tashiro"],
  ["4b1ae1aa-6a3e-5488-92d2-413e9ee234c3", "Milton V Tassi"],
  ["1db40257-5dad-5045-a40a-a82ed477a3bf", "Gloria P Tassin"],
  ["a52e7b76-189c-5a38-a441-de5a0e856b8a", "Ennio Tassinari"],
  ["d072f639-f9d3-5fb9-bb0b-fe38d39c295d", "Richard M Tasso"],
  ["73fd75bd-2d47-50a6-938b-485e9f221a78", "Oliver Tassotti"],
  ["fca8f7fa-627c-519c-ac48-9cefd40458b8", "Rudolf Tate"],
  ["7abf6438-df33-506d-a62d-c8182ab24aff", "Solon H Tate"],
  ["363d610c-6a82-5a1f-93a5-52070598fdad", "Solon H Tate"],
  ["3853b443-67c5-570c-bcf0-f2f086aedb71", "Alice Tatham"],
  ["c199732a-da53-5b1e-a740-895d6de73ba1", "Eddison C Tatham"],
  ["18db0105-4a8b-59d3-9b1e-a1425b21307e", "Jack H Tattersall"],
] as const;

async function peopleShard(request: APIRequestContext, letter: string) {
  const response = await request.get(`./data/people/${letter}.json`);
  expect(response.ok()).toBeTruthy();
  return response.json();
}

test("Batch 941 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("Ennio Tassinari keeps ORI as an immediate affiliation rather than an employer", async ({ request, page }) => {
  await page.goto("./people/a52e7b76-189c-5a38-a441-de5a0e856b8a/");
  const main = page.locator("main");
  await expect(main).toContainText("Organizzazione della Resistenza Italiana");
  await expect(main).toContainText("volunteer");
  const person = (await peopleShard(request, "e")).find((item: { person_id: string }) => item.person_id === "a52e7b76-189c-5a38-a441-de5a0e856b8a");
  expect(person.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "Organizzazione della Resistenza Italiana",
    relationship_type: "volunteer",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("the confirmed Solon Tate row alone receives the Army-to-OSS pathway", async ({ request, page }) => {
  const people = await peopleShard(request, "s");
  const unresolved = people.find((item: { person_id: string }) => item.person_id === "7abf6438-df33-506d-a62d-c8182ab24aff");
  const confirmed = people.find((item: { person_id: string }) => item.person_id === "363d610c-6a82-5a1f-93a5-52070598fdad");
  expect(unresolved.identity_status).toBe("ambiguous");
  expect(unresolved.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(confirmed.identity_status).toBe("confirmed");
  expect(confirmed.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    relationship_type: "military_assignment",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "high",
  });
  await page.goto("./people/7abf6438-df33-506d-a62d-c8182ab24aff/");
  await expect(page.locator("main")).toContainText("different protected identifier");
});

test("the two John Targakis rows remain separate identity conflicts", async ({ request, page }) => {
  const people = await peopleShard(request, "j");
  for (const id of ["72293415-151b-59ef-a265-187a0142a5d2", "486a3afa-aa1c-57ff-9741-24860b997a7c"]) {
    const person = people.find((item: { person_id: string }) => item.person_id === id);
    expect(person.identity_status).toBe("ambiguous");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims.some((item: { claim_confidence: string }) => item.claim_confidence === "conflicting")).toBeTruthy();
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("two identical John Targakis rows");
  }
});

test("Army spelling variants remain visible and do not become silent corrections", async ({ request }) => {
  const rudolf = (await peopleShard(request, "r")).find((item: { person_id: string }) => item.person_id === "fca8f7fa-627c-519c-ac48-9cefd40458b8");
  const yukio = (await peopleShard(request, "y")).find((item: { person_id: string }) => item.person_id === "dfbbbfd1-a918-5fcc-87d8-82738ce676cf");
  expect(rudolf.name_variants).toContain("Rudolph Tate");
  expect(yukio.name_variants).toContain("Yudio Tashiro");
  expect(rudolf.display_name).toBe("Rudolf Tate");
  expect(yukio.display_name).toBe("Yukio Tashiro");
});

test("coded Army occupations remain unnamed qualified occupations", async ({ request }) => {
  const louis = (await peopleShard(request, "l")).find((item: { person_id: string }) => item.person_id === "b2496d1b-8659-59c1-aec5-e161411e8658");
  const jack = (await peopleShard(request, "j")).find((item: { person_id: string }) => item.person_id === "18db0105-4a8b-59d3-9b1e-a1425b21307e");
  for (const person of [louis, jack]) {
    expect(person.other_pre_oss_affiliations).toHaveLength(1);
    expect(person.other_pre_oss_affiliations[0].canonical_organization).toBeNull();
    expect(person.other_pre_oss_affiliations[0].claim_confidence).toBe("medium");
    expect(person.last_civilian_pre_service).toHaveLength(0);
  }
});

test("unresolved Batch 941 names receive archival guidance rather than borrowed claims", async ({ request, page }) => {
  await page.goto("./people/a32c26eb-45b9-5881-98c3-251ce3e8ef9d/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold.");
  const person = (await peopleShard(request, "r")).find((item: { person_id: string }) => item.person_id === "a32c26eb-45b9-5881-98c3-251ce3e8ef9d");
  expect(person.identity_status).toBe("unresolved");
  expect(person.claims).toHaveLength(0);
});

test("Batch 941 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Organizzazione della Resistenza Italiana");
});

test("Batch 941 evidence excludes credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 941 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 639,
    research_attempted_people: 14_586,
    verified_affiliation_people: 1_035,
    verified_employer_people: 463,
    archival_review_assessed_people: 13_060,
    published_claims: 9_020,
    public_sources: 5_950,
  });
});
