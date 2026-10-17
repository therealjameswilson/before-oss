import { expect, test } from "@playwright/test";

const profiles = [
  ["a9a65dd0-3dbc-520f-8597-ad2a9b483022", "Oliver M Silsby"],
  ["1181766d-9b43-538e-b37e-ff15aaf865ee", "Louis J Silva"],
  ["d557a2e7-286d-522a-8c3f-e42e65d3fc26", "Stelvio Silvani"],
  ["621671c5-0648-504f-b453-1bca4c2dad87", "Fernando A Silveire"],
  ["25d2892f-8bf4-5d29-ac4c-286aad29b9ba", "Irwin S Silver"],
  ["69d71538-36b3-5c90-985c-17661b7f3cd2", "Jack M Silver"],
  ["0e7133e6-537f-5f60-a336-879e5ff90f02", "Augusta Silverman"],
  ["7d9c8574-7d24-5bc9-ac68-03ab1addf501", "Gerald S Silverman"],
  ["5c511854-1637-5d0f-9f08-4a74989e6e74", "Milton Silverman"],
  ["dc4ee112-b0aa-5313-9caf-8b5d01b2554f", "Norman Silverman"],
  ["146c3633-c475-5719-9aee-b0e3f484a20f", "Sidney Silverman"],
  ["4fd015bb-24e3-5ec7-8f8e-9de4328fea83", "Raymond J Silverstein"],
  ["ae103258-b02f-5576-908e-ea038870de11", "Carl Silvestri"],
  ["2749d5d9-7946-52b5-86b0-cfd2dcfc6ec0", "Mario J Silvestri"],
  ["a73bb1b0-7f61-5f1f-8947-7127d2d06792", "Agnes F Silvey"],
  ["b42db698-f9d1-57d4-abc0-779d150f8db2", "Joseph M Silvis"],
  ["7fdc1519-8dee-5298-8660-4354e31d5dba", "Irwin W Simans"],
  ["5f63a67f-27a8-5fc1-9cc9-d02dbe3e0bd6", "Albert Simard"],
  ["9882cb4b-fc54-5024-a803-fbfdcd32fd2f", "Rene Simard"],
  ["11ba4eca-97e9-5d26-ab28-d3de4efc1305", "Elizabeth K Simeon"],
  ["9dc7807e-02aa-5161-b6e1-965c31a6a97d", "Frank G Simeone"],
  ["46455192-e74f-50e6-819a-f912976446a9", "Dominic J Simeri"],
  ["38a85223-12bb-579a-bfd5-0f21d7cdedc5", "Uumo A Simila"],
] as const;

test("Batch 876 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 876 documents Oliver Silsby's Army-to-OSS pathway without inventing a civilian employer", async ({ page }) => {
  await page.goto("./people/a9a65dd0-3dbc-520f-8597-ad2a9b483022/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconfirmed");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Corporal and radio operator");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("Last civilian employer before serviceNo reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("Review Box 711");
});

test("Batch 876 preserves the Mario Silvestri Army-name conflict", async ({ page }) => {
  await page.goto("./people/2749d5d9-7946-52b5-86b0-cfd2dcfc6ec0/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Evidence conflicts");
  await expect(main).toContainText("SELLERS JIM rather than Mario J Silvestri");
  await expect(main).toContainText("No employer, occupation or chronology is inferred");
});

test("Batch 876 keeps the Albert Simard France Forever lead unassigned", async ({ page }) => {
  await page.goto("./people/5f63a67f-27a8-5fc1-9cc9-d02dbe3e0bd6/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("France Forever");
  await expect(main).toContainText("no shared identifier");
  await expect(main).toContainText("Review Box 712 before assigning Dr. Albert Simard");
  await expect(main).toContainText("Immediate pre-OSS affiliationNo reviewed claim currently meets the publication threshold");
});

test("Batch 876 rejects the unsupported Uumo Simila genealogy lead", async ({ page }) => {
  await page.goto("./people/38a85223-12bb-579a-bfd5-0f21d7cdedc5/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("unsourced genealogy page");
  await expect(main).toContainText("no middle initial, protected identifier, OSS connection or employment evidence");
  await expect(main).toContainText("Review Box 712");
});

test("Batch 876 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 583,
    research_attempted_people: 13_111,
    verified_affiliation_people: 950,
    verified_employer_people: 431,
    archival_review_assessed_people: 11_578,
    published_claims: 7_913,
    public_sources: 5_380,
  });
});
