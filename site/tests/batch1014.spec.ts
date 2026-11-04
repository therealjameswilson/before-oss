import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page504-wiley-to-williams-review_batch-1014_2026-11-04.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["56350580-c247-5ea8-9bfe-4fd9adb6bf6e", "Norman B Wiley"],
  ["ebbacbb0-07e3-520d-a3cd-d506b7d2dfad", "William L Wiley"],
  ["945ccf71-0bfe-566a-b6b3-26ee39dd080f", "William R Wiley"],
  ["4b33b6ba-e24e-5205-852e-9f03a95a535e", "Ernest R Wilham"],
  ["d921687e-852c-5473-9ee3-fb23f9ab97d6", "Phyllis Wilhide"],
  ["8d96d1ab-2ec8-5d34-a50b-e04bb0f1223a", "Myra M Wilkens"],
  ["52659721-f37f-5680-a292-59fb5b07dd06", "William C Wilkenson"],
  ["bf21b913-09fb-53cb-81c8-b53b87c42e48", "Charles A Wilkerson"],
  ["eae8f1be-1305-52f8-b97f-bfd02f07e883", "Dewitt C Wilkerson Jr."],
  ["a848893e-2c5c-546f-81b3-3cb929d92618", "Eugene F Wilkerson"],
  ["6ff26672-6f89-5167-97c3-143c20c6b027", "James L Wilkerson Sr."],
  ["9dbd3d04-7950-5a80-809c-73dbe34d2c08", "Odean H Wilkerson"],
  ["9ff788ba-cdb1-50a8-a298-4a5a1fa45295", "John Wilkeson"],
  ["7369d7ad-4535-59aa-9ef2-f384e982e74d", "William D Wilkey"],
  ["95329ef0-97e0-556a-b353-210ae5e1fd57", "William H Wilkie"],
  ["7c34f0d1-0e6e-5946-9ab8-b8c68bf8f212", "Julia C Wilkin"],
  ["9a8d22a9-ac17-5640-bef7-07545fa4fc06", "Byron S Wilkins"],
  ["534a9217-40f7-51f9-a815-b974436a96f5", "Myra M Wilkins"],
  ["308e936a-679b-5e95-b424-5066708d22fe", "Samuel D Wilkins"],
  ["2df9ec4a-8b18-5aee-a1e2-9f8ac8356e86", "Woodrow Wilkins"],
  ["9e629d49-64fc-5cb0-9963-b12c0d104c6b", "Caroline T Wilkinson"],
  ["87d39172-5cf8-5113-b302-f8d7e95bf2a6", "Francis P Wilkinson"],
  ["eb5edd25-c7f8-5696-86f1-ed0ce5b1d0bf", "Irene M Wilkinson"],
  ["e119e65c-5b7f-5338-873f-3d3685f0ac31", "Robert J Wilkinson Jr."],
  ["6f10019c-7c6e-5405-a661-2e8461b4f98d", "Thomas R Wilkinson"],
  ["8c827eeb-7c55-5ee4-9445-d95d6ce3de27", "William C Wilkinson"],
  ["6c5710b8-1c60-5c7e-b7fe-1246ef40a2b7", "Hubert L Will"],
  ["e8c90660-2044-5cfa-8fbe-d1134164ca52", "Hugo L Will"],
  ["b8cee774-9b17-5524-a246-c5e291d44083", "Martha G Will"],
  ["30820944-d932-5c24-887a-959fda4ced57", "Phyllis Will"],
  ["a6227747-39bf-56ec-abbf-6e9144023e7f", "Richard V Will"],
  ["1bb58462-c825-5904-9b0a-6668321a1f7f", "Edwin A Willard"],
  ["3851031a-a6e7-5236-8d6e-ae7c12834583", "Stanley E Willard"],
  ["81bfa3f3-543e-58d1-9245-6c73839b747e", "Stanley E Willard"],
  ["784aea2c-073c-503b-840a-0ad092b1d650", "Max Willenz"],
  ["bf56eb3a-e476-54f1-a2f1-503b5d4b22a5", "Gordon E Willert"],
  ["e17ef200-1723-5ebf-9bc2-5040b0cd1654", "Harriet A Willetis"],
  ["ed21a92d-e048-53dd-af6a-a16869a52a66", "Robert A Willett"],
  ["1ad71d35-0d19-5031-bed7-0c7789ee5e54", "Harriet A Willette"],
  ["f3e1a720-b09f-5f76-929d-7c985ffb606c", "Hazel M Willey"],
  ["ee2bdfa9-a23f-5101-8b4a-66c38ee76585", "Jack A William"],
  ["6967ab9d-94a7-5143-8ec5-0af018388c9d", "Joseph M William"],
  ["281ae78b-a1bc-519f-b41c-f97aae9756bf", "Alfred E Williams"],
  ["5df3c789-3794-5b3a-b723-41a70e4f00f6", "Alvin H Williams"],
  ["0dc6648b-f10b-5ae3-a68b-ef3bb15e1c91", "Anna G Williams"],
  ["53b700e7-115f-5635-93bf-c06da4bba041", "Arthur J Williams"],
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

