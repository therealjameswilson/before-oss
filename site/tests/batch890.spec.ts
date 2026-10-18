import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page435-smith-review_batch-890_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["bd83eb6d-d97c-59b2-b0c0-c51c29576631", "Martha F Smith", "724"],
  ["728e98e8-9e89-5db9-854d-57f936580d61", "Martin E Smith", "724"],
  ["d5e5f1d7-0414-5332-bd37-9b07801f9499", "Martin E Smith", "724"],
  ["ad35e74a-73df-5889-afb6-f2150f871e50", "Mary R Smith", "724"],
  ["4939ea4d-129e-5551-8e8b-d68c6ebe6ace", "Matthew D Smith", "724"],
  ["94e9842e-05f1-5794-a1fb-3f2005d23840", "Mehlon B Smith", "723"],
  ["a77734f1-6e3e-5158-b5ca-8f516dbb1516", "Murray W Smith", "724"],
  ["febd24c8-c79b-599f-aa6b-375803d57247", "Myron P Smith", "724"],
  ["7baa9c4c-5aea-568a-9b41-a53a75c3c7d2", "Nelson M Smith", "724"],
  ["45f220f1-4668-5395-b0e4-f7a4921b254f", "Nicol Smith", "724"],
  ["ffae0086-139e-5d29-bf24-85031c780bc6", "Noble M Smith", "724"],
  ["a3497a60-4207-5e0e-ada3-66474f199478", "Odell E Smith", "724"],
  ["777f0705-4343-5316-8603-af7b2c0d46a1", "Paul L Smith", "724"],
  ["ad3877a2-eefc-56d7-ada5-aa504e118d35", "Philip J Smith", "724"],
  ["c9a552fd-d012-5e75-80bd-60d1db1afed3", "Phyllis C Smith", "724"],
  ["e50d433b-d3ba-5a9e-9602-87525a242502", "Quayle B Smith", "724"],
  ["669b6669-3b42-5b74-b301-9907128ca8df", "R J Smith", "724"],
  ["0e880540-d441-5101-a76f-bd26ca47b931", "Rae H Smith", "724"],
  ["cbee25e3-9a3f-5704-ab23-3ac7f554a3eb", "Ralph L Smith", "724"],
  ["7d4d1984-c08f-51b5-8a71-c462896fd1f3", "Ratio P Smith", "724"],
  ["17a18241-e381-54f4-ac90-b237d35ac192", "Regina D Smith", "724"],
  ["1595832f-f451-5a35-8c7b-a03d6550b666", "Richard G Smith", "724"],
  ["c4738870-9e3f-5a3c-b157-b93bdc6b8673", "Robert F Smith", "724"],
] as const;

test("Batch 890 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).toContainText(box);
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 890 publishes five qualified non-employer findings", async ({ page }) => {
  const checks = [
    ["728e98e8-9e89-5db9-854d-57f936580d61", "Machine shop and related occupations, n.e.c."],
    ["ffae0086-139e-5d29-bf24-85031c780bc6", "Paymasters, payroll clerks, and timekeepers"],
    ["777f0705-4343-5316-8603-af7b2c0d46a1", "Chauffeurs and drivers, bus, taxi, truck, and tractor"],
    ["ad3877a2-eefc-56d7-ada5-aa504e118d35", "recorded as a student"],
    ["cbee25e3-9a3f-5704-ab23-3ac7f554a3eb", "recorded as a student"],
  ] as const;
  for (const [id, finding] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(finding);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Noble Smith's malformed Army date remains visibly qualified", async ({ page }) => {
  await page.goto("./people/ffae0086-139e-5d29-bf24-85031c780bc6/");
  const main = page.locator("main");
  await expect(main).toContainText("date field is malformed");
  await expect(main).toContainText(/temporal relation uncertain/i);
  await expect(main).not.toContainText("1993");
});

test("Army suffixes remain documented variants without replacing indexed names", async ({ page }) => {
  const checks = [
    ["777f0705-4343-5316-8603-af7b2c0d46a1", "Paul L Smith", "Paul L Smith Jr"],
    ["ad3877a2-eefc-56d7-ada5-aa504e118d35", "Philip J Smith", "Philip J Smith Jr"],
    ["cbee25e3-9a3f-5704-ab23-3ac7f554a3eb", "Ralph L Smith", "Ralph L Smith Jr"],
  ] as const;
  for (const [id, indexed, variant] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(`Indexed form${indexed}`);
    await expect(main).toContainText(variant);
  }
});

test("both Martin E Smith rows remain separate and visibly grouped", async ({ page, request }) => {
  const ids = [
    "728e98e8-9e89-5db9-854d-57f936580d61",
    "d5e5f1d7-0414-5332-bd37-9b07801f9499",
  ];
  for (const id of ids) {
    const response = await request.get(`./people/${id}/`);
    expect(response.ok()).toBeTruthy();
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("duplicate-832d5a555240");
  }
  expect(new Set(ids).size).toBe(ids.length);
});

test("R J Smith preserves the printed note without resolving the initials", async ({ page }) => {
  await page.goto("./people/669b6669-3b42-5b74-b301-9907128ca8df/");
  const main = page.locator("main");
  await expect(main).toContainText("File sent");
  await expect(main).toContainText("unresolved");
});

test("Nicol Smith's earlier verified travel-writing result remains intact", async ({ page }) => {
  await page.goto("./people/45f220f1-4668-5395-b0e4-f7a4921b254f/");
  const main = page.locator("main");
  await expect(main).toContainText("travel writer");
  await expect(main).toContainText("self-employment");
  await expect(main).toContainText("verified employer found");
});

test("Batch 890 evidence inputs exclude protected identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 890 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 591,
    research_attempted_people: 13_430,
    verified_affiliation_people: 964,
    verified_employer_people: 435,
    archival_review_assessed_people: 11_898,
    published_claims: 8_115,
    public_sources: 5_472,
  });
});
