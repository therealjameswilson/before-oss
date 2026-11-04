import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page521-ernest-zimmerman-to-charles-zuccardy-review_batch-1031_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  edmundZinder: ["89903963-283b-5ff8-b5ea-5bfa880015e0", "Edmund F Zinder"],
  paulZinner: ["3a8f7bc4-91e6-526a-9896-3b35a9da3a6a", "Paul E Zinner"],
  zlotnick: ["bd18c2fb-141c-52ea-a853-08b44637db52", "Jack Zlotnick"],
  zobatta: ["725f1b30-f216-5d48-9a0c-2ab274dcad2d", "Frank V Zobatta"],
  zonas: ["415fa958-1b38-5f4f-b787-841aedc35e5f", "James Zonas"],
  zonenberg: ["8379828c-c96d-511c-9bb8-8703154d24fc", "John W Zonenberg"],
  zoschke: ["3c07772b-8e42-5430-afad-17144efc49f3", "Jack H Zoschke"],
  zotter: ["b2a9b748-4995-5757-9a20-59df588060a8", "Louis Zotter Jr."],
  zubkoff: ["64783aa3-7beb-56d7-90b1-09046ac6a0b8", "Maurice J Zubkoff"],
  zuccardy: ["51414282-6d0d-5b24-98b4-ee9032d42b03", "Charles A Zuccardy"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1031 publishes every page 521 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 521);
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

test("Paul Zinner keeps Tufts student status separate from the Army pathway", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.paulZinner);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", relationship_type: "military_assignment" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Tufts College", relationship_type: "student" }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto(`./people/${profiles.paulZinner[0]}/`);
  await expect(page.locator("main")).toContainText("Tufts College");
  await expect(page.locator("main")).toContainText("United States Army");
});

test("Edmund Zinder displays the Linder alias and separate Allied pathways", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.edmundZinder);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "needs_temporal_review" });
  expect(person.name_variants).toContain("Edmund F Linder");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "British Army", temporal_basis: "explicit_immediate" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "French Foreign Legion" }),
  ]);
  await page.goto(`./people/${profiles.edmundZinder[0]}/`);
  await expect(page.locator("main")).toContainText("Edmund F Linder");
  await expect(page.locator("main")).toContainText("British Army");
});

test("Jack Zlotnick's Army pathway remains qualified", async ({ request }) => {
  const person = await publicPerson(request, profiles.zlotnick);
  expect(person).toMatchObject({ identity_status: "confirmed", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", temporal_basis: "probable_immediate" }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ occupation: "stenographer or typist" }),
  ]);
});

test("Maurice Zubkoff's Cornell record remains student status", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.zubkoff);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "Cornell University", relationship_type: "student" }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto(`./people/${profiles.zubkoff[0]}/`);
  await expect(page.locator("main")).toContainText("Cornell University");
});

test("shared and late Army links remain conflicts without occupations", async ({ request }) => {
  for (const profile of [profiles.zobatta, profiles.zonas, profiles.zonenberg]) {
    const person = await publicPerson(request, profile);
    expect(person.research_status).toBe("conflicting_sources");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
  }
});

test("Zoschke membership and Zotter military service remain qualified", async ({ request }) => {
  const zoschke = await publicPerson(request, profiles.zoschke);
  expect(zoschke).toMatchObject({ identity_status: "probable", research_status: "needs_identity_review" });
  expect(zoschke.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Institute of Radio Engineers",
      relationship_type: "professional_affiliation",
      temporal_basis: "temporal_relation_uncertain",
    }),
  ]);

  const zotter = await publicPerson(request, profiles.zotter);
  expect(zotter).toMatchObject({ identity_status: "high_confidence", research_status: "needs_temporal_review" });
  expect(zotter.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({ canonical_organization: "United States Army", temporal_basis: "temporal_relation_uncertain" }),
  ]);
});

test("Charles Zuccardy's Ritchie roster lead does not invent an affiliation", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.zuccardy);
  expect(person).toMatchObject({ identity_status: "probable", research_status: "needs_identity_review" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.zuccardy[0]}/`);
  await expect(page.locator("main")).toContainText("Ritchie Boys");
});

test("Batch 1031 public assets do not expose protected identifiers", async ({ request }) => {
  const forbidden = new Set(
    JSON.parse(evidence)
      .person_updates.flatMap((item: { name_variants?: string[] }) => item.name_variants ?? [])
      .filter((value: string) => /^\d{7,9}$/.test(value)),
  );
  expect(forbidden.size).toBe(0);
  const response = await request.get("./data/people/z.json");
  const text = await response.text();
  expect(text).not.toContain("candidate_identifier");
  expect(text).not.toContain("serial_number");
  expect(text).not.toContain("service_number");
});
