import { expect, test } from "@playwright/test";

const profiles = [
  ["5a70e149-a0ec-5ef4-ab83-9adde0b10655", "William J Moriarity"],
  ["3b4e8457-bb19-515d-af43-19306afe4d7c", "Richard P Moriarty"],
  ["9a9cfc00-180e-5b77-9067-8b9a00363091", "Paul F Morillon"],
  ["45ceeb2d-f3db-536b-97b5-f39c6528a9fe", "Alfred J Morin"],
  ["c88f064a-aea4-51c6-8fcd-189312e6579d", "Fernand D Morin"],
  ["f9d5240f-799d-5f69-b192-dd4cd69b28fa", "Leo J Morin"],
  ["efb1de92-58ca-54d3-b334-356586fecfda", "Michele Morin"],
  ["1be5b581-dbb6-5564-9dec-92fea5998b26", "Roger J Morin"],
  ["ab63ade6-152e-5f39-9a6d-391a49c958fd", "Virgilio D Morini"],
  ["ca89973b-64ac-5fcf-8fac-fa3f97ca237d", "Mauriyio Moris"],
  ["2d9f450b-d17d-5033-a11d-f1696376f44f", "George Y Morishita"],
  ["12b41f06-ef56-50d6-bf60-c909b6e5a042", "Herve F Morisseau"],
  ["af9729df-ec25-5f8d-9984-7f76f73be2e6", "Miki Moriwaki"],
  ["7bcadd4c-d28c-5602-bf65-e5f689cb8158", "Per Morland"],
  ["20b460b5-3ec0-5c02-806f-1ec3c728e1b8", "Charles Morley"],
  ["68e6a7e5-7eb4-5f2e-9f47-71237ccd107a", "Brunnon E Mormand"],
  ["26843f5c-2c04-50de-a2b1-4e2f76cd6458", "George C Mormann"],
  ["032fe6f8-7ed4-5542-b6aa-364ce12bad3c", "Michele Moroni"],
  ["52c6fd51-dba0-5ba2-ba8d-ff2c8424ad79", "Panos Morphopoulos"],
  ["889872e3-7c1c-59f2-a268-dd62233f3332", "Mario T Morpurgo"],
  ["54760ccc-ac22-5c84-a735-c66666bbcf40", "Mario Morpurgo"],
  ["77ee4608-3cd3-5464-a292-00277d8d297e", "Glen E Morr"],
  ["86f67dd6-983f-57bd-b39e-6d6040ced040", "Doris J Morrell"],
] as const;

const highConfidenceArmyMatches = [
  ["3b4e8457-bb19-515d-af43-19306afe4d7c", "Richard P Moriarty", "••••7923"],
  ["45ceeb2d-f3db-536b-97b5-f39c6528a9fe", "Alfred J Morin", "••••5927"],
  ["f9d5240f-799d-5f69-b192-dd4cd69b28fa", "Leo J Morin", "••••8247"],
] as const;

test("Batch 679 publishes all 23 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 330");
    await expect(page.locator("main")).toContainText(/Archive box(538|539)/);
  }
});

test("Batch 679 publishes three high-confidence Army identities without employer inference", async ({ page }) => {
  for (const [id, name, maskedSerial] of highConfidenceArmyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText(maskedSerial);
    await expect(main).toContainText("coded occupation remain private");
  }
});

test("Batch 679 publishes Charles Morley's three qualified teaching affiliations", async ({ page }) => {
  await page.goto("./people/20b460b5-3ec0-5c02-806f-1ec3c728e1b8/");
  const main = page.locator("main");
  const immediateAffiliation = page.locator('section[aria-labelledby="immediate-affiliation"]');
  const civilianEmployer = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(main).toContainText("University of North Dakota");
  await expect(main).toContainText("University of Nebraska");
  await expect(main).toContainText("University of Wisconsin");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("American Historical Association");
  await expect(main).toContainText("The Ohio State University");
  await expect(immediateAffiliation).not.toContainText("University of North Dakota");
  await expect(civilianEmployer).not.toContainText("University of North Dakota");
});

test("Batch 679 qualifies Panos Morphopoulos without inventing an immediate employer", async ({ page }) => {
  await page.goto("./people/52c6fd51-dba0-5ba2-ba8d-ff2c8424ad79/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Johns Hopkins University");
  await expect(main).toContainText("Instructor in Romance Languages");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("Panos Paul Morphos");
  await expect(main).not.toContainText("Newsweek", { useInnerText: true });
});

test("Batch 679 keeps Miki Moriwaki's civilian-faculty record as a government assignment", async ({ page }) => {
  await page.goto("./people/af9729df-ec25-5f8d-9984-7f76f73be2e6/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("Military Intelligence Service Language School");
  await expect(main).toContainText("civilian faculty");
  await expect(main).toContainText("government assignment");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 679 preserves the Morisseau and Mormand identity conflicts", async ({ page }) => {
  await page.goto("./people/12b41f06-ef56-50d6-bf60-c909b6e5a042/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("JOSEPH H F");
  await expect(main).toContainText("Bryant University");
  await expect(main).toContainText("No reviewed claim currently meets the publication threshold");
  await expect(main).not.toContainText("Verified employer");

  await page.goto("./people/68e6a7e5-7eb4-5f2e-9f47-71237ccd107a/");
  main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Brunnon C Normand");
  await expect(main).toContainText("Boxes 539 and 563");
  await expect(main).toContainText("not merged");
});

test("Batch 679 keeps the two Mario Morpurgo records separate", async ({ page }) => {
  await page.goto("./people/889872e3-7c1c-59f2-a268-dd62233f3332/");
  let main = page.locator("main");
  await expect(main).toContainText("ambiguous");
  await expect(main).toContainText("T-3");
  await expect(main).toContainText("different protected identifiers and ranks");

  await page.goto("./people/54760ccc-ac22-5c84-a735-c66666bbcf40/");
  main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Mario Morpurgo", level: 1 })).toBeVisible();
  await expect(main).toContainText("2nd Lt");
  await expect(main).toContainText("different protected identifiers and ranks");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 679 publishes George Morishita as a qualified identity lead only", async ({ page }) => {
  await page.goto("./people/2d9f450b-d17d-5033-a11d-f1696376f44f/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("War Relocation Authority");
  await expect(main).toContainText("Minidoka");
  await expect(main).toContainText("requires archival review");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 679 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,669");
  await expect(page.locator("body")).toContainText("36.21%");
  await expect(page.locator("body")).toContainText("305");
  const category = page.locator("#oil-companies");
  await expect(category.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator(".oil-directory__person")).toHaveCount(8);
  await expect(category).toContainText("10 historically named oil companies");

  await page.goto("./people/");
  const directoryCategory = page.locator(".featured-directory-category");
  await expect(directoryCategory.locator("li")).toHaveCount(8);
});
