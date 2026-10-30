import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page476-george-tweed-to-john-tyson-review_batch-972_2026-10-30.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["58664c19-dff1-59b7-8b78-f8d3d0fb7134", "George B Tweed"],
  ["d9440d10-fe0c-509f-a09c-0691f2c95fcb", "John B Tweedy"],
  ["63e7b2e7-5900-57c9-bf2e-02804ac80b1a", "Lawrence L Tweedy"],
  ["cbb28220-65d3-5096-bdc3-ac76c719bc38", "Grant M Tweiten"],
  ["920fc446-1a31-561d-bea6-7de943b1183d", "Wayne Twigg"],
  ["4c0af134-6060-5ddd-9ce5-2e5b449dce2e", "Otto Twingley"],
  ["03fe9760-0057-5e5f-a8c2-3fbad2123d37", "Jack W Twist"],
  ["f8cd2018-0b24-52b7-a54b-ff805ed8f002", "Thomas S Twohy"],
  ["8754e68e-3a1a-54b9-859e-b25ebe364d1c", "John J Twork"],
  ["a917da94-edb9-51ff-ab9d-7d067a29016b", "Francis R Tworzydlo"],
  ["2d652241-1006-531e-b802-5ee7a40e937c", "John E Tyczkowski"],
  ["db95a650-f77e-5d14-8a1b-fd0a03bcb7f9", "Esther M Tyler"],
  ["29e02dfb-fe5a-5617-82a1-3a72e9cc81a7", "Lucia L Tyler"],
  ["21ae02a6-ad5d-5e51-a847-c5429c6701ae", "Mary G Tyler"],
  ["618f6c30-1e41-5ada-8c0b-0e34b248be5e", "Robert W Tyler"],
  ["9ab0881e-5f03-5657-9c8d-c894f22e7b96", "Stephen Tymonko"],
  ["aadc6e66-f287-5979-ad3f-0e8eb337e09a", "Mary L Tynan"],
  ["1ca517cd-d3fd-559e-b1bc-d23db10ac78a", "Marvin E Tyree"],
  ["ee586699-07ca-5a36-8d67-f6b5cf0c34b0", "James P Tyrell"],
  ["763b648a-9219-5440-ae6d-aafa51b4e55a", "Evan S Tyrrell"],
  ["4b8b68f4-0e75-5e11-932f-ab77cbe27d57", "Dorothy A Tyson"],
  ["31f19a9c-0486-5883-8a2e-c584bee93d49", "James L Tyson"],
  ["838a228f-60b7-598a-a781-d2e985aca146", "John Tyson"],
] as const;

const occupationProfiles = [
  ["63e7b2e7-5900-57c9-bf2e-02804ac80b1a", "Lawrence L Tweedy", "animal or livestock farm hand", "unknown"],
  ["8754e68e-3a1a-54b9-859e-b25ebe364d1c", "John J Twork", "student", "student"],
  ["618f6c30-1e41-5ada-8c0b-0e34b248be5e", "Robert W Tyler", "student", "student"],
  ["9ab0881e-5f03-5657-9c8d-c894f22e7b96", "Stephen Tymonko", "chauffeur or bus, taxi, truck or tractor driver", "unknown"],
] as const;

const unresolvedProfiles = [
  ["58664c19-dff1-59b7-8b78-f8d3d0fb7134", "George B Tweed"],
  ["cbb28220-65d3-5096-bdc3-ac76c719bc38", "Grant M Tweiten"],
  ["920fc446-1a31-561d-bea6-7de943b1183d", "Wayne Twigg"],
  ["03fe9760-0057-5e5f-a8c2-3fbad2123d37", "Jack W Twist"],
  ["f8cd2018-0b24-52b7-a54b-ff805ed8f002", "Thomas S Twohy"],
  ["a917da94-edb9-51ff-ab9d-7d067a29016b", "Francis R Tworzydlo"],
  ["db95a650-f77e-5d14-8a1b-fd0a03bcb7f9", "Esther M Tyler"],
  ["29e02dfb-fe5a-5617-82a1-3a72e9cc81a7", "Lucia L Tyler"],
  ["21ae02a6-ad5d-5e51-a847-c5429c6701ae", "Mary G Tyler"],
  ["aadc6e66-f287-5979-ad3f-0e8eb337e09a", "Mary L Tynan"],
  ["ee586699-07ca-5a36-8d67-f6b5cf0c34b0", "James P Tyrell"],
  ["763b648a-9219-5440-ae6d-aafa51b4e55a", "Evan S Tyrrell"],
  ["4b8b68f4-0e75-5e11-932f-ab77cbe27d57", "Dorothy A Tyson"],
  ["31f19a9c-0486-5883-8a2e-c584bee93d49", "James L Tyson"],
] as const;

