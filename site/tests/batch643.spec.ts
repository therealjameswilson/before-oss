import { expect, test } from "@playwright/test";

test("Batch 643 publishes eight high-confidence identity outcomes without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["6cd113ce-3751-5a09-b1e2-ac656e2a578c", "Thomas J McNamara"],
    ["fad5c77b-2530-5e2a-8492-11170f289b77", "William D McNeely"],
    ["494364ee-0148-5275-b1c7-c7d9d4c4ef82", "Edward F McNeil"],
    ["84ecd8d1-be9d-5602-b428-39452050ce43", "Volney G McNeill"],
    ["e2efb896-63f7-5dea-96b5-470d29a2a9de", "Harry P McNickle"],
    ["50bc7aa2-4d18-5aba-b532-195174995035", "John J McNulty"],
    ["10c8b5ad-b31c-5bf9-9d9a-db7595fe5540", "Joseph S McNulty"],
    ["172783fb-b807-5847-aa14-ffb843f67e35", "Joseph G McNulty"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText("protected identifier");
    await expect(page.locator("main")).toContainText(
      "No publishable pre-OSS affiliation is recorded yet",
    );
  }
});

test("Batch 643 exposes the Coy I McNeil name conflict", async ({ page }) => {
  await page.goto("./people/2df2c498-74e4-588e-9d85-43e2fdf7a147/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "Coy I McNeil", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("MC VIEL/COY");
  await expect(main).toContainText("Box 512");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(
    page.locator(".index-record dl > div").filter({ hasText: "Serial" }).locator("dd"),
  ).toHaveText(/^••••\w{4}$/);
  await expect(main).toContainText("the number is withheld from public output");
});

test("Batch 643 preserves the McNearnry-McNerney duplicate boundary", async ({ page }) => {
  const profiles = [
    ["cae1845d-65c0-5bfb-ba5a-1e3494d35551", "James E McNearnry"],
    ["86bbdb79-84c5-5ce5-81aa-58de02c2d582", "James E McNerney"],
  ];

  for (const [personId, displayName] of profiles) {
    await page.goto(`./people/${personId}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: displayName, level: 1 })).toBeVisible();
    await expect(main).toContainText("probable");
    await expect(main).toContainText("separate");
    await expect(main).toContainText("Box 512");
    await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  }
});

test("Batch 643 rejects namesake occupations and postwar public figures", async ({ page }) => {
  const excludedProfiles: Array<[string, string[]]> = [
    ["c0ed47cf-000e-5ac2-aaae-21cf60a9c056", ["labor prisoner", "dynamiting"]],
    ["db06d14f-5735-5fb5-9b77-f4db9b7301d0", ["Defense Secretary", "Trainman"]],
    ["50bc7aa2-4d18-5aba-b532-195174995035", ["Fire Coordinator", "Firemen's Association"]],
    ["e2de50f6-5979-5fdf-9104-22d721c13f82", ["truck driver", "William C. McNeil"]],
  ];

  for (const [personId, excludedTerms] of excludedProfiles) {
    await page.goto(`./people/${personId}/`);
    const body = await page.locator("main").innerText();
    for (const term of excludedTerms) expect(body).not.toContain(term);
  }
});

test("Batch 643 publishes the exact coverage checkpoint and retains the top oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,899");
  await expect(page.locator("body")).toContainText("33.00%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".page-hero .lede")).toContainText("9 historically named oil");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McNamara");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McNulty");
});
