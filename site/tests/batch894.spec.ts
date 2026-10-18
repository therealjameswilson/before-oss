import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page437-smyth-to-snyder-review_batch-894_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["70ffc830-4c39-57aa-9acb-d6b30487a942", "Howard M Smyth", "726"],
  ["7a9e1465-aa07-5da7-87f7-8ead85a2a699", "Edith W Smythe", "726"],
  ["46d0bea3-2039-5f4d-80fe-6a7f327720ab", "Sarah E Smythe", "726"],
  ["23e71660-bee2-5b09-ada1-08fcb84081fa", "James F Snapp", "727"],
  ["009fc40d-571f-51d1-834f-3cf74c0eebfe", "Paul A Snearline", "727"],
  ["588e8538-2277-57fa-83ec-c593c7117126", "William K Snedecker", "727"],
  ["a07b88d3-1d00-5c82-81f5-3eeb117ca320", "Daniel T Snell", "727"],
  ["efb448dd-013b-51c2-8572-908ab3600127", "Harry D Snell", "727"],
  ["ae79fec5-d504-5791-b253-83db22d26886", "William M Snelling", "727"],
  ["ffbbc250-a298-5be6-b425-083547a2b306", "Charles C Snider", "727"],
  ["47c2c0ee-c331-58e3-a496-e78a3fd6033c", "R H Snider", "727"],
  ["fd5ad97f-872a-5629-bd4d-31971b1d49a8", "Paul C Snodgrass", "727"],
  ["52d2c58c-e260-58e4-8273-f1a613ef14bc", "Roy L Snodgrass", "727"],
  ["4a6a9e7b-838e-57a0-a381-55b376b47b6f", "Paul C Snodgress", "727"],
  ["8a4528ee-354f-50af-8161-4413b20f914f", "Davis W Snow", "727"],
  ["b32e47b5-ed21-56b4-871c-bc7372ea14da", "Harold C Snow", "727"],
  ["e3820167-e0ea-50db-a59f-6756b5570508", "Charles R Snowden", "727"],
  ["dc5f0a30-4c3f-50f2-83cf-49381bf44c4f", "Charles R Snowden", "727"],
  ["84ea25db-f77e-55db-ad7d-b373fe898f2c", "William Snower", "727"],
  ["3d9eb348-dee6-5edf-ae6c-e5257697248b", "Joseph Snoy", "727"],
  ["4c1e2c3f-ba2a-5337-becf-fea5a67c8f84", "Andrew J Snyder", "727"],
  ["98a5e40a-df4f-52fb-a468-123d29002ab1", "Arthur L Snyder", "727"],
  ["926c80b5-ab2a-54e4-8262-16d0daf34b56", "Clarke C Snyder", "727"],
] as const;

test("Batch 894 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Howard McGaw Smyth publishes UC Berkeley as a strongly bounded immediate employer", async ({ page }) => {
  await page.goto("./people/70ffc830-4c39-57aa-9acb-d6b30487a942/");
  const main = page.locator("main");
  await expect(main).toContainText("Howard McGaw Smyth");
  await expect(main).toContainText("University of California, Berkeley");
  await expect(main).toContainText("professor of modern European history");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "University of California, Berkeley",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "University of California, Berkeley",
  );
  await expect(main).toContainText("strongly date bounded");
});

test("William Snower keeps Army language training and Harvard student status distinct from employment", async ({ page }) => {
  await page.goto("./people/84ea25db-f77e-55db-ad7d-b373fe898f2c/");
  const main = page.locator("main");
  await expect(main).toContainText("William Snower Jr.");
  await expect(main).toContainText("Army Specialized Training Program Swedish Area and Language");
  await expect(main).toContainText("Harvard College");
  await expect(main).toContainText("A.B. magna cum laude in government");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Army Specialized Training Program",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Army occupation categories stay qualified and do not become employers", async ({ page }) => {
  const checks = [
    ["588e8538-2277-57fa-83ec-c593c7117126", "Architects"],
    ["52d2c58c-e260-58e4-8273-f1a613ef14bc", "mechanical treatment of metals"],
    ["98a5e40a-df4f-52fb-a468-123d29002ab1", "Attendants, recreation and amusement"],
  ] as const;
  for (const [id, occupation] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("medium");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Andrew Snyder's postwar Army record supplies identity only", async ({ page }) => {
  await page.goto("./people/4c1e2c3f-ba2a-5337-becf-fea5a67c8f84/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("post-OSS");
  await expect(main).not.toContainText("occupation code 195");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("spelling variants and same-name Snowden rows remain separate", async ({ page }) => {
  for (const id of [
    "fd5ad97f-872a-5629-bd4d-31971b1d49a8",
    "4a6a9e7b-838e-57a0-a381-55b376b47b6f",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("duplicate-7716d411e76a");
  }
  for (const id of [
    "e3820167-e0ea-50db-a59f-6756b5570508",
    "dc5f0a30-4c3f-50f2-83cf-49381bf44c4f",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("duplicate-067c391cee9a");
  }
});

test("Batch 894 evidence inputs exclude protected identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 894 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 598,
    research_attempted_people: 13_520,
    verified_affiliation_people: 968,
    verified_employer_people: 436,
    archival_review_assessed_people: 11_990,
    published_claims: 8_179,
    public_sources: 5_501,
  });
});
