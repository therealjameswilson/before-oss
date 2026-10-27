import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page453-harry-strozer-to-jack-r-stubbs-review_batch-926_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["4071581a-cf4d-5465-b9ab-b048a4834ede", "Harry Strozer"],
  ["2f89d8a4-08ae-5572-9bc6-95c714f7037a", "Francois Strub"],
  ["df309945-6593-580e-8f3f-9242add28fde", "Byron T Strubbs"],
  ["5b7b3a9e-8a78-50d8-82c7-d677b1b8df42", "James M Strueber"],
  ["6e123cf0-88ad-5b80-ac87-ac64de77b32c", "Benjamin Strunk"],
  ["e305ccad-b2e5-5551-ba96-491d5ca24185", "Benjamin F Strunk"],
  ["411691a6-cd6a-5734-be55-2be3fd0d4167", "Norman W Strunk"],
  ["776ee0ec-ca66-5acc-a913-8ed07ab3bf81", "Joseph L Strup"],
  ["b0ace79b-87fe-5a71-9521-5d08a66166e3", "Walter Struwe"],
  ["7a9b6b86-a4e2-5b08-b7ed-e5db13b82978", "Melvin Struz"],
  ["a4d4ab5b-b85c-558d-acc2-21cbade2c2f9", "Zbigniew Strzelinski"],
  ["674ad910-1f5d-5e79-9b9a-ea7395c80bd0", "Arthur W Stuart"],
  ["f2c0fcde-197d-5083-b523-54ae075d8ba8", "Arthur W Stuart"],
  ["f87ee060-f3bd-561e-a5ba-c8fd61c6ad2a", "Charles E Stuart"],
  ["25e677b9-c89f-59d8-9c21-4ba95cfed7fa", "Chester J Stuart"],
  ["915da674-6281-5950-a3c3-29674e8a86ae", "Ernest A Stuart"],
  ["55d5598b-ec0e-5d2a-b11e-2d509c338a7c", "James Stuart"],
  ["15857283-ee80-5e7d-a09c-0bef619e304f", "Jean F Stuart"],
  ["4b99de9f-5faf-5673-9031-62f48d4a995f", "Kimberly Stuart"],
  ["13a10b6e-1455-576d-9c9f-7140afcc35f9", "Richard Stuart"],
  ["933f1373-855a-53df-9249-4e2e66351513", "Richard Stuart"],
  ["81653b6f-53e2-5fcf-8a2a-046707041c34", "Roger M Stuart"],
  ["80266adb-1261-5f48-be76-99878dcdacb7", "Jack R Stubbs"],
] as const;

test("Batch 926 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("six Army occupation findings remain qualified and employer-free", async ({ page }) => {
  const cases = [
    ["df309945-6593-580e-8f3f-9242add28fde", "Mechanics and repairmen, n.e.c.", "1943-03-12"],
    ["e305ccad-b2e5-5551-ba96-491d5ca24185", "Stamping occupations in mechanical treatment of metals", "1942-10-30"],
    ["776ee0ec-ca66-5acc-a913-8ed07ab3bf81", "Photographers", "1942-10-17"],
    ["7a9b6b86-a4e2-5b08-b7ed-e5db13b82978", "Students", "1943-07-19"],
    ["674ad910-1f5d-5e79-9b9a-ea7395c80bd0", "Managers and officials, n.e.c.", "1943-08-16"],
    ["80266adb-1261-5f48-be76-99878dcdacb7", "Students", "1944-11-03"],
  ] as const;

  for (const [id, occupation, date] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText(date);
    await expect(main).toContainText("no employer or institution is named");
    await expect(main).toContainText("occupation only found");
  }
});

test("Walter Struwe publishes an explicit trade-unionist pathway without inventing an employer", async ({ page }) => {
  await page.goto("./people/b0ace79b-87fe-5a71-9521-5d08a66166e3/");
  const main = page.locator("main");
  await expect(main).toContainText("Walter Strüwe");
  await expect(main).toContainText("trade unionist");
  await expect(main).toContainText("late August 1944");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("German Anti-Nazi Espionage in the Second World War");
  await expect(main).not.toContainText("bricklayer");
});

