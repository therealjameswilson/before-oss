import { expect, test } from "@playwright/test";

const profiles = [
  ["c9b9e56e-8980-5d67-a9f2-be78d9f3f9ba", "Mack J Schaefer"],
  ["ee1719fc-c71e-523b-817b-5e8142f1581d", "Raymond M Schaefer"],
  ["71438330-c8db-53e5-b557-7a8f06895cfa", "Sydney L Schaefer"],
  ["1fca1c0e-ecaf-5320-9ed3-349adf57f562", "Ralph A Schaff"],
  ["05f87d2a-63ca-5d99-8e87-8fa6fa78cbd4", "Kurt P Schaffenberge"],
  ["c36d37d9-c9d0-53ca-adaa-29cb8db8d313", "Joanne L Schaffer"],
  ["55beaabb-a0c9-5220-8d04-0177e2a1ed6e", "Franklin J Schaffner"],
  ["a5f9c531-35b8-571d-8469-a80a66f036e7", "Harold E Schagrin"],
  ["44a604b8-c460-509a-a5f6-2f15a9f8810d", "Harold J Schaller"],
  ["9aa9b60a-3337-5305-a27d-a4f65cbe3252", "Raymond B Schantz"],
  ["b452a2a8-b506-50c0-9dcd-12a356d1aa4a", "Edward M Scharf"],
  ["c5bb7a3f-6f70-529f-96e0-9e92bc80a7f3", "Mathilde M Scharff"],
  ["17b5d06e-5b12-5b82-b96c-783ae7c5b6b8", "Max Schatzberg"],
  ["856d3efb-e217-587a-920c-6ffcdaf7859e", "Edgar Schauber"],
  ["b06acaad-28c8-53f0-851f-2dbf6bfc6333", "Edward L Scheaf"],
  ["11ba7ff9-647d-5f53-871f-bac8e79177be", "Joseph B Schechtmann"],
  ["4c02932d-8086-539d-9cef-217fc01f0b23", "Rachel D Schechtmann"],
  ["05eed329-9a5e-5809-9add-cb8cfebfeac2", "Paul Scheffer"],
  ["4f61e8e0-c9d5-5f80-a61b-edf248cf504f", "Delbert R Schefhle"],
  ["4c5e62b9-798d-5f0b-a5aa-16c8415b75b4", "Francis Schehl"],
  ["7441d56d-1b5a-5ce6-a724-8e42dfaa1ba8", "Hildegarde R Scheibe"],
  ["331dea67-2663-5542-b172-08e44fc89c52", "Erich Scheiber"],
  ["bd0897da-c2e1-5f74-aee4-b04d81fffadc", "Franklin O Scheiber"],
] as const;

