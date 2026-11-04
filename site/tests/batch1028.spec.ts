import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page518-cecile-youmanns-to-renie-yuen-review_batch-1028_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  billy: ["0ab2055a-bbd9-5e7e-8c64-df1be9ae4073", "Billy B Young"],
  cuyler: ["2a713c79-9136-5570-a860-487b8f8d9730", "Cuyler T Young"],
  jamesB: ["a1b5ac23-70e5-5d15-b958-eb13f0df4cf1", "James B Young"],
  rodney: ["3875835c-ef00-57d8-8ffd-dd1e7eed5857", "Rodney S Young"],
  richard: ["84daf75f-418f-5a3a-943f-59520de47f1d", "Richard K Young"],
  evelle: ["e8b40847-8897-5d2a-8d44-03dbd47d705f", "Evelle J Younger"],
  williamYoungs: ["2b34c859-063a-59e1-83f4-3d11a3ef16fb", "William E Youngs"],
  peter: ["a859c7a1-daa0-5e28-8fba-ff3236d4cf26", "Peter, Dr. Yovanovich"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1028 publishes every page 518 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 518);
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

test("Cuyler Young has a supported Toronto employer without inferred end dates", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.cuyler);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.name_variants).toContain("T. Cuyler Young");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Toronto",
      relationship_type: "employment",
      start_date: "1938",
      end_date: null,
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(1);
  await page.goto(`./people/${profiles.cuyler[0]}/`);
  await expect(page.getByRole("heading", { name: profiles.cuyler[1], level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("University of Toronto");
});

test("Evelle Younger preserves FBI service as federal employment and immediate affiliation", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.evelle);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Federal Bureau of Investigation",
      relationship_type: "government_assignment",
      end_date: null,
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(1);
  await page.goto(`./people/${profiles.evelle[0]}/`);
  await expect(page.locator("main")).toContainText("section chief; Special Agent");
});

test("Rodney Young's volunteer pathway is not recast as employment", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.rodney);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "requires_archival_review" });
  expect(person.name_variants).toContain("Rodney Stuart Young");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Greek Red Cross",
      relationship_type: "volunteer",
      last_civilian_pre_service: false,
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "American School of Classical Studies at Athens",
      relationship_type: "professional_affiliation",
    }),
  ]);
  await page.goto(`./people/${profiles.rodney[0]}/`);
  await expect(page.locator("main")).toContainText("volunteer ambulance driver");
});

test("Peter Yovanovich preserves indexed order and publishes occupation without an employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.peter);
  expect(person.display_name).toBe("Peter, Dr. Yovanovich");
  expect(person.name_variants).toContain("Dr. Peter Yovanovich");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "physician",
      role_title: "medico",
      relationship_type: "unknown",
      end_date: null,
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto(`./people/${profiles.peter[0]}/`);
  await expect(page.locator("main")).toContainText("physician");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("Petroleum-coded occupations do not create oil-company employers", async ({ request }) => {
  for (const profile of [profiles.richard, profiles.williamYoungs]) {
    const person = await publicPerson(request, profile);
    expect(person.research_status).toBe("occupation_only_found");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        relationship_type: "unknown",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("Postwar and undefined Army codes remain identity evidence only", async ({ request }) => {
  for (const profile of [profiles.billy, profiles.jamesB]) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual([expect.objectContaining({ claim_type: "identity" })]);
  }
});

test("Batch 1028 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});
