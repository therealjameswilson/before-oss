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
    page.getByText(/53 entities currently have confirmed\/high published employment or self-employment evidence/i),
  ).toBeVisible();
  await expect(page.getByText(/broader affiliation measure currently covers 84 entities/i)).toBeVisible();
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
      earlier: "Pennsylvania Academy of the Fine Arts",
      source: "Edna Andrade: From the OSS to Op Art",
    },
    {
      id: "f87b5adb-6496-5f61-a50f-2b098032d189",
      name: "Jane Burrell",
      earlier: "Smith College",
      secondEarlier: "Columbia University",
      source:
        "The Mystery of Jane Wallis Burrell: The First CIA Officer To Die in the Agency's Service",
    },
    {
      id: "697f0736-ba27-55b6-ae7a-6550dd87aa3c",
      name: "Edmund M Burke",
      earlier: "University of Pennsylvania",
      source: "Hollywood and the Office of Strategic Services",
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
      .getByText("No reviewed claim currently meets the publication threshold.", {
        exact: true,
      }),
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
      .getByText("No reviewed claim currently meets the publication threshold.", {
        exact: true,
      }),
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
        "No reviewed claim currently meets the publication threshold.",
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
        "No reviewed claim currently meets the publication threshold.",
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
        "No reviewed claim currently meets the publication threshold.",
        { exact: true },
      ),
  ).toBeVisible();
});
