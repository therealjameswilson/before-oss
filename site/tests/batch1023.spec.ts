import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page513-william-wood-to-perry-woosley-review_batch-1023_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  woodhouse: ["b3045f6a-2338-5298-b5eb-b0e1cc04eefb", "Christopher M Woodhouse"],
  woolbert: ["27dfd47b-0c66-5d10-8b61-10a07d7b549f", "Robert G Woolbert"],
  woolcock: ["e18fcc1d-d6de-5baf-945e-fc1a766993b4", "Iris Woolcock"],
  samA: ["b004796b-b64c-501a-839e-4d13e2dd1144", "Sam A Woolington"],
  samS: ["798d27bb-223f-538c-bb58-9b965dc3789c", "Sam S Woolington"],
  woolley: ["93df2242-7184-577e-b648-d2b2ff830364", "H.G.A. Woolley"],
  woolverton: ["90f77e6d-ed3b-5148-8cd3-a96ab0779541", "William H Woolverton"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1023 publishes every page 513 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 513);
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

test("Woodhouse and Woolley publish military pathways without inventing civilian employers", async ({ request }) => {
  const woodhouse = await publicPerson(request, profiles.woodhouse);
  expect(woodhouse).toMatchObject({ identity_status: "high_confidence", personnel_category: "foreign_or_allied_military_personnel", commissioned_officer: true });
  expect(woodhouse.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(woodhouse.other_pre_oss_affiliations).toEqual([expect.objectContaining({ relationship_type: "military_assignment" })]);

  const woolley = await publicPerson(request, profiles.woolley);
  expect(woolley).toMatchObject({ identity_status: "confirmed", research_status: "completed", allied_or_foreign_personnel: true });
  expect(woolley.immediate_pre_oss_affiliations).toEqual([expect.objectContaining({ canonical_organization: "Royal Navy", relationship_type: "military_assignment" })]);
  expect(woolley.last_civilian_pre_service).toHaveLength(0);
});

test("publication and photography evidence remain non-employment affiliations", async ({ request }) => {
  const woolbert = await publicPerson(request, profiles.woolbert);
  expect(woolbert.research_status).toBe("occupation_only_found");
  expect(woolbert.last_civilian_pre_service).toHaveLength(0);
  expect(woolbert.other_pre_oss_affiliations).toEqual([expect.objectContaining({ relationship_type: "professional_affiliation", canonical_organization: "Foreign Affairs" })]);

  const woolcock = await publicPerson(request, profiles.woolcock);
  expect(woolcock.last_civilian_pre_service).toHaveLength(0);
  expect(woolcock.other_pre_oss_affiliations).toEqual([expect.objectContaining({ relationship_type: "unknown", occupation: "photographer" })]);
});

test("Woolverton separates Army pathway, last civilian work, and earlier employer", async ({ request, page }) => {
  const woolverton = await publicPerson(request, profiles.woolverton);
  expect(woolverton.research_status).toBe("verified_employer_found");
  expect(woolverton.immediate_pre_oss_affiliations).toEqual([expect.objectContaining({ relationship_type: "military_assignment", canonical_organization: "United States Army" })]);
  expect(woolverton.last_civilian_pre_service).toEqual([expect.objectContaining({ relationship_type: "self_employment", occupation: "farm manager" })]);
  expect(woolverton.other_pre_oss_affiliations).toEqual([expect.objectContaining({ canonical_organization: "New York Transfer Company" })]);
  await page.goto(`./people/${profiles.woolverton[0]}/`);
  await expect(page.getByRole("heading", { name: "William H Woolverton", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("family-estate farms");
});

test("Sam A and Sam S Woolington remain separate possible duplicates", async ({ request }) => {
  const samA = await publicPerson(request, profiles.samA);
  const samS = await publicPerson(request, profiles.samS);
  expect(samA.person_id).not.toBe(samS.person_id);
  expect(samA.identity_status).toBe("ambiguous");
  expect(samS.identity_status).toBe("confirmed");
  expect(samA.possible_duplicate_group).toBe(samS.possible_duplicate_group);
});

test("Batch 1023 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});
