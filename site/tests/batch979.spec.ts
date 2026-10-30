import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page480-elizabeth-van-kuyk-to-robert-vance-review_batch-979_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["fb3e8af2-3eae-5f71-a06a-2904d98f2713", "Elizabeth Van Kuyk"],
  ["06727acb-210c-530c-b3d2-89669ee76e47", "Rene W Van Lacke"],
  ["984c6f78-7ba5-53be-8291-587a9d28b756", "Piet Van Leer"],
  ["74658c63-7063-50dd-80e3-fc8fe12c23c0", "R V Van Liew"],
  ["e240bfb5-a20e-5627-abe5-83e29e6125f6", "Robert L Van Nice"],
  ["278e9f10-8396-5443-9dfe-c9418f5951e8", "Leonard M Van Noppen"],
  ["f2cf633f-617a-53fd-bcb7-600722b3638a", "Winifred M Van Patter"],
  ["9f97d996-8a72-5f90-b67e-3509147fd391", "Alex Van Praag"],
  ["de73693e-01b3-50f0-bc95-5a3de7ba626b", "Dollis E Van Roden"],
  ["38e76cc5-6d85-520e-8fe5-77f67f2fecfd", "Peter H Van Scherpe"],
  ["8117f959-f643-505f-b656-e2b7d1821fd0", "* Van Scyloren"],
  ["78082177-5934-590a-9391-3201b6a26439", "Chester F Van Sickle"],
  ["b1783b70-92f1-5dce-b2e2-a289886121cb", "Max W Van Sickle"],
  ["0647d353-da82-5cc5-9f0d-7e132c79d718", "Francis E Van Timmeren"],
  ["a1668642-89d6-5c37-a417-d4a0be299485", "Hubert Van Tol"],
  ["76710072-32d8-5806-ad70-a5b5a51c5fbd", "Donald W Van Treese"],
  ["5c2d05d0-126f-5ad7-bda6-cc6ecb9023c9", "Samuel Van Valkenber"],
  ["257d18cd-9707-51fe-96b6-dae5d64f329f", "Claude W Van Vleet"],
  ["74d44806-10bc-5ab5-a40f-59945ef10f1a", "Howard E Van Winkle Jr."],
  ["9f8f0d7d-1213-5fe1-8f5a-12208d2207cc", "Helen Van Zonnevel"],
  ["a9d5d4ca-9a95-549c-b20a-aacb35bb8ed6", "Johan Adria Van Zuylen"],
  ["5d8a4511-445b-55fd-a3b7-bd61d72ae30c", "Robert J Vanasse"],
  ["3b744079-1ec3-5900-8789-440107b7a057", "Robert G Vance"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 979 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
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

test("Van Nice publishes the project, not a modern institutional substitute", async ({ request }) => {
  const person = await publicPerson(request, "e240bfb5-a20e-5627-abe5-83e29e6125f6", "Robert L Van Nice");
  expect(person).toMatchObject({
    identity_status: "confirmed",
    research_status: "verified_employer_found",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  const expected = expect.objectContaining({
    canonical_organization: "Hagia Sophia architectural survey (William Emerson project)",
    role_title: "architectural surveyor",
    occupation: "architect",
    relationship_type: "employment",
    temporal_basis: "strongly_date_bounded",
    claim_confidence: "confirmed",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([expected]);
  expect(person.last_civilian_pre_service).toEqual([expected]);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Myron Bement Smith Iranian architectural survey",
      role_title: "architectural survey assistant",
      temporal_basis: "documented_prewar",
      claim_confidence: "confirmed",
    }),
  ]));
});

test("Van Valkenber preserves the print form while publishing Clark as last civilian employer", async ({ request }) => {
  const person = await publicPerson(request, "5c2d05d0-126f-5ad7-bda6-cc6ecb9023c9", "Samuel Van Valkenber");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
  });
  expect(person.name_variants).toContain("Samuel Van Valkenburg");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Clark University",
      role_title: "professor of geography",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
    }),
  ]);
});

test("official Army identity bridges publish dated occupations, never employers", async ({ request }) => {
  const expected = [
    ["06727acb-210c-530c-b3d2-89669ee76e47", "Rene W Van Lacke", "paymaster, payroll clerk, or timekeeper"],
    ["74658c63-7063-50dd-80e3-fc8fe12c23c0", "R V Van Liew", "farm hand on a general farm"],
    ["0647d353-da82-5cc5-9f0d-7e132c79d718", "Francis E Van Timmeren", "metal-products fabrication occupation, not elsewhere classified"],
    ["76710072-32d8-5806-ad70-a5b5a51c5fbd", "Donald W Van Treese", "mechanic or repairman, not elsewhere classified"],
    ["3b744079-1ec3-5900-8789-440107b7a057", "Robert G Vance", "photographer"],
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
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("unbridged namesakes and incomplete names create no public affiliations", async ({ request }) => {
  for (const [id, name] of [
    ["fb3e8af2-3eae-5f71-a06a-2904d98f2713", "Elizabeth Van Kuyk"],
    ["9f97d996-8a72-5f90-b67e-3509147fd391", "Alex Van Praag"],
    ["8117f959-f643-505f-b656-e2b7d1821fd0", "* Van Scyloren"],
    ["b1783b70-92f1-5dce-b2e2-a289886121cb", "Max W Van Sickle"],
    ["a1668642-89d6-5c37-a417-d4a0be299485", "Hubert Van Tol"],
    ["5d8a4511-445b-55fd-a3b7-bd61d72ae30c", "Robert J Vanasse"],
  ] as const) {
    const person = await publicPerson(request, id, name);
    expect(person.identity_status).toBe("ambiguous");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("printed ranks remain classifications without inventing employers", async ({ request }) => {
  const officers = [
    ["278e9f10-8396-5443-9dfe-c9418f5951e8", "Leonard M Van Noppen"],
    ["257d18cd-9707-51fe-96b6-dae5d64f329f", "Claude W Van Vleet"],
  ] as const;
  for (const [id, name] of officers) {
    const person = await publicPerson(request, id, name);
    expect(person.personnel_category).toBe("commissioned_army_officer");
    expect(person.commissioned_officer).toBe(true);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
  }
});

test("Batch 979 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/RA\d{8}/);
});

test("Batch 979 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 667,
    research_attempted_people: 15_452,
    verified_affiliation_people: 1_115,
    verified_employer_people: 501,
    archival_review_assessed_people: 13_928,
    published_claims: 9_821,
    public_sources: 6_354,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
