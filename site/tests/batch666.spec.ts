import { expect, test } from "@playwright/test";

const profiles = [
  ["3bae7554-ba84-5c9f-b246-1431eb0519ab", "Carl W Mitchell"],
  ["16f24151-03d6-544a-a4f2-94000e12a771", "David H Mitchell"],
  ["4e5c8f24-7602-59cd-998b-5d2be0b6940c", "Denis M Mitchell"],
  ["37399a80-6240-5c3f-b718-57a85ffd0d5e", "Dorothea D Mitchell"],
  ["e1042479-a979-5795-a107-720647b9b507", "Dorothy D Mitchell"],
  ["330f31f3-63f0-5532-bfe3-94008001fadc", "Earl L Mitchell Jr."],
  ["2097fe98-6fd2-5931-8f26-f0b167c3b30c", "Florence L Mitchell"],
  ["d89f614f-9424-5670-badd-5b1312ad1cd1", "George T Mitchell"],
  ["61c7f2f1-3868-5166-a90f-15872c4cfb0f", "James Mitchell Jr."],
  ["6b80d7a0-23da-5790-a6a0-593070735c92", "John W Mitchell"],
  ["43edc966-810d-5a8d-934d-e6c721f4f4ee", "Lillian T Mitchell"],
  ["e4e44408-31b0-592a-9d0d-69c1a0b8e4c5", "Mack C Mitchell"],
  ["0a33eac8-0e22-5ff2-a239-2ffd4bc65250", "Marion Mitchell"],
  ["8fb6dabc-739e-5cc5-bd65-a18c4d9854f4", "Mary A Mitchell"],
  ["f27d328d-1f0d-542d-abc7-f326fb21257e", "Michael G Mitchell"],
  ["443fc218-df96-51aa-a606-7a53206962e1", "Stanley F Mitchell"],
  ["e4284aac-8055-5bbf-b097-738155ced200", "Thomas J Mitchell"],
  ["505d1194-669f-53ed-961d-dccd38e0bad9", "William E Mitchell"],
  ["62e05e85-6a22-523a-b299-2d2bbc2980cd", "Anne F Mitcheson"],
  ["f9ef458a-852e-52b1-bf9d-a2a0130ede2e", "Louise Mithoff"],
  ["dec99106-8f8c-509a-80fb-ba5f4c513d57", "John T Mitrou"],
  ["5344371d-4453-5dc9-9e95-21572e8b6e76", "Jimmie W Mitrougenis"],
] as const;

test("Batch 666 publishes all 22 direct profile routes", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
  }
});

test("Batch 666 publishes Anne Mitcheson's documented pre-OSS chronology", async ({ page }) => {
  await page.goto("./people/62e05e85-6a22-523a-b299-2d2bbc2980cd/");
  const main = page.locator("main");

  await expect(main).toContainText("Anne F Mitcheson (Henry)");
  await expect(main).toContainText("Wartime censorship, Liverpool, Manchester & Bermuda");
  await expect(main).toContainText("Four chiefs of staff, Washington");
  await expect(main).toContainText("probable immediate");
  await expect(main).toContainText("Sherborne School for Girls Old Girls' Union Membership List");
});

test("Batch 666 does not misclassify Anne Mitcheson's post-OSS oil-company work", async ({ page }) => {
  await page.goto("./people/62e05e85-6a22-523a-b299-2d2bbc2980cd/");

  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("Asiatic Petroleum");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("Asiatic Petroleum");
  await expect(page.locator('section[aria-labelledby="earlier-affiliations"]')).not.toContainText("Asiatic Petroleum");

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  await expect(oilList).not.toContainText("Anne F Mitcheson");
});

test("Batch 666 publishes three protected-identifier identities without invented employers", async ({ page }) => {
  const armyMatches = [
    ["4e5c8f24-7602-59cd-998b-5d2be0b6940c", "Denis M Mitchell"],
    ["330f31f3-63f0-5532-bfe3-94008001fadc", "Earl L Mitchell Jr."],
    ["e4e44408-31b0-592a-9d0d-69c1a0b8e4c5", "Mack C Mitchell"],
  ] as const;

  for (const [id, name] of armyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).not.toContainText("Verified employer");
  }
});

test("Batch 666 keeps Dorothea and Dorothy Mitchell separate", async ({ page }) => {
  await page.goto("./people/37399a80-6240-5c3f-b718-57a85ffd0d5e/");
  await expect(page.getByRole("heading", { name: "Dorothea D Mitchell", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("715f100e-2107-5a09-a4d5-1b7405fd2b4e");
  await expect(page.locator("main")).not.toContainText("Mitchell | Dorothy | D");

  await page.goto("./people/e1042479-a979-5795-a107-720647b9b507/");
  await expect(page.getByRole("heading", { name: "Dorothy D Mitchell", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("5fba586d-5881-5b3c-9fb0-b785d80d97c8");
  await expect(page.locator("main")).not.toContainText("Mitchell | Dorothea | D");
});

test("Batch 666 withholds a plausible John W Mitchell namesake", async ({ page }) => {
  await page.goto("./people/6b80d7a0-23da-5790-a6a0-593070735c92/");
  const main = page.locator("main");

  await expect(main).toContainText("North Carolina agricultural agent");
  await expect(main).toContainText("no reliable result after protocol");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 666 excludes Louise Mithoff's postwar employment from pre-OSS findings", async ({ page }) => {
  await page.goto("./people/f9ef458a-852e-52b1-bf9d-a2a0130ede2e/");
  const main = page.locator("main");

  await expect(main).toContainText("no reliable result after protocol");
  await expect(page.locator('section[aria-labelledby="immediate-affiliation"]')).not.toContainText("War Department");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText("War Department");
  await expect(main).not.toContainText("Verified employer");
});

test("Batch 666 updates exact coverage and preserves the evidence-scoped oil category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,402");
  await expect(page.locator("body")).toContainText("35.10%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./people/");
  const category = page.locator(".featured-directory-category");
  await expect(category).toBeVisible();
  await expect(category.locator("li")).toHaveCount(8);
  await category.getByRole("button", { name: /View category/ }).click();
  await expect(page.locator("#result-summary")).toContainText("8 results");

  await page.goto("./oil-companies/");
  await expect(page.getByRole("region", { name: "Oil company work list" }).locator(".oil-directory__person")).toHaveCount(8);
});