test("Batch 1014 publishes all 46 reviewed people and preserves page 504 rows", async ({ request }) => {
  let sourceRows = 0;
  for (const [id, name] of profiles) {
    const person = await publicPerson(request, id, name);
    expect(person, name).toBeTruthy();
    expect(person.research_status).not.toBe("not_started");
    expect(person.research_status).not.toBe("in_progress");
    sourceRows += person.source_records.filter(
      (row: { pdf_page: number }) => row.pdf_page === 504,
    ).length;
    expect(JSON.stringify(person)).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
  }
  expect(sourceRows).toBe(46);
});

test("eight Army categories remain qualified and never invent employers", async ({ request }) => {
  const expected = new Map([
    [profiles[13][0], "stenographer or typist"],
    [profiles[14][0], "accountant or auditor"],
    [profiles[19][0], "farm hand on a general farm"],
    [profiles[24][0], "post office clerk"],
    [profiles[30][0], "telegraph, telephone, or power lineman or serviceman"],
    [profiles[35][0], "general office clerk"],
    [profiles[37][0], "mechanic or repairman, not elsewhere classified"],
    [profiles[43][0], "meatcutter outside slaughtering and packing houses"],
  ]);
  for (const [id, occupation] of expected) {
    const name = profiles.find(([personId]) => personId === id)![1];
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
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

test("Hubert Will separates immediate federal assignment from earlier government work", async ({ request, page }) => {
  const person = await publicPerson(request, profiles[26][0], profiles[26][1]);
  expect(person).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "completed",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Office of Alien Property Custodian",
      role_title: "tax counsel",
      relationship_type: "government_assignment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(1);
  expect(person.last_civilian_pre_service[0].affiliation_id).toBe(
    person.immediate_pre_oss_affiliations[0].affiliation_id,
  );
  expect(person.other_pre_oss_affiliations.map(
    (item: { canonical_organization: string }) => item.canonical_organization,
  )).toEqual(expect.arrayContaining([
    "Office of Price Administration",
    "U.S. Department of Justice",
  ]));
  await page.goto(`./people/${profiles[26][0]}/`);
  await expect(page.getByRole("heading", { name: "Hubert L Will", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Office of Alien Property Custodian");
});

test("Max Willenz publishes pre-OSS performance evidence without inventing an employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles[34][0], profiles[34][1]);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "civilian_professional_or_administrative_grade",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      organization_name_as_found: "Vienna theater productions",
      occupation: "singer, tenor, and actor",
      relationship_type: "professional_affiliation",
    }),
    expect.objectContaining({
      organization_name_as_found: "Overture to Glory",
      occupation: "actor",
      relationship_type: "professional_affiliation",
    }),
  ]));
  await page.goto(`./people/${profiles[34][0]}/`);
  await expect(page.getByRole("heading", { name: "Max Willenz", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Overture to Glory");
});

test("Jack William conflict transfers no Army occupation or chronology", async ({ request }) => {
  const person = await publicPerson(request, profiles[40][0], profiles[40][1]);
  expect(person).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  ]);
});

test("three page 504 duplicate leads remain separate and visibly grouped", async ({ request }) => {
  for (const [left, right] of [[5, 17], [32, 33], [36, 38]] as const) {
    const first = await publicPerson(request, profiles[left][0], profiles[left][1]);
    const second = await publicPerson(request, profiles[right][0], profiles[right][1]);
    expect(first.person_id).not.toBe(second.person_id);
    expect(first.possible_duplicate_group).toBeTruthy();
    expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
    expect(first.manual_review_required).toBe(true);
    expect(second.manual_review_required).toBe(true);
  }
});

test("Batch 1014 evidence excludes secrets, identifiers, and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
  expect(evidence).not.toMatch(/\b[ORW]-?\d{5,9}\b/);
});

test("Batch 1014 claims retain inspectable short citations", async ({ request }) => {
  const claimIndexes = [13, 14, 19, 24, 26, 30, 34, 35, 37, 40, 43] as const;
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

test("Batch 1014 coverage totals are public", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23978,
    person_entities: 23935,
    research_attempted_people: 16571,
    verified_affiliation_people: 1173,
    verified_employer_people: 536,
    archival_review_assessed_people: 15048,
  });
});
