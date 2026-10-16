import { expect, test } from "@playwright/test";

const profiles = [
  ["fd92421b-6396-586a-8a68-eec2201d2a14", "Dagmar S Scott"],
  ["6cc9c30f-6efe-577d-b38b-e05c11e93c7f", "Delbert Scott"],
  ["c36ba4be-432a-5f37-8a0c-9969a5ddea99", "Dharles R Scott"],
  ["4233dc13-1d6f-589c-a0e7-e96aef57cf37", "Edward F Scott"],
  ["728ad677-3ba8-5ba6-a864-7b299a2f212e", "Edward F Scott"],
  ["8ea4f830-8745-5dad-9473-ecb426682803", "Edward F Scott"],
  ["db781a07-4d76-5d69-bf6b-6b0728d9ddea", "Franklin D Scott"],
  ["eec056a4-0710-5a3e-b9cb-ac3aa32c475c", "George Scott"],
  ["627d61f1-f7a9-576b-a554-34d7ad3e83da", "George H Scott"],
  ["7d142c98-a8b5-5d21-bfec-2deac9fffec8", "Gordon Scott"],
  ["3d3bc9ba-20a1-5221-a729-4ec74aadd886", "Herbert W Scott"],
  ["eef51b68-03c8-59aa-9534-a0a77dd8f118", "James H Scott"],
  ["bbbdafdd-e7d7-51b5-885e-90a588a097b3", "James M Scott"],
  ["73c57dfe-a03e-59b9-bc78-6aec8459651d", "Janice L Scott"],
  ["1ef47a4c-c629-575e-91df-3e10f99db82c", "Jesse W Scott"],
  ["b48ee87a-b022-5bae-91d8-7ccb19b96072", "John L Scott"],
  ["6e9ef929-aaa5-56f0-9b3d-bd690d83fa87", "Lillie Scott"],
  ["52b6c3fa-6286-53a7-9705-1c3f18f9016c", "Marianne Scott"],
  ["79da1722-c555-55c3-82c6-f8f0530fef35", "Marianne Scott"],
  ["91f4463e-ff0c-5b42-9811-9246f8432d80", "Mary C Scott"],
  ["7e882c6b-7f23-5a74-bcae-f95871c879d6", "R W Scott"],
  ["976d5fcc-d08d-51a5-8eb0-757855b60100", "Richard P Scott"],
  ["88f28d1a-ff4c-5fd8-a539-f4ea08c7d4a7", "Robert F Scott"],
] as const;

test("Batch 855 publishes all 23 profiles with terminal outcomes and masked identifiers", async ({ page }) => {
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

test("the three official Army matches publish identity evidence only", async ({ page }) => {
  const matches = [
    ["6cc9c30f-6efe-577d-b38b-e05c11e93c7f", "Delbert Scott"],
    ["627d61f1-f7a9-576b-a554-34d7ad3e83da", "George H Scott"],
    ["bbbdafdd-e7d7-51b5-885e-90a588a097b3", "James M Scott"],
  ] as const;

  for (const [id, name] of matches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText("requires archival review");
    await expect(main).toContainText("Electronic Army Serial Number Merged File");
    await expect(main).toContainText("Identity crosswalk only");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main.getByRole("heading", { name: /Army Serial Number/i })).toHaveCount(0);
    await expect(main).toContainText(name);
  }
});

test("repeated Edward and Marianne rows remain separate and visibly ambiguous", async ({ page }) => {
  const repeated = [
    ["4233dc13-1d6f-589c-a0e7-e96aef57cf37", "duplicate-81799cd3a1e3"],
    ["728ad677-3ba8-5ba6-a864-7b299a2f212e", "duplicate-81799cd3a1e3"],
    ["8ea4f830-8745-5dad-9473-ecb426682803", "duplicate-81799cd3a1e3"],
    ["52b6c3fa-6286-53a7-9705-1c3f18f9016c", "duplicate-4a521574c9c4"],
    ["79da1722-c555-55c3-82c6-f8f0530fef35", "duplicate-4a521574c9c4"],
  ] as const;

  for (const [id, duplicateGroup] of repeated) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusambiguous");
    await expect(main).toContainText(`Duplicate group${duplicateGroup}`);
    await expect(main).toContainText("preserve the separate rows");
    await expect(page).toHaveURL(new RegExp(`/people/${id}/$`));
  }
});

test("plausible Scott namesakes remain rejected rather than becoming affiliations", async ({ page }) => {
  await page.goto("./people/db781a07-4d76-5d69-bf6b-6b0728d9ddea/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("plausible exact-name lead");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main.getByRole("heading", { name: "Northwestern University" })).toHaveCount(0);

  await page.goto("./people/6e9ef929-aaa5-56f0-9b3d-bd690d83fa87/");
  main = page.locator("main");
  await expect(main).toContainText("wartime aircraft-worker obituary");
  await expect(main).toContainText("candidate was not accepted");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/976d5fcc-d08d-51a5-8eb0-757855b60100/");
  main = page.locator("main");
  await expect(main).toContainText("award record for a Major Richard P. Scott was rejected");
  await expect(main).toContainText("does not match the protected identifier");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");

  await page.goto("./people/88f28d1a-ff4c-5fd8-a539-f4ea08c7d4a7/");
  main = page.locator("main");
  await expect(main).toContainText("different Robert F. Scott candidates");
  await expect(main).toContainText("neither supplies an OSS or index-identifier bridge");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});
