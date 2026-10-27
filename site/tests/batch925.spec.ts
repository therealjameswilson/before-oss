import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page453-charlie-e-stringer-to-bernard-e-strozenski-review_batch-925_2026-10-26.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["76e80fa6-1a97-5b8d-87fd-a41f1f124314", "Charlie E Stringer"],
  ["5ceda236-9a1e-5c3f-91c5-b3117ec25989", "James A Stringer"],
  ["5fda078e-0385-586a-9257-c3b99737a8a7", "Elden R Stringfellow"],
  ["323aa721-0234-53d2-9da8-5f5cb06229fc", "Horace Stringfellow"],
  ["3f6fef6c-0374-52f3-8e35-bc44710d72a1", "Harry R Stritman"],
  ["9e1f8844-880f-5c12-a8bc-7874a97eaff7", "Anthony J Strobl"],
  ["598a0f40-31e6-5acc-8807-c30ffca57c47", "Sylvia S Strohman"],
  ["b3919726-c363-5da4-9258-156e6e8e6ba7", "Lester A Stromberg"],
  ["638047fa-fbbe-53c7-96d4-77c794b814c2", "Edmund I Stromholt"],
  ["87031931-cac0-53eb-829a-03e87dc4b2d0", "Birger Stromsheim"],
  ["04292e37-b226-552b-860c-336b8b48b126", "David F Strong"],
  ["dcbc6a3f-534d-5681-aba3-43064e772089", "Joan M Strong"],
  ["d3c854f7-60c5-5d4a-bf28-428146db4061", "Philip D Strong"],
  ["15a35f9d-2de5-5c55-9cc5-0fd3b3ff5394", "Sherman I Strong"],
  ["88a9dda3-01d2-5385-b121-ba17ca341dd8", "Philip Strongin"],
  ["0a7e8099-31d5-504e-b3bb-8e1f990130e6", "Edward K Stropp"],
  ["e763e441-1516-5f89-8f03-3def28d07a81", "Jaunita H Strosnider"],
  ["2404a3bd-01c7-552e-ab1d-0c07adc3c20d", "Jeanne H Stroud"],
  ["2551c9c8-3307-5ca3-b498-f1b9348bc45e", "Robert L Stroud"],
  ["8264951b-a33e-5155-9a62-996388c1acf2", "Ray M Stroupe"],
  ["5bca5a08-f53d-5f02-8a4c-c75e3c0781cd", "Harry D Strouse"],
  ["ee569abe-319c-567c-a922-49ff72153677", "Bernard B Strozenski"],
  ["ce77c56f-052f-511b-a375-ae9b026f1492", "Bernard E Strozenski"],
] as const;

test("Batch 925 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Anthony Strobl publishes Disney as a last civilian employer, not an immediate OSS predecessor", async ({ page }) => {
  await page.goto("./people/9e1f8844-880f-5c12-a8bc-7874a97eaff7/");
  const main = page.locator("main");
  await expect(main).toContainText("Walt Disney Studios");
  await expect(main).toContainText("in-betweener and animator");
  await expect(main).toContainText("December 1938");
  await expect(main).toContainText("December 1941");
  await expect(main).toContainText("last documented civilian employer before service");
  await expect(main).toContainText("Commercial artists");
  await expect(main).toContainText("no employer is identified");
  await expect(main).toContainText("The classic Donald Duck of Tony Strobl");
});

test("Birger Stromsheim remains a qualified probable identity and employer finding", async ({ page }) => {
  await page.goto("./people/87031931-cac0-53eb-829a-03e87dc4b2d0/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("construction contractor");
  await expect(main).toContainText("Norwegian Independent Company 1");
  await expect(main).toContainText("not a proven immediate OSS predecessor");
  await expect(main).toContainText("Box 753 has not been reviewed");
});

test("five additional Army occupation findings remain qualified and employer-free", async ({ page }) => {
  const cases = [
    ["76e80fa6-1a97-5b8d-87fd-a41f1f124314", "Machinists' apprentices", "1943-01-29"],
    ["323aa721-0234-53d2-9da8-5f5cb06229fc", "Servicemen and linemen, telegraph, telephone, and power", "1941-07-10"],
    ["d3c854f7-60c5-5d4a-bf28-428146db4061", "Students", "1942-11-11"],
    ["88a9dda3-01d2-5385-b121-ba17ca341dd8", "Commercial artists", "1942-04-27"],
    ["ee569abe-319c-567c-a922-49ff72153677", "Students", "1944-07-03"],
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

test("James Stringer's undefined 1946 code is not converted into an occupation", async ({ page }) => {
  await page.goto("./people/5ceda236-9a1e-5c3f-91c5-b3117ec25989/");
  const main = page.locator("main");
  await expect(main).toContainText("official code 055 is not interpreted");
  await expect(main).toContainText("1946 Army-entry date does not establish pre-OSS chronology");
  await expect(main).not.toContainText("occupation only found");
});

test("Harry Strouse's father-son conflict transfers no career to the index row", async ({ page }) => {
  await page.goto("./people/5bca5a08-f53d-5f02-8a4c-c75e3c0781cd/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Major Harry D. Strouse");
  await expect(main).toContainText("Harry Dunlap Strouse Jr.");
  await expect(main).toContainText("cannot yet be assigned");
  await expect(main).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed",
  );
});

test("the two Bernard Strozenski rows remain separate and visibly linked", async ({ page }) => {
  await page.goto("./people/ee569abe-319c-567c-a922-49ff72153677/");
  let main = page.locator("main");
  await expect(main).toContainText("Possible duplicate group");
  await expect(main).toContainText("Bernard E Strozenski");
  await expect(main).toContainText("Students");

  await page.goto("./people/ce77c56f-052f-511b-a375-ae9b026f1492/");
  main = page.locator("main");
  await expect(main).toContainText("Possible duplicate group");
  await expect(main).toContainText("Bernard B Strozenski");
  await expect(main).toContainText("ambiguous");
  await expect(main).not.toContainText("At Army entry on 1944-07-03");
});

test("printed Jaunita spelling is preserved and Edmund Stromholt's completed outcome is retained", async ({ page }) => {
  await page.goto("./people/e763e441-1516-5f89-8f03-3def28d07a81/");
  await expect(page.getByRole("heading", { name: "Jaunita H Strosnider", level: 1 })).toBeVisible();

  await page.goto("./people/638047fa-fbbe-53c7-96d4-77c794b814c2/");
  const main = page.locator("main");
  await expect(main).toContainText("completed");
  await expect(main).toContainText("Norwegian Army");
  await expect(main).toContainText("Lieutenant and raiding instructor");
});

test("Batch 925 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 925 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 623,
    research_attempted_people: 14_223,
    verified_affiliation_people: 1_011,
    verified_employer_people: 456,
    archival_review_assessed_people: 12_696,
    published_claims: 8_727,
    public_sources: 5_786,
  });
});
