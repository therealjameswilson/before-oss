import { expect, test } from "@playwright/test";

const profiles = [
  ["44bd38fb-05d7-5a94-a3f4-60f64e2f2d4d", "Gerard Petron"],
  ["f2fb6ba1-45bb-5faa-8dba-4fbb2488c8c8", "Edward S Petros"],
  ["bd31016c-22dd-5c52-95ed-bb6805ac9e81", "Dimitri Petrou"],
  ["6beb6b85-8918-583a-9751-3d43792e56fa", "Michael B Petrovich"],
  ["73a0cc22-2b1a-5e95-b2a4-467a4729269e", "Christ J Petrow"],
  ["cfbebe7e-a6af-574d-8a9f-e5ef10d28560", "Donato A. F. Petrucelli"],
  ["1416fc44-3e3b-5ebc-8544-99692e411049", "Anthony S Petrullo"],
  ["3903ccf4-6632-50fb-8439-19ae15af0352", "Charles E Petrullo"],
  ["3386a008-f2c3-539c-9a86-8610f64b5d95", "Vincenzo Petrullo"],
  ["61f05cdd-f6ad-5452-a451-64902cf4d5e1", "Alex J Petruska"],
  ["15da58dd-b2f5-50dc-bce3-76b8acd21e9a", "Kroger Pettengill"],
  ["08f286b0-5491-5d0e-a9fb-f7cb4be915a1", "Donald R Petterson"],
  ["78571719-2206-5a3b-a67b-c98f3085a793", "Thomas M Pettey"],
  ["84d01f1c-50e9-508d-84fe-51418808b22c", "William J Pettigrew"],
  ["7514c526-e614-5f0d-9915-041077ebac3e", "Charles W Pettit"],
  ["c4d8d53a-2576-5be6-bd03-45eafb31514d", "Paul H Pettit"],
  ["fd2c4ed7-4d9c-5287-9b69-3774642121fa", "Robert L Pettit"],
  ["5221e904-3b9d-5500-af88-65eb9b90f8e6", "Willard B Pettit"],
  ["10a699a1-bb34-5d3c-a5a4-8dda6f3fdd99", "Dwight H Petty"],
  ["83887621-19d4-554c-81d7-ecf874d1f590", "George R Petty"],
  ["45ccf690-c2f6-5555-92f1-15e205ff7ec9", "George R Petty"],
  ["e371f8c1-7a71-5791-87d0-9a0221b1eafc", "Harold J Petty"],
  ["ec38f8ee-89b7-5d30-8c4f-b999b0be7034", "Julian J Petty"],
] as const;

test("Batch 752 publishes all 23 page-366 profiles with reviewed outcomes", async ({ page }) => {
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

test("Batch 752 distinguishes immediate military and civilian affiliations", async ({ page }) => {
  await page.goto("./people/bd31016c-22dd-5c52-95ed-bb6805ac9e81/");
  const petrou = page.locator("main");
  await expect(petrou.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Free Voice of Greece",
  );
  await expect(petrou).toContainText("explicit immediate");
  await expect(petrou).toContainText("Review the indexed personnel file to confirm job title");

  await page.goto("./people/3903ccf4-6632-50fb-8439-19ae15af0352/");
  const petrullo = page.locator("main");
  await expect(petrullo.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "U.S. Army Air Service Command",
  );
  await expect(petrullo).toContainText("military assignment");
  await expect(petrullo.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 752 qualifies Petrullo's last named employer and earlier work", async ({ page }) => {
  await page.goto("./people/3386a008-f2c3-539c-9a86-8610f64b5d95/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Works Progress Administration",
  );
  await expect(main).toContainText("Archaeological consultant");
  await expect(main).toContainText("University of Pennsylvania Museum");
  await expect(main).toContainText("1940 research period in Mexico");
  await expect(main).not.toContainText("Immediate pre-OSS affiliation\nWorks Progress Administration");
});

test("Batch 752 preserves student and professional affiliations without inventing employers", async ({ page }) => {
  await page.goto("./people/73a0cc22-2b1a-5e95-b2a4-467a4729269e/");
  const petrow = page.locator("main");
  await expect(petrow).toContainText("Harvard Law School");
  await expect(petrow).toContainText("Second-year law student");
  await expect(petrow).toContainText("Sons of Pericles");
  await expect(petrow).toContainText("professional affiliation");
  await expect(petrow.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./people/15da58dd-b2f5-50dc-bce3-76b8acd21e9a/");
  const pettengill = page.locator("main");
  await expect(pettengill).toContainText("Princeton University");
  await expect(pettengill).toContainText("Economics student");
  await expect(pettengill.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 752 keeps the Petitt conflict and adjacent Petty rows separate", async ({ page }) => {
  await page.goto("./people/fd2c4ed7-4d9c-5287-9b69-3774642121fa/");
  const pettit = page.locator("main");
  await expect(pettit).toContainText("conflicting");
  await expect(pettit).toContainText("shared by separate Petitt and Pettit index rows");
  await expect(pettit).toContainText("entities remain separate");

  await page.goto("./people/83887621-19d4-554c-81d7-ecf874d1f590/");
  const unranked = page.locator("main");
  await expect(unranked).toContainText("high confidence");
  await expect(unranked).toContainText("unranked row 43");

  await page.goto("./people/45ccf690-c2f6-5555-92f1-15e205ff7ec9/");
  const officer = page.locator("main");
  await expect(officer).toContainText("unresolved");
  await expect(officer).toContainText("adjacent first-lieutenant row");
});

test("home page exposes the rebuilt Batch 752 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,325");
  await expect(home).toContainText("43.13%");
  await expect(home).toContainText("13,609");
  await expect(home).toContainText("771");
  await expect(home).toContainText("342");
  await expect(home).toContainText("8,784");
});
