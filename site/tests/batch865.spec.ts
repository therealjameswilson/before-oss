import { expect, test } from "@playwright/test";

const profiles = [
  ["b126aba8-d1b6-53b3-927f-e620d2f09df8", "Jerome W Shay"],
  ["9fc0ed34-cad9-5536-a1a5-d2cc5fdbe7dc", "Helen M Shea"],
  ["bffcadd8-d9cf-5847-84a1-5558e1a3aa27", "James O Shea"],
  ["0975693b-eb7f-5e74-a459-1c543199ac05", "John J Shea"],
  ["9aa6c4c5-8bb4-553f-954f-8e33928646dd", "Joseph C Shea"],
  ["8fdd2d77-ce04-5296-96bb-cdfd37de6fc4", "Michael J Shea"],
  ["ce22e834-859f-5f00-b079-7e795a772340", "Robert D Shea"],
  ["8cc696dd-e7ef-597a-9ef5-1fc12befeac0", "William L Shea"],
  ["cf4835bd-c8d9-57f5-ade9-32eda79d9f35", "Germaine A Sheahan"],
  ["8a07b7a9-b2e5-5ea0-bc47-021df641535e", "Charles W Shearer"],
  ["50254e02-e191-55d1-b558-553e55a9716d", "Clyde Shearer"],
  ["318d27a5-75cd-52c9-9ce7-5c58176b3b01", "Clyde Shearer"],
  ["b30e376c-848b-5d18-9d2a-a2065457a5b7", "Douglas G Shearer"],
  ["2f09ffb4-a915-5a30-8092-14ec955aec10", "Douglas G Shearer"],
  ["2aa4c38c-db65-52e0-ac0b-2d252c87e82e", "Rudolph C Shearer"],
  ["517901d2-721a-5c65-b6ba-a23ac8a39fe8", "Roslyn T Shearin"],
  ["9c0015a9-da44-5c6e-8049-9d38f2876df4", "William H Shedden"],
  ["6a2ff1da-e282-5f7d-913d-742c729d33f3", "Francis C Sheehan"],
  ["f211e533-fae5-57c9-bcad-c090845c6a71", "Morgan C Sheehan"],
  ["834aa92c-ef51-5b6f-b636-c42856b2b655", "Stanley J Sheehan"],
  ["9c6f0fd3-9391-5878-aa04-c371b1feb307", "Thomas C Sheehan"],
  ["fe8624f4-3e58-5ce2-8416-0299238a456f", "Nellie M Sheehy"],
] as const;

test("Batch 865 publishes all 22 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText("requires archival review");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("John Shea publishes only the accepted identity bridge", async ({ page }) => {
  await page.goto("./people/0975693b-eb7f-5e74-a459-1c543199ac05/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("official Army bulk record");
  await expect(main).toContainText("omits the indexed middle initial");
  await expect(main).toContainText("neither a named employer nor an Army-to-OSS chronology");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("bulk record ordinal 403257; protected identifier withheld");
});

test("Charles Shearer keeps both immutable source rows on one supported entity", async ({ page }) => {
  await page.goto("./people/8a07b7a9-b2e5-5ea0-bc47-021df641535e/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("two printed Charles W. Shearer rows");
  await expect(main).toContainText("Both immutable source rows remain visible");
  await expect(main.locator("a[href$='#page=422']")).toHaveCount(2);
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("same-name Clyde and Douglas Shearer records remain separate", async ({ page }) => {
  for (const id of [
    "50254e02-e191-55d1-b558-553e55a9716d",
    "318d27a5-75cd-52c9-9ce7-5c58176b3b01",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("Compare both Clyde Shearer files");
  }

  for (const id of [
    "b30e376c-848b-5d18-9d2a-a2065457a5b7",
    "2f09ffb4-a915-5a30-8092-14ec955aec10",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("Compare both Douglas G. Shearer files");
  }
});

test("incompatible and unbridged candidates stay qualified", async ({ page }) => {
  await page.goto("./people/8cc696dd-e7ef-597a-9ef5-1fc12befeac0/");
  let main = page.locator("main");
  await expect(main).toContainText("branch and rank do not match the indexed Ensign");
  await expect(main).toContainText("Review Box 701 and Navy officer records");

  await page.goto("./people/9c6f0fd3-9391-5878-aa04-c371b1feb307/");
  main = page.locator("main");
  await expect(main).toContainText("does not carry the indexed protected identifier");
  await expect(main).toContainText("before accepting or rejecting");
});

test("Batch 865 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 578,
    research_attempted_people: 12_862,
    verified_affiliation_people: 933,
    verified_employer_people: 423,
    archival_review_assessed_people: 11_329,
    published_claims: 7_766,
    public_sources: 5_305,
  });
});
