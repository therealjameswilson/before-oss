import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const organizations = JSON.parse(fs.readFileSync(new URL("../src/data/generated/organizations.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 416 separates Archie Chun-Ming's immediate Army assignment, occupation, and civic affiliation", async ({ page }) => {
  const p = profile("370cf1be-3778-5aad-bf3b-690f5cd78525");
  expect(p.identity_status).toBe("high_confidence");
  expect(p.personnel_category).toBe("commissioned_army_officer");
  expect(p.commissioned_officer).toBe(true);
  expect(p.research_status).toBe("completed");
  expect(p.source_records[0]).toMatchObject({
    pdf_page: 81,
    box: "124",
    rank_as_indexed: null,
    serial_masked: "••••8700",
  });
  expect(p.immediate_pre_oss_affiliations).toHaveLength(1);
  expect(p.immediate_pre_oss_affiliations[0]).toMatchObject({
    canonical_organization: "United States Army",
    organization_name_as_found: "a reserve unit in Hawaii",
    role_title: "captain, Medical Corps",
    occupation: "physician",
    relationship_type: "military_assignment",
    temporal_basis: "explicit_immediate",
    claim_confidence: "high",
  });
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual(expect.arrayContaining([
    expect.objectContaining({
      canonical_organization: "Hawaii Chinese Civic Association",
      role_title: "president",
      relationship_type: "professional_affiliation",
      temporal_basis: "documented_prewar",
    }),
    expect.objectContaining({
      canonical_organization: null,
      occupation: "physician",
      relationship_type: "unknown",
      city: "Honolulu",
      temporal_basis: "documented_prewar",
    }),
  ]));

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Archie Chun-Ming", exact: true })).toBeVisible();
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("unidentified Hawaii reserve unit");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("military assignment");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("Hawaii Chinese Civic Association");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText("physician");
  await expect(page.locator("main")).toContainText("The Fighting Doctors of the Office of Strategic Services");

  const hcca = organizations.find((o: { canonical_name: string }) => o.canonical_name === "Hawaii Chinese Civic Association");
  expect(hcca).toBeTruthy();
  expect(hcca.documented_person_count).toBe(1);
  await page.goto(`./organizations/${hcca.organization_id}/`);
  await expect(page.getByRole("heading", { name: "Hawaii Chinese Civic Association", exact: true })).toBeVisible();
  await expect(page.getByRole("link", { name: "Archie Chun-Ming", exact: true })).toBeVisible();
});

test("Batch 416 publishes four bounded Army occupations without inventing employers", async ({ page }) => {
  for (const [id, name, occupation, date, serial, category] of [
    ["8c84a6ca-626d-51dd-b4d4-851be285f3b8", "Oral L Chupp", "Repairmen and mechanics, n.e.c.", "10 March 1942", "••••8325", "enlisted_army_personnel"],
    ["9e0f0f21-c4a4-5105-95fe-9e326dde87f5", "Edward J Church", "Clerks, general office", "18 April 1941", "••••1469", "unknown_or_indeterminate"],
    ["b6e6a6d2-4da7-580a-bc82-874764976636", "Phillip E Churchill", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "29 October 1942", "••••3631", "enlisted_army_personnel"],
    ["3e6c06db-82ef-5df9-918a-d3a7a7a35d16", "Raymond Chynoweth", "Shipping and receiving clerks", "23 April 1942", "••••8312", "enlisted_army_personnel"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.personnel_category).toBe(category);
    expect(p.commissioned_officer).toBe(category === "enlisted_army_personnel" ? false : null);
    expect(p.research_status).toBe("occupation_only_found");
    expect(p.source_records[0]).toMatchObject({ pdf_page: 81, box: "124", serial_masked: serial });
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toHaveLength(1);
    expect(p.other_pre_oss_affiliations[0]).toMatchObject({
      occupation,
      organization_id: null,
      relationship_type: "unknown",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    });
    expect(p.other_pre_oss_affiliations[0].date_precision).toContain(date);

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, exact: true })).toBeVisible();
    await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).toContainText(occupation);
    await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
    await expect(page.locator("main")).toContainText("NARA Compiled Code Lists");
  }

  expect(profile("b6e6a6d2-4da7-580a-bc82-874764976636").name_variants).toContain("Philip E Churchill");
  expect(profile("9e0f0f21-c4a4-5105-95fe-9e326dde87f5").identity_evidence).toContain("malformed grade and branch fields");

  await page.goto("./people/9e0f0f21-c4a4-5105-95fe-9e326dde87f5/");
  await expect(page.locator("main")).toContainText("record-quality warning");
  await expect(page.locator("main")).toContainText("malformed grade and branch fields");
});

test("Batch 416 preserves the Woon Chung rank mismatch as an unpublished identity candidate", async ({ page }) => {
  const p = profile("070898ca-4d78-5bee-9550-e4690a32fc34");
  expect(p.identity_status).toBe("ambiguous");
  expect(p.research_status).toBe("needs_identity_review");
  expect(p.personnel_category).toBe("commissioned_army_officer");
  expect(p.commissioned_officer).toBe(true);
  expect(p.source_records[0]).toMatchObject({ rank_as_indexed: "1st Lt", serial_masked: null });
  expect(p.claims).toEqual([]);
  expect(p.immediate_pre_oss_affiliations).toEqual([]);
  expect(p.last_civilian_pre_service).toEqual([]);
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Woon S Chung", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("one exact-name private entry dated 9 June 1943");
  await expect(page.locator("main")).toContainText("no hometown, birth datum, unit, promotion or personnel-file bridge");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Batch 416 archive-routes four unresolved people and makes the full cohort searchable", async ({ page }) => {
  for (const id of [
    "d432e581-7896-58b9-b132-fbe3cfbe36a9",
    "b59eb964-ab13-5d7b-bb80-1c53517f7285",
    "1afbe106-7187-5933-9beb-f3e298f54c50",
    "e7a62c0e-a77b-5615-b506-42ec4940ca0f",
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("unresolved");
    expect(p.research_status).toBe("requires_archival_review");
    expect(p.claims).toEqual([]);
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);
    expect(p.source_records[0].serial_masked).toBeNull();
  }
  expect(profile("e7a62c0e-a77b-5615-b506-42ec4940ca0f").source_records[0].box).toBe("125");

  for (const name of [
    "Woon S Chung",
    "Archie Chun-Ming",
    "Oral L Chupp",
    "Edward J Church",
    "Mallory D Church",
    "Rosa M Church",
    "Phillip E Churchill",
    "Mary B Chynoweth",
    "Raymond Chynoweth",
    "Michael A Ciaccio",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
