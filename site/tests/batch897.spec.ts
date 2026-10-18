import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page438-sonagere-to-soria-review_batch-897_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["8c8efd33-2060-5c04-87f5-09599b422571", "Henry Sonagere"],
  ["d7666c7d-28f6-5cb3-a4bb-c95eb7d63ec9", "Eddie O Sondeno"],
  ["10149fe1-e3ed-5e1c-9270-ee541143d978", "Hun Y Song"],
  ["aa915e34-3cbf-50d1-88dd-fbcdb9f9e524", "Guy S Songy"],
  ["e7d70d1f-3767-5c0e-95e8-422fb9f2838d", "Edgar H Sonnanstine"],
  ["064b5404-1961-558c-99bb-43fcd530dac5", "Edgar H Sonnanstine"],
  ["a1b9e306-7701-5be7-a5ac-ca4cfbaabb42", "R Sonnenburg"],
  ["cf853711-8d0e-57db-9b23-2b0d101d5211", "Gunnar Sonsteby"],
  ["dc35d48f-b507-5254-a731-8b07ebb1c9ef", "Yook L Soo Hoo"],
  ["e081fd1c-ceb2-5092-96c0-590540c16b05", "Louis Soos"],
  ["9abc9082-7d2d-537a-b98f-9ba6d5fa1852", "Salvatore Sorbella"],
  ["447531c8-82a3-5723-bd41-49c31491f117", "Victor S Sordan"],
  ["e3d434c4-9a4b-5f81-b011-b0a2dc92eb8a", "Abel R Sorensen"],
  ["86e51692-30de-58b0-85b0-f832b109cabf", "Daniel A Sorensen"],
  ["3f8709f2-c28c-5cd9-9c07-a7dc267b09e3", "Hobart H Sorensen"],
  ["108c39e4-b6c3-5b84-afc8-0242bbc80ccd", "Elsie M Sorenson"],
  ["c3679746-d14b-5907-8ba4-79a0be4db1ce", "Robert W Sorenson"],
  ["e933f2d3-3614-58e0-9a3c-799554549255", "Robert J Sorenson"],
  ["7f610304-9c29-5dc7-b4de-d5be0b5d443d", "Robert W Sorenson"],
  ["fdf2916f-eb18-55ba-8313-8fdeb82b628d", "Ruby E Sorenson"],
  ["d6bf9abb-5bef-5887-b188-df9930ef13e3", "Karl G Sorg"],
  ["4feea52b-18ad-589f-aff7-d2fd608a06e0", "Jack A Sorgenfrei"],
  ["31ea8aa4-b33f-5c5a-b2d4-2f3d6b75145a", "Dario Soria"],
] as const;

test("Batch 897 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("accepted Army bridges remain qualified occupations rather than employers", async ({ page }) => {
  const checks = [
    ["d7666c7d-28f6-5cb3-a4bb-c95eb7d63ec9", "Carpenters"],
    ["dc35d48f-b507-5254-a731-8b07ebb1c9ef", "Students"],
    ["9abc9082-7d2d-537a-b98f-9ba6d5fa1852", "Blacksmiths"],
    ["d6bf9abb-5bef-5887-b188-df9930ef13e3", "Actors and actresses"],
    ["4feea52b-18ad-589f-aff7-d2fd608a06e0", "Stock clerks"],
  ] as const;

  for (const [id, occupation] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("qualified lead");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Henry Sonagere separates the immediate military pathway from unnamed carpentry work", async ({ page }) => {
  await page.goto("./people/8c8efd33-2060-5c04-87f5-09599b422571/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "82nd Airborne Division",
  );
  await expect(main).toContainText("carpentry trainee");
  await expect(main).toContainText("no employer is named");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Gunnar Sonsteby preserves Norwegian employers, Milorg and SOE distinctions", async ({ page }) => {
  await page.goto("./people/cf853711-8d0e-57db-9b23-2b0d101d5211/");
  const main = page.locator("main");
  await expect(main).toContainText("Gunnar Sønsteby");
  await expect(main).toContainText("Gjensidige");
  await expect(main).toContainText("Rjukan Salpeterfabrikker");
  await expect(main).toContainText("Milorg");
  await expect(main).toContainText("British SOE");
  await expect(main).toContainText("do not use postwar Esso employment");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
});

test("Karl Sorg keeps Dartmouth student status separate from Army occupation evidence", async ({ page }) => {
  await page.goto("./people/d6bf9abb-5bef-5887-b188-df9930ef13e3/");
  const main = page.locator("main");
  await expect(main).toContainText("Dartmouth College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("Actors and actresses");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Dario Soria publishes probable, temporally qualified affiliations only", async ({ page }) => {
  await page.goto("./people/31ea8aa4-b33f-5c5a-b2d4-2f3d6b75145a/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Dario Pellegrino Soria");
  await expect(main).toContainText("Raxor Trading Company");
  await expect(main).toContainText("Voice of America");
  await expect(main).toContainText("Columbia Broadcasting System");
  await expect(main).toContainText("D'Arcy Advertising Company");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("cousin Guido Soria");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Sonnanstine and Sorensen-Sorenson conflicts remain visible without occupation transfer", async ({ page }) => {
  await page.goto("./people/064b5404-1961-558c-99bb-43fcd530dac5/");
  const edgar = page.locator("main");
  await expect(edgar).toContainText("conflicting");
  await expect(edgar).toContainText("Brown Owen L");
  await expect(edgar).not.toContainText("Molders");

  await page.goto("./people/86e51692-30de-58b0-85b0-f832b109cabf/");
  const daniel = page.locator("main");
  await expect(daniel).toContainText("conflicting");
  await expect(daniel).toContainText("Robert W Sorenson");
  await expect(daniel).toContainText("serial-conflict:[private identifier omitted]");
  await expect(daniel).not.toContainText("Upholsterers");

  await page.goto("./people/c3679746-d14b-5907-8ba4-79a0be4db1ce/");
  const robert = page.locator("main");
  await expect(robert).toContainText("conflicting");
  await expect(robert).toContainText("Daniel A Sorenson");
  await expect(robert).not.toContainText("Upholsterers");
});

test("Batch 897 evidence and public projection exclude protected identifiers and credentials", () => {
  const people = fs.readFileSync(
    new URL("../src/data/generated/people.json", import.meta.url),
    "utf8",
  );
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("31326668");
});

test("Batch 897 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 599,
    research_attempted_people: 13_588,
    verified_affiliation_people: 976,
    verified_employer_people: 438,
    archival_review_assessed_people: 12_059,
    published_claims: 8_242,
    public_sources: 5_530,
  });
});
