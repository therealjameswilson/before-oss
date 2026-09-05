import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"));
const profile = (id: string) => people.find((p: { person_id: string }) => p.person_id === id);

test("Batch 424 publishes three qualified observations without inventing employers", async ({ page }) => {
  for (const [id, name, category, occupation, relationship] of [
    ["2e0e902e-a559-5fe2-bd37-7babfa5aabde", "Richard E Clark", "enlisted_army_personnel", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "unknown"],
    ["5bb7af15-9e32-5a5e-851b-7946837107ea", "Roger A Clark Jr.", "enlisted_army_personnel", "Student", "student"],
    ["b818c5b2-95ae-5ce7-b871-6197d800a2e4", "Russell W Clark", "unknown_or_indeterminate", "Photographers", "unknown"],
  ]) {
    const p = profile(String(id));
    expect(p).toMatchObject({
      display_name: name,
      personnel_category: category,
      research_status: "occupation_only_found",
    });
    expect(p.immediate_pre_oss_affiliations).toEqual([]);
    expect(p.last_civilian_pre_service).toEqual([]);
    expect(p.other_pre_oss_affiliations).toContainEqual(expect.objectContaining({
      organization_id: null,
      occupation,
      relationship_type: relationship,
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }));

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: String(name), exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(String(occupation));
    await expect(page.locator("main")).toContainText("No reliable pre-OSS employer");
    await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 424 applies the reserve-card layout and preserves Russell Clark's anomaly", async ({ page }) => {
  const roger = profile("5bb7af15-9e32-5a5e-851b-7946837107ea");
  expect(roger).toMatchObject({ identity_status: "confirmed", commissioned_officer: false });
  expect(roger.claims).toContainEqual(expect.objectContaining({
    claim_type: "other_pre_oss_affiliation",
    claim_confidence: "medium",
  }));
  expect(JSON.stringify(roger)).not.toContain("699");

  await page.goto(`./people/${roger.person_id}/`);
  await expect(page.locator("main")).toContainText("Enlisted Reserve Corps alternate-card occupation field at columns 71-73");
  await expect(page.locator("main")).toContainText("no school or employer is identified");

  const russell = profile("b818c5b2-95ae-5ce7-b871-6197d800a2e4");
  expect(russell).toMatchObject({
    identity_status: "high_confidence",
    personnel_category: "unknown_or_indeterminate",
    commissioned_officer: null,
  });
  await page.goto(`./people/${russell.person_id}/`);
  await expect(page.locator("main")).toContainText("grade field is malformed");
  await expect(page.locator("main")).toContainText("no employer or employment arrangement is identified");
});

test("Batch 424 publishes Samuel Clark's identity but leaves value 999 uninterpreted", async ({ page }) => {
  const p = profile("3e156d88-65fd-58a1-ad6e-b45a9f61cdec");
  expect(p).toMatchObject({
    display_name: "Samuel E Clark",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "requires_archival_review",
  });
  expect(p.claims).toHaveLength(1);
  expect(p.claims[0]).toMatchObject({ claim_type: "identity", claim_confidence: "confirmed" });
  expect(p.other_pre_oss_affiliations).toEqual([]);

  await page.goto(`./people/${p.person_id}/`);
  await expect(page.locator("main")).toContainText("resolve occupation value 999");
  await expect(page.locator("main")).toContainText("Review Box 127 and the original Army card");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");
});

test("Batch 424 keeps identifier non-hits and name-only candidates out of public claims", async ({ page }) => {
  for (const [id, name, identityStatus, researchStatus, evidence] of [
    ["8d7b6513-1090-5798-9ba8-917be5d007d9", "Phillip H Clark", "unresolved", "requires_archival_review", "no exact-name Phillip H Clark row"],
    ["43402ffe-ace2-524d-863b-8adea6e98a37", "Randall E Clark", "ambiguous", "needs_identity_review", "sole exact-name Randall E Clark Army row"],
    ["fec61968-d846-54ea-960a-5214a12cca6e", "Richard N Clark Jr.", "unresolved", "requires_archival_review", "no exact-name-and-suffix Richard N Clark Jr. row"],
    ["01ea3571-0349-5c25-ac26-2053f333beca", "Robert G Clark", "unresolved", "requires_archival_review", "Thirty exact-name Robert G Clark Army rows carry other identifiers"],
    ["69f0e97c-4ba4-5c98-a55c-5ed87b25a883", "Sherman W Clark", "ambiguous", "needs_identity_review", "one exact-name Sherman W Clark row"],
    ["fe2954af-6122-5eea-836c-14c9a6179738", "Sidney E Clark", "ambiguous", "needs_identity_review", "two exact-name Sidney E Clark rows"],
  ]) {
    const p = profile(String(id));
    expect(p).toMatchObject({
      display_name: name,
      identity_status: identityStatus,
      research_status: researchStatus,
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
    });
    expect(p.claims).toEqual([]);
    expect(p.other_pre_oss_affiliations).toEqual([]);

    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: String(name), exact: true })).toBeVisible();
    await expect(page.locator("main")).toContainText(String(evidence));
    await expect(page.locator("main")).toContainText("Review Box 127");
    await expect(page.locator("main")).not.toContainText(/\b\d{8}\b/);
  }
});

test("Batch 424 preserves page 83, Box 127 and exact-name search", async ({ page }) => {
  const expected = [
    ["8d7b6513-1090-5798-9ba8-917be5d007d9", "Phillip H Clark", "3412247e-46b0-5b0b-b639-cbd79868e41f"],
    ["43402ffe-ace2-524d-863b-8adea6e98a37", "Randall E Clark", "bff6764a-6887-5822-a8a8-d88750bd4f56"],
    ["2e0e902e-a559-5fe2-bd37-7babfa5aabde", "Richard E Clark", "bc958133-b675-531d-a91c-7a28a9711d85"],
    ["fec61968-d846-54ea-960a-5214a12cca6e", "Richard N Clark Jr.", "5ca23dae-80b9-5436-8752-60d5244efa77"],
    ["01ea3571-0349-5c25-ac26-2053f333beca", "Robert G Clark", "24363638-a5e9-57cf-8ac4-5e58efb77781"],
    ["5bb7af15-9e32-5a5e-851b-7946837107ea", "Roger A Clark Jr.", "2dc74065-1220-51c9-bebe-545dca3bbbd1"],
    ["b818c5b2-95ae-5ce7-b871-6197d800a2e4", "Russell W Clark", "aea20add-5e8e-5eb7-9150-9d0506f18e58"],
    ["3e156d88-65fd-58a1-ad6e-b45a9f61cdec", "Samuel E Clark", "eda6e52c-e437-5c3e-b2bd-50e20121f682"],
    ["69f0e97c-4ba4-5c98-a55c-5ed87b25a883", "Sherman W Clark", "cd952cc4-b158-5310-94d5-cc1c228ca460"],
    ["fe2954af-6122-5eea-836c-14c9a6179738", "Sidney E Clark", "306079e6-e411-52d8-88e8-94c309d934b9"],
  ];

  for (const [id, name, sourceRecordId] of expected) {
    const p = profile(id);
    expect(p.source_records[0]).toMatchObject({
      source_record_id: sourceRecordId,
      pdf_page: 83,
      box: "127",
      archive_location: "230/86/28/07",
    });

    await page.goto(`./people/?q=${encodeURIComponent(name)}`);
    await expect(page.getByRole("link", { name, exact: true })).toBeVisible();
  }
});
