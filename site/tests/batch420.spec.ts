import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 420 publishes only identifier-backed occupation evidence", async ({ page }) => {
  for (const [id, name, occupation, serial] of [
    ["87d5154e-7d88-548c-b8dd-3d12fc9d61d3", "Eugene H Clapp", "Accountants and auditors", "••••0531"],
    ["b21b8400-e4ab-5d12-afd4-8beb5b171805", "Aldo Clara", "Cement and concrete finishers", "••••7654"],
    ["ccd26a63-4584-5572-8a65-d80b4804ec57", "Alfred C Clark", "Actors and actresses", "••••1738"],
    ["80502274-6aa9-565e-8bb9-9eeede5228dc", "Alvin Clark", "Waiters and waitresses, except private family", "••••3404"],
  ] as const) {
    const p = profile(id);
    expect(p).toMatchObject({
      display_name: name,
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "occupation_only_found",
    });
    expect(p.source_records[0]).toMatchObject({ pdf_page: 82, serial_masked: serial });
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
      occupation,
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
      organization_id: null,
    }));

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(occupation);
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(/No (?:reviewed claim|reliable pre-OSS employer)/);
  }
});

test("Batch 420 preserves Eugene Clapp's unexplained Army text without changing the indexed name", async ({ page }) => {
  const p = profile("87d5154e-7d88-548c-b8dd-3d12fc9d61d3");
  expect(p.display_name).toBe("Eugene H Clapp");
  expect(p.name_variants).not.toContain("Eugene H Clapp II");

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.locator("main")).toContainText("SND");
  await expect(page.locator("main")).toContainText("preserved without expansion");
  await expect(page.locator("main")).not.toContainText("Eugene H Clapp II");
});

test("Batch 420 records Alvin C Clark as a variant while keeping entry and index grades distinct", async ({ page }) => {
  const p = profile("80502274-6aa9-565e-8bb9-9eeede5228dc");
  expect(p.name_variants).toContain("Alvin C Clark");
  expect(p.source_records[0]).toMatchObject({ rank_as_indexed: "T-5", box: "126" });

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.locator("main")).toContainText("Alvin C Clark");
  await expect(page.locator("main")).toContainText("entry grade Private");
  await expect(page.locator("main")).toContainText("T-5");
});

test("Batch 420 keeps James Clance's identifier conflict visible and candidate assignments unmerged", async ({ page }) => {
  const p = profile("124c45f8-fd99-58fe-8434-aff464a3e0ed");
  expect(p).toMatchObject({
    display_name: "James W Clance",
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
    research_status: "conflicting_sources",
  });
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);
  expect(p.claims).toHaveLength(1);
  expect(p.claims[0]).toMatchObject({ claim_type: "identity", claim_confidence: "conflicting", publication_status: "conflicting" });

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "James W Clance", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("different private identifier");
  await expect(page.locator("main")).toContainText("records remain unmerged");
  await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 420 withholds Richard Clair and Frederick Clapp candidates", async ({ page }) => {
  for (const [id, name] of [
    ["f94889dd-75c6-53aa-9f57-d280eb5e4194", "Richard R Clair"],
    ["bc2db47c-a1dd-5f25-9455-b4e06f9f4920", "Frederick G Clapp"],
  ]) {
    const p = profile(id);
    expect(p).toMatchObject({
      display_name: name,
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "candidate_found",
    });
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reviewed claim currently meets the publication threshold");
    await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 420 keeps all sixteen Albert Clark candidates separate", async ({ page }) => {
  const p = profile("2142e71f-e1a7-5762-88ff-570a42caf409");
  expect(p).toMatchObject({
    display_name: "Albert L Clark",
    identity_status: "ambiguous",
    research_status: "needs_identity_review",
  });
  expect(p.claims).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.locator("main")).toContainText("sixteen exact-name");
  await expect(page.locator("main")).toContainText("unit to distinguish them");
  await expect(page.locator("main")).toContainText("Box 126");
});

test("Batch 420 gives Beulah Clapp and Cloyd Clare complete archival-review profiles", async ({ page }) => {
  for (const [id, name, box] of [
    ["dec041d6-5431-5f49-827c-6fe8f38a7f61", "Beulah O Clapp", "125"],
    ["623adcf2-e8e5-5ed8-979e-ea21b4d69746", "Cloyd Clare", "126"],
  ]) {
    const p = profile(id);
    expect(p).toMatchObject({
      display_name: name,
      identity_status: "unresolved",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
    });
    expect(p.claims).toEqual([]);
    expect(p.source_records[0]).toMatchObject({ pdf_page: 82, box });

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText("requires archival review");
    await expect(page.locator("main")).toContainText(`Box ${box}`);
    await expect(page.locator("main")).toContainText("230/86/28/06");
  }
});

test("Batch 420 cohort is searchable by exact indexed name", async ({ page }) => {
  for (const name of [
    "Richard R Clair",
    "James W Clance",
    "Beulah O Clapp",
    "Eugene H Clapp",
    "Frederick G Clapp",
    "Aldo Clara",
    "Cloyd Clare",
    "Albert L Clark",
    "Alfred C Clark",
    "Alvin Clark",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
