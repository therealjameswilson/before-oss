import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page517-janet-yasunobu-to-merle-youkers-review_batch-1027_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  yempuku: ["0518eb8d-5e87-5981-b79f-87a99ab16913", "Ralph T Yempuku"],
  yerkes: ["515353ea-5df4-517e-a6b0-5eaf7ebce805", "David N Yerkes"],
  yinkley: ["d6481f01-cfb1-54a5-a5aa-e60ea88842e3", "Arden Yinkley Jr."],
  yokoi: ["e2220125-5fb2-59df-9dea-d25fdef05c97", "Jutaro Yokoi"],
  yoshida: ["15eb879e-4646-5ad8-9f28-6a8376698bc7", "Shizuo Yoshida"],
  yoshihashi: ["e1f44440-4a38-5a4f-9c29-03b5c3c61e3f", "Takehiko Yoshihashi"],
  usuda: ["f50f7fc3-bd26-5601-ad93-be444b0d4eeb", "Usuda Yoshisada"],
  youkers: ["b77cbce7-be3a-5031-97f5-336049318510", "Merle S Youkers"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1027 publishes every page 517 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 517);
      if (rows.length) {
        people += 1;
        sourceRows += rows.length;
        expect(person.research_status).not.toBe("not_started");
        expect(person.research_status).not.toBe("in_progress");
      }
    }
  }
  expect(people).toBe(46);
  expect(sourceRows).toBe(46);
});

test("Yempuku separates the civilian employer from the immediate Army assignment", async ({ request, page }) => {
  const yempuku = await publicPerson(request, profiles.yempuku);
  expect(yempuku).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(yempuku.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "442nd Regimental Combat Team",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(yempuku.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Hawaii",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
  await page.goto(`./people/${profiles.yempuku[0]}/`);
  await expect(page.getByRole("heading", { name: profiles.yempuku[1], level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("442d Regimental Combat Team");
  await expect(page.locator("main")).toContainText("University of Hawaii");
});

test("Yerkes keeps Yale student status separate from a qualified Corps pathway", async ({ request, page }) => {
  const yerkes = await publicPerson(request, profiles.yerkes);
  expect(yerkes).toMatchObject({ identity_status: "high_confidence", research_status: "needs_temporal_review" });
  expect(yerkes.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Corps of Engineers",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(yerkes.last_civilian_pre_service).toHaveLength(0);
  expect(yerkes.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Yale University", relationship_type: "student" }),
  ]);
  await page.goto(`./people/${profiles.yerkes[0]}/`);
  await expect(page.locator("main")).toContainText("Probable immediate");
  await expect(page.locator("main")).toContainText("student");
});

test("Yinkley and Yoshihashi retain unresolved government-to-OSS timing", async ({ request }) => {
  for (const profile of [profiles.yinkley, profiles.yoshihashi]) {
    const person = await publicPerson(request, profile);
    expect(person.research_status).toBe("needs_temporal_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        relationship_type: "government_assignment",
        temporal_basis: "temporal_relation_uncertain",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Yokoi's ministry is a professional affiliation rather than an employer", async ({ request, page }) => {
  const yokoi = await publicPerson(request, profiles.yokoi);
  expect(yokoi).toMatchObject({ identity_status: "probable", research_status: "needs_identity_review" });
  expect(yokoi.last_civilian_pre_service).toHaveLength(0);
  expect(yokoi.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Sage Methodist Church",
      relationship_type: "professional_affiliation",
      publication_status: "publish_qualified",
    }),
  ]);
  await page.goto(`./people/${profiles.yokoi[0]}/`);
  await expect(page.locator("main")).toContainText("pastor and founder");
});

test("The OSS travel order strengthens identity without inventing pre-OSS employers", async ({ request }) => {
  const yoshida = await publicPerson(request, profiles.yoshida);
  const usuda = await publicPerson(request, profiles.usuda);
  for (const person of [yoshida, usuda]) {
    expect(person.identity_status).toBe("high_confidence");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual([expect.objectContaining({ claim_type: "identity" })]);
  }
  expect(usuda.name_variants).toContain("Yoshisada Katoi Usuda");
  expect(usuda.display_name).toBe("Usuda Yoshisada");
});

test("Youkers's conflicting protected identifier transfers no Army evidence", async ({ request }) => {
  const youkers = await publicPerson(request, profiles.youkers);
  expect(youkers).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(youkers.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(youkers.last_civilian_pre_service).toHaveLength(0);
  expect(youkers.other_pre_oss_affiliations).toHaveLength(0);
  expect(youkers.claims).toHaveLength(0);
  expect(youkers.possible_duplicate_group).toMatch(/^duplicate-[0-9a-f]{12}$/);
});

test("Batch 1027 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});
