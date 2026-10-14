import { expect, test } from "@playwright/test";

const profiles = [
  ["27bdfa6b-1365-59e8-8842-e2d6fb6ca6d2", "Lesta L Reid"],
  ["77e608a1-7024-57d9-b362-6033ec765929", "Lucille M Reid"],
  ["96f941b9-76c9-5208-9710-be9b746993bc", "Marne F Reid"],
  ["5d2a1bf7-676b-5095-85d3-45154f96d55b", "Peter C Reid"],
  ["3c5b0879-dcf9-5c66-93e2-ef48b8f65294", "Roberta J Reid"],
  ["0a2419a2-0950-57e7-a5cc-b9d90ad7c8fb", "William S Reid"],
  ["ad3e134f-5d6e-5269-b7a5-7c509723a637", "James A Reidler Jr"],
  ["78c18952-e390-5e9e-a768-32597801a8ee", "Joseph P Reidy"],
  ["4937579f-fd54-5065-8968-38d6ccc356b4", "Michael J Reidy"],
  ["4d3e38b0-16a3-5d5e-91f4-c639a0501bcd", "Bertram Reifkind"],
  ["a745c018-dbd0-5c30-ad4a-63605b4bf09e", "Alfred Reifman"],
  ["ce8364cb-7f71-505c-ad3e-3be3d33a633a", "John Reifsnider"],
  ["b595965d-6e7d-56b7-a6e1-ce614c899e0c", "Anita R Reilly"],
  ["9e4c26b6-adc1-5618-9043-61e537ba63a7", "Gordon E Reilly"],
  ["d981e049-ef1a-5758-8db1-5661cc6d9855", "John J Reilly"],
  ["f7ede111-2316-5a19-a624-6e6a13d5044a", "Judith C Reilly"],
  ["f4500db2-4f57-5eb1-bcf7-8c59bf228430", "Richard W Reilly"],
  ["5f882024-0544-5ba4-8c3a-94c81a6eb9f7", "Richard K Reilly"],
  ["413ae270-07a2-5514-a325-a3d2bcae6b81", "George Reim"],
  ["ad6cef91-9e40-5487-945c-fdc59707be55", "Charles F Reimer"],
  ["6f0b0337-c5b5-5b47-9e7f-cc121b7838af", "Clarence Reimer"],
  ["2d088f97-b8ee-5501-a049-dae7616d009b", "William W Rein"],
  ["3f670b02-37a6-5b2e-b674-aa83d17fe9ae", "Albert C Reinert"],
] as const;

const officialIdentityProfiles = [
  "96f941b9-76c9-5208-9710-be9b746993bc",
  "4d3e38b0-16a3-5d5e-91f4-c639a0501bcd",
  "9e4c26b6-adc1-5618-9043-61e537ba63a7",
  "f4500db2-4f57-5eb1-bcf7-8c59bf228430",
  "413ae270-07a2-5514-a325-a3d2bcae6b81",
  "ad6cef91-9e40-5487-945c-fdc59707be55",
] as const;

test("Batch 795 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 795 publishes six official identity claims without inventing employers", async ({ page }) => {
  for (const id of officialIdentityProfiles) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("Official Army bulk data supports a high-confidence identification");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Reifman publishes the OPA-to-Army-to-OSS chronology with official citations", async ({ page }) => {
  await page.goto("./people/a745c018-dbd0-5c30-ad4a-63605b4bf09e/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "United States Army",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "United States Office of Price Administration",
  );
  await expect(main).toContainText("economist");
  await expect(main).toContainText("Congressional Record - Senate, March 12, 1948");
  await expect(main).toContainText("possible duplicate");
});

test("Batch 795 keeps the Richard K Reilly name conflict explicit and employer-free", async ({ page }) => {
  await page.goto("./people/5f882024-0544-5ba4-8c3a-94c81a6eb9f7/");
  const main = page.locator("main");
  await expect(main).toContainText("REILLY ROBERT K");
  await expect(main).toContainText("conflict");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("home page exposes the rebuilt Batch 795 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,278");
  await expect(home).toContainText("47.11%");
  await expect(home).toContainText("12,656");
  await expect(home).toContainText("811");
  await expect(home).toContainText("365");
  await expect(home).toContainText("9,739");
});
