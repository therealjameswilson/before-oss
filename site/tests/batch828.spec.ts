import { expect, test } from "@playwright/test";

const profiles = [
  ["32d69e79-0bf5-512d-a55a-ed5baf00278c", "Arthur A Ruozzi"],
  ["dabe37ed-5431-5d7e-85d0-896bbda1b93c", "Horace E Rupert Jr."],
  ["36debe5a-effb-5fc2-ba77-9b8dce93d49a", "Norma Rupert"],
  ["eb15f8d4-fb73-5cf7-876f-fcd01623c799", "Elena V Ruperto"],
  ["f21f6853-e16b-53b7-a6f9-859d596ff94f", "Elva E Ruppel"],
  ["6a5e6344-b2bb-5b6a-8687-6dc7021888d6", "Lawrence V Ruppel"],
  ["f88b3402-5af2-5fcd-acc3-bc46f5eaeeaa", "Louis Ruppel"],
  ["9ab4c5b8-53f8-51da-a256-7f40606a6557", "Andrew L Ruscio"],
  ["abe3882d-93ab-555f-b0be-5446c3801782", "Peter J Ruscitti"],
  ["edde92d4-39e8-5b9e-a322-f4cf706158d7", "Tom Rusdal"],
  ["ebe9c595-df0a-51d7-920b-e90c527185e3", "Robert F Rushin"],
  ["8acc7c05-ae8a-538c-b697-0ea69b1b0c8f", "Andrew J Ruska"],
  ["efcff56c-988d-570b-891f-ec7efda93133", "Arthur J Russ Jr."],
  ["444aa25f-6b4a-5f21-b73c-f5802fb9cc73", "Aimee G Russell"],
  ["2ce253be-adc8-5d81-a989-9bda46953529", "Arthur J Russell Jr."],
  ["84ba941d-13de-5b50-837a-6a175d5d25f1", "Calvin J Russell"],
  ["f3cda5a8-8e8d-5b72-89f7-bc42795f7d5c", "Donald E Russell"],
  ["7671158f-0427-5fc5-9b52-48f70ac44d08", "Donald W Russell"],
  ["692a55d6-7627-50fb-91b9-e9a377e7e29b", "Harry E Russell"],
  ["1066b81a-a672-575e-a500-cbe2cb8468cd", "Hattie W Russell"],
  ["4d0244fb-13f1-5834-a6fe-1217b0c7c6ec", "James W Russell"],
  ["8da99e36-c0d6-5019-b307-1a206a4c9c13", "Janet Russell"],
  ["c8933575-5d23-52f0-a946-0af4e803479e", "John P Russell"],
] as const;

test("Batch 828 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Louis Ruppel profile separates Crowell-Collier employment from the Marine pathway", async ({ page }) => {
  await page.goto("./people/f88b3402-5af2-5fcd-acc3-bc46f5eaeeaa/");
  const main = page.locator("main");
  await expect(main).toContainText("commissioned marine corps officer");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("United States Marine Corps");
  await expect(immediate).toContainText("probable immediate");
  await expect(immediate).toContainText("medium");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("Crowell-Collier Publishing Company");
  await expect(civilian).toContainText("executive assistant to the president");
  await expect(civilian).not.toContainText("United States Marine Corps");
});

test("Robert Rushin profile publishes Home Insurance with official X-2 identity evidence", async ({ page }) => {
  await page.goto("./people/ebe9c595-df0a-51d7-920b-e90c527185e3/");
  const main = page.locator("main");
  await expect(main).toContainText("The Home Insurance Company");
  await expect(main).toContainText("head of Insurance Unit of X-2");
  await expect(main).toContainText("PDF page 108, printed page 81");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("probable immediate");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("executive");
});

test("Tom Rusdal profile preserves name variants and occupation-only limits", async ({ page }) => {
  await page.goto("./people/edde92d4-39e8-5b9e-a322-f4cf706158d7/");
  const main = page.locator("main");
  await expect(main).toContainText("Tosten Rusdal");
  await expect(main).toContainText("Torsten Rusdal");
  await expect(main).toContainText("Unit Rype");
  await expect(main).toContainText("tree topper");
  await expect(main).toContainText("occupation only found");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(civilian).not.toContainText("West Coast logging company");
});

test("accepted Army identities publish no private identifiers or coded occupations", async ({ page }) => {
  for (const id of [
    "32d69e79-0bf5-512d-a55a-ed5baf00278c",
    "6a5e6344-b2bb-5b6a-8687-6dc7021888d6",
    "9ab4c5b8-53f8-51da-a256-7f40606a6557",
    "efcff56c-988d-570b-891f-ec7efda93133",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/Official Army/i);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
    await expect(main).not.toContainText(/\b(?:105|350|736)\b/);
  }
});

test("three protected-identifier conflicts remain visible and unmerged", async ({ page }) => {
  for (const [id, conflictingName, box] of [
    ["dabe37ed-5431-5d7e-85d0-896bbda1b93c", "Oliver J. Headings", "Box 666"],
    ["f3cda5a8-8e8d-5b72-89f7-bc42795f7d5c", "Charles C. Smith", "Box 667"],
    ["7671158f-0427-5fc5-9b52-48f70ac44d08", "Donald N. Russell", "Box 667"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(conflictingName);
    await expect(main).toContainText(/rejected/i);
    await expect(main).toContainText("conflicting sources");
    await expect(main).toContainText(box);
  }
});
