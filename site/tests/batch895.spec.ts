import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page437-snyder-to-soha-review_batch-895_2026-10-18.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["a0eb56fc-94e0-5d7a-94d0-620cb727a61b", "Edwin N Snyder"],
  ["3de98a54-5732-59c6-b6b5-675e49475a74", "Fred R Snyder"],
  ["81846ed3-29e1-5a6a-9b7d-c91bff9e6105", "Horace Snyder"],
  ["c688e6ed-7a90-5040-b025-a560d83f814a", "Jacques F Snyder"],
  ["0d52f2fb-07cb-5351-9fef-b17b9f36a125", "John C Snyder"],
  ["79f26601-d2c7-587f-9751-674bd8810456", "John T Snyder"],
  ["b4bafedb-05f7-5804-9d4b-d55b5a88eb20", "Kinsley D Snyder"],
  ["0a9138af-4eeb-535f-a40f-27356379b953", "Mary J Snyder"],
  ["fc6928ae-ec6f-5fc8-92ae-158bbcedca2d", "Robert P Snyder"],
  ["dd583670-17a6-5fa3-9b22-9b61a0d1c0c5", "Robert M Snyder"],
  ["66ba5ebe-29d9-5d0e-b96d-0f32d9a03012", "William T Snyder"],
  ["e9ecdc74-486b-5081-b7e8-6f733753c4c8", "John N Soares"],
  ["725f8e08-fc9a-53ee-a009-1a103df5cf27", "Leonard F Soares"],
  ["64973a5c-cdd2-5fb4-bb7c-2580a953bcbb", "Franciszek Sobecki"],
  ["5cee0934-c05e-52df-afa4-1a7b4462b635", "Julian Sobiechowski"],
  ["f5db58ba-c46b-57dc-b190-6b3d79769c5c", "Amato D Soccorsy"],
  ["57200a17-49a2-506a-98b8-c979c6f8ae0f", "Gloria H Soderberg"],
  ["75b19183-870f-57e8-bf4e-9375b3d0825c", "M Soegihadji"],
  ["8d32f609-60a0-5dce-a87f-158e9509f57a", "Louis T Sofa"],
  ["09426597-aa08-5f50-8bae-68a0a068d0fb", "Heinrich C Soffner"],
  ["00262806-355a-5598-bce4-f1b49140ed5b", "Heirich C Soffner"],
  ["d014b325-de84-5e57-9b29-5be897a3f4b8", "Vincent J Sofiano"],
  ["56563af8-16d1-5c82-9893-320aaa316b5b", "John Soha"],
] as const;

test("Batch 895 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Jacques Snyder keeps his immediate Army path and earlier Canadian service distinct", async ({ page }) => {
  await page.goto("./people/c688e6ed-7a90-5040-b025-a560d83f814a/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "U.S. Army Air Corps language training school in Tennessee",
  );
  await expect(main).toContainText("French-language trainee");
  await expect(main).toContainText("Canadian armed forces");
  await expect(main).toContainText("Teachers (secondary school) and principals");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Franciszek Sobecki publishes direct OSS identity evidence without inventing a predecessor", async ({ page }) => {
  await page.goto("./people/64973a5c-cdd2-5fb4-bb7c-2580a953bcbb/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("Polish Army major");
  await expect(main).toContainText("contributed to OSS operations");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
});

test("Heinrich Soffner merges the Henry Sutton alias record but keeps the adjacent Heirich row separate", async ({ page }) => {
  await page.goto("./people/09426597-aa08-5f50-8bae-68a0a068d0fb/");
  const merged = page.locator("main");
  await expect(merged).toContainText("Henry C Sutton");
  await expect(merged).toContainText("Soffner, Heinrich C");
  await expect(merged).toContainText("Sutton, Henry C");
  await expect(merged).toContainText("••••1314");
  await expect(merged).not.toContainText("33751314");
  await expect(merged.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("U.S. Army");
  await expect(merged).toContainText("White Collar Workers Union");
  await expect(merged).toContainText("Austrian refugee organization in Paris");
  await expect(merged).toContainText("duplicate-4c5b2ae9d07d");

  await page.goto("./people/00262806-355a-5598-bce4-f1b49140ed5b/");
  const separate = page.locator("main");
  await expect(page.getByRole("heading", { name: "Heirich C Soffner", level: 1 })).toBeVisible();
  await expect(separate).toContainText("unresolved");
  await expect(separate).toContainText("duplicate-4c5b2ae9d07d");
  await expect(separate).not.toContainText("White Collar Workers Union");
});

test("Vincent Sofiano publishes the RAF pathway with its temporal limit", async ({ page }) => {
  await page.goto("./people/d014b325-de84-5e57-9b29-5be897a3f4b8/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Royal Air Force",
  );
  await expect(main).toContainText("Group Captain");
  await expect(main).toContainText("exact OSS attachment date is not supplied");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("John T Snyder does not inherit the rejected Carmon Donald candidate", async ({ page }) => {
  await page.goto("./people/79f26601-d2c7-587f-9751-674bd8810456/");
  const main = page.locator("main");
  await expect(main).toContainText("unresolved");
  await expect(main).toContainText("Carmon Donald F");
  await expect(main).toContainText("formally rejected");
  await expect(main).not.toContainText("Photographers");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 895 evidence and public projection exclude protected identifiers and credentials", () => {
  const people = fs.readFileSync(
    new URL("../src/data/generated/people.json", import.meta.url),
    "utf8",
  );
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("33751314");
  expect(people).not.toContain("8aab67c1-6776-594a-8670-80bb8d294fbc");
});

test("Batch 895 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 598,
    research_attempted_people: 13_542,
    verified_affiliation_people: 971,
    verified_employer_people: 436,
    archival_review_assessed_people: 12_013,
    published_claims: 8_197,
    public_sources: 5_511,
  });
});
