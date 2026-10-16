import { expect, test } from "@playwright/test";

const profiles = [
  ["4648fb15-e75d-5544-947c-e5189c37c7a7", "Edward F Scannell"],
  ["69377883-6216-5861-8d19-b4ab9c3e20db", "Raymond B Scantz"],
  ["f3ef947f-d681-5133-807d-58cd2dde357e", "Albert T Scaramucci"],
  ["7242b721-dd10-5170-899e-4b6dcf6e3d67", "Pantelli Scaravelaci"],
  ["923410dd-9080-55fd-a38c-93cc849769bd", "Michael A Scardamaglia"],
  ["050e6576-a019-5208-a859-b11a5ed0de99", "Anthony Scariano"],
  ["f6b31e0c-10e7-5e7b-873b-430a91241de4", "James J Scaringi"],
  ["560317dd-7388-570a-b8d8-2935473c0adc", "Anthony J Scarlati"],
  ["6f7bde48-8581-570e-b0dc-591237256bd9", "Pateli Scarveliaci"],
  ["13b868e3-4769-5811-a775-d19c0b932f78", "Emery M Scates"],
  ["0a9e9f12-335d-54ed-8965-272e5999ebfa", "John J Scattoreggio"],
  ["709914cd-199d-508f-9ed2-b66a7c27d3ab", "Chester A Scerra"],
  ["45ba7052-0853-56b6-8d56-c738f8c13d42", "John R Schaaf"],
  ["183aa0e1-b65c-5054-bc63-20321d551523", "Sterling Schaar"],
  ["c8443a24-e4c3-57f6-a9e8-15110ff3f22b", "Oscar Schachter"],
  ["51ccbee6-880c-5ae7-bc4c-b17993ce81c4", "Yvette Schachter"],
  ["a5dd617d-581a-5316-aceb-24d3e454a506", "Dorothy F Schackleton"],
  ["29f0089c-d5c0-5a97-b449-c96c2cf2efaa", "Charles W Schad"],
  ["8d80b399-ca8a-574c-a61b-d0cb5522aa45", "Martin Schadi"],
  ["ab3ef519-de4f-5f89-a8db-9121bfe38b70", "Carl Schaefer"],
  ["7eb3cd6c-95e7-58a2-ae81-9c37b0954f74", "George H Schaefer"],
  ["060038cb-1fe8-5f59-a91c-bf63595f51d2", "John W Schaefer"],
  ["59c707e4-6f88-5e88-9b03-dff8d4150eff", "Leland L Schaefer"],
] as const;

test("Batch 842 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
  for (const [id, name] of profiles) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    const main = page.locator("main");
    await expect(main).toContainText("Archive box");
    await expect(main).not.toContainText("not started");
    const serials = await main.locator("dt").filter({ hasText: /^Serial$/ })
      .locator("xpath=following-sibling::dd[1]").allTextContents();
    for (const value of serials) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}(?:RA)?$/);
  }
});

test("Anthony Scariano publishes qualified student status without inventing an employer", async ({ page }) => {
  await page.goto("./people/050e6576-a019-5208-a859-b11a5ed0de99/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("George Washington University");
  await expect(main).toContainText("student");
  await expect(main).toContainText("documented pre-OSS");
  await expect(main).toContainText("graduated in 1942");
  await expect(main).toContainText("Student status is not employment and is excluded from employer analytics");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Chester Scerra and Martin Schadi publish high-confidence identity only", async ({ page }) => {
  for (const [id, sourceText] of [
    ["709914cd-199d-508f-9ed2-b66a7c27d3ab", "Obituary for Chester A. Scerra"],
    ["8d80b399-ca8a-574c-a61b-d0cb5522aa45", "Martin 'Scotty' Schadi obituary"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(sourceText);
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
  }
});

test("accepted Batch 842 Army crosswalks publish identity but no coded occupation", async ({ page }) => {
  for (const id of [
    "4648fb15-e75d-5544-947c-e5189c37c7a7",
    "7242b721-dd10-5170-899e-4b6dcf6e3d67",
    "923410dd-9080-55fd-a38c-93cc849769bd",
    "f6b31e0c-10e7-5e7b-873b-430a91241de4",
    "0a9e9f12-335d-54ed-8965-272e5999ebfa",
    "45ba7052-0853-56b6-8d56-c738f8c13d42",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(/private official Army crosswalk/i);
    await expect(main).not.toContainText("Army occupation code");
  }
});

test("Scantz and Schantz remain separate in one visible duplicate group", async ({ page }) => {
  for (const [id, name] of [
    ["69377883-6216-5861-8d19-b4ab9c3e20db", "Raymond B Scantz"],
    ["9aa9b60a-3337-5305-a27d-a4f65cbe3252", "Raymond B Schantz"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(main).toContainText("Identity statusambiguous");
    await expect(main).toContainText("Duplicate groupduplicate-b2ef441ee385");
  }
});

test("Scaravelaci and Scarveliaci remain separate and reviewable", async ({ page }) => {
  await page.goto("./people/7242b721-dd10-5170-899e-4b6dcf6e3d67/");
  let main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Duplicate groupduplicate-4243ef133d4c");

  await page.goto("./people/6f7bde48-8581-570e-b0dc-591237256bd9/");
  main = page.locator("main");
  await expect(main).toContainText("Identity statusambiguous");
  await expect(main).toContainText("Duplicate groupduplicate-4243ef133d4c");
});

test("unresolved Batch 842 profiles retain archival guidance", async ({ page }) => {
  for (const [id, box] of [
    ["f3ef947f-d681-5133-807d-58cd2dde357e", "680"],
    ["560317dd-7388-570a-b8d8-2935473c0adc", "680"],
    ["13b868e3-4769-5811-a775-d19c0b932f78", "680"],
    ["183aa0e1-b65c-5054-bc63-20321d551523", "681"],
    ["c8443a24-e4c3-57f6-a9e8-15110ff3f22b", "681"],
    ["51ccbee6-880c-5ae7-bc4c-b17993ce81c4", "681"],
    ["a5dd617d-581a-5316-aceb-24d3e454a506", "681"],
    ["29f0089c-d5c0-5a97-b449-c96c2cf2efaa", "681"],
    ["ab3ef519-de4f-5f89-a8db-9121bfe38b70", "681"],
    ["7eb3cd6c-95e7-58a2-ae81-9c37b0954f74", "681"],
    ["060038cb-1fe8-5f59-a91c-bf63595f51d2", "681"],
    ["59c707e4-6f88-5e88-9b03-dff8d4150eff", "681"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusunresolved");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText(`Review Box ${box}`);
  }
});
