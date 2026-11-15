# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-15 22:18 UTC

New CVEs published between 2026-11-15 21:18 UTC and 2026-11-15 22:18 UTC.

[Full CSV](data/new-cves-2026-11-15T22-18-41-133917Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-15 22:17:17 | [CVE-2026-118389](https://nvd.nist.gov/vuln/detail/CVE-2026-118389) |  |  | The RubyGems package registry accepted gems whose platform, dependency names or dependency version requirements contain… |
| 2026-11-15 22:17:17 | [CVE-2026-118535](https://nvd.nist.gov/vuln/detail/CVE-2026-118535) |  |  | A repository registered by its owner as a source of scoped workflows kept that registration when it was transferred to… |
| 2026-11-15 22:17:17 | [CVE-2026-120725](https://nvd.nist.gov/vuln/detail/CVE-2026-120725) |  |  | With `REQUIRE_SIGNIN_VIEW = true`, the Git LFS endpoints still answered unauthenticated requests for repositories that… |
| 2026-11-15 22:17:17 | [CVE-2026-120729](https://nvd.nist.gov/vuln/detail/CVE-2026-120729) |  |  | The popup shown when hovering an issue reference loaded its data from the path of the hovered link and inserted part of… |
| 2026-11-15 22:17:17 | [CVE-2026-120991](https://nvd.nist.gov/vuln/detail/CVE-2026-120991) |  |  | When a container blob upload was rejected, for example because it exceeded a package size quota, the cleanup removed th… |
| 2026-11-15 22:17:18 | [CVE-2026-123002](https://nvd.nist.gov/vuln/detail/CVE-2026-123002) |  |  | Gitea accepted an unlimited number of wrong TOTP passcodes during sign-in, in the password reset flow and for Basic aut… |
| 2026-11-15 22:17:18 | [CVE-2026-123009](https://nvd.nist.gov/vuln/detail/CVE-2026-123009) |  |  | When a file is edited in a fork through the web editor, Gitea can first copy a branch from the base repository into the… |
| 2026-11-15 22:17:18 | [CVE-2026-123065](https://nvd.nist.gov/vuln/detail/CVE-2026-123065) |  |  | When a release was edited, the files of the attachments to remove were deleted by the identifiers submitted in the form… |
| 2026-11-15 22:17:18 | [CVE-2026-123638](https://nvd.nist.gov/vuln/detail/CVE-2026-123638) |  |  | The "Protected file patterns" setting of a branch protection rule was checked against file names as git prints them, an… |
| 2026-11-15 22:17:18 | [CVE-2026-123642](https://nvd.nist.gov/vuln/detail/CVE-2026-123642) |  |  | The AGit flow (pushing to `refs/for/...`) did not check the pusher's access to pull requests again when it created the… |
| 2026-11-15 22:17:18 | [CVE-2026-125617](https://nvd.nist.gov/vuln/detail/CVE-2026-125617) |  |  | `GET /api/v1/users/{username}/orgs/{org}/permissions` only checked that the organization is visible to the caller and t… |
| 2026-11-15 22:17:18 | [CVE-2026-126338](https://nvd.nist.gov/vuln/detail/CVE-2026-126338) |  |  | Replying to a code review comment accepted a review ID that belongs to a different pull request, through the web form,… |
| 2026-11-15 22:17:19 | [CVE-2026-127958](https://nvd.nist.gov/vuln/detail/CVE-2026-127958) |  |  | A pull request review created through the API as a draft (`event` set to `PENDING` or left empty) was added to the pull… |
| 2026-11-15 22:17:19 | [CVE-2026-128359](https://nvd.nist.gov/vuln/detail/CVE-2026-128359) |  |  | When Gitea acts as an OAuth2 or OpenID Connect provider, the token endpoint did not check the state of the user. After… |
| 2026-11-15 22:17:19 | [CVE-2026-128365](https://nvd.nist.gov/vuln/detail/CVE-2026-128365) |  |  | Removing a team's review request looked up a review by the negated team ID, which for the team with ID 2 is the ID of t… |
| 2026-11-15 22:17:19 | [CVE-2026-129337](https://nvd.nist.gov/vuln/detail/CVE-2026-129337) |  |  | Git over HTTP lowers the required permission for pushes to read access, so that the AGit flow works, and relies on the… |
| 2026-11-15 22:17:19 | [CVE-2026-129341](https://nvd.nist.gov/vuln/detail/CVE-2026-129341) |  |  | The web endpoint that removes an attachment skipped the permission check when the request came from the user who had up… |
| 2026-11-15 22:17:19 | [CVE-2026-129525](https://nvd.nist.gov/vuln/detail/CVE-2026-129525) |  |  | Several endpoints that work on both issues and pull requests did not check which of the two the addressed item is. A us… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
