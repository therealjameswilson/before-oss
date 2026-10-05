import { expect, test } from "@playwright/test";

const profiles = [
  ["73ea295a-687c-5ab2-9eab-f0ae2e17dbf6", "Victoria A Paul"],
  ["7940c259-d7e7-5020-bb32-d0c32a77870f", "John Paulick"],
  ["94b2e256-2dcf-57da-8ccd-2390f88ad6e4", "Joseph K Paull"],
  ["18869cd0-e25c-5edc-a4b5-6d86b301f1bb", "Alf H Paulson"],
  ["c452defc-bbfb-51e8-bf87-cfa32d1c638f", "Evelyn D Paulson"],
  ["546d66a0-094c-5e4d-8e06-7425698d0a0f", "June M Paulson"],
  ["45f6bb93-a539-55a7-91c9-87f129bb7fbd", "Albert Pauly"],
  ["c4aec5b2-463e-5362-bb99-9d632e26b69f", "Walter F Pauly Jr."],
  ["cd75f819-091c-56bb-a662-8c903be1ccaa", "Leo Paur"],
  ["ae9c997c-70e6-5dcd-a643-eabb71645969", "Harold A Paus"],
  ["46e546bc-ebab-5210-b71e-e2d97dd65c0d", "O Paus"],
  ["22bb975a-1bc9-5767-8578-82b5d9e5bcec", "Arthur A Pava"],
  ["0085f72a-fe5d-559f-9062-a2c00aaedf26", "Angelo J Pavan"],
  ["3bcaab08-cd06-5efd-b313-5ff0e462f4bd", "Charles Paveloi"],
  ["54108fcc-3fcb-5a72-b190-7344f25236fa", "Vincent Pavia"],
  ["f61718e9-fd99-567b-8552-32619eb5e110", "George Pavik"],
  ["5c78a42c-79e8-51b5-819a-6fff7d83c855", "Joseph Pavlacka"],
  ["49c353c0-1694-555d-9180-df01234613fe", "Daniel Pavletich"],
  ["8187d21a-5594-55af-b953-1834808882c0", "Olga Pavlova"],
  ["5615f2ac-d0ed-531e-b498-4b3d2c4ab783", "Miles Pavlovich"],
  ["3c8fdbc2-91fe-5c3a-8a57-c3da55c548a8", "Virginia H Pavlovsky"],
  ["a2aa6774-a4df-5ba5-97fb-bed368eea34f", "Vincent E Pawlak"],
  ["0a02afc4-8864-5f07-aede-c2b98e047840", "Eugene D Pawley"],
] as const;

test("Batch 740 publishes all 23 page-360 profiles with reviewed outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\d{4,8}$/);
  }
});

test("Arthur Pava keeps employer, student status, and Army assignment separate", async ({ page }) => {
  await page.goto("./people/22bb975a-1bc9-5767-8578-82b5d9e5bcec/");
  const main = page.locator("main");
  await expect(main).toContainText("New York State Agricultural Experiment Station");
  await expect(main).toContainText("Cornell University");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("high confidence");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "New York State Agricultural Experiment Station",
  );
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText(
    "graduate student",
  );
});

test("Daniel Pavletich publishes an occupation without inventing an employer", async ({ page }) => {
  await page.goto("./people/49c353c0-1694-555d-9180-df01234613fe/");
  const main = page.locator("main");
  await expect(main).toContainText("radio operator on a merchant ship");
  await expect(main).toContainText("ship and employing company are not identified");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Miles Pavlovich publishes the documented Army-to-OSS chronology", async ({ page }) => {
  await page.goto("./people/5615f2ac-d0ed-531e-b498-4b3d2c4ab783/");
  const main = page.locator("main");
  await expect(main).toContainText("Miles J Pavlovich");
  await expect(main).toContainText("March 15, 1938");
  await expect(main).toContainText("June 1943");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("confirmed");
});

test("identity-only records remain unresolved for pre-OSS affiliation", async ({ page }) => {
  for (const id of [
    "3bcaab08-cd06-5efd-b313-5ff0e462f4bd",
    "54108fcc-3fcb-5a72-b190-7344f25236fa",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Eugene Pawley's CNAC affiliation stays visibly qualified", async ({ page }) => {
  await page.goto("./people/0a02afc4-8864-5f07-aede-c2b98e047840/");
  const main = page.locator("main");
  await expect(main).toContainText("China National Aviation Corporation");
  await expect(main).toContainText("medium documented pre-OSS");
  await expect(main).toContainText("do not establish his job title");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 740 rebuilds exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("10,052");
  await expect(main).toContainText("41.99%");
  await expect(main).toContainText("13,882");
  await expect(main).toContainText("751");
  await expect(main).toContainText("335");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
