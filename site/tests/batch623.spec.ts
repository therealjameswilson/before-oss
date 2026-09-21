import { expect, test } from "@playwright/test";

test("official Army crosswalks improve identity without inventing employers", async ({ page }) => {
  const cases = [
    ["9a838d2e-e71b-533a-82f3-07a519001f44", "Anthony B May"],
    ["51028b1e-5c4c-5549-9726-2ea57824bfe5", "Sam Mavromihales"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("high confidence");
    await expect(page.locator("main")).toContainText(/official Army bulk entry/i);
    await expect(page.locator("main")).toContainText(
      "No publishable pre-OSS affiliation is recorded yet",
    );
  }
});

test("Charles Maxwell stays probable and Erwin Mauss stays conflicting", async ({ page }) => {
  await page.goto("./people/bbdeca8e-84d8-571c-aa35-91064cd2dc10/");
  await expect(page.getByRole("heading", { name: "Charles Maxwell", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("probable");
  await expect(page.locator("main")).toContainText(/MAXWELC CHARLES R/i);
  await expect(page.locator("main")).toContainText("high");

  await page.goto("./people/4b97ed0c-9c0b-5f68-a7a1-c49471df5b6b/");
  await expect(page.getByRole("heading", { name: "Erwin Mauss", level: 1 })).toBeVisible();
  await expect(page.locator("main")).toContainText("conflicting");
  await expect(page.locator("main")).toContainText("Stephen Z Krzyzaniak");
  await expect(page.locator("main")).toContainText("critical");
});

test("Ward and William McCabe remain a visible identifier conflict", async ({ page }) => {
  const cases = [
    ["6b4b6e22-e835-55ae-b7a6-40a112ecb5b7", "Ward McCabe"],
    ["d7c03613-c5e1-5938-ba61-e2e48cd4941b", "William W McCabe"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("conflicting");
    await expect(page.locator("main")).toContainText(/same protected identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("McAragle and McGaragle and McCarary and McCrary remain variants", async ({ page }) => {
  const cases = [
    ["5925506f-0976-5138-9c6a-794f152a31d9", "William C McAragle"],
    ["4d6eb7f9-83b2-567a-aa76-25683a32d761", "William C McGaragle"],
    ["1aa37e74-b066-54a9-b781-89500217fb27", "Jack L McCarary"],
    ["4960f431-455c-5d03-a23d-90159edbc153", "Jack L McCrary"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/protected identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("leading-zero and missing-zero variants remain explicit", async ({ page }) => {
  const cases = [
    ["ff0e53eb-3398-5e5e-86ec-d8d5547ad224", "John A McCargar", /leading zero/i],
    ["f378adb4-7779-533a-934a-0be8f4f721f3", "John A McCaroar", /leading zero/i],
    ["85c12836-4535-5df2-bdc9-3b0cc2d61af2", "Paul W McCausland", /missing zero/i],
    ["b641e203-1d4e-51f8-993a-38270141ec15", "Paul W McClausland", /omits one zero/i],
  ];
  for (const [id, name, evidence] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name: String(name), level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(evidence as RegExp);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("same-name rows with insufficient evidence remain separate", async ({ page }) => {
  const cases = [
    ["98b57dae-121f-52b2-810c-165e26f3751a", "John F McCarthy"],
    ["d5db343c-7209-505d-b40b-f777f67cf63c", "John F McCarthy"],
    ["6530a476-0f7c-58aa-bb49-3fb56edc8118", "Alice M McCool"],
    ["ef714a0d-639b-584c-b23e-b994ad27312e", "Alice M McCool"],
    ["11561770-114f-5e51-9220-efe6e7eff8dc", "Alice M McCool"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("the three Edward McCaughy and McGaughy rows stay unresolved", async ({ page }) => {
  const cases = [
    ["dbbe0d36-756b-5061-87a8-aaab00a15a41", "Edward A McCaughy"],
    ["806e928a-6bb1-5935-a8cc-258cb69cbdf6", "Edward A McGaughy"],
    ["73bc3437-460f-5c09-9903-82b581914e1e", "Edward McGaughy"],
  ];
  for (const [id, name] of cases) {
    await page.goto(`./people/${id}/`);
    await expect(page.getByRole("heading", { name, level: 1 })).toBeVisible();
    await expect(page.locator("main")).toContainText("ambiguous");
    await expect(page.locator("main")).toContainText(/final identifier digit|shortened identifier/i);
    await expect(page.locator("main")).toContainText(/duplicate-[a-f0-9]{12}/i);
  }
});

test("Batch 623 keeps the oil-company evidence set unchanged", async ({ page }) => {
  await page.goto("./oil-companies/");
  await expect(page.locator(".oil-directory__person")).toHaveCount(7);
  await expect(page.locator(".oil-directory__list")).not.toContainText("Charles Maxwell");
});
