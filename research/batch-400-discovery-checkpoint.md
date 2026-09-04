# Batch 400 discovery checkpoint

Prepared 2026-09-04 UTC while Batch 399 release checks ran. This is a working
research checkpoint, excluded from site exports, not itself published fact. The initial notes below
describe discovery before adjudication. A validated Batch 400 bundle was
subsequently imported twice to verify idempotence: eleven sources, one
qualified affiliation, seven claims, twenty claim-source links, ten person
updates, and ten durable attempts. The resulting local attempted-person
count is 3,783; the deployed Batch 399 count remains 3,773 until a new release.

## Source cohort

The NARA index pages 77 and 78 were rendered at 150 dpi and visually inspected.
Page 77 has 46 personnel rows. The cohort crosses the page boundary: page 77,
rows 38-46, then page 78, row 1. All ten are in Box 119, location
230/86/28/05. Printed notes are blank; only Alston H. Chase has a printed rank,
Capt. Preserve the printed Charpenter, Charter, Chartres, and other spellings.
Private identifiers remain solely in the private source database.

| Person ID | Indexed name | Page / row |
|---|---|---|
| dad12733-0ef3-501c-a6fb-e5f88acfaa9f | Rene L Charpenter | 77 / 38 |
| 3dd2eb07-c525-56fe-b3b4-edd891978307 | James C Charr | 77 / 39 |
| c62f5f51-07a8-5941-985b-d03a485e70b8 | Ira E Chart | 77 / 40 |
| c85518d7-32b2-5b90-bec9-a1182bf723f5 | Louis Y Charter | 77 / 41 |
| 3214e809-f1bc-5763-8822-bf7431ef40d9 | Chester R Chartrand | 77 / 42 |
| 4ebcd2f6-ad23-5944-96f1-b0394969593b | Mary I Chartres | 77 / 43 |
| b6b84469-bc14-561d-b7fe-7b679acdda5c | Alston H Chase | 77 / 44 |
| b855a928-8fcf-5a0a-a905-5d22e0017f98 | Caroline C Chase | 77 / 45 |
| 5b3fb33e-05e2-55c9-a27e-57e06aa4fb22 | Harrison V Chase | 77 / 46 |
| 5a73b6fc-3899-5487-823e-1b8465ff85d4 | Herbert E Chase | 78 / 1 |

## Searches actually run

The 2026-09-04 continuation checked CIA Reading Room-indexed discovery for
Rene L Charpenter, Rene Charpentier, James Charr, Ira Chart, Louis Chartier,
Chester Chartrand, Mary Chartres, Alston Chase, Caroline Chase, Harrison Chase,
and Herbert Chase. It found a James Charr entry in a postwar college-list
document (CIA-RDP80B01676R003800080034-8; not accepted as employment evidence)
and a Chester Chartrand lead (CIA-RDP13X00001R000100140006-3). Opening the
latter redirected to the Reading Room home page; its search excerpt is not
an inspected final source. Remaining searches supplied no accepted external
identity or employer.

LoC-domain exact-name discovery was also run for Harrison V. Chase, Ira E.
Chart, Mary I. Chartres, and Caroline C. Chase. The returned early nineteenth-
century Judge Chase newspaper and unrelated name-list results were rejected
for date/name/context mismatch. They are not evidence about these personnel.

Additional employment/institutional queries: `Rene Charpenter occupation
obituary`; `Rene L Charpentier biography 1940`; `Herbert E Chase occupation
obituary OSS`; `Louis Y Chartier obituary attorney`; `Rene Charpenter archive`;
`Ira E. Chart employment`; `Mary I. Chartres occupation`; `Caroline C. Chase
university 1940`; `Alston Hurd Chase intelligence`; `Alston Chase Office of
Strategic Services`; `Alston H Chase Andover 1944`; `Alston H. Chase OSS
captain`. Preserve the explicit negative findings and unrelated/name-only
rejections; do not substitute a younger writer's biography for Alston H. Chase.

Exact quoted full indexed name plus quoted OSS for all ten people. Additional
queries: Alston Hurd Chase + OSS; Chester Chartrand + Office of Strategic
Services; Alston Hurd Chase + Strategic; Alston + Chase + OSS + Andover;
Louis Charter + OSS; Rene Charpenter alone; Alston Chase + captain +
intelligence; Chester R Chartrand + before war / 1939; Louis Y Charter +
biography; Rene L Charpentier + OSS; site:pa59ers.com/library/Chase + O.S.S. /
Intelligence; site:cia.gov/readingroom + Alston + Chase. No authenticated
Catalog API was called. These are discovery searches, not the minimum
completed protocol.

