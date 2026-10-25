import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page443-st-thomas-to-stamnock-review_batch-906_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["c75c56b5-e909-5af5-b768-b60db5609e5e", "Jean St. Thomas"],
  ["8661ce76-3af7-5bf1-992e-1d4a89a7ac37", "Jacov Staal"],
  ["c6a4198d-cfeb-5558-9e8a-1850dd75f225", "J R Staats"],
  ["051d8378-29bf-583c-9b60-41c923cc41a0", "Ryneer A Staats"],
  ["fac95fd7-1393-51ed-8df0-cea97facbd3b", "Clifford D Stack"],
  ["56c59499-289a-5b81-8083-36f6499be217", "James F Stacy"],
  ["c589c231-cb5a-518e-9cdd-114484bc119c", "John A Stacy"],
  ["ac36f6a3-16e0-5fb1-9e6a-6e1b6f8c20db", "Howard A Stadermann"],
  ["aae82823-6bc7-5f01-9c3d-0535d99e052f", "Frederick J Stadler"],
  ["4338c90d-460f-56b0-9367-ad0ceb83c52f", "Glen M Stadler"],
  ["97695d0a-6fdd-5dda-8a75-ccb0d7252e77", "Jimmie Stafford"],
  ["edd7eae3-d9cd-5725-8945-a80b4e28b090", "Walter E Stafford"],
  ["2ca0c4ef-6c8c-5640-b2b3-1758b090ea95", "Ella M Stagg"],
  ["e64fd301-0183-5535-bf7b-3c9e885902e9", "Donald C Stahl"],
  ["41c6eca3-ac25-595c-ab12-fcdcc6b7c8e6", "Martin Stahl"],
  ["d4e11632-c367-5d3b-ab4d-e583cf8fa7ce", "Ferdinando Stahly"],
  ["2b671e64-23bb-5753-8582-b91a7729c6e5", "Eugene L Staiger"],
  ["727a6826-b4c7-5d0f-ad18-5a48b6696605", "Stanley A Staiger"],
  ["2cc57327-5011-58e7-8122-145adacf288d", "Richard D Stainbrook"],
  ["1448fa2a-a922-56e4-a160-6a3bc1478b29", "Laurence T Stallings"],
  ["f852edf0-d68f-56b8-9f54-5910ec700d23", "Peter Stamates"],
  ["9b7207d9-0de2-5210-9397-ca4acfcf8c32", "Max Stamler"],
  ["15f9a410-37d7-57b8-83e6-98ce98e51fb3", "Leonard V Stamnock"],
] as const;

test("Batch 906 publishes all 23 people with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 906 Army bridges publish qualified occupations, not employers", async ({ page }) => {
  const checks = [
    ["c75c56b5-e909-5af5-b768-b60db5609e5e", "Photographers"],
    ["56c59499-289a-5b81-8083-36f6499be217", "Clerks, general office"],
    ["edd7eae3-d9cd-5725-8945-a80b4e28b090", "Semiskilled chauffeurs and drivers"],
    ["e64fd301-0183-5535-bf7b-3c9e885902e9", "Semiskilled chauffeurs and drivers"],
    ["2b671e64-23bb-5753-8582-b91a7729c6e5", "fabrication of metal products"],
    ["2cc57327-5011-58e7-8122-145adacf288d", "Students"],
    ["f852edf0-d68f-56b8-9f54-5910ec700d23", "structural and ornamental-metal workers"],
  ] as const;

  for (const [id, occupation] of checks) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(occupation);
    await expect(main).toContainText("no employer is identified");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Stainbrook uses NARA's amended code 992 and not the superseded metal-production label", async ({ page }) => {
  await page.goto("./people/2cc57327-5011-58e7-8122-145adacf288d/");
  const main = page.locator("main");
  await expect(main).toContainText("Students");
  await expect(main).not.toContainText("production of ferrous and nonferrous metals");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Stanley Staiger keeps University of Oregon as student status", async ({ page }) => {
  await page.goto("./people/727a6826-b4c7-5d0f-ad18-5a48b6696605/");
  const main = page.locator("main");
  await expect(main).toContainText("DUCK Mission");
  await expect(main).toContainText("University of Oregon");
  await expect(main).toContainText("student; ROTC class member");
  await expect(main).toContainText("university was not his employer");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Stallings and Stadler findings remain visibly qualified", async ({ page }) => {
  await page.goto("./people/1448fa2a-a922-56e4-a160-6a3bc1478b29/");
  let main = page.locator("main");
  await expect(main).toContainText("Metro-Goldwyn-Mayer");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("If the indexed person is Laurence Tucker Stallings");

  await page.goto("./people/4338c90d-460f-56b0-9367-ad0ceb83c52f/");
  main = page.locator("main");
  await expect(main).toContainText("United Press");
  await expect(main).toContainText("Paris bureau correspondent");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("A probable match worked for United Press");
});

test("Martin Stahl low-confidence memo lead stays private", async ({ page }) => {
  await page.goto("./people/41c6eca3-ac25-595c-ab12-fcdcc6b7c8e6/");
  const main = page.locator("main");
  await expect(main).not.toContainText("Westfield Mission");
  await expect(main).not.toContainText("Central European Section");
  await expect(main).toContainText("archival");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 906 evidence and public projection exclude credentials and protected fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("7762afb4-79b0-5397-ad08-1d0e4585fb89");
  expect(people).not.toContain("d9c58708-dafb-59be-9672-75cc92cbb656");
  expect(people).not.toContain("70b4f6cd-045b-5e2a-b194-535349668d27");
});

test("Batch 906 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 608,
    research_attempted_people: 13_789,
    verified_affiliation_people: 990,
    verified_employer_people: 447,
    archival_review_assessed_people: 12_260,
    published_claims: 8_423,
    public_sources: 5_625,
  });
});
