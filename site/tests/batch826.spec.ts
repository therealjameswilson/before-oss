import { expect, test } from "@playwright/test";

const profiles = [
  ["c50cc349-aed4-5563-90c2-583648c520aa", "Howard L Ruble"],
  ["f7e5edbd-f668-5607-8d96-8cb236c9164a", "Theobald J Ruby"],
  ["a26dc65c-819f-5769-b735-45f960f26381", "Ellen T Rucker"],
  ["3a546e1a-a6a2-5b34-a60a-7f1f69a661b0", "Lucius O Rucker Jr."],
  ["d1f97d5e-23d1-5926-a437-182b14128ef0", "Scott Ruckman"],
  ["9ede1f13-2d3a-5a54-b052-891344d01974", "Joseph Rudas"],
  ["34de904f-6548-5530-89a2-21e888acb5a9", "Irving G Rudd"],
  ["e1f7be59-d39e-5af8-bf32-cb614968f3dd", "John B Rudd"],
  ["d3e84044-d6c3-57c6-b117-75f5e25f9d2b", "Paul V Rudden"],
  ["5d86a8cb-1d06-58d2-8165-77c760e43bdf", "Roscoe Ruddle"],
  ["8e36672c-1b9c-5a21-94bd-1a16cf83bca8", "Merritt K Ruddock"],
  ["767471b0-c15d-52cc-97a2-46533582af5e", "Ann B Ruddy"],
  ["4d65d5de-a036-56f5-85ab-939965e10836", "Ellen M Rudebeck"],
  ["4c7ee580-1e1a-5ae0-8cbf-2de9b5ec8e46", "Carl E Ruder"],
  ["3699be60-df8c-51ac-b37d-76b9af34e09f", "Joanna V Rudis"],
  ["8cfe28a5-65eb-5d9e-9f62-8e2bb4833730", "Eryl Rudlin"],
  ["fe3432ca-39dc-5301-8195-4835bc424413", "Jack M Rudolph"],
  ["290d61e8-eea1-56d1-b051-28351ab80de0", "Selna Rudy"],
  ["d7a27aa3-7da9-5855-8abf-679de4a45ba0", "Walter H Ruef"],
  ["c5e9a62c-ba7c-501b-8fde-8583d6b03d60", "William F Rueff"],
  ["bd0bf11d-daa9-5808-92bd-8fc9c79be3f6", "Fritz Ruesch"],
  ["60fad3a7-cb27-52ee-af3d-b04e873e398f", "Gilbert J Ruest"],
  ["d85eb435-d317-5e67-bd8a-9c0e57073c76", "David F Ruf"],
] as const;

test("Batch 826 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Lucius Rucker profile treats the Army path as an immediate military affiliation", async ({ page }) => {
  await page.goto("./people/3a546e1a-a6a2-5b34-a60a-7f1f69a661b0/");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("U.S. Army");
  await expect(immediate).toContainText("career Army officer and paratrooper");
  await expect(immediate).toContainText("strongly date bounded");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(civilian).not.toContainText("U.S. Army");
});

test("Merritt Ruddock profile keeps both 1941 journalism roles as earlier documented work", async ({ page }) => {
  await page.goto("./people/8e36672c-1b9c-5a21-94bd-1a16cf83bca8/");
  const earlier = page.getByRole("region", { name: "Earlier pre-OSS affiliations" });
  await expect(earlier).toContainText("Mutual Broadcasting System");
  await expect(earlier).toContainText("WRNL");
  await expect(earlier).toContainText("news analyst");
  await expect(earlier).toContainText("newsman");
  await expect(earlier).toContainText(/documented pre-OSS/i);
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("No reviewed claim currently meets the publication threshold");
});

test("Jack Rudolph profile publishes Kimberly-Clark only as the last civilian employer", async ({ page }) => {
  await page.goto("./people/fe3432ca-39dc-5301-8195-4835bc424413/");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("Kimberly-Clark Corporation");
  await expect(civilian).toContainText("Employment");
  await expect(civilian).toContainText("strongly date bounded");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).not.toContainText("Kimberly-Clark");
  await expect(page.locator("main")).not.toContainText(/chemical engineer at Kimberly-Clark/i);
});

test("Ruest and Rudlin profiles preserve temporal and identity qualifications", async ({ page }) => {
  await page.goto("./people/60fad3a7-cb27-52ee-af3d-b04e873e398f/");
  let main = page.locator("main");
  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("whether it preceded, overlapped, or followed OSS duty");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/8cfe28a5-65eb-5d9e-9f62-8e2bb4833730/");
  main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("supplies no OSS, Box 665, grade, or employer bridge");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("accepted Army identities do not expose coded occupations or invent employers", async ({ page }) => {
  for (const id of [
    "f7e5edbd-f668-5607-8d96-8cb236c9164a",
    "9ede1f13-2d3a-5a54-b052-891344d01974",
    "4c7ee580-1e1a-5ae0-8cbf-2de9b5ec8e46",
    "bd0bf11d-daa9-5808-92bd-8fc9c79be3f6",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/Official Army/i);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("occupation code");
  }
});

test("John Rudd protected-identifier conflict remains visible and unmerged", async ({ page }) => {
  await page.goto("./people/e1f7be59-d39e-5af8-bf32-cb614968f3dd/");
  const main = page.locator("main");
  await expect(main).toContainText("John B. Rodd");
  await expect(main).toContainText(/rejected/i);
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Box 653");
  await expect(main).toContainText("Box 665");
});
