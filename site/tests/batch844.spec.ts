import { expect, test } from "@playwright/test";

const profiles = [
  ["8966bb26-1bec-5fab-8456-128c2c25c10a", "Henry Scheiber III"],
  ["a851dcc1-2e23-5fab-8d37-e59eacfeff0c", "Richard L Scheibker"],
  ["9f6e8b4e-66c9-5659-8ba3-60a60876b12e", "Albert L Scheiner"],
  ["60e3bc67-bc18-55db-a502-e8d2addb870b", "John Scheiner"],
  ["ccf748cd-dbaf-5407-a7a5-de1b1bad5482", "George J Schell"],
  ["b10accf9-b204-55b3-8aef-bb92b186ba43", "James W Schenider"],
  ["e92a66ff-e493-5a4b-8182-eaf3c6b7b1c3", "Gustave E Schenk"],
  ["66f3e753-c306-5938-b1cf-f427bf5fcf0c", "Samuel L Schepps"],
  ["95abf2fe-e7f0-51bc-92b4-3ffd0c5ffd8d", "Frank P Scherl"],
  ["61d8f6e3-1686-58a8-8f30-4cc0f64797be", "Frederick J Scherman"],
  ["de44d24b-05f7-582a-b32a-81b769dc130c", "Robert Scheuer"],
  ["9b3bce8a-4eee-5e68-92bf-4136a283091f", "Ludwig R Scheur"],
  ["1389e962-7c74-517b-ae0c-e350dd783a5a", "Richard D Scheurmann"],
  ["9fccb17b-dcc0-5359-92c8-0cefff52084e", "Stanford L Schewel"],
  ["2f0659a7-40f2-5c19-b26d-e5fec0b92ceb", "Stanford L Schewel"],
  ["451428e2-970f-5f01-8d8d-2ef2fc1b4519", "Elwood L Schexnayder"],
  ["a668b208-d84f-5515-9db1-077faaa84eb7", "Alfred D Schiaffo"],
  ["3412889d-85ba-55c5-8eee-0d111f208995", "Leo J Schick"],
  ["7a7194de-6c64-5a1c-be6c-f9e9ff02b513", "William O Schieffelin"],
  ["417c3e14-08fc-557e-9df8-717962661f4f", "Robert M Schiff"],
  ["d4c32c6f-1691-5c06-85af-5a21fc012fa7", "Robert M Schiff"],
  ["30a38b17-4501-5bf1-9d22-4e5147cb6dfb", "Gertrude M Schiffauer"],
] as const;

test("Batch 844 publishes all 22 active reviewed profiles with masked identifiers", async ({ page }) => {
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

test("Elwood Schexnayder merges two index rows but excludes postwar Shell Oil", async ({ page }) => {
  await page.goto("./people/451428e2-970f-5f01-8d8d-2ef2fc1b4519/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Elwood Louis Schexnayder");
  await expect(main).toContainText("Elwood L Schexmayder");
  await expect(main).toContainText("Boxes 682 and 686");
  await expect(main).toContainText("U.S. Army OSS veteran stationed in Ceylon");
  await expect(main).toContainText("Shell Oil employment is explicitly postwar");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("Index row 1");
  await expect(main).toContainText("Index row 2");
});

test("Alfred Schiaffo remains probable and visibly qualified", async ({ page }) => {
  await page.goto("./people/a668b208-d84f-5515-9db1-077faaa84eb7/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Signal Corps OCS Class 10-42");
  await expect(main).toContainText("graduated November 16, 1942");
  await expect(main).toContainText("medium D correlative or secondary");
  await expect(main).toContainText("Probable rather than high confidence");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("accepted Batch 844 Army crosswalks publish identity only", async ({ page }) => {
  for (const id of [
    "ccf748cd-dbaf-5407-a7a5-de1b1bad5482",
    "b10accf9-b204-55b3-8aef-bb92b186ba43",
    "66f3e753-c306-5938-b1cf-f427bf5fcf0c",
    "9b3bce8a-4eee-5e68-92bf-4136a283091f",
    "7a7194de-6c64-5a1c-be6c-f9e9ff02b513",
    "d4c32c6f-1691-5c06-85af-5a21fc012fa7",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(/protected identifier|private official Army crosswalk/i);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }
});

test("Stanford Schewel rows remain separate and ambiguous", async ({ page }) => {
  for (const id of [
    "9fccb17b-dcc0-5359-92c8-0cefff52084e",
    "2f0659a7-40f2-5c19-b26d-e5fec0b92ceb",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusambiguous");
    await expect(main).toContainText("Duplicate group");
    await expect(main).toContainText("two identical index rows");
    await expect(main).toContainText("Compare both Stanford L. Schewel files in Box 682");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("Robert Schiff rows remain separate despite one accepted Army identity", async ({ page }) => {
  await page.goto("./people/417c3e14-08fc-557e-9df8-717962661f4f/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusunresolved");
  await expect(main).toContainText("Duplicate group");
  await expect(main).toContainText("insufficient to merge or transfer the Army identity");

  await page.goto("./people/d4c32c6f-1691-5c06-85af-5a21fc012fa7/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Duplicate group");
  await expect(main).toContainText("numbered indexed Private First Class Robert M. Schiff");
  await expect(main).toContainText("No merge is made without direct evidence");
});

test("Robert Scheuer exposes the conflict without publishing the private alternate identity", async ({ page }) => {
  await page.goto("./people/de44d24b-05f7-582a-b32a-81b769dc130c/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("materially different full name");
  await expect(main).toContainText("do not publish the alternate name");
  await expect(main).not.toContainText("Alternate identity:");
});

test("unresolved Batch 844 profiles retain archival guidance", async ({ page }) => {
  for (const [id, box] of [
    ["8966bb26-1bec-5fab-8456-128c2c25c10a", "682"],
    ["a851dcc1-2e23-5fab-8d37-e59eacfeff0c", "682"],
    ["9f6e8b4e-66c9-5659-8ba3-60a60876b12e", "682"],
    ["60e3bc67-bc18-55db-a502-e8d2addb870b", "682"],
    ["e92a66ff-e493-5a4b-8182-eaf3c6b7b1c3", "682"],
    ["95abf2fe-e7f0-51bc-92b4-3ffd0c5ffd8d", "682"],
    ["61d8f6e3-1686-58a8-8f30-4cc0f64797be", "682"],
    ["1389e962-7c74-517b-ae0c-e350dd783a5a", "682"],
    ["3412889d-85ba-55c5-8eee-0d111f208995", "683"],
    ["417c3e14-08fc-557e-9df8-717962661f4f", "683"],
    ["30a38b17-4501-5bf1-9d22-4e5147cb6dfb", "683"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText(`Box ${box}`);
  }
});
