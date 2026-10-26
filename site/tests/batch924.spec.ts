import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page452-william-s-strauss-to-theophanes-g-strimenos-review_batch-924_2026-10-26.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c1d42fce-baf7-5259-978e-1360e936b29b", "William S Strauss"],
  ["e00eb3c2-d676-526a-89c2-e6829a91046a", "George Strawbridge"],
  ["dbe6304d-6bb1-5483-93b6-eb41572f0668", "Ernest H Streed"],
  ["a83e8685-38a2-598b-bc91-42598bd5232d", "Elmer E Streeter"],
  ["e46e59df-3e9d-5073-93f5-e72c7616ac24", "Elmer S Streeter"],
  ["802cbb13-1a4d-5078-a233-6fefbc226de0", "Norman E Streeter"],
  ["3ec9d787-c0ca-5d3b-9bf6-8266543a29d6", "Stephen Streeter"],
  ["2abae00d-4604-50eb-a84d-23049d23c7c0", "Thomas W Streeter"],
  ["803ea5df-1954-5848-829c-a5af19f134d2", "Robert E Streif"],
  ["873441b6-b61b-5cd4-988e-64204693367a", "Walter H Streilein"],
  ["515e65a9-5d06-5f79-b585-4a2cd23eb528", "Kathleen Streissguth"],
  ["8e39dd9b-d723-5ced-9d44-ab0d7dfd42d9", "Pierre D Streit"],
  ["543bc104-fac6-5352-84ca-e0d1a66b38e7", "J E Strick"],
  ["ebdb36f9-54a2-5972-b030-0fef7dd7b5c8", "Bessie Strickland"],
  ["684a6676-6e1a-527a-89a3-22d9f12957ed", "Irene Strickland"],
  ["c7b71ec2-a3bb-5508-acb1-3749dea49018", "Mary W Strickland"],
  ["1466bcf3-31c9-5381-9c42-223d086dd20c", "Robert E Strickland"],
  ["1cd1e7c4-8c21-5d0a-86e1-788915338430", "William C Strickland"],
  ["d8dbe549-c4b2-5dfe-9070-ab83a98b79f8", "William C Strickland"],
  ["d36a49ed-dd13-552b-9509-6477fe43872a", "Robert A Stricklin"],
  ["9e24f3ef-d1e6-5f00-9661-33583be17f01", "Robert E Strief"],
  ["526fc414-2a93-566a-9f5e-1246122f61f5", "Nicholas L Strike"],
  ["2b92e253-f5d1-5fb0-93d1-662da49b084d", "Theophanes G Strimenos"],
] as const;

test("Batch 924 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("George Strawbridge publishes Campbell Soup with a temporal qualification", async ({ page }) => {
  await page.goto("./people/e00eb3c2-d676-526a-89c2-e6829a91046a/");
  const main = page.locator("main");
  await expect(main).toContainText("Campbell Soup Company");
  await expect(main).toContainText("public relations and assistant treasurer");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("not a proven immediate OSS predecessor");
  await expect(main).toContainText("Princeton Alumni Weekly");
  await expect(main).toContainText("St. Paul's School");
});

test("five Army occupation findings remain qualified and employer-free", async ({ page }) => {
  const cases = [
    ["a83e8685-38a2-598b-bc91-42598bd5232d", "Machinists' apprentices", "1943-06-03"],
    ["802cbb13-1a4d-5078-a233-6fefbc226de0", "Chauffeurs and drivers, bus, taxi, truck, and tractor", "1945-03-20"],
    ["8e39dd9b-d723-5ced-9d44-ab0d7dfd42d9", "Students", "1943-06-03"],
    ["1cd1e7c4-8c21-5d0a-86e1-788915338430", "Stock clerks", "1941-04-09"],
    ["d36a49ed-dd13-552b-9509-6477fe43872a", "Semiprofessional occupations, not elsewhere classified", "1943-08-12"],
  ] as const;

  for (const [id, occupation, date] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText(date);
    await expect(main).toContainText(/no (?:school or )?employer is identified/i);
    await expect(main).toContainText("occupation only found");
  }
});

test("Norman Streeter's 1945 occupation remains temporally uncertain", async ({ page }) => {
  await page.goto("./people/802cbb13-1a4d-5078-a233-6fefbc226de0/");
  const main = page.locator("main");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("Because this entry date is in 1945");
});

test("rejected Streed and Thomas Streeter Army candidates transfer no fields", async ({ page }) => {
  await page.goto("./people/dbe6304d-6bb1-5483-93b6-eb41572f0668/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Ernest H Steed");
  await expect(main).toContainText("all attached fields were rejected");

  await page.goto("./people/2abae00d-4604-50eb-a84d-23049d23c7c0/");
  main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("James E OConnell");
  await expect(main).toContainText("Do not transfer any field");
});

test("variant clusters stay separate and visible", async ({ page }) => {
  const cases = [
    ["a83e8685-38a2-598b-bc91-42598bd5232d", "Elmer S Streeter"],
    ["803ea5df-1954-5848-829c-a5af19f134d2", "Robert E Strief"],
    ["1cd1e7c4-8c21-5d0a-86e1-788915338430", "William C Strickland"],
  ] as const;
  for (const [id, alternate] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Possible duplicate group");
    await expect(main).toContainText(alternate);
  }
});

test("Stephen Streeter retains the Box 752 versus 753 qualification", async ({ page }) => {
  await page.goto("./people/3ec9d787-c0ca-5d3b-9bf6-8266543a29d6/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("OSS X-2 Balkans");
  await expect(main).toContainText("Box 752");
  await expect(main).toContainText("Box 753");
  await expect(main).toContainText("requires archival review");
});

test("Nicholas Strike keeps prewar organizational leadership separate from employment", async ({ page }) => {
  await page.goto("./people/526fc414-2a93-566a-9f5e-1246122f61f5/");
  const main = page.locator("main");
  await expect(main).toContainText("Sons of Pericles");
  await expect(main).toContainText("national president");
  await expect(main).toContainText("professional affiliation");
  await expect(main).toContainText("not employment");
  await expect(main).toContainText("probable");
  const civilianEmployer = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(civilianEmployer).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed",
  );
});

test("Theophanes Strimenos publishes direct military and civilian chronology", async ({ page }) => {
  await page.goto("./people/2b92e253-f5d1-5fb0-93d1-662da49b084d/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Alabama National Guard");
  await expect(main).toContainText("November 1940");
  await expect(main).toContainText("September 1943");
  await expect(main).toContainText("cafe worker");
  await expect(main).toContainText("unnamed cafe in Mobile, Alabama");
  await expect(main).toContainText("employer's name is not given");
  await expect(main).toContainText("Hoover Institution");
});

test("Batch 924 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 924 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 622,
    research_attempted_people: 14_201,
    verified_affiliation_people: 1_010,
    verified_employer_people: 455,
    archival_review_assessed_people: 12_674,
    published_claims: 8_709,
    public_sources: 5_779,
  });
});
