import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page290-nelle-maertens-to-robert-maisonpierre-review_batch-1035_2026-11-04.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  maffin: ["0222f773-9e95-5dfe-afb3-5ec4cac228cf", "Clyde M Maffin"],
  magdic: ["ade234fb-950f-5379-9e64-0fb78d937ce1", "Matthew P Magdic"],
  magill: ["248b53bd-d4e9-5241-ae97-2cee6e0e61e4", "Orrin R Magill Jr."],
  maharg: ["972d2cdb-c882-5eb7-92bb-5317612f9a4c", "John D Maharg"],
  mains: ["57e0f633-3022-52bc-ba7b-3d13a9ab5829", "Shirley K Mains"],
  maisonpierre: ["62bdae40-7c17-59a6-bf36-824653811f9c", "Robert J Maisonpierre"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1035 publishes every page 290 row with a terminal outcome", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 290),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 290))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("accepted Army links remain qualified occupations or student status", async ({ request, page }) => {
  const magdic = await publicPerson(request, profiles.magdic);
  expect(magdic).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(magdic.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(magdic.last_civilian_pre_service).toHaveLength(0);
  expect(magdic.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      occupation: "semiskilled construction occupation, not elsewhere classified",
      claim_confidence: "medium",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);

  const magill = await publicPerson(request, profiles.magill);
  expect(magill.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ relationship_type: "student", role_title: "student" }),
  ]);
  expect(magill.name_variants).toContain("Orrin F Magill Jr.");

  const maisonpierre = await publicPerson(request, profiles.maisonpierre);
  expect(maisonpierre.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "college president, professor, or instructor" }),
  ]);

  await page.goto(`./people/${profiles.magill[0]}/`);
  await expect(page.locator("main")).toContainText("student");
  await expect(page.locator("main")).toContainText("Orrin F Magill Jr.");
});

test("rejected Maffin candidate transfers no Army occupation", async ({ request, page }) => {
  const maffin = await publicPerson(request, profiles.maffin);
  expect(maffin).toMatchObject({ identity_status: "unresolved", research_status: "requires_archival_review" });
  expect(maffin.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(maffin.last_civilian_pre_service).toHaveLength(0);
  expect(maffin.other_pre_oss_affiliations).toHaveLength(0);
  expect(maffin.claims).toHaveLength(0);
  await page.goto(`./people/${profiles.maffin[0]}/`);
  await expect(page.locator("main")).toContainText("damaged Army candidate");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("John Maharg has direct OSS identity evidence without an invented employer", async ({ request, page }) => {
  const maharg = await publicPerson(request, profiles.maharg);
  expect(maharg).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(maharg.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(maharg.last_civilian_pre_service).toHaveLength(0);
  expect(maharg.other_pre_oss_affiliations).toHaveLength(0);
  expect(maharg.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high" }),
  ]);
  await page.goto(`./people/${profiles.maharg[0]}/`);
  await expect(page.locator("main")).toContainText("OSS SU Detachment 101");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
});

test("indexed alias notes remain search variants", async ({ request }) => {
  const mains = await publicPerson(request, profiles.mains);
  expect(mains.name_variants).toContain("Shirley K Ray");
  expect(mains.research_status).toBe("requires_archival_review");
  expect(mains.other_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 1035 public assets omit protected identifiers", async ({ request }) => {
  const batchIds = new Set(evidence.person_updates.map((item: { person_id: string }) => item.person_id));
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    people.push(...(await response.json()).filter((person: { person_id: string }) => batchIds.has(person.person_id)));
  }
  expect(people).toHaveLength(45);
  const serialized = JSON.stringify(people);
  expect(serialized).not.toContain("candidate_identifier");
  expect(serialized).not.toContain("serial_number");
  expect(serialized).not.toContain("service_number");
  expect(serialized).not.toContain("bulk_record_ordinal");
});