Further discovery queries: Chartrand, Chester + Register / 1942; Chase, Alston
+ 1943 + Army; Charr, James + occupation; Chester + Chartrand + missionary
+ OSS; Chester Ray Chartrand + 1941; Alston H Chase + Captain (excluding index
mirrors). Preserve these variants as search aliases, not source corrections.

## Reviewed leads and limitations

Additional completed discovery searches (no accepted identity from a result
snippet): `Ira E Chart occupation obituary`; `Mary I Chartres obituary`;
`Caroline C Chase obituary`; `Harrison V Chase biography`; `Harrison V Chase
professor OSS`; `Harrison Chase Office of Strategic Services`; `Caroline Chase
Office of Strategic Services`; `Ira Chart OSS`; `Harrison V. Chase calendar
professor`; `Ira E. Chart obituary Torrance`; `Louis Y. Chartier lawyer`;
`Caroline C. Chase obituary`; `Chester Ray Chartrand missionary 1939 1941`;
`Harrison V Chase OSS`; `Alston Hurd Chase OSS`.

AncientFaces/cemetery namesakes remain discovery-only and unaccepted. Modern
people-finder results were rejected without retaining their personal details.
Hagley's January 11, 2021 article at
https://www.hagley.org/research/news/hagley-vault/second-monday-january-national-clean-your
was opened and reviewed: it names a Harrison V. Chase as a cofounder of a
calendar publication in 1958 but establishes neither OSS service nor prewar
employment. No profile claim is accepted from this postwar, name-only lead.

### James C Charr

- Independence Hall of Korea, Dictionary of Korean Independence Activists,
  entry Cha Jin-ju, author Kim Do-hun:
  https://search.i815.or.kr/dictionary/detail.do?id=13936&index=1&reSearchWord=&searchType=all&searchWord=
  Opened and reviewed. Explicitly names James C. Charr, describes New York
  Korean National Association offices in 1940-1943, and later OSS/NAPKO
  service. Treat organizational office as an affiliation unless paid
  employment is independently established. The text has a malformed Army
  entry date, so do not silently normalize it.
- Korean Ministry of Patriots and Veterans Affairs, award record 955042:
  https://e-gonghun.mpva.go.kr/user/ContribuReportDetail.do?goTocode=20001&mngNo=955042&pageTitle=Report
  Opened and reviewed. The summary says January 1944 while the narrative from
  the 2014 award-history volume says November 1944. Compare the underlying
  Army record and preserve any unresolved chronology conflict. The two Korean
  entries may depend on the same historical material; do not count them as
  automatically independent corroboration.

### Chester R Chartrand

- The Baptist Herald, December 1, 1944, vol. 22 no. 23, editorial "God's
  Wonders and the Printed Page", printed page 3 / physical PDF page 2:
  https://www.nabarchives.org/wp-content/uploads/2019/05/BapHer1944Dec1.pdf
  The full extracted page text was reviewed on 2026-09-04. It identifies
  Captain Chester Chartrand as a former Burma missionary then serving in
  United States Army Intelligence, and recounts a letter from Myitkyina.
  This links the missionary occupation to the captain/Burma context in the
  official wartime history. It does not name the employing missionary body,
  date OSS entry, or establish the last civilian employer. Two page-image
  requests failed at the browsing tool; visual verification remains pending.
  A direct public retrieval returned HTTP 406, also recorded as an access
  limitation. No full copyrighted PDF or page image was saved locally.
  The source credits an earlier item in Missions magazine. Do not count the
  editorial and that underlying item as independent evidence if both are used.

- Troy J. Sacquety, A Special Forces Model: Detachment 101 in the Myitkyina
  Campaign, Part I, USASOC History Office, Veritas 4(1):
  https://arsof-history.org/articles/v4n1_myitkyina_part_1_page_1.html
  Opened and reviewed. Full name and captain rank appear in the account of
  the OSS liaison to Northern Combat Area Command in early 1944 (note 20).
  This is wartime identity/role context, not pre-OSS employment or evidence
  that NCAC was an immediate predecessor. Inspect cited personnel material
  and a rank/identifier-backed record before accepting the identity.
- State Department, FRUS 1952-1954, volume XI, part 1, document 2, note 2:
  https://history.state.gov/historicaldocuments/frus1952-54v11p1/d2
  Opened and reviewed. A same-name public affairs officer served in Pretoria
  in 1952. This can guide a search of the official biographic register, but
  does not prove prewar employment or identity by itself.
- American Baptist Historical Society, International Ministries - Missionary
  Correspondence, Group 1-Series 1, Chartrand, Chester Ray (1901- ), 1926-1946:
  https://libraries.mercer.edu/archivesspace/repositories/2/archival_objects/4702
  The browser fetch failed but a direct public GET returned HTTP 200. The
  biographical note was inspected in memory: missionary in Burma circa
  1926-1939; University of Denver B.A. 1925. Two digitized correspondence
  groups cover 1926-1929 and 1930-1939. Do not substitute the collection's
  modern corporate creator for the historical employing organization.
