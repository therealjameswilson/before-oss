import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page441-sperry-to-spiro-review_batch-902_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["989dc0b4-8775-571a-bcbf-ef35253a6ad7", "Ann Sperry"],
  ["2e82ba9e-45c5-5e8c-88e8-45461da6c26b", "Anne Sperry"],
  ["7a69f633-b44e-577d-a8dd-69853acff3ab", "Edith Sperry"],
  ["8a5c5fc6-c42d-59c1-ae8f-1b4eb4016262", "Gunther J Speyer"],
  ["a38189f4-0af5-5945-b4b0-ced968869fd4", "Vincent H Spezia"],
  ["23918e3b-eea4-5a2d-beb2-ed3bc5c5808e", "Astor R Spezzano"],
  ["82530ee1-c03f-5692-a8a3-0ca9e4942d06", "John B Spidell"],
  ["4967f3ba-9acd-51ad-bbd7-c4c90dc5835e", "Henry W Spiegel"],
  ["8d32f19f-759e-57bd-9b72-edc31b5ea36b", "Irving Spiegel"],
  ["352972f9-10bd-5401-814f-9e109af2fc0a", "Nathan Spiegel"],
  ["d37c5b8f-e59c-597e-8960-80b87c34976b", "Joe G Spiegler"],
  ["791a77b5-e77b-5ebb-bb1e-6c3500d3911f", "Alan G Spielman"],
  ["7c99d61f-bf69-5ccf-a9a3-df06278133c9", "Alan G Spielman"],
  ["56a06a5c-eb38-583f-a5d3-97ef0b392064", "Francis E Spiezer"],
  ["8a932868-bb4a-5bfc-85be-b77ef69871ed", "James M Spigner"],
  ["75b29c03-ed04-579d-97f3-fdf5c8972bdd", "Isaac P Spike"],
  ["cfaa40c5-45d8-5f53-941a-7a9353f29178", "David H Spiller"],
  ["7e1b875f-7c61-540f-b430-907565ef6329", "Frank W Spiller"],
  ["a415fc27-60e9-5602-bbdd-df33b8b47b26", "Saverio Spinelli"],
  ["b11c3a96-c099-5b37-a4a5-9345e08735d4", "Veniero Spinelli"],
  ["75827460-c5df-5427-ae00-ad88babe8aca", "Edward Spingarn"],
  ["284c71df-f606-5ce2-83ec-251d33730f53", "Merle J Spirek"],
  ["c5c624f4-500f-5e4c-96a2-703c98460a04", "Grace M Spiro"],
] as const;

test("Batch 902 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 902 Army bridges stay qualified and use the visually checked labels", async ({ page }) => {
  const checks = [
    ["8a5c5fc6-c42d-59c1-ae8f-1b4eb4016262", "Salespersons"],
    ["82530ee1-c03f-5692-a8a3-0ca9e4942d06", "Inspectors, not elsewhere classified"],
    ["8d32f19f-759e-57bd-9b72-edc31b5ea36b", "Construction occupations"],
    ["56a06a5c-eb38-583f-a5d3-97ef0b392064", "Student; institution not recorded"],
    ["75b29c03-ed04-579d-97f3-fdf5c8972bdd", "Routemen"],
    ["a415fc27-60e9-5602-bbdd-df33b8b47b26", "Brick and stone masons"],
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

test("Henry Spiegel publishes Duquesne separately from the Army occupation code", async ({ page }) => {
  await page.goto("./people/4967f3ba-9acd-51ad-bbd7-c4c90dc5835e/");
  const main = page.locator("main");
  await expect(main).toContainText("Henry William Spiegel");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Duquesne University",
  );
  await expect(main).toContainText("1939");
  await expect(main).toContainText("College presidents, professors, and instructors");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
});

test("Edward Spingarn separates Trinity employment from Signal Corps assignment", async ({ page }) => {
  await page.goto("./people/75827460-c5df-5427-ae00-ad88babe8aca/");
  const main = page.locator("main");
  await expect(main).toContainText("Edward David Woodberry Spingarn");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Trinity College",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "U.S. Army Signal Corps",
  );
  await expect(main).toContainText("explicit immediate");
  await expect(main).not.toContainText("Born on October 22, 1944");
});

test("Veniero Spinelli keeps FIAT as earlier employment and the Army chronology qualified", async ({ page }) => {
  await page.goto("./people/b11c3a96-c099-5b37-a4a5-9345e08735d4/");
  const main = page.locator("main");
  await expect(main).toContainText("FIAT");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("same-name Alan Spielman rows remain separate", async ({ page }) => {
  for (const id of [
    "791a77b5-e77b-5ebb-bb1e-6c3500d3911f",
    "7c99d61f-bf69-5ccf-a9a3-df06278133c9",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("identity review");
    await expect(main).toContainText("Two separately printed Alan G Spielman rows");
    await expect(main).not.toContainText("same-name:alan-g-spielman-page441");
  }
});

test("Grace Spiro boundary duplicate stays in identity review", async ({ page }) => {
  await page.goto("./people/c5c624f4-500f-5e4c-96a2-703c98460a04/");
  const main = page.locator("main");
  await expect(main).toContainText("identity review");
  await expect(main).toContainText("second separately printed Grace M Spiro row");
  await expect(main).not.toContainText("same-name:grace-m-spiro-page441");
});

test("Joe Spiegler conflict does not transfer the disputed occupation", async ({ page }) => {
  await page.goto("./people/d37c5b8f-e59c-597e-8960-80b87c34976b/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("separately printed Joe G Speigler row");
  await expect(main).not.toContainText("Clerks, general office");
  await expect(main).not.toContainText("shared-identifier:joe-g-spiegler-speigler-pages440-441");
});

test("Batch 902 evidence and public projection exclude credential fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("same-name:alan-g-spielman-page441");
  expect(people).not.toContain("same-name:grace-m-spiro-page441");
});

test("Batch 902 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 606,
    research_attempted_people: 13_702,
    verified_affiliation_people: 983,
    verified_employer_people: 444,
    archival_review_assessed_people: 12_173,
    published_claims: 8_338,
    public_sources: 5_582,
  });
});
