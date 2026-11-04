import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page502-whitley-to-wiener-review_batch-1012_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["7838874e-963c-5779-9f0f-052b2e87a620", "Jack Whitley"],
  ["db7520cb-4275-59a9-937b-70390dcfd5e9", "Flody C Whitlow"],
  ["70be42d4-9df1-5189-ad85-b559c44ada31", "Floyd C Whitlow"],
  ["9b7626c8-45d0-5cb0-8b5e-a8ab980bfca1", "Alain S Whitman"],
  ["5b21625a-1574-5e6a-8908-9015adef921c", "Elda Whitman"],
  ["bf76f3c6-a6aa-541f-b867-48ec63a8fc3e", "James L Whitman"],
  ["5dcda7f2-ca42-5496-8172-c3977437fb27", "James R Whitman"],
  ["dc2d945c-570f-5723-b27b-4f4e51f922f9", "Joe Whitman"],
  ["73cae803-0d8c-5461-9cc5-9baee05eeea8", "Marvin L Whitmer"],
  ["946bb265-5ef0-59ea-8da7-85dd2c21d22f", "Hamie L Whitmore"],
  ["dbdfbbb8-f3dc-5d95-815e-1de8a3798d66", "Alice Whitney"],
  ["ea14553b-c7e5-5f1c-950f-54161d1441f8", "Burke E Whitney"],
  ["dde0cd8f-aee1-5fa2-aaa7-b96bad191921", "Stephen Whitney"],
  ["ffb02d3b-860c-5391-9fc8-14b2a7630182", "Stephen Whitney"],
  ["91277af5-9982-59b9-ba32-db8c5ba278fe", "Thomas P Whitney"],
  ["74e0a6d6-7eec-518b-b850-d8bea49dc339", "William D Whitney"],
  ["227bcffa-5ff0-5f4d-99a3-e8ab46383f9a", "Charles W Whittaker"],
  ["ec6577b3-4b52-50c6-b2e2-3e137cfd10b2", "Lee Whittaker"],
  ["ee4576f2-9604-547e-9481-6dcdfef67f8a", "Frank H Whittemore"],
  ["ed72223d-e154-5da0-95b4-690d57ae2889", "Henry L Whittemore Jr."],
  ["d5f92db6-28db-5b37-9cd1-6fce3b67a68b", "Robert F Whitten"],
  ["f4c1c840-dee1-5968-a016-9d2d7cae193b", "Charles A Whittier"],
  ["412a907d-1dbf-5de6-828d-24f893a656e2", "George D Whittinghill"],
  ["a3079498-0b64-5e35-bb48-ecf2de04516e", "Robert B Whittinghill"],
  ["9fa0f8ff-40fe-5719-a157-532bcb46afe5", "Derwent Whittlesey"],
  ["8d95ec22-1b44-5079-a891-4f18761db83b", "Ivan D Whitver"],
  ["2c2de58d-6615-542f-9038-2fa14bd830dd", "Charles F Wible Jr."],
  ["e0aef62a-65d5-5ad9-8889-28b2436c3d4e", "Robert Wichmann"],
  ["2a068be3-dbc9-54e7-ae6d-0c1f52745884", "Frank J Wicichowski"],
  ["5bf43b23-92a8-5b64-ae7b-8b672e5a3b0c", "Norman C Wicker"],
  ["b0839f15-2b3c-587b-a93c-4690809b6da0", "Norman E Wicker"],
  ["ee7d8330-1d97-57f9-b53f-e15bdf91945e", "Eleanor E Wickert"],
  ["df2f5b71-5523-57ff-ab69-480d2e9d61c6", "George A Wickes"],
  ["53f28d57-a6a5-56f2-8c4d-11db2bb46d86", "John A Wickham"],
  ["019f50f9-50a3-51aa-9069-50cd1685e0e2", "Richard V Wickham"],
  ["cd75f4b2-34ac-5131-ae2c-2404ac4aa3ac", "Jeannette Wicks"],
  ["6360e3d0-4a67-500b-a484-f3a9a0ca6364", "Walter F Wicks"],
  ["f288f7ea-401e-5d56-8a21-a3c1f2567c4f", "Donald R Widman"],
  ["03e5f5f3-37a4-54ec-aa9e-6ba1c600b8e0", "Frederick J Widmayer"],
  ["91a4ff2a-58a5-541a-a684-cb8030536b0f", "Dean R Widrig"],
  ["0a3f6f92-1312-590d-b7de-5b28b9ea8228", "Howard Wiedemann"],
  ["6712cfeb-a2cd-5299-96da-2e4624a7e396", "Hermann C Wiegert"],
  ["419a4fe6-8242-5019-a86d-1adf5ad8ce69", "Clarion B Wiener"],
  ["e738ef02-1123-5431-9403-b2f396a69e2c", "Irene P Wiener"],
  ["7c128775-a49f-52b3-b2ea-9983ed87bdeb", "Louis L Wiener"],
  ["54d06d0f-f16d-5578-aec9-3ead65fe5c79", "Max Wiener"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const first = name[0].toLowerCase();
  const shard = /^[a-z]$/.test(first) ? first : "other";
  const response = await request.get(`./data/people/${shard}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find(
    (item: { person_id: string }) => item.person_id === id,
  );
}

test("Batch 1012 publishes all 46 reviewed people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    await expect(main).not.toContainText(/\b[ORW]-?\d{5,9}\b/);
  }
});

test("all 46 page 502 rows remain separately recoverable", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    sourceRows += person.source_records.filter(
      (row: { pdf_page: number }) => row.pdf_page === 502,
    ).length;
  }
  expect(sourceRows).toBe(46);
});

test("eleven Army categories remain qualified and never invent employers", async ({ request }) => {
  const expected = new Map([
    [profiles[5][0], "unskilled textile-manufacturing worker, not elsewhere classified"],
    [profiles[7][0], "salesman or sales agent, except sales to consumers"],
    [profiles[13][0], "secondary-school teacher or principal"],
    [profiles[17][0], "airplane mechanic or repairman"],
    [profiles[18][0], "lawyer or judge"],
    [profiles[19][0], "secondary-school teacher or principal"],
    [profiles[26][0], "student"],
    [profiles[28][0], "unskilled nonprocess manufacturing worker, not elsewhere classified"],
    [profiles[32][0], "student"],
    [profiles[37][0], "author, editor, or reporter"],
    [profiles[39][0], "telegraph, telephone, or power lineman or serviceman"],
  ]);
  for (const [id, occupation] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.identity_status).toMatch(/^(confirmed|high_confidence)$/);
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]);
  }
});

test("the Whitaker and Whittaker protected-identifier conflict remains visible and unmerged", async ({ request }) => {
  const whittaker = await publicPerson(request, profiles[16][0], profiles[16][1]);
  const whitaker = await publicPerson(
    request,
    "80a06373-a9d5-5f9c-962b-6ba65be60edc",
    "Charles W Whitaker",
  );
  expect(whittaker).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(whitaker).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(whittaker.person_id).not.toBe(whitaker.person_id);
  expect(whittaker.other_pre_oss_affiliations).toHaveLength(0);
  expect(JSON.stringify(whittaker.claims)).toContain("remain separate");
});

test("Thomas Porter Whitney keeps the unidentified Bennett College explicit", async ({ request }) => {
  const person = await publicPerson(request, profiles[14][0], profiles[14][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Bennett College (institution unspecified)",
      role_title: "instructor of social sciences",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(1);
});

test("Robert Whittinghill separates immediate military assignment from two civilian jobs", async ({ request }) => {
  const person = await publicPerson(request, profiles[23][0], profiles[23][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Prisoner of War Section, G-2, Allied Force Headquarters",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "confirmed",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "Time, Inc.",
        organization_name_as_found: "Time magazine",
        relationship_type: "employment",
      }),
      expect.objectContaining({
        canonical_organization: null,
        organization_name_as_found: "a private school near Cornell",
        role_title: "teacher of French and Italian",
      }),
    ]),
  );
});

test("George Whittinghill and Derwent Whittlesey remain documented prewar rather than immediate", async ({ request }) => {
  const george = await publicPerson(request, profiles[22][0], profiles[22][1]);
  expect(george).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
  });
  expect(george.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(george.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Department of State",
      relationship_type: "government_assignment",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);

  const derwent = await publicPerson(request, profiles[24][0], profiles[24][1]);
  expect(derwent).toMatchObject({
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
  });
  expect(derwent.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(derwent.last_civilian_pre_service).toHaveLength(0);
  expect(derwent.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      role_title: "professor of geography",
      start_date: "1928",
      claim_confidence: "high",
    }),
  ]);
});

test("Batch 1012 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1012 public claims retain inspectable short citations", async ({ request }) => {
  const claimIndexes = [5, 7, 13, 14, 16, 17, 18, 19, 22, 23, 24, 26, 28, 32, 37, 39] as const;
  for (const index of claimIndexes) {
    const person = await publicPerson(request, profiles[index][0], profiles[index][1]);
    expect(person.claims.length).toBeGreaterThan(0);
    for (const item of person.claims) {
      expect(item.sources.length).toBeGreaterThan(0);
      for (const link of item.sources) {
        expect(link.source.stable_url || link.source.archival_identifier).toBeTruthy();
        const excerpt = link.excerpt_override ?? item.evidence_excerpt ?? "";
        expect(excerpt.trim() ? excerpt.trim().split(/\s+/).length : 0).toBeLessThanOrEqual(25);
      }
    }
  }
});
