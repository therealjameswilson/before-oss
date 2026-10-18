import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page434-smith-review_batch-888_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["31e56a99-0f8e-5a98-9783-7529045aab49", "Harley E Smith", "722"],
  ["566ad5ed-6abf-5b6e-86f6-8369572238dc", "Harrison V Smith", "722"],
  ["273573e1-c101-5c9a-9875-8a6ea0b04f2d", "Harry B Smith", "722"],
  ["34491082-cb72-5913-b231-d54254f5f77c", "Harry P Smith", "722"],
  ["faff1940-6327-5fd6-8a46-65ae7a72063a", "Helen E Smith", "722"],
  ["db68bc7e-d2ea-5b91-abba-5da2750ff4dd", "Helen L Smith", "722"],
  ["fe20f51f-9fe0-5667-bbbb-bbc4f0194daa", "Helen A Smith", "722"],
  ["922462ca-bb98-5462-bc47-c40728d8ec7c", "Henry G Smith", "722"],
  ["e4d54178-c09f-5f9a-8f21-8fca9329ab4c", "Henry N Smith", "722"],
  ["0953ee05-4a3a-5bab-81f3-b39e494595b7", "Henry E Smith", "722"],
  ["e1f9022b-3eef-54ed-859a-5c2fbe03878d", "Horace E Smith", "722"],
  ["9a002395-4e68-527a-b465-6a825b9e7784", "Horatio B Smith", "722"],
  ["ef7f9746-be90-564e-b2d1-d4dc57cfbf99", "Howard E Smith", "723"],
  ["9305644e-88f3-556e-8f26-d32d2bc666e3", "Howard E Smith", "723"],
  ["b09f8cb5-dd40-5503-bd3a-d9ce91b2ef9b", "Howard L Smith", "723"],
  ["76032d05-f10d-5c8f-91dc-dbcd61a6a413", "J B Smith", "723"],
  ["a8f0b92a-a130-5abb-8479-431ce6d9166b", "Jack C Smith", "723"],
  ["d42bdf5e-167f-5bbd-806a-f210c2fbf227", "Jacqueline H Smith", "723"],
  ["00b299d4-41a9-55c9-ab00-bf1e461641ec", "James J Smith", "723"],
  ["bdf57ce6-c23f-562a-bbc5-05111914e116", "James R Smith", "723"],
  ["4479d86b-9fc9-5d99-84b1-07765318f69a", "James B Smith", "723"],
  ["58c88009-7142-59c3-b0f7-a50e0a5684ac", "James G Smith", "723"],
  ["d51f8577-0fec-5b7f-a735-15188f3f6418", "Jeanne M Smith", "723"],
] as const;

test("Batch 888 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto("./people/" + id + "/");
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

test("Batch 888 publishes five qualified occupations without inventing employers", async ({ page }) => {
  const checks = [
    ["273573e1-c101-5c9a-9875-8a6ea0b04f2d", "Miscellaneous occupations, n. e. c."],
    ["e4d54178-c09f-5f9a-8f21-8fca9329ab4c", "Financial institution clerks, n. e. c."],
    ["ef7f9746-be90-564e-b2d1-d4dc57cfbf99", "Farm hands, general farms"],
    ["9305644e-88f3-556e-8f26-d32d2bc666e3", "Decorators and window dressers"],
    ["a8f0b92a-a130-5abb-8479-431ce6d9166b", "Occupations in production of miscellaneous petroleum and coal products"],
  ] as const;
  for (const [id, occupation] of checks) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(occupation);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 888 does not turn a petroleum occupation into an oil-company employer", async ({ page }) => {
  await page.goto("./people/a8f0b92a-a130-5abb-8479-431ce6d9166b/");
  const main = page.locator("main");
  await expect(main).toContainText(
    "Occupations in production of miscellaneous petroleum and coal products",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./oil-companies/");
  await expect(page.locator("main")).not.toContainText("Jack C Smith");
});

test("Batch 888 leaves two undefined Army occupation values uninterpreted", async ({ page }) => {
  for (const id of [
    "4479d86b-9fc9-5d99-84b1-07765318f69a",
    "58c88009-7142-59c3-b0f7-a50e0a5684ac",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("not defined");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(main).not.toContainText("Miscellaneous occupations, n. e. c.");
  }
});

test("Batch 888 keeps both Howard E Smith rows distinct", async ({ request }) => {
  const ids = [
    "ef7f9746-be90-564e-b2d1-d4dc57cfbf99",
    "9305644e-88f3-556e-8f26-d32d2bc666e3",
  ];
  for (const id of ids) {
    const response = await request.get("./people/" + id + "/");
    expect(response.ok()).toBeTruthy();
  }
  expect(new Set(ids).size).toBe(ids.length);
});

test("Batch 888 evidence inputs exclude private identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 888 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 589,
    research_attempted_people: 13_385,
    verified_affiliation_people: 964,
    verified_employer_people: 435,
    archival_review_assessed_people: 11_853,
    published_claims: 8_097,
    public_sources: 5_464,
  });
});
