import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page433-smith-review_batch-887_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["f7650062-cc87-55c6-8806-9b808094b76f", "Dorothy M Smith", "721"],
  ["5cfc6c51-8710-5720-aa75-d68da9ba40ee", "Edith B Smith", "721"],
  ["6f9ab594-677c-5319-8ad6-20653243b7d7", "Edith B Smith", "722"],
  ["6554125d-3444-5a7b-ae69-128c37f8472e", "Edmund S Smith", "721"],
  ["7e3e17ac-4cb3-5d30-b2c3-6b407eeb4a0e", "Edward G Smith", "721"],
  ["b2a55b01-d71a-58d0-b04e-42b607a913ff", "Edward R Smith", "721"],
  ["4d573095-39d5-5ffc-bb00-8f73fdbe167e", "Edward R Smith", "721"],
  ["d1c26bb7-9468-546e-9496-cfb2a75d1908", "Edward R Smith", "721"],
  ["ec3aa12b-772d-5d22-b7dd-7f5f75a88115", "Edward B Smith", "721"],
  ["fd623f24-dcf1-5e20-a2bf-58dd8df18364", "Elizabeth Smith", "722"],
  ["b4d89309-5ac0-5eff-a76e-257d2fdff1f1", "Elizabeth H Smith", "722"],
  ["9af7e723-9d34-5c69-927f-83a1b2e44836", "Elmer E Smith", "722"],
  ["79e102b2-0e13-57e2-962a-92357bc1a4c8", "Ethel F Smith", "722"],
  ["eb7e8a8e-4a73-5409-a66b-5fbc38667ccd", "Eugene H Smith", "722"],
  ["8b64d546-6df9-5ec1-8ab0-d79520c4dfc6", "Everett H Smith", "722"],
  ["c9401858-0c70-526d-9020-4737c946a60c", "Everett H Smith", "722"],
  ["52c59637-abb4-5fc1-8096-e46e791b9e28", "F T Smith", "722"],
  ["932b1900-68fe-505c-810d-405b3c0b4f1f", "Florence M Smith", "722"],
  ["296f8c8b-7612-5eb7-b97c-265b94685692", "Foy E Smith", "722"],
  ["80a0018f-c782-55c9-9b3b-b847589269f1", "Frank R Smith", "722"],
  ["28a4a74d-3fdd-5429-b883-00f8a6c7fbc4", "Fulton E Smith", "722"],
  ["e720d386-b20d-5b3b-9306-e9d970d3e024", "Glennard L Smith", "722"],
  ["5dc1c31e-2baf-5531-b8bb-c1dea222a2b8", "Gordon M Smith", "722"],
] as const;

test("Batch 887 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 887 publishes five qualified occupations without inventing employers", async ({ page }) => {
  const checks = [
    ["ec3aa12b-772d-5d22-b7dd-7f5f75a88115", "high confidence", "Bookkeepers and cashiers, except bank cashiers"],
    ["4d573095-39d5-5ffc-bb00-8f73fdbe167e", "probable", "Foremen, n.e.c."],
    ["eb7e8a8e-4a73-5409-a66b-5fbc38667ccd", "high confidence", "Occupations in building of aircraft, n.e.c."],
    ["8b64d546-6df9-5ec1-8ab0-d79520c4dfc6", "high confidence", "Occupations in manufacture of automobiles, n.e.c."],
    ["e720d386-b20d-5b3b-9306-e9d970d3e024", "high confidence", "Salesmen and sales agents, except to consumers"],
  ] as const;
  for (const [id, identity, occupation] of checks) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Identity status" + identity);
    await expect(main).toContainText(occupation);
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 887 discloses the qualified leading-zero identity crosswalk", async ({ page }) => {
  await page.goto("./people/4d573095-39d5-5ffc-bb00-8f73fdbe167e/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("leading zero");
  await expect(main).toContainText("Foremen, n.e.c.");
  await expect(main).not.toContainText("confirmed identity");
});

test("Batch 887 preserves both Army identity conflicts without transferring occupations", async ({ page }) => {
  await page.goto("./people/7e3e17ac-4cb3-5d30-b2c3-6b407eeb4a0e/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("different person");
  await expect(main).not.toContainText("civilian occupation code");

  await page.goto("./people/c9401858-0c70-526d-9020-4737c946a60c/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("different given name");
  await expect(main).not.toContainText("Foresters");
});

test("Batch 887 keeps repeated Smith rows distinct", async ({ request }) => {
  for (const ids of [
    ["5cfc6c51-8710-5720-aa75-d68da9ba40ee", "6f9ab594-677c-5319-8ad6-20653243b7d7"],
    ["b2a55b01-d71a-58d0-b04e-42b607a913ff", "4d573095-39d5-5ffc-bb00-8f73fdbe167e", "d1c26bb7-9468-546e-9496-cfb2a75d1908"],
    ["8b64d546-6df9-5ec1-8ab0-d79520c4dfc6", "c9401858-0c70-526d-9020-4737c946a60c"],
  ]) {
    for (const id of ids) {
      const response = await request.get("./people/" + id + "/");
      expect(response.ok()).toBeTruthy();
    }
    expect(new Set(ids).size).toBe(ids.length);
  }
});

test("Batch 887 cites the official VA identity corroboration for Glennard L Smith", async ({ page }) => {
  await page.goto("./people/e720d386-b20d-5b3b-9306-e9d970d3e024/");
  const main = page.locator("main");
  await expect(main).toContainText("Department of Veterans Affairs");
  await expect(main).toContainText("Glennard L Smith's memorial page");
  await expect(main.getByRole("link", { name: "Glennard L Smith's memorial page" })).toHaveAttribute(
    "href",
    "https://www.vlm.cem.va.gov/GLENNARDLSMITH/11362C2",
  );
});

test("Batch 887 evidence inputs exclude private identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 887 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 588,
    research_attempted_people: 13_362,
    verified_affiliation_people: 964,
    verified_employer_people: 435,
    archival_review_assessed_people: 11_830,
    published_claims: 8_085,
    public_sources: 5_460,
  });
});
