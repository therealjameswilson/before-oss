import { expect, test } from "@playwright/test";

const profiles = [
  ["059c7686-17e6-5979-9fa9-8f06e6814c7d", "George R Moore", "534"],
  ["cb755cb4-3f05-546d-a755-c88b12fee087", "Hannah Moore", "534"],
  ["60c55a5f-5113-53d7-9975-171c616e62ed", "Harold E Moore", "535"],
  ["f6441819-f535-5f8b-bed4-b9216502ca21", "Henry W Moore", "535"],
  ["3a6a81a9-77d8-5479-bc1f-32850ae5ae95", "James L Moore", "535"],
  ["820e515a-56df-5554-90bf-c5de2e3d0a95", "James W Moore", "535"],
  ["51af5943-67f7-536a-8529-a7d4cfe7c258", "John R Moore", "535"],
  ["53508f11-4b44-5eec-8c74-f486f53efb04", "John H Moore", "535"],
  ["df5091d8-a335-539c-912e-d6f4505af7a2", "John F Moore", "535"],
  ["1cc5accc-3991-5803-906d-f6121227b930", "Justine Moore", "535"],
  ["627d49d0-ac16-52d6-a8d2-cf47d19608db", "Margeret A Moore", "535"],
  ["cd7c88e7-a225-5ff1-a458-3d0f60f13397", "Milton Moore", "535"],
  ["81ff37dd-7a34-5a60-b2a9-1d5d3f3cbc95", "Phyllis Y Moore", "535"],
  ["0faf554e-976b-57ab-9feb-698ea379d2a9", "Prentis Moore", "535"],
  ["15e4118f-87ff-5070-845a-2796f75f4d3e", "Price W Moore", "535"],
  ["656e2e90-6d8d-593e-b5b4-a391f2154f8e", "Raymond E Moore", "535"],
  ["27e7d989-9ddb-5025-9f0c-d666f29c55cc", "Richard H Moore", "535"],
  ["75418064-7006-5ab3-9feb-ac7443965ab0", "Robert J Moore", "535"],
  ["2e6aa050-ccd2-5c55-ace8-5c328d529b4d", "Robert K Moore", "535"],
  ["02077cfc-8c2b-5c79-a0cc-d6009c6458e2", "Robert B Moore", "535"],
  ["b150101e-1f27-58ac-894a-3e5b0cbb7e23", "Robert D Moore", "535"],
  ["a0fbfcc1-acc9-5fb9-bf8b-48d6bc96effa", "Roy D Moore", "535"],
  ["989c6c9f-7a6f-5de9-a070-2b27a5a70fdc", "Ruben E Moore", "535"],
  ["b3f021ad-1e36-5023-85e3-9c5798a275c9", "Russell C Moore", "535"],
] as const;

const armyMatches = [
  ["059c7686-17e6-5979-9fa9-8f06e6814c7d", "George R Moore", "827"],
  ["3a6a81a9-77d8-5479-bc1f-32850ae5ae95", "James L Moore", "072"],
  ["53508f11-4b44-5eec-8c74-f486f53efb04", "John H Moore", "758"],
  ["df5091d8-a335-539c-912e-d6f4505af7a2", "John F Moore", "893"],
  ["0faf554e-976b-57ab-9feb-698ea379d2a9", "Prentis Moore", "170"],
  ["15e4118f-87ff-5070-845a-2796f75f4d3e", "Price W Moore", "525"],
  ["27e7d989-9ddb-5025-9f0c-d666f29c55cc", "Richard H Moore", "094"],
  ["b150101e-1f27-58ac-894a-3e5b0cbb7e23", "Robert D Moore", "091"],
  ["989c6c9f-7a6f-5de9-a070-2b27a5a70fdc", "Ruben E Moore", "099"],
  ["b3f021ad-1e36-5023-85e3-9c5798a275c9", "Russell C Moore", "688"],
] as const;

