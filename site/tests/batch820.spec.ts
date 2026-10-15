import { expect, test } from "@playwright/test";

const profiles = [
  ["66e93f9b-b64b-5dce-83a1-41ce4741c43d", "Ronald E Rosen"],
  ["27e7f5c2-4c62-5d83-88af-b5e10554bff9", "James N Rosenau"],
  ["d073cf51-db2d-5128-8e40-7e879dfee282", "Joseph H Rosenbaum"],
  ["2ac28e2f-ead0-57ba-a7ad-fa6b02be0634", "Benjamin Rosenberg"],
  ["078343e0-c08a-50cd-831a-9da05cdd6d5c", "Clarence R Rosenberg"],
  ["283c0fd9-eb31-5cd3-96ea-faa2a71b239d", "Elsif Rosenberg"],
  ["5fa32809-9057-5c6b-9e33-ff687e907dfb", "Irwin M Rosenberg"],
  ["6bd8cbc2-b1dc-5ea3-893d-2dd552ee88c3", "Sam Rosenberg"],
  ["e6254c35-029d-5883-b7b1-b634b4b97358", "Shirley Rosenberg"],
  ["37b4e905-46ca-51fd-a825-fab0c927657e", "Arthur J Rosenblatt"],
  ["5e9bbe70-8a45-565c-a75f-76dead276389", "Eliott H Rosenblatt"],
  ["8b3e2e7a-88af-5e0c-8275-ab4193535698", "Shirley S Rosenblatt"],
  ["c77e4fa2-e89c-5abf-88c2-346bfd29bfaa", "William A Rosenborough"],
  ["661d4acc-07f4-510c-a3fa-b2bcb4502ecd", "Sven H Rosendahl"],
  ["b70b4e83-a9f3-515d-ba20-17ad23096436", "Julius A Rosenfeld"],
  ["de0f55b5-b68d-5087-ad1d-0d79b29b1284", "Meriam H Rosenfeld"],
  ["dcab81d6-f1e8-5a0a-be10-34d9577f0dac", "Miria S Rosenfeld"],
  ["4a18d10f-9c83-559d-9e13-11517f3029c3", "John M Rosenfield III"],
  ["135ca7c6-738e-5aee-a139-05000ed6a9d2", "Alfred Rosenhal"],
  ["53197b32-78f1-5a96-b36a-020d091c0800", "Elizabeth J Rosenheim"],
  ["3adec1bb-cefb-58be-ae87-bb5c0726dd83", "Martin P Rosenmeyer Jr."],
  ["c44beff8-db86-570b-9e58-67bdc91dc36b", "Frank L Rosenstock"],
  ["924fac44-ad0a-50ac-a728-bafc5522b228", "Alvin Rosenthal"],
] as const;

test("Batch 820 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("James Rosenau profile separates university study from the Army-to-OSS pathway", async ({ page }) => {
  await page.goto("./people/27e7f5c2-4c62-5d83-88af-b5e10554bff9/");
  const main = page.locator("main");
  await expect(main).toContainText("University of Wisconsin-Madison");
  await expect(main).toContainText("student");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("OSS cryptographer");
});

test("John Rosenfield profile preserves the full-name variant and qualifies the military-intelligence timing", async ({ page }) => {
  await page.goto("./people/4a18d10f-9c83-559d-9e13-11517f3029c3/");
  const main = page.locator("main");
  await expect(main).toContainText("John Max Rosenfield");
  await expect(main).toContainText("University of Texas at Austin");
  await expect(main).toContainText("U.S. Military Intelligence");
  await expect(main).toContainText("precise timing relative to OSS is uncertain");
});

test("Alfred Rosenhal profile keeps the indexed spelling while publishing the supported Rosenthal variant", async ({ page }) => {
  await page.goto("./people/135ca7c6-738e-5aee-a139-05000ed6a9d2/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Alfred Rosenhal", level: 1 })).toBeVisible();
  await expect(main).toContainText("Alfred Rosenthal");
  await expect(main).toContainText("reconnaissance battalion");
  await expect(main).toContainText("transferred to a secret O.S.S. training base");
});

test("Army identity-only matches do not become employer claims", async ({ page }) => {
  for (const id of [
    "37b4e905-46ca-51fd-a825-fab0c927657e",
    "5e9bbe70-8a45-565c-a75f-76dead276389",
    "661d4acc-07f4-510c-a3fa-b2bcb4502ecd",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("official Army bulk record");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Sam Rosenberg remains an unresolved archival-review case rather than an obituary namesake claim", async ({ page }) => {
  await page.goto("./people/6bd8cbc2-b1dc-5ea3-893d-2dd552ee88c3/");
  const main = page.locator("main");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("A plausible Samuel Rosenberg obituary mentions OSS photo-analysis and prewar theater work");
  await expect(main).not.toContainText("theater work immediately before OSS");
});
