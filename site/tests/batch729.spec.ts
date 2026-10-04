import { expect, test } from "@playwright/test";

const profiles = [
  ["b66b1c4b-6e39-5f22-a375-085a6b629a48", "William R Page"],
  ["9cc2ace0-66bb-5c20-92b4-57b4b37de212", "Francis K Paget"],
  ["b09f6727-cdc3-5722-8962-9fb662e1741d", "Roy G Pagnello"],
  ["3eeb421a-149f-580e-8766-b9b48b5738c4", "Louis E Pahigeanis"],
  ["01238a31-0d42-5721-9907-2b8c09243b4d", "Albert R Pahl"],
  ["a8fd0ad6-1da7-544d-b36f-1bcc6294dbb8", "Gregory M Pahules"],
  ["339283f6-5bdd-5036-bce5-cdd30e443a8b", "Joseph A Paiano"],
  ["4c01de6e-9adc-5d89-9361-122d24e102a8", "Peter G Paidas"],
  ["4efa88b4-7d26-53d6-8522-bbffd825e0b5", "Jason Paige Jr."],
  ["e0605e92-1501-5cee-9af6-74f8705a0420", "Mary S Painter"],
  ["0b9117b1-d434-5d5d-b332-bde6cd7d3097", "Mary J Painter"],
  ["4f5cb150-8525-52eb-809d-57ad79af2fd2", "Robert L Painter"],
  ["9b2ff600-331b-5b18-9359-8bc5738cc66b", "Jozef Pajak"],
  ["02a763c1-2301-5406-9434-cedd0612cee3", "Thomas P Palades"],
  ["ecce875d-5381-5e2e-aba9-966fd1aba2e6", "Gus Palans"],
  ["db249014-5fef-5cbf-a0a1-44aca33c0ce4", "Nicholas P Paledes"],
  ["cac04f30-dc05-531d-b530-66e937233f19", "Stephen P Paledes"],
  ["cd96a75a-f380-5cce-b13e-7175877a0fcb", "Henry Palenik Jr."],
  ["c90b0b99-e614-5337-ba34-1ad65c6bbfd3", "Daisy H Paletti"],
  ["a73f8d30-9489-53d2-b84f-83471eefcad7", "William G Paletti"],
  ["191df9a7-c1e0-5e6e-af4a-55cfadb56046", "Joseph G Palguta"],
  ["ac5f627b-9fbb-523e-94e2-6ea694c94b76", "Ann M Palko"],
  ["b7cf27ea-90a4-516b-bd88-110df45976fd", "George Pallay"],
] as const;

test("Batch 729 publishes all 23 direct profile routes with reviewed outcomes", async ({ page }) => {
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

test("Batch 729 separates Paledes civilian work from his immediate Army pathway", async ({ page }) => {
  await page.goto("./people/db249014-5fef-5cbf-a0a1-44aca33c0ce4/");
  const main = page.locator("main");
  await expect(main).toContainText("Grocery-store operator");
  await expect(main).toContainText("Last civilian employer");
  await expect(main).toContainText("Self-employed");
  await expect(main).toContainText("Immediate pre-OSS affiliation");
  await expect(main).toContainText("United States Army");
  await expect(main).toContainText("September 1941");
  await expect(main).toContainText("October 1943");
  await expect(main).toContainText("verified employer found");
  await expect(main).toContainText("Nicholas P Peledes");
});

test("Batch 729 presents Painter's Albright role as student status, never employment", async ({ page }) => {
  await page.goto("./people/0b9117b1-d434-5d5d-b332-bde6cd7d3097/");
  const main = page.locator("main");
  await expect(main).toContainText("Mary Jane Painter");
  await expect(main).toContainText("Albright College");
  await expect(main).toContainText("Student");
  await expect(main).toContainText("quit Albright College");
  await expect(main).not.toContainText("Immediate pre-OSS affiliationAlbright College");
  await expect(main).not.toContainText("Last civilian employerAlbright College");
});

test("Batch 729 publishes corroborated Greek operational-group identities only as identity evidence", async ({ page }) => {
  await page.goto("./people/a8fd0ad6-1da7-544d-b36f-1bcc6294dbb8/");
  await expect(page.locator("main")).toContainText("T/5 Gregory M. Pahules");
  await expect(page.locator("main")).not.toContainText("Immediate pre-OSS affiliationGreek Group I");

  await page.goto("./people/4c01de6e-9adc-5d89-9361-122d24e102a8/");
  await expect(page.locator("main")).toContainText("Pete G. Paidas");
  await expect(page.locator("main")).not.toContainText("Last civilian employerGreek Group V");

  await page.goto("./people/ecce875d-5381-5e2e-aba9-966fd1aba2e6/");
  await expect(page.locator("main")).toContainText("Gus L. Palans");
  await expect(page.locator("main")).toContainText("National Park Service");
});

test("Batch 729 preserves the Paletti-Plaetti conflict and exact rebuilt coverage", async ({ page }) => {
  await page.goto("./people/a73f8d30-9489-53d2-b84f-83471eefcad7/");
  const profile = page.locator("main");
  await expect(profile).toContainText("William G Plaetti");
  await expect(profile).toContainText("conflicting sources");
  await expect(profile).toContainText("Last civilian employer before service");
  await expect(profile).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(profile).not.toContainText("Last civilian employer before serviceSelf-employed");

  await page.goto("./");
  const main = page.locator("main");
  await expect(main).toContainText("9,803");
  await expect(main).toContainText("40.95%");
  await expect(main).toContainText("14,131");
  await expect(main).toContainText("741");
  await expect(main).toContainText("332");
  await expect(page.locator("#oil-companies .oil-directory__person")).toHaveCount(9);
  await expect(page.locator("#oil-companies")).not.toContainText("Francis K Paget");
});
