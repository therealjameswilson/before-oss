import { expect, test } from "@playwright/test";

const profiles = [
  ["48739bd5-d126-56d3-ae80-cfeee11d81f3", "Josephine S Peterson"],
  ["312482b0-564b-55eb-8be1-b4b8474ad6fb", "Kathleen J Peterson"],
  ["fbc11b9c-3d3c-50aa-a348-2baec56cb5d2", "Kenneth N Peterson"],
  ["96817071-a78b-5b50-bc1e-80bd74eada82", "Marvin K Peterson"],
  ["12e56298-9073-579b-8b83-b0abc9e1631b", "Norman H Peterson"],
  ["a57aa553-933c-5f9e-88a3-da71ba6fd11a", "Norman E Peterson"],
  ["de2631cd-a5f8-555a-9633-5aa8bb161ea2", "Ross T Peterson"],
  ["2f94c430-3343-5767-b1c0-9155d9329f50", "Roy C Peterson"],
  ["05e97bd5-ca62-5fa5-8fa1-c58892654246", "Vivian A Peterson"],
  ["8a9cb80f-3552-5070-a3a6-89ca33e85f1f", "William G Peterson"],
  ["9cae1ec5-6243-5267-b24e-72924f557ff1", "Ross L Pethtel"],
  ["6b56c569-17a4-5805-ac78-5f0c32d4e68f", "Melvin Petievich"],
  ["c71d0c5e-7239-51b4-b187-13a49ee265d9", "Henri Petit"],
  ["89097cbc-d399-5f33-aa6f-eb10c1e39091", "Frank A Petito"],
  ["8fd36aaa-23c4-5208-bdf8-390e922b5b50", "Joseph E Petitpas"],
  ["412b4531-961a-5861-8bd7-76f18d99df4f", "Robert L Petitt"],
  ["32cc187a-71e3-5138-9434-c8d03f0aeaf8", "Peter P Petkoff"],
  ["b76c052d-7bfd-5135-b8a0-f13ad150130a", "Angelo S Petraglia"],
  ["4dff71d8-1fcb-5f81-bba6-4c3c0845420b", "David Petrie"],
  ["008fcdc9-a1a7-5287-89c8-93ae809a5425", "Albert M Petrilli"],
  ["dd0dbb16-381d-5ffa-a92b-fb9a23b49ec6", "Nicholas C Petris"],
  ["234038eb-54fd-55c9-bafc-d3f0cd2d8b89", "Edward A Petro"],
  ["745d0f3b-1117-55e3-b6dc-96de8ac08cd7", "Boris B Petroff"],
] as const;

test("Batch 751 publishes all 23 page-366 profiles with reviewed outcomes", async ({ page }) => {
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

test("Batch 751 publishes Petris and Petkoff as student affiliations, never employers", async ({ page }) => {
  await page.goto("./people/dd0dbb16-381d-5ffa-a92b-fb9a23b49ec6/");
  const petris = page.locator("main");
  await expect(petris).toContainText("University of California, Berkeley");
  await expect(petris).toContainText("Bachelor's student in journalism");
  await expect(petris).toContainText("served with the Office of Strategic Services during World War II");
  await expect(petris.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );

  await page.goto("./people/32cc187a-71e3-5138-9434-c8d03f0aeaf8/");
  const petkoff = page.locator("main");
  await expect(petkoff).toContainText("University of Michigan");
  await expect(petkoff).toContainText("Bachelor of Science student in engineering");
  await expect(petkoff).toContainText("one of the original members of the OSS");
  await expect(petkoff.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 751 qualifies Boris Petroff's last civilian employer", async ({ page }) => {
  await page.goto("./people/745d0f3b-1117-55e3-b6dc-96de8ac08cd7/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("North Carolina State Highway Commission");
  await expect(main).toContainText("Assistant manager of Traffic Survey");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("does not directly mention OSS");
});

test("Batch 751 keeps the Petievich-Corvin and Petitt-Pettit conflicts visible", async ({ page }) => {
  await page.goto("./people/6b56c569-17a4-5805-ac78-5f0c32d4e68f/");
  const petievich = page.locator("main");
  await expect(petievich).toContainText("conflicting");
  await expect(petievich).toContainText("Melvin Corvin");
  await expect(petievich).toContainText("entities remain separate");

  await page.goto("./people/412b4531-961a-5861-8bd7-76f18d99df4f/");
  const petitt = page.locator("main");
  await expect(petitt).toContainText("conflicting");
  await expect(petitt).toContainText("Robert L Pettit Jr");
  await expect(petitt).toContainText("entities remain separate");
});

test("home page exposes the rebuilt Batch 751 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("10,302");
  await expect(home).toContainText("43.03%");
  await expect(home).toContainText("13,632");
  await expect(home).toContainText("766");
  await expect(home).toContainText("340");
  await expect(home).toContainText("8,761");
});
