import { expect, test } from "@playwright/test";

const reviewedPeople = [
  ["deb0fc16-7d75-59f6-82ff-3c63bc7386d6", "James E Devenney"],
  ["cb694a4a-6fe3-5f82-bad0-0e89a0c6060c", "Raymond M Devenuto"],
  ["b85a2c66-0b49-50d4-809b-53160e6feea3", "Jose M Deveraux"],
  ["5ce9acda-3faf-5cdf-b3b9-9c81a5be8ed4", "Joseph M Deveraux Jr."],
  ["c1735abf-29cf-580b-b685-0c5da3563aeb", "Eugene N Devers"],
  ["28434202-8ad3-5f0b-871d-697df276c1f6", "Ronnie A DeVico"],
  ["aea110b2-d582-5651-a42b-9b90a1c8cbcb", "Robert C Devilbiss"],
  ["1f8cf5c5-fb18-5333-92d3-a03b4890ca19", "Geraldine N Devine"],
  ["f5b5322c-6dee-56d1-9a81-9016b7bae8f1", "Gordon D Devins"],
  ["57a5f2aa-d0a9-51db-8fd5-a04bd4006eb3", "Peter P Devivi"],
] as const;

test("batch 576 profiles preserve unresolved employers and Box 183 guidance", async ({ page }) => {
  for (const [personId, name] of reviewedPeople) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.getByText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
      { exact: true },
    ).first()).toBeVisible();
    await expect(page.getByText("No publishable pre-OSS affiliation is recorded yet")).toBeVisible();
  }
});

test("Army identity links are cited without creating employers", async ({ page }) => {
  for (const personId of [
    "28434202-8ad3-5f0b-871d-697df276c1f6",
    "f5b5322c-6dee-56d1-9a81-9016b7bae8f1",
  ]) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
    await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" }).first()).toHaveAttribute(
      "href",
      "https://catalog.archives.gov/id/1263923",
    );
    await expect(page.getByText("No reviewed claim currently meets the publication threshold.").first()).toBeVisible();
  }
});

test("a different Army name does not become Peter Devivi's identity or occupation", async ({ page }) => {
  await page.goto("./people/57a5f2aa-d0a9-51db-8fd5-a04bd4006eb3/");
  await expect(page.getByText("conflicting", { exact: true }).first()).toBeVisible();
  await expect(page.getByText(/Army bulk entry sharing the private identifier names George W Delamarter/i).first()).toBeVisible();
  await expect(page.getByText("No reviewed claim currently meets the publication threshold.").first()).toBeVisible();
});
