# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 10:19 UTC

New CVEs published between 2026-11-01 09:18 UTC and 2026-11-01 10:19 UTC.

[Full CSV](data/new-cves-2026-11-01T10-19-52-670323Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 10:18:33 | [CVE-2026-112887](https://nvd.nist.gov/vuln/detail/CVE-2026-112887) |  |  | Gitea Actions task tokens authenticate to the REST API as a shared system user with a negative ID, which repository, or… |
| 2026-11-01 10:18:34 | [CVE-2026-113429](https://nvd.nist.gov/vuln/detail/CVE-2026-113429) |  |  | Legacy (v1 to v3) Actions artifact uploads stored the request's `Content-Encoding` header unchecked in the column that… |
| 2026-11-01 10:18:34 | [CVE-2026-114199](https://nvd.nist.gov/vuln/detail/CVE-2026-114199) |  |  | `GET /api/v1/users/{username}/heatmap` computed the contribution heatmap with the repository access of the token owner… |
| 2026-11-01 10:18:34 | [CVE-2026-116289](https://nvd.nist.gov/vuln/detail/CVE-2026-116289) |  |  | Gitea did not reject personal access tokens restricted to public resources (`public-only`) on the organization Actions… |
| 2026-11-01 10:18:35 | [CVE-2026-116296](https://nvd.nist.gov/vuln/detail/CVE-2026-116296) |  |  | The API routes for releases, release assets, milestones and repository labels did not reject changes to archived reposi… |
| 2026-11-01 10:18:35 | [CVE-2026-116474](https://nvd.nist.gov/vuln/detail/CVE-2026-116474) |  |  | The `GITEA_TOKEN` of a Gitea Actions job authenticates as the `gitea-actions` system user, and the `/api/v1/user` email… |
| 2026-11-01 10:18:35 | [CVE-2026-117635](https://nvd.nist.gov/vuln/detail/CVE-2026-117635) |  |  | The `/api/v1/admin` route group did not enforce the `public-only` restriction of personal access tokens. A public-only… |
| 2026-11-01 10:18:35 | [CVE-2026-117646](https://nvd.nist.gov/vuln/detail/CVE-2026-117646) |  |  | The repositories, stars and watching tabs of user profiles and the repository list of organization home pages included… |
| 2026-11-01 10:18:35 | [CVE-2026-117649](https://nvd.nist.gov/vuln/detail/CVE-2026-117649) |  |  | The issue timeline API and the web issue page hid cross-reference events that point at issues the reader cannot access,… |
| 2026-11-01 10:18:35 | [CVE-2026-117677](https://nvd.nist.gov/vuln/detail/CVE-2026-117677) |  |  | When parsing an uploaded Helm chart, Gitea decompressed the archive and read every tar entry while looking for `Chart.y… |
| 2026-11-01 10:18:35 | [CVE-2026-117685](https://nvd.nist.gov/vuln/detail/CVE-2026-117685) |  |  | The OCI registry's cross-repository blob mount checked the target package against the token's `public-only` restriction… |
| 2026-11-01 10:18:36 | [CVE-2026-118386](https://nvd.nist.gov/vuln/detail/CVE-2026-118386) |  |  | Workflows triggered by a pull request review were read from the commit named in the review's `commit_id`, while the for… |
| 2026-11-01 10:18:36 | [CVE-2026-118394](https://nvd.nist.gov/vuln/detail/CVE-2026-118394) |  |  | The OAuth2 userinfo endpoint (`/login/oauth/userinfo`) decided whether to limit the `groups` claim to public organizati… |
| 2026-11-01 10:18:36 | [CVE-2026-118395](https://nvd.nist.gov/vuln/detail/CVE-2026-118395) |  |  | Gitea 1.27.3 stopped personal access tokens restricted to public resources (`public-only`) from creating repositories t… |
| 2026-11-01 10:18:36 | [CVE-2026-118504](https://nvd.nist.gov/vuln/detail/CVE-2026-118504) |  |  | The web interface blocks issue and pull request changes on archived repositories, but several issue routes of the REST… |
| 2026-11-01 10:18:36 | [CVE-2026-119441](https://nvd.nist.gov/vuln/detail/CVE-2026-119441) |  |  | `DELETE /api/v1/orgs/{org}/repos` deletes all repositories of an organization, but it did not enforce the public-only r… |
| 2026-11-01 10:18:36 | [CVE-2026-119533](https://nvd.nist.gov/vuln/detail/CVE-2026-119533) |  |  | Repository and organization project boards listed the pull requests that reference each issue on the board without chec… |
| 2026-11-01 10:18:36 | [CVE-2026-119625](https://nvd.nist.gov/vuln/detail/CVE-2026-119625) |  |  | The `/{username}` web route accepted personal access tokens over HTTP Basic authentication without checking their scope… |
| 2026-11-01 10:18:37 | [CVE-2026-119627](https://nvd.nist.gov/vuln/detail/CVE-2026-119627) |  |  | The web profile and RSS/Atom feed routes of users and organizations checked only whether a signed-in viewer could see a… |
| 2026-11-01 10:18:37 | [CVE-2026-120223](https://nvd.nist.gov/vuln/detail/CVE-2026-120223) | Low | 1.3 | A vulnerability was identified in Oray Pugongying X5 Pro up to 7.6.1. This impacts the function session_get of the file… |
| 2026-11-01 10:18:37 | [CVE-2026-120263](https://nvd.nist.gov/vuln/detail/CVE-2026-120263) |  |  | When `[oauth2_client].ACCOUNT_LINKING` is set to `auto` (not the default) and registration is enabled, the link-account… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
