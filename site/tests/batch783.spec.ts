import { expect, test } from "@playwright/test";

const profiles = [
  ["9c879a21-9aa9-5fc9-8b53-3811c51effbb", "John P Quertermous"],
  ["a2aff92b-d815-5d6c-9ef3-77895f42a164", "James L Quesada"],
  ["cbe1e8d3-aaec-5517-99fd-ae9f34e464e5", "Georgia A Quesenberry"],
  ["b69b0461-5f0a-56e1-9182-078ba709111c", "Glenford Quick"],
  ["ec2b1374-2e41-5c29-bcf1-02c96232c1f2", "Jean M Quick"],
  ["73f5695d-2fce-5188-8e08-f262c9054af1", "Luther P Quick"],
  ["2b063090-b075-5683-9619-c4894d247cea", "LaVonne S Quidley"],
  ["2d64f0dc-8f3f-51a0-85c6-13aa5d197bd6", "Harold S Quigley"],
  ["e442e936-13df-5d26-8ca7-10fd50cf5405", "Lucille A Quigley"],
  ["04640773-dd74-53fd-bf27-dfe822e8cfed", "Martin S Quigley"],
  ["83c8e8da-c7ce-52c9-bad4-e069c8ba7adb", "Timothy B Quill"],
  ["047998a6-cc32-5ab2-b1e4-07f0ffe379d5", "Kenneth H Quin"],
  ["1220e36d-0b4b-5680-b388-d323cbf1d62b", "Mary J Quinlan"],
  ["35046cc0-72ea-5fde-ae26-cebaecee6433", "Agnes P Quinn"],
  ["dcdd2113-ccdf-54d1-ba48-5eb9153489e8", "Jean B Quinn"],
  ["040e5084-7593-5dc9-81f7-60575cce50db", "Jean Q Quinn"],
  ["cb64369f-fe0d-5277-88a3-ea099c12d5b1", "John F Quinn"],
  ["e0efa13f-2ff7-5e97-9970-a49be1cedac5", "Mary I Quinn"],
  ["85049a21-6b08-5748-bccb-4770ffc04e73", "Myrtle V Quinn"],
  ["00d8ea9d-23ae-55ad-ad4b-ed7b0eec60f2", "Patrick E Quinn"],
  ["be9ee1b4-684e-5757-a7d1-59d7864af7c0", "Robert S Quinn"],
  ["69383a59-bb00-59b5-b825-d74874913f68", "William Quinn"],
  ["087f1155-67ec-50fe-b44c-eff9858c5eb7", "Waldo S Quinney"],
] as const;

test("Batch 783 publishes all 23 profiles with terminal attempted outcomes", async ({ page }) => {
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
    for (const value of serialValues) expect(value).not.toMatch(/^[A-Z]?\s?\d{4,9}$/);
  }
});

test("Batch 783 publishes accepted Army identity evidence without inventing employers", async ({ page }) => {
  for (const id of [
    "9c879a21-9aa9-5fc9-8b53-3811c51effbb",
    "b69b0461-5f0a-56e1-9182-078ba709111c",
    "83c8e8da-c7ce-52c9-bad4-e069c8ba7adb",
  ]) {
    await page.goto("./people/" + id + "/");
    const main = page.locator("main");
    await expect(main).toContainText("nonshared protected identifier");
    await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
      "No reliable pre-OSS employer",
    );
  }
});

test("Batch 783 preserves Luther Quick's conflicting Army candidate", async ({ page }) => {
  await page.goto("./people/73f5695d-2fce-5188-8e08-f262c9054af1/");
  const main = page.locator("main");
  await expect(main).toContainText("QUICK H R P");
  await expect(main).toContainText("conflicting");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 783 publishes Quigley's sourced pre-OSS chronology", async ({ page }) => {
  await page.goto("./people/04640773-dd74-53fd-bf27-dfe822e8cfed/");
  const main = page.locator("main");
  await expect(main.locator("section[aria-labelledby='immediate-affiliation']")).toContainText(
    "Office of the Coordinator of Information",
  );
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "Quigley Publishing Company",
  );
  await expect(main).toContainText("Motion Picture Herald");
  await expect(main).toContainText("A U.S. Spy in Ireland");
});

test("Batch 783 qualifies Quidley's and Robert Quinn's unresolved chronology", async ({ page }) => {
  await page.goto("./people/2b063090-b075-5683-9619-c4894d247cea/");
  let main = page.locator("main");
  await expect(main).toContainText("United States federal government");
  await expect(main).toContainText("probable");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );

  await page.goto("./people/be9ee1b4-684e-5757-a7d1-59d7864af7c0/");
  main = page.locator("main");
  await expect(main).toContainText("50th Fighter Group");
  await expect(main).toContainText("temporal relation uncertain");
  await expect(main.locator("section[aria-labelledby='civilian-employer']")).toContainText(
    "No reliable pre-OSS employer",
  );
});

test("Batch 783 preserves literal clipped index notes", async ({ page }) => {
  await page.goto("./people/83c8e8da-c7ce-52c9-bad4-e069c8ba7adb/");
  await expect(page.locator("main")).toContainText("Extract fr");

  await page.goto("./people/040e5084-7593-5dc9-81f7-60575cce50db/");
  await expect(page.locator("main")).toContainText("One of t");
});

test("home page exposes the rebuilt Batch 783 coverage totals", async ({ page }) => {
  await page.goto("./");
  const home = page.locator("main");
  await expect(home).toContainText("11,009");
  await expect(home).toContainText("45.99%");
  await expect(home).toContainText("12,925");
  await expect(home).toContainText("801");
  await expect(home).toContainText("358");
  await expect(home).toContainText("9,468");
});
