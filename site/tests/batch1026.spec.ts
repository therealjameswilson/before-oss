import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page516-william-wynn-to-george-yasukochi-review_batch-1026_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = {
  yanaga: ["9a228001-aa0d-5872-85db-78fc9d4600f4", "Ohitoshi Yanaga"],
  yarrow: ["cb3f3e20-4d50-5108-95a7-84f5a9d97472", "Bernard Yarrow"],
  yamamoto: ["694e706b-bf34-5b36-96cf-10bda80cd32c", "Sannosuke Yamamoto"],
  yamazaki: ["8642e536-31e3-5988-be3b-9c87159b846b", "Tomomasa Yamazaki"],
  yarmey: ["adb39191-76c6-59e0-a77b-7c520345b122", "John Yarmey"],
} as const;

async function publicPerson(request: APIRequestContext, [id, name]: readonly [string, string]) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 1026 publishes every page 516 row with a terminal outcome", async ({ request }) => {
  let sourceRows = 0;
  let people = 0;
  for (const letter of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${letter}.json`);
    expect(response.ok()).toBeTruthy();
    for (const person of await response.json()) {
      const rows = person.source_records.filter((row: { pdf_page: number }) => row.pdf_page === 516);
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

test("Yanaga preserves the index spelling and publishes the dated institutional sequence", async ({ request, page }) => {
  const yanaga = await publicPerson(request, profiles.yanaga);
  expect(yanaga).toMatchObject({ identity_status: "high_confidence", research_status: "verified_employer_found" });
  expect(yanaga.name_variants).toContain("Chitoshi Yanaga");
  expect(yanaga.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Foreign Broadcast Intelligence Service, Federal Communications Commission",
      relationship_type: "government_assignment",
      claim_confidence: "high",
    }),
  ]);
  expect(yanaga.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "University of California, Berkeley",
      relationship_type: "employment",
      claim_confidence: "high",
    }),
  ]);
  await page.goto(`./people/${profiles.yanaga[0]}/`);
  await expect(page.getByRole("heading", { name: profiles.yanaga[1], level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Chitoshi Yanaga");
  await expect(page.locator("main")).toContainText("Foreign Broadcast Intelligence Service");
});

test("Yarrow publishes an explicit district-attorney-to-OSS transition", async ({ request, page }) => {
  const yarrow = await publicPerson(request, profiles.yarrow);
  expect(yarrow).toMatchObject({ identity_status: "high_confidence", research_status: "completed" });
  expect(yarrow.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "New York County District Attorney's Office",
      relationship_type: "government_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  await page.goto(`./people/${profiles.yarrow[0]}/`);
  await expect(page.locator("main")).toContainText("Rackets Bureau");
  await expect(page.locator("main")).toContainText("November 1942");
});

test("Yamamoto's Philadelphia teaching remains temporally qualified", async ({ request, page }) => {
  const yamamoto = await publicPerson(request, profiles.yamamoto);
  expect(yamamoto).toMatchObject({ identity_status: "probable", research_status: "needs_temporal_review" });
  expect(yamamoto.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(yamamoto.last_civilian_pre_service).toHaveLength(0);
  expect(yamamoto.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Philadelphia Navy League School",
      temporal_basis: "temporal_relation_uncertain",
      publication_status: "publish_qualified",
    }),
  ]);
  await page.goto(`./people/${profiles.yamamoto[0]}/`);
  await expect(page.locator("main")).toContainText("Exact OSS entry remains unknown");
});

test("Yamazaki keeps the Navy-school job separate from earlier newspapers", async ({ request, page }) => {
  const yamazaki = await publicPerson(request, profiles.yamazaki);
  expect(yamazaki).toMatchObject({ identity_status: "probable", research_status: "documented_prewar_employer_found" });
  expect(yamazaki.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "U.S. Navy Japanese Language School, Boulder" }),
  ]);
  expect(yamazaki.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "New World-Sun" }),
      expect.objectContaining({ canonical_organization: "Sangyo Nippo" }),
    ]),
  );
  await page.goto(`./people/${profiles.yamazaki[0]}/`);
  await expect(page.locator("main")).toContainText("New World-Sun");
  await expect(page.locator("main")).toContainText("Sangyo Nippo");
});

test("Yarmey's conflicting protected identifier transfers no Army evidence", async ({ request }) => {
  const yarmey = await publicPerson(request, profiles.yarmey);
  expect(yarmey).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(yarmey.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(yarmey.last_civilian_pre_service).toHaveLength(0);
  expect(yarmey.other_pre_oss_affiliations).toHaveLength(0);
  expect(yarmey.claims).toHaveLength(0);
  expect(yarmey.possible_duplicate_group).toMatch(/^duplicate-[0-9a-f]{12}$/);
});

test("Batch 1026 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});
