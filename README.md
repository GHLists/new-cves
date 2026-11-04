# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-04 18:19 UTC

New CVEs published between 2026-11-04 17:18 UTC and 2026-11-04 18:19 UTC.

[Full CSV](data/new-cves-2026-11-04T18-19-33-896925Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-04 18:17:42 | [CVE-2026-121927](https://nvd.nist.gov/vuln/detail/CVE-2026-121927) | Low | 2.1 | A vulnerability has been found in InfiniFlow RAGFlow up to 0.27.3. Affected by this issue is the function _account_get… |
| 2026-11-04 18:17:43 | [CVE-2026-121971](https://nvd.nist.gov/vuln/detail/CVE-2026-121971) | High | 8.2 | The component ScopingHttpClient in Symfony HttpClient merges the options of its default scope (such as auth_bearer or a… |
| 2026-11-04 18:17:43 | [CVE-2026-122054](https://nvd.nist.gov/vuln/detail/CVE-2026-122054) | Medium | 5.9 | Converting crafted BIG-HKSCS input to UCS-4 or the internal wide character encoding, for example with iconv, in the GNU… |
| 2026-11-04 18:17:43 | [CVE-2026-122116](https://nvd.nist.gov/vuln/detail/CVE-2026-122116) | Medium | 4.3 | Certain Yealink terminal devices before 2026-04-21 contain an improper access control vulnerability in the Wi-Fi 802.1X… |
| 2026-11-04 18:17:43 | [CVE-2026-122118](https://nvd.nist.gov/vuln/detail/CVE-2026-122118) | High | 7.4 | In certain Yealink products before 2026-04-15, when the Wi-Fi AP function is enabled, a default 8-digit numeric PSK wit… |
| 2026-11-04 18:17:44 | [CVE-2026-57853](https://nvd.nist.gov/vuln/detail/CVE-2026-57853) | High | 8.7 | DataGerry before 3.3.0 contains a server-side template injection vulnerability that allows authenticated attackers with… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
