import { expect, test } from "@playwright/test";

const profiles = [
  ["89f19086-492c-5c52-91b3-0aeaec0ea86c", "Arthur R Miller"],
  ["a82bcc4d-220b-5945-a1b2-c5bfeab4006d", "Bernard L Miller"],
  ["a2c0081e-0313-54ca-bbf8-ee640e89602d", "Betty J Miller"],
  ["43ffcb58-3017-568b-be97-687fadc799c1", "Carl H Miller"],
  ["6c7fe758-44de-5d09-9642-bcce6d0972bc", "Carl W Miller"],
  ["e56f4974-bee5-557c-a3db-4825e25ac506", "Charles H Miller"],
  ["734aa596-3490-5b88-8702-42b7ab128136", "Claire D Miller"],
  ["eb36ab35-5c04-5e52-9fe3-87d05de1ec2c", "Clarence A Miller"],
  ["26eea0ed-57af-5003-88f2-331405de0035", "David Miller"],
  ["4d33c365-05b2-53df-bd93-fe94c58a3a69", "Dora L Miller"],
  ["099fd270-b304-5962-96fd-fc3abb231416", "Doris N Miller"],
  ["d67d590a-9939-5b81-9d0a-6c4280e2d367", "E W Miller"],
  ["2154e8d3-43af-53bc-94d1-2141580628b9", "Earle R Miller"],
  ["e538b168-ffc8-59ce-8cf5-a8f7906584ca", "Eda D Miller"],
  ["9fff63a9-bfd2-5716-b1cd-2de4b1647434", "Edward C Miller"],
  ["27670962-7099-5e2c-8b52-c15b5cee1ab8", "Edward N Miller"],
  ["e68d6e7e-18d3-53a4-b5df-d96bc31e7e0b", "Edwin Miller"],
  ["0be84208-de0a-52a0-9049-1a726958d1e0", "Edwin J Miller"],
  ["4fdff0cd-2443-5b03-bcc7-223b59cbfebf", "Eli D Miller"],
  ["e948262b-991b-5ac4-b652-0f9eba78e2a4", "Ernest L Miller"],
  ["a1d1ef8e-9c1d-5a00-bb6a-96c9a49cb939", "Evelyn Miller"],
  ["d5ae5010-380a-5892-adb2-86b5396651aa", "Francis Miller"],
] as const;

test("Batch 659 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 659 publishes the Bernard-Benard spelling conflict", async ({ page }) => {
  await page.goto("./people/a82bcc4d-220b-5945-a1b2-c5bfeab4006d/");
  const main = page.locator("main");

  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Benard");
  await expect(main).toContainText("Box 524");
  await expect(main).toContainText("not silently corrected");
});

test("Batch 659 publishes the Eli Miller-Charles Tallent conflict", async ({ page }) => {
  await page.goto("./people/4fdff0cd-2443-5b03-bcc7-223b59cbfebf/");
  const main = page.locator("main");

  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Charles E. Tallent");
  await expect(main).toContainText("Box 524");
  await expect(main).toContainText("before resolving identity");
});

test("Batch 659 keeps identity-only Army evidence separate from employment", async ({ page }) => {
  await page.goto("./people/6c7fe758-44de-5d09-9642-bcce6d0972bc/");
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("does not establish a named employer");
  await expect(main).toContainText("requires archival review");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 659 rejects the prominent Francis Pickens Miller namesake", async ({ page }) => {
  await page.goto("./people/d5ae5010-380a-5892-adb2-86b5396651aa/");
  const main = page.locator("main");

  await expect(main).toContainText("high confidence");
  await expect(main).toContainText("Francis Pickens Miller");
  await expect(main).toContainText("conflict in rank or lack the identifier");
});

test("Batch 659 updates exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,250");
  await expect(page.locator("body")).toContainText("34.46%");

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
