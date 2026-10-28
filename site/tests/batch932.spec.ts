import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page456-donald-e-sutcliffe-to-betty-h-swadley-review_batch-932_2026-10-27.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["c48691a9-43d2-5246-ba69-9702e8a4eb4a", "Donald E Sutcliffe"],
  ["bd135d1d-e4e2-5566-aed2-8c94c3d7a836", "Philip H Suter"],
  ["31bc2825-2c85-5e81-8702-318864b1c26e", "Arthur F Sutherland"],
  ["91c208f5-0d6e-5907-8dda-822c81418fe6", "Arthur E Sutherland"],
  ["cc19aec8-7e7b-5960-a126-b43f5ba4167c", "Charles B Sutherland"],
  ["f0673e96-19cf-533a-ba7c-7aaf377a6ac4", "Joel Sutherland"],
  ["bf559bc5-6ac5-5915-b07a-68a8ca2b3058", "Martha T Sutphin"],
  ["dae6c4b2-1b06-5e73-88ff-07faad620041", "Lawson R Suttles"],
  ["0b31ec21-8a8b-5e7f-bd54-03b19c909ae2", "Henry C Sutton"],
  ["09426597-aa08-5f50-8bae-68a0a068d0fb", "Heinrich C Soffner"],
  ["cc776681-e03c-50b2-bfc4-7c8de7c9a17f", "John H Sutton"],
  ["81694444-7f10-5e36-9004-e4822f2d5921", "Ray C Sutton"],
  ["bb34db8a-a210-593c-b88e-3cb9ae7447e6", "Robert H Sutton"],
  ["1d18d704-45f8-5ffd-b3e7-c532d06bc6ca", "Robert W Sutton"],
  ["ac571642-c904-5648-a9e6-c907c39ada95", "Walter D Sutton"],
  ["4dd22b11-1980-525b-bc63-41267b69e8f5", "Walter L Sutton"],
  ["c0b90cc3-9062-5de2-849f-6910c029d68d", "Kenneth F Suydam"],
  ["a7a4d94f-eb50-5ade-924e-2e3f5bbe0fbb", "Robert F Suyeoka"],
  ["d22d6aa0-0003-537e-8c95-b2c4901533a3", "Ken I Suzuki"],
  ["f9922ab4-f9d2-58b9-bf58-81bf4e80418e", "Koshi Suzuki"],
  ["e023423d-078d-51a3-958e-e7e83c832fba", "M C Svasti"],
  ["54bc4ff1-8995-57fe-ae9a-b2ea515aee5e", "Morris H Swadesh"],
  ["26454c44-5f8a-53d3-bddb-dc279a093075", "Betty H Swadley"],
] as const;

