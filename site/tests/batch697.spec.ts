import { expect, test } from "@playwright/test";

const profiles = [
  ["5f1db816-c3e7-5dda-92d6-ce3fbf8ca14c", "Jacqueline H Neff"],
  ["322de5c7-9673-5520-8233-2846e966e49f", "Ralph R Neff"],
  ["3edab7e3-c67a-59f0-8aa5-2fed5942bfcf", "Robert P/R Neff"],
  ["7016f44e-d2f4-59f7-b631-26599fd88f61", "Nicholas Nefopulas"],
  ["e57ad6f3-ce63-520d-a267-6193ff6c306a", "Leonard Negre"],
  ["24a36966-0f89-5bd1-b312-d04c3ea5a710", "Stanley Nehmer"],
  ["8223d1f9-be6e-5220-ace6-cddc102968ff", "Bernard R Nehring"],
  ["cf6773ae-48ad-5ee4-98c9-be76da24f924", "Eldon N Nehring"],
  ["decae704-05e0-5097-8c8f-3f636c4b08a3", "Bert D Neiber"],
  ["e3b4ae0e-2157-5c4f-a335-31716c212bdd", "Jack S Neidorff"],
  ["e86b2679-1d5f-5ead-af99-631e823f6174", "Leroy A Neigh"],
  ["03299284-849c-5bbd-91c0-acc79403af77", "Charles L Neil"],
  ["5b3ace80-ed17-5fec-a5f2-7d7880badd47", "Lenoore M Neil"],
  ["4b548f93-3c2b-5e7a-acf6-df71520c992b", "Malcolm W Neill"],
  ["b48fce54-ec82-5a8f-b90e-60ce3469e747", "Eugene A Neilson"],
  ["61cb539b-5293-5078-b5df-1173bd7b9c6e", "John W Neilson"],
  ["a1d13119-3b9d-5d07-b786-0f89027b80f8", "Lester C Neimann"],
  ["caa08125-eae0-5cde-8682-01d3ad6ee141", "Julian M Neimczylc"],
  ["e7f87b64-20ef-502c-b9e3-f4d8d8d28890", "Gabrielle Neiss"],
  ["9df4e3e3-d98a-5e21-90e6-23ed1e277b75", "Ben Neivert"],
  ["b3ab5776-1ed5-59c6-9223-829fb262dc2c", "Harold Nelchin"],
  ["8b761a35-58e5-5da0-97b3-1936b360dfc0", "Jack F Neller"],
  ["90501879-599f-5f4b-84b5-d2f872ef0318", "Gerhardt Nellhaus"],
] as const;

test("Batch 697 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^\d{7,8}$/);
  }
});

test("Batch 697 separates Stanley Nehmer's student status from employment", async ({ page }) => {
  await page.goto("./people/24a36966-0f89-5bd1-b312-d04c3ea5a710/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(earlier).toContainText("City College of New York");
  await expect(earlier).toContainText("Student and graduate");
  await expect(earlier).toContainText("student");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 697 qualifies Julian Niemczyk's identity and Army pathway", async ({ page }) => {
  await page.goto("./people/caa08125-eae0-5cde-8682-01d3ad6ee141/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Julian Martin Niemczyk");
  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("Battery commander; second lieutenant");
  await expect(immediate).toContainText("explicit immediate");
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(earlier).toContainText("University of Oklahoma");
  await expect(earlier).toContainText("Student");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 697 preserves the Eldon Nehring and Lester Neimann conflicts", async ({ page }) => {
  await page.goto("./people/cf6773ae-48ad-5ee4-98c9-be76da24f924/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Evidence conflict");
  await expect(main).toContainText("different Army name and grade");

  await page.goto("./people/a1d13119-3b9d-5d07-b786-0f89027b80f8/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Evidence conflict");
  await expect(main).toContainText("shared by a separate OSS index entity");
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 697 publishes Nellhaus only as temporally uncertain wartime context", async ({ page }) => {
  await page.goto("./people/90501879-599f-5f4b-84b5-d2f872ef0318/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Gerhard Nellhaus");
  const earlier = page.locator('section[aria-labelledby="earlier-affiliations"]');
  await expect(earlier).toContainText("348th Bombardment Squadron");
  await expect(earlier).toContainText("German radio-message intercept operator");
  await expect(earlier).toContainText("temporal relation uncertain");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"] .affiliation-card')).toHaveCount(0);
  await expect(page.locator('section[aria-labelledby="civilian-employer"] .affiliation-card')).toHaveCount(0);
});

test("Batch 697 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  const body = page.locator("body");
  await expect(body).toContainText("9,075");
  await expect(body).toContainText("37.91%");
  await expect(body).toContainText("317");
  await expect(body).toContainText("14,859");

  const oilCategory = page.locator("#oil-companies");
  await expect(oilCategory.locator(".oil-directory__person")).toHaveCount(9);
  await expect(oilCategory).toContainText("11 historically named oil companies");
});
