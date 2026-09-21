import { expect, test } from "@playwright/test";

test("Army crosswalks improve Mayer identities without inventing employers", async ({ page }) => {
  const cases = [
    ["1364045d-eec0-547c-96b1-8b50f5ea90d3", "Charles A Mayer"],
    ["7ed4cef0-5c5c-5b9a-b3aa-538a30dd11c9", "Emil Mayer"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText(/official Army bulk entry/i);
    await expect(page.locator("main")).toContainText(/occupation code.*not treated/i);
    await expect(page.locator("main")).toContainText(
      "No publishable pre-OSS affiliation is recorded yet",
    );
  }
});

test("common-name Charles Mayer stays unresolved without publishing rejected namesakes", async ({ page }) => {
  await page.goto("./people/d227219c-fd99-5084-b69e-397f1ea483b3/");
  await expect(page.getByRole("heading", { name: "Charles Mayer", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("unresolved");
  await expect(page.locator("main")).toContainText("Research is in progress");
  await expect(page.locator("main")).not.toContainText("633 Fulton");
  await expect(page.locator("main")).toContainText(
    "No publishable pre-OSS affiliation is recorded yet",
  );
});

test("Batch 624 publishes the exact coverage checkpoint", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,478");
  await expect(page.locator("body")).toContainText("31.24%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Charles A Mayer");
  await expect(page.locator(".oil-directory__list")).not.toContainText("Emil Mayer");
});