- The Baptist Herald, December 1, 1944, archived by the North American Baptist
  Conference: https://www.nabarchives.org/wp-content/uploads/2019/05/BapHer1944Dec1.pdf
  Discovery result identifies Captain Chester Chartrand as a former Burma
  missionary then in Army Intelligence. PDF context/image not yet reviewed;
  locate the relevant page and investigate the named original Missions item.

### Alston H Chase

- Rutgers Database of Classical Scholars, Alston Hurd Chase:
  https://dbcs.rutgers.edu/all-scholars/chase-alston-hurd
  Opened and reviewed. The candidate taught at Harvard and Phillips Academy
  before Army Air Corps service. It does not explicitly establish an OSS
  relationship. Do not attach this biography based on name similarity alone.
- The candidate memoir Time Remembered has an online alumni transcription:
  https://www.pa59ers.com/library/Chase/time2-1n2.html
  Discovery only so far; follow the contents to the war chapters and verify
  captain/OSS identity and the chronology before any publication.
- A Dumbarton Oaks biography was discovered through an authority-record lead:
  https://www.doaks.org/library-archives/garden-archives/biographies/alston-h-chase
  The open attempt returned an internal access error. Not reviewed.
- Keep the classicist separate from the later writer Alston Chase who appears
  in searches about Harvard and the Unabomber.
- Leonard F. James, Phillips Academy, Andover in World War II (1948), war
  service records, was discovered at
  https://www.pa59ers.com/library/James/ww2b.html . The current open failed;
  locate an accessible institutional copy. Several memoir open attempts also
  failed, so do not treat the search snippets as inspected autobiography.

### Remaining seven people

Exact-name OSS searches produced no accepted external identity or employer.
AncientFaces' Mary I. Chartres result is discovery-only genealogy without an
OSS link; it cannot establish identity or employment. Modern corporate,
utility, patent, and unrelated literary results for other names were not
accepted. Continue the official-source, variant, employment-focused,
institutional/newspaper, and archival-source protocol before assigning any
terminal research status. A failed exact-name search is not evidence of no
previous employment.

## Next work

### Army bulk comparison completed, chronology adjudication still pending

The official code-list images were rendered at 130 dpi and fully inspected
on 2026-09-04: physical page 171 (printed X-XI) confirms code 0-22, Lawyers
and judges; physical page 172 (printed XII-XIII) confirms code 2-27, Waiters
and waitresses, except private family. These are broad occupations, not named
employers. Basic documentation physical pages 44-45 confirm the 1-based
columns for name, date (DD/MM/YY), grade, and civilian occupation. They also
warn that a minority of source cards use an E.R.C. statistical layout and
that the exact coding manual used on a card is not always ascertainable.

On 2026-09-04 UTC, read the official ASNEF.FIN.DAT transiently from the
recoverable Batch 399 download, using the documented fixed-width layout.
All 9,200,232 records were examined. No raw row or full identifier was retained
in this checkpoint. The two eight-digit eligible source identifiers yielded:

- James C. Charr: exact name and identifier; Army-entry field 1945-01-12;
  PVT; civilian-occupation value 227. The official code list (physical page
  172, printed XII) text identifies waiters and waitresses, except private
  family. Its source image still needs a Batch 400 visual check. The entry
  date is later than the Korean histories' 1944 OSS/recruitment chronology;
  do not promote this to a settled pre-OSS occupation without resolving the
  temporal relationship. It may be a later military-processing event rather
  than proof that the institutional history is wrong.
- Louis Y. Charter: same private identifier but returned name Louis Y.
  Chartier; Army-entry field 1942-10-05; PVT; occupation value 022. The official
  code list (physical page 171, printed X) text identifies lawyers and judges.
  Source-image and residual-field review remain required. Preserve Charter
  as printed and treat Chartier as a source-supported variant only after
  identity review; do not infer a law firm or self-employment from the code.

Exact alphabetic name comparison yielded one candidate each for James C.
Charr and Herbert E. Chase, and zero for the other eight indexed spellings.
The Herbert E. Chase row is name-only and has not been accepted. Six-digit
officer identifiers were not forced into the eight-digit enlisted file.
Missing matches are not evidence that a person did not serve.

A second complete transient comparison of all 9,200,232 records on
2026-09-04 reconfirmed those two identifier-backed entries. Only selected
non-sensitive fields were inspected; no full raw row or identifier was saved.
Charr's birth-year code is 05, whereas the Korean dictionary gives 1904.
This additional discrepancy must be preserved alongside the 1944/1945 entry
timing problem; the Korean institutional biography must not silently overwrite
the Army record. Charter/Chartier's branch letters are unfamiliar and are not
normalized or published from resemblance to a known branch. The accepted
Army-entry occupation codes and private-grade fields do not establish an
OSS-entry chronology or named employer for either person.

