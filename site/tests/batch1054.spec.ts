import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page309-barry-mcgill-to-ernest-f-mcguire-review_batch-1054_2026-11-11.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  barryMcGill: ["a574c48c-ad3b-57a1-ae43-c985d9c94364", "Barry McGill"],
  davidMcGinnis505: ["19527627-c8ef-5beb-9c82-4eb2b082fed0", "David K McGinnis"],
  davidMcGinnis506: ["4d925235-45a5-5159-a7a5-a62ecfa8f571", "David K McGinnis"],
  leonMcGinnis: ["f466bb16-1781-5ad5-b65f-d35f17033d3c", "Leon A McGinnis"],
  owenMcGivern: ["8c545524-a2bf-51a0-a47b-6fa703c1d0a0", "Owen McGivern"],
  williamMMcGovern: ["80e851c4-c1ae-5bd5-b591-9ec4c92a351a", "William M McGovern"],
  johnMcGowanLt: ["8cb882e2-137b-5126-96c5-c3415e716d7f", "John E McGowan"],
  johnMcGowanT3: ["5b3f8268-a841-5291-8096-84d6bdc48b8d", "John E McGowan"],
  williamHMcGowan: ["7beb9f96-3fa1-509a-9ac4-c62cfd9e9eec", "William H McGowan"],
  donaldMcGrannahan: ["bbe4a616-0be8-5952-a230-1be0c8365dfa", "Donald V McGrannahan"],
  williamMcGrath: ["3bb3ab9d-4e83-5cd7-840a-8681229a6f70", "William McGrath"],
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

test("Batch 1054 publishes all 46 page-309 rows as 46 separate researched people", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(
      ...(await response.json()).filter(
        (person: { source_records: { pdf_page: number }[] }) =>
          person.source_records.some((row) => row.pdf_page === 309),
      ),
    );
  }
  expect(people).toHaveLength(46);
  expect(
    people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.filter((row) => row.pdf_page === 309),
    ),
  ).toHaveLength(46);
  for (const person of people) {
    expect(["not_started", "in_progress", "candidate_found"]).not.toContain(
      person.research_status,
    );
  }
});

test("Owen McGivern separates Navy, Assembly, and earlier legal employers", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.owenMcGivern);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.immediate_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "United States Navy",
      relationship_type: "military_assignment",
      temporal_basis: "explicit_immediate",
    }),
  ]);
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "New York State Assembly",
      relationship_type: "government_assignment",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Donovan, Leisure, Newton & Lumbard" }),
      expect.objectContaining({ canonical_organization: "James J. Dooling law office" }),
    ]),
  );
  await page.goto(`./people/${profiles.owenMcGivern[0]}/`);
  await expect(page.locator("main")).toContainText("OSS Naval Liaison Officer");
  await expect(page.locator("main")).toContainText("New York State Assembly");
  await expect(page.locator("main")).toContainText("Donovan, Leisure, Newton & Lumbard");
});

test("William McGovern separates Harvard from earlier Northwestern and Chicago Times jobs", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.williamMMcGovern);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "verified_employer_found",
  });
  expect(person.last_civilian_pre_service).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      role_title: "visiting lecturer in government",
      relationship_type: "employment",
      temporal_basis: "strongly_date_bounded",
    }),
  ]);
  expect(person.other_pre_oss_affiliations).toEqual(
    expect.arrayContaining([
      expect.objectContaining({ canonical_organization: "Northwestern University" }),
      expect.objectContaining({
        canonical_organization: "Chicago Daily Times",
        organization_name_as_found: "Chicago Times",
      }),
    ]),
  );
  await page.goto(`./people/${profiles.williamMMcGovern[0]}/`);
  await expect(page.locator("main")).toContainText("visiting lecturer in government");
  await expect(page.locator("main")).toContainText("Far East correspondent");
});

test("Donald McGrannahan remains a qualified probable student identity, not a Harvard employee", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.donaldMcGrannahan);
  expect(person).toMatchObject({
    identity_status: "probable",
    research_status: "occupation_only_found",
  });
  expect(person.name_variants).toEqual(
    expect.arrayContaining(["Donald V McGranahan", "Donald Vincent McGranahan"]),
  );
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: "Harvard University",
      relationship_type: "student",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  ]);
  await page.goto(`./people/${profiles.donaldMcGrannahan[0]}/`);
  await expect(page.locator("main")).toContainText("Donald Vincent McGranahan");
  await expect(page.locator("main")).toContainText("probable");
  await expect(page.locator("main")).toContainText("student");
});

test("Page-309 Army student category remains qualified and unnamed", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.barryMcGill);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "occupation_only_found",
  });
  expect(person.other_pre_oss_affiliations).toEqual([
    expect.objectContaining({
      canonical_organization: null,
      organization_id: null,
      occupation: "student",
      relationship_type: "student",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  ]);
  await page.goto(`./people/${profiles.barryMcGill[0]}/`);
  await expect(page.locator("main")).toContainText("student");
  await expect(page.locator("main")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Post-OSS and undefined Army entries create no public occupation", async ({ request, page }) => {
  for (const profile of [profiles.williamHMcGowan, profiles.williamMcGrath]) {
    const person = await publicPerson(request, profile);
    expect(person.identity_status).toBe("high_confidence");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).not.toEqual(
      expect.arrayContaining([expect.objectContaining({ claim_type: "occupation" })]),
    );
  }
  await page.goto(`./people/${profiles.williamHMcGowan[0]}/`);
  await expect(page.locator("main")).toContainText("1945-12-28");
  await page.goto(`./people/${profiles.williamMcGrath[0]}/`);
  await expect(page.locator("main")).toContainText("undefined code 590");
});

test("Page-309 duplicate and conflicting identities remain separate and visible", async ({ request, page }) => {
  for (const pair of [
    [profiles.davidMcGinnis505, profiles.davidMcGinnis506],
    [profiles.johnMcGowanLt, profiles.johnMcGowanT3],
  ] as const) {
    const first = await publicPerson(request, pair[0]);
    const second = await publicPerson(request, pair[1]);
    expect(first.person_id).not.toBe(second.person_id);
    expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
    expect(first.identity_status).toBe("ambiguous");
    expect(second.identity_status).toBe("ambiguous");
  }
  const leon = await publicPerson(request, profiles.leonMcGinnis);
  expect(leon).toMatchObject({
    identity_status: "conflicting",
    research_status: "conflicting_sources",
  });
  await page.goto(`./people/${profiles.leonMcGinnis[0]}/`);
  await expect(page.locator("main")).toContainText("Leon D. McGinnis");
});

test("Batch 1054 public assets omit private identifiers", async ({ request }) => {
  const batchIds = new Set(
    evidence.person_updates.map((item: { person_id: string }) => item.person_id),
  );
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    people.push(
      ...(await response.json()).filter((person: { person_id: string }) =>
        batchIds.has(person.person_id),
      ),
    );
  }
  expect(people).toHaveLength(46);
  const serialized = JSON.stringify(people);
  expect(serialized).not.toContain("candidate_identifier");
  expect(serialized).not.toContain("serial_number");
  expect(serialized).not.toContain("service_number");
  expect(serialized).not.toContain("raw_api_response");
});
