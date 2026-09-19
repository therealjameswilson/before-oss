import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const stats = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/stats.json", import.meta.url), "utf8"),
);
const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page-one-hundred-and-fifteen-christian-desorbier-through-raymond-deston_batch-573_2026-09-19.json",
    import.meta.url,
  ),
  "utf8",
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

const cohort = [
  ["32f23b6d-a799-59b7-9eda-46a6fc7f49f4", "Christian DeSorbier", "dd39dd8a-dca4-56fe-952a-8aeeff90e9c1", "182", "Lt", false],
  ["a7988d87-9dad-53a1-91f6-65dbafad31ee", "Emile F Desormier", "c90ea87f-0234-5af9-933c-58bd5c6189e8", "182", "Cpl", true],
  ["92bf4459-408e-5f1e-a69a-f5f05cf58f9b", "Frank J Desota", "0d35b72f-cc28-5913-88f3-a14ee871befa", "182", null, true],
  ["7b1b530b-f4e7-5e70-a618-d3747eed3742", "Michel E Despax", "1cf73b85-4a83-53a9-802d-0dc0dadc65c4", "182", null, false],
  ["dea984f4-584d-5b6e-b5e5-640897b3b40c", "Rene Despax", "14894f3d-84af-530a-8c18-660d72c962ea", "182", "Lt Col", false],
  ["7c2a5414-0200-59e8-a6d4-0362e52975d4", "Gabriel H Desplaines", "c284b42f-a225-5650-ad5c-3009be59a605", "183", null, true],
  ["ae91f5d4-44b6-5096-89e9-9f6debbf5a24", "Emile Despres", "1e2569fd-155e-5fac-b09e-4b7ce8e8dbcc", "183", null, false],
  ["c4bf8ffb-b608-54e0-8bdf-4f727409af0b", "Jean P Desroberts", "00e96b50-2231-5e67-b738-9ff2cd3b9985", "183", null, true],
  ["89fffaf0-2b34-5343-aa1c-dfb7c39f4e50", "Dorothy G Dessin", "eb5781c9-7578-51f1-9f9b-61e4f42de670", "183", null, false],
  ["b6886b80-62ec-5ae0-8b78-d7af99b31c0f", "Raymond Deston", "d2f067c9-96cb-5a95-a2dc-0571cc9b3736", "183", null, false],
] as const;

test("Batch 573 retains every indexed row, box transition and private-value masking", () => {
  for (const [id, name, sourceRecordId, box, rank, hasPrivateIdentifier] of cohort) {
    const person = profile(id);
    expect(person.display_name).toBe(name);
    const record = person.source_records.find(
      (row: { source_record_id: string }) => row.source_record_id === sourceRecordId,
    );
    expect(record).toMatchObject({
      pdf_page: 115,
      box,
      archive_location: box === "182" ? "230/86/29/07" : "230/86/30/01",
      rank_as_indexed: rank,
    });
    if (hasPrivateIdentifier) {
      expect(record.serial_masked).toMatch(/^•+\d{4}$/);
    } else {
      expect(record.serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
  expect(evidence).not.toMatch(/"serial_number"|"serial_number_raw"|"serial_number_normalized"/);
});

test("Batch 573 separates French identity triangulation from unproven immediate affiliation", () => {
  const christian = profile("32f23b6d-a799-59b7-9eda-46a6fc7f49f4");
  const rene = profile("dea984f4-584d-5b6e-b5e5-640897b3b40c");
  for (const person of [christian, rene]) {
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      personnel_category: "foreign_or_allied_military_personnel",
      commissioned_officer: true,
      research_status: "requires_archival_review",
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }
  expect(christian.name_variants).toContain("Christian de Sorbier de Pougnadoresse");
  expect(rene.name_variants).toContain("René Louis Auguste Despax");
  expect(JSON.stringify(rene)).toContain("René Jules Despax");
  expect(JSON.stringify(rene)).not.toContain("Guynemer as an immediate");
});

test("Batch 573 publishes three Army-entry occupations but no invented employer", () => {
  for (const [id, occupation, confidence] of [
    ["a7988d87-9dad-53a1-91f6-65dbafad31ee", "Chauffeur or bus, taxi, truck or tractor driver", "confirmed"],
    ["7c2a5414-0200-59e8-a6d4-0362e52975d4", "General office clerk", "confirmed"],
    ["c4bf8ffb-b608-54e0-8bdf-4f727409af0b", "Machinist", "high"],
  ] as const) {
    const person = profile(id);
    expect(person.research_status).toBe("occupation_only_found");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        occupation,
        canonical_organization: null,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: confidence,
      }),
    ]);
    expect(JSON.stringify(person)).toContain(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 573 qualifies Deston's 1941 insurance lead and keeps postwar firm out of prewar claims", () => {
  const raymond = profile("b6886b80-62ec-5ae0-8b78-d7af99b31c0f");
  expect(raymond).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "commissioned_naval_officer",
    commissioned_officer: true,
    research_status: "occupation_only_found",
  });
  expect(raymond.immediate_pre_oss_affiliations).toEqual([]);
  expect(raymond.last_civilian_pre_service).toEqual([]);
  expect(raymond.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      occupation: "Insurance work",
      relationship_type: "unknown",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(JSON.stringify(raymond)).toContain("Central Information Division");
  expect(raymond.claims.some((claim: { claim_text: string }) =>
    claim.claim_text.includes("John Hancock"),
  )).toBe(false);
});