### Remaining work

1. Complete official/source-specific checks and meaningful variants for all
   ten, including direct source-image and residual-field review of the two
   identifier-backed Army results and disambiguation of Herbert E. Chase.
2. Read and assess the candidate sources, establish identity evidence, and
   separate civilian employment, organizational membership, student status,
   and military assignment.
3. Import a validated reviewed-evidence bundle only after adjudication; then
   regenerate coverage, review queues, public assets, and release tests.

### Final continuation notes

Further discovery queries (`Chartrand Biographic Register`, `Alston Hurd
Chase war Andover` excluding the younger author, and `Chester Chartrand
missionary Burma American Baptist`) repeated the existing archival/memoir
leads but supplied no new accepted identifier linkage. Do not continue
postwar biography reconstruction without a concrete identity-disambiguation
purpose. The strongest unresolved next steps are:

- Rene L. Charpenter, Ira E. Chart, Mary I. Chartres, Caroline C. Chase,
  Harrison V. Chase, and Herbert E. Chase: adjudicate the documented negative
  and name-only findings and record an individual Box 119 archival question.
- Louis Y. Charter: exact identifier plus the compatible Chartier name form
  supports an Army-entry identity/occupation assessment. Keep the original
  spelling; do not infer a lawyer's employing firm or an immediate OSS role.
- James C. Charr: retain the identifier-backed Army identity and both chronology
  and birth-year discrepancies before assigning the Korean institutional
  biography. Officeholding is not proof of paid employment. Publication of a
  qualified affiliation requires an explicit candidate-to-person assessment.
- Chester R. Chartrand: the official OSS history, contemporary Baptist item,
  and missionary finding aid form a promising chain, but direct officer/file
  linkage and the original-page visual check remain open. Do not use the
  modern collection creator as the historical employing organization.
- Alston H. Chase: the classics/Andover biography remains a candidate. A full
  name and a general wartime Air Corps description are not sufficient to
  attach its employers to this index entry without further corroboration.

No reviewed-evidence bundle has been imported for Batch 400, and none of these
ten people is included in the release's 3,773 attempted-person coverage yet.

### Additional review at 2026-09-04 01:59 UTC

Reopened the NARA personnel overview, the complete relevant USASOC Chartrand
passage, Rutgers Chase professional-experience section, both Korean Charr
entries, and the Baptist Herald editorial text. The earlier image-access
limitation remains: the editorial has been textually reviewed, not visually
certified. No Catalog API request was made.

Queries actually run in this continuation: `Alston Hurd Chase OSS`; `Alston
H. Chase captain 1944`; `Chester R. Chartrand personnel`; `James C. Charr 1945
OSS`; `James Chen Charr waiter`; `James Chen Charr OSS employment`.

Two additional Charr sources were opened and inspected, not accepted as an
identity bridge based on a relative:

- Chang, Jeong Youn, "Mary Sungduk Youn's Life and Musical Activities based
  on Primary Sources and Historical Records", Musicology 40 (2021), printed
  page 27 / physical PDF page 21, footnote 42:
  https://journal.kci.go.kr/musicology/archive/articlePdf?artiId=ART002738227
  The footnote supplies James Chen Charr and birth year 1905, contrasting with
  the Korean dictionary's 1904. It also has different college attendance
  dates. This is a scholarly disagreement to preserve, not authority to
  silently fix either record or transfer the relative's employment. Its page
  image has not been inspected; no complete PDF was saved.
- U.S. Senate, Report 483, 80th Congress, 1st session, July 11, 1947, "Mary
  Sungduk Charr", pages 1-2:
  https://www.govinfo.gov/content/pkg/SERIALSET-11116_00_00-114-0483-0000/pdf/SERIALSET-11116_00_00-114-0483-0000.pdf
  The report names James Chen Charr as a World War II veteran, but its
  postal employment evidence is explicitly current in 1947. Reject that
  occupation as pre-OSS evidence. Do not retain the unrelated immigration,
  family, or personal details, or use a relative as the principal match.

The expanded searches still supplied no private-identifier bridge for the
Chase classicist or Chartrand missionary candidate. The Bible-society name
in the Baptist editorial identifies a publication, not Chartrand's employer.
The 1944 NCAC liaison was an OSS assignment, not an immediate predecessor.

Adjudication direction for the next import: preserve six unresolved names
with individual Box 119 questions; keep Alston's academic biography and
Chester's missionary biography in identity review; accept only the
identifier-backed Charter/Chartier Army occupation with uncertain OSS timing;
and retain Charr's confirmed Army match separately from disputed biographical
and chronological candidates. No new named employer is established by these
sources.
