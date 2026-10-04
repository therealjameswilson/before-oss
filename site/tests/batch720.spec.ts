import { expect, test } from "@playwright/test";

const profiles = [
  ["303686b5-c36a-5d3b-a353-cbecf2c92dd9", "Eugene F Omeara"],
  ["227405a9-d795-53f8-b1f6-ca7f0d6197e5", "Walter A Omeara"],
  ["af30a0a0-3426-512d-ba6f-5b827109d950", "Malcolm B Omelia"],
  ["3e555bb5-a65c-58fc-835c-84216b24f812", "George Y Onada"],
  ["87d178a0-7289-5eb5-b09c-33c404f64f1f", "Roger OnaHary"],
  ["ea2975e9-a625-5ed1-8828-9d05cb91d21a", "Jose V Onativia"],
  ["67e08a94-53d8-5a8b-ac78-444cc8e46fdf", "Marie A Onativia"],
  ["c0104324-60ad-58b3-948e-c14611bf046d", "George S Ondreas"],
  ["a9c6d6c5-0030-5f0c-ac92-74ffc956d4ad", "Everett C Oneal"],
  ["5e33d50a-6740-535d-94f3-cc994d00691b", "Kelly Oneal"],
  ["15cd2540-6e6a-588d-84f6-553a2bbc9d43", "Thomas Oneal"],
  ["b742bdfa-4263-5b03-926a-32c66fe70169", "Charles K Oneil"],
  ["85e23bb7-a782-531c-92e1-ba2a85a3c689", "William F Oneil"],
  ["b388deeb-a330-5320-b9f6-cab6a5e4cacf", "Alan L Oneill"],
  ["7320d6b8-c1b8-5589-8721-6c2842f5200c", "Charles B Oneill"],
  ["b7a0f506-1b34-5680-8453-b6e9c254b9de", "Cornelia Oneill"],
  ["8924c849-052c-5dab-9f42-7c2e603274df", "Dermot M Oneill"],
  ["0ac7e7ba-52d9-5b17-9d1c-e4c1f3a50560", "Ellen M Oneill"],
  ["f630e152-c3c0-5dd3-8394-7a55db92007a", "Lucille M Oneill"],
  ["2e871b7f-cc5f-5d93-a981-d7188f93f02b", "Ray B Oneill"],
  ["0d16d2aa-78d3-5e9e-9f2e-d4976df32b3e", "Richard W Oneill"],
  ["bc963bb7-4ebf-558b-b644-3f116da8816b", "Robert G Oneill"],
  ["e8a1c0b0-1d53-55bf-85a1-2559427e56d1", "William F Oneill"],
] as const;

test("Batch 720 publishes all 23 direct profile routes with terminal outcomes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
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

test("Batch 720 qualifies Walter O'Meara's likely immediate employer", async ({ page }) => {
  await page.goto("./people/227405a9-d795-53f8-b1f6-ca7f0d6197e5/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("J. Walter Thompson Co.");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("Benton & Bowles");
  await expect(main).toContainText("Duluth News Tribune");
  await expect(main).toContainText("Walter O'Meara: An Inventory of His Papers");
});

test("Batch 720 publishes Charles O'Neill's occupation without overstating immediacy", async ({ page }) => {
  await page.goto("./people/b742bdfa-4263-5b03-926a-32c66fe70169/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Charles Kendall O'Neill");
  await expect(main).toContainText("Freelance writer");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 720 keeps Cornelia O'Neill's education separate from employment", async ({ page }) => {
  await page.goto("./people/b7a0f506-1b34-5680-8453-b6e9c254b9de/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Cornelia Rockwell O'Neill");
  await expect(main).toContainText("Smith College");
  await expect(main).toContainText("University of Minnesota");
  await expect(main).toContainText("Student");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Batch 720 visibly qualifies Dermot O'Neill's probable identity and civilian chronology", async ({ page }) => {
  await page.goto("./people/8924c849-052c-5dab-9f42-7c2e603274df/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("British Embassy, Tokyo");
  await expect(main).toContainText("Head of security");
  await expect(main).toContainText("Shanghai Municipal Police");
  await expect(main).toContainText("medium");
  await expect(main).toContainText("no service-number or direct personnel-file bridge");
});

test("Batch 720 preserves Alan O'Neill's protected-identifier conflict", async ({ page }) => {
  await page.goto("./people/b388deeb-a330-5320-b9f6-cab6a5e4cacf/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("Bruce W Johnson");
});

test("Batch 720 publishes exact rebuilt coverage without changing the oil directory", async ({ page }) => {
  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,598");
  await expect(main).toContainText("40.09%");
  await expect(main).toContainText("14,336");
  await expect(main).toContainText("728");
  await expect(main).toContainText("328");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Walter A Omeara");
});