async function publicPerson(request: APIRequestContext, id: string, name: string) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find((item: { person_id: string }) => item.person_id === id);
}

test("Batch 972 publishes all 23 audited people with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("four Army categories remain qualified occupations or student status without named employers", async ({ request }) => {
  for (const [id, name, occupation, relationshipType] of occupationProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: null,
        occupation,
        relationship_type: relationshipType,
        temporal_basis: "documented_prewar",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]));
  }
});

test("John Tweedy remains a probable identity with a qualified 86th Infantry assignment", async ({ request, page }) => {
  const person = await publicPerson(request, "d9440d10-fe0c-509f-a09c-0691f2c95fcb", "John B Tweedy");
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "requires_archival_review",
    commissioned_officer: null,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "86th Infantry Regiment, 10th Mountain Division",
      organization_name_as_found: "E Company, 86th Infantry",
      relationship_type: "military_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  await page.goto("./organizations/f8e9ea53-68e2-5383-8740-d36e9631a47c/");
  await expect(page.getByRole("heading", { name: "86th Infantry Regiment, 10th Mountain Division", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("John B Tweedy");
});

test("Otto Twingley publishes an immediate 99th Infantry military pathway, not a civilian employer", async ({ request, page }) => {
  const person = await publicPerson(request, "4c0af134-6060-5ddd-9ce5-2e5b449dce2e", "Otto Twingley");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "99th Infantry Battalion (Separate)",
      organization_name_as_found: "D Company, 99th Infantry",
      relationship_type: "military_assignment",
      temporal_basis: "strongly_date_bounded",
      claim_confidence: "high",
      immediate_pre_oss: true,
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  await page.goto("./organizations/a9ed25cf-8cdc-56e7-a6de-0ab28065fb8c/");
  await expect(page.getByRole("heading", { name: "99th Infantry Battalion (Separate)", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Otto Twingley");
});

test("John Tyczkowski keeps the protected-identifier name defect visible and gains no occupation", async ({ request, page }) => {
  const person = await publicPerson(request, "2d652241-1006-531e-b802-5ee7a40e937c", "John E Tyczkowski");
  expect(person).toMatchObject({ identity_status: "conflicting", research_status: "conflicting_sources" });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "conflicting", publication_status: "conflicting" }),
  ]);
  await page.goto("./people/2d652241-1006-531e-b802-5ee7a40e937c/");
  await expect(page.locator("main")).toContainText("Tyczkowski Ohn E");
});

test("Marvin Tyree uses post-OSS Army rows for identity only", async ({ request }) => {
  const person = await publicPerson(request, "1ca517cd-d3fd-559e-b1bc-d23db10ac78a", "Marvin E Tyree");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual([
    expect.objectContaining({ claim_type: "identity", claim_confidence: "high", publication_status: "published" }),
  ]);
});

test("John Tyson separates immediate and last-civilian insurance work from earlier railroad employment", async ({ request, page }) => {
  const person = await publicPerson(request, "838a228f-60b7-598a-a781-d2e985aca146", "John Tyson");
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Hutchinson, Rivinus & Co.",
      role_title: "partner",
      occupation: "insurance broker",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
      immediate_pre_oss: true,
      last_civilian_pre_service: true,
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({ canonical_organization: "Hutchinson, Rivinus & Co.", last_civilian_pre_service: true }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Pennsylvania Railroad",
      role_title: "fireman",
      occupation: "railroad fireman",
      temporal_basis: "documented_prewar",
    }),
  ]);
  await page.goto("./organizations/f2fc3eaa-9e56-51e2-a777-7c354abfade9/");
  await expect(page.getByRole("heading", { name: "Hutchinson, Rivinus & Co.", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("John Tyson");
  await page.goto("./organizations/b13c0dc1-58b7-5c40-8ab9-544db5b0da08/");
  await expect(page.getByRole("heading", { name: "Pennsylvania Railroad", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("John Tyson");
});

test("fourteen unresolved profiles remain dignified archival-review cases", async ({ request }) => {
  for (const [id, name] of unresolvedProfiles) {
    const person = await publicPerson(request, id, name);
    expect(person).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toHaveLength(0);
  }
});

test("Batch 972 evidence excludes secrets, full identifiers and raw bulk records", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("candidate_identifier");
  expect(evidence).not.toContain("bulk_record_ordinal");
});

test("Batch 972 publishes exact coverage counters and preserves oil counts", async ({ request, page }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  expect(await response.json()).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 664,
    research_attempted_people: 15_292,
    verified_affiliation_people: 1_097,
    verified_employer_people: 490,
    archival_review_assessed_people: 13_768,
    published_claims: 9_678,
    public_sources: 6_263,
  });
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
});
