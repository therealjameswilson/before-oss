import fs from "node:fs";
import { expect, test } from "@playwright/test";
import type { APIRequestContext } from "@playwright/test";

const evidence = JSON.parse(
  fs.readFileSync(
    new URL(
      "../../research/evidence-page307-charles-w-mcdaniel-to-michael-v-mcdowell-review_batch-1052_2026-11-11.json",
      import.meta.url,
    ),
    "utf8",
  ),
);

const profiles = {
  geneMcDaniel: ["718ff7d4-e469-544e-993c-1f77cc15c5ab", "Gene A McDaniel"],
  deweyMcDonald: ["646b8baa-726e-5da5-9373-5d3515172cad", "Dewey E McDonald"],
  thomasMcDonnell: ["229b4fa8-5af4-5b8a-9980-4b643adfa6f9", "Thomas F McDonnell"],
  michaelMcDowell: ["43fafdd6-80a4-5d5d-9d08-bbca38e8a96f", "Michael V McDowell"],
  paulMcDougall: ["93a587a3-5e94-5c72-a349-009778e2cfe8", "Paul J McDougall"],
  jamesMcDaniel: ["38ffc93e-398c-5040-839b-16e2d30592d7", "James E McDaniel"],
  raymondMcDonald: ["c9f2ee69-91f5-5e10-a206-2ddef07ccf37", "Raymond W McDonald"],
  royMcDonald: ["53e08adb-c626-5a51-8ed8-3e8111c37709", "Roy W McDonald"],
  derveyMcDonald: ["24c85fe3-ff5a-5a8d-a9fd-14eeac196896", "Dervey A McDonald"],
  herveyMcDonald: ["7498979d-3069-5bd2-8ab0-748855fec83d", "Hervey A McDonald"],
  robertMcDougalT5: ["7db9f7df-bf95-5c1f-a059-f03c440c517c", "Robert L McDougal"],
  robertMcDougalUnranked: ["c6a74455-3ace-5b0a-9c9a-ddc2c70770c5", "Robert L McDougal"],
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

test("Batch 1052 publishes all page 307 rows with terminal outcomes", async ({ request }) => {
  const people = [];
  for (const shard of [..."abcdefghijklmnopqrstuvw", "y", "z", "other"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(
      ...(await response.json()).filter(
        (person: { source_records: { pdf_page: number }[] }) =>
          person.source_records.some((row) => row.pdf_page === 307),
      ),
    );
  }
  expect(people).toHaveLength(46);
  expect(
    people.flatMap((person: { source_records: { pdf_page: number }[] }) =>
      person.source_records.filter((row) => row.pdf_page === 307),
    ),
  ).toHaveLength(46);
  for (const person of people) {
    expect([
      "not_started",
      "in_progress",
      "candidate_found",
      "needs_identity_review",
      "needs_temporal_review",
    ]).not.toContain(person.research_status);
  }
});

test("Gene McDaniel and Dewey McDonald remain students rather than employees", async ({ request, page }) => {
  for (const profile of [profiles.geneMcDaniel, profiles.deweyMcDonald]) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        occupation: "student",
        relationship_type: "student",
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    ]);
  }
  await page.goto(`./people/${profiles.geneMcDaniel[0]}/`);
  await expect(page.locator("main")).toContainText("student");
  await expect(page.locator("main")).toContainText(
    "A dated occupation record does not establish that it immediately preceded OSS service",
  );
});

test("Page 307 occupations stay qualified and do not become named employers", async ({ request, page }) => {
  const expected = [
    [profiles.thomasMcDonnell, "miscellaneous occupation, not elsewhere classified"],
    [profiles.michaelMcDowell, "millwright"],
  ] as const;
  for (const [profile, occupation] of expected) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({
      identity_status: "high_confidence",
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toEqual([
      expect.objectContaining({
        canonical_organization: null,
        organization_id: null,
        occupation,
        relationship_type: "unknown",
        temporal_basis: "temporal_relation_uncertain",
        claim_confidence: "medium",
      }),
    ]);
  }
  await page.goto(`./people/${profiles.michaelMcDowell[0]}/`);
  await expect(page.locator("main")).toContainText("millwright");
  await expect(page.locator("main")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Undefined Army code 993 produces no Paul McDougall occupation claim", async ({ request, page }) => {
  const person = await publicPerson(request, profiles.paulMcDougall);
  expect(person).toMatchObject({
    identity_status: "high_confidence",
    research_status: "requires_archival_review",
  });
  expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(person.last_civilian_pre_service).toHaveLength(0);
  expect(person.other_pre_oss_affiliations).toHaveLength(0);
  expect(person.claims).not.toEqual(
    expect.arrayContaining([expect.objectContaining({ claim_type: "occupation" })]),
  );
  await page.goto(`./people/${profiles.paulMcDougall[0]}/`);
  await expect(page.locator("main")).toContainText("undefined code 993");
  await expect(page.locator("main")).toContainText("Archival-review priority");
});

test("Conflicting protected identifiers do not publish affiliations", async ({ request, page }) => {
  for (const profile of [
    profiles.jamesMcDaniel,
    profiles.raymondMcDonald,
    profiles.royMcDonald,
  ]) {
    const person = await publicPerson(request, profile);
    expect(person).toMatchObject({
      identity_status: "conflicting",
      research_status: "conflicting_sources",
    });
    expect(person.immediate_pre_oss_affiliations).toHaveLength(0);
    expect(person.last_civilian_pre_service).toHaveLength(0);
    expect(person.other_pre_oss_affiliations).toHaveLength(0);
    expect(person.claims).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          claim_type: "identity",
          claim_confidence: "conflicting",
          publication_status: "conflicting",
        }),
      ]),
    );
  }
  await page.goto(`./people/${profiles.royMcDonald[0]}/`);
  await expect(page.locator("main")).toContainText("Evidence conflict");
  await expect(page.locator("main")).toContainText(
    "No disputed affiliation is treated as an established employer",
  );
});

test("Both page 307 duplicate clusters remain separate and visible", async ({ request, page }) => {
  for (const [firstProfile, secondProfile] of [
    [profiles.derveyMcDonald, profiles.herveyMcDonald],
    [profiles.robertMcDougalT5, profiles.robertMcDougalUnranked],
  ] as const) {
    const first = await publicPerson(request, firstProfile);
    const second = await publicPerson(request, secondProfile);
    expect(first.person_id).not.toBe(second.person_id);
    expect(first.possible_duplicate_group).toBeTruthy();
    expect(first.possible_duplicate_group).toBe(second.possible_duplicate_group);
    expect(first.identity_status).toBe("ambiguous");
    expect(second.identity_status).toBe("ambiguous");
  }
  await page.goto(`./people/${profiles.derveyMcDonald[0]}/`);
  await expect(page.locator("main")).toContainText("Hervey A McDonald");
  await page.goto(`./people/${profiles.robertMcDougalT5[0]}/`);
  await expect(page.locator("main")).toContainText("Robert L McDougal");
});

test("Batch 1052 public assets omit private identifiers", async ({ request }) => {
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
  expect(serialized).not.toContain("bulk_record_ordinal");
  expect(serialized).not.toContain("raw_api_response");
});
