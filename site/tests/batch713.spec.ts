import { expect, test } from "@playwright/test";

const profiles = [
  ["7d95f3f8-0360-5a17-8c08-1dc61ea872e0", "Joseph P Obuckley"],
  ["fc8d882c-7344-5547-9e79-ecabaff9ee84", "Elvera A Obusen"],
  ["864538f2-12c9-58ac-9dc0-f34006ac0b25", "Joseph F Ochnat"],
  ["365e5b7c-2aac-59a3-bd5b-18ad359c205a", "Joseph S Ochranek"],
  ["94a59f88-05e6-5dc3-b920-42bef32ef74b", "Blanche Oconnell"],
  ["517a5d9d-d610-5d14-8d85-48674c83c325", "Daniel J Oconnell"],
  ["15c36921-39f8-50b2-a0f2-b97920b4a0d5", "James L Oconnell"],
  ["7f07d6dd-4bb0-5970-af12-a9f7ee736ddc", "Peter R Oconnell"],
  ["34cdf085-875d-5708-8a35-b603cf016489", "Edward V Oconnor"],
  ["2332e9f0-5855-528b-b27e-8eea50b1f5d6", "Evelyn F Oconnor"],
  ["d8748527-cbbd-52e5-9d63-5b2c28e08d70", "John A Oconnor"],
  ["28b22932-80fb-52b2-b933-d9ff78eb1186", "Joseph A Oconnor"],
  ["7937e743-492d-5d36-b618-df8cff99982c", "Raymond R Oconnor"],
  ["98277239-aeb3-5cec-8996-ba5dcae55162", "Robert C Oconnor"],
  ["44d6bc85-ab48-5d31-87e2-d0aa2709d71a", "Vincent Oconnor"],
  ["b59c8731-6e90-5845-9f50-80ef38dce6a5", "William F Oconnor"],
  ["7932ac0e-b256-52ec-90da-fa1dd8fe92b8", "James G Oconor"],
  ["eccc8f25-7ae0-5acd-a069-4b974f2c1c3c", "Miyoji Oda"],
  ["121df7ce-e69c-5858-ba2e-f1519903167f", "Gabriel Odalovich"],
  ["028a8bc0-8b5c-5157-9a39-62c7c3fb21dd", "Joseph J Oddo"],
  ["42f2b3d0-7b9d-595a-958c-f0f3ba2e48fd", "John A Odea"],
  ["7c6a0a4a-8430-5344-b608-9a0d70d7c2bf", "William K Odell"],
  ["5a6b917e-fe32-5c71-bb87-806e3404e619", "John F Odeneal"],
] as const;

test("Batch 713 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^\d{4,8}$/);
  }
});

test("Batch 713 publishes reviewed Army identities without inventing employers", async ({ page }) => {
  for (const id of [
    "365e5b7c-2aac-59a3-bd5b-18ad359c205a",
    "517a5d9d-d610-5d14-8d85-48674c83c325",
    "d8748527-cbbd-52e5-9d63-5b2c28e08d70",
    "028a8bc0-8b5c-5157-9a39-62c7c3fb21dd",
    "7c6a0a4a-8430-5344-b608-9a0d70d7c2bf",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 713 preserves the Ochnat and OCHWAT identity conflict", async ({ page }) => {
  await page.goto("./people/864538f2-12c9-58ac-9dc0-f34006ac0b25/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("OCHWAT");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("do not merge");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Batch 713 publishes Miyoji Oda's identity context without inventing employment", async ({ page }) => {
  await page.goto("./people/eccc8f25-7ae0-5acd-a069-4b974f2c1c3c/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Evacuee roster");
  await expect(main).toContainText("Miyoji Oda Obituary");
  await expect(main).toContainText("Frank, Kazume, and Lillian");
  await expect(main).toContainText("does not identify an employer");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 713 visibly qualifies Gabriel Odalovich's probable identity", async ({ page }) => {
  await page.goto("./people/121df7ce-e69c-5858-ba2e-f1519903167f/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("probably the World War II Army first lieutenant");
  await expect(main).toContainText("medium D correlative or secondary");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 713 keeps unbridged student and obituary leads unresolved", async ({ page }) => {
  for (const id of [
    "5a6b917e-fe32-5c71-bb87-806e3404e619",
    "2332e9f0-5855-528b-b27e-8eea50b1f5d6",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusunresolved");
    await expect(main).toContainText("no reliable result after protocol");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Batch 713 publishes exact rebuilt coverage and preserves the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,437");
  await expect(main).toContainText("39.42%");
  await expect(main).toContainText("14,497");
  await expect(main).toContainText("720");
  await expect(main).toContainText("325");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
