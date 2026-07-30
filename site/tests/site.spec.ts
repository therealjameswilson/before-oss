import { expect, test } from "@playwright/test";
import fs from "node:fs";

type Person = { person_id: string; display_name: string };
const people = JSON.parse(
  fs.readFileSync(new URL("../src/data/generated/people.json", import.meta.url), "utf8"),
) as Person[];
const firstPerson = people[0];

test("home reports the complete index and incomplete research honestly", async ({ page }) => {
  await page.goto("./");
  await expect(page.getByRole("heading", { name: /Who were they before OSS/i })).toBeVisible();
  await expect(page.getByText("23,978", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("Verified employer found", { exact: true })).toBeVisible();
  await expect(
    page.getByText(/112 entities currently have confirmed\/high published employment or self-employment evidence/i),
  ).toBeVisible();
  await expect(page.getByText(/broader affiliation measure currently covers 189 entities/i)).toBeVisible();
  await expect(page.getByText(/The directory is complete; the historical research is not/i)).toBeVisible();
});

test("directory search, commissioned filter, and URL state work", async ({ page }) => {
  await page.goto("./people/");
  await expect(page.getByText(/23,941 results/)).toBeVisible({ timeout: 30_000 });
  await page
    .getByRole("searchbox", { name: "Search", exact: true })
    .fill(firstPerson.display_name);
  await expect(page.getByRole("link", { name: firstPerson.display_name }).first()).toBeVisible();
  await expect(page).toHaveURL(/q=/);
  await page.getByLabel("Commissioned status").selectOption("true");
  await expect(page).toHaveURL(/commissioned=true/);
  await expect(page.locator("#result-summary")).not.toHaveText(/23,941 results/);
});

test("direct person route preserves source evidence and masks serials", async ({ page }) => {
  await page.goto(`./people/${firstPerson.person_id}/`);
  await expect(page.getByRole("heading", { name: firstPerson.display_name, exact: true })).toBeVisible();
  await expect(page.getByRole("heading", { name: "How the person appears in the index" })).toBeVisible();
  const content = await page.locator("body").innerText();
  expect(content).not.toMatch(/\b\d{7,8}\b/);
});

test("organizations, analysis, methodology, sources, and downloads are direct routes", async ({ page }) => {
  for (const route of ["organizations/", "analysis/", "methodology/", "sources/", "downloads/"]) {
    const response = await page.goto(`./${route}`);
    expect(response?.ok(), route).toBeTruthy();
    await expect(page.locator("h1")).toBeVisible();
  }
  const download = await page.request.get("./downloads/personnel_public.csv");
  expect(download.ok()).toBeTruthy();
  expect((await download.text()).split("\n")[0]).toContain("serial_masked");
});

test("a researched profile displays claim-level citations", async ({ page }) => {
  await page.goto(
    "./people/21a6b6f2-5daa-5569-826e-6d193f387d4a/",
  );
  await expect(page.getByRole("heading", { name: "Evidence and citations" })).toBeVisible();
  await expect(page.getByRole("heading", { name: "Sources for this claim" }).first()).toBeVisible();
  await expect(page.getByRole("link", { name: "Mort Bobrow Obituary (1923–2019)" }).first()).toHaveAttribute(
    "href",
    /legacy\.com/,
  );
  await expect(page.getByText("Accessed 2026-07-29.", { exact: false }).first()).toBeVisible();
});

test("the confirmed McWilliams profile separates immediate and civilian affiliations", async ({
  page,
}) => {
  await page.goto(
    "./people/a417086c-3c99-5b5a-a198-35e1dc27f553/",
  );
  await expect(
    page.getByRole("heading", { name: "Julia C McWilliams", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("Julia Child", { exact: false }).first()).toBeVisible();
  await expect(
    page.getByRole("heading", { name: "Office of War Information", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("heading", { name: "W. & J. Sloane", exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "NAID 2180661", exact: true }),
  ).toHaveAttribute("href", "https://catalog.archives.gov/id/2180661");
});

test("the reviewed NARA batch preserves each person's distinct pre-OSS pathway", async ({
  page,
}) => {
  const profiles = [
    {
      id: "0cde0770-6d7d-5642-a1d3-d3e0b94c6dfc",
      name: "Ralph J Bunche",
      immediate: "Howard University",
      catalogId: "2168596",
    },
    {
      id: "6e014675-a236-513e-94cc-fadb5d986aa9",
      name: "William J Casey",
      immediate: "Board of Economic Warfare",
      catalogId: "2169187",
    },
    {
      id: "604d1099-bc8e-526c-a002-eeaa723c44e3",
      name: "Arthur J Goldberg",
      immediate: "Self-employed",
      catalogId: "2174048",
    },
    {
      id: "f02c5c3b-b8ff-5cb8-990d-3735dbbe0e19",
      name: "Sterling W Hayden",
      immediate: "United States Marine Corps Reserve",
      catalogId: "2175283",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.immediate, exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByRole("link", { name: `NAID ${profile.catalogId}`, exact: true }),
    ).toHaveAttribute("href", `https://catalog.archives.gov/id/${profile.catalogId}`);
  }
});

test("the reviewed CIA batch distinguishes military, government, and civilian pathways", async ({
  page,
}) => {
  const profiles = [
    {
      id: "491ada54-8954-5518-b03e-88e0ed92d573",
      name: "Morris Berg",
      immediate: "Office of Inter-American Affairs",
      lastCivilian: "Boston Red Sox",
      source: "Moe Berg: Baseball Player, Linguist, Lawyer, Intel Officer",
    },
    {
      id: "d66cd8d4-b1c4-5dff-9432-a69a90e7caa4",
      name: "Virginia Hall",
      immediate: "Special Operations Executive",
      source: "The Office of Strategic Services: America's First Intelligence Agency",
    },
    {
      id: "0a1cbed6-2239-51a5-8ada-245100eb6fa0",
      name: "Richard M Helms",
      immediate: "United States Naval Reserve",
      lastCivilian: "The Indianapolis Times",
      source: "Richard Helms: The Intelligence Professional Personified",
    },
    {
      id: "7a26fb60-b1e2-5377-9092-f16406580dfd",
      name: "William E Colby",
      immediate: "United States Army",
      source: "Office of Strategic Services Compass",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.immediate, exact: true }).first(),
    ).toBeVisible();
    const civilianSection = page.locator(
      'section[aria-labelledby="civilian-employer"]',
    );
    if (profile.lastCivilian) {
      await expect(
        civilianSection.getByRole("heading", {
          name: profile.lastCivilian,
          exact: true,
        }),
      ).toBeVisible();
    } else {
      await expect(
        civilianSection.getByText(
          "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
          { exact: true },
        ),
      ).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toHaveAttribute("href", /cia\.gov/);
  }
});

test("the second reviewed CIA batch keeps student, military, employer, and identity-review evidence distinct", async ({
  page,
}) => {
  const profiles = [
    {
      id: "7d6735a8-041f-5f74-9a6b-d59f868201d8",
      name: "John Ford",
      immediate: "United States Naval Reserve",
      source: "Hollywood and the Office of Strategic Services",
      missingCivilian:
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    },
    {
      id: "3566565e-bc22-57c6-945e-88a7c8983bfc",
      name: "Christian J Lambertsen",
      immediate: "University of Pennsylvania School of Medicine",
      lastCivilian: "Ohio Chemical and Manufacturing Company",
      source: "Christian Lambertsen and the Secret Story Behind Scuba",
    },
    {
      id: "411028ea-e6ef-5d8e-b5c2-574d65e8da21",
      name: "Alfonso Rodriguez",
      immediate: "United States Army G-2",
      source:
        'The "Glorious Amateurs" of OSS: A Diverse Group of Characters Who Helped Win a World War',
      missingCivilian:
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    },
    {
      id: "8061a334-7c98-5f3e-9e20-d8771f19bd50",
      name: "Sidney L Bartlett",
      immediate: "United States Army",
      source: "Hollywood and the Office of Strategic Services",
      missingCivilian: "No reviewed claim currently meets the publication threshold.",
      needsIdentityReview: true,
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.immediate, exact: true }).first(),
    ).toBeVisible();
    const civilianSection = page.locator(
      'section[aria-labelledby="civilian-employer"]',
    );
    if (profile.lastCivilian) {
      await expect(
        civilianSection.getByRole("heading", {
          name: profile.lastCivilian,
          exact: true,
        }),
      ).toBeVisible();
    } else {
      await expect(
        civilianSection.getByText(profile.missingCivilian!, { exact: true }),
      ).toBeVisible();
    }
    if (profile.needsIdentityReview) {
      await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toHaveAttribute("href", /cia\.gov/);
  }
});

test("the alias batch preserves indexed names, documented variants, and unnamed occupations", async ({
  page,
}) => {
  const profiles = [
    {
      id: "852fe132-4da7-54f3-8b43-9e496bb8bc4c",
      name: "Rene Veuve",
      variant: "Rene Joyeuse",
      affiliation: "French Resistance",
    },
    {
      id: "aa60664e-da42-5dd7-a4d0-d8bbfb43368e",
      name: "Jun Atshushi Iwamatsu",
      variant: "Taro Yashima",
      affiliation: "United States Office of War Information",
      authorityId: "n82056657",
    },
    {
      id: "1456d4d2-f29f-56ed-a26c-a9318ed40fab",
      name: "Tomoe Iwamatsu",
      variant: "Mitsu Yashima",
      affiliation: "Art student",
      authorityId: "n82056669",
    },
    {
      id: "c10592a8-6d9e-5673-bf46-5296b828d186",
      name: "Joseph Savoldi Jr.",
      variant: "Joseph Anthony Savoldi",
      affiliation: "Professional wrestler",
      needsIdentityReview: true,
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(page.getByText(profile.variant, { exact: false }).first()).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.affiliation, exact: true }).first(),
    ).toBeVisible();
    if (profile.authorityId) {
      await expect(
        page.getByRole("link", { name: new RegExp(`Yashima, .+19`) }).first(),
      ).toHaveAttribute(
        "href",
        `https://id.loc.gov/authorities/names/${profile.authorityId}`,
      );
    }
    if (profile.needsIdentityReview) {
      await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
      await expect(
        page.getByText("No reviewed claim currently meets the publication threshold.", {
          exact: true,
        }),
      ).toBeVisible();
    }
  }
});

test("the wartime-pathways batch separates military, government, civilian, and student affiliations", async ({
  page,
}) => {
  const profiles = [
    {
      id: "75964751-419e-529e-9fbf-4c755aa42091",
      name: "Peter J Ortiz",
      immediate: "United States Marine Corps",
      earlier: "French Foreign Legion",
      source:
        'The "Glorious Amateurs" of OSS: A Diverse Group of Characters Who Helped Win a World War',
      category: "commissioned marine corps officer",
      missingCivilian:
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    },
    {
      id: "00580293-bf23-52eb-9a5b-352989863c88",
      name: "Fisher Howe",
      immediate: "Coordinator of Information",
      lastCivilian: "Webb School",
      earlier: "Coats and Clark Thread Company",
      source: "The Spymaster's Assistant",
    },
    {
      id: "73b65df0-9cd0-5750-b796-ed8693999501",
      name: "Betty A Lussier",
      immediate: "Air Transport Auxiliary",
      lastCivilian: "Aircraft plant nightshift worker",
      earlier: "University of Maryland",
      source: "The Intrepid Woman: Betty Ann Lussier",
    },
    {
      id: "0d9432b3-fbd7-5934-9e46-7dea8aab6cc3",
      name: "Cordelia Dodson",
      immediate: "U.S. Military Intelligence",
      earlier: "Reed College",
      source: 'The "Glorious Amateurs" of OSS: A Sisterhood of Spies',
      missingCivilian:
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.immediate, exact: true }).first(),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.earlier, exact: true }).first(),
    ).toBeVisible();

    const civilianSection = page.locator(
      'section[aria-labelledby="civilian-employer"]',
    );
    if (profile.lastCivilian) {
      await expect(
        civilianSection.getByRole("heading", {
          name: profile.lastCivilian,
          exact: true,
        }),
      ).toBeVisible();
    } else {
      await expect(
        civilianSection.getByText(profile.missingCivilian!, { exact: true }),
      ).toBeVisible();
    }

    if (profile.category) {
      await expect(
        page.getByText(profile.category, { exact: true }).first(),
      ).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toHaveAttribute("href", /cia\.gov/);
  }
});

test("the education-and-service batch does not turn schools or a spouse's work into employers", async ({
  page,
}) => {
  const profiles = [
    {
      id: "2f189352-aabb-5d3e-899c-ffaafef19aad",
      name: "James Angleton",
      immediate: "United States Army",
      earlier: "Harvard Law School",
      source: "James Angleton: Master Spy Hunter",
      terminalMissingCivilian: true,
    },
    {
      id: "2201ee7c-3d64-5672-b519-0aad4625d185",
      name: "Edna W Andrade",
      immediate: "The Hecht Company",
      lastCivilian: "The Hecht Company",
      earlier: "Pennsylvania Academy of the Fine Arts",
      secondEarlier: "H. Sophie Newcomb Memorial College",
      source: "Edna Andrade: From the OSS to Op Art",
      secondSource: "Oral history interview with Edna Andrade, 1987 April 1-29",
    },
    {
      id: "f87b5adb-6496-5f61-a50f-2b098032d189",
      name: "Jane Burrell",
      earlier: "Smith College",
      secondEarlier: "Columbia University",
      source:
        "The Mystery of Jane Wallis Burrell: The First CIA Officer To Die in the Agency's Service",
      terminalMissingCivilian: true,
    },
    {
      id: "697f0736-ba27-55b6-ae7a-6550dd87aa3c",
      name: "Edmund M Burke",
      earlier: "University of Pennsylvania",
      source: "Hollywood and the Office of Strategic Services",
      terminalMissingCivilian: true,
    },
    {
      id: "990ec032-d116-5a93-bace-517a5dbc9c6d",
      name: "Robert C Broughton",
      immediate: "United States Army",
      lastCivilian: "Walt Disney Studios",
      earlier: "University of California, Los Angeles",
      source: "From Walt Disney to War Movies: Bob Broughton",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page.getByRole("heading", { name: profile.earlier, exact: true }).first(),
    ).toBeVisible();
    if (profile.secondEarlier) {
      await expect(
        page
          .getByRole("heading", { name: profile.secondEarlier, exact: true })
          .first(),
      ).toBeVisible();
    }

    const immediateSection = page.locator(
      'section[aria-labelledby="immediate-affiliation"]',
    );
    if (profile.immediate) {
      await expect(
        immediateSection.getByRole("heading", {
          name: profile.immediate,
          exact: true,
        }),
      ).toBeVisible();
    } else {
      await expect(
        immediateSection.getByText(
          "No reviewed claim currently meets the publication threshold.",
          { exact: true },
        ),
      ).toBeVisible();
    }

    const civilianSection = page.locator(
      'section[aria-labelledby="civilian-employer"]',
    );
    if (profile.lastCivilian) {
      await expect(
        civilianSection.getByRole("heading", {
          name: profile.lastCivilian,
          exact: true,
        }),
      ).toBeVisible();
    } else {
      await expect(
        civilianSection.getByText(
          profile.terminalMissingCivilian
            ? "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed."
            : "No reviewed claim currently meets the publication threshold.",
          { exact: true },
        ),
      ).toBeVisible();
    }

    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toHaveAttribute("href", /cia\.gov/);
    if (profile.secondSource) {
      await expect(
        page.getByRole("link", { name: profile.secondSource, exact: true }).first(),
      ).toHaveAttribute("href", /aaa\.si\.edu/);
    }
  }
});

