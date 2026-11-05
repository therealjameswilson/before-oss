import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page298-maurice-l-martin-to-frank-m-masiokas-review_batch-1043_2026-11-05.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  maurice: ["3829bec1-1e0e-58e6-953c-5a2173d4e326", "Maurice L Martin"],
  norman: ["8a23fe1c-dfe2-5383-9efa-e94d05092ea1", "Norman J Martin"],
  obrey: ["84efe429-0bdb-513c-945a-01d657435d50", "Obrey E Martin"],
  wallace: ["e8e076c0-2807-5f2a-980e-4b9abcda22ec", "Wallace H Martin"],
  elfego: ["12902d41-ac89-5209-b391-d1234e503b31", "Elfego P Martinez"],
  james: ["ad7cd1a4-ad7c-527d-a3cf-07c3efccf67c", "James H Martinez"],
  rigiberto: ["18ce3b9b-2b46-56fe-a247-565c907a530a", "Rigiberto Martinez Sr."],
  pierre: ["278ae3c6-d915-5022-90c4-e953c26ee6ea", "Pierre M Martinot"],
  frank: ["5f75f48a-957b-569c-83ca-1bdc59cbd7cd", "Frank A Marvian"],
  carl: ["78a39be1-b959-5207-90a6-fde42035f61c", "Carl A Marzani"],
  roger: ["75f7854c-bc68-5ba5-a2e1-e97a30a995fd", "Roger W Masenior"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1043 publishes all page 298 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 298),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 298))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Maurice Martin and Pierre Martinot expose identity evidence without invented employers", async ({ request, page }) => {
  for (const profile of [profiles.maurice, profiles.pierre]) {
    const person = await publicPerson(request, profile);
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    await page.goto(`./people/${profile[0]}/`);
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
  }
  await page.goto(`./people/${profiles.maurice[0]}/`);
  await expect(page.locator("main")).toContainText("Beggar-circuit radio operator");
  await expect(page.locator("main")).toContainText("Adam");
  await page.goto(`./people/${profiles.pierre[0]}/`);
  await expect(page.locator("main")).toContainText("direct February 1944 OSS memorandum");
});

test("Army categories stay qualified and code 993 remains undefined", async ({ request, page }) => {
  const norman = await publicPerson(request, profiles.norman);
  expect(norman).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(norman.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ role_title: "student", relationship_type: "student", claim_confidence: "medium" }),
  ]);

  const wallace = await publicPerson(request, profiles.wallace);
  expect(wallace.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "skilled worker fabricating textile products, not elsewhere classified" }),
  ]);

  const elfego = await publicPerson(request, profiles.elfego);
  expect(elfego.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "semiskilled worker in furniture manufacturing, not elsewhere classified" }),
  ]);

  const obrey = await publicPerson(request, profiles.obrey);
  expect(obrey).toMatchObject({ identity_status: "confirmed", research_status: "requires_archival_review" });
  expect(obrey.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.obrey[0]}/`);
  await expect(page.locator("main")).toContainText("code 993 is undefined");
});

test("page 298 identity conflicts transfer no Army affiliation", async ({ request, page }) => {
  const james = await publicPerson(request, profiles.james);
  expect(james).toMatchObject({ identity_status: "conflicting", research_status: "needs_identity_review" });
  expect(james.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(james.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.james[0]}/`);
  await expect(page.locator("main")).toContainText("Evidence conflicts");
  await expect(page.locator("main")).toContainText("middle-initial conflict");

  const frank = await publicPerson(request, profiles.frank);
  expect(frank).toMatchObject({ identity_status: "conflicting", research_status: "needs_identity_review" });
  expect(frank.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.frank[0]}/`);
  await expect(page.locator("main")).toContainText("surname Marx materially conflicts with indexed surname Marvian");
});

test("index spellings remain primary while reviewed variants stay searchable", async ({ request, page }) => {
  const rigiberto = await publicPerson(request, profiles.rigiberto);
  expect(rigiberto.display_name).toBe("Rigiberto Martinez Sr.");
  expect(rigiberto.name_variants).toContain("Rigoberto Martinez Sr.");
  expect(rigiberto.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "bartender", claim_confidence: "medium" }),
  ]);

  const roger = await publicPerson(request, profiles.roger);
  expect(roger.display_name).toBe("Roger W Masenior");
  expect(roger.name_variants).toContain("Roger W Masenoir");
  await page.goto(`./people/${profiles.roger[0]}/`);
  await expect(page.locator("main")).toContainText("Roger W Masenoir");
});

test("Carl Marzani publishes only a qualified private-pursuits predecessor", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.carl);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "private pursuits (source wording)",
      relationship_type: "unknown",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto(`./people/${profiles.carl[0]}/`);
  await expect(page.locator("main")).toContainText("private pursuits (source wording)");
  await expect(page.locator("main")).toContainText("probable immediate");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 1043 public assets omit protected identifiers", async ({ request }) => {
  const batchIds = new Set(evidence.person_updates.map((item: { person_id: string }) => item.person_id));
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    people.push(...(await response.json()).filter((person: { person_id: string }) => batchIds.has(person.person_id)));
  }
  expect(people).toHaveLength(46);
  const serialized = JSON.stringify(people);
  expect(serialized).not.toContain("candidate_identifier");
  expect(serialized).not.toContain("serial_number");
  expect(serialized).not.toContain("service_number");
  expect(serialized).not.toContain("bulk_record_ordinal");
});
