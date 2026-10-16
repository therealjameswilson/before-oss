import { expect, test } from "@playwright/test";

const profiles = [
  ["305ea101-23a5-578b-a476-e1494124046d", "Ferdinand M Ruff"],
  ["05ba9c31-effc-5e5e-b0b8-9175996eaaf1", "George P Ruff"],
  ["8ec481bb-c6f7-5973-820b-cb1cd6f8946d", "Frank J Ruffina"],
  ["1da44c89-59d6-5e89-983b-2646d0a2b8dc", "John M Ruffing"],
  ["f748aab3-7f36-5bb2-9592-5dfba08a4fb6", "Ruth O Rugenstein"],
  ["e1e392dd-9f03-5a16-bc3c-e57c1fdd2f55", "Vito V Ruggiero"],
  ["fb7a0de8-160c-5a87-a98e-f272799a9982", "Carolyn B Ruggles"],
  ["788fbf2b-2148-55cd-a9d8-d119bd301c0f", "Melville J Ruggles"],
  ["08aa0c81-74f5-5e51-8124-d87af605ee02", "Richard F Ruggles"],
  ["66e5d427-0594-51a0-8f4c-3827b5adf8eb", "Wallace B Ruggles"],
  ["49e929d2-91f6-5a30-9474-58f98ad8eca5", "John F Ruhat"],
  ["5bd3d57e-9802-5f3a-a613-afa837fe0751", "Paul V Ruhl"],
  ["877f2f1e-6a36-52f9-bccd-f1e83717bafb", "Teresa A Rullan"],
  ["8f899a85-f215-50d2-a867-1e7261509b1f", "George R Rummey"],
  ["f3214666-19d2-56e9-8db7-26845878e713", "Osborne R Rumph"],
  ["c13fc360-a0dc-5354-829e-6e90df9fe9b8", "James E Rumple"],
  ["a1d3b9c5-d56d-5442-8316-4ca4688e75f0", "Elvira L Rumthun"],
  ["191056ff-1e10-5dd5-8aaa-41b25fb76768", "Donald L Rundquist"],
  ["69641a73-75d5-5370-80a8-67eb581dfbca", "Carlotta J Rundstrom"],
  ["d4ef3a74-bf70-5124-b43c-4e8b6321345c", "Stefan J Rundt"],
  ["fb2fd490-d60c-5f39-b7ed-83881afe7c52", "Dorothy E Runge"],
  ["90f822c4-aa34-514f-91c0-ec5e6ca58140", "Scott F Runkle"],
  ["4f45149d-7e5c-5bce-9e13-7d08f825ab53", "Dorothy E Runyon"],
] as const;

test("Batch 827 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Richard Ruggles profile separates immediate Harvard student status from employment", async ({ page }) => {
  await page.goto("./people/08aa0c81-74f5-5e51-8124-d87af605ee02/");
  const main = page.locator("main");
  await expect(main).toContainText("Richard Francis Ruggles");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("Harvard University");
  await expect(immediate).toContainText(/student/i);
  await expect(immediate).toContainText("explicit immediate");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(civilian).not.toContainText("Harvard University");
});

test("Scott Runkle profile separates the Army pathway from earlier Sorbonne study", async ({ page }) => {
  await page.goto("./people/90f822c4-aa34-514f-91c0-ec5e6ca58140/");
  const main = page.locator("main");
  await expect(main).toContainText("Scott Frederick Runkle");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("General Omar Bradley");
  await expect(immediate).toContainText(/military assignment/i);
  const earlier = page.getByRole("region", { name: "Earlier pre-OSS affiliations" });
  await expect(earlier).toContainText("University of Paris (Sorbonne)");
  await expect(earlier).toContainText(/student/i);
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Melville Ruggles remains a qualified occupation-only result", async ({ page }) => {
  await page.goto("./people/788fbf2b-2148-55cd-a9d8-d119bd301c0f/");
  const main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("published researcher or author on Soviet industry");
  await expect(main).toContainText("occupation only found");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText(/employer:\s*The Russian Review/i);
});

test("accepted Army identities publish no coded occupations or invented employers", async ({ page }) => {
  for (const id of [
    "05ba9c31-effc-5e5e-b0b8-9175996eaaf1",
    "e1e392dd-9f03-5a16-bc3c-e57c1fdd2f55",
    "191056ff-1e10-5dd5-8aaa-41b25fb76768",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/Official Army/i);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("occupation code");
  }
});

test("three protected-identifier name conflicts remain visible and unmerged", async ({ page }) => {
  for (const [id, conflictingName] of [
    ["305ea101-23a5-578b-a476-e1494124046d", "Ferdinand H. Ruff"],
    ["49e929d2-91f6-5a30-9474-58f98ad8eca5", "John F. Rukat"],
    ["d4ef3a74-bf70-5124-b43c-4e8b6321345c", "John E. Powers"],
  ] as const) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(conflictingName);
    await expect(main).toContainText(/rejected/i);
    await expect(main).toContainText("conflicting sources");
    await expect(main).toContainText("Box 666");
  }
});
