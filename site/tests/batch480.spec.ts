import { expect, test } from "@playwright/test";
import fs from "node:fs";

const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
);
const profile = (id: string) =>
  people.find((person: { person_id: string }) => person.person_id === id);

test("Batch 480 preserves page 95 rows 10-19 and masks private identifiers", () => {
  const expected = [
    ["4456c938-eb83-53a7-8b34-77f2db2cb0a7", "Leonidas Coulourides", "fb1fd39b-9b22-50a4-9c14-e5adb109772e", "••••2551"],
    ["df0f6149-7a85-515f-a997-a98f954d0464", "Robert E Coulson", "e78655b7-2331-5e33-b3c8-8aab2d76e649", "••••1187"],
    ["f482707f-eba0-5d2d-a141-f7409e7e1403", "Earl W Coulter", "1120b31b-56b2-5ff8-98cd-8db2027421b2", "••••6205"],
    ["0f53899b-c294-5f53-9a7c-5c1594d00218", "Emile R Counasse", "be53a058-eb89-5fb2-8cbd-fd910543f666", "••••5215"],
    ["1bd4a801-b571-523f-8758-8d4f8f7940a7", "Eula F Council", "c9ea0b1e-dc12-51bb-a303-fa48ffe88ff3", null],
    ["b559be87-4e37-5209-a02a-eb3d00d7afd0", "Harry G Council", "ea4e3e3e-e1ca-54f9-bfc8-42a5e62f0b34", "••••8617"],
    ["92c86b9f-8cfd-50bc-aa1f-436c2383eba1", "Dennis N Countouris", "a98817b7-128a-51b5-abb5-791daac6c5af", "••••6973"],
    ["56713cc7-ed96-5abe-93b4-ef7354404df4", "Clifford Countryman", "f1aedcb4-1f75-5246-882b-e02e1a14c78b", "••••6926"],
    ["ed5c7b70-3727-5a8c-9a64-2c418abf8492", "Leonard C Counts", "8ec8bfd3-671a-53d2-b2c4-2d5ce983c666", "••••4312"],
    ["e6e3c2a5-4d11-519b-b901-ad9cd600d077", "George C Courpas", "5feeb9da-922f-5980-8b51-c586ae479812", "••••0381"],
  ];

  for (const [id, name, sourceRecordId, serial] of expected) {
    const person = profile(String(id));
    expect(person).toMatchObject({ display_name: name });
    expect(person.source_records).toContainEqual(
      expect.objectContaining({
        source_record_id: sourceRecordId,
        serial_masked: serial,
        box: "148",
        archive_location: "230/86/29/03",
        pdf_page: 95,
      }),
    );
    expect(JSON.stringify(person)).not.toMatch(
      /"serial_number"|"serial_number_raw"|"serial_number_normalized"/,
    );
  }
});

test("Batch 480 confirms three exact Army identities without inventing affiliations", () => {
  for (const id of [
    "4456c938-eb83-53a7-8b34-77f2db2cb0a7",
    "ed5c7b70-3727-5a8c-9a64-2c418abf8492",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "confirmed",
      personnel_category: "enlisted_army_personnel",
      commissioned_officer: false,
      research_status: "requires_archival_review",
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
    });
  }
  expect(profile("e6e3c2a5-4d11-519b-b901-ad9cd600d077")).toMatchObject({
    identity_status: "confirmed",
    personnel_category: "enlisted_army_personnel",
    commissioned_officer: false,
    research_status: "occupation_only_found",
  });
});

test("Batch 480 publishes two occupations without converting them into employers", async ({ page }) => {
  const expected = [
    ["92c86b9f-8cfd-50bc-aa1f-436c2383eba1", "Kitchen worker in a hotel, restaurant, railroad, steamship or similar setting, not elsewhere classified"],
    ["e6e3c2a5-4d11-519b-b901-ad9cd600d077", "Waiter, except in a private family"],
  ];
  for (const [id, occupation] of expected) {
    const person = profile(id);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toContainEqual(
      expect.objectContaining({
        occupation,
        relationship_type: "unknown",
        temporal_basis: "strongly_date_bounded",
        claim_confidence: "medium",
      }),
    );
  }

  await page.goto("./people/92c86b9f-8cfd-50bc-aa1f-436c2383eba1/");
  await expect(page.getByRole("heading", { name: "Dennis N Countouris", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("Kountouris");
  await expect(page.locator("main")).toContainText("Kitchen worker");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 480 identifies Emile Counasse as a commissioned Army officer without a pre-OSS affiliation", async ({ page }) => {
  const person = profile("0f53899b-c294-5f53-9a7c-5c1594d00218");
  expect(person).toMatchObject({
    display_name: "Emile R Counasse",
    identity_status: "high_confidence",
    personnel_category: "commissioned_army_officer",
    commissioned_officer: true,
    research_status: "requires_archival_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });

  await page.goto("./people/0f53899b-c294-5f53-9a7c-5c1594d00218/");
  await expect(page.getByRole("heading", { name: "Emile R Counasse", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("First Lieutenant Emile R. Counasse");
  await expect(page.locator("main")).toContainText("OSS Detachment 404");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 480 preserves Earl Coulter's identifier conflict without adopting the Army candidate", async ({ page }) => {
  const person = profile("f482707f-eba0-5d2d-a141-f7409e7e1403");
  expect(person).toMatchObject({
    display_name: "Earl W Coulter",
    identity_status: "conflicting",
    personnel_category: "unknown_or_indeterminate",
    research_status: "needs_identity_review",
    immediate_pre_oss_affiliations: [],
    last_civilian_pre_service: [],
    other_pre_oss_affiliations: [],
  });
  expect(person.claims).toContainEqual(
    expect.objectContaining({
      claim_type: "identity",
      claim_confidence: "conflicting",
      publication_status: "conflicting",
    }),
  );

  await page.goto("./people/f482707f-eba0-5d2d-a141-f7409e7e1403/");
  await expect(page.getByRole("heading", { name: "Earl W Coulter", exact: true })).toBeVisible();
  await expect(page.locator("main")).toContainText("different private identifier");
  await expect(page.locator("main")).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 480 leaves four unsupported identities unresolved", () => {
  for (const id of [
    "df0f6149-7a85-515f-a997-a98f954d0464",
    "1bd4a801-b571-523f-8758-8d4f8f7940a7",
    "b559be87-4e37-5209-a02a-eb3d00d7afd0",
    "56713cc7-ed96-5abe-93b4-ef7354404df4",
  ]) {
    expect(profile(id)).toMatchObject({
      identity_status: "unresolved",
      research_status: "requires_archival_review",
      manual_review_required: true,
      immediate_pre_oss_affiliations: [],
      last_civilian_pre_service: [],
      other_pre_oss_affiliations: [],
      claims: [],
    });
  }
});