test("Batch 932 publishes all 23 indexed-row entities with terminal outcomes", async ({ page }) => {
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

test("five Army findings remain occupation-only and employer-free", async ({ page }) => {
  for (const [id, occupation] of [
    ["c48691a9-43d2-5246-ba69-9702e8a4eb4a", "Occupations in manufacture of textiles"],
    ["bb34db8a-a210-593c-b88e-3cb9ae7447e6", "Stenographers and typists"],
    ["1d18d704-45f8-5ffd-b3e7-c532d06bc6ca", "Clerks, general office"],
    ["c0b90cc3-9062-5de2-849f-6910c029d68d", "Cooks, except private family"],
    ["a7a4d94f-eb50-5ade-924e-2e3f5bbe0fbb", "Electricians"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("no employer or workplace");
    await expect(main).toContainText("occupation only found");
    await expect(main).not.toContainText("Last civilian employer before wartime service");
  }
});

test("Morris Swadesh publishes employers and distinct government assignments without an immediate claim", async ({ request, page }) => {
  await page.goto("./people/54bc4ff1-8995-57fe-ae9a-b2ea515aee5e/");
  const main = page.locator("main");
  await expect(main).toContainText("Instituto Politécnico Nacional");
  await expect(main).toContainText("Escuela de Antropología e Historia");
  await expect(main).toContainText("Consejo de Lenguas Indígenas");
  await expect(main).toContainText("Departamento de Asuntos Indígenas");
  await expect(main).toContainText("Signal Corps");
  await expect(main).toContainText("First lieutenant");

  const response = await request.get("./data/people/m.json");
  const people = await response.json();
  const swadesh = people.find((item: { person_id: string }) => item.person_id === "54bc4ff1-8995-57fe-ae9a-b2ea515aee5e");
  expect(swadesh.immediate_pre_oss_affiliations).toHaveLength(0);
  expect(swadesh.last_civilian_pre_service).toHaveLength(4);
  expect(swadesh.last_civilian_pre_service.filter((item: { relationship_type: string }) => item.relationship_type === "employment")).toHaveLength(2);
  expect(swadesh.last_civilian_pre_service.filter((item: { relationship_type: string }) => item.relationship_type === "government_assignment")).toHaveLength(2);
});

test("Robert Suyeoka keeps MIS language training distinct from civilian occupation", async ({ page }) => {
  await page.goto("./people/a7a4d94f-eb50-5ade-924e-2e3f5bbe0fbb/");
  const main = page.locator("main");
  await expect(main).toContainText("Bobby Suyeoka");
  await expect(main).toContainText("Electricians");
  await expect(main).toContainText("Military Intelligence Service Language School");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).not.toContainText("Last civilian employer before wartime service");
});

test("Koshi Suzuki and M C Svasti remain visibly qualified probable identities", async ({ page }) => {
  await page.goto("./people/f9922ab4-f9d2-58b9-bf58-81bf4e80418e/");
  let main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Kinmon Gakuen");
  await expect(main).toContainText("Naval Intelligence Language School");
  await expect(main).toContainText("medium");

  await page.goto("./people/e023423d-078d-51a3-958e-e7e83c832fba/");
  main = page.locator("main");
  await expect(main).toContainText("Prince Subhasvasti Wongsnit Savasdivatana");
  await expect(main).toContainText("Royal Military Academy, Woolwich");
  await expect(main).toContainText("Royal Guard");
  await expect(main).toContainText("Force 136");
  await expect(main).toContainText("probable");
});

test("the Henry Sutton duplicate conflict remains separate from Heinrich Soffner", async ({ request, page }) => {
  await page.goto("./people/0b31ec21-8a8b-5e7f-bd54-03b19c909ae2/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Heinrich C Soffner");
  await expect(main).toContainText("identifiers differ");

  const response = await request.get("./data/people/h.json");
  const people = await response.json();
  const henry = people.find((item: { person_id: string }) => item.person_id === "0b31ec21-8a8b-5e7f-bd54-03b19c909ae2");
  const heinrich = people.find((item: { person_id: string }) => item.person_id === "09426597-aa08-5f50-8bae-68a0a068d0fb");
  expect(henry.possible_duplicate_group).toBeTruthy();
  expect(henry.possible_duplicate_group).toBe(heinrich.possible_duplicate_group);
  expect(henry.identity_status).toBe("ambiguous");
  expect(heinrich.identity_status).toBe("confirmed");
});

test("John Sutton preserves the duplicate Army-row grade disagreement", async ({ page }) => {
  await page.goto("./people/cc776681-e03c-50b2-bfc4-7c8de7c9a17f/");
  const main = page.locator("main");
  await expect(main).toContainText("PVT versus 0");
  await expect(main).toContainText("code 999 is not interpreted");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("Last civilian employer before wartime service");
});

test("Batch 932 does not change the evidence-defined oil-company category", async ({ page }) => {
  await page.goto("./oil-companies/");
  const main = page.locator("main");
  await expect(main).toContainText("14 people");
  await expect(main).toContainText("15 historically named");
  await expect(main).not.toContainText("Kinmon Gakuen");
});

test("Batch 932 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(evidence).not.toMatch(/serial-conflict:\d/);
});

test("Batch 932 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 631,
    research_attempted_people: 14_382,
    verified_affiliation_people: 1_019,
    verified_employer_people: 460,
    archival_review_assessed_people: 12_855,
    published_claims: 8_856,
    public_sources: 5_844,
  });
});
