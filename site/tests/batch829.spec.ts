import { expect, test } from "@playwright/test";

const profiles = [
  ["2eb2c6d6-c9ce-5fe2-9e94-b3c2e4e646f7", "John S Russell"],
  ["46b83ac1-1117-5fb5-bce9-8aa1016bc451", "John A Russell"],
  ["e6d36fba-3160-5bc1-8c6c-fa2484766c44", "Joseph A Russell"],
  ["f2018e17-0fdd-51b3-9df5-def867d658e1", "Phyllis A Russell"],
  ["c636ec7e-f39a-5ab5-ba9c-e34dc41cb231", "Robert W Russell"],
  ["f8594743-6d19-521d-b07f-d6545cff52a6", "Theodore W Russell"],
  ["602b0c75-64c9-5cbb-a2b4-3ca2ea8fdb97", "Wayne A Russell"],
  ["4430b0e9-182f-5e44-bd4a-7dbc9a05c716", "William H Russell"],
  ["d7667caf-7e4e-592f-b724-49376b551e59", "William J Russell"],
  ["eb08828b-ea1b-55ae-aed6-8957a12feea2", "Wima Russell"],
  ["04888f83-19a5-5f97-8c6c-f6bc05bd21b1", "Charles J Russhon"],
  ["efface03-c4b9-5bb8-b19c-56406d7a7c4a", "Alexander P Russo"],
  ["7951486d-e7f9-5138-818b-96918e74b8b5", "Chlorinda V Russo"],
  ["2261f780-37bc-5fed-a852-02faa72b3a50", "Fred B Russo"],
  ["aa1be20d-a9fe-55f1-9af5-0689d58db6ce", "Harold J Russo"],
  ["251f692c-4dbc-5250-b4ac-89fab3e99261", "James J Russo"],
  ["da972e80-68dc-5759-aeee-7683878aaf1f", "John M Russo"],
  ["bd673867-a022-51d0-8006-d187c897da8e", "Joseph P Russo"],
  ["d4826a74-9393-5aaf-8c54-0030b741fc4e", "Maria J Russo"],
  ["55af1236-6d1b-5c5e-8d9f-950ae0c96581", "Olgo A Russo"],
  ["30888dca-99b5-55ed-a8e9-9a4769b3fac0", "Pirto Russo"],
  ["63ab570f-a867-506e-9575-0dd8a0ec021d", "Umberto Russo"],
  ["007b2f54-0127-54b6-8263-0ebc7a68d0bc", "Vincent J Russo"],
] as const;

test("Batch 829 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("Charles Russhon profile publishes two prewar employers without guessing their order", async ({ page }) => {
  await page.goto("./people/04888f83-19a5-5f97-8c6c-f6bc05bd21b1/");
  const main = page.locator("main");
  await expect(main).toContainText("National Broadcasting Company");
  await expect(main).toContainText("Republic Pictures");
  await expect(main).toContainText("sound engineer");
  await expect(main).toContainText("documented prewar employer found");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("No reviewed claim currently meets the publication threshold");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Alexander Russo profile treats Pratt as student status and preserves the grade discrepancy", async ({ page }) => {
  await page.goto("./people/efface03-c4b9-5bb8-b19c-56406d7a7c4a/");
  const main = page.locator("main");
  await expect(main).toContainText("Pratt Institute");
  await expect(main).toContainText("student");
  await expect(main).toContainText("enlisted naval personnel");
  await expect(main).toContainText("Specialist First Class");
  await expect(main).toContainText("SP2C");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).not.toContainText("Pratt Institute");
});

test("Theodore Russell profile publishes the Army pathway separately from civilian employment", async ({ page }) => {
  await page.goto("./people/f8594743-6d19-521d-b07f-d6545cff52a6/");
  const immediate = page.getByRole("region", { name: "Immediate pre-OSS affiliation" });
  await expect(immediate).toContainText("United States Army");
  await expect(immediate).toContainText("infantry officer");
  await expect(immediate).toContainText("explicit immediate");
  const civilian = page.getByRole("region", { name: "Last civilian employer before service" });
  await expect(civilian).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(civilian).not.toContainText("United States Army");
});

test("accepted Army identities publish no coded occupations or unmasked identifiers", async ({ page }) => {
  for (const id of [
    "c636ec7e-f39a-5ab5-ba9c-e34dc41cb231",
    "4430b0e9-182f-5e44-bd4a-7dbc9a05c716",
    "d7667caf-7e4e-592f-b724-49376b551e59",
    "2261f780-37bc-5fed-a852-02faa72b3a50",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText(/Official Army/i);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("civilian occupation code");
  }
});

test("two protected-identifier conflicts remain visible and unmerged", async ({ page }) => {
  await page.goto("./people/da972e80-68dc-5759-aeee-7683878aaf1f/");
  let main = page.locator("main");
  await expect(main).toContainText("Marco J. Russo");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Box 668");

  await page.goto("./people/30888dca-99b5-55ed-a8e9-9a4769b3fac0/");
  main = page.locator("main");
  await expect(main).toContainText("incompatible");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("Box 668");
});
