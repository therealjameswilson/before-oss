import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page449-sties-to-stiteler-review_batch-918_2026-10-26.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["83ba9d62-be87-58db-a413-32ea6067119d", "Bernard J Sties"],
  ["0f3d9b46-82b1-50bf-9335-82670357e0e8", "Meredith R Stiff"],
  ["baf96760-6a9a-5da5-8df8-e74e39e3a26a", "Gus Stikas"],
  ["6e859c75-0d49-53b3-8e88-ff08d7815a99", "Lois Stiles"],
  ["1e2d4f78-aeb2-5d05-b569-c054c17e49e5", "Ralph S Stillman"],
  ["65089006-e3b3-51ad-b130-692b819c7785", "William R Stillman"],
  ["0369edcc-6ea0-5d1b-82e1-40f865ec2ddf", "Marjorie Stillwell"],
  ["9c2b9bfd-5779-513d-9ea1-767b0a3e3eee", "Robert E Stillwell"],
  ["687cac4b-9486-5a6b-854f-73d60e13a124", "Margaret H Stilp"],
  ["bc4158b8-1856-5a10-95f5-2a7649b1868a", "Stephen Stimac"],
  ["65832d1e-5925-5032-b521-82bc2c8e7765", "Bradford J Stimpson"],
  ["ee880962-8913-584f-a995-870b8ed7dd35", "Harry F Stimpson"],
  ["976a2b4e-f5c4-5a28-9e74-d41f601aaf99", "Clifford E Stine"],
  ["f4035a23-f465-5c33-bad6-2fd1bb5b2c9b", "Nell C Stine"],
  ["133893ce-2a7a-5315-861a-54e7835c797e", "Charter D Stinespring"],
  ["f5d6883b-b4c9-5ed6-a76f-56d5a7a4e583", "Harriet M Stinson"],
  ["b5511f96-d54c-53ac-8470-092ffc6ae178", "John D Stinson"],
  ["bd78e839-5810-58e3-966c-b568df05de0f", "Woodrow W Stinson"],
  ["22e12290-d309-5e85-9536-63ada21a7553", "Branko Stipanovic"],
  ["df379047-78b7-5d44-8768-b2283a02ef8d", "John A Stippick"],
  ["269bf631-b75d-5834-8c26-80873e2db234", "Mary J Stirling"],
  ["c33c4e2d-8049-5879-a798-e6b22af7ffa2", "Walter E Stirnus"],
  ["c68a60a4-f321-5373-b5be-7e11cd719867", "Leroy G Stiteler"],
] as const;

test("Batch 918 publishes all 23 people with saved outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 918 Army codes remain occupations rather than employers", async ({ page }) => {
  const cases = [
    ["83ba9d62-be87-58db-a413-32ea6067119d", "Clerks, general office"],
    ["baf96760-6a9a-5da5-8df8-e74e39e3a26a", "Sailors and deckhands"],
    ["65089006-e3b3-51ad-b130-692b819c7785", "Architects"],
    ["133893ce-2a7a-5315-861a-54e7835c797e", "Mechanics and repairmen"],
    ["b5511f96-d54c-53ac-8470-092ffc6ae178", "radios and phonographs"],
    ["c33c4e2d-8049-5879-a798-e6b22af7ffa2", "Linemen and servicemen"],
    ["c68a60a4-f321-5373-b5be-7e11cd719867", "Mechanics and repairmen"],
  ] as const;
  for (const [id, label] of cases) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText(label);
    await expect(main).toContainText("no employer is identified");
    await expect(main).toContainText("occupation only found");
  }
});

test("Bradford Stimpson keeps OCS training separate from an immediate OSS pathway", async ({ page }) => {
  await page.goto("./people/65832d1e-5925-5032-b521-82bc2c8e7765/");
  const main = page.locator("main");
  await expect(main).toContainText("Signal Corps Officer Candidate School");
  await expect(main).toContainText("21 June 1944");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Walter Stirnus shows the 86th Infantry assignment with visible temporal uncertainty", async ({ page }) => {
  await page.goto("./people/c33c4e2d-8049-5879-a798-e6b22af7ffa2/");
  const main = page.locator("main");
  await expect(main).toContainText("86th Infantry Regiment");
  await expect(main).toContainText("Headquarters company");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Robert Stillwell exposes the spelling conflict without transferring the disputed occupation", async ({ page }) => {
  await page.goto("./people/9c2b9bfd-5779-513d-9ea1-767b0a3e3eee/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Stilwell");
  await expect(main).not.toContainText("Managers and officials");
});

test("unbridged Harry Stimpson and Branko Stipanovic candidates remain private", async ({ page }) => {
  await page.goto("./people/ee880962-8913-584f-a995-870b8ed7dd35/");
  await expect(page.locator("main")).not.toContainText("Harry Farnum Stimpson");
  await expect(page.locator("main")).not.toContainText("Ambassador to Paraguay");

  await page.goto("./people/22e12290-d309-5e85-9536-63ada21a7553/");
  await expect(page.locator("main")).not.toContainText("Stipanovich");
  await expect(page.locator("main")).not.toContainText("deportation");
});

test("Batch 918 evidence excludes credentials and protected identifier fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 918 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 617,
    research_attempted_people: 14_063,
    verified_affiliation_people: 1_003,
    verified_employer_people: 451,
    archival_review_assessed_people: 12_536,
    published_claims: 8_622,
    public_sources: 5_727,
  });
});
