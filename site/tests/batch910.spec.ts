import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page445-stavanja-to-steele-review_batch-910_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["9f532a3c-ad5e-5bd9-989e-17c458c7f159", "Lewis C Stavanja"],
  ["e7408420-ea7a-526f-9a15-b1360f3852b8", "Joseph W Staves"],
  ["bec8b5a5-95fb-506a-8be4-b2a3dcbc8736", "Aristides Stavrakis"],
  ["a80b497b-3554-5791-952d-d45ccb1194a3", "Lefterios S Stavriancos"],
  ["afea3b6d-4ccc-5a4a-8a1f-f14efe01912e", "Theharis S Stavrides"],
  ["9ad96232-d988-5165-9cb7-df87ccafdf5e", "John M Stavrou"],
  ["81a909c9-4856-5df4-bad5-60b916eda144", "Wyman Steadman"],
  ["8563efb4-48c2-5e28-8661-3bf619d35000", "Charles B Stearns"],
  ["352416a9-81bf-555c-99f4-48d063042058", "Constance D Stearns"],
  ["fad0e215-f4c5-5b07-8abe-18d84aa91f66", "Edward B Stearns"],
  ["48445b29-9b92-5ab0-a034-d0099ec4f918", "Norah D Stearns"],
  ["d21ce953-4e05-5b6b-954a-7dcbbb211c73", "Parks H Stearns"],
  ["07d6f44a-733a-5427-bc36-856482abea1a", "Paul E Stearns"],
  ["41f3ef20-1155-55bd-885e-8c905a59b321", "Philip O Stearns"],
  ["2442260d-c2c5-59a4-b829-3deb110ab7d4", "Rose H Stearns"],
  ["3d6244c2-cdcb-531f-a2bd-dcaf95a8573d", "Homer A Stebbins"],
  ["37d2c848-d9ef-59b6-a598-159b0bf36e4e", "Michael L Steck"],
  ["3fb4646c-4575-5a26-b08d-746cbf63709e", "Ernest H Steed"],
  ["0ceeec2b-94ad-5c92-8702-db7af3f769dd", "James R Steed"],
  ["e869ed0f-aeff-58c7-a423-85fc227136bc", "Francis J Steegmuller"],
  ["76fc5905-59a0-595d-bea9-495e3dfb0684", "Charles C Steele"],
  ["45c8a2bb-a4c9-5dfc-8933-3747bba86ae2", "Daniel H Steele"],
  ["6cae361e-3498-5bae-84d8-170ef829e014", "Francis R Steele"],
] as const;

test("Batch 910 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).not.toContainText("not started");
    await expect(main).not.toContainText("in progress");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Lewis C Stavanja separates Army pathway from documented civilian employment", async ({ page }) => {
  await page.goto("./people/9f532a3c-ad5e-5bd9-989e-17c458c7f159/");
  const main = page.locator("main");
  await expect(main).toContainText("White Motor");
  await expect(main).toContainText("rear-axle assembly line");
  await expect(main).toContainText("immediate pre-OSS pathway was active service in the U.S. Army");
  await expect(main).toContainText("does not explicitly call it his last civilian job");
});

test("qualified variant profiles stay visibly qualified", async ({ page }) => {
  await page.goto("./people/a80b497b-3554-5791-952d-d45ccb1194a3/");
  let main = page.locator("main");
  await expect(main).toContainText("Leften Stavros Stavrianos");
  await expect(main).toContainText("Smith College");
  await expect(main).toContainText("probable match");

  await page.goto("./people/48445b29-9b92-5ab0-a034-d0099ec4f918/");
  main = page.locator("main");
  await expect(main).toContainText("Norah Dowell Stearns");
  await expect(main).toContainText("U.S. Geological Survey");
  await expect(main).toContainText("not shown to be the immediate pre-OSS affiliation");
});

test("student, occupation, and employer categories remain distinct", async ({ page }) => {
  await page.goto("./people/41f3ef20-1155-55bd-885e-8c905a59b321/");
  let main = page.locator("main");
  await expect(main).toContainText("Princeton University");
  await expect(main).toContainText("not classified as his employer");

  await page.goto("./people/9ad96232-d988-5165-9cb7-df87ccafdf5e/");
  main = page.locator("main");
  await expect(main).toContainText("civil engineer");
  await expect(main).toContainText("no employer is identified");

  await page.goto("./people/e869ed0f-aeff-58c7-a423-85fc227136bc/");
  main = page.locator("main");
  await expect(main).toContainText("writer, novelist and biographer");
  await expect(main).toContainText("do not identify a named employer");
});

test("Ernest H Steed shared-identifier candidate remains private and conflicting", async ({ page }) => {
  await page.goto("./people/3fb4646c-4575-5a26-b08d-746cbf63709e/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Ernest H. Streed");
  await expect(main.locator("section[aria-labelledby='evidence']")).toHaveCount(0);
  await expect(main).not.toContainText("Farm hands");
});

test("Batch 910 evidence and public projection exclude credentials and protected identifiers", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toContain("38071515");
  expect(people).not.toContain("candidate-ernest-h-steed-army-b910");
});

test("Batch 910 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 613,
    research_attempted_people: 13_879,
    verified_affiliation_people: 994,
    verified_employer_people: 448,
    archival_review_assessed_people: 12_352,
    published_claims: 8_483,
    public_sources: 5_661,
  });
});
