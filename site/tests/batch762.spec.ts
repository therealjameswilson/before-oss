import { expect, test } from "@playwright/test";

const profiles = [
  ["c0d6a6d0-06a6-5b91-af24-d416da53d374", "Vincent Pizutto"],
  ["31dea57e-4633-5320-a272-0f11aeae021e", "Alexander J Pizzi"],
  ["a13a9f4f-af49-5d7a-8411-8de35ce440c5", "John Pizzoferrato"],
  ["66998131-9d8c-5304-9bc7-238aac1dd226", "Frank R Pizzuto"],
  ["93a1f5a6-f2d9-5ab2-a4b1-d7001ec3873a", "Samuel J Pizzuto"],
  ["2a2535e9-8993-5d0e-a411-6aac0b048cd4", "Russell P Place"],
  ["2205dfae-272b-54ea-94f6-01c91539674a", "Lyle G Pladna"],
  ["81eb4830-773c-5610-88aa-eaf11331780e", "William G Plaetti"],
  ["47c21baa-6c8e-5d1c-a497-45dcedec2793", "Alfred D Plamondon"],
  ["3177bbf8-1643-5ef3-8fae-75c3a9dbc515", "Rade Plan"],
  ["bfb91646-ffae-597b-a959-92b424fbb74f", "Henry B Plant"],
  ["6c4448fc-1b89-5801-bfb2-d7ed73ad7bea", "Gerard A Plante"],
  ["7ffded6f-830a-5e53-9ddb-87d66e63f5ae", "Norman W Plantin"],
  ["30424d64-f6e7-5ea2-9eb3-59c67f5e7e56", "James J Platner"],
  ["78a2d9e4-0e2f-54f7-8e36-b4915b61d34d", "Frank P Platnick"],
  ["b929ab73-329e-57c2-991c-4f8b1ba49881", "Gardiner S Platt"],
  ["02134331-d853-5285-b6ab-026fcc8f3238", "Helen I Platt"],
  ["cbc37cbc-c880-546e-983b-3a75b1f182f3", "Robert S Platt"],
] as const;

test("Batch 762 publishes all 18 page-371 profiles with attempted outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 762 keeps Rade Plan's qualified battalion affiliation separate from employment", async ({
  page,
}) => {
  await page.goto("./people/3177bbf8-1643-5ef3-8fae-75c3a9dbc515/");
  const main = page.locator("main");
  await expect(main).toContainText("Robert Perry");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Yugoslav Battalion at Haifa");
  await expect(earlier).toContainText("military assignment");
  await expect(earlier).toContainText("documented pre-OSS");
  await expect(earlier).toContainText("medium");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "Yugoslav Battalion",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "Yugoslav Battalion",
  );
});

test("Batch 762 uses Gardiner Platt's OSS memorandum for identity only", async ({ page }) => {
  await page.goto("./people/b929ab73-329e-57c2-991c-4f8b1ba49881/");
  const main = page.locator("main");
  await expect(main).toContainText("31 May 1944");
  await expect(main).toContainText("Memorandum from Gardiner S. Platt to Margaret Crossby");
  await expect(main).toContainText("does not establish a pre-OSS employer or affiliation");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "JICAME",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "JICAME",
  );
});

test("Batch 762 exposes Plaetti's spelling conflict without transferring Army metadata", async ({
  page,
}) => {
  await page.goto("./people/81eb4830-773c-5610-88aa-eaf11331780e/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Paletti");
  await expect(main).toContainText("shared by a separate");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "United States Army",
  );
});

test("Batch 762 withholds Robert Swanton Platt's biography without an OSS bridge", async ({ page }) => {
  await page.goto("./people/cbc37cbc-c880-546e-983b-3a75b1f182f3/");
  const main = page.locator("main");
  await expect(main).toContainText("Robert Swanton Platt");
  await expect(main).toContainText("not assigned to this row");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "University of Chicago",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "University of Chicago",
  );
});

test("home page exposes the rebuilt Batch 762 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,526");
  await expect(home).toContainText("43.97%");
  await expect(home).toContainText("13,408");
  await expect(home).toContainText("781");
  await expect(home).toContainText("345");
  await expect(home).toContainText("8,984");
});
