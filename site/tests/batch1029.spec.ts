import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page519-francis-yuhashi-to-joseph-zbeig-review_batch-1029_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  frank: ["4d9f33c3-aedc-5902-ab6b-94e94b9e094a", "Frank V Zabatta"],
  zagier: ["da2f9a29-00f7-5fe5-b7d4-08e69d39087f", "David D Zagier"],
  zagoria: ["d71b8b07-7f93-507d-8942-6ddfbfd27549", "Sylvia B Zagoria"],
  zagorski: ["b1d8132b-5d0d-5df2-90b1-ca768fd3defc", "Wilhelm Zagorski"],
  zaikowsky: ["440f52da-44e6-5029-967b-78b3adbb91d9", "Dim V Zaikowsky"],
  zarembo: ["3e83394b-b3bd-59b3-9e90-9d2c6c36cb23", "Edward B Zarembo"],
  zaret: ["137d7de3-00cf-5560-891d-b6e6ef238c03", "Daniel A Zaret"],
  zatz: ["9f0e97f7-6707-5833-a97a-3c357192915b", "Asa Zatz"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1029 publishes every page 519 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 519);
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

test("Sylvia Zagoria's student status is not recast as employment", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.zagoria);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(person.name_variants).toContain("Sylvia Beatrice Zagoria");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Brooklyn College",
      relationship_type: "student",
      last_civilian_pre_service: false,
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: null, occupation: "dance instructor" }),
  ]);
  await page.goto(`./people/${profiles.zagoria[0]}/`);
  await expect(page.getByRole("heading", { name: profiles.zagoria[1], level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Brooklyn College");
});

test("David Zagier publishes a qualified occupation without inventing an employer", async ({ request }) => {
  const person = await publicPerson(request, profiles.zagier);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "journalist",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: null, occupation: "journalist" }),
  ]);
});

test("Wilhelm Zagorski separates civilian work from coerced military service", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.zagorski);
  expect(person.name_variants).toContain("Wilhelm Zagórski");
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "railway worker",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "German Army",
      relationship_type: "military_assignment",
      last_civilian_pre_service: false,
    }),
  ]);
  await page.goto(`./people/${profiles.zagorski[0]}/`);
  await expect(page.locator("main")).toContainText("railway worker");
  await expect(page.locator("main")).toContainText("conscripted soldier");
});

test("Edward Zarembo's commission, cadet status, and military assignment remain distinct", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.zarembo);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    commissioned_officer: true,
    personnel_category: "commissioned_army_officer",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army Quartermaster Corps",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Military Academy",
      relationship_type: "student",
    }),
  ]);
  await page.goto(`./people/${profiles.zarembo[0]}/`);
  await expect(page.locator("main")).toContainText("United States Army Quartermaster Corps");
  await expect(page.locator("main")).toContainText("United States Military Academy");
});

test("uncertain and volunteer evidence remains visibly qualified", async ({ request }) => {
  const zaikowsky = await publicPerson(request, profiles.zaikowsky);
  expect(zaikowsky).toMatchObject({ identity_status: "probable", research_status: "needs_temporal_review" });
  expect(zaikowsky.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "film technician",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]);

  const zaret = await publicPerson(request, profiles.zaret);
  expect(zaret.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Abraham Lincoln Brigade",
      relationship_type: "volunteer",
      temporal_basis: "documented_prewar",
    }),
  ]);
});

test("conflicting identity links do not create occupation or employer claims", async ({ request }) => {
  for (const profile of [profiles.frank, profiles.zatz]) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual([expect.objectContaining({ claim_type: "identity" })]);
  }
  const frank = await publicPerson(request, profiles.frank);
  expect(frank.possible_duplicate_group).toBeTruthy();
});

test("Batch 1029 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toContain("raw_record");
});
