import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const profiles = {
  thomasMcGuire: ["74bcb75d-d0b9-54c5-9404-33d108056164", "Thomas F McGuire"],
  williamMcGuire: ["cab5a497-9f2c-5f8e-ac99-557fc564d797", "William T McGuire"],
  carolynS: ["ae5d6a79-fad8-57c1-9076-6d7ba2e0d892", "Carolyn S McIntosh"],
  carolyn: ["e440e796-473a-51d5-97a9-fdbcdc42b986", "Carolyn McIntosh"],
  henryMcIntosh: ["c9a01212-57dd-51e7-a539-0fcd48426344", "Henry D McIntosh"],
  robertMcIntosh: ["7c53e363-a224-512d-aa0f-c60c7cdb3e80", "Robert McIntosh"],
  peterMcKeand: ["f634b404-7d17-5e3b-a77d-91211c565ba1", "Peter A.H. McKeand"],
  calvinMcKee: ["985ad762-bd86-5d93-a99b-c2db86b41f28", "Calvin C McKee"],
  charlesMcKee: ["66c4779b-2e27-555c-8157-0522ea46def5", "Charles T McKee"],
} as const;

async function publicPerson(
  request: APIRequestContext,
  [id, name]: readonly [string, string],
) {
  const response = await request.get(`./data/people/${name[0].toLowerCase()}.json`);
  expect(response.ok()).toBeTruthy();
  return (await response.json()).find(
    (item: { person_id: string }) => item.person_id === id,
  );
}

test("Batch 1055 publishes all 46 page-310 rows with no unattempted profile", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(
      ...(await response.json()).filter(
        (person: { source_records: { pdf_page: number }[] }) =>
          person.source_records.some((row) => row.pdf_page === 310),
      ),
    );
  }
  expect(people).toHaveLength(46);
  expect(
    people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.filter((row) => row.pdf_page === 310),
    ),
  ).toHaveLength(46);
  for (const person of people) {
    expect(["not_started", "in_progress", "candidate_found"]).not.toContain(
      person.research_status,
    );
  }
});

test("Henry McIntosh separates the Army Airborne pathway from Davidson student status", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.henryMcIntosh);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
  });
  expect(person.name_variants).toContain("Henry Deane McIntosh");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      organization_name_as_found: "Army Airborne",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Davidson College",
      relationship_type: "student",
    }),
  ]);
  await page.goto(`./people/${profiles.henryMcIntosh[0]}/`);
  await expect(page.locator("main")).toContainText("Army Airborne");
  await expect(page.locator("main")).toContainText("Davidson College");
  await expect(page.locator("main")).toContainText("student");
});

test("Calvin McKee publishes a qualified Army pathway, not a postwar oil employer", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.calvinMcKee);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
  });
  expect(person.name_variants).toContain("Calvin Charles McKee");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Army",
      relationship_type: "military_assignment",
      temporal_basis: "probable_immediate",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  expect(JSON.stringify(person)).not.toContain("Warren Petroleum");
  expect(JSON.stringify(person)).not.toContain("Gulf Oil");
  await page.goto(`./people/${profiles.calvinMcKee[0]}/`);
  await expect(page.locator("main")).toContainText("probable immediate");
});

test("Peter McKeand remains a qualified probable identity without a predecessor claim", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.peterMcKeand);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
  });
  expect(person.name_variants).toContain("Peter Andrew Hannay McKeand");
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        claim_type: "identity",
        claim_confidence: "medium",
        publication_status: "publish_qualified",
      }),
    ]),
  );
  await page.goto(`./people/${profiles.peterMcKeand[0]}/`);
  await expect(page.locator("main")).toContainText("Peter Andrew Hannay McKeand");
  await expect(page.locator("main")).toContainText("probable");
});

test("Robert McIntosh and Charles McKee keep qualified Army-entry categories unnamed", async ({ request, page }) => {
  const robert = await publicPerson(request, profiles.robertMcIntosh);
  expect(robert.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "financial institution clerk, not elsewhere classified",
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  const charles = await publicPerson(request, profiles.charlesMcKee);
  expect(charles.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "student",
      relationship_type: "student",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.robertMcIntosh[0]}/`);
  await expect(page.locator("main")).toContainText("financial institution clerk");
  await page.goto(`./people/${profiles.charlesMcKee[0]}/`);
  await expect(page.locator("main")).toContainText("student");
});

test("Page-310 duplicate, conflict, and post-OSS safeguards remain public", async ({ request, page }) => {
  const first = await publicPerson(request, profiles.carolynS);
  const second = await publicPerson(request, profiles.carolyn);
  expect(first.person_id).not.toBe(second.person_id);
  expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
  expect(first.identity_status).toBe("ambiguous");
  expect(second.identity_status).toBe("ambiguous");

  const thomas = await publicPerson(request, profiles.thomasMcGuire);
  expect(thomas).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  const william = await publicPerson(request, profiles.williamMcGuire);
  expect(william.identity_status).toBe("high_confidence");
  expect(william.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.williamMcGuire[0]}/`);
  await expect(page.locator("main")).toContainText("1946-07-25");
});

test("Batch 1055 public profile data omits private Army crosswalk fields", async ({ request }) => {
  for (const profile of Object.values(profiles)) {
    const person = await publicPerson(request, profile);
    const serialized = JSON.stringify(person);
    expect(serialized).not.toContain("candidate_identifier");
    expect(serialized).not.toContain("bulk_record_ordinal");
    expect(serialized).not.toContain("private_identifier");
  }
});
