import fs from "node:fs";
import { expect, test } from "@playwright/test";

const evidence = fs.readFileSync(
  new URL(
    "../../research/evidence-page431-skurla-sliwa-review_batch-883_2026-10-17.json",
    import.meta.url,
  ),
  "utf8",
);

const profiles = [
  ["ed5c9c81-5774-5ff2-9df9-87858fe6bd82", "Peter J Skurla"],
  ["8ea177c3-2dc8-5d40-ad65-c4334de3d86b", "Joseph K Slabicki"],
  ["d4137a23-bf8c-54c2-848e-e36f3b571065", "Stanley J Slabik"],
  ["7e854378-9d81-55b7-b9c8-863b50f2b83a", "Earl H Slack"],
  ["393cb3f0-bd75-59ed-8ccd-4ea9a88eb010", "Harold H Slack"],
  ["89f18c27-1fe5-54b0-9e2a-f04d649b93e7", "Gertrude W Sladek"],
  ["f2938355-fcc6-5e91-9477-575ad7a22679", "Robert R Slager"],
  ["ff805271-2f98-5608-b4b6-4f6acbd31e9e", "William A Slagg"],
  ["65443bbd-e027-596b-9dde-a61ea7159e5d", "Rudolph Slapansky"],
  ["79bec99d-7879-5af2-9e3c-aadedc195c61", "Katherine J Slappey"],
  ["44941947-727e-5221-9c91-721392070acd", "Wanda G Slasko"],
  ["20ea3494-d13a-517d-bd51-2d78b9c63dd9", "Alden V Slattengren"],
  ["54aef596-d6dd-5d6c-a68b-56fb8bbfec99", "Michael Slauta"],
  ["8d6ee918-1785-52d7-9d9f-9f416366fce9", "Robert K Slaven"],
  ["90a1faf2-42e6-54cd-adc4-c995d19c6518", "Joseph W Slavin"],
  ["7e7e63aa-d5f2-59c3-8b13-6c5e02c02f98", "Michael Slavin"],
  ["cc68b3b3-eeb2-54d1-9b4a-e9fadafd7822", "Margaret K Sleder"],
  ["ea6782e3-b3f8-5ea8-8c9a-7ed13e17a1f6", "Edward L Slepicka"],
  ["13b5be3d-5b16-54e7-8246-78c5e3993e8c", "Andrew J Slesicki"],
  ["808dcc28-b85e-5ae8-8eb3-716f8c771480", "Conrad H Sletta"],
  ["06741f14-79c5-5ccc-b63a-35b06059609b", "Robert L Sliker"],
  ["bace80ac-fc62-5347-9ff0-8152a36c48fa", "George S Slining"],
  ["332c40e2-03c3-5d12-9c2b-5d992536408e", "Edward Sliwa"],
] as const;

test("Batch 883 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
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

test("Batch 883 publishes Sladek's Library of Congress work as the documented employer", async ({ page }) => {
  await page.goto("./people/89f18c27-1fe5-54b0-9e2a-f04d649b93e7/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Library of Congress",
  );
  const civilian = main.locator("section[aria-labelledby='civilian-employer']");
  await expect(civilian).toContainText("Czechoslovak specialist");
  await expect(civilian).toContainText("probable immediate");
  await expect(civilian).toContainText("high");
});

test("Batch 883 keeps Skurla's education and Navy evidence qualified", async ({ page }) => {
  await page.goto("./people/ed5c9c81-5774-5ff2-9df9-87858fe6bd82/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Newark College of Engineering");
  await expect(earlier).toContainText("United States Navy");
  await expect(earlier).toContainText("student");
  await expect(earlier).toContainText("military assignment");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 883 identifies Slauta as a commissioned Army officer without backdating his assignment", async ({ page }) => {
  await page.goto("./people/54aef596-d6dd-5d6c-a68b-56fb8bbfec99/");
  const main = page.locator("main");
  await expect(main).toContainText("commissioned army officer");
  await expect(main).toContainText("Commissioned officerYes");
  await expect(main).toContainText("Quartermaster specialist");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "No reviewed claim currently meets the publication threshold",
  );
});

test("Batch 883 labels Sletta's school evidence as student status, not employment", async ({ page }) => {
  await page.goto("./people/808dcc28-b85e-5ae8-8eb3-716f8c771480/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("St. James High School");
  await expect(earlier).toContainText("Student");
  await expect(earlier).toContainText("student");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 883 evidence bundle excludes private identifiers and credentials", () => {
  expect(evidence).not.toMatch(/"serial_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toMatch(/"service_number(?:_raw|_normalized)?"/);
  expect(evidence).not.toContain("NARA_API_KEY");
  expect(evidence).not.toContain("x-api-key");
});

test("Batch 883 publishes its exact coverage counters", async ({ request }) => {
  const response = await request.get("./data/stats.json");
  expect(response.ok()).toBeTruthy();
  const stats = await response.json();
  expect(stats).toMatchObject({
    source_rows: 23_978,
    person_entities: 23_937,
    possible_duplicate_groups: 585,
    research_attempted_people: 13_271,
    verified_affiliation_people: 962,
    verified_employer_people: 434,
    archival_review_assessed_people: 11_738,
    published_claims: 8_026,
    public_sources: 5_433,
  });
});
