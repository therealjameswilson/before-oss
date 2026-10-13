import { expect, test } from "@playwright/test";

const profiles = [
  ["deecbfca-3cd4-5dec-871c-390b9062c11c", "Murcil M Pittard"],
  ["6404f1c0-8e8a-59e5-8461-971339f91389", "Ernest M Pittaro"],
  ["0e749749-a597-5309-8cc1-f65012e10ba0", "Felicetta Pittaro"],
  ["e1b69548-c9ab-519f-ab70-01c52ce07be0", "Frank S Pittillo"],
  ["704a8b9e-5b76-5003-8e68-db25613e0f66", "Lawrence R Pitts"],
  ["f64eb36a-27d3-5524-9652-0049c4360763", "Lillian M Pitts"],
  ["987ea677-f6f7-5f17-8c46-1c789e7a607c", "Robert F Pitts"],
  ["481390c7-98b7-5f0f-81ca-e09644e147e6", "Otto G Pitz"],
  ["5d9c25ed-90a1-5c0f-8af1-69732d614f6c", "Donald W Pixley"],
  ["b6514aed-3c7c-5df8-bdf0-84286302edad", "James P Pizor"],
] as const;

test("Batch 761 publishes all ten page-370 profiles with attempted outcomes", async ({ page }) => {
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

test("Batch 761 publishes Pittard and Pittaro education as qualified earlier affiliations, never employment", async ({
  page,
}) => {
  for (const [id, organization] of [
    ["deecbfca-3cd4-5dec-871c-390b9062c11c", "Wake Forest College"],
    ["0e749749-a597-5309-8cc1-f65012e10ba0", "Hunter College"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
    await expect(earlier).toContainText(organization);
    await expect(earlier).toContainText("student");
    await expect(earlier).toContainText("documented pre-OSS");
    await expect(earlier).toContainText("medium");
    await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
      organization,
    );
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
      organization,
    );
  }
});

test("Batch 761 keeps Pizor's education separate from employment and identifies the correct OCS class", async ({
  page,
}) => {
  await page.goto("./people/b6514aed-3c7c-5df8-bdf0-84286302edad/");
  const main = page.locator("main");
  const earlier = main.locator("section[aria-labelledby='earlier-affiliations']");
  await expect(earlier).toContainText("Grove City College");
  await expect(earlier).toContainText("student");
  await expect(main).toContainText("class 8-42");
  await expect(main).toContainText("16 April 1942");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "Grove City College",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "Grove City College",
  );
});

test("Batch 761 uses Pitz's 1942 record for identity only", async ({ page }) => {
  await page.goto("./people/481390c7-98b7-5f0f-81ca-e09644e147e6/");
  const main = page.locator("main");
  await expect(main).toContainText("Otto Godfrey Pitz");
  await expect(main).toContainText("not treated as proof of a pre-OSS assignment");
  await expect(main).toContainText("Congressional Record, Senate confirmations");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "Coast Artillery",
  );
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toHaveCount(0);
});

test("Batch 761 exposes Robert Pitts's official-name conflict without transferring Army metadata", async ({
  page,
}) => {
  await page.goto("./people/987ea677-f6f7-5f17-8c46-1c789e7a607c/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Dovidio Alfonso");
  await expect(main).toContainText("Box 607");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText(
    "United States Army",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText(
    "United States Army",
  );
});

test("home page exposes the rebuilt Batch 761 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,508");
  await expect(home).toContainText("43.89%");
  await expect(home).toContainText("13,426");
  await expect(home).toContainText("781");
  await expect(home).toContainText("345");
  await expect(home).toContainText("8,966");
});
