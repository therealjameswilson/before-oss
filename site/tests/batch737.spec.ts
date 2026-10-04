import { expect, test } from "@playwright/test";

const profiles = [
  ["78ace810-659f-5c08-a185-7b357de4bd84", "Angeline Pascuzzi"],
  ["a00c87ec-3654-52bd-a19c-3a728e8856a0", "Arthur Pashcow"],
  ["93b72db4-104b-5d84-ac5b-24a1dbb5e01e", "Kalman Pasichnyek"],
  ["5dd51dbb-6b82-5fb0-a971-6a63a8150d92", "Louise A Pasnick"],
  ["4a12b989-1ede-5949-9331-bb4c98bec089", "Augustine P Pasquale"],
  ["ba5a591a-c19e-50b3-b523-3d94f544948f", "Frank A Pasquale"],
  ["096e748d-1038-586b-948f-87bb5c76141c", "Francesco Pasqualigo"],
  ["76e02644-22a3-5a05-857c-d45b3a96818d", "Felix Pasqualino"],
  ["1d3cd3cc-c9c6-5fbe-a80e-d0e6b29b80c2", "Ruth Pass"],
  ["799b51e5-06d4-5bab-8ed6-5f9479c6f65a", "Cosmo Passalacqua"],
  ["dd2f44ac-1dd6-501c-b331-dda37c71ee23", "Sebastian J Passanesi"],
  ["40fc8329-c546-5397-9f2c-10dc9aadb050", "Michael H Passarella"],
  ["b7df5cde-d357-5b31-8417-cb8e677bbe46", "David A Passet"],
  ["2e219b1d-a32f-550e-afa2-d76369f46b2e", "Andre Passy"],
  ["2233645f-534d-5b32-a0b6-61c6a0d1b351", "John Pastilock"],
  ["95e0adb5-dfa7-52ba-8c37-d48ea2b52e1e", "Morris A Pastor"],
  ["01e7f51b-d49a-539a-ba6f-549bcbbd1c02", "Connie Patane"],
  ["3671a7b2-e04c-513a-a0c5-1e36ff6084a1", "Frances F Patch"],
  ["6d48067d-c595-5292-a813-6dce64b0f743", "Lloyd E Patch"],
  ["ecddb149-30c0-564e-883b-7e5957e29da5", "John J Pater"],
  ["bbb2af68-440b-5124-b259-a523da00e896", "Paul J Paterni"],
  ["11b03185-aeda-58ae-bf3f-a31cf5f3a8c6", "Paul J Paterni"],
  ["1fe5474a-b8b6-534a-8654-4034f80abf3c", "Jane Paterson"],
] as const;

test("Batch 737 publishes all 23 page-359 profiles with terminal dispositions", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto("./people/" + id + "/");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serialValues = await main
      .locator("dt")
      .filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]")
      .allTextContents();
    for (const value of serialValues) expect(value).not.toMatch(/^\d{4,8}$/);
  }
});

test("Batch 737 publishes Paterni's three-part chronology without merging the two index rows", async ({ page }) => {
  await page.goto("./people/bbb2af68-440b-5124-b259-a523da00e896/");
  let main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText("United States Army");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText("United States Secret Service");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("Veterans Administration");
  await expect(main).toContainText("paint-spreader occupation belongs to Michael A. Grandinetti");
  await expect(main).toContainText("duplicate-");

  await page.goto("./people/11b03185-aeda-58ae-bf3f-a31cf5f3a8c6/");
  main = page.locator("main");
  await expect(main).toContainText("probable");
  await expect(main).toContainText("enlisted man and was commissioned overseas");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).not.toContainText("United States Army");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).not.toContainText("United States Secret Service");
  await expect(main).toContainText("duplicate-");
});

test("Batch 737 labels Passanesi's university link as student evidence, not employment", async ({ page }) => {
  await page.goto("./people/dd2f44ac-1dd6-501c-b331-dda37c71ee23/");
  const main = page.locator("main");
  await expect(main).toContainText("commissioned marine corps officer");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("Catholic University of America");
  await expect(main.locator("section[aria-labelledby='earlier-affiliations']")).toContainText("Architecture student");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
});

test("Batch 737 keeps identity-only evidence separate from employer evidence", async ({ page }) => {
  for (const id of [
    "a00c87ec-3654-52bd-a19c-3a728e8856a0",
    "93b72db4-104b-5d84-ac5b-24a1dbb5e01e",
    "ba5a591a-c19e-50b3-b523-3d94f544948f",
    "76e02644-22a3-5a05-857c-d45b3a96818d",
    "40fc8329-c546-5397-9f2c-10dc9aadb050",
    "b7df5cde-d357-5b31-8417-cb8e677bbe46",
    "01e7f51b-d49a-539a-ba6f-549bcbbd1c02",
    "6d48067d-c595-5292-a813-6dce64b0f743",
    "ecddb149-30c0-564e-883b-7e5957e29da5",
  ]) {
    await page.goto("./people/" + id + "/");
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
  }
});

test("Batch 737 exposes the Pastilock conflict and preserves printed anomalies", async ({ page }) => {
  await page.goto("./people/2233645f-534d-5b32-a0b6-61c6a0d1b351/");
  let main = page.locator("main");
  await expect(main).toContainText("conflicting");
  await expect(main).toContainText("PAST OCK JOHN");
  await expect(main).toContainText("critical");

  await page.goto("./people/40fc8329-c546-5397-9f2c-10dc9aadb050/");
  await expect(page.locator("main")).toContainText("Extracte");

  await page.goto("./people/6d48067d-c595-5292-a813-6dce64b0f743/");
  await expect(page.locator("main")).toContainText("Cpt");

  await page.goto("./people/a00c87ec-3654-52bd-a19c-3a728e8856a0/");
  main = page.locator("main");
  await expect(main).toContainText("Box 587");
});

test("Batch 737 rebuilds exact coverage while preserving the oil-company category", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,985");
  await expect(main).toContainText("41.71%");
  await expect(main).toContainText("13,949");
  await expect(main).toContainText("747");
  await expect(main).toContainText("334");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
});
