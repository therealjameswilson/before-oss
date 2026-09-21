import { expect, test } from "@playwright/test";

test("Fairbank's probable COI predecessor stays separate from Harvard employment", async ({ page }) => {
  await page.goto("./people/e091453b-28d3-5f35-a907-415c62dfc364/");
  await expect(page.getByRole("heading", { name: "John King Fairbank", level: 1 }))
    .toBeVisible();
  await expect(page.getByRole("link", { name: "Page 140" })).toBeVisible();

  const immediate = page.locator('section[aria-labelledby="immediate-affiliation"]');
  await expect(immediate).toContainText("Coordinator of Information");
  await expect(immediate).toContainText("exact position not established");
  await expect(immediate).toContainText("medium");
  await expect(immediate).not.toContainText("Harvard University");

  const civilian = page.locator('section[aria-labelledby="civilian-employer"]');
  await expect(civilian).toContainText("Harvard University");
  await expect(civilian).not.toContainText("Coordinator of Information");
  await expect(page.locator('section[aria-labelledby="evidence"]'))
    .toContainText("John King Fairbank: Present at the Creation");
});

test("two printed Ruth E Evans rows remain separate public profiles", async ({ page }) => {
  const ids = [
    "6bf06cbd-5227-5e28-a6b8-5a96808861b3",
    "79be4725-9ae5-5b44-a21b-d1ecfe3fe10a",
  ];
  for (const id of ids) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: "Ruth E Evans", level: 1 }))
      .toBeVisible();
    await expect(page.getByRole("link", { name: "Page 139" })).toBeVisible();
    await expect(page.locator("main")).toContainText("Duplicate group");
    await expect(page.locator("main")).toContainText("duplicate-e3ed6158141e");
  }
});
