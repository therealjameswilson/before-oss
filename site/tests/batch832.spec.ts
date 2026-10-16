import { expect, test } from "@playwright/test";

const profiles = [
  ["ef14ba8c-a150-5348-aed4-2383a6ca65d3", "Harriet W Sabine"],
  ["56870d3c-ea4b-5ad3-8ed3-a0101f98a1d7", "Knute Sabo"],
  ["99093191-560b-5fc0-9b5c-37567b74ffdb", "Stanley J Sabolepski"],
  ["5acbf66b-7afc-5fd7-9418-ba68733d313b", "Otto A Saborsky"],
  ["585906ec-7db5-5a86-a56e-4abb2c1dee9f", "Marco P Sabovich"],
  ["6cbfc521-0329-5f63-b355-0c7345ef8c7f", "Sarah C Sabow"],
  ["95274b81-09bf-59d6-b320-35464aed15f8", "William L Sachbe"],
  ["58471566-2651-592b-aee3-ef84d6c84925", "Alexander Sachs"],
  ["846b267f-fc04-50c5-9cdd-fb2bf687231d", "Bernard Sachs"],
  ["5b6c7ea4-eb42-51ed-a666-9c020eb90a17", "James B Sackrider"],
  ["ab7a1fdc-c857-5aea-82a5-3b5d44bf92dd", "Sara R Sacks"],
  ["04a47d76-0755-515d-b36f-8de50d4743f6", "Saul Sacks"],
  ["f03d4625-06f0-5615-9aa8-004724f497a0", "Henry R Sacrett"],
  ["43584b85-f88d-5e55-8b8e-b2fb13505a11", "Sushi M Sadi"],
  ["cb509dc8-a55a-5605-9427-9c05f6f338e6", "Mumir M Sadim"],
  ["878f41c6-c65e-5753-993c-29595b78e68b", "Ralph B Sadler"],
  ["f620ec11-1b93-562c-8e28-27c8cf2842b8", "Leo S Sadowski"],
  ["ec6b25a2-5990-53c9-b7bd-ad64ba3902fe", "Preston Saenz"],
  ["c1993509-02ba-5a77-9e4e-3917e93a667b", "Eugene H Saerchinger"],
  ["dc965089-2d9c-538d-8eaa-96001a5e06b2", "Jerry M Sage"],
  ["1ee54497-ec78-5e18-9dad-8e9a6fd17811", "William H Sage"],
  ["11142f01-020f-5fa5-a34b-d3e69fe83c03", "Philip Sagon"],
  ["7415bf93-9aeb-5988-9837-29c58f38ad5c", "George M Saharov"],
] as const;

test("Batch 832 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Alexander Sachs separates probable independent consulting from earlier Lehman employment", async ({ page }) => {
  await page.goto("./people/58471566-2651-592b-aee3-ef84d6c84925/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("documented prewar employer found");

  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("Self-employed");
  await expect(immediate).toContainText("independent economic consultant");
  await expect(immediate).toContainText("probable immediate");
  await expect(immediate).toContainText("medium");

  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("Self-employed");

  const earlier = page.getByRole("region", { name: "Earlier pre-OSS affiliations" });
  await expect(earlier).toContainText("Lehman Corporation");
  await expect(earlier).toContainText("vice-president");
  await expect(earlier).not.toContainText("Lehman Brothers");
});

test("George Saharov publishes documented ICC work without claiming an immediate transfer", async ({ page }) => {
  await page.goto("./people/7415bf93-9aeb-5988-9837-29c58f38ad5c/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Principal Transportation Economist, Office of Strategic Services");

  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("No reviewed claim currently meets the publication threshold");

  const earlier = page.getByRole("region", { name: "Earlier pre-OSS affiliations" });
  await expect(earlier).toContainText("Bureau of Transport Economics and Statistics");
  await expect(earlier).toContainText("associate economist");
  await expect(earlier).toContainText("government assignment");
});

test("Philip Sagon gains a confirmed identity and OSS bridge but no invented prewar employer", async ({ page }) => {
  await page.goto("./people/11142f01-020f-5fa5-a34b-d3e69fe83c03/");
  const main = page.locator("main");
  await expect(main).toContainText("Philip H. Sagon");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("working with OSS in 1943");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("real estate developer");
});

test("Bernard Sachs keeps the Army name conflict visible and out of affiliations", async ({ page }) => {
  await page.goto("./people/846b267f-fc04-50c5-9cdd-fb2bf687231d/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Sachs Gerhard");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(page.getByRole("region", { name: "Immediate pre-OSS affiliation" })).not.toContainText("Sachs Gerhard");
});

test("accepted Army identities publish no coded occupations or unmasked identifiers", async ({ page }) => {
  for (const id of [
    "99093191-560b-5fc0-9b5c-37567b74ffdb",
    "04a47d76-0755-515d-b36f-8de50d4743f6",
    "ec6b25a2-5990-53c9-b7bd-ad64ba3902fe",
    "11142f01-020f-5fa5-a34b-d3e69fe83c03",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/Official Army/i);
    await expect(main).not.toContainText("civilian occupation code");
  }
});

test("Jerry Sage's previously verified employer and military pathway survive the batch rebuild", async ({ page }) => {
  await page.goto("./people/dc965089-2d9c-538d-8eaa-96001a5e06b2/");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("Fort Lewis");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("Procter and Gamble");
  await expect(civilian).toContainText("Salesman");
  await expect(civilian).toContainText("United States West Coast");
  await expect(civilian).toContainText("salesman in fall 1941");
});
