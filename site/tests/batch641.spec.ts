import { expect, test } from "@playwright/test";

test("Batch 641 publishes five high-confidence Army identity crosswalks without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["89b2aba3-fb16-54e8-9bff-50d0583671f5", "Howard R McKee"],
    ["87540427-e043-5313-87cf-d48c48ed3dd8", "Samuel R McKee"],
    ["caf52600-59af-5780-b723-63a8a5bb316f", "A.Q. McKenzie"],
    ["7a8902f5-3e2e-5d0a-a294-fe4fd28c68c9", "Francis W McKenzie"],
    ["b7ded7ef-a3c0-5436-9575-c4dfba76b4a8", "Louis F McKenzie"],
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

test("Batch 641 exposes the James A McKenskey name conflict without a full identifier", async ({
  page,
}) => {
  await page.goto("./people/dd60dccf-c3e9-531a-98fe-2e3f2a33dc09/");
  const main = page.locator("main");
  await expect(page.getByRole("heading", { name: "James A McKenskey", level: 1 })).toBeVisible();
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("Philip Cappella");
  await expect(main).toContainText("Box 509");
  await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
  await expect(
    page.locator(".index-record dl > div").filter({ hasText: "Serial" }).locator("dd"),
  ).toHaveText(/^••••\w{4}$/);
  await expect(main).toContainText("the number is withheld from public output");
});

test("Batch 641 preserves both Stewart L McKenney rows as separate ambiguous profiles", async ({
  page,
}) => {
  const profiles = [
    ["e7a2e42a-3dbe-59b6-8280-ef258ea7f6c1", "••••EP39"],
    ["bfb5330a-d471-5fd6-8edc-be0f506d26e0", "••••3484"],
  ];

  for (const [personId, maskedSerial] of profiles) {
    await page.goto(`./people/${personId}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name: "Stewart L McKenney", level: 1 })).toBeVisible();
    await expect(main).toContainText("ambiguous");
    await expect(main).toContainText("adjacent identical-name and rank row");
    await expect(main).toContainText("different protected identifiers");
    await expect(main).toContainText(
      "Compare both Stewart L. McKenney personnel files in Box 508",
    );
    await expect(
      page.locator(".index-record dl > div").filter({ hasText: "Serial" }).locator("dd"),
    ).toHaveText(maskedSerial);
  }
});

test("rejected Batch 641 namesakes and occupations stay out of public profiles", async ({
  page,
}) => {
  const profiles = [
    ["87540427-e043-5313-87cf-d48c48ed3dd8", ["Mrs. Samuel A. McKee", "treasurer"]],
    ["caf52600-59af-5780-b723-63a8a5bb316f", ["Katheryn McKenzie", "A.G. McKenzie"]],
    ["a7c00d21-8729-53b4-9bed-302b19c45902", ["state senator", "district attorney"]],
    ["f42515e7-f2a0-5cb9-bd6c-71095461cf08", ["Industrial Foremen", "traffic list"]],
    ["f0f67f98-825e-5a38-8f84-5daedafd5fed", ["Industrial Foremen", "traffic list"]],
  ];

  for (const [personId, excludedTerms] of profiles) {
    await page.goto(`./people/${personId}/`);
    const body = await page.locator("main").innerText();
    for (const term of excludedTerms) expect(body).not.toContain(term);
  }
});

test("Batch 641 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,855");
  await expect(page.locator("body")).toContainText("32.81%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".page-hero .lede")).toContainText("9 historically named oil");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McKee");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McKenzie");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McKenskey");
});
