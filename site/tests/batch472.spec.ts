import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 472 preserves the page 93 cohort, Box boundary, and masked identifiers", () => {
  const expected = [
    ["64de9625-5a61-5ecd-ade5-e0937f3c1f23", "Alceste G Cornaro", "17b96c3e-3e64-59b6-a491-543ab913c9f6", null, "144"],
    ["2cd574bb-443d-5564-998a-74b407f7de8d", "Marion J Corne", "9cbbdb54-90e2-56ed-af2a-be8bc3418d60", "••••5492", "144"],
    ["e9393991-f8df-5cdd-b3d3-ebecfe97b059", "Floyd Cornelison", "070b69d5-30bf-5629-913a-39671df7ea98", "••••0704", "144"],
    ["5feaf943-eb7c-5ba2-97c3-179835f207cc", "Anthony Cornell", "c1a6ee45-44be-53b4-9da5-546d439a7e8d", null, "145"],
    ["16160757-5094-5425-9d3c-d25db8dca3bc", "Florence Cornell", "5bceacb6-78b9-5213-a5ad-5fee7e0b5b66", null, "145"],
    ["add0d4e3-e23c-5f07-b1e9-af0150087ab6", "James H Cornell Jr.", "3d7b90f4-1d7c-53be-945f-84b103ab8256", null, "145"],
    ["dfd1e1a2-67c0-5573-8217-0acdffbdacfb", "Keith W Cornell", "b17ef0a1-c8c6-5846-8154-cd9dc3fe1112", null, "145"],
    ["61e1fee6-96c8-5307-82de-7ccc20f6ba44", "Patricia M Cornell", "aad429ff-94a5-5489-b336-4b444991efd0", null, "145"],
    ["2b198a70-e538-591e-90f4-b08793aaaf68", "Pierre F Cornell-D'Ech", "ea5eb247-c74a-5fda-8b91-eba5bbcfaf71", null, "145"],
    ["50f5b84d-5c15-549e-8708-b67aa5f0d85f", "Thelma Cornette", "7cce50bc-2b10-569d-af88-c61acd9605a0", null, "145"],
  ];

  for (const [id, name, sourceRecordId, serial, box] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        rank_as_indexed: null,
        serial_masked: serial,
        notes_as_indexed: null,
        box,
        archive_location: "230/86/29/02",
        pdf_page: 93,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 472 qualifies Cornaro's CCC pathway and occupation without inventing an employer", async ({ page }) => {
  const alceste = profile("64de9625-5a61-5ecd-ade5-e0937f3c1f23");
  expect(alceste).toMatchObject({
    display_name: "Alceste G Cornaro",
    identity_status: "high_confidence",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(alceste.immediate_pre_oss_affiliations).toEqual([]);
  expect(alceste.last_civilian_pre_service).toEqual([]);
  expect(alceste.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      canonical_organization: "Civilian Conservation Corps",
      relationship_type: "government_assignment",
      temporal_basis: "documented_prewar",
      claim_confidence: "medium",
    }),
  );
  expect(alceste.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Machinists",
      relationship_type: "unknown",
      end_date: "1942-01-29",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/64de9625-5a61-5ecd-ade5-e0937f3c1f23/");
  await expect(page.getByRole("heading", { name: "Alceste G Cornaro", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Civilian Conservation Corps");
  await expect(page.locator("main")).toContainText("Machinists");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 472 confirms Cornelison but publishes only the bounded farm occupation", async ({ page }) => {
  const floyd = profile("e9393991-f8df-5cdd-b3d3-ebecfe97b059");
  expect(floyd).toMatchObject({
    display_name: "Floyd Cornelison",
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
  expect(floyd.immediate_pre_oss_affiliations).toEqual([]);
  expect(floyd.last_civilian_pre_service).toEqual([]);
  expect(floyd.other_pre_oss_affiliations).toContainEqual(
    expect.objectContaining({
      organization_id: null,
      occupation: "Farm hands, general farms",
      end_date: "1942-04-15",
      temporal_basis: "temporal_relation_uncertain",
      claim_confidence: "medium",
    }),
  );

  await page.goto("./people/e9393991-f8df-5cdd-b3d3-ebecfe97b059/");
  await expect(page.getByRole("heading", { name: "Floyd Cornelison", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Farm hands, general farms");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 472 withholds all unbridged Cornell and Cornette candidate facts", () => {
  for (const id of [
    "2cd574bb-443d-5564-998a-74b407f7de8d",
    "5feaf943-eb7c-5ba2-97c3-179835f207cc",
    "16160757-5094-5425-9d3c-d25db8dca3bc",
    "61e1fee6-96c8-5307-82de-7ccc20f6ba44",
    "2b198a70-e538-591e-90f4-b08793aaaf68",
    "50f5b84d-5c15-549e-8708-b67aa5f0d85f",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }

  for (const id of [
    "add0d4e3-e23c-5f07-b1e9-af0150087ab6",
    "dfd1e1a2-67c0-5573-8217-0acdffbdacfb",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "ambiguous",
      personnel_category: "unknown_or_indeterminate",
      commissioned_officer: null,
      research_status: "requires_archival_review",
      manual_review_required: true,
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }

  expect(JSON.stringify(profile("16160757-5094-5425-9d3c-d25db8dca3bc"))).not.toContain(
    "Adams School",
  );
});
