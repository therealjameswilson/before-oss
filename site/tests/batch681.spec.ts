import { expect, test } from "@playwright/test";

const profiles = [
  ["ef2a3cbd-b171-5e28-96e4-467e89cc1e24", "Thomas T Morrison"],
  ["335c3553-b0e9-5c76-94f5-b3a88dfbfea8", "William D Morrison"],
  ["502cdece-efbd-5204-a028-13c6e939299d", "Edward F Morrissey"],
  ["eba0c8df-f5a2-5c5f-a68e-6e6e90a24782", "Robert H Morrissey"],
  ["a6cf28c3-7a26-50d3-81d4-90ec2d57974d", "Billie J Morrone"],
  ["bc4f2425-a2b6-5ad0-bb9f-dfa2d70d96c7", "John E Morrone"],
  ["58beeece-93b2-5189-9abc-0c6915cbc4dc", "Archie G Morrow"],
  ["d8d09e1d-4e35-58f1-bcf4-1024479880b6", "Charlie B Morrow"],
  ["7a7092a2-67b3-5f69-9784-f11fdd2fba10", "Lloyd J Morrow"],
  ["025318bc-bb51-5ebd-9d13-fb4c728dbfa8", "Chandler Morse"],
  ["f7c38468-5108-5e2d-95e5-6165f6cb0e87", "Charles E Morse"],
  ["62b3e35b-63f9-506c-bb3f-c3b59b8a4446", "George P Morse"],
  ["72a41733-b7cd-5884-9a12-6232de1532d8", "Harlie P Morse"],
  ["d632456e-aca2-5700-b5c7-6de2c69111d9", "Richard Morse"],
  ["10a4d8bb-110f-52a2-a1d7-6d16b1b97867", "Roberta H Morse"],
  ["9b6dbd1b-c127-5a20-a219-bd2e612047d1", "Don E Mort"],
  ["35f76dd6-dac1-5a83-b304-bd734b051b5d", "Derek G Mortlock"],
  ["99f74d72-be36-58aa-b0dc-2f566d140a27", "Guy Mortner"],
  ["733f6727-eb28-5eda-bb8e-baf256ef2785", "Arlo G Morton"],
  ["12715f08-4cb1-5b74-b7f8-27a9e5502ae2", "Dorothy V Morton"],
  ["284c9e1b-dfb3-54b4-bc60-e551648d50d2", "Melvin S Morton"],
  ["f7655acf-75e9-5fbc-81de-cb0c9d4fc47a", "William G Morwood"],
  ["f31949e9-5456-5621-b9df-97d87e650b56", "William G Morwood"],
] as const;

test("Batch 681 publishes all 23 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 331");
    await expect(page.locator("main")).toContainText("Archive box");
    await expect(page.locator("main")).toContainText("540");
  }
});

test("Batch 681 preserves Chandler Morse's prior Federal Reserve findings", async ({ page }) => {
  await page.goto("./people/025318bc-bb51-5ebd-9d13-fb4c728dbfa8/");
  const main = page.locator("main");
  await expect(main).toContainText("Board of Governors of the Federal Reserve System");
  await expect(main).toContainText("Federal Reserve Bank of New York");
  await expect(main).toContainText("verified employer found");
});

test("Batch 681 distinguishes Richard Morse's student status from employment", async ({ page }) => {
  await page.goto("./people/d632456e-aca2-5700-b5c7-6de2c69111d9/");
  const main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Dartmouth College");
  await expect(main).toContainText("Class of 1944 student");
  await expect(main).toContainText("OSS liaison in Burma");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("Dartmouth College");
});

test("Batch 681 publishes Don Mort's Army pathway and occupation without inventing an employer", async ({ page }) => {
  await page.goto("./people/9b6dbd1b-c127-5a20-a219-bd2e612047d1/");
  const main = page.locator("main");
  await expect(main).toContainText("confirmed");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("salesman");
  await expect(main).toContainText("employer is not named");
  await expect(main).toContainText("Office of Strategic Services personnel review board proceedings, Caserta");
});

test("Batch 681 preserves the two Morwood rows and publishes only the supported enlisted-row claims", async ({ page }) => {
  await page.goto("./people/f31949e9-5456-5621-b9df-97d87e650b56/");
  let main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("radio writer");
  await expect(main).toContainText("Army conscript transferred to OSS Morale Operations");
  await expect(main).toContainText("Radio Warfare: OSS and CIA Subversive Propaganda");

  await page.goto("./people/f7655acf-75e9-5fbc-81de-cb0c9d4fc47a/");
  main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("identifiers differ");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 681 preserves protected-identifier spelling conflicts", async ({ page }) => {
  await page.goto("./people/72a41733-b7cd-5884-9a12-6232de1532d8/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Harlie B Morse");
  await expect(main).toContainText("Harlie P Morse");

  await page.goto("./people/284c9e1b-dfb3-54b4-bc60-e551648d50d2/");
  main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Melvin S Mooton");
  await expect(main).toContainText("Melvin S Morton");
});

test("Batch 681 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,714");
  await expect(page.locator("body")).toContainText("36.40%");
  await expect(page.locator("body")).toContainText("306");
  const category = page.locator("#oil-companies");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator(".oil-directory__person")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil companies");

  await page.goto("./people/");
  await expect(page.locator(".featured-directory-category li")).toHaveCount(8);
});