test("Batch 843 publishes all 23 reviewed profiles with masked identifiers", async ({ page }) => {
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

test("Franklin Schaffner separates Navy service from student status", async ({ page }) => {
  await page.goto("./people/55beaabb-a0c9-5220-8d04-0177e2a1ed6e/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("United States Navy");
  await expect(main).toContainText("amphibious forces in Europe and North Africa");
  await expect(main).toContainText("Franklin & Marshall College");
  await expect(main).toContainText("student");
  await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
});

test("Joseph Schechtman publishes immediate and last civilian research roles", async ({ page }) => {
  await page.goto("./people/11ba7ff9-647d-5f53-871f-bac8e79177be/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Joseph B Schechtman");
  await expect(main).toContainText("Research Bureau on Population Movements");
  await expect(main).toContainText("director and co-founder");
  await expect(main).toContainText("Institute of Jewish Affairs");
  await expect(main).toContainText("verified employer found");
});

test("Paul Scheffer publishes journalism with temporal qualification", async ({ page }) => {
  await page.goto("./people/05eed329-9a5e-5809-9add-cb8cfebfeac2/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("WN#13481-WN#13482");
  await expect(main).toContainText("freelance journalist");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main).toContainText("Berliner Tageblatt");
  await expect(main).not.toContainText("Puyallup society notice");
});

test("Francis Schehl publishes an explicit immediate employer", async ({ page }) => {
  await page.goto("./people/4c5e62b9-798d-5f0b-a5aa-16c8415b75b4/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statushigh confidence");
  await expect(main).toContainText("Franz Schehl");
  await expect(main).toContainText("Portsmouth Priory School");
  await expect(main).toContainText("head of the Classics Department");
  await expect(main).toContainText("explicit immediate");
  await expect(main).toContainText("verified employer found");
});

test("Kurt Schaffenberger keeps qualified studio and Army claims", async ({ page }) => {
  await page.goto("./people/05f87d2a-63ca-5d99-8e87-8fa6fa78cbd4/");
  const main = page.locator("main");
  await expect(main).toContainText("Kurt P Schaffenberger");
  await expect(main).toContainText("Binder Studio");
  await expect(main).toContainText("Qualified and excluded from default high-confidence employer analytics.");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("no unit or formal transfer date");
});

test("Hildegarde Scheibe remains probable and visibly qualified", async ({ page }) => {
  await page.goto("./people/7441d56d-1b5a-5ce6-a724-8e42dfaa1ba8/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusprobable");
  await expect(main).toContainText("Hildegarde M Scheibe");
  await expect(main).toContainText("middle-initial discrepancy");
  await expect(main).toContainText("The Knox School");
  await expect(main).toContainText("University of Wisconsin-Madison");
  await expect(main).toContainText("Qualified and excluded from default high-confidence employer analytics.");
});

test("accepted Batch 843 Army crosswalks publish identity only", async ({ page }) => {
  for (const id of [
    "9aa9b60a-3337-5305-a27d-a4f65cbe3252",
    "b452a2a8-b506-50c0-9dcd-12a356d1aa4a",
    "17b5d06e-5b12-5b82-b96c-783ae7c5b6b8",
    "856d3efb-e217-587a-920c-6ffcdaf7859e",
    "b06acaad-28c8-53f0-851f-2dbf6bfc6333",
  ]) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statushigh confidence");
    await expect(main).toContainText(/private official Army crosswalk|official Army record/i);
    await expect(main).not.toContainText("Army occupation code");
  }
});

test("unresolved Batch 843 profiles retain archival guidance", async ({ page }) => {
  for (const [id, box] of [
    ["c9b9e56e-8980-5d67-a9f2-be78d9f3f9ba", "681"],
    ["ee1719fc-c71e-523b-817b-5e8142f1581d", "681"],
    ["71438330-c8db-53e5-b557-7a8f06895cfa", "681"],
    ["1fca1c0e-ecaf-5320-9ed3-349adf57f562", "681"],
    ["c36d37d9-c9d0-53ca-adaa-29cb8db8d313", "681"],
    ["a5f9c531-35b8-571d-8469-a80a66f036e7", "681"],
    ["44a604b8-c460-509a-a5f6-2f15a9f8810d", "681"],
    ["c5bb7a3f-6f70-529f-96e0-9e92bc80a7f3", "681"],
    ["4c02932d-8086-539d-9cef-217fc01f0b23", "682"],
    ["4f61e8e0-c9d5-5f80-a61b-edf248cf504f", "682"],
    ["331dea67-2663-5542-b172-08e44fc89c52", "682"],
  ] as const) {
    await page.goto(`./people/${id}/`);
    const main = page.locator("main");
    await expect(main).toContainText("Identity statusunresolved");
    await expect(main).toContainText("No reliable pre-OSS employer has yet been identified");
    await expect(main).toContainText(`Review Box ${box}`);
  }
});

test("Franklin O Scheiber exposes the conflict without publishing the private alternate identity", async ({ page }) => {
  await page.goto("./people/bd0897da-c2e1-5f74-aee4-b04d81fffadc/");
  const main = page.locator("main");
  await expect(main).toContainText("Identity statusconflicting");
  await expect(main).toContainText("materially different full name");
  await expect(main).toContainText("do not publish the alternate name");
  await expect(main).not.toContainText("Alternate identity:");
});
