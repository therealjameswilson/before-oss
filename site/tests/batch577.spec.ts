import { expect, test } from "@playwright/test";

const people = [
  ["27d05517-09b8-5564-ab08-4aee471c4b19", "Francis T Devlin", "183"],
  ["314c26c6-8d31-5a78-bae7-e79e6197a004", "Joseph H Devlin", "183"],
  ["66123868-dc22-5f67-8f32-f5dde4f01d20", "Joseph B Devlin", "183"],
  ["6f934089-11b8-59d6-ab58-4e87476cce9b", "Elleen M Devney", "183"],
  ["db3cc415-2324-5573-a029-5dc743284335", "Carl Devoe", "183"],
  ["7dbf51ee-ed8b-5d6c-9f21-89912882cec4", "Charles E DeVogel", "184"],
  ["d7310e5d-9485-5e47-aefc-4b940a223e44", "Sarah J DeVol", "184"],
  ["f3f730dc-b223-5498-be06-a02b11b5fdfa", "Phillippe DeVomecourt", "184"],
  ["7036165b-288a-5d25-8ed4-06c7eb808352", "Clyde H Devore", "184"],
  ["dba636b3-f30f-58bd-bde9-354500042743", "Raymond Devos", "184"],
] as const;

test("batch 577 keeps each indexed person and unresolved employer visible", async ({ page }) => {
  for (const [id, name, box] of people) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("heading", { name, exact: true, level: 1 })).toBeVisible();
    await expect(page.getByText("requires archival review", { exact: true }).first()).toBeVisible();
    await expect(page.getByText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
      { exact: true },
    ).first()).toBeVisible();
    await expect(page.getByText("No publishable pre-OSS affiliation is recorded yet")).toBeVisible();
    await expect(page.getByText(`Box ${box}`, { exact: false }).first()).toBeVisible();
  }
});

test("Army identity evidence does not become an employer claim", async ({ page }) => {
  for (const id of [
    "314c26c6-8d31-5a78-bae7-e79e6197a004",
    "db3cc415-2324-5573-a029-5dc743284335",
    "7dbf51ee-ed8b-5d6c-9f21-89912882cec4",
  ]) {
    await page.goto(`./people/${id}/`, { waitUntil: "domcontentloaded" });
    await expect(page.getByRole("link", { name: "Electronic Army Serial Number Merged File, ca. 1938-1946" }).first()).toHaveAttribute(
      "href", "https://catalog.archives.gov/id/1263923",
    );
    await expect(page.getByText("No publishable pre-OSS affiliation is recorded yet")).toBeVisible();
  }
});

test("Carl Devoe's naval namesake and Phillippe DeVomecourt's SOE lead stay qualified", async ({ page }) => {
  await page.goto("./people/db3cc415-2324-5573-a029-5dc743284335/", { waitUntil: "domcontentloaded" });
  await expect(page.getByText(/whether he is the index's Carl Devoe is unresolved/i)).toBeVisible();
  await expect(page.getByRole("link", { name: "Eleventh Semi-Monthly Report of Activities of OSS-ME" })).toBeVisible();
  await expect(page.getByText("unknown or indeterminate", { exact: true }).first()).toBeVisible();

  await page.goto("./people/f3f730dc-b223-5498-be06-a02b11b5fdfa/", { waitUntil: "domcontentloaded" });
  await expect(page.getByText(/SOE organizer named Philippe de Vomécourt, but the identity is unverified/i)).toBeVisible();
  await expect(page.getByRole("link", { name: "Philippe DE CREVOISIER DE VOMECOURT" })).toBeVisible();
  await expect(page.getByText("Société de gérance des wagons de grande capacité", { exact: false })).toHaveCount(0);
});
