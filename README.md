# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 10:18 UTC

New CVEs published between 2026-11-03 09:18 UTC and 2026-11-03 10:18 UTC.

[Full CSV](data/new-cves-2026-11-03T10-18-46-101561Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 10:17:14 | [CVE-2026-119641](https://nvd.nist.gov/vuln/detail/CVE-2026-119641) |  |  | ** UNSUPPORTED WHEN ASSIGNED ** Improper input validation vulnerability in Apache Oozie. An authenticated Oozie user ca… |
| 2026-11-03 10:17:15 | [CVE-2026-119724](https://nvd.nist.gov/vuln/detail/CVE-2026-119724) |  |  | ** UNSUPPORTED WHEN ASSIGNED ** Improper restriction of recursive entity references in DTDs ('XML entity expansion') vu… |
| 2026-11-03 10:17:16 | [CVE-2026-119843](https://nvd.nist.gov/vuln/detail/CVE-2026-119843) | Medium | 6.5 | A flaw was found in GStreamer's gst-plugins-good package. The FLV media demuxer does not properly validate buffer sizes… |
| 2026-11-03 10:17:17 | [CVE-2026-120327](https://nvd.nist.gov/vuln/detail/CVE-2026-120327) | Medium | 5.3 | The click tracking middleware accepts an arbitrary target URL and redirects to it. Attackers can misuse links to the we… |
| 2026-11-03 10:17:17 | [CVE-2026-120328](https://nvd.nist.gov/vuln/detail/CVE-2026-120328) | Medium | 6.9 | The click tracking middleware does not validate the authentication code of a recipient if the code is omitted. Unauthen… |
| 2026-11-03 10:17:17 | [CVE-2026-120329](https://nvd.nist.gov/vuln/detail/CVE-2026-120329) | Medium | 5.3 | Saving the configuration of the mail backend module writes submitted settings to the page TSconfig without restricting… |
| 2026-11-03 10:17:17 | [CVE-2026-120330](https://nvd.nist.gov/vuln/detail/CVE-2026-120330) | High | 7.1 | Backend actions and ajax routes of the mail module do not check whether the backend user has access to the page of the… |
| 2026-11-03 10:17:17 | [CVE-2026-120331](https://nvd.nist.gov/vuln/detail/CVE-2026-120331) | Medium | 5.3 | Content of external URL mails, their stylesheets and images to embed is fetched by the server without validating the ta… |
| 2026-11-03 10:17:18 | [CVE-2026-120332](https://nvd.nist.gov/vuln/detail/CVE-2026-120332) | Medium | 5.1 | The HTML content of mails and tracked URLs are rendered unescaped in the backend module. Backend users with access to t… |
| 2026-11-03 10:17:18 | [CVE-2026-120333](https://nvd.nist.gov/vuln/detail/CVE-2026-120333) | High | 8.8 | The actions linked in the emails of the extension (e.g. to confirm a registration or the deletion of an account) do not… |
| 2026-11-03 10:17:18 | [CVE-2026-77691](https://nvd.nist.gov/vuln/detail/CVE-2026-77691) | High | 8.1 | ZohoCorp ManageEngine Key Manager Plus versions before 7151 allow authenticated users to enter malicious input when con… |
| 2026-11-03 10:17:19 | [CVE-2026-77777](https://nvd.nist.gov/vuln/detail/CVE-2026-77777) | High | 7.1 | ManageEngine Key Manager Plus versions before 7151 are vulnerable to an improper access control issue that allow authen… |
| 2026-11-03 10:17:19 | [CVE-2026-77778](https://nvd.nist.gov/vuln/detail/CVE-2026-77778) | High | 7.1 | ZohoCorp ManageEngine Key Manager Plus versions up to 7150 allow authenticated users to export certificates belonging t… |
| 2026-11-03 10:17:19 | [CVE-2026-89229](https://nvd.nist.gov/vuln/detail/CVE-2026-89229) | Medium | 5.1 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') in the ShareActivity component of BlueLM… |
| 2026-11-03 10:17:20 | [CVE-2026-89292](https://nvd.nist.gov/vuln/detail/CVE-2026-89292) | Critical | 9.2 | In Eclipse Mnestix Browser versions 1.6.0 up until but excluding 2.3.0 it was possible for an unauthenticated attacker… |
| 2026-11-03 10:17:20 | [CVE-2026-89293](https://nvd.nist.gov/vuln/detail/CVE-2026-89293) | High | 8.8 | In Eclipse Mnestix Browser versions 1.2.0 up until but excluding 2.3.0 it was possible for an unauthenticated attacker… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
