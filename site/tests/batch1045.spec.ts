import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page300-steve-p-mathiakes-to-leonard-j-matuszek-review_batch-1045_2026-11-05.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  carlo: ["1cf617cf-8efe-5bf8-8d3c-800ca365c944", "Carlo-Felice Mathieu"],
  harold: ["fca002e6-da76-5af0-a742-2d2beaf8550e", "Harold L Mathis"],
  johnMathis: ["106f76e8-7a5f-553d-824d-8186ceffb73d", "John H Mathis"],
  lesley: ["b3d6b8a5-ab1b-5a43-bf01-6047ced68a25", "Lesley Mathwig"],
  joseph: ["e0b85199-a220-588b-a074-8ba2d2e300ba", "Joseph Matovich"],
  charles: ["4c1bc377-1904-5fea-a33b-0a74402eb3ac", "Charles Y Matsunaka"],
  andrew: ["44df2777-a96c-595c-9c9d-16bfb5ba8245", "Andrew J Matta"],
  eugeneCaptain: ["25689d5d-02b6-5777-afd0-5053e025dec6", "Eugene K Matthews"],
  eugeneLieutenant: ["c91e6700-1847-531b-9b16-ea7876434623", "Eugene K Matthews"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1045 publishes all page 300 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 300),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 300))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Matsunaka keeps his Army pathway separate from radio occupation", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.charles);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: null, occupation: "radio operator", claim_confidence: "medium" }),
  ]);
  expect(person.immediate_pre_oss_affiliations[0].canonical_organization).toBe("United States Army");
  expect(person.immediate_pre_oss_affiliations[0].organization_name_as_found).toBe("serving in India");
  await page.goto(`./people/${profiles.charles[0]}/`);
  await expect(page.locator("main")).toContainText("United States Army");
  await expect(page.locator("main")).toContainText("radio operator");
  await expect(page.locator("main")).toContainText("probable immediate");
});

test("Carlo-Felice Mathieu presents occupation and student status without inventing an employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.carlo);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(person.name_variants).toContain("Arturo Carlo Felice Mathieu");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Princeton University",
      role_title: "graduate student",
      relationship_type: "student",
    }),
    expect.objectContaining({
      canonical_organization: null,
      occupation: "language teacher",
      relationship_type: "employment",
      claim_confidence: "medium",
    }),
  ]));
  await page.goto(`./people/${profiles.carlo[0]}/`);
  await expect(page.locator("main")).toContainText("Princeton University");
  await expect(page.locator("main")).toContainText("teacher of French and Spanish");
  await expect(page.locator("main")).toContainText("student");
});

test("Matovich shows student status and wartime identity without a named employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.joseph);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: null, role_title: "student", relationship_type: "student" }),
  ]);
  await page.goto(`./people/${profiles.joseph[0]}/`);
  await expect(page.locator("main")).toContainText("student");
  await expect(page.locator("main")).toContainText("OSS communications technician");
});

test("Army variants remain visible and broad categories remain nonemployer evidence", async ({ request, page }) => {
  const john = await publicPerson(request, profiles.johnMathis);
  expect(john.name_variants).toContain("John H Mathis Sr.");
  expect(john.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "semiskilled textile-manufacturing worker, not elsewhere classified",
      claim_confidence: "medium",
    }),
  ]);

  const lesley = await publicPerson(request, profiles.lesley);
  expect(lesley.name_variants).toContain("Lesley M Mathwig");
  const andrew = await publicPerson(request, profiles.andrew);
  expect(andrew.name_variants).toContain("Andrew J Matta Jr.");

  await page.goto(`./people/${profiles.harold[0]}/`);
  await expect(page.locator("main")).toContainText("general farm hand");
  await expect(page.locator("main")).toContainText("no employer, institution, or workplace is identified");
});

test("the two Eugene K Matthews rows remain distinct and visibly unresolved", async ({ request, page }) => {
  const captain = await publicPerson(request, profiles.eugeneCaptain);
  const lieutenant = await publicPerson(request, profiles.eugeneLieutenant);
  expect(captain.person_id).not.toBe(lieutenant.person_id);
  expect(captain).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  expect(lieutenant).toMatchObject({ identity_status: "conflicting", research_status: "needs_identity_review" });
  expect(captain.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(lieutenant.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.eugeneCaptain[0]}/`);
  await expect(page.locator("main")).toContainText("Evidence conflicts");
  await page.goto(`./people/${profiles.eugeneLieutenant[0]}/`);
  await expect(page.locator("main")).toContainText("protected identifier conflicts");
});

test("Batch 1045 public assets omit protected identifiers", async ({ request }) => {
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