test("Zbigniew Strzelinski publishes a qualified military pathway and documented aliases", async ({ page }) => {
  await page.goto("./people/a4d4ab5b-b85c-558d-acc2-21cbade2c2f9/");
  const main = page.locator("main");
  await expect(main).toContainText("Zbigniew Strzeliński");
  await expect(main).toContainText("Zbigniew Paprzycki");
  await expect(main).toContainText("Polish Armed Forces");
  await expect(main).toContainText("Wehrmacht");
  await expect(main).toContainText("Project Eagle");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("Chojnicki Orzeł");
});

test("withheld namesake candidates create no public claim or affiliation", async ({ request, page }) => {
  const people = [];
  for (const shard of ["f", "h", "r"]) {
    const response = await request.get(`./data/people/${shard}.json`);
    expect(response.ok()).toBeTruthy();
    people.push(...await response.json());
  }
  const ids = new Set([
    "4071581a-cf4d-5465-b9ab-b048a4834ede",
    "2f89d8a4-08ae-5572-9bc6-95c714f7037a",
    "13a10b6e-1455-576d-9c9f-7140afcc35f9",
    "933f1373-855a-53df-9249-4e2e66351513",
  ]);
  const withheld = people.filter((person: { person_id: string }) => ids.has(person.person_id));
  expect(withheld).toHaveLength(4);
  for (const person of withheld) {
    expect(person.claims).toEqual([]);
    expect(person.immediate_pre_oss_affiliations).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
    expect(person.other_pre_oss_affiliations).toEqual([]);
  }

  await page.goto("./people/4071581a-cf4d-5465-b9ab-b048a4834ede/");
  await expect(page.locator("main")).not.toContainText("Dutro & Co.");
  await page.goto("./people/2f89d8a4-08ae-5572-9bc6-95c714f7037a/");
  await expect(page.locator("main")).not.toContainText("GénéaFrance");
});

test("Benjamin, Arthur and Richard duplicate pairs remain separate and visibly linked", async ({ page }) => {
  const pairs = [
    ["6e123cf0-88ad-5b80-ac87-ac64de77b32c", "e305ccad-b2e5-5551-ba96-491d5ca24185", "Benjamin F Strunk"],
    ["674ad910-1f5d-5e79-9b9a-ea7395c80bd0", "f2c0fcde-197d-5083-b523-54ae075d8ba8", "Arthur W Stuart"],
    ["13a10b6e-1455-576d-9c9f-7140afcc35f9", "933f1373-855a-53df-9249-4e2e66351513", "Richard Stuart"],
  ] as const;

  for (const [first, second, otherName] of pairs) {
    await page.goto(`./people/${first}/`);
    await expect(page.locator("main")).toContainText("Possible duplicate group");
    await expect(page.locator(`a[href*="/people/${second}/"]`)).toContainText(otherName);
    await page.goto(`./people/${second}/`);
    await expect(page.locator("main")).toContainText("Possible duplicate group");
    await expect(page.locator(`a[href*="/people/${first}/"]`)).toContainText(/Benjamin Strunk|Arthur W Stuart|Richard Stuart/);
  }
});

test("the two Richard Stuart rows receive no school-principal affiliation as fact", async ({ request }) => {
  const response = await request.get("./data/people/r.json");
  const people = await response.json();
  for (const id of [
    "13a10b6e-1455-576d-9c9f-7140afcc35f9",
    "933f1373-855a-53df-9249-4e2e66351513",
  ]) {
    const person = people.find((item: { person_id: string }) => item.person_id === id);
    expect(person.identity_status).toBe("ambiguous");
    expect(person.claims).toEqual([]);
    expect(person.last_civilian_pre_service).toEqual([]);
  }
});

test("Batch 926 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 926 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 626,
    research_attempted_people: 14_245,
    verified_affiliation_people: 1_012,
    verified_employer_people: 456,
    archival_review_assessed_people: 12_718,
    published_claims: 8_738,
    public_sources: 5_792,
  });
});