test("the official-pathways batch preserves employers, military assignments, and provisional identities", async ({
  page,
}) => {
  const profiles = [
    {
      id: "7227c423-8f14-5430-9824-e79ccac87230",
      name: "Barbara J Lauwers",
      immediate: "Women's Army Corps",
      lastCivilian: "Embassy of Czechoslovakia in Washington",
      source: "Barbara Lauwers: Deceiving the Enemy",
    },
    {
      id: "404292b8-801c-58f0-8f74-6fd447da6adf",
      name: "Franklin P Holcomb",
      immediate: "Office of Naval Intelligence",
      earlier: "Georgetown University",
      source: 'The "Scholastic" Marine Who Won a Secret War',
      category: "commissioned marine corps officer",
    },
    {
      id: "db23d265-0e22-5004-96ad-ab1762b43b92",
      name: "Jeanne H Taylor",
      earlier: "Works Progress Administration, Index of American Design",
      source: 'The "Glorious Amateurs" of OSS: A Sisterhood of Spies',
      needsIdentityReview: true,
    },
    {
      id: "b78087f9-4898-5aae-bf3d-43dba862cb78",
      name: "Sherman Kent",
      immediate: "Coordinator of Information",
      lastCivilian: "Yale University",
      source: "Sherman Kent and the Profession of Intelligence Analysis",
    },
    {
      id: "d94ecc56-f483-5cd6-8577-22447eb6a8d7",
      name: "Walter C Langer",
      immediate: "Self-employed",
      lastCivilian: "Self-employed",
      source: "Official OSS Exhibition Catalogue",
    },
    {
      id: "e9aac0ee-0132-5166-b8ab-1e9e8d89fe93",
      name: "William L Langer",
      immediate: "Harvard University",
      lastCivilian: "Harvard University",
      earlier: "Clark University",
      source: "The Historian-Autobiographers",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();

    const immediateSection = page.locator(
      'section[aria-labelledby="immediate-affiliation"]',
    );
    if (profile.immediate) {
      await expect(
        immediateSection.getByRole("heading", {
          name: profile.immediate,
          exact: true,
        }),
      ).toBeVisible();
    }

    const civilianSection = page.locator(
      'section[aria-labelledby="civilian-employer"]',
    );
    if (profile.lastCivilian) {
      await expect(
        civilianSection.getByRole("heading", {
          name: profile.lastCivilian,
          exact: true,
        }),
      ).toBeVisible();
    }

    if (profile.earlier) {
      await expect(
        page.getByRole("heading", { name: profile.earlier, exact: true }).first(),
      ).toBeVisible();
    }
    if (profile.category) {
      await expect(page.getByText(profile.category, { exact: true }).first()).toBeVisible();
    }
    if (profile.needsIdentityReview) {
      await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toBeVisible();
  }
});

test("Batch 009 preserves civilian, military, government, and duplicate-row boundaries", async ({
  page,
}) => {
  const profiles = [
    {
      id: "52aacf03-c330-5566-9091-7bc961b1266b",
      name: "William J Donovan",
      immediate: "Coordinator of Information",
      lastCivilian: "Donovan, Leisure, Newton & Irvine",
      source: "William Donovan: Spymaster, War Hero, and Columbia Law School Graduate",
    },
    {
      id: "a0f164c7-505d-5cb9-88e1-0c3c1f1be22f",
      name: "Carl F Eifler",
      immediate: "K Company, 35th Infantry Regiment",
      lastCivilian: "United States Customs Service",
      source: "Colonel Carl F. Eifler, US Army, Retired",
    },
    {
      id: "c353768b-d393-5b1c-92ba-47d7cbfe28dc",
      name: "David K Bruce",
      immediate: "American Red Cross",
      lastCivilian: "American Red Cross",
      source: "David K. E. Bruce Oral History Interview",
    },
    {
      id: "7ac0f4ab-1444-5819-9a43-ee750f6f5617",
      name: "Frank G Wisner",
      immediate: "Office of Naval Intelligence",
      lastCivilian: "Carter, Ledyard & Milburn",
      source: "General Walter Bedell Smith as Director of Central Intelligence, October 1950-February 1953, Volume II",
    },
    {
      id: "fdfd99fd-2cdd-5f1e-a101-0d1a36440f06",
      name: "John A Bross",
      immediate: "United States Army Air Forces",
      lastCivilian: "Self-employed legal practice",
      source: "John Bross Receives Army Air Forces Commission (April 1942)",
    },
    {
      id: "221b804d-039b-5da1-ad65-c62ea650a63b",
      name: "Kermit Roosevelt Jr.",
      immediate: "California Institute of Technology",
      lastCivilian: "California Institute of Technology",
      source: "Zendebad, Shah! The Central Intelligence Agency and the Fall of Iranian Prime Minister Mohammad Mossadeq, August 1953",
    },
    {
      id: "8f01ec1e-7a03-5d7b-8ebd-8144fdfd6d85",
      name: "Samson Lane Faison",
      immediate: "United States Naval Reserve",
      lastCivilian: "Williams College",
      source: "Legendary Art History Teacher and Long-time Williams Faculty Member Lane Faison Dies",
    },
    {
      id: "a2d66764-90d0-5d8d-8102-30c2e0b03ba1",
      name: "Peter M F Sichel",
      immediate: "United States Army Medical Corps",
      source: "The Secrets of My Life: Vintner, Prisoner, Soldier, Spy",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    await expect(
      page
        .locator('section[aria-labelledby="immediate-affiliation"]')
        .getByRole("heading", { name: profile.immediate, exact: true }),
    ).toBeVisible();
    if (profile.lastCivilian) {
      await expect(
        page
          .locator('section[aria-labelledby="civilian-employer"]')
          .getByRole("heading", { name: profile.lastCivilian, exact: true }),
      ).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toBeVisible();
  }

  await page.goto("./people/1bf7bd5e-a790-51d0-9a46-e6046cab07f2/");
  await expect(
    page.getByRole("heading", { name: "Peter M Sichel", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();
  await expect(page.getByText("duplicate-1f825d1c2a6f", { exact: true })).toBeVisible();
  await expect(
    page.getByText(
      "The Peter M. Sichel row remains separate from the adjacent Peter M. F. Sichel row pending direct service-number linkage.",
      { exact: true },
    ),
  ).toBeVisible();
});

test("Batch 010 preserves military, government, civilian-employer, fellowship, and unresolved boundaries", async ({
  page,
}) => {
  const profiles = [
    {
      id: "b6f213df-1110-5f54-8821-8787886a7633",
      name: "Aaron Bank",
      immediate: "Unspecified Transportation Railroad Battalion",
      earlier: "Unidentified resort in Biarritz",
      source: "Colonel Aaron Bank: 1902-2004",
    },
    {
      id: "7f111cc6-d046-5eac-93ab-63f6387c204b",
      name: "Arthur M Schlesinger",
      immediate: "United States Office of War Information",
      earlier: "Harvard Society of Fellows",
      source: "Schlesinger, Arthur Meier, Jr., 1917-2007",
    },
    {
      id: "e972f0e6-54f0-5b2e-a07c-035c83718850",
      name: "John K Singlaub",
      immediate: "515th Parachute Infantry Regiment",
      source: "Interview with Maj. Gen. John K. Singlaub, U.S. Army, Ret.",
    },
    {
      id: "e091453b-28d3-5f35-a907-415c62dfc364",
      name: "John King Fairbank",
      lastCivilian: "Harvard University",
      source: "John K. Fairbank: The Life of John King Fairbank",
    },
    {
      id: "6dff4a3a-1141-5a4c-8a77-2ea2a7c99ab0",
      name: "Walt W Rostow",
      lastCivilian: "Columbia University",
      source: "Walt Rostow, 86; Top Advisor on Vietnam",
    },
    {
      id: "4ed9479d-32f1-5c48-9d6e-645d0405c42f",
      name: "Roger Hilsman",
      immediate: "5307th Composite Unit (Provisional)",
      source: "Roger Hilsman, foreign policy adviser to JFK, dies at 94",
    },
    {
      id: "a48e130d-4c6d-58b0-9257-bc88435ed84b",
      name: "Lyman B Kirkpatrick",
      immediate: "United States Army",
      lastCivilian: "United States News",
      source: "Lyman Bickford Kirkpatrick Jr. '38",
    },
    {
      id: "d8754b27-3c32-5445-a5fe-063299aa869c",
      name: "Ray S Cline",
      immediate: "United States Department of the Navy",
      earlier: "Harvard Society of Fellows",
      source: "Ray S. Cline Papers",
    },
    {
      id: "12930941-5301-558f-9ded-a45a0d6e4b82",
      name: "Paul Mellon",
      immediate: "United States Army",
      earlier: "Mellon Bank (historical name as found)",
      source: "Paul Mellon, Founder",
    },
  ];

  for (const profile of profiles) {
    await page.goto(`./people/${profile.id}/`);
    await expect(
      page.getByRole("heading", { name: profile.name, exact: true }),
    ).toBeVisible();
    if (profile.immediate) {
      await expect(
        page
          .locator('section[aria-labelledby="immediate-affiliation"]')
          .getByRole("heading", { name: profile.immediate, exact: true }),
      ).toBeVisible();
    }
    if (profile.lastCivilian) {
      await expect(
        page
          .locator('section[aria-labelledby="civilian-employer"]')
          .getByRole("heading", { name: profile.lastCivilian, exact: true }),
      ).toBeVisible();
    }
    if (profile.earlier) {
      await expect(
        page
          .locator('section[aria-labelledby="earlier-affiliations"]')
          .getByRole("heading", { name: profile.earlier, exact: true }),
      ).toBeVisible();
    }
    await expect(
      page.getByRole("link", { name: profile.source, exact: true }).first(),
    ).toBeVisible();
  }

  await page.goto("./people/c490f753-bc95-59f6-8f99-7ab2d2455293/");
  await expect(
    page.getByRole("heading", { name: "Archimedes L Patti", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true })).toBeVisible();
  await expect(
    page.getByText(
      "Review Box 589 and Army personnel records to establish the immediate pre-OSS assignment and last civilian employer.",
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "OSS in Action: The Pacific and the Far East", exact: true }),
  ).toBeVisible();
});

test("Batch 011 preserves concurrent employment, predecessor agencies, military pathways, and non-employer affiliations", async ({
  page,
}) => {
  await page.goto("./people/928871ef-6c5b-54dd-8967-08e8afcd7efc/");
  await expect(
    page.getByRole("heading", { name: "Carleton S Coon", exact: true }),
  ).toBeVisible();
  for (const organization of [
    "Harvard University",
    "Peabody Museum of Archaeology and Ethnology",
  ]) {
    await expect(
      page
        .locator('section[aria-labelledby="immediate-affiliation"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
    await expect(
      page
        .locator('section[aria-labelledby="civilian-employer"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
  }
  await expect(
    page.getByRole("link", { name: "Carleton Stevens Coon papers", exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/9e161c56-f13d-52f7-bc8c-778fe6ff8677/");
  await expect(
    page.getByRole("heading", { name: "Norman H Pearson", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Yale University", exact: true }),
    ).toBeVisible();
  }
  await expect(
    page.getByRole("link", { name: "History of the Department", exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/86d85b71-ed82-5b7f-87dd-0d456d58ff3d/");
  await expect(
    page.getByRole("heading", { name: "Philip E Mosely", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Cornell University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "United States Department of State, Division of Special Research",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Cornell Alumni News", exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/cae068be-d703-5d95-adc7-a645430834fd/");
  await expect(
    page.getByRole("heading", { name: "Millard P Goodfellow", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army G-2", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "M. Preston Goodfellow's unnamed business",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "OSS Training in the National Parks and Service Abroad in World War II: Chapter 1, Origins of the OSS",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/3f476b5c-bf12-532d-8879-1646130029e0/");
  await expect(
    page.getByRole("heading", { name: "Whitney Shepardson", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Council on Foreign Relations", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true })).toBeVisible();
  await expect(
    page.getByText(
      "Review Box 703 and CFR archival records to identify Shepardson's immediate pre-OSS status and last civilian employer without treating his officer role as employment.",
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "The Office of Strategic Services: America's First Intelligence Agency",
        exact: true,
      })
      .first(),
  ).toBeVisible();
});

test("Batch 012 preserves qualified military pathways, unnamed employers, student status, and archival uncertainty", async ({
  page,
}) => {
  await page.goto("./people/495e4e73-3aa2-5afa-b5b3-838e28cc7957/");
  await expect(
    page.getByRole("heading", { name: "William A Eddy", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Marine Corps", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Hobart and William Smith Colleges",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Presidents and Deans", exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/66142cc6-36c6-519b-8765-986f995322e3/");
  await expect(
    page.getByRole("heading", { name: "Archibald B Roosevelt", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Unidentified Spokane and San Francisco newspapers",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "New York Herald Tribune", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", { name: "Archibald Roosevelt Jr. Papers", exact: true })
      .first(),
  ).toBeVisible();

  await page.goto("./people/01360217-ccc5-5754-a6d5-9d126bfc08f0/");
  await expect(
    page.getByRole("heading", { name: "John H Hemingway", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Dartmouth College", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", { name: "The Son Also Rises: Jack Hemingway", exact: true })
      .first(),
  ).toBeVisible();

  await page.goto("./people/142be2db-06a1-51ef-8725-027388a3d15e/");
  await expect(
    page.getByRole("heading", { name: "Gertrude Legendre", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "American Museum of Natural History",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true })).toBeVisible();
  await expect(
    page.getByText(
      "Review Box 443 and Mss 0182 wartime files to identify her immediate pre-OSS status and any civilian employer without converting property ownership or expedition participation into employment.",
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "The Gertrude Sanford Legendre papers",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/c9accc19-41c3-51ce-b173-2a51b4eea522/");
  await expect(
    page.getByRole("heading", { name: "DeWitt C Poole", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Princeton University School of Public Affairs",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Donovan and the CIA: A History of the Establishment of the Central Intelligence Agency",
        exact: true,
      })
      .first(),
  ).toBeVisible();
});

test("Batch 013 preserves career-military, civilian-cover, academic, probable-identity, and qualified-employer pathways", async ({
  page,
}) => {
  await page.goto("./people/a93ac760-896e-50b9-9746-754d434a1200/");
  await expect(
    page.getByRole("heading", { name: "John Magruder", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "U.S. Military Mission to China", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Origins of Central Intelligence",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/f443009b-dd5f-542b-9a0c-3af2d21f8611/");
  await expect(
    page.getByRole("heading", { name: "Donald C Downes", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Free World Association", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Free World Association", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Robert College", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Guide to the Donald Chase Downes Papers",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/8dd153b1-fab9-5ab0-a015-3f2e6bcfaac1/");
  await expect(
    page.getByRole("heading", { name: "Bruce C Hopper", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Papers of Bruce Campbell Hopper, 1918-1971",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/62745da7-0c09-58fa-be20-99a797c8d9aa/");
  await expect(
    page.getByRole("heading", { name: "Leopold Schwarsschild", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Das Neue Tage-Buch", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("probable", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText(
      "Review Box 690 to confirm the spelling, birth details, immigration history, and whether the CAF-11 record belongs to editor Leopold Schwarzschild.",
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Leopold Schwarzschild / Photograph by Fred Stein",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/a9b1ec13-509a-57f2-bb04-d2453d49e908/");
  await expect(
    page.getByRole("heading", { name: "Paul C Child", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Avon Old Farms School", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Avon Old Farms School", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("medium", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Julia Child: Cooking Up Spy Ops for OSS",
        exact: true,
      })
      .first(),
  ).toBeVisible();
});

test("Batch 014 preserves Allied transfers, concurrent employers, student status, government pathways, and unnamed self-employment", async ({
  page,
}) => {
  await page.goto("./people/b635033f-c426-5c5c-b55d-73c37acb9cd7/");
  await expect(
    page.getByRole("heading", { name: "Stewart J Alsop", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "King's Royal Rifle Corps, 60th Regiment",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Doubleday, Doran & Company", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Joseph Alsop and Stewart Alsop Papers",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/d5ef765f-15f7-5b73-bfa8-40b49281e265/");
  await expect(
    page.getByRole("heading", { name: "Ross Lee Finney", exact: true }),
  ).toBeVisible();
  for (const organization of ["Mount Holyoke College", "Hartt School of Music"]) {
    await expect(
      page
        .locator('section[aria-labelledby="immediate-affiliation"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
    await expect(
      page
        .locator('section[aria-labelledby="civilian-employer"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Smith College", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", { name: "Ross Lee Finney Papers", exact: true })
      .first(),
  ).toBeVisible();

  await page.goto("./people/6cf300e3-bf39-5847-a2ab-50c7320d26cd/");
  await expect(
    page.getByRole("heading", { name: "Doris A Sharrar", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Montgomery Blair High School", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page.getByText(
      "Review Box 700 for Sharrar's activity between 1940 graduation and post-Pearl Harbor OSS entry; no pre-OSS employer is documented online.",
      { exact: true },
    ),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "The Glorious Amateurs of OSS: A Sisterhood of Spies",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/a908557f-c6ef-52b3-a94f-878cbf920f79/");
  await expect(
    page.getByRole("heading", { name: "Chauncy D Harris", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Department of State, Office of the Geographer",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Chicago", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Guide to the Chauncy D. Harris Papers 1893-2003",
        exact: true,
      })
      .first(),
  ).toBeVisible();

  await page.goto("./people/4f5707b0-a4d3-5fb1-940e-223b8d0e0d41/");
  await expect(
    page.getByRole("heading", { name: "Stanley P Lovell", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Self-employed", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Self-employed", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("heading", {
      name: "Lovell was running his own Massachusetts company when Donovan recruited him to lead OSS Research and Development.",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", { name: "OSS Exhibition Catalogue", exact: true })
      .first(),
  ).toBeVisible();
});

test("Batch 015 preserves academic, fashion, military, student, and unnamed-employer pathways", async ({
  page,
}) => {
  await page.goto("./people/c691c388-f4c1-51be-9047-eea867abc968/");
  await expect(
    page.getByRole("heading", { name: "Gardner Ackley", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Office of Price Administration",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Michigan", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "The Ohio State University", exact: true }),
  ).toBeVisible();

  await page.goto("./people/c1f57bc0-8b8e-5fbe-b4b8-1e146322c366/");
  await expect(
    page.getByRole("heading", { name: "Marie Aline Griffith", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Hattie Carnegie", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/0b96a6dd-4d77-53b2-aad5-e942aebe4d3a/");
  await expect(
    page.getByRole("heading", { name: "John W Gardner", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Marine Corps", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Mount Holyoke College", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();

  await page.goto("./people/2dc32dd2-4124-5470-9c31-7fe64bfbb9f7/");
  await expect(
    page.getByRole("heading", { name: "Hugh Montgomery", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();

  await page.goto("./people/5e7905c6-6565-5f51-8b37-03e0f57205a1/");
  await expect(
    page.getByRole("heading", { name: "Lucien E Conein", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Unidentified Kansas City printer",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Kansas National Guard, Company G, 137th Infantry Regiment",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "\"No Boy Scout\": CIA Operations Officer Lucien Conein: A Study in Contrasts and Controversy",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", /cia\.gov/);
});

test("Batch 016 preserves academic, design, military, government, alias, and occupation-only pathways", async ({
  page,
}) => {
  await page.goto("./people/039ff924-7560-5963-be0d-3e15c917d9d2/");
  await expect(
    page.getByRole("heading", { name: "Henry A Murray", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Harvard Psychological Clinic", exact: true }),
  ).toBeVisible();

  await page.goto("./people/d1b224f9-97fc-5bc8-8aac-088a4f139d48/");
  await expect(
    page.getByRole("heading", { name: "Conyers Read", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Pennsylvania", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "William F. Read and Sons Company", exact: true }),
  ).toBeVisible();

  await page.goto("./people/b716d0a6-b18c-55c9-addd-721ae710f134/");
  await expect(
    page.getByRole("heading", { name: "Donal McLaughlin", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Raymond Loewy industrial design office", exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "National Park Service", exact: true }),
  ).toBeVisible();

  await page.goto("./people/2c22bdd2-c625-51d7-b16d-10602a1770fa/");
  await expect(
    page.getByRole("heading", { name: "Lincoln Lundquist", exact: true }),
  ).toBeVisible();
  await expect(page.getByText(/Oliver Lincoln Lundquist/).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States War Department", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Raymond Loewy industrial design office", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();

  await page.goto("./people/232b3c0e-0988-59b0-a34c-9984cc3170c8/");
  await expect(
    page.getByRole("heading", { name: "William J Morgan", exact: true }),
  ).toBeVisible();
  await expect(page.getByText(/Anthony J\. Mitrano/).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(page.getByText(/school psychologist/i).first()).toBeVisible();
});

test("Batch 017 preserves membership, overlapping employment, qualified government pathways, and indexed variants", async ({
  page,
}) => {
  await page.goto("./people/d5fddfcc-304b-5207-878a-e5231e647295/");
  await expect(
    page.getByRole("heading", { name: "Felix Gilbert", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Institute for Advanced Study", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText(/professional affiliation/i),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Scripps College", exact: true }),
  ).toBeVisible();

  await page.goto("./people/9d917a08-06a5-5ec3-bebf-5c43b422a5aa/");
  await expect(
    page.getByRole("heading", { name: "Franz L Neumann", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Board of Economic Warfare",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("medium", { exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Institute for Social Research", exact: true }),
  ).toBeVisible();

  await page.goto("./people/690eab64-a21e-57dc-ae33-6dc576d5ea07/");
  await expect(
    page.getByRole("heading", { name: "Haje Holborn", exact: true }),
  ).toBeVisible();
  await expect(page.getByText(/Dr\. Hajo Holborn;.*Hajo Holborn/).first()).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Yale University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/1a923c3f-6b6e-5107-a470-9804a030c2bd/");
  await expect(
    page.getByRole("heading", { name: "Edward M Earle", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Institute for Advanced Study", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/4ebb85b3-0542-5281-b254-b36e810242bb/");
  await expect(
    page.getByRole("heading", { name: "Sigmund Neumann", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Wesleyan University", exact: true }),
    ).toBeVisible();
  }
});

test("Batch 018 separates continuing academic employment, Army transitions, and student status", async ({
  page,
}) => {
  await page.goto("./people/1adc6b42-2c4d-5611-ba6e-8cdbfd8ac6e0/");
  await expect(
    page.getByRole("heading", { name: "Crane Brinton", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Harvard University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/b47e5c36-3250-5574-a213-c8902573806a/");
  await expect(
    page.getByRole("heading", { name: "Harold C Deutsch", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "University of Minnesota", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/c974e4f4-d9ea-5e9f-bcef-8bb019cb9f1f/");
  await expect(
    page.getByRole("heading", { name: "Perry G.E. Miller", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();

  await page.goto("./people/78c03a2c-11e1-5f34-bf53-bc76c5f33817/");
  await expect(
    page.getByRole("heading", { name: "Franklin L Ford", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Cornell University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByText("Graduate student", { exact: true }),
  ).toBeVisible();

  await page.goto("./people/fb9b02f9-9dfb-5965-8514-fa5b73e3b2c9/");
  await expect(
    page.getByRole("heading", { name: "Gordon A Craig", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Princeton University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("medium", { exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("Doctoral student", { exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
});

test("Batch 019 separates federal and academic employment, Army service, and doctoral study", async ({
  page,
}) => {
  await page.goto("./people/5fc9dce9-664e-591d-bbed-c0d6b517c1e3/");
  await expect(
    page.getByRole("heading", { name: "Charles P Kindleberger", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", {
          name: "Board of Governors of the Federal Reserve System",
          exact: true,
        }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Bank for International Settlements", exact: true }),
  ).toBeVisible();

  await page.goto("./people/2e169a05-3d86-50b7-b195-4e5bb9b7cf0d/");
  await expect(
    page.getByRole("heading", { name: "Abram Bergson", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "University of Texas at Austin", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/3afb0ff0-6fae-57d7-812e-3a6143a4db19/");
  await expect(
    page.getByRole("heading", { name: "Stuart H Hughes", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Brown University", exact: true }),
  ).toBeVisible();

  await page.goto("./people/d086f590-f86d-5535-8411-aa60aa252f01/");
  await expect(
    page.getByRole("heading", { name: "Carl E Schorske", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("Doctoral student in German history", { exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();

  await page.goto("./people/2ed25b69-80d3-5c7b-91cd-d70bca18cd2a/");
  await expect(
    page.getByRole("heading", { name: "Richard Hartshorne", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "University of Wisconsin-Madison", exact: true }),
    ).toBeVisible();
  }
});

test("Batch 020 separates student, civilian-employer, and government-assignment pathways", async ({
  page,
}) => {
  await page.goto("./people/e909510a-c0a7-53e3-adb2-4e0c29f8a601/");
  await expect(
    page.getByRole("heading", { name: "Arthur H Robinson", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "The Ohio State University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("Graduate student pursuing a Ph.D. in geography", { exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();

  await page.goto("./people/79d464a9-2e5e-5f96-b326-e8bbb03d7a79/");
  await expect(
    page.getByRole("heading", { name: "Edward A Ackerman", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Harvard University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/ae91f5d4-44b6-5096-89e9-9f6debbf5a24/");
  await expect(
    page.getByRole("heading", { name: "Emile Despres", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", {
          name: "Board of Governors of the Federal Reserve System",
          exact: true,
        }),
    ).toBeVisible();
  }

  await page.goto("./people/803386f6-0ee8-59b5-ae2a-4c0c086993a7/");
  await expect(
    page.getByRole("heading", { name: "Carl Kaysen", exact: true }),
  ).toBeVisible();
  for (const organization of [
    "National Bureau of Economic Research",
    "Columbia University",
  ]) {
    await expect(
      page
        .locator('section[aria-labelledby="immediate-affiliation"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "National Bureau of Economic Research",
        exact: true,
      }),
  ).toBeVisible();

  await page.goto("./people/e3b15c03-9d62-5a59-8ac0-117fe8e68bef/");
  await expect(
    page.getByRole("heading", { name: "Edward S Mason", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "U.S. Office of Production Management",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "U.S. Department of Labor", exact: true }),
  ).toBeVisible();
});

test("Batch 021 separates academic, Federal Reserve, NBER, and OPA pathways", async ({
  page,
}) => {
  await page.goto("./people/e6f133b8-bd4a-5796-978c-b91076896fef/");
  await expect(
    page.getByRole("heading", { name: "Geroid T Robinson", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Columbia University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/d633583e-637d-519b-a417-0eeb7ee8305b/");
  await expect(
    page.getByRole("heading", { name: "Barrington Moore", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByText("No reviewed claim currently meets the publication threshold.", {
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByText(
        "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
        { exact: true },
      ),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Yale University", exact: true }),
  ).toBeVisible();

  await page.goto("./people/1d4ac037-dc29-51c0-81b4-c55b3b536f46/");
  await expect(
    page.getByRole("heading", { name: "Calvin B Hoover", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Duke University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/025318bc-bb51-5ebd-9d13-fb4c728dbfa8/");
  await expect(
    page.getByRole("heading", { name: "Chandler Morse", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Board of Governors of the Federal Reserve System",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Federal Reserve Bank of New York", exact: true }),
  ).toBeVisible();

  await page.goto("./people/d38ec240-05df-5155-abc9-3ed54484ff5f/");
  await expect(
    page.getByRole("heading", { name: "Sidney S Alexander", exact: true }),
  ).toBeVisible();
  for (const organization of [
    "National Bureau of Economic Research",
    "United States Office of Price Administration",
  ]) {
    await expect(
      page
        .locator('section[aria-labelledby="immediate-affiliation"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "National Bureau of Economic Research",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
});

test("Batch 022 separates museum, university, research, and student pathways", async ({
  page,
}) => {
  await page.goto("./people/1147408f-3793-5ab4-9176-58a04dd8ad5f/");
  await expect(
    page.getByRole("heading", { name: "Gregory Bateson", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "The Museum of Modern Art", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/ae597b0c-6982-5c47-8b87-f74cfb29b92c/");
  await expect(
    page.getByRole("heading", { name: "John F Embree", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "University of Toronto", exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "University of Hawaii", exact: true }),
  ).toBeVisible();

  await page.goto("./people/90b3258d-f890-5535-982f-6fd2b275caf9/");
  await expect(
    page.getByRole("heading", { name: "Ralph Linton", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Columbia University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/0c060ee9-da85-5446-94b6-77bc939fd231/");
  await expect(
    page.getByRole("heading", { name: "Rhoda Metraux", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "National Research Council", exact: true }),
    ).toBeVisible();
  }
  for (const organization of ["Oxford University Press", "Yale University"]) {
    await expect(
      page
        .locator('section[aria-labelledby="earlier-affiliations"]')
        .getByRole("heading", { name: organization, exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/59eb0f93-2dc1-51db-8fe3-100a43fef801/");
  await expect(
    page.getByRole("heading", { name: "Raymond Kennedy", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Yale University", exact: true }),
    ).toBeVisible();
  }
});

test("Batch 023 separates civilian employers from COI and Army predecessor assignments", async ({
  page,
}) => {
  await page.goto("./people/0481f178-4ac5-565a-8a7a-09733f86f6fa/");
  await expect(
    page.getByRole("heading", { name: "James P Baxter III", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Williams College", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("WO C", { exact: true })).toBeVisible();
  await expect(
    page.getByText("unknown or indeterminate", { exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/6c04259d-0aaf-5c19-87e9-6fb1d7000112/");
  await expect(
    page.getByRole("heading", { name: "Saul K Padover", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", {
          name: "United States Department of the Interior",
          exact: true,
        }),
    ).toBeVisible();
  }
  await expect(page.getByText("Assistant to the Secretary", { exact: true }).first()).toBeVisible();

  await page.goto("./people/988b1615-a74b-5020-a82d-cbd8831f21c9/");
  await expect(
    page.getByRole("heading", { name: "C. Martin Wilbur", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Field Museum of Natural History", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/2da25f0d-1148-57f0-b356-810e445c281b/");
  await expect(
    page.getByRole("heading", { name: "Charles F Remer", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Michigan", exact: true }),
  ).toBeVisible();
  await expect(page.getByRole("link", { name: "NAID 2184121", exact: true })).toHaveAttribute(
    "href",
    "https://catalog.archives.gov/id/2184121",
  );

  await page.goto("./people/b5293d31-eab2-5557-a664-0c2097017949/");
  await expect(
    page.getByRole("heading", { name: "Morris Janowitz", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "United States Department of Justice", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "New York University", exact: true }),
  ).toBeVisible();
});

test("Batch 024 preserves academic, government, military, and uncertain pathways", async ({
  page,
}) => {
  await page.goto("./people/61638d98-2b07-50f1-b1fd-ee8f1254c3e6/");
  await expect(
    page.getByRole("heading", { name: "Edward A Shils", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Chicago", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable immediate", { exact: true })).toBeVisible();

  await page.goto("./people/6885339c-afe2-5326-982a-6e0d6735c28c/");
  await expect(
    page.getByRole("heading", { name: "Sterling Dow", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "Harvard University", exact: true }),
    ).toBeVisible();
  }

  await page.goto("./people/424a424a-9dbb-5ed8-a29c-69aa4c2e9831/");
  await expect(
    page.getByRole("heading", { name: "Donald C McKay", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Coordinator of Information", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();

  await page.goto("./people/bc1757bd-9946-593f-8575-8c470dd6c61f/");
  await expect(
    page.getByRole("heading", { name: "John L Clive", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Hans Leo Kleyff");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "University of North Carolina at Chapel Hill",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "No reliable pre-OSS civilian employer has yet been identified",
  );
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);

  await page.goto("./people/fe8ec29a-718c-56f3-af64-d619600f4f0d/");
  await expect(
    page.getByRole("heading", { name: "Robert L Wolff", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("temporal relation uncertain", { exact: true })).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByText("medium", { exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "does not establish whether it preceded or followed OSS",
  );
});

test("Batch 025 separates academic employment, student status, and military or government predecessors", async ({
  page,
}) => {
  await page.goto("./people/29a830f4-a1d4-5821-af64-d014e89c71da/");
  await expect(
    page.getByRole("heading", { name: "Preston E James", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Coordinator of Information",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "University of Michigan", exact: true }),
  ).toBeVisible();

  await page.goto("./people/08a92bff-7683-5a94-bd92-09a33ef5e667/");
  await expect(
    page.getByRole("heading", { name: "Norman O Brown", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Nebraska Wesleyan University",
        exact: true,
      }),
  ).toBeVisible();

  await page.goto("./people/56b8952b-c21c-5f0f-b653-22fb22980b15/");
  await expect(
    page.getByRole("heading", { name: "Leonard Krieger", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Yale University", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "No reliable pre-OSS civilian employer has yet been identified",
  );
});

test("Batch 025 keeps the two Paul M Sweezy rows separate and withholds the biographical candidate", async ({
  page,
}) => {
  const profiles = [
    "ead0d460-6fcd-51cd-a6d4-01862ecc82f8",
    "8686bb8e-3b16-5aa2-bb72-bdd2e6a6f3aa",
  ];
  for (const personId of profiles) {
    await page.goto(`./people/${personId}/`);
    await expect(
      page.getByRole("heading", { name: "Paul M Sweezy", exact: true }),
    ).toBeVisible();
    await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.getByText("critical", { exact: true })).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "accessible sources do not map either number",
    );
    await expect(page.locator("body")).toContainText(
      "No reviewed claim currently meets the publication threshold",
    );
    expect(await page.locator("article.claim-card").count()).toBe(0);
    expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
  }
});

test("Batch 026 separates civilian work, military assignment, and student status for five women", async ({
  page,
}) => {
  await page.goto("./people/9b51ae67-0705-5366-84d1-75d1266f4e1e/");
  await expect(
    page.getByRole("heading", { name: "Mary D Bancroft", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Self-employed", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Self-employed", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Reminiscences of Mary Bancroft, 1979-1980",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://researchworks.oclc.org/archivegrid/archiveComponent/269253002",
  );

  await page.goto("./people/dce57294-738d-5a94-980d-df3821ed4b3e/");
  await expect(
    page.getByRole("heading", { name: "Stephanie Czech", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Women's Army Corps", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Texas Oil Company", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("commissioned army officer", { exact: true }).first()).toBeVisible();

  await page.goto("./people/16cc0420-e809-5938-bbb5-042b165dcfc4/");
  await expect(
    page.getByRole("heading", { name: "Elizabeth P MacDonald", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Scripps-Howard News Service", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Honolulu Advertiser", exact: true }),
  ).toBeVisible();

  await page.goto("./people/614cf208-c223-5a74-b23d-f4d3edd1bfda/");
  await expect(
    page.getByRole("heading", { name: "Jane Foster", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Mills College", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("student");
  await expect(page.locator("body")).toContainText(
    "No reliable named pre-OSS employer has yet been identified",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Transitioning into CIA: The Strategic Services Unit in Indonesia",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/resources/csi/static/Transitioning-into-CIA.pdf",
  );

  await page.goto("./people/128fcc95-79fa-5d1f-8893-90ba9c5defb6/");
  await expect(
    page.getByRole("heading", { name: "Stella T Uzdawinis", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "No reliable pre-OSS employer has yet been identified",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Stella Uzdawinis's Office of Strategic Services Pendant",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/legacy/museum/artifact/stella-uzdawiniss-office-of-strategic-services-pendant/",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 027 separates employers, independent scholarship, military status, and unnamed financial work", async ({
  page,
}) => {
  await page.goto("./people/5dd07840-484a-5a8d-be2c-4b1b16545ed6/");
  await expect(
    page.getByRole("heading", { name: "Joseph R Hayden", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", { name: "University of Michigan", exact: true }),
    ).toBeVisible();
  }
  await expect(
    page
      .getByRole("link", {
        name: "Joseph Ralston Hayden Papers, 1854-1975",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://findingaids.lib.umich.edu/catalog/umich-bhl-851643",
  );

  await page.goto("./people/20cd1668-459e-529d-ac47-85b422f746e4/");
  await expect(
    page.getByRole("heading", { name: "Wilmarth S Lewis", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Independent Horace Walpole scholarship and collecting",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText("professional affiliation");

  await page.goto("./people/aaa83b52-5ab0-5c86-9146-db6dc477dd9e/");
  await expect(
    page.getByRole("heading", { name: "Junius S Morgan", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "J.P. Morgan & Co.", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("commissioned naval officer", { exact: true }).first(),
  ).toBeVisible();

  await page.goto("./people/fd719ab0-0e3d-56dd-b163-810da257da6e/");
  await expect(
    page.getByRole("heading", { name: "William L Rehm", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "one of the largest investment trusts in the United States",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/dac80940-34d9-5545-8d3b-b3b509a69238/");
  await expect(
    page.getByRole("heading", { name: "R H Goddard", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Goddard Brothers", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Robert H. Ives Goddard");
  await expect(page.locator("body")).toContainText("professional affiliation");

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 028 separates government, business, military, fellowship, and student pathways", async ({
  page,
}) => {
  await page.goto("./people/78a869fb-aa25-5d6a-aca6-59feb5e38171/");
  await expect(
    page.getByRole("heading", { name: "Paul Baran", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Office of Price Administration",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText(
    "Brookings Institution research fellowship",
  );
  await expect(page.locator("body")).toContainText(
    "his uncles' timber business",
  );

  await page.goto("./people/4004a23d-52bc-5ce6-b450-36238827b287/");
  await expect(
    page.getByRole("heading", { name: "G E Buxton", exact: true }),
  ).toBeVisible();
  for (const section of ["immediate-affiliation", "civilian-employer"]) {
    await expect(
      page
        .locator(`section[aria-labelledby="${section}"]`)
        .getByRole("heading", {
          name: "B. B. & R. Knight Company",
          exact: true,
        }),
    ).toBeVisible();
  }
  await expect(page.locator("body")).toContainText(
    "exact B. B. & R. Knight departure date, 1939-1941 activities",
  );

  await page.goto("./people/30ddbc7e-f6fe-56ab-8651-8f743563cd7c/");
  await expect(
    page.getByRole("heading", { name: "James R Forgan", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText(
    "No reviewed claim currently meets the publication threshold.",
  );
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Glore, Forgan & Co.", exact: true }),
  ).toBeVisible();

  await page.goto("./people/0d2d73be-e7ba-5b98-8494-0e9b9adaa189/");
  await expect(
    page.getByRole("heading", { name: "Everette H Hunt Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText(
    "Brown is not classified as his employer",
  );

  await page.goto("./people/ab9ab673-8090-56bf-9973-36b0edc77610/");
  await expect(
    page.getByRole("heading", { name: "Shaw Livermore Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Mercersburg Academy");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 029 separates SOE, police, military, maritime, student, and unnamed work pathways", async ({
  page,
}) => {
  await page.goto("./people/44112d43-06b1-5114-aa17-91a6cffb1939/");
  await expect(
    page.getByRole("heading", { name: "William E Fairbairn", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Special Operations Executive", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Shanghai Municipal Police", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("British A");

  await page.goto("./people/789afa1d-9778-5d84-904a-0f341884f736/");
  await expect(
    page.getByRole("heading", { name: "Frank V Huston", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Navy", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("United States Coast Guard");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/bd3c2c04-e39d-57a9-b1ed-6e01285235e3/");
  await expect(
    page.getByRole("heading", { name: "Edward E Nicholas Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Signal Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "University of Illinois Urbana-Champaign",
  );
  await expect(page.locator("body")).toContainText("University of Chicago");

  await page.goto("./people/83cada86-f7bc-557c-a378-6b9af5a5f4a1/");
  await expect(
    page.getByRole("heading", {
      name: "Vincent L Gonzalez Jr.",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Merchant Marine",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Runner");
  await expect(page.locator("body")).toContainText("unnamed employer");
  await expect(page.locator("body")).toContainText("professional affiliation");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/3e307074-39c7-5736-8318-0203a3a813b6/");
  await expect(
    page.getByRole("heading", { name: "Roger L Belanger", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Air Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Instructing for Dangerous Missions",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 030 separates named employers, military and government paths, student status, and an unnamed journalism employer", async ({
  page,
}) => {
  await page.goto("./people/192b5ab4-e4d7-58d4-8ea8-d12e489bf089/");
  await expect(
    page.getByRole("heading", { name: "Edgar A Prichard", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("journalist in Oklahoma");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/dc965089-2d9c-538d-8eaa-96001a5e06b2/");
  await expect(
    page.getByRole("heading", { name: "Jerry M Sage", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Procter & Gamble", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Salesman");

  await page.goto("./people/22cdf385-f081-5297-8f59-5db0c83088d5/");
  await expect(
    page.getByRole("heading", { name: "Elmer Harris", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Marine Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "General Petroleum Company",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("USMCR");

  await page.goto("./people/6c066bb5-f2ad-5a1c-a5e6-85de659ea560/");
  await expect(
    page.getByRole("heading", { name: "George H White", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Federal Bureau of Narcotics",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("probable immediate");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/7f4c48f4-c54f-53da-b317-94db785f8c0b/");
  await expect(
    page.getByRole("heading", {
      name: "Charles M Parkin Jr.",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Corps of Engineers",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Pennsylvania State University",
  );
  await expect(page.locator("body")).toContainText("student");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Instructing for Dangerous Missions",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 031 separates Area B military pathways from student and qualified athletic affiliations", async ({
  page,
}) => {
  await page.goto("./people/a57ba5cd-7218-58e5-a325-6a9e70d925f5/");
  await expect(
    page.getByRole("heading", { name: "Albert Robinso Guay", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("American University");
  await expect(
    page.getByText("enlisted army personnel", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/4626fb9d-f7ed-56b4-a7ec-492c76374b2b/");
  await expect(
    page.getByRole("heading", { name: "Arden W Dow", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Army lieutenant in Military Police");
  await expect(page.locator("body")).toContainText("Washington State University");

  await page.goto("./people/d0e64eee-71c2-58eb-bf99-0e98b74a880a/");
  await expect(
    page.getByRole("heading", { name: "Frank A Gleason", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Corps of Engineers",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Pennsylvania State University",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/832d939e-cbb0-5979-9c57-bb0c0e27113d/");
  await expect(
    page.getByRole("heading", { name: "Joseph Collart", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Washington State University");
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).toContainText(
    "No publishable immediate affiliation or civilian employer is recorded yet",
  );

  await page.goto("./people/576aa158-a1be-56a6-96fc-c6c536de6381/");
  await expect(
    page.getByRole("heading", { name: "Rex Applegate", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("209th Military Police Company");
  await expect(page.locator("body")).toContainText("University of Oregon");
  await expect(page.locator("body")).toContainText("Oregon State University");
  await expect(page.locator("body")).toContainText(
    "exact nature and dates of that institutional association remain uncertain",
  );
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Roll Call: Lieutenant Colonel Rex Applegate (1914-1998)",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.dvidshub.net/news/476096/roll-call-lieutenant-colonel-rex-applegate-1914-1998",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 032 preserves Area B command, engineer, occupation-only, and identity-review boundaries", async ({
  page,
}) => {
  await page.goto("./people/c4b9c664-cdcf-56e7-8bd1-eaa7d5c13a4a/");
  await expect(
    page.getByRole("heading", { name: "Ainsworth Blogg", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Reserve infantry officer assigned to Military Police",
  );
  await expect(page.locator("body")).toContainText(
    "insurance-company executive in Seattle",
  );
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/17ca80e8-cf1a-59e0-b414-e4b748013fa3/");
  await expect(
    page.getByRole("heading", { name: "Louise D Cohen", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("needs identity review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Box 133");
  await expect(page.locator("body")).toContainText(
    "no reviewed service-number or file linkage establishes",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/3049d936-8a0c-5bc3-9e6d-4024e9f59dd3/");
  await expect(
    page.getByRole("heading", { name: "Morris M Kessler", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "probably is the psychiatrist and Captain Morris M. Kessler",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/aaffd5ea-3b75-54a0-b333-ea7e962ed025/");
  await expect(
    page.getByRole("heading", { name: "Joseph E/M Lazarsky", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Joseph E. Lazarsky");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Corps of Engineers",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Sergeant and demolitions instructor",
  );
  await expect(
    page
      .getByRole("link", {
        name: "The Office of Strategic Services (OSS) in World War II",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://coph.fullerton.edu/collections/OHP_18_OSS%20Finding%20Aid.pdf",
  );

  await page.goto("./people/c1fe22b5-0087-5440-9858-6484c72c46e6/");
  await expect(
    page.getByRole("heading", { name: "Leopold Karwoski", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Leopold Karwaski");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Corps of Engineers",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.getByText("Capt", { exact: true }).first()).toBeVisible();

  await expect(
    page
      .getByRole("link", {
        name: "Instructing for Dangerous Missions",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 033 preserves civilian, Army, SOE, qualified-employer, and occupation-only boundaries", async ({
  page,
}) => {
  await page.goto("./people/521c80ee-c975-552a-b41f-d565c60a921b/");
  await expect(
    page.getByRole("heading", { name: "George S Wuchinich", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Fairbanks, Morse and Company",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "determine whether Fairbanks, Morse and Company remained his employer until Army enlistment",
  );
  await expect(
    page
      .getByRole("link", { name: "Carnegie Alumnus", exact: true })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://iiif.library.cmu.edu/file/ALU_1939_025_002_12001939/ALU_1939_025_002_12001939.pdf",
  );

  await page.goto("./people/f28308b3-7c6e-5819-834d-62ec9ef7a65f/");
  await expect(
    page.getByRole("heading", { name: "Hans V Tofte", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Special Operations Executive",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Tofte's immediate pre-OSS affiliation was United States Army service",
  );

  await page.goto("./people/43d0bb66-4c39-5627-85a1-3a85350d973d/");
  await expect(
    page.getByRole("heading", { name: "Howard E Manning", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "Self-employed legal practice",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Manning's last documented civilian work before Army service was his individual legal practice in Raleigh",
  );
  await expect(page.locator("body")).not.toContainText("Manning & Manning");
  await expect(
    page
      .getByRole("link", {
        name: "Hill's Raleigh (Wake County, N.C.) City Directory [1940]",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", "https://lib.digitalnc.org/record/25789?ln=en");

  await page.goto("./people/2bb10033-1c66-53cc-8c22-f465a0085b9d/");
  await expect(
    page.getByRole("heading", { name: "John F Navarro", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("occupation only found", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "restaurateur in New England",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/59b8e455-1c85-5ea4-a087-e756d4d1f5b3/");
  await expect(
    page.getByRole("heading", { name: "Peter G Mero", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "investment executive in Chicago",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Instructing for Dangerous Missions",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 034 preserves radio, cryptology, military, student, and unnamed-institution boundaries", async ({
  page,
}) => {
  await page.goto("./people/f4887f88-5b29-5975-beb5-09370cb58b0c/");
  await expect(
    page.getByRole("heading", { name: "James F Ranney", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Signal Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "engineer at an unnamed radio station in Youngstown",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/d0270e61-812f-5936-95cf-52fed2d3ec42/");
  await expect(
    page.getByRole("heading", {
      name: "Spyridon G Kapponnis",
      exact: true,
    }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Spiro Cappony");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Navy", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Michigan State College", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", { name: "Final Report of the Evros Mission", exact: true })
      .first(),
  ).toHaveAttribute("href", /elia\.org\.gr/);

  await page.goto("./people/5b33ad31-3142-5f14-8cba-5742f5ed22de/");
  await expect(
    page.getByRole("heading", { name: "Arthur F Reinhardt", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Air Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("extract fr");
  await expect(page.locator("body")).not.toContainText(
    "family farm was his employer",
  );

  await page.goto("./people/481bfe0a-c476-5e72-9f85-02a45791f78e/");
  await expect(
    page.getByRole("heading", { name: "Gail F Donnalley", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Ohio Wesleyan University", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Sophomore student");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/f1f25aef-0f06-516c-ac04-4cc449634133/");
  await expect(
    page.getByRole("heading", { name: "John W Brunner", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "college (institution not identified)",
  );
  await expect(page.locator("body")).toContainText(
    "NPS says the Army sent Brunner to study Chinese",
  );
  await expect(page.locator("body")).toContainText(
    "The official history documents the subjects and student status but names no institution.",
  );
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 035 preserves communications, occupation-only, Army-pathway, and self-employment boundaries", async ({
  page,
}) => {
  await page.goto("./people/50c70f7c-dfec-5a4e-9c02-5ca83112c7f3/");
  await expect(
    page.getByRole("heading", { name: "Timothy R Marsh", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Signal Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("United States Army Signal Corps");
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Coyne Radio School", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("civilian Signal Corps radio operator");

  await page.goto("./people/f7687b71-e238-5390-a43c-2552d9e641d6/");
  await expect(
    page.getByRole("heading", { name: "Lawrence W Lowman", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Columbia Broadcasting System",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Columbia Broadcasting System");
  await expect(page.locator("body")).toContainText("vice president in charge of operations");
  await expect(
    page
      .getByRole("link", {
        name: "A Wartime Organization for Unconventional Warfare",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/a-wartime-organization-for-unconventional-warfare.htm",
  );

  await page.goto("./people/2ae252cc-7164-560c-b4b9-d8e91d49e05d/");
  await expect(
    page.getByRole("heading", { name: "John M Balsamo", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "The indexed John M. Balsamo is probably",
  );
  await expect(page.locator("body")).toContainText("Wall Street telegrapher");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).not.toContainText("Western Union");

  await page.goto("./people/6989c183-4a99-52c5-a208-5f7b95f354d7/");
  await expect(
    page.getByRole("heading", { name: "William R Peers", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "probably commissioned service in the United States Army",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .getByRole("link", {
        name: "Intelligence Operations of OSS Detachment 101",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/resources/csi/studies-in-intelligence/archives/vol-4-no-3/intelligence-operations-of-oss-detachment-101/",
  );

  await page.goto("./people/45f220f1-4668-5395-b0e4-f7a4921b254f/");
  await expect(
    page.getByRole("heading", { name: "Nicol Smith", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Nichol Smith");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Self-employed", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Self-employed");
  await expect(page.locator("body")).toContainText("travel writer and author");
  await expect(
    page
      .getByRole("link", {
        name: "War of a Different Kind: OSS and Free Thai Operations in World War II",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/resources/csi/static/OSS-and-Free-Thai.pdf",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 036 preserves communications pathways, unnamed employers, student status, and duplicate uncertainty", async ({
  page,
}) => {
  await page.goto("./people/46e3bd6e-3f4a-59d4-b4e3-52a9aeb1a3a0/");
  await expect(
    page.getByRole("heading", { name: "Lawrence Hollander", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Lawyer", exact: true }),
  ).toBeVisible();
  const civilianEmployerSection = page.locator(
    'section[aria-labelledby="civilian-employer"]',
  );
  await expect(civilianEmployerSection).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    civilianEmployerSection.getByRole("heading", {
      name: "Self-employed",
      exact: true,
    }),
  ).toHaveCount(0);
  await expect(page.locator("body")).toContainText("duplicate-36fe462e632d");
  await expect(
    page
      .getByRole("link", {
        name: "OSS Training in the National Parks and Service Abroad in World War II",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", /ossreborn\.com/);

  await page.goto("./people/dfef5646-c18d-5421-b981-9b3f3b573cf8/");
  await expect(
    page.getByRole("heading", { name: "L L Hollander", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("requires archival review", { exact: true })).toBeVisible();
  await expect(page.locator("body")).toContainText("duplicate-36fe462e632d");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).not.toContainText(
    "Hollander was a lawyer in Chicago immediately before OSS recruitment.",
  );

  await page.goto("./people/00a5d0a9-dc9b-5185-a142-b81a5395cbed/");
  await expect(
    page.getByRole("heading", { name: "Marvin S Flisser", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Brooklyn College", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText(
    "student",
  );

  await page.goto("./people/2d2a4f2a-652a-56f0-94f4-c7f0af234134/");
  await expect(
    page.getByRole("heading", { name: "Willis S Georgia Jr.", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("W. Scudder Georgia Jr.");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Navy", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Hobart and William Smith Colleges",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/96468b14-dc3d-58df-b454-ba38f51d4cfe/");
  await expect(
    page.getByRole("heading", { name: "Robert R Kehoe", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Signal Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "a chemical plant (not named)",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "A Memoir of Jed Team Frederick: An Allied Team with the French Resistance, 1944",
        exact: true,
      })
      .first(),
  ).toHaveAttribute(
    "href",
    "https://www.cia.gov/resources/csi/static/Allied-Team-French-Resistance.pdf",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 037 resolves an Allied pathway while preserving unknown staff backgrounds and the two Herbert rows", async ({
  page,
}) => {
  await page.goto("./people/8c8af948-dd3b-536e-8ba0-988f6cf3d97f/");
  await expect(
    page.getByRole("heading", { name: "Benton E Bickham Jr.", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Benton E. Bickham from Louisiana.");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/fae94705-43d9-5e0b-8567-70e624282604/");
  await expect(
    page.getByRole("heading", { name: "Milton W Griffith", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("Milton Giffith");
  await expect(page.locator("body")).toContainText(
    "whether 'bus driver' described camp duty or prewar employment",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/654e73f7-0645-5c3c-a3c8-529f5f049b7f/");
  await expect(
    page.getByRole("heading", { name: "Louis Lostfogel", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("physician");
  await expect(page.locator("body")).toContainText(
    "pre-OSS practice, employer, and Medical Corps entry chronology",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/638047fa-fbbe-53c7-96d4-77c794b814c2/");
  await expect(
    page.getByRole("heading", { name: "Edmund I Stromholt", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Edward Stromholt");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Norwegian Army", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Veteran of Lofoten Raid", exact: true }).first(),
  ).toHaveAttribute(
    "href",
    "https://princealbertlibrary.ca/padh/1941/October/Oct%2015%2C%201941.pdf",
  );

  await page.goto("./people/5ba837c6-75af-5db2-88f8-648243ded832/");
  await expect(
    page.getByRole("heading", { name: "James Herbert", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("duplicate-f6de91a0d711");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).not.toContainText("United States Navy");

  await page.goto("./people/f91af878-e2dc-5144-80f5-76aae6e74d1b/");
  await expect(
    page.getByRole("heading", { name: "James E Herbert", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("duplicate-f6de91a0d711");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).not.toContainText("United States Navy");

  await page.goto("./organizations/7fe1f71a-6ae9-5437-812e-946a18e377a4/");
  await expect(
    page.getByRole("heading", { name: "Norwegian Army", exact: true }),
  ).toBeVisible();
  await expect(page.getByRole("link", { name: "Edmund I Stromholt" })).toBeVisible();

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 038 distinguishes the Velleman brothers and withholds incomplete Area B identities", async ({
  page,
}) => {
  await page.goto("./people/833cab1f-839d-5766-baf2-4bebff78cada/");
  await expect(
    page.getByRole("heading", { name: "Moritz Velleman", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "a friend's office in Lisbon (organization not named)",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/9a81eee3-9800-507c-b604-ef49aafc3da3/");
  await expect(
    page.getByRole("heading", { name: "Arthur H Velleman", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("OSS Documents Division");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/858dafc5-02bc-5660-a2f3-1027fdc6e0af/");
  await expect(
    page.getByRole("heading", { name: "George A George", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("Georges George");

  for (const [personId, displayName] of [
    ["abee3674-bf36-50b9-bf28-b28905129288", "Howard C Ressler"],
    ["264a44a0-6a03-5451-a2aa-8fd8805c0cf0", "Raymond W Deisher"],
  ] as const) {
    await page.goto(`./people/${personId}/`);
    await expect(page.getByRole("heading", { name: displayName, exact: true })).toBeVisible();
    await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="immediate-affiliation"]'),
    ).toContainText("No reviewed claim currently meets the publication threshold.");
  }

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 039 preserves film, media, military, and occupation-only boundaries", async ({
  page,
}) => {
  await page.goto("./people/b7a8a36f-3f0e-54c1-a0ff-23c840498501/");
  await expect(
    page.getByRole("heading", { name: "Seymour W Schulberg", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Budd Wilson Schulberg");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Naval Reserve", exact: true }),
  ).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "Columbia Pictures",
  );
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText("RKO");
  await expect(page.locator("body")).toContainText("Selznick Pictures");

  await page.goto("./people/63d92813-94cd-578e-942a-c2bdc37a92d8/");
  await expect(
    page.getByRole("heading", { name: "Stuart H Schulberg", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("enlisted marine corps personnel");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Marine Corps");
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "Washington Daily News",
  );

  await page.goto("./people/47b86de9-0ac5-583a-9eae-707215c42f9f/");
  await expect(
    page.getByRole("heading", { name: "Robert R Parrish", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("assistant editor and sound editor");
  await expect(page.locator("body")).toContainText("CSP P");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/92b2503f-4ea7-5399-8362-16f04547fe7d/");
  await expect(page.getByRole("heading", { name: "Sol Kaplan", exact: true })).toBeVisible();
  await expect(page.locator("body")).toContainText("pianist and composer");
  await expect(page.locator("body")).toContainText("Army Signal Corps");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/cb463c42-75dd-58ee-8222-d192e2b2c684/");
  await expect(page.getByRole("heading", { name: "Corey Ford", exact: true })).toBeVisible();
  await expect(page.locator("body")).toContainText("commissioned army officer");
  await expect(page.locator("body")).toContainText("Vanity Fair");
  await expect(page.locator("body")).toContainText("The Saturday Evening Post");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 040 preserves field pathways, occupation boundaries, spelling variants, and separate Mayer rows", async ({
  page,
}) => {
  await page.goto("./people/72ba8a20-2fdf-56be-b228-6dbb45dde0af/");
  await expect(
    page.getByRole("heading", { name: "Roderick G.S. Hall", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "270th Engineer Combat Battalion, United States Army",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Yale University");

  await page.goto("./people/cde21206-1f2d-5241-82c6-7b30c8f95aa0/");
  await expect(
    page.getByRole("heading", { name: "Miles A Copeland", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("professional jazz musician");
  await expect(page.locator("body")).not.toContainText("Benny Goodman");

  await page.goto("./people/6df71376-3491-5715-91af-53606a60d0fd/");
  await expect(
    page.getByRole("heading", { name: "George S Musolin", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("George S. Musulin");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("115th Infantry Regiment");
  await expect(page.locator("body")).toContainText("professional football");

  await page.goto("./people/59f66a94-282a-5f09-b5d1-ea7cdeed4705/");
  await expect(
    page.getByRole("heading", { name: "Frederick Mayer", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("United States Army");
  await expect(page.locator("body")).toContainText("Ford Motor Company");
  await expect(page.locator("body")).toContainText("General Motors");
  await expect(page.locator("body")).toContainText(/duplicate-[a-f0-9]{12}/);

  await page.goto("./people/ed9e4da5-f917-555a-9fda-052036f02574/");
  await expect(
    page.getByRole("heading", { name: "Frederick Mayer", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText(/duplicate-[a-f0-9]{12}/);
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).not.toContainText("Ford Motor Company");
  await expect(page.locator("body")).not.toContainText("General Motors");

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 041 preserves Mediterranean military pathways, veterans affiliations, unnamed occupations, and separate Felsen rows", async ({
  page,
}) => {
  await page.goto("./people/97b90b5c-774c-5d9c-8e52-ca3a4aaeaeec/");
  await expect(
    page.getByRole("heading", { name: "Milton Felsen", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("Abraham Lincoln Brigade");
  await expect(page.locator("body")).toContainText("Recording Secretary");
  await expect(page.locator("body")).toContainText("University of Iowa");
  await expect(page.locator("body")).toContainText(/duplicate-[a-f0-9]{12}/);

  await page.goto("./people/42f68c35-d165-58cf-9ad3-365a27b9cec0/");
  await expect(
    page.getByRole("heading", { name: "Milton Felsen", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("ambiguous", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText(/duplicate-[a-f0-9]{12}/);
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).not.toContainText("University of Iowa");

  await page.goto("./people/4b1fbe1c-9f20-51e5-ae9f-0ef466d3c5b8/");
  await expect(
    page.getByRole("heading", { name: "Irving Goff", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("National Executive Secretary");
  await expect(page.locator("body")).toContainText("adagio dancer");
  await expect(page.locator("body")).toContainText(
    "Unnamed adagio-dance employer or engagement",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/af3332e4-4282-5f1d-8bd2-4dc0f8097b9a/");
  await expect(
    page.getByRole("heading", { name: "Paul H Gale", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "1st Infantry Division, United States Army",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Captain and staff officer");

  await page.goto("./people/7bee69f7-b984-5850-96e1-38253676750e/");
  await expect(
    page.getByRole("heading", { name: "Serge Obolensky", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "New York National Guard", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("St. Regis Hotel");
  await expect(page.locator("body")).toContainText(
    "Unnamed New York banking and real-estate organizations",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 042 preserves academic, broadcast, Allied, naval, and Coast Guard pathways", async ({
  page,
}) => {
  await page.goto("./people/b76c60a1-20b9-547e-a824-20217835f29b/");
  await expect(
    page.getByRole("heading", { name: "Clarence A Berdahl", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("confirmed", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "University of Illinois Urbana-Champaign",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "University of Illinois",
  );

  await page.goto("./people/a583532b-5750-5264-90a4-cbb5ca567a71/");
  await expect(
    page.getByRole("heading", { name: "Hugh M Beville", exact: true }),
  ).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).toContainText(
    "National Broadcasting Company",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/b5c889e5-13d7-5a47-bb1d-f8536f24be22/");
  await expect(
    page.getByRole("heading", { name: "Richard G Arnold-Baker", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("high confidence", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).toContainText("British Army Intelligence Corps");
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");

  await page.goto("./people/1f9ace73-691d-5b96-8349-203d8c7594f4/");
  await expect(
    page.getByRole("heading", { name: "Everett J Athens", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Everette J. Athens");
  await expect(page.locator("body")).toContainText("commissioned naval officer");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/19c983e0-37cb-5b11-8e40-1c4bd39b7103/");
  await expect(
    page.getByRole("heading", { name: "John P Booth", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("commissioned coast guard officer");
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Coast Guard", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Operational Swimmer Group II");

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 043 separates students, earlier employment, and civilian and military ONI service", async ({
  page,
}) => {
  await page.goto("./people/404292b8-801c-58f0-8f74-6fd447da6adf/");
  await expect(
    page.getByRole("heading", { name: "Franklin P Holcomb", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Office of Naval Intelligence", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("Marine Reserve officer at ONI");
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Office of Naval Intelligence", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("Western Hemisphere Division portfolio officer");

  await page.goto("./people/bb6a423b-f07a-55b3-829a-492f44faf418/");
  await expect(
    page.getByRole("heading", { name: "Cora Dubois", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Hunter College", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("Boston Psychopathic Hospital");
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("professional affiliation");

  for (const profile of [
    ["d086f590-f86d-5535-8411-aa60aa252f01", "Carl E Schorske"],
    ["78c03a2c-11e1-5f34-bf53-bc76c5f33817", "Franklin L Ford"],
    ["fb9b02f9-9dfb-5965-8514-fa5b73e3b2c9", "Gordon A Craig"],
    ["813fb48c-b658-5cdf-a265-ce63acb776fc", "James C Luce"],
  ]) {
    await page.goto(`./people/${profile[0]}/`);
    await expect(
      page.getByRole("heading", { name: profile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.locator('section[aria-labelledby="civilian-employer"]'),
    ).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
  }

  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);
});

test("Batch 044 adds supported employers while preserving student, military, and duplicate boundaries", async ({
  page,
}) => {
  await page.goto("./people/2201ee7c-3d64-5672-b519-0aad4625d185/");
  await expect(
    page.getByRole("heading", { name: "Edna W Andrade", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "The Hecht Company", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "The Hecht Company", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "H. Sophie Newcomb Memorial College",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Oral history interview with Edna Andrade, 1987 April 1-29",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", /aaa\.si\.edu/);

  await page.goto("./people/6b90e0e8-f17e-585f-8d21-ecde2a323f1b/");
  await expect(
    page.getByRole("heading", { name: "Conrad F Lagueux", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "University of Rhode Island", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("student");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );

  await page.goto("./people/a2d66764-90d0-5d8d-8102-30c2e0b03ba1/");
  await expect(
    page.getByRole("heading", { name: "Peter M F Sichel", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army Medical Corps",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "H. Sichel Söhne", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "The adjacent Peter M. Sichel row has a different service number and remains separate.",
  );
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);

  await page.goto("./people/1bf7bd5e-a790-51d0-9a46-e6046cab07f2/");
  await expect(
    page.getByRole("heading", { name: "Peter M Sichel", exact: true }),
  ).toBeVisible();
  await expect(page.locator('section[aria-labelledby="civilian-employer"]')).not.toContainText(
    "H. Sichel Söhne",
  );
  await expect(page.getByText("needs identity review", { exact: true })).toBeVisible();

  for (const terminalProfile of [
    ["21a6b6f2-5daa-5569-826e-6d193f387d4a", "Mort S Bobrow", "completed"],
    ["697f0736-ba27-55b6-ae7a-6550dd87aa3c", "Edmund M Burke", "requires archival review"],
    ["f87b5adb-6496-5f61-a50f-2b098032d189", "Jane Burrell", "requires archival review"],
    ["01360217-ccc5-5754-a6d5-9d126bfc08f0", "John H Hemingway", "completed"],
    ["a93ac760-896e-50b9-9746-754d434a1200", "John Magruder", "completed"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText(terminalProfile[2], { exact: true }).first(),
    ).toBeVisible();
  }
});

test("Batch 045 publishes the Allied pathway while routing unresolved cases to archival review", async ({
  page,
}) => {
  await page.goto("./people/b9907bf8-4544-55fe-85a2-e99e9530df73/");
  await expect(
    page.getByRole("heading", { name: "Etienne Ancergues", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("completed", { exact: true }).first()).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "Bureau Central de Renseignements et d'Action",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "French Navy", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page.getByRole("link", {
      name: "Dossier individuel de personnel de ANCERGUES, ETIENNE ANDRÉ GEORGES",
      exact: true,
    }),
  ).toHaveAttribute("href", /servicehistorique\.sga\.defense\.gouv\.fr/);
  await expect(page.locator("body")).toContainText("PDF page 8");
  await expect(page.locator("body")).toContainText("Box 14");
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);

  await page.goto("./people/6ea50bee-54e9-54f1-91ca-b052afc98eda/");
  await expect(
    page.getByRole("heading", { name: "Philip H Chadbourn Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="earlier-affiliations"]'),
  ).toContainText("student");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{7,8}\b/);

  for (const terminalProfile of [
    ["933cbc8e-758f-51de-90fc-afd7d32dba55", "Billie F Akin"],
    ["c407e9fa-3a4c-5cfc-b5ec-d0664ab4133d", "Julia N Barnhart"],
    ["64b5b181-046f-5037-8595-fcf2ea049259", "Jacqueline M Landry"],
    ["329114e6-1dbc-5227-b149-74eb8d7468a1", "Gus Macriyanni"],
    ["1c0bf216-76cf-5444-ba1a-ac373bc715ae", "Carl D Marshall"],
    ["29281682-12ea-5516-9434-4cbc05741a99", "Constantine Papadopoulos"],
    ["26117ce0-c1d9-5bf3-a036-63c23c6b868e", "Lawrence N Stevens"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }
});

test("Batch 046 separates student status, a named employer, an earlier government assignment, and an unnamed employer", async ({
  page,
}) => {
  await page.goto("./people/5a8ea4f7-acc3-5a6f-8bca-c4de1746cc49/");
  await expect(
    page.getByRole("heading", { name: "S D Cater Jr.", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Harvard University", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("student");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page
      .getByRole("link", { name: "A Tribute to Douglass Cater", exact: true })
      .first(),
  ).toHaveAttribute("href", /congress\.gov/);

  await page.goto("./people/0413c4b8-fd84-5f0f-b0b7-b6d0651b66a6/");
  await expect(
    page.getByRole("heading", { name: "Marshall W Houts", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Eastern Air Lines", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Eastern Air Lines", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "Federal Bureau of Investigation",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .getByRole("link", {
        name: "Garrison Investigation of Kennedy Assassination: Marshall Wilson Houts",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", /archives\.gov/);

  await page.goto("./people/5bc32ab9-22d4-5f2f-ada5-25ec431c6181/");
  await expect(
    page.getByRole("heading", { name: "Jane Lester", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("a brokerage in Buffalo");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText("a brokerage in Buffalo");
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();
  await expect(page.locator("body")).not.toContainText("Merrill Lynch");

  for (const terminalProfile of [
    ["be18a8aa-49d3-5600-8d66-eae7b28afb78", "Millard A Copeland"],
    ["86a952a7-c08e-50b9-be06-fbcdb2af8f37", "Jacques Delmas"],
    ["83359650-6c9b-52c4-a60d-22de5ee4885e", "Grier Durant"],
    ["a66a0f48-fda1-5169-84f6-77fa0fd2acfa", "Shigekata Ikeda"],
    ["3c26f2a2-98c8-5a66-9455-ee7e70de8f83", "Jackson E Nordin"],
    ["b2d1f2ba-8862-5b16-b620-3ffbbd9c67d6", "Lucille E Temple"],
    ["2c5e78d0-84b4-5ccb-9604-40ebe233fc06", "Dorothy I Tolley"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(page.locator("body")).not.toContainText("14122318");
  }
});

test("Batch 047 publishes the 99th Infantry pathway and keeps nine names unresolved", async ({
  page,
}) => {
  await page.goto("./people/90851873-c347-5a03-a11f-fac184e844ae/");
  await expect(
    page.getByRole("heading", { name: "Olaf H Aanonsen", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "United States Army, 99th Infantry Battalion (Separate)",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("military assignment");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page.getByRole("link", { name: "10th Mountain Division Name Index", exact: true }).first(),
  ).toHaveAttribute("href", /denverlibrary\.org/);
  await expect(
    page
      .getByRole("link", {
        name: "Among the Firsts: Lieutenant Colonel Gerhard L. Bolland's Unconventional War",
        exact: true,
      })
      .first(),
  ).toHaveAttribute("href", /casematepublishers\.com/);
  await expect(page.locator("body")).toContainText("PVT");
  await expect(page.locator("body")).toContainText("Pfc.");
  await expect(page.locator("body")).toContainText("Cpl");

  for (const terminalProfile of [
    ["f8b9fde8-b58d-5008-a43c-6306f5e79dd8", "Sigurd J Aalbu"],
    ["c0207d96-2125-5ebe-ba47-1e1fba48c9f7", "Helen G Abbenante"],
    ["271bfa40-ff5a-5ab2-8382-bc7e02036d7c", "Charles R Abele"],
    ["ddd74408-e908-507d-b288-cd5cdf380b0e", "Herbert A Abele Jr."],
    ["010bc8e2-5848-5363-ba32-80e5a119c703", "Norman W Abendschein"],
    ["cb7a4651-b52c-5555-baee-f5a76dbd104c", "Michael K Abraham"],
    ["c33df873-b7d9-5f77-aa01-ad5ae4effe3e", "Alexander A Abromaitis"],
    ["24dc19da-1915-55b1-8331-e3f8b54d3c94", "Salvatore H Acampora"],
    ["6042194f-2110-58d4-a4ff-0b7f5e9aa6df", "John Achelis"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    expect(await page.locator("body").innerText()).not.toMatch(/\b\d{6,8}\b/);
  }
});

test("Batch 048 separates immediate military pathways, civilian employers, and earlier affiliations", async ({
  page,
}) => {
  await page.goto("./people/fe42994f-c24f-5ccd-877f-d4f19ce8339f/");
  await expect(
    page.getByRole("heading", { name: "Moses Abrahamovitz", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "National Bureau of Economic Research",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "War Production Board", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("Moses Abramovitz", { exact: false }).first()).toBeVisible();

  await page.goto("./people/d1d45462-bcb9-52d7-9744-8424b27d6480/");
  await expect(
    page.getByRole("heading", { name: "Albert Abrahamson", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "National Refugee Service", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Bowdoin College", exact: true }),
  ).toBeVisible();

  await page.goto("./people/06b73b73-212c-5b38-8b59-eea4cb7ee257/");
  await expect(
    page.getByRole("heading", { name: "Allen Abrams", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Marathon Corporation", exact: true }),
  ).toBeVisible();
  await expect(page.getByText("probable", { exact: true }).first()).toBeVisible();
  await expect(page.getByText("medium", { exact: true }).first()).toBeVisible();

  await page.goto("./people/38c62333-9630-5fe8-a014-401f8f1350a0/");
  await expect(
    page.getByRole("heading", { name: "Vincent A Abrignani", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText(
    "No reviewed claim currently meets the publication threshold.",
  );
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "71st Infantry Regiment, New York National Guard",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.getByText("requires archival review", { exact: true }).first(),
  ).toBeVisible();
  expect(await page.locator("body").innerText()).not.toMatch(/\b\d{6,8}\b/);
});

test("Batch 049 preserves an incomplete printed name and routes ten unresolved common-name cases to Box 1", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["611c81b3-54a7-5c1a-a233-6c6b9581ef5a", "Caf-3 E Aaberg"],
    ["0a389c36-5a98-5e04-9053-d608250a5f56", "Frank Abbote"],
    ["d315b651-4752-55ba-b732-6df89544609e", "John A Abbote"],
    ["3ffe31e6-0f44-5270-b7cf-c688ebc7d1f2", "Delbert H Abbott"],
    ["beec8347-ccd6-50df-87d9-07e07622fb7a", "Floyd H Abbott"],
    ["05ec6d1d-2196-59b9-8a64-4dc15c0e2fcc", "Frederick K Abbott"],
    ["324f3b70-e14c-5391-bc98-cff4f2605d7a", "James E Abbott"],
    ["73e33700-fdae-5574-879a-17b36c017efc", "James F Abbott"],
    ["29abc44d-1bd9-52be-a4ef-d32d07d3841c", "Norman Abbott"],
    ["58e53125-1044-5ff9-937a-b0fc08fe8629", "Robert J Abbott"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(page.locator("body")).toContainText("Box 1");
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/611c81b3-54a7-5c1a-a233-6c6b9581ef5a/");
  await expect(page.locator("body")).toContainText(
    "Aaberg | Caf-3 | E",
  );
  await expect(
    page.getByText("critical", { exact: true }).first(),
  ).toBeVisible();
});

test("Batch 050 routes ten unresolved Abbott-through-Achin records to their indexed archival boxes", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["7088db2a-da18-5a1a-b0fa-058c50d4f7be", "Victor J Abbott", "1"],
    ["9737ab8a-966a-5355-80ce-b0f97a19dcb1", "Robert V Abee", "1"],
    ["89d29fd5-4bac-55f4-9510-622853453a8e", "Arthur A Abel", "1"],
    ["f375230c-f337-5251-8d34-90c5b7dd72f0", "Calvin J Abel", "1"],
    ["ed582713-c52c-5745-8971-a742fafa17db", "John C Abel", "1"],
    ["bba65c39-e1b9-52a3-ad1b-8fa343f42104", "James D Abernathy", "1"],
    ["2b3188cd-9595-57ac-a4e9-ca10cc4293a0", "James K Abney", "1"],
    ["79a323b7-5075-5fb9-b98d-421a24460e07", "John H Achenbach", "2"],
    ["3ca8fbd1-b6d1-5ecd-9cb8-f99c7a42c3d9", "Edward C Acheson", "2"],
    ["c4771919-35b2-5e2c-9d5d-74a8c775cafe", "Paul P Achin", "2"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page
        .locator(".profile-aside")
        .getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }
});

test("Batch 051 preserves ten unresolved Ackelmire-through-Acord profiles and their Box 2 review paths", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["c1462464-a46c-5e24-b15a-b7b483ccabb7", "John G Ackelmire"],
    ["90350c1a-b25a-58d4-b08d-32f7943e4f19", "Mignon S Acker"],
    ["3d951ae3-0734-5e18-97b3-08f369b7db7a", "Walter W Acker"],
    ["cc204427-a08d-543c-9daa-c325e4fb60cd", "Eugene L Ackerman"],
    ["bf12e4f7-95bf-57a5-baad-f680ed96eaa3", "Moris Ackerman"],
    ["c900291b-40fa-5219-adae-3fe78ff6abe9", "Benjamin R Ackerson"],
    ["d7effc9c-3f36-5e02-ad1c-31d469214fe5", "Julia E Ackert"],
    ["16ce1e2c-8ee1-520c-b134-da4ff94b747c", "Barbara H Ackles"],
    ["3d1db48a-f080-5d35-82b1-8d1f8d7fc834", "Lester W Ackley"],
    ["10010105-b843-5b2c-bd94-081b60bbccc2", "Joe F Acord"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page.locator(".profile-aside").getByText("2", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/c1462464-a46c-5e24-b15a-b7b483ccabb7/");
  await expect(page.locator("body")).toContainText(
    "103d Infantry Division officer",
  );
  await expect(page.locator("body")).toContainText(
    "may be treated as pre-OSS without dated linkage",
  );
});

test("Batch 052 preserves grade and rank distinctions while routing ten Acosta-through-Adams profiles to archival review", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["ba724894-06f3-5fdc-b01a-c7e47c34e2bb", "Francis. J Acosta Jr.", "2"],
    ["fe2e1bff-6cb4-5b19-a02f-eb7a6e1d0c58", "Gilmore J Acosta", "2"],
    ["7e9a1132-887b-5fca-8377-31da1a7d4d87", "William L Acree", "2"],
    ["4bce82dd-9a96-519f-9c3b-26a9a4766100", "Doris D Adair", "3"],
    ["cf526949-0343-5e66-a95a-f69b08cb52c4", "Milo J Adair", "3"],
    ["62a14599-d3a6-5556-b032-6266601d4def", "Ben Adam", "3"],
    ["6fd2ad38-7b17-5ae0-9dc2-0e8861389bb0", "Allen G Adams", "3"],
    ["41bc6be2-00a7-5149-9867-0922b5671da4", "Alton G Adams", "3"],
    ["48ad393c-4ef0-55c2-ba41-fc67dc6e549f", "Andrew D Adams", "3"],
    ["9fd314c5-4ada-5e1d-8ea0-a54d8ceffc70", "Arthur F Adams", "3"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page
        .locator(".profile-aside")
        .getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/7e9a1132-887b-5fca-8377-31da1a7d4d87/");
  await expect(page.locator("body")).toContainText(
    "Virginia Tech class-of-1942 lead only if the file supplies corroborating education or hometown evidence",
  );

  await page.goto("./people/6fd2ad38-7b17-5ae0-9dc2-0e8861389bb0/");
  await expect(page.locator("body")).toContainText("commissioned army officer");

  await page.goto("./people/41bc6be2-00a7-5149-9867-0922b5671da4/");
  await expect(page.locator("body")).toContainText("enlisted naval personnel");
});

test("Batch 053 publishes Donald Keith Adams's Duke pathway and preserves nine unresolved Adams profiles", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["acaa96ad-5242-565b-96e8-86f61e2966b7", "Carl Adams Jr."],
    ["382c6ec0-2199-5de7-9dd5-84553b44d400", "Cleva L Adams"],
    ["0fb0ed85-23e8-5e70-88e1-7e145efd917b", "Clyde J Adams"],
    ["8d630b07-b0dd-5474-aa0c-51bc67a57aa3", "Dean D Adams"],
    ["aea9b4ca-9944-502d-a468-92ce0430b349", "Diana M Adams"],
    ["a5c16d60-21b2-5ab2-80de-87bdcca90154", "Dorothea Adams"],
    ["bf16069b-79b0-5703-aae4-07478948d2aa", "Eula Adams"],
    ["5cd66f1a-75bd-5035-af52-2cbfeecc8da8", "George K Adams Jr."],
    ["8d137c21-161a-5c58-945c-9986b5e53331", "Glenn D Adams"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page.locator(".profile-aside").getByText("3", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/c3eeda33-d44b-5791-9cb7-1a7f6953660e/");
  await expect(
    page.getByRole("heading", { name: "Donald K Adams", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "Duke University", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", { name: "Duke University", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Associate Professor of Psychology and Psychiatry",
  );
  await expect(page.locator("body")).toContainText(
    "Black Mountain College 1943 Catalogue",
  );
  await expect(page.locator("body")).toContainText(
    "Adams, Donald Keith",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^(Not printed|••••\d{4})$/);

  await page.goto("./people/8d137c21-161a-5c58-945c-9986b5e53331/");
  await expect(page.locator("body")).toContainText(
    "unlinked 1941 Dallas directory copywriter lead",
  );
});

test("Batch 054 preserves ten common-name Adams cases and their Box 3 or Box 4 archival routes", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["5cdfcf25-c06d-5dc6-a352-07307ebc2bff", "James T Adams", "3"],
    ["93e94718-f1a9-5824-9887-1c0d601d79d7", "John H Adams", "3"],
    ["f1a4c3b6-0d4b-519b-8fb7-4935911e56fd", "Lou A Adams", "3"],
    ["6b352679-550a-5c4d-bd0e-9e4b85f2b2d4", "Paul Adams", "3"],
    ["62a30117-937c-570d-99a4-dce86c19cc30", "Phillip Adams", "3"],
    ["02eb8833-34f7-553c-857e-0fbb16dcd2fa", "Robert E Adams", "4"],
    ["90ec5a1a-02e9-56fc-b9d7-ad8bd8d3a375", "Ruth D Adams", "4"],
    ["cc1f026b-d636-56e9-a487-4f95aee46c92", "Sidney M Adams", "4"],
    ["0d873fa4-51aa-5d01-9262-ca773bfe985e", "Thomas F Adams", "4"],
    ["6b9e3edd-e0ce-5389-8798-4e10375db04e", "Willard A Adams", "4"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page
        .locator(".profile-aside")
        .getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/0d873fa4-51aa-5d01-9262-ca773bfe985e/");
  await expect(page.locator("body")).toContainText(
    "Adams, McEntee & Co. photograph-file lead",
  );

  await page.goto("./people/02eb8833-34f7-553c-857e-0fbb16dcd2fa/");
  await expect(page.locator("body")).toContainText(
    "commissioned army officer",
  );
});

test("Batch 055 publishes Kenneth Addicott's qualified museum-to-Army pathway and preserves nine archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["732a3de7-b0e6-55c8-bb90-cdfa67dd31e4", "William T Adams"],
    ["3b303694-f915-5ce2-a751-deb3bd1e8141", "William C Adams"],
    ["84dab33f-b0ca-5653-ad78-0bff0a4761db", "William H Adams"],
    ["90f35664-6ee8-5d77-b53c-f021b8af6bd8", "William M Adams"],
    ["fa18617b-bcc0-5bfc-bb68-32c32a3d1c31", "William N Adams"],
    ["0578df03-5bbb-50e8-b779-d38f3ac1b463", "William S Adams Jr."],
    ["9302c6da-895c-592a-bdf5-f9e6b1a15119", "Pinckney J Adamson"],
    ["58350381-05c5-53d1-837c-fe5110f2e858", "Salvatore S Adelfio"],
    ["c0440f07-59ab-552a-b50b-66d74c0e2c3d", "Reginald Adeling"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page.locator(".profile-aside").getByText("4", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/35c4500e-4d99-5938-8cb2-e144a144161d/");
  await expect(
    page.getByRole("heading", { name: "Kenneth K Addicott", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("verified employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "American Museum of Natural History",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "transfer sequence remains unconfirmed",
  );
  await expect(page.locator("body")).toContainText(
    "The Development of Pedagogical Authority Through Teacher Programs",
  );
  await expect(page.locator("body")).toContainText(
    "CIA's Clandestine Services: Histories of Civil Air Transport",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^(Not printed|••••\d{4})$/);
});

test("Batch 056 publishes Burton Adkinson's qualified university role, corrects Sonia Adelson's normalized name, and preserves nine archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["7a02160d-6ed8-55ed-a161-b61b5d12a038", "George W Adelman"],
    ["4210a353-de81-5116-aa10-f524e35f3289", "Ivan J Adels"],
    ["190ca40e-d78b-52dc-94fe-09e8d4b0d525", "Ruth M Adels"],
    ["4e7dd907-82f6-55be-aa57-fc8f83c4b856", "Sonia Adelson"],
    ["edf8ab5d-3c41-56ef-a28b-3e1259e0f367", "Dean J Adinamis"],
    ["9094f471-2cd5-563f-8616-94ad5d74e86c", "John C Adison"],
    ["808803cf-80aa-525b-9c82-f9729760a582", "Glenn J Adkins"],
    ["12715fea-b544-5d75-8d5f-ed81e21a7dd4", "Robert S Adkins"],
    ["9242df8a-bd16-57ab-90be-9b5dc025ebbf", "Carmen G Adkisson"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
    );
    await expect(
      page.locator(".profile-aside").getByText("4", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/4e7dd907-82f6-55be-aa57-fc8f83c4b856/");
  await expect(
    page.getByRole("heading", { name: "Sonia Adelson", exact: true }),
  ).toBeVisible();
  await expect(page.locator(".profile-aside")).toContainText(
    "civilian professional or administrative grade",
  );
  await expect(page.locator(".index-record").first()).toContainText(
    "Adelson | Sonia | P-2",
  );

  await page.goto("./people/a0aa49cd-76c2-53dd-ac35-1165231cd008/");
  await expect(
    page.getByRole("heading", { name: "Burton W Adkinson", exact: true }),
  ).toBeVisible();
  await expect(
    page
      .getByText("documented prewar employer found", { exact: true })
      .first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="civilian-employer"]')
      .getByRole("heading", {
        name: "University of Washington",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(page.locator("body")).toContainText(
    "last documented civilian employer found before his wartime OSS service",
  );
  await expect(page.locator("body")).toContainText(
    "University of Washington General Catalog, 1942-1943",
  );
  await expect(page.locator("body")).toContainText(
    "Assistant Chief of the Map Intelligence Section",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^(Not printed|••••\d{4})$/);

  await page.goto("./people/edf8ab5d-3c41-56ef-a28b-3e1259e0f367/");
  await expect(page.locator("body")).toContainText(
    "whether the Fitzsimons T/5 is Dean J. Adinamis",
  );
  await expect(page.locator("body")).not.toContainText(
    "T/5 Dean Adinamis",
  );
});

test("Batch 057 distinguishes student and religious affiliations from employers and preserves eight archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["01de5ef4-3268-54f6-a94a-2e9bd7b27656", "F P Adler", "4"],
    ["1a769a5a-6e0f-5bef-9f4f-b078efd23f9f", "Maxine Adler", "4"],
    ["a2ba8347-2109-5194-9137-5154419b1f37", "Louis D Adlon", "4"],
    ["30c9db1e-d89a-5917-bfd6-8d9d94be411a", "Alex C Adrian", "4"],
    ["ed266912-fe51-5dd7-b939-f2174a5debdc", "Leonard Adrian", "4"],
    ["ba040b97-398e-5ce2-b5df-36e4dec1c596", "Demetra Aeton", "5"],
    ["a5f8c0c0-32e0-50b1-abf3-1c780d395b08", "Percy C Afferton", "5"],
    ["533cb41c-e235-5aa3-85f6-9ef0bc73f908", "Nehmet Aga-Ogla", "5"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page
        .locator(".profile-aside")
        .getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/ae2ce160-ad06-54e0-9fa5-31809c7c80ea/");
  await expect(
    page.getByRole("heading", { name: "Ernest H Adolph", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("completed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "Cornell University", exact: true }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText(
    "this is a student affiliation, not an employer finding",
  );
  await expect(page.locator("body")).toContainText(
    "served in the OSS (MO) from 1943 until 1945",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^(Not printed|••••\d{4})$/);

  await page.goto("./people/d9b0c480-badf-50cc-9ba2-24f4d4b6e037/");
  await expect(
    page.getByRole("heading", { name: "Merrill S Ady", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("completed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", {
        name: "American Presbyterian Mission",
        exact: true,
      }),
  ).toBeVisible();
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText(
    "field agent in Secret Intelligence with U.S. Army Office of Strategic Services in China",
  );
  await expect(page.locator("body")).toContainText(
    "Merrill S. Ady, of the American Presbyterian Mission",
  );
});

test("Batch 058 publishes Aglione's Army pathway, confirms two roster identities, and preserves seven review cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["6002e291-755d-5b83-879b-2e05c1439854", "Frederick B Agee Jr."],
    ["303d483f-6fd7-5f76-9327-3d12020eaa33", "Susie W Agee"],
    ["fc892342-811c-5b16-8bcc-27c6ebf7bd08", "Athanas Aggo"],
    ["cbe852be-9d30-5eb2-b68f-58e3e3940c2c", "Cornelius R Agnew"],
    ["a42c8e38-18b0-5d29-bea7-f2c54255eac4", "Joseph A Agrillo"],
    ["e585e775-2188-5ece-b92c-123e15445a2d", "Antonio Agugliaro"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText("5", { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/931925ce-767a-5905-957c-7b1c32ba8d3f/");
  await expect(
    page.getByRole("heading", { name: "Albert H Agert", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("needs identity review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Albert Hippolyte Agert is a plausible candidate",
  );
  await expect(page.locator("body")).not.toContainText(
    "Special Operations Executive personnel file: Albert",
  );

  await page.goto("./people/9d0ea528-05c0-505f-a982-b4cb416e3abf/");
  await expect(
    page.getByRole("heading", { name: "Evangelo Ageloras", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("Evangelo Agelopas");
  await expect(page.locator("body")).toContainText(
    "confirms identity and OSS service but not a pre-OSS affiliation",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);

  await page.goto("./people/e96a1c0e-6b4f-5736-b1e0-42179955dc2f/");
  await expect(
    page.getByRole("heading", { name: "Arthur J Agoritsas", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Technical Grade 5 Arthur J. Agoritsas",
  );
  await expect(page.locator("body")).toContainText(
    "sources print different enlisted-grade labels",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);

  await page.goto("./people/35afb022-93c2-532d-a08b-60ac54c81b9f/");
  await expect(
    page.getByRole("heading", { name: "Peter M Aglione", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("completed", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="immediate-affiliation"]')
      .getByRole("heading", { name: "United States Army", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "best-supported immediate pre-OSS affiliation was United States Army service",
  );
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(page.locator("body")).toContainText(
    "Entered the Army January 1941. Was recruited by Captain Bonfiglio and Lieutenant Daddario",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^••••\d{4}$/);
});

test("Batch 059 publishes Ahlstrom's qualified prewar faculty role and preserves nine archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["c6d95182-4820-5a22-b650-b6e9c3be2f25", "Pedgro J Aguirre"],
    ["47abd0de-8fa9-5285-8147-d02cb1c9578c", "German Agustini"],
    ["5d9d660a-6d35-554e-b01f-81f002f029a4", "Cornelius J Ahearn"],
    ["f7bdeada-d129-517f-b69d-dea4d5d9dbeb", "David Ahearn"],
    ["dca8ac2c-3fb0-5b2d-a36d-9f3904e8c5ae", "Margaret Ahearn"],
    ["153bb624-79ed-56ec-8b86-838f4059c4f8", "Leonard Ahern"],
    ["53bbd21a-a7ec-53f6-bb7f-25b78ee59160", "Philston Ahn"],
    ["d71ea9e1-88a5-58a6-b9da-4d9f73fa0cf9", "Kenneth E Ahola"],
    ["9424dece-0e80-5f8c-9db8-f18512bdd3bd", "Amedeo M Aiello"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page.locator(".profile-aside").getByText(/^[56]$/, { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/dc625dce-f632-5092-9329-bee6db98b005/");
  await expect(
    page.getByRole("heading", { name: "Alvida Ahlstrom", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("probable", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("documented prewar employer found", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", {
        name: "La Crosse State Teachers College",
        exact: true,
      }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("French faculty");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page.getByRole("link", { name: "La Crosse", exact: true }).first(),
  ).toHaveAttribute(
    "href",
    "https://www.e-yearbook.com/yearbooks/University_Wisconsin_La_Crosse_La_Crosse_Yearbook/1940/Page_28.html",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText(/^(Not printed|••••\d{4})$/);

  await page.goto(
    "./organizations/de9fc8b5-5d0a-5ca5-b39b-392da9358c3d/",
  );
  await expect(
    page.getByRole("heading", {
      name: "La Crosse State Teachers College",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Alvida Ahlstrom", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "other documented pre-OSS affiliation",
  );
  await expect(
    page.getByText("medium", { exact: true }).first(),
  ).toBeVisible();
});

test("Batch 060 preserves a transposed-name duplicate, publishes Aiton's earlier university employment, and routes eight archival cases", async ({
  page,
}) => {
  for (const terminalProfile of [
    ["7cf7b3d0-1260-59c3-8543-1a39da5f4b43", "Salvatore Aiello", "6"],
    ["b9883af7-7ab7-5b23-b8c8-2dc9cf3ac401", "James A Aiken", "6"],
    ["0e575e76-5d33-5e19-af3f-1526fa8a5db0", "Estella L Aikman", "6"],
    ["766c0cd6-23f0-512e-a363-807eb7935812", "Alice Aird", "6"],
    ["382fb70e-490e-5777-b264-f3dac5764df7", "Gilbert S Aitken", "6"],
    ["69bee485-9cbc-5d03-a7a2-27bae3f5ab05", "Robert T Aitken", "6"],
    ["d23a902b-bb0c-561c-a783-e5f47f3b03ac", "Belle B Aizen", "6"],
    ["86d62ffb-cfba-560b-a832-82745d911dfd", "Christian Akeo Jr.", "7"],
  ]) {
    await page.goto(`./people/${terminalProfile[0]}/`);
    await expect(
      page.getByRole("heading", { name: terminalProfile[1], exact: true }),
    ).toBeVisible();
    await expect(
      page.getByText("requires archival review", { exact: true }).first(),
    ).toBeVisible();
    await expect(page.locator("body")).toContainText(
      "No reliable pre-OSS employer has yet been identified",
    );
    await expect(
      page
        .locator(".profile-aside")
        .getByText(terminalProfile[2], { exact: true }),
    ).toBeVisible();
    await expect(
      page.locator(".index-record").first().locator("dd").nth(2),
    ).toHaveText(/^(Not printed|••••\d{4})$/);
  }

  await page.goto("./people/00a094cd-16e2-50fa-9e0e-784a2a7af6e6/");
  await expect(
    page.getByRole("heading", { name: "Blogg Ainsworth", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("probable", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page.getByText("needs identity review", { exact: true }).first(),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("duplicate-02ab1d7dcdda");
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(
    page.getByRole("link", {
      name: "Instructing for Dangerous Missions",
      exact: true,
    }),
  ).toHaveAttribute(
    "href",
    "https://www.nps.gov/articles/instructing-for-dangerous-missions.htm",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText("Not printed");

  await page.goto("./people/c4b9c664-cdcf-56e7-8bd1-eaa7d5c13a4a/");
  await expect(
    page.getByRole("heading", { name: "Ainsworth Blogg", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText("duplicate-02ab1d7dcdda");

  await page.goto("./people/05072153-d5a0-55b6-bac5-1137fdd9ed7b/");
  await expect(
    page.getByRole("heading", { name: "Arthur S Aiton", exact: true }),
  ).toBeVisible();
  await expect(
    page.getByText("high confidence", { exact: true }).first(),
  ).toBeVisible();
  await expect(
    page
      .getByText("documented prewar employer found", { exact: true })
      .first(),
  ).toBeVisible();
  await expect(
    page
      .locator('section[aria-labelledby="earlier-affiliations"]')
      .getByRole("heading", { name: "University of Michigan", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "Instructor, later professor of Latin American history",
  );
  await expect(
    page.locator('section[aria-labelledby="immediate-affiliation"]'),
  ).toContainText("No reviewed claim currently meets the publication threshold.");
  await expect(
    page.locator('section[aria-labelledby="civilian-employer"]'),
  ).toContainText(
    "No reliable pre-OSS employer has yet been identified in the accessible sources reviewed.",
  );
  await expect(
    page.getByRole("link", {
      name: "Arthur Scott Aiton papers, 1922-1959",
      exact: true,
    }).first(),
  ).toHaveAttribute(
    "href",
    "https://findingaids.lib.umich.edu/catalog/umich-bhl-85852",
  );
  await expect(
    page.locator(".index-record").first().locator("dd").nth(1),
  ).toHaveText("NR");
  await expect(
    page.locator(".index-record").first().locator("dd").nth(2),
  ).toHaveText("Not printed");

  await page.goto(
    "./organizations/4ee8a858-3cd1-5a2d-94a7-0d3c7a3fdb3a/",
  );
  await expect(
    page.getByRole("heading", {
      name: "University of Michigan",
      exact: true,
    }),
  ).toBeVisible();
  await expect(
    page.getByRole("link", { name: "Arthur S Aiton", exact: true }),
  ).toBeVisible();
  await expect(page.locator("body")).toContainText(
    "other documented pre-OSS affiliation",
  );
  await expect(
    page.getByText("high", { exact: true }).first(),
  ).toBeVisible();
});
