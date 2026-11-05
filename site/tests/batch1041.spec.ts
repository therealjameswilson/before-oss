import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page296-richard-s-marnocha-to-robert-f-marszalek-review_batch-1041_2026-11-05.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  marquard: ["68c3948f-1dfc-5ab9-a6f0-a1a16dcf6a02", "Carl F Marquard"],
  marsales: ["8c645beb-4287-5b8d-b020-3418dcf097b1", "Hildegarde R Marsales"],
  marsching: ["ee0225cf-4f92-5e12-9d79-9d1b797a47cd", "John H Marsching"],
  marritts: ["84cbf17c-b33e-58d2-ab99-4b7aaf44e83c", "William L Marritts"],
  cornwall: ["580a69c2-ad8e-5916-904d-d2f4e24c51ce", "Cornwall Marshall"],
  maclean: ["170b79ee-5ab1-5c01-9434-d12cdb0d291b", "Maclean Marshall"],
  marshallCorn: ["cf0e34d2-366a-5d72-a306-baa7f81263fb", "James H Marshall-Corn"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1041 publishes all page 296 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...(await response.json()).filter((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.some((row) => row.pdf_page === 296),
    ));
  }
  expect(people).toHaveLength(46);
  expect(people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
    person.source_records.filter((row) => row.pdf_page === 296))).toHaveLength(46);
  for (const person of people) {
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
  }
});

test("Carl Marquard publishes Mascot Pictures only as qualified earlier employment", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.marquard);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "documented_prewar_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Mascot Pictures",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.marquard[0]}/`);
  await expect(page.locator("main")).toContainText("Mascot Pictures");
  await expect(page.locator("main")).toContainText("not shown to be the immediate predecessor");
});

test("Hildegarde Marsales separates probable immediate UW work from earlier Knox teaching", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.marsales);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "University of Wisconsin",
      relationship_type: "employment",
      temporal_basis: "probable_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "University of Wisconsin" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Knox School" }),
  ]);
  await page.goto(`./people/${profiles.marsales[0]}/`);
  await expect(page.locator("main")).toContainText("University of Wisconsin");
  await expect(page.locator("main")).toContainText("Knox School");
});

test("John Marsching remains a qualified probable NBC identity", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.marsching);
  expect(person).toMatchObject({ identity_status: "probable", research_status: "documented_prewar_employer_found" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "National Broadcasting Company",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.marsching[0]}/`);
  await expect(page.locator("main")).toContainText("probable identity candidate");
  await expect(page.locator("main")).toContainText("NBC");
});

test("Maclean Marshall preserves Civil Air Patrol volunteer status and no named employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.maclean);
  expect(person.name_variants).toEqual(expect.arrayContaining(["MacLean Marshall", "Mac Lean Marshall"]));
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({ canonical_organization: "Civil Air Patrol", relationship_type: "volunteer" }),
    expect.objectContaining({ canonical_organization: null, relationship_type: "unknown" }),
  ]));
  await page.goto(`./people/${profiles.maclean[0]}/`);
  await expect(page.locator("main")).toContainText("Civil Air Patrol");
  await expect(page.locator("main")).toContainText("rather than employment");
});

test("page 296 conflicts and possible duplicates remain separate", async ({ request, page }) => {
  const marritts = await publicPerson(request, profiles.marritts);
  expect(marritts).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(marritts.other_pre_oss_affiliations).toHaveLength(0);

  const cornwall = await publicPerson(request, profiles.cornwall);
  const marshallCorn = await publicPerson(request, profiles.marshallCorn);
  expect(cornwall).toMatchObject({ identity_status: "ambiguous", research_status: "needs_identity_review" });
  expect(marshallCorn).toMatchObject({ identity_status: "high_confidence", research_status: "needs_identity_review" });
  expect(cornwall.person_id).not.toBe(marshallCorn.person_id);
  expect(cornwall.possible_duplicate_group).toBe(marshallCorn.possible_duplicate_group);
  expect(cornwall.claims).toHaveLength(0);

  await page.goto(`./people/${profiles.marshallCorn[0]}/`);
  await expect(page.locator("main")).toContainText("same-box Cornwall Marshall row is preserved as a possible duplicate");
  await expect(page.locator("main")).toContainText("does not establish that he joined OSS");
});

test("Batch 1041 public assets omit protected identifiers", async ({ request }) => {
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
