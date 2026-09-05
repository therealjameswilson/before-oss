import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 417 publishes six bounded Army occupations without inventing employers", async ({ page }) => {
  for (const [id, name, occupation, date, serial] of [
    ["f87a2514-743b-5784-aa1c-10ae3f74f207", "Cafiero Cicala", "Accountants and auditors", "21 May 1941", "••••4480"],
    ["310667a6-01eb-5938-993b-7459a3a0a756", "Anthony L Cicatelli", "Furnacemen, smelters, and pourers", "25 May 1943", "••••8183"],
    ["498487fe-3615-5a6b-a647-79d8d4aa109a", "Peter J Cicchini", "Chauffeurs and drivers, bus, taxi, truck, tractor", "12 May 1943", "••••9871"],
    ["bf3d2193-fd17-5ce7-96d9-0e82b6f958d3", "Salvatore Cicciari", "Occupations in fabrication of textile products, n.e.c.", "2 December 1942", "••••1932"],
    ["eb613c4a-ebc5-5888-9bd7-b85ae2a00f0b", "Angelo R Ciccolella", "Semiprofessional occupations, n.e.c.", "28 October 1942", "••••8437"],
    ["46cd2a91-c16f-55a3-9385-dd028afab8e1", "Charles Ciccone", "Filers, grinders, buffers, and polishers (metal)", "20 November 1942", "••••2715"],
  ]) {
    const p = profile(id);
    expect(p.identity_status).toBe("high_confidence");
    expect(p.personnel_category).toBe("enlisted_army_personnel");
    expect(p.commissioned_officer).toBe(false);
    expect(p.research_status).toBe("occupation_only_found");
    expect(p.source_records[0]).toMatchObject({ pdf_page: 81, box: "125", serial_masked: serial });
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
});

test("Batch 417 keeps unlabeled Army codes out of occupation claims", async ({ page }) => {
  const george = profile("fc079b9b-2f09-52f0-bce0-bcc0cdad9290");
  expect(george).toMatchObject({
    display_name: "George Ciampa",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(george.source_records[0]).toMatchObject({ pdf_page: 81, box: "125", serial_masked: "••••3170" });
  expect(george.other_pre_oss_affiliations).toEqual([]);
  expect(george.claims.map((c: { claim_type: string }) => c.claim_type)).toEqual(["identity"]);
  expect(george.identity_evidence).toContain("value 999");
  expect(george.identity_evidence).toContain("not assigned a defensible label");

  await page.goto(`./people/${george.person_id}/`);
  await expect(page.getByRole("heading", { name: "George Ciampa", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("value 999");
  await expect(page.locator("main")).toContainText("different identifier and 1943 entry chronology");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");

  const guy = profile("0e6f2086-89b8-5e61-9e90-16f67826784f");
  expect(guy).toMatchObject({
    display_name: "Guy A Ciaraldi",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "needs_temporal_review",
  });
  expect(guy.source_records[0]).toMatchObject({ pdf_page: 81, box: "125", serial_masked: "••••0925" });
  expect(guy.other_pre_oss_affiliations).toEqual([]);
  expect(guy.claims.map((c: { claim_type: string }) => c.claim_type)).toEqual(["identity"]);
  expect(guy.identity_evidence).toContain("1 July 1946");
  expect(guy.identity_evidence).toContain("value 177 is not decoded");

  await page.goto(`./people/${guy.person_id}/`);
  await expect(page.getByRole("heading", { name: "Guy A Ciaraldi", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("after OSS termination");
  await expect(page.locator("main")).toContainText("20 September 1945");
  await expect(page.locator("main")).toContainText("value 177");
});

test("Batch 417 preserves identity-only evidence for Clement Cianfichi and Arthur Ciarmicoli", async ({ page }) => {
  const clement = profile("f1402cfa-f7fc-57c2-8c4f-000d5eb20813");
  expect(clement).toMatchObject({
    display_name: "Clement Cianfichi",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(clement.source_records[0]).toMatchObject({ serial_masked: "••••0817", box: "125" });
  expect(clement.immediate_pre_oss_affiliations).toEqual([]);
  expect(clement.last_civilian_pre_service).toEqual([]);
  expect(clement.other_pre_oss_affiliations).toEqual([]);
  await page.goto(`./people/${clement.person_id}/`);
  await expect(page.getByRole("heading", { name: "Clement Cianfichi", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Army OSS veteran");
  await expect(page.locator("main")).toContainText("post-1959 master-carpenter career");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");

  const arthur = profile("6e929fd1-2acc-5260-a61d-abe4c9fc7373");
  expect(arthur).toMatchObject({
    display_name: "Arthur Ciarmicoli",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(arthur.source_records[0]).toMatchObject({ serial_masked: null, box: "125" });
  expect(arthur.immediate_pre_oss_affiliations).toEqual([]);
  expect(arthur.last_civilian_pre_service).toEqual([]);
  expect(arthur.other_pre_oss_affiliations).toEqual([]);
  await page.goto(`./people/${arthur.person_id}/`);
  await expect(page.getByRole("heading", { name: "Arthur Ciarmicoli", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Chrysler Mission");
  await expect(page.locator("main")).toContainText("In re Lo Dolce");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("No reliable pre-OSS employer");
});

test("Batch 417 withholds the unbridged Charles Ciccone Tacoma candidate", async ({ page }) => {
  const p = profile("46cd2a91-c16f-55a3-9385-dd028afab8e1");
  expect(p.claims).toHaveLength(2);
  expect(p.claims.map((c: { claim_text: string }) => c.claim_text).join(" ")).not.toContain("Tacoma Mission sergeant");
  expect(p.other_pre_oss_affiliations).toHaveLength(1);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.getByRole("heading", { name: "Charles Ciccone", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("no identifier bridge establishes that he is the indexed person");
  await expect(page.locator("main")).not.toContainText("demolitions man");
  await expect(page.locator("main")).not.toContainText("OSS in Action: The Mediterranean and European Theaters");
  await expect(page.locator("main")).toContainText("Filers, grinders, buffers, and polishers (metal)");
});

test("Batch 417 cohort is searchable by exact indexed name", async ({ page }) => {
  for (const name of [
    "George Ciampa",
    "Clement Cianfichi",
    "Guy A Ciaraldi",
    "Arthur Ciarmicoli",
    "Cafiero Cicala",
    "Anthony L Cicatelli",
    "Peter J Cicchini",
    "Salvatore Cicciari",
    "Angelo R Ciccolella",
    "Charles Ciccone",
  ]) {
    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
