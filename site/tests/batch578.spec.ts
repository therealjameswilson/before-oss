import { expect, test } from "@playwright/test";

const cohort = [
  ["f39cebf2-167f-5c0a-8e19-0521b15e0e30", "Cornelis Devries"],
  ["d17210d7-c571-5bee-9d3d-0f9b0482b886", "Henry P Devries"],
  ["8f7e8604-9772-5a6b-916d-f5e4b8de8db6", "Mike Devyak"],
  ["aa2f0ede-3070-54b8-9102-24ad6bf92e45", "Nicholas DeVyner"],
  ["197efe67-37d6-57c7-ba5a-ef878be4c198", "Gwendolyn J Dew"],
  ["f98133e8-5681-50d2-bac7-dce0ff4e857c", "Carl L Dewald"],
  ["60fde37e-28cc-53df-a62c-2382ec797a1b", "William T Dewart Jr."],
  ["b0775594-d3a1-5b62-a4cb-4fa5e88563d8", "Andre DeWavrins"],
  ["824fe808-8e38-5574-9dcb-a0108940cb96", "Ralph A DeWeese"],
  ["2488deb6-43a5-598e-b6cd-9fafc8868676", "Robert K Deweese"],
] as const;

test("batch 578 publishes all ten indexed profiles without inventing an employer", async ({ page }) => {
  for (const [id, name] of cohort) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.getByText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
      { exact: true },
    ).first()).toBeVisible();
    await expect(page.getByText("Box 184", { exact: false }).first()).toBeVisible();
  }
});

test("Mike Devyak's Navy transfer is an affiliation, not a civilian employer", async ({ page }) => {
  await page.goto("./people/8f7e8604-9772-5a6b-916d-f5e4b8de8db6/", { waitUntil: "domcontentloaded" });
  await expect(page.getByText("United States Navy", { exact: false }).first()).toBeVisible();
  await expect(page.getByText(/entered the U\.S\. Navy in February 1943/i)).toBeVisible();
  await expect(page.getByRole("link", { name: "Office of Strategic Services board proceedings, Italy, May 1944" }).first()).toBeVisible();
});

test("Dewart Jr.'s dated company role and DeWavrins's unmerged lead stay qualified", async ({ page }) => {
  await page.goto("./people/60fde37e-28cc-53df-a62c-2382ec797a1b/", { waitUntil: "domcontentloaded" });
  await expect(page.getByText("The Frank A. Munsey Company", { exact: false }).first()).toBeVisible();
  await expect(page.getByText(/1940 Frank A\. Munsey Company magazine masthead/i)).toBeVisible();
  await expect(page.getByRole("link", { name: "Detective Fiction Weekly" }).first()).toBeVisible();
  await expect(page.getByText("No publishable immediate affiliation or civilian employer is recorded yet")).toBeVisible();

  await page.goto("./people/b0775594-d3a1-5b62-a4cb-4fa5e88563d8/", { waitUntil: "domcontentloaded" });
  await expect(page.getByText(/resembles Free French intelligence chief André Dewavrin/i)).toBeVisible();
  await expect(page.getByText("No publishable pre-OSS affiliation is recorded yet")).toBeVisible();
});
