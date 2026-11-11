import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const profiles = {
  porterMcKeever: ["2b0fbee8-d22b-5382-80d0-bbe878feee01", "Porter H McKeever"],
  donaldMcKinnon: ["d5ef7413-3d25-5bbb-b99f-80c6ba91d775", "Donald W McKinnon"],
  richardMcLallen: ["395c1942-d8b8-5871-99bc-98edd53c8b80", "Richard V McLallen"],
  marjorieMcKillop: ["6200df0a-f592-52d0-a420-3a1dd16d0c2e", "Marjorie L McKillop"],
  stewartMcKenneyA: ["e7a2e42a-3dbe-59b6-8280-ef258ea7f6c1", "Stewart L McKenney"],
  stewartMcKenneyB: ["bfb5330a-d471-5fd6-8edc-be0f506d26e0", "Stewart L McKenney"],
  jamesMcKenskey: ["dd60dccf-c3e9-531a-98fe-2e3f2a33dc09", "James A McKenskey"],
  aqMcKenzie: ["caf52600-59af-5780-b723-63a8a5bb316f", "A.Q. McKenzie"],
  francisMcKenzie: ["7a8902f5-3e2e-5d0a-a294-fe4fd28c68c9", "Francis W McKenzie"],
  kennethMcKown: ["512518ac-900f-5640-93cb-5da5cc084103", "Kenneth L McKown"],
  kennethMcKownT5: ["e3c44fcb-5b5e-5fef-b2cb-8c529acf5fa9", "Kenneth L McKown"],
  howardMcKee: ["89b2aba3-fb16-54e8-9bff-50d0583671f5", "Howard R McKee"],
  gordonMcKinley: ["02588cbd-f852-5812-8267-e238d3a6137a", "Gordon S McKinley"],
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

test("Batch 1056 publishes all 46 page-311 rows as 45 terminal profiles", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(
      ...(await response.json()).filter(
        (person: { source_records: { pdf_page: number }[] }) =>
          person.source_records.some((row) => row.pdf_page === 311),
      ),
    );
  }
  expect(people).toHaveLength(45);
  expect(
    people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.filter((row) => row.pdf_page === 311),
    ),
  ).toHaveLength(46);
  for (const person of people) {
    expect(["not_started", "in_progress", "candidate_found"]).not.toContain(
      person.research_status,
    );
  }
});

test("Donald MacKinnon publishes Bryn Mawr as an explicit immediate predecessor", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.donaldMcKinnon);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.name_variants).toContain("Donald Wallace MacKinnon");
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Bryn Mawr College",
      role_title: "professor of psychology",
      relationship_type: "employment",
      temporal_basis: "explicit_immediate",
      claim_confidence: "high",
    }),
  ]);
  expect(person.last_civilian_pre_service).toHaveLength(1);
  await page.goto(`./people/${profiles.donaldMcKinnon[0]}/`);
  await expect(page.locator("main")).toContainText("Bryn Mawr College");
  await expect(page.locator("main")).toContainText("explicit immediate");
});

test("Porter McKeever keeps civilian newspaper employers distinct from OWI", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.porterMcKeever);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "The News & Observer" }),
      expect.objectContaining({ canonical_organization: "The Greenville News" }),
    ]),
  );
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Office of War Information",
      relationship_type: "government_assignment",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.porterMcKeever[0]}/`);
  await expect(page.locator("main")).toContainText("The News & Observer");
  await expect(page.locator("main")).toContainText("Office of War Information");
});

test("Marjorie McKillop remains a qualified probable identity with student and Signal Corps roles", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.marjorieMcKillop);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "needs_identity_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({
        canonical_organization: "University of Washington",
        relationship_type: "student",
        claim_confidence: "medium",
      }),
      expect.objectContaining({
        canonical_organization: "United States Army Signal Corps",
        relationship_type: "military_assignment",
        claim_confidence: "medium",
      }),
    ]),
  );
  await page.goto(`./people/${profiles.marjorieMcKillop[0]}/`);
  await expect(page.locator("main")).toContainText("University of Washington");
  await expect(page.locator("main")).toContainText("Signal Corps");
  await expect(page.locator("main")).toContainText("probable");
});

test("Page-311 duplicate and conflict safeguards remain visible", async ({ request }) => {
  const stewartA = await publicPerson(request, profiles.stewartMcKenneyA);
  const stewartB = await publicPerson(request, profiles.stewartMcKenneyB);
  expect(stewartA.person_id).not.toBe(stewartB.person_id);
  expect(stewartA.possible_duplicate_group).toBe(stewartB.possible_duplicate_group);
  expect(stewartA.identity_status).toBe("ambiguous");
  expect(stewartB.identity_status).toBe("ambiguous");

  const kenneth = await publicPerson(request, profiles.kennethMcKown);
  const kennethT5 = await publicPerson(request, profiles.kennethMcKownT5);
  expect(kenneth.person_id).not.toBe(kennethT5.person_id);
  expect(kenneth.source_records).toHaveLength(2);
  expect(kennethT5.source_records).toHaveLength(1);
  expect(kennethT5.source_records[0].rank_as_indexed).toBe("T 5");

  const james = await publicPerson(request, profiles.jamesMcKenskey);
  expect(james).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  expect(james.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(james.last_civilian_pre_service).toHaveLength(0);
  expect(james.other_pre_oss_affiliations).toHaveLength(0);
});

test("Army-entry occupations stay qualified and unnamed", async ({ request, page }) => {
  const howard = await publicPerson(request, profiles.howardMcKee);
  expect(howard.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "general industry clerk",
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  const gordon = await publicPerson(request, profiles.gordonMcKinley);
  expect(gordon.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      occupation: "student",
      relationship_type: "student",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.howardMcKee[0]}/`);
  await expect(page.locator("main")).toContainText("general industry clerk");
  await page.goto(`./people/${profiles.gordonMcKinley[0]}/`);
  await expect(page.locator("main")).toContainText("student");
});

test("Uninterpreted Army codes do not become public occupations", async ({ request }) => {
  for (const profile of [profiles.aqMcKenzie, profiles.francisMcKenzie]) {
    const person = await publicPerson(request, profile);
    expect(person.identity_status).toBe("high_confidence");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims.every((claim: { claim_type: string }) => claim.claim_type === "identity")).toBeTruthy();
  }
});

test("Richard McLallen confirms identity without inventing a predecessor affiliation", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.richardMcLallen);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  await page.goto(`./people/${profiles.richardMcLallen[0]}/`);
  await expect(page.locator("main")).toContainText("Major Richard V. McLallen");
  await expect(page.locator("main")).toContainText("archival review");
});

test("Batch 1056 public data omits private identity crosswalk fields", async ({ request }) => {
  for (const profile of Object.values(profiles)) {
    const person = await publicPerson(request, profile);
    const serialized = JSON.stringify(person);
    expect(serialized).not.toContain("candidate_identifier");
    expect(serialized).not.toContain("bulk_record_ordinal");
    expect(serialized).not.toContain("private_identifier");
    expect(serialized).not.toContain("service_number_normalized");
  }
});