const unresolved = [
  ["cb755cb4-3f05-546d-a755-c88b12fee087", "Hannah Moore"],
  ["60c55a5f-5113-53d7-9975-171c616e62ed", "Harold E Moore"],
  ["f6441819-f535-5f8b-bed4-b9216502ca21", "Henry W Moore"],
  ["820e515a-56df-5554-90bf-c5de2e3d0a95", "James W Moore"],
  ["51af5943-67f7-536a-8529-a7d4cfe7c258", "John R Moore"],
  ["1cc5accc-3991-5803-906d-f6121227b930", "Justine Moore"],
  ["627d49d0-ac16-52d6-a8d2-cf47d19608db", "Margeret A Moore"],
  ["cd7c88e7-a225-5ff1-a458-3d0f60f13397", "Milton Moore"],
  ["81ff37dd-7a34-5a60-b2a9-1d5d3f3cbc95", "Phyllis Y Moore"],
  ["656e2e90-6d8d-593e-b5b4-a391f2154f8e", "Raymond E Moore"],
  ["75418064-7006-5ab3-9feb-ac7443965ab0", "Robert J Moore"],
  ["2e6aa050-ccd2-5c55-ace8-5c328d529b4d", "Robert K Moore"],
  ["02077cfc-8c2b-5c79-a0cc-d6009c6458e2", "Robert B Moore"],
  ["a0fbfcc1-acc9-5fb9-bf8b-48d6bc96effa", "Roy D Moore"],
] as const;

test("Batch 674 publishes all 24 direct profile routes", async ({ page }) => {
  for (const [id, name, box] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("Page 327");
    await expect(page.locator("main")).toContainText(`Archive box${box}`);
  }
});

test("Batch 674 publishes ten protected-identifier identities without employer inference", async ({ page }) => {
  for (const [id, name, privateOccupationCode] of armyMatches) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("high confidence");
    await expect(main).toContainText("nonshared protected identifier");
    if (id === "27e7d989-9ddb-5025-9f0c-d666f29c55cc") {
      await expect(main).toContainText("No publishable pre-OSS affiliation is recorded yet");
    } else {
      await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    }
    await expect(main).not.toContainText("Verified employer");
    await expect(main).not.toContainText(`occupation code ${privateOccupationCode}`);
    await expect(main).not.toContainText(`civilian_occupation_code=${privateOccupationCode}`);
  }
});

test("Batch 674 keeps Richard Moore's rank disagreement visible", async ({ page }) => {
  await page.goto("./people/27e7d989-9ddb-5025-9f0c-d666f29c55cc/");
  const main = page.locator("main");
  await expect(main).toContainText("conflicting sources");
  await expect(main).toContainText("private as the entry grade");
  await expect(main).toContainText("index prints Col");
  await expect(main).toContainText("Box 535");
});

test("Batch 674 preserves the Robert D Moore suffix qualification and index note", async ({ page }) => {
  await page.goto("./people/b150101e-1f27-58ac-894a-3e5b0cbb7e23/");
  const main = page.locator("main");
  await expect(main).toContainText("Jr. suffix absent from the index");
  await expect(main).toContainText("possible");
  await expect(main).toContainText("high confidence");
});

test("Batch 674 preserves Margeret exactly as indexed", async ({ page }) => {
  await page.goto("./people/627d49d0-ac16-52d6-a8d2-cf47d19608db/");
  await expect(page.getByRole("heading", { name: "Margeret A Moore", level: 1 })).toBeVisible();
  await expect(page.locator("main")).not.toContainText("Margaret A Moore");
});

test("Batch 674 gives all fourteen unresolved people terminal research pages", async ({ page }) => {
  for (const [id, name] of unresolved) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText("Archival-review priorityhigh");
    await expect(main).not.toContainText("Verified employer");
  }
});

test("Batch 674 updates exact coverage and preserves the oil-company category", async ({ page }) => {
  await page.goto("./");
  await expect(page.locator("body")).toContainText("8,556");
  await expect(page.locator("body")).toContainText("35.74%");
  await expect(page.getByRole("heading", { name: "People who worked for oil companies" })).toBeVisible();

  await page.goto("./oil-companies/");
  const oilList = page.getByRole("region", { name: "Oil company work list" });
  await expect(oilList.locator(".oil-directory__person")).toHaveCount(8);
  for (const [, name] of profiles) {
    await expect(oilList).not.toContainText(name);
  }
});
