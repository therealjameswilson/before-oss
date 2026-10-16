import { expect, test } from "@playwright/test";

const profiles = [
  ["7ef7e244-f61b-56e3-8c68-72d008028b41", "Anthony Santulli"],
  ["caff86ae-4b70-5344-9b3d-8e2f71c81243", "Alfred N Sanzari"],
  ["53fe9328-6d7f-5b3f-b19f-4549c284ea26", "James W Saper"],
  ["18fecb9a-fff3-544f-9c0b-278d8b1bd759", "Alfred J Sapierza"],
  ["0865eae4-bd3e-57c6-ad6b-94ad82782c3e", "Michael S Sapna"],
  ["26239e14-c04a-5e9e-b07c-19ce1f5bc666", "Alphonse F Saporito"],
  ["01662455-c097-5b4d-8166-e9474554e600", "Vincent J Saporito"],
  ["c2758aeb-5cde-5bcf-b9d1-844bf6b80f1f", "Albert B Sapp"],
  ["bf81f034-771c-5096-bf36-36a88fda381c", "Julia S Sapp"],
  ["22c1d1c0-52da-5d54-af84-b95191694809", "Albert J Saputo"],
  ["5c246b18-3e76-561d-bfdb-e0f3d9beb742", "Albert Saraceno"],
  ["8073bfe6-7a4e-5277-a9b3-5b3c2e13bb9e", "Edgar G Sarbo"],
  ["975c48a2-a7a0-5847-a777-d8ba62bb3ac9", "Joe J Sardella"],
  ["bd18b5bf-eff9-54a9-8ae2-869e932a75bb", "Robert E Sare"],
  ["df2638cf-e726-5896-8b60-c385d9c0d8b0", "Donald H Sarem"],
  ["453e14af-8b21-5af6-8841-87900dde35ee", "Clyde B Sargent"],
  ["f2f8e3e7-ceb5-5c0c-88e9-d5f1a95a0b84", "Christopher T Saris"],
  ["a4116b74-df37-562c-8b61-c18e0cda2406", "Jacques Sarlie"],
  ["e4f15c9c-8168-5fe2-a541-9da6b7babbf3", "Rudolf Sarlie"],
  ["fe5f45b6-084c-5f6a-95db-f75eed4c3b04", "Peter R Sarni"],
  ["d16c6514-ba8b-5895-9abf-2f2470cafeb4", "Barbara Saro"],
  ["5b08dee2-41f8-5003-a1a9-6e41776ccbc5", "Nicholas Saros"],
  ["ada9c2dc-aafb-52a5-9233-c077400ade9f", "Harry Sarris"],
] as const;

test("Batch 838 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
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

test("Alfred Sanzari publishes only the supported occupation and keeps the employer unnamed", async ({ page }) => {
  await page.goto("./people/caff86ae-4b70-5344-9b3d-8e2f71c81243/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("sheet-metal worker");
  await expect(main).toContainText("unnamed company");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("private Army crosswalk remains isolated");
});

test("Clyde Sargent publishes Cheeloo University with qualified immediate timing", async ({ page }) => {
  await page.goto("./people/453e14af-8b21-5af6-8841-87900dde35ee/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Cheeloo University");
  await expect(main).toContainText("professor and Foreign Language Department head");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("Last civilian employer before service");
});

test("Julia Sapp keeps the documented WASP role temporally uncertain", async ({ page }) => {
  await page.goto("./people/bf81f034-771c-5096-bf36-36a88fda381c/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Central Flying Training Command");
  await expect(main).toContainText("WASP Staff Executive");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("whether this preceded or overlapped her OSS service");
  await expect(main.getByRole("heading", { name: "Immediate pre-OSS affiliation" })
    .locator("xpath=following-sibling::p[1]")).toContainText("No reviewed claim");
});

test("Nicholas Saros publishes qualified Newark legal practice without inventing a firm", async ({ page }) => {
  await page.goto("./people/5b08dee2-41f8-5003-a1a9-6e41776ccbc5/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("law practice in Newark");
  await expect(main).toContainText("attorney");
  await expect(main).toContainText("strongly date bounded");
  await expect(main).toContainText("no firm name is identified");
});

test("Jacques Sarlie uses postwar evidence for identity only", async ({ page }) => {
  await page.goto("./people/a4116b74-df37-562c-8b61-c18e0cda2406/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Dutch-born");
  await expect(main).toContainText("U.S. Army officer in France");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).toContainText("Postwar art collecting and finance are identity evidence only");
});

test("accepted Army crosswalks publish identity evidence but no coded occupation", async ({ page }) => {
  for (const id of [
    "5c246b18-3e76-561d-bfdb-e0f3d9beb742",
    "df2638cf-e726-5896-8b60-c385d9c0d8b0",
    "8073bfe6-7a4e-5277-a9b3-5b3c2e13bb9e",
    "975c48a2-a7a0-5847-a777-d8ba62bb3ac9",
    "fe5f45b6-084c-5f6a-95db-f75eed4c3b04",
    "bd18b5bf-eff9-54a9-8ae2-869e932a75bb",
    "01662455-c097-5b4d-8166-e9474554e600",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("protected identifier");
    await expect(main).not.toContainText("Army occupation code");
  }
});

test("Sapierza and Sapienza remain documented variants instead of a silent correction", async ({ page }) => {
  await page.goto("./people/18fecb9a-fff3-544f-9c0b-278d8b1bd759/");
  const main = page.locator("main");
  await expect(main).toContainText("Indexed formAlfred J Sapierza");
  await expect(main).toContainText("Documented variantsAlfred J Sapienza");
  await expect(main).toContainText("R-versus-N surname disagreement remains explicit");
  await expect(main).toContainText("requires archival review");
});

test("Army name conflicts remain visible without publishing alternate candidates", async ({ page }) => {
  for (const id of [
    "7ef7e244-f61b-56e3-8c68-72d008028b41",
    "0865eae4-bd3e-57c6-ad6b-94ad82782c3e",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusconflicting");
    await expect(main).toContainText("materially different name");
    await expect(main).toContainText("alternate identity and coded fields are withheld");
    await expect(main).not.toContainText("Army occupation code");
  }
});

test("unresolved Batch 838 profiles retain dignified archival guidance", async ({ page }) => {
  for (const id of [
    "53fe9328-6d7f-5b3f-b19f-4549c284ea26",
    "26239e14-c04a-5e9e-b07c-19ce1f5bc666",
    "c2758aeb-5cde-5bcf-b9d1-844bf6b80f1f",
    "22c1d1c0-52da-5d54-af84-b95191694809",
    "f2f8e3e7-ceb5-5c0c-88e9-d5f1a95a0b84",
    "e4f15c9c-8168-5fe2-a541-9da6b7babbf3",
    "d16c6514-ba8b-5895-9abf-2f2470cafeb4",
    "ada9c2dc-aafb-52a5-9233-c077400ade9f",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusunresolved");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("Review Box");
  }
});