test("Batch 573 leaves ambiguous and unresolved names as archival-review profiles", () => {
  for (const id of [
    "92bf4459-408e-5f1e-a69a-f5f05cf58f9b",
    "7b1b530b-f4e7-5e70-a618-d3747eed3742",
    "89fffaf0-2b34-5343-aa1c-dfb7c39f4e50",
  ]) {
    const person = profile(id);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toHaveLength(1);
  }
  expect(profile("7b1b530b-f4e7-5e70-a618-d3747eed3742").identity_status).toBe("ambiguous");
  const desota = profile("92bf4459-408e-5f1e-a69a-f5f05cf58f9b");
  const desuta = profile("918c8146-4378-5171-b6a6-71f0a185c63a");
  expect(desota.possible_duplicate_group).toMatch(/^duplicate-/);
  expect(desuta.possible_duplicate_group).toBe(desota.possible_duplicate_group);
  expect(desuta.research_status).toBe("not_started");
  expect(desuta.person_id).not.toBe(desota.person_id);
});

test("Batch 573 retains the earlier Emile Despres employer and exact coverage denominators", () => {
  const emile = profile("ae91f5d4-44b6-5096-89e9-9f6debbf5a24");
  expect(emile.research_status).toBe("verified_employer_found");
  expect(JSON.stringify(emile)).toContain("Federal Reserve Board");
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23940,
    possible_duplicate_groups: 256,
    research_attempted_people: 5495,
    verified_affiliation_people: 596,
    verified_employer_people: 260,
    archival_review_assessed_people: 5450,
  });
});

test("Batch 573 direct profile URLs render qualified findings and archival guidance", async ({ page }) => {
  await page.goto("people/b6886b80-62ec-5ae0-8b78-d7af99b31c0f/");
  await expect(page.getByRole("heading", { name: "Raymond Deston", exact: true })).toBeVisible();
  await expect(page.getByText("Insurance work", { exact: true }).first()).toBeVisible();
  await expect(page.getByText(/No reliable pre-OSS employer has yet been identified/).first()).toBeVisible();

  await page.goto("people/dea984f4-584d-5b6e-b5e5-640897b3b40c/");
  await expect(page.getByRole("heading", { name: "Rene Despax", exact: true })).toBeVisible();
  await expect(page.getByText(/René Louis Auguste Despax/).first()).toBeVisible();
  await expect(page.getByText(/No reliable pre-OSS employer has yet been identified/).first()).toBeVisible();
});
