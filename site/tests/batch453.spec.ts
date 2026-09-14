import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 453 preserves all ten printed rows and masks every private identifier", async () => {
  const expected = [
    ["3d79bf51-05bc-517a-bab2-706744659601", "Agent Confidential", "9aa56d54-f05c-5ddd-9229-d60d7b597864", null, null],
    ["733c3e5e-f419-5308-82de-a65a67111c88", "Eugene A Confrey", "5cc468b1-07b7-5160-b43b-2e9721c44fca", "T-5", "••••1812"],
    ["52f4e38d-79e4-5b49-9aab-313cfbbee46a", "Gerard M Congdon", "cb0d8691-4566-5122-8f3b-661bbd40ca25", null, "••••0188"],
    ["b4cc82ec-7a65-5e7f-b750-78ca839038fe", "Louise E Congdon", "d18debd3-f418-5969-9a69-2a64f9e0515d", null, null],
    ["a63425f3-7fcc-5a16-a5fd-f72f6a0ebc47", "Dolores S Conger", "c1248c1b-6b9e-5323-b7f8-d57b02dfeeef", null, null],
    ["98182e2d-bddb-5228-9b5c-3dafaea32ff8", "Melvin R Conger", "08cae408-5635-5da5-b713-d74f587ecc0e", null, "••••8122"],
    ["afeaf736-44a0-50a3-a427-90cff3491583", "Eleanor F Congleton", "478d46a0-ee94-5598-907a-9258e34679db", null, "••••7187"],
    ["054d1a09-c264-548c-b4a4-f3e9dfb6a6e0", "Charles E Conkey", "3e789a3d-c6c0-5e34-97b2-6cd8bb5c4ab2", null, "••••9571"],
    ["a05400b2-22d1-5ec2-9c56-980a93e2a311", "Garret E Conklin", "f4959844-3565-5ba6-98fc-08dd15253401", null, "••••1470"],
    ["234fcca0-46ae-59ba-8779-c2022f50c50b", "Groff Conklin", "df88c6b9-97de-53f0-bc91-517304e1473a", null, null],
  ];

  for (const [id, name, sourceRecordId, rank, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      rank_as_indexed: rank,
      serial_masked: serial,
      box: "138",
      archive_location: "230/86/29/01",
      pdf_page: 89,
    });
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 453 preserves the anonymized row without expanding its note", async ({ page }) => {
  const agent = profile("3d79bf51-05bc-517a-bab2-706744659601");
  expect(agent).toMatchObject({
    display_name: "Agent Confidential",
    identity_status: "unresolved",
    research_status: "requires_archival_review",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
  });
  expect(agent.source_records[0].notes_as_indexed).toBe("no real n");
  expect(agent.claims).toEqual([]);

  await page.goto(`./people/${agent.person_id}/`);
  await expect(page.getByRole("heading", { name: "Agent Confidential", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("no real n");
  await expect(page.locator("main")).toContainText("deliberately anonymized");
  await expect(page.locator("main")).not.toContainText("no real name");
});

test("Batch 453 publishes Groff Conklin's earlier Doubleday role without conflating temporal categories", async ({ page }) => {
  const groff = profile("234fcca0-46ae-59ba-8779-c2022f50c50b");
  expect(groff).toMatchObject({
    display_name: "Groff Conklin",
    identity_status: "high_confidence",
    research_status: "documented_prewar_employer_found",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
  });
  expect(groff.immediate_pre_oss_affiliations).toEqual([]);
  expect(groff.last_civilian_pre_service).toEqual([]);
  expect(groff.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Doubleday Bookstore",
      organization_name_as_found: "New York's Doubleday Bookstore",
      role_title: "Assistant manager",
      occupation: "Fiction editor",
      relationship_type: "employment",
      temporal_basis: "documented_prewar",
      claim_confidence: "high",
      immediate_pre_oss: false,
      last_civilian_pre_service: false,
    }),
  );
  expect(groff.claims).toHaveLength(2);

  await page.goto(`./people/${groff.person_id}/`);
  await expect(page.getByRole("heading", { name: "Groff Conklin", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Doubleday Bookstore");
  await expect(page.locator("main")).toContainText("Assistant manager");
  await expect(page.locator("main")).toContainText("fiction editor");
  await expect(page.locator("main")).toContainText("documented pre-OSS");
  await expect(page.locator("main")).toContainText(
    "Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold",
  );
  await expect(page.locator("main")).toContainText(
    "Last civilian employer before serviceFor this question: No reliable pre-OSS employer has yet been identified",
  );
  await expect(page.locator("main")).toContainText(
    "A single last civilian employer before wartime or military service has not yet been established",
  );
});

test("Batch 453 exposes both supporting Groff Conklin sources", async ({ page }) => {
  const groff = profile("234fcca0-46ae-59ba-8779-c2022f50c50b");
  const sourceUrls = groff.claims.flatMap((claim: { sources: { source: { stable_url: string } }[] }) =>
    claim.sources.map(({ source }) => source.stable_url),
  );
  expect(sourceUrls).toContain("https://www.cia.gov/stories/story/edna-andrade-from-the-oss-to-op-art/");
  expect(sourceUrls).toContain("https://findingaids.library.upenn.edu/records/PRIN_MUDD_C1656");

  await page.goto(`./people/${groff.person_id}/`);
  await expect(page.getByRole("link", { name: "Edna Andrade: From the OSS to Op Art" }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: "Groff Conklin Files for The Smart Set Anthology" }).first()).toBeVisible();
  await expect(page.locator("main")).toContainText(/high confidence/i);
});

test("Batch 453 leaves unverified candidates claim-free and directs them to Box 138", async ({ page }) => {
  const expected = [
    ["733c3e5e-f419-5308-82de-a65a67111c88", "Eugene A Confrey", "unresolved", "needs_identity_review"],
    ["52f4e38d-79e4-5b49-9aab-313cfbbee46a", "Gerard M Congdon", "unresolved", "needs_identity_review"],
    ["b4cc82ec-7a65-5e7f-b750-78ca839038fe", "Louise E Congdon", "unresolved", "requires_archival_review"],
    ["a63425f3-7fcc-5a16-a5fd-f72f6a0ebc47", "Dolores S Conger", "unresolved", "requires_archival_review"],
    ["98182e2d-bddb-5228-9b5c-3dafaea32ff8", "Melvin R Conger", "ambiguous", "needs_identity_review"],
    ["afeaf736-44a0-50a3-a427-90cff3491583", "Eleanor F Congleton", "unresolved", "needs_identity_review"],
    ["054d1a09-c264-548c-b4a4-f3e9dfb6a6e0", "Charles E Conkey", "unresolved", "needs_identity_review"],
    ["a05400b2-22d1-5ec2-9c56-980a93e2a311", "Garret E Conklin", "unresolved", "needs_identity_review"],
  ];

  for (const [id, name, identityStatus, researchStatus] of expected) {
    const person = profile(id);
    expect(person).toMatchObject({
      display_name: name,
      identity_status: identityStatus,
      research_status: researchStatus,
    });
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
    expect(person.next_action).toContain("Box 138");
  }

  const melvin = profile("98182e2d-bddb-5228-9b5c-3dafaea32ff8");
  await page.goto(`./people/${melvin.person_id}/`);
  await expect(page.getByRole("heading", { name: "Melvin R Conger", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("A biographical lead aligns that candidate");
  await expect(page.locator("main")).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed",
  );
});
