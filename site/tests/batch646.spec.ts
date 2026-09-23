import { expect, test } from "@playwright/test";

test("Batch 646 publishes Edwin Meader's civilian and military pathways separately", async ({
  page,
}) => {
  await page.goto("./people/cd2a9ff7-13d3-5386-9652-c47686c756cb/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Edwin E Meader", level: 1 })).toBeVisible();
  await expect(main).toContainText("Kalamazoo Vegetable Parchment Company");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("Kalamazoo Gazette");
  await expect(main).toContainText("University of Michigan");
});

test("Batch 646 publishes Donn Medalie's documented Foreign Service pathway without overstating immediacy", async ({
  page,
}) => {
  await page.goto("./people/e4f06177-71b0-59d9-b72d-9f36f3377345/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Donn P Medalie", level: 1 })).toBeVisible();
  await expect(main).toContainText("United States Department of State");
  await expect(main).toContainText("American Vice Consul");
  await expect(main).toContainText("documented prewar");
  await expect(main).toContainText("The American Foreign Service Journal");
  await expect(main).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );
});

test("Batch 646 qualifies David Meck's probable identity and overlapping affiliations", async ({
  page,
}) => {
  await page.goto("./people/70ac74b0-8618-5493-a6fa-98f29450a20d/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "David C Meck", level: 1 })).toBeVisible();
  await expect(main).toContainText("probable");
  await expect(main).toContainText("John Marshall School of Law");
  await expect(main).toContainText("Federal Security Agency");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("Cleveland State University College of Law");
});

test("Batch 646 publishes Thomas Medlicott's official Coast Guard assignment to OSS duty", async ({
  page,
}) => {
  await page.goto("./people/c2f1a32f-db57-537f-91d3-e21198ed9dbd/");
  const main = page.locator("main");

  await expect(page.getByRole("heading", { name: "Thomas O Medlicott", level: 1 })).toBeVisible();
  await expect(main).toContainText("United States Coast Guard");
  await expect(main).toContainText("Operational Swimmer Group II");
  await expect(main).toContainText("Chief warrant officer");
  await expect(main).toContainText("Guardian Spies");
  await expect(main).toContainText("explicit immediate");
});

test("Batch 646 keeps Army conflicts and the Lorraine duplicate boundary visible", async ({ page }) => {
  await page.goto("./people/382588a9-b2e3-50ad-89fa-1c91994f3511/");
  let main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Joseph B Medagliant", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("RAUSCH LEONARD");
  await expect(main).toContainText("MEDAGLIANI JOSEPH B");

  for (const [personId, displayName] of [
    ["e1d3612e-1ec2-5438-8a7f-8768cad5816d", "Lorraine M Meader"],
    ["87534337-8145-51b8-bd77-c4748c6de875", "Lorraine M Meador"],
  ]) {
    await page.goto(`./people/${personId}/`);
    main = page.locator("main");
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(main).toContainText("probable");
    await expect(main).toContainText("separate entity");
    await expect(main).toContainText("Box 514");
  }
});

test("Batch 646 publishes exact coverage while retaining the top oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,967");
  await expect(page.locator("body")).toContainText("33.28%");
  await expect(
    page.getByRole("heading", { name: "People who worked for oil companies" }),
  ).toBeVisible();

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Meader");
});
