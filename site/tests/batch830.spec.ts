import { expect, test } from "@playwright/test";

const profiles = [
  ["121a018d-b374-5657-88ea-436e83850036", "William J Rust"],
  ["5bf62eb3-bbeb-51e1-b9bd-2c1e3431616a", "William G Ruthenberg"],
  ["91c647ca-5f7c-57c9-a277-422c351e3e00", "Arthur B Rutherford"],
  ["ba218889-8ac3-5ba7-b425-387dc60af1aa", "John P Rutherford"],
  ["94d8e3bd-5be4-5f8d-8478-85d8ad2676a5", "Katherine A Rutherford"],
  ["8ed80169-761b-5a6c-bc6b-b58d8b0ea8c5", "Winthrop Rutherford"],
  ["6adc74d3-b366-5b69-8d74-688aec98bea2", "Walter F Rutkowski"],
  ["f68bd20e-8604-5008-b2a4-463719e15889", "Homer T Rutledge"],
  ["bbcef610-f168-52e9-86bc-8307cbf70624", "John M Rutledge"],
  ["77c7d595-2bbd-5bec-8422-e8e12079261d", "Thomas W Rutter"],
  ["ad6606a2-f0b3-5fd7-93ed-1e0d6394d9e6", "David Rutzisky"],
  ["6f5cb9f0-943c-5891-ae29-4b31320d74ce", "Florence M Ruysellaere"],
  ["ae48bbd3-2e21-53a7-93a5-5d14a85fbd21", "Louis Ruzich"],
  ["8bd4962e-9e31-5bb0-84c2-b0a901e3d594", "Henry F Ruzza"],
  ["48b02af8-d6da-582e-9cc0-36fdcce4a3cb", "Vada T Ryal"],
  ["9ca3d993-1ce8-5cba-98c4-6cbf3c269039", "Andrew J Ryan"],
  ["55cf2123-620d-5e7a-9061-9fc249bbe796", "Daniel E Ryan"],
  ["f0157487-6555-5d5e-a7d6-cc6e73a4ff0f", "Ellis W Ryan"],
  ["e4750c09-febe-51c2-bd95-16db6804ec7a", "Frank T Ryan"],
  ["e2ec0d9c-fda5-5b57-b6aa-810a413e0a74", "Frederick L Ryan"],
  ["63769924-9d5a-5ea7-9137-17f68e753770", "Ingrid T Ryan"],
  ["0f668ce9-099c-5a31-b4cd-18dc5d2d335d", "James J Ryan"],
  ["9d72497f-b85e-549a-a655-dc4cfababbd5", "Joseph A Ryan"],
] as const;

test("Batch 830 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Ellis Ryan profile separates last civilian enterprise from immediate military pathway", async ({ page }) => {
  await page.goto("./people/f0157487-6555-5d5e-a7d6-cc6e73a4ff0f/");
  const main = page.locator("main");
  await expect(main).toContainText("verified employer found");
  await expect(main).toContainText("Ellis Wilson Ryan");

  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("United States Army Air Corps");
  await expect(immediate).toContainText("Randolph Field");
  await expect(immediate).toContainText("military assignment");
  await expect(immediate).not.toContainText("Toledo Ice House");

  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("Toledo Ice House");
  await expect(civilian).toContainText("self employment");
  await expect(civilian).not.toContainText("Army Air Corps");

  const earlier = page.getByRole("region", { name: "Earlier pre-OSS affiliations" });
  await expect(earlier).toContainText("W. F. Ryan Company");
  await expect(earlier).toContainText("Cleveland Arena");
});

test("Louis Ruzich profile preserves the Louie variant and qualifies prior Army service", async ({ page }) => {
  await page.goto("./people/ae48bbd3-2e21-53a7-93a5-5d14a85fbd21/");
  const main = page.locator("main");
  await expect(main).toContainText("Louie Ruzich");
  await expect(main).toContainText("OSS Detachment 101");
  await expect(main).toContainText("United States Army Corps of Engineers");
  await expect(main).toContainText("medium");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(civilian).not.toContainText("family farm");
});

test("Winthrop Rutherford and John Rutherford receive transparent service classifications", async ({ page }) => {
  await page.goto("./people/8ed80169-761b-5a6c-bc6b-b58d8b0ea8c5/");
  let main = page.locator("main");
  await expect(main).toContainText("commissioned marine corps officer");
  await expect(main).toContainText("Capt Winthrop Rutherford in Southern France");
  await expect(main).toContainText("high confidence");

  await page.goto("./people/ba218889-8ac3-5ba7-b425-387dc60af1aa/");
  main = page.locator("main");
  await expect(main).toContainText("commissioned naval officer");
  await expect(main).toContainText("LT NR");
  await expect(main).toContainText("requires archival review");
});

test("accepted Army identities publish no coded occupations or unmasked identifiers", async ({ page }) => {
  for (const id of [
    "121a018d-b374-5657-88ea-436e83850036",
    "ad6606a2-f0b3-5fd7-93ed-1e0d6394d9e6",
    "9ca3d993-1ce8-5cba-98c4-6cbf3c269039",
    "9d72497f-b85e-549a-a655-dc4cfababbd5",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/Official Army/i);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }
});
