# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-18 19:18 UTC

New CVEs published between 2026-10-18 18:20 UTC and 2026-10-18 19:18 UTC.

[Full CSV](data/new-cves-2026-10-18T19-18-42-816565Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-18 19:16:32 | [CVE-2026-104627](https://nvd.nist.gov/vuln/detail/CVE-2026-104627) |  |  | The Gitea OpenID association callback in the security settings accepted a positive OpenID 2.0 assertion without checkin… |
| 2026-10-18 19:16:32 | [CVE-2026-105661](https://nvd.nist.gov/vuln/detail/CVE-2026-105661) |  |  | Requesting `/{username}/-/repositories` for an individual user instead of an organization made the organization home ha… |
| 2026-10-18 19:16:32 | [CVE-2026-105964](https://nvd.nist.gov/vuln/detail/CVE-2026-105964) |  |  | The Gitea Actions artifact v4 (Twirp) handlers read the whole request body into memory without a size limit. A user who… |
| 2026-10-18 19:16:32 | [CVE-2026-107618](https://nvd.nist.gov/vuln/detail/CVE-2026-107618) |  |  | `POST /{owner}/{repo}/topics` was registered without the sign-in middleware that provides the cross-origin protection,… |
| 2026-10-18 19:16:32 | [CVE-2026-107686](https://nvd.nist.gov/vuln/detail/CVE-2026-107686) |  |  | The Gitea web handlers for adding and removing reactions on issues and comments did not refuse locked issues for users… |
| 2026-10-18 19:16:32 | [CVE-2026-109553](https://nvd.nist.gov/vuln/detail/CVE-2026-109553) |  |  | Gitea resolved the principals of an SSH certificate by searching the content of all stored public keys instead of only… |
| 2026-10-18 19:16:33 | [CVE-2026-109844](https://nvd.nist.gov/vuln/detail/CVE-2026-109844) |  |  | `GET /api/v1/user/subscriptions` returned the metadata of every repository a user was watching without checking that th… |
| 2026-10-18 19:16:33 | [CVE-2026-110311](https://nvd.nist.gov/vuln/detail/CVE-2026-110311) |  |  | Creating a draft release through the API returned an `assets` list that was built from a release without an ID, which m… |
| 2026-10-18 19:16:33 | [CVE-2026-110324](https://nvd.nist.gov/vuln/detail/CVE-2026-110324) |  |  | The visibility check of Gitea user profiles was applied to GET requests only, while `POST /{username}` (follow and unfo… |
| 2026-10-18 19:16:33 | [CVE-2026-110494](https://nvd.nist.gov/vuln/detail/CVE-2026-110494) |  |  | Adding attachments to a release checked the repository and release of an attachment but not whether it was already link… |
| 2026-10-18 19:16:33 | [CVE-2026-97204](https://nvd.nist.gov/vuln/detail/CVE-2026-97204) |  |  | Deleting a label compared the ID of the repository in the request against the organization ID of organization labels, a… |
| 2026-10-18 19:16:33 | [CVE-2026-97859](https://nvd.nist.gov/vuln/detail/CVE-2026-97859) |  |  | Seven Gitea API routes under `/api/v1/users/{username}` (followers, following, following/{target}, starred, subscriptio… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
