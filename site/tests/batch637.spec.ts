import { expect, test } from "@playwright/test";

test("Batch 637 publishes qualified Army identities without inventing employers", async ({
  page,
}) => {
  const profiles = [
    ["c7305cd7-23c2-54f5-989e-7a2156333733", "Lawerence B McFaddin"],
    ["10aeb551-a334-5bf2-966a-44b1188202ff", "Neil McFadyen"],
    ["6b8e782a-5b29-5d33-a730-501bf048dbc7", "Dallas A McFarland"],
    ["835bb837-5b5f-5ccd-a6a5-68108180ebb5", "Jack McFarland"],
    ["c731cbb9-43ca-55d2-840e-98d9265dd4c9", "Frank McGavock"],
    ["80460459-4d0f-5e93-996f-7d5c203d9cfe", "James A McGay"],
    ["6c35b80e-0504-545c-985a-97bffa274e55", "John R McGee"],
    ["aee6f423-0fe3-5673-acf7-828279715655", "Philip McGevna"],
    ["2173b96f-f737-577e-a6ec-2aa37a333e42", "Harvey D McGhee"],
    ["88d785e5-31e0-5452-bfd1-8ea5e71cd9ac", "William M McGhee"],
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

test("Batch 637 preserves sourced name and code anomalies", async ({ page }) => {
  await page.goto("./people/c7305cd7-23c2-54f5-989e-7a2156333733/");
  await expect(page.locator("main")).toContainText("Lawerence/Lawrence");

  await page.goto("./people/c731cbb9-43ca-55d2-840e-98d9265dd4c9/");
  await expect(page.locator("main")).toContainText("Frank/Francis");

  await page.goto("./people/835bb837-5b5f-5ccd-a6a5-68108180ebb5/");
  await expect(page.locator("main")).toContainText("MCTFARLAND");

  await page.goto("./people/88d785e5-31e0-5452-bfd1-8ea5e71cd9ac/");
  await expect(page.locator("main")).toContainText("anomalous");
  await expect(page.locator("main")).toContainText("remains uninterpreted");
});

test("Batch 637 keeps McAragle and McGaragle separate and ambiguous", async ({ page }) => {
  await page.goto("./people/4d6eb7f9-83b2-567a-aa76-25683a32d761/");
  await expect(page.getByRole("heading", { name: "William C McGaragle", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("ambiguous");
  await expect(page.locator("main")).toContainText("Boxes 496 and 505");
  await expect(page.locator("main")).toContainText("No publishable pre-OSS affiliation is recorded yet");

  await page.goto("./people/5925506f-0976-5138-9c6a-794f152a31d9/");
  await expect(page.getByRole("heading", { name: "William C McAragle", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("ambiguous");
});

test("rejected Batch 637 newspaper namesakes stay out of public profiles", async ({ page }) => {
  await page.goto("./people/f134f978-8244-5d89-9ccb-156d80d0bcb6/");
  await expect(page.locator("main")).not.toContainText("Charles White McGehee");
  await expect(page.locator("main")).not.toContainText("Summit Sun");

  await page.goto("./people/74bf9c95-6e09-5abd-91f7-030c8f9a73ef/");
  await expect(page.locator("main")).not.toContainText("James J. McGee");
  await expect(page.locator("main")).not.toContainText("James T. McGee");

  await page.goto("./people/2eddcd14-4226-55e9-9e42-22e3f23d0bdb/");
  await expect(page.locator("main")).not.toContainText("Mary Helen McGee");
  await expect(page.locator("main")).not.toContainText("Mary L. McGee");

  await page.goto("./people/42986f6e-6650-55bc-8600-c28ba3928a8a/");
  await expect(page.locator("main")).not.toContainText("William J. McGarry");
});

test("Batch 637 publishes the exact coverage checkpoint and retains the oil category", async ({
  page,
}) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("7,763");
  await expect(page.locator("body")).toContainText("32.43%");

  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("McFaddin");
  await expect(page.locator(".oil-directory__list")).not.toContainText("McGhee");
});
