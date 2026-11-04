import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page515-mundy-wright-to-hans-wyner-review_batch-1025_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  wuorinen: ["93dd2d8f-507f-57d5-b146-2e78f31275d3", "John H Wuorinen"],
  wynberg: ["5d6efed7-0465-5d86-bf92-bfa923623d5b", "Hans Wynberg"],
  wylie: ["3890f008-d6f6-5903-9921-31034b37902b", "Betty Jane Wylie"],
  wylly: ["d2cf9c26-f78f-5999-9cd0-e97592fb167d", "Richard D Wylly"],
  robertC: ["266a1510-87a8-5103-bdc8-52ded6feeeb8", "Robert C Wright"],
  robertG: ["fcf1b637-9c4f-5931-9042-ff01317c31fb", "Robert G Wright"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1025 publishes every page 515 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 515);
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

test("Wuorinen publishes Columbia as a high-confidence employer", async ({ request, page }) => {
  const wuorinen = await publicPerson(request, profiles.wuorinen);
  expect(wuorinen).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(wuorinen.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Columbia University",
      relationship_type: "employment",
      claim_confidence: "high",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  await page.goto(`./people/${profiles.wuorinen[0]}/`);
  await expect(page.getByRole("heading", { name: profiles.wuorinen[1], level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Associate Professor of History");
});

test("Wynberg keeps Pfizer employment separate from his Army pathway", async ({ request, page }) => {
  const wynberg = await publicPerson(request, profiles.wynberg);
  expect(wynberg).toMatchObject({ identity_status: "confirmed", research_status: "verified_employer_found" });
  expect(wynberg.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment" }),
  ]);
  expect(wynberg.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Charles Pfizer & Co.", relationship_type: "employment", claim_confidence: "high" }),
  ]);
  await page.goto(`./people/${profiles.wynberg[0]}/`);
  await expect(page.locator("main")).toContainText("Charles Pfizer & Co.");
  await expect(page.locator("main")).toContainText("United States Army");
});

test("Wylie's General Mills claim remains visibly qualified", async ({ request, page }) => {
  const wylie = await publicPerson(request, profiles.wylie);
  expect(wylie.research_status).toBe("documented_prewar_employer_found");
  expect(wylie.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "General Mills, Inc.", claim_confidence: "medium", temporal_basis: "explicit_immediate" }),
  ]);
  await page.goto(`./people/${profiles.wylie[0]}/`);
  await expect(page.locator("main")).toContainText("General Mills");
  await expect(page.locator("main")).toContainText("medium");
});

test("the two Robert Wright rows remain separate, conflicted, and safely grouped", async ({ request }) => {
  const robertC = await publicPerson(request, profiles.robertC);
  const robertG = await publicPerson(request, profiles.robertG);
  expect(robertC.person_id).not.toBe(robertG.person_id);
  expect(robertC.identity_status).toBe("conflicting");
  expect(robertG.identity_status).toBe("conflicting");
  expect(robertC.possible_duplicate_group).toBe(robertG.possible_duplicate_group);
  expect(robertC.possible_duplicate_group).toMatch(/^duplicate-[0-9a-f]{12}$/);
  expect(robertC.possible_duplicate_group).not.toContain("identifier");
  expect(robertC.claims).toHaveLength(0);
  expect(robertG.claims).toHaveLength(0);
});

test("Wylly's Marine evidence is military assignment, not civilian employment", async ({ request, page }) => {
  const wylly = await publicPerson(request, profiles.wylly);
  expect(wylly).toMatchObject({ personnel_category: "commissioned_marine_corps_officer", commissioned_officer: true });
  expect(wylly.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Marine Corps", relationship_type: "military_assignment" }),
  ]);
  expect(wylly.last_civilian_pre_service).toHaveLength(0);
  await page.goto(`./people/${profiles.wylly[0]}/`);
  await expect(page.locator("main")).toContainText("United States Marine Corps");
});

test("Batch 1025 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});
