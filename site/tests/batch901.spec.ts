import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page440-spence-to-sperling-review_batch-901_2026-10-25.json",
    import.meta.url,
  ),
  "utf8",
);

const people = fs.readFileSync(
  new URL("../src/data/generated/people.json", import.meta.url),
  "utf8",
);

const profiles = [
  ["22d683f2-1f51-5f72-bd72-6c32c48b325c", "Marion J Spence"],
  ["f10bbf26-3c73-5a67-bdef-a4d2031e6a11", "Barbara Spencer"],
  ["04e3c400-20f0-5310-8a53-13861ee5852c", "Deforest Spencer"],
  ["64a557ab-4806-578a-8cf9-7dcbe16d8f5e", "Dorothy M Spencer"],
  ["12d9239d-bfc4-54ac-9dea-c52c45a0a08d", "Douglas Spencer"],
  ["cd4cefc2-85f7-5b72-b512-7ab4630ecc85", "F A Spencer"],
  ["0aee7f4e-25fa-554d-ade5-3adae58fae59", "Floyd A Spencer"],
  ["c1d34e5d-03a2-5c25-a727-51d76d1da055", "Francis G Spencer"],
  ["1d7db4a2-d24b-5d93-8407-2c7e46fd0161", "Frank C Spencer"],
  ["cfbace4a-ab61-5db8-bd53-0624906d5b64", "Frank B Spencer"],
  ["d54593fb-3737-5c08-bd00-cd0db0a3ded0", "Frederick A Spencer"],
  ["c965acc6-eea1-5d31-9165-4875cde97520", "James D Spencer"],
  ["33eeca2a-bc78-591e-9820-1b8b45c3b415", "James A Spencer"],
  ["eeef63b2-e307-5c6b-8197-8a3b2c3edd71", "Joseph E Spencer"],
  ["cf325764-5e3e-519f-bc0d-8d8b62550bca", "Alphonse G Spera"],
  ["c0d3ce41-37b3-5f38-a560-6f0cfd7e1658", "Edmond Speraber"],
  ["bbd9eabc-f647-53d3-b725-02603c3f5ce4", "Sam G Speranza"],
  ["2b062f8b-e7fa-55b9-a4b5-9886e7dcb970", "Joseph Sperli"],
  ["3f149a8a-c316-5285-919a-d6de772bc833", "Anton E Sperling"],
  ["cfb993f1-85e2-5a55-bd98-57d8fcf9defc", "Harry G Sperling"],
  ["0d333e9e-e785-5e69-94af-8f0c4b72cb3b", "Harry G Sperling"],
  ["7836eecd-c4d8-5d41-b89c-6335b0180b0a", "Jerome Sperling"],
] as const;

test("Batch 901 publishes all 22 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Batch 901 Army bridges remain qualified occupations or student status", async ({ page }) => {
  const checks = [
    ["1d7db4a2-d24b-5d93-8407-2c7e46fd0161", "Foremen, manufacturing"],
    ["cfbace4a-ab61-5db8-bd53-0624906d5b64", "Bookkeepers and cashiers"],
    ["33eeca2a-bc78-591e-9820-1b8b45c3b415", "Student; institution not recorded"],
    ["2b062f8b-e7fa-55b9-a4b5-9886e7dcb970", "Chauffeurs and drivers"],
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

test("Deforest Spencer keeps both source rows and one cautious entity", async ({ page }) => {
  await page.goto("./people/04e3c400-20f0-5310-8a53-13861ee5852c/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Box731");
  await expect(main).toContainText("Box732");
  await expect(main).toContainText("two separately printed");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Edmond Speraber separates medical practice, military service, and network work", async ({ page }) => {
  await page.goto("./people/c0d3ce41-37b3-5f38-a560-6f0cfd7e1658/");
  const main = page.locator("main");
  await expect(main).toContainText("Edmond Charles Speraber");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Self-employed medical practice",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Self-employed medical practice",
  );
  await expect(main).toContainText("French Army Health Service");
  await expect(main).toContainText("Comète, Margot and Nivelle");
  await expect(main).toContainText("probable immediate");
});

test("Jerome Sperling publishes Yale while keeping immediacy qualified", async ({ page }) => {
  await page.goto("./people/7836eecd-c4d8-5d41-b89c-6335b0180b0a/");
  const main = page.locator("main");
  await expect(main).toContainText("Jerome W. Sperling");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Yale University",
  );
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Yale University",
  );
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("Greek Desk");
});

test("same-name Harry Sperling rows remain separate and gallery evidence stays withheld", async ({ page }) => {
  await page.goto("./people/cfb993f1-85e2-5a55-bd98-57d8fcf9defc/");
  let main = page.locator("main");
  await expect(main).toContainText("identity review");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main.getByRole("link", { name: "F. Kleinberger Galleries" })).toHaveCount(0);

  await page.goto("./people/0d333e9e-e785-5e69-94af-8f0c4b72cb3b/");
  main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("source name is damaged");
  await expect(main).not.toContainText("Artists, sculptors, and teachers of art");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(main.getByRole("link", { name: "F. Kleinberger Galleries" })).toHaveCount(0);
  await expect(main).not.toContainText("same-name:harry-g-sperling-page440");
});

test("Douglas Spencer candidate stays withheld", async ({ page }) => {
  await page.goto("./people/12d9239d-bfc4-54ac-9dea-c52c45a0a08d/");
  const main = page.locator("main");
  await expect(main).toContainText("identity review");
  await expect(main).not.toContainText("OSS Assessment Staff");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 901 evidence and public projection exclude credential fields", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
  expect(people).not.toContain("same-name:harry-g-sperling-page440");
});

test("Batch 901 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_936,
    possible_duplicate_groups: 604,
    research_attempted_people: 13_679,
    verified_affiliation_people: 981,
    verified_employer_people: 442,
    archival_review_assessed_people: 12_150,
    published_claims: 8_315,
    public_sources: 5_571,
  });
});
