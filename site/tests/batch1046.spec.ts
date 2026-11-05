import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page301-josef-matuszowicz-to-lewis-l-may-review_batch-1046_2026-11-05.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  joseph: ["afb2ef1d-8661-50fc-8e0a-27938f5d56b7", "Joseph P Mauro"],
  erwinMauss: ["4b97ed0c-9c0b-5f68-a7a1-c49471df5b6b", "Erwin Mauss"],
  josephMautner: ["dc92c3c1-dd07-53b9-befd-b2e4f8ba018c", "Joseph P Mautner"],
  floyd: ["64ba13a9-502e-5e08-8a9f-f753ddb6f93d", "Floyd E Maves"],
  charles: ["bbdeca8e-84d8-571c-aa35-91064cd2dc10", "Charles Maxwell"],
  georgesOfficer: ["b39c237a-1c75-5dd0-a2be-01b88172e126", "Georges May"],
  georgesEnlisted: ["96d23cce-ea21-58ca-a626-4e13d8243f04", "Georges May"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1046 publishes all page 301 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 301),
    ));
  }
  expect(people).toHaveLength(45);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 301))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Floyd Maves shows qualified occupation and direct Detachment 101 identity evidence", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.floyd);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "semiskilled mechanic or repairman, not elsewhere classified",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.floyd[0]}/`);
  await expect(page.locator("main")).toContainText("Detachment 101");
  await expect(page.locator("main")).toContainText("semiskilled mechanic or repairman");
  await expect(page.locator("main")).toContainText("Maves, Floyd E | Cpl | Sgt");
});

test("Joseph Mauro keeps two immutable source rows on one cautious entity", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.joseph);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 301)).toHaveLength(2);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: null, occupation: "insurance salesman" }),
  ]);
  await page.goto(`./people/${profiles.joseph[0]}/`);
  await expect(page.locator("main")).toContainText("Two printed Joseph P. Mauro index rows");
  await expect(page.locator("main")).toContainText("insurance salesman");
});

test("identity conflicts and low-confidence candidates do not transfer occupations", async ({ request, page }) => {
  const erwin = await publicPerson(request, profiles.erwinMauss);
  expect(erwin).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(erwin.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.erwinMauss[0]}/`);
  await expect(page.locator("main")).toContainText("Evidence conflicts");
  await expect(page.locator("main")).not.toContainText("sheet-metal worker");

  const charles = await publicPerson(request, profiles.charles);
  expect(charles).toMatchObject({ identity_status: "probable", research_status: "needs_identity_review" });
  expect(charles.other_pre_oss_affiliations).toHaveLength(0);
});

test("the two Georges May entities remain separate and only the enlisted row has an occupation", async ({ request, page }) => {
  const officer = await publicPerson(request, profiles.georgesOfficer);
  const enlisted = await publicPerson(request, profiles.georgesEnlisted);
  expect(officer.person_id).not.toBe(enlisted.person_id);
  expect(officer).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  expect(officer.other_pre_oss_affiliations).toHaveLength(0);
  expect(enlisted).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(enlisted.name_variants).toContain("Georges C May");
  expect(enlisted.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "secondary-school teacher or principal" }),
  ]);
  await page.goto(`./people/${profiles.georgesOfficer[0]}/`);
  await expect(page.locator("main")).toContainText("Evidence conflicts");
});

test("undefined Army code 993 is not exposed as an occupation", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.josephMautner);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "requires_archival_review" });
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.josephMautner[0]}/`);
  await expect(page.locator("main")).toContainText("Code 993 is not interpreted");
});

test("Batch 1046 public assets omit protected identifiers", async ({ request }) => {
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
