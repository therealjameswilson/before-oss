import { expect, test } from "@playwright/test";

const profiles = [
  ["c0c6317b-3656-517b-82b3-62ad34a1c5cd", "Anne Sirotenko"],
  ["5f8e8710-a65f-5995-a6c9-d18aa3a9f790", "Anthony Sirtaut"],
  ["0e775c55-4587-5dd5-a362-49e047ca33c3", "Fidencio Sisneros"],
  ["0bd8536c-44a5-546b-820f-b1c81e5c1dec", "Yvette Sisselman"],
  ["100a1fcb-4f57-5510-934b-b10ba3e5cd08", "Howard R Sites"],
  ["36625c0c-0f6f-5b4b-a6b0-be382ee20dcc", "Paul D Sivak"],
  ["2904cab5-61a7-5609-8e96-87e04875defa", "Morgan M Sivia"],
  ["f516c079-192d-5890-8e19-7a55c5d79b3c", "Michael W Sivy"],
  ["52834d80-7117-5ba0-acc3-9d9f2df7e71b", "Robert J Siwecki"],
  ["af6ce9fa-9a9e-5434-9c89-311b2063c29f", "William R Sizemore"],
  ["98850fd4-c5cd-5bc9-909b-2e82c89d9bf7", "Earl E Sizer"],
  ["14c6a8a6-964a-5804-8461-6a30978c3b23", "Elizabeth R Sizer"],
  ["a6471068-1e1d-5e4c-ab65-7dcdcac45f47", "Hans H Skabo"],
  ["bc6e5931-4123-5c94-8018-c43b51cf889d", "John W Skadan"],
  ["91884f4f-895f-5b0c-89b0-b9e65bb816f8", "Victor W Skala"],
  ["4b69316a-508c-5861-ba82-40c916108f83", "Youri Skarzynski"],
  ["4d0679f6-7476-53ab-81ef-39e34d80d2e7", "Emil M Skasa"],
  ["9c9ddd31-67a5-54a5-9c68-19335da6eaea", "Paul E Skeen"],
  ["22e28bdc-39d1-5f4b-8489-3b105a1e8a8e", "Richard P Skelton"],
  ["604ed04f-fca1-51ec-90c2-2977b00555bd", "Axel B Skeppstedt"],
  ["8754f632-9530-57be-9f21-2779313237c7", "Alfred A Skerpan"],
  ["b47cfb60-6b17-5005-b980-8fefd447f998", "Walter Skerpan"],
  ["fc96429f-60b5-523a-967e-12acbf57b08d", "H Skgolsvik"],
] as const;

test("Batch 881 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Batch 881 publishes Youri Skarzynski's explicit French Army pathway without calling it employment", async ({ page }) => {
  await page.goto("./people/4b69316a-508c-5861-ba82-40c916108f83/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Yuri Skarzynski");
  const immediate = main.locator("section[aria-labelledby='immediate-affiliation']");
  await expect(immediate).toContainText("French Army");
  await expect(immediate).toContainText("military assignment");
  await expect(immediate).toContainText("explicit immediate");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 881 keeps Hans Skabo's prewar Guard service distinct from an immediate OSS predecessor", async ({ page }) => {
  await page.goto("./people/a6471068-1e1d-5e4c-ab65-7dcdcac45f47/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("commissioned army officer");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Indiana National Guard");
  await expect(earlier).toContainText("military assignment");
  await expect(earlier).toContainText("documented pre-OSS");
});

test("Batch 881 publishes Alfred Skerpan's Harvard history only as student status", async ({ page }) => {
  await page.goto("./people/8754f632-9530-57be-9f21-2779313237c7/");
  const main = page.locator("main");
  await expect(main).toContainText("Alfred Andrew Skerpan");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Harvard University");
  await expect(earlier).toContainText("student");
  await expect(main).toContainText("not an employer");
});

test("Batch 881 exposes the H Skgolsvik conflict without publishing a full protected identifier", async ({ page }) => {
  await page.goto("./people/fc96429f-60b5-523a-967e-12acbf57b08d/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Both index entities remain separate");
  await expect(main).toContainText("Review Box 716 together with the adjacent Hakon A Skjolsvik file");
  const serial = main.locator("dt").filter({ hasText: /^Serial$/ })
    .locator("xpath=following-sibling::dd[1]");
  await expect(serial).toContainText("••••");
  await expect(serial).not.toHaveText(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
});

test("Batch 881 publishes the six accepted Army identity bridges", async ({ page }) => {
  for (const id of [
    "5f8e8710-a65f-5995-a6c9-d18aa3a9f790",
    "0e775c55-4587-5dd5-a362-49e047ca33c3",
    "36625c0c-0f6f-5b4b-a6b0-be382ee20dcc",
    "f516c079-192d-5890-8e19-7a55c5d79b3c",
    "9c9ddd31-67a5-54a5-9c68-19335da6eaea",
    "604ed04f-fca1-51ec-90c2-2977b00555bd",
  ]) {
    await page.goto(`./people/${id}/`);
    await expect(page.locator("main")).toContainText("Identity statushigh confidence");
  }
});

test("Batch 881 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 584,
    research_attempted_people: 13_225,
    verified_affiliation_people: 959,
    verified_employer_people: 433,
    archival_review_assessed_people: 11_692,
    published_claims: 7_982,
    public_sources: 5_413,
  });
});
