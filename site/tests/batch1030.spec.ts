import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page520-francis-zdaniecki-to-christian-zimmerman-review_batch-1030_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  zeek: ["25d323d6-d833-539d-bc5d-1c541bcd875e", "Josepoh L Zeek"],
  zelenka: ["8fdf183a-5e5a-5697-8dcb-e7a515709758", "Louis P Zelenka"],
  zerdilla: ["92dcec2c-3404-5e21-9e15-8a01f383b064", "Peter Zerdilla"],
  ziegner: ["191ff779-1a55-5b8a-9f06-be0970ecd4ef", "Paul F Ziegner"],
  ziegler: ["f11d9c14-c493-537d-8034-87033505961e", "Evarts Ziegler"],
  zigman: ["1d1653b9-c361-5adb-a99b-807d28395738", "Joseph Zigman"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1030 publishes every page 520 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 520);
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

test("the Zeek index typo remains visible while the reviewed variant is searchable", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.zeek);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(person.name_variants).toContain("Joseph L Zeek");
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "food-canning or preserving worker",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  await page.goto(`./people/${profiles.zeek[0]}/`);
  await expect(page.getByRole("heading", { name: profiles.zeek[1], level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Joseph L Zeek");
});

test("Louis Zelenka is classified as commissioned without inventing a predecessor", async ({ request }) => {
  const person = await publicPerson(request, profiles.zelenka);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    commissioned_officer: true,
    personnel_category: "commissioned_army_officer",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
});

test("Evarts Ziegler's National Guard record remains a qualified earlier military affiliation", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.ziegler);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "needs_temporal_review" });
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "New York National Guard",
      relationship_type: "military_assignment",
      temporal_basis: "documented_prewar",
      last_civilian_pre_service: false,
    }),
  ]);
  await page.goto(`./people/${profiles.ziegler[0]}/`);
  await expect(page.locator("main")).toContainText("New York National Guard");
});

test("Joseph Zigman separates last civilian occupation from the Navy pathway", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.zigman);
  expect(person).toMatchObject({ identity_status: "high_confidence", research_status: "occupation_only_found" });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Navy",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: null, occupation: "film editor" }),
  ]);
  await page.goto(`./people/${profiles.zigman[0]}/`);
  await expect(page.locator("main")).toContainText("film editor");
  await expect(page.locator("main")).toContainText("United States Navy");
});

test("conflicting and late Army links do not create pre-OSS affiliations", async ({ request }) => {
  const zerdilla = await publicPerson(request, profiles.zerdilla);
  expect(zerdilla).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(zerdilla.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(zerdilla.last_civilian_pre_service).toHaveLength(0);
  expect(zerdilla.other_pre_oss_affiliations).toHaveLength(0);

  const ziegner = await publicPerson(request, profiles.ziegner);
  expect(ziegner.name_variants).toContain("Paul F Ziegner Jr.");
  expect(ziegner.research_status).toBe("requires_archival_review");
  expect(ziegner.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(ziegner.last_civilian_pre_service).toHaveLength(0);
  expect(ziegner.other_pre_oss_affiliations).toHaveLength(0);
});

test("Batch 1030 public assets do not expose protected identifiers", async ({ request }) => {
  const forbidden = new Set(
    JSON.parse(evidence)
      .person_updates.flatMap((item: { name_variants?: string[] }) => item.name_variants ?? [])
      .filter((value: string) => /^\d{7,9}$/.test(value)),
  );
  expect(forbidden.size).toBe(0);
  for (const letter of ["z"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    const text = await response.text();
    expect(text).not.toContain("candidate_identifier");
    expect(text).not.toContain("serial_number");
    expect(text).not.toContain("service_number");
  }
});
