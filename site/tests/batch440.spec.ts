import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 440 preserves five Army occupation categories without inventing employers", async ({ page }) => {
  const expected = [
    ["10ab5945-87d3-54c6-b24a-464067350c63", "Myron Cohn", "Accountants and auditors", "1942-10-22", "A_direct_official"],
    ["647df6e3-22f8-5676-bbd4-4b7e3ef93c78", "Trayone J Cojerian", "Machinists", "1942-10-19", "A_direct_official"],
    ["4a54a1c2-512e-59d7-868d-667e06fb32de", "Raymond T Col", "Accountants and auditors", "1942-08-29", "A_direct_official"],
    ["ceece5a5-3961-56e1-9ab5-0e3433237f2b", "Hugo Colacicco", "Machinists", "1941-09-08", "A_direct_official"],
    ["b7cfa9e8-1ce0-52fc-a02c-2af2fd1695ae", "Alfred Colandrea", "Job pressman or casting-machine operator (code 649)", "1943-05-14", "D_correlative_or_secondary"],
  ];

  for (const [id, name, occupation, endDate, sourceQuality] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        organization_id: null,
        occupation,
        relationship_type: "unknown",
        end_date: endDate,
        temporal_basis: "strongly_date_bounded",
        identity_confidence: "confirmed",
        claim_confidence: "medium",
        source_quality: sourceQuality,
      }),
    );
  }

  const alfred = profile("b7cfa9e8-1ce0-52fc-a02c-2af2fd1695ae");
  await page.goto(`./people/${alfred.person_id}/`);
  await expect(page.getByRole("heading", { name: "Alfred Colandrea", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Job pressman or casting-machine operator");
  await expect(page.locator("main")).toContainText("does not distinguish them or identify an employer");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 440 models Theodore Cohn as a student rather than an employee", async ({ page }) => {
  const theodore = profile("308c828c-c004-58ea-b908-8694d998d3be");
  expect(theodore).toMatchObject({
    display_name: "Theodore Cohn",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(theodore.immediate_pre_oss_affiliations).toEqual([]);
  expect(theodore.last_civilian_pre_service).toEqual([]);
  expect(theodore.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      role_title: "Student",
      occupation: null,
      relationship_type: "student",
      end_date: "1942-09-08",
      temporal_basis: "strongly_date_bounded",
      identity_confidence: "confirmed",
      claim_confidence: "medium",
    }),
  );

  await page.goto(`./people/${theodore.person_id}/`);
  await expect(page.getByRole("heading", { name: "Theodore Cohn", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Student");
  await expect(page.locator("main")).toContainText("no school or employer is identified");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 440 publishes Martin G Cohn only as a probable earlier occupation", async ({ page }) => {
  const martin = profile("2636ea5f-bee1-5024-8a41-2f0d26e29935");
  expect(martin).toMatchObject({
    display_name: "Martin G Cohn",
    identity_status: "probable",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "occupation_only_found",
  });
  expect(martin.immediate_pre_oss_affiliations).toEqual([]);
  expect(martin.last_civilian_pre_service).toEqual([]);
  expect(martin.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "film editor",
      relationship_type: "unknown",
      start_date: "1920",
      end_date: "1920",
      temporal_basis: "documented_prewar",
      identity_confidence: "probable",
      claim_confidence: "medium",
      publication_status: "publish_qualified",
    }),
  );

  await page.goto(`./people/${martin.person_id}/`);
  await expect(page.getByRole("heading", { name: "Martin G Cohn", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("film editor");
  await expect(page.locator("main")).toContainText("probable");
  await expect(page.locator("main")).toContainText("1920");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 440 preserves every row, masks identifiers and keeps unresolved people visible", async ({ page }) => {
  const expected = [
    ["2636ea5f-bee1-5024-8a41-2f0d26e29935", "Martin G Cohn", "934a363a-48d3-503d-bf01-ecc56f325ac8", false],
    ["10ab5945-87d3-54c6-b24a-464067350c63", "Myron Cohn", "a78f2568-5280-5eff-b499-fb391d76ff9d", true],
    ["308c828c-c004-58ea-b908-8694d998d3be", "Theodore Cohn", "f1c7b930-4202-51ae-bdea-b05ba2bcd5d2", true],
    ["647df6e3-22f8-5676-bbd4-4b7e3ef93c78", "Trayone J Cojerian", "86b34432-622b-5719-996f-cf415c4ea17b", true],
    ["2adf8f2a-eba9-5070-9c00-9069c64701c4", "Owen S Coke", "61f55de7-1fb7-5dfc-ba29-9a9db48d226f", true],
    ["9fd2fecf-69de-5e40-90db-5ebbb37eb95a", "Dorothy E Cokeley", "6b0eea28-0ed3-5444-848c-2b8bb6ba5cb8", false],
    ["7d7e46cd-d204-50d0-999e-7a2486231ba6", "Vassilia Cokinides", "5e2f49fb-4c37-5480-93ad-8a2380c67d82", false],
    ["4a54a1c2-512e-59d7-868d-667e06fb32de", "Raymond T Col", "a85ebadd-3e05-5a80-b7cf-9969c38d2a72", true],
    ["ceece5a5-3961-56e1-9ab5-0e3433237f2b", "Hugo Colacicco", "2069a336-359a-50a0-a2b8-fe9d06cc48f4", true],
    ["b7cfa9e8-1ce0-52fc-a02c-2af2fd1695ae", "Alfred Colandrea", "108af738-f172-5409-864a-a974d3a449db", true],
  ];

  for (const [id, name, sourceRecordId, hasSerial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 86,
      rank_as_indexed: null,
      box: "133",
      archive_location: "230/86/28/07",
    });
    if (hasSerial) {
      expect(person.source_records[0].serial_masked).toMatch(/^••••.{4}$/u);
    } else {
      expect(person.source_records[0].serial_masked).toBeNull();
    }
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }

  for (const id of [
    "2adf8f2a-eba9-5070-9c00-9069c64701c4",
    "9fd2fecf-69de-5e40-90db-5ebbb37eb95a",
    "7d7e46cd-d204-50d0-999e-7a2486231ba6",
  ]) {
    const person = profile(id);
    expect(person.identity_status).toBe("unresolved");
    expect(person.research_status).toBe("requires_archival_review");
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.claims).toEqual([]);
  }

  const owen = profile("2adf8f2a-eba9-5070-9c00-9069c64701c4");
  await page.goto(`./people/${owen.person_id}/`);
  await expect(page.getByRole("heading", { name: "Owen S Coke", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("short six-digit private identifier");
  await expect(page.locator("main")).toContainText("Review Box 133");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});
