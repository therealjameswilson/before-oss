import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page448-stevens-to-stewart-review_batch-916_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["59aef3b2-c750-53ca-ae7b-b655520fac6b", "Rebecca B Stevens"],
  ["8a9a7f4d-a482-5901-a9c5-2d3102153e8f", "Rowland P Stevens"],
  ["b968b43f-3213-5f0c-a176-335cdef07db8", "Alexander Stevenson"],
  ["a9149157-d807-516b-b2fe-49bf722495eb", "Beatrice Ellen Stevenson"],
  ["f85654fd-b770-5089-88f2-aa6e0d5d4b21", "Caroline S Stevenson"],
  ["0a9b0230-fe9b-5242-91e3-2799e1d8b28d", "Chester Stevenson"],
  ["b5f8a1e5-9fc9-55bb-923a-dd2248c55366", "Dorothy S Stevenson"],
  ["ce0c6016-a47a-5cb8-8495-01fc0967c3e4", "Harold R Stevenson"],
  ["0c1c613e-024d-5afc-9a43-1ef18d06932a", "Thomas T Stevenson"],
  ["e5fcfea6-b88a-5014-9c82-e3ac48159c39", "Viola M Stevenson"],
  ["4e7c1024-67a2-5bd5-af44-8b7fc75cad42", "Wayne J Stevenson"],
  ["5ed0be1f-d66f-50be-b9e0-b16e22090251", "Richard C Steward"],
  ["edef257d-0310-5658-9b94-ec2807a16757", "Arthur W Stewart"],
  ["d4159c13-03e6-5bdf-b2ca-822b44c3cf1b", "Charles L Stewart"],
  ["29512173-cebb-5f66-9f7c-c5f5faddff1c", "Dean W Stewart"],
  ["f6fa86e3-545f-5628-9e71-4ab7a97085d0", "Donald C Stewart"],
  ["d2588419-39c6-56c9-bdec-34411ed7e547", "Francis J Stewart"],
  ["c9cb6a53-a776-5546-a5bd-7e0d9050485d", "George W Stewart"],
  ["a07b46f7-fd11-5e8b-99d3-459107ce1ad5", "Gordon Stewart"],
  ["0923d0e0-c668-5900-89e7-8b6ec446a291", "Grace A Stewart"],
  ["db9f016d-859a-59a8-8215-fb8378f17a24", "Gretchen E Stewart"],
  ["9138358d-a977-5800-befd-70a991f2f5f7", "Harrison M Stewart"],
  ["9a695ad7-53e7-5bab-8db7-690290c2cab1", "Harvey S Stewart"],
] as const;

test("Batch 916 publishes all 23 people with saved outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 916 Army categories remain occupations or student status rather than employers", async ({ page }) => {
  const cases = [
    ["b968b43f-3213-5f0c-a176-335cdef07db8", "Professional occupations, not elsewhere classified"],
    ["4e7c1024-67a2-5bd5-af44-8b7fc75cad42", "Clerks, general office"],
    ["5ed0be1f-d66f-50be-b9e0-b16e22090251", "Decorators and window dressers"],
    ["edef257d-0310-5658-9b94-ec2807a16757", "Artists, sculptors, and teachers of art"],
    ["d4159c13-03e6-5bdf-b2ca-822b44c3cf1b", "Managers and officials, not elsewhere classified"],
    ["29512173-cebb-5f66-9f7c-c5f5faddff1c", "Mail carriers"],
    ["f6fa86e3-545f-5628-9e71-4ab7a97085d0", "Hotel and restaurant managers"],
    ["d2588419-39c6-56c9-bdec-34411ed7e547", "Guards and watchmen, except crossing watchmen"],
    ["c9cb6a53-a776-5546-a5bd-7e0d9050485d", "General farmers"],
    ["9138358d-a977-5800-befd-70a991f2f5f7", "Students"],
    ["9a695ad7-53e7-5bab-8db7-690290c2cab1", "Policemen and detectives, public service"],
  ] as const;
  for (const [id, label] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(label);
    await expect(main).toContainText("no employer is identified");
  }
});

test("Arthur W Stewart publishes a prewar art affiliation without inventing an employer", async ({ page }) => {
  await page.goto("./people/edef257d-0310-5658-9b94-ec2807a16757/");
  const main = page.locator("main");
  await expect(main).toContainText("Arthur Walter Stewart");
  await expect(main).toContainText("Dixie Art Colony");
  await expect(main).toContainText("artist participant");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./organizations/5ff8b974-76c0-5603-b741-2b7b6de2b7d5/");
  await expect(page.getByRole("heading", { name: "Dixie Art Colony", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("Arthur W Stewart");
  await expect(page.locator("main")).toContainText("distinct from the Dixie Art Colony Foundation");
});

test("Gordon Stewart remains unresolved instead of inheriting an unbridged namesake biography", async ({ page }) => {
  await page.goto("./people/a07b46f7-fd11-5e8b-99d3-459107ce1ad5/");
  const main = page.locator("main");
  await expect(main).toContainText("Gordon Matthews Stewart");
  await expect(main).toContainText("plausible namesake only");
  await expect(main).toContainText("requires archival review");
});

test("Batch 916 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 916 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 615,
    research_attempted_people: 14_017,
    verified_affiliation_people: 1_002,
    verified_employer_people: 451,
    archival_review_assessed_people: 12_490,
    published_claims: 8_595,
    public_sources: 5_710,
  });
});
