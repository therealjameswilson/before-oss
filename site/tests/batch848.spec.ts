import { expect, test } from "@playwright/test";

const profiles = [
  ["fe9fff7c-798c-55c7-9d51-ee3e062b6d9f", "Louis Schneider"],
  ["5775e2a1-a9a6-57e8-9d7e-268516846f93", "William E Schneider"],
  ["85439eee-e88d-5573-8794-a8b8c619f755", "Horace J Schnelzer"],
  ["c1231d59-eab2-59b2-b564-5a87ceb70c15", "Herbert W Schnetzky"],
  ["6b53cba0-b03b-562d-a54c-5830e8f908bc", "Solomon Schneyer"],
  ["a7db35a9-093c-52ae-82aa-9558928b846f", "Walter O Schnyder"],
  ["2c47e158-0bbe-5824-a09b-26d8173429f4", "Thomas D Schocken"],
  ["4e1df07a-0cbc-5866-9b88-543840172f87", "Eddie W Schodt"],
  ["e5d33182-4089-58d6-9f53-9174e037ae72", "Eugene Schoemann"],
  ["cb250c15-143e-5b77-b166-66fc7f874ea8", "John R Schoemer"],
  ["90c75815-d07f-54aa-946f-4c8d7c09e602", "Herbert V Schoen"],
  ["314b65db-796e-5a6d-85d1-ee0deb5fb945", "Robert J Schoen"],
  ["c7e2cd6f-ff48-599e-a238-cfaef19b5c03", "John F Schoenack"],
  ["73aa55d7-c4e7-555d-b229-47d89bf37c60", "Jerry Schoenbaum"],
  ["01af2a86-6ad2-5882-bd2b-fa9abaf5bbbb", "Richard T Schoenberger"],
  ["6742852b-3539-5f84-a687-3708b2b6238d", "Marion R Schoenfeld"],
  ["4ae3b426-c5e4-5991-8742-9185838baec8", "Milton C Schoenheim"],
  ["b27d8d4c-7e77-549b-9507-a9347f63adb0", "Elmer H Schoening"],
  ["dedcadfe-9052-509b-975c-7c8e9cb92bb9", "William A Schoepper"],
  ["5abbf57e-30a6-58bd-a7d1-6dde7ff5b6a0", "Ralph A Schoff"],
  ["75ea5d89-25df-5f47-b92b-cb9deb5ed521", "Donald R Schofield"],
  ["b4b63d34-b449-503a-ae5e-6bd8ee42cb45", "George Schofield"],
  ["eef09759-80e1-52fb-bb9c-e4a612009a22", "LA Vonne L Schofield"],
] as const;

test("Batch 848 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("John Schoemer publishes the dated law-firm pathway without overstating recruitment", async ({ page }) => {
  await page.goto("./people/cb250c15-143e-5b77-b166-66fc7f874ea8/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("John R. Schoemer Jr.");
  await expect(main).toContainText("Townley & Updike");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Last civilian employer before service");
  await expect(main).toContainText("Attorney");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("direct recruitment");
});

test("Thomas Schocken keeps three earlier professional affiliations separate from an unknown immediate employer", async ({ page }) => {
  await page.goto("./people/2c47e158-0bbe-5824-a09b-26d8173429f4/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Thomas Daniel Schocken");
  await expect(main).toContainText("commissioned naval officer");
  await expect(main).toContainText("Estanislao Seguróla");
  await expect(main).toContainText("Ernst May planning group");
  await expect(main).toContainText("Town and Country Planning Association");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).not.toContainText("Last civilian employer before serviceTown and Country Planning Association");
});

test("Eddie Schodt publishes education as student status rather than employment", async ({ page }) => {
  await page.goto("./people/4e1df07a-0cbc-5866-9b88-543840172f87/");
  const main = page.locator("main");
  await expect(main).toContainText("Eddie William Schodt");
  await expect(main).toContainText("State Teachers College, Valley City");
  await expect(main).toContainText("University of Colorado Boulder");
  await expect(main).toContainText("student");
  await expect(main).toContainText("education only, not as an employer");
  await expect(main).toContainText("1940");
});

test("Solomon Schneyer's Temple affiliation remains visibly qualified", async ({ page }) => {
  await page.goto("./people/6b53cba0-b03b-562d-a54c-5830e8f908bc/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Temple University School of Chiropody");
  await expect(main).toContainText("Senior student; class historian");
  await expect(main).toContainText("medium documented pre-OSS");
  await expect(main).toContainText("yearbook has no protected identifier or OSS link");
});

test("Richard Schoenberger shows a qualified military pathway, not a civilian employer", async ({ page }) => {
  await page.goto("./people/01af2a86-6ad2-5882-bd2b-fa9abaf5bbbb/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("United States Army Quartermaster Corps");
  await expect(main).toContainText("military assignment");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("not a civilian employer");
  await expect(main).toContainText("later Sears career is excluded");
});

test("Army-only identities do not expose coded occupations or invent employers", async ({ page }) => {
  for (const id of [
    "85439eee-e88d-5573-8794-a8b8c619f755",
    "a7db35a9-093c-52ae-82aa-9558928b846f",
    "314b65db-796e-5a6d-85d1-ee0deb5fb945",
    "73aa55d7-c4e7-555d-b229-47d89bf37c60",
    "4ae3b426-c5e4-5991-8742-9185838baec8",
    "dedcadfe-9052-509b-975c-7c8e9cb92bb9",
    "75ea5d89-25df-5f47-b92b-cb9deb5ed521",
    "b4b63d34-b449-503a-ae5e-6bd8ee42cb45",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }
});
