# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-26 04:20 UTC

New CVEs published between 2026-11-26 03:18 UTC and 2026-11-26 04:20 UTC.

[Full CSV](data/new-cves-2026-11-26T04-20-22-168669Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-26 04:17:09 | [CVE-2026-123688](https://nvd.nist.gov/vuln/detail/CVE-2026-123688) | Medium | 5.3 | An improper authorization vulnerability exists in the patch management functionality of StellarOne. An attacker with Vi… |
| 2026-11-26 04:17:09 | [CVE-2026-123689](https://nvd.nist.gov/vuln/detail/CVE-2026-123689) | High | 8.6 | A SQL injection vulnerability exists in the Search Agents API of StellarOne due to improper sanitization of user-suppli… |
| 2026-11-26 04:17:10 | [CVE-2026-133202](https://nvd.nist.gov/vuln/detail/CVE-2026-133202) | Medium | 5.4 | In Revive Adserver through 6.0.9, an authenticated manager with access to two advertisers can associate a conversion tr… |
| 2026-11-26 04:17:10 | [CVE-2026-133203](https://nvd.nist.gov/vuln/detail/CVE-2026-133203) | Medium | 5.3 | In Revive Adserver through 6.0.9, the public conversion-variable endpoint does not verify that a caller-supplied conver… |
| 2026-11-26 04:17:10 | [CVE-2026-133204](https://nvd.nist.gov/vuln/detail/CVE-2026-133204) | Medium | 4.3 | In Revive Adserver through 6.0.9, the zone-linking page can disclose campaign and banner names and identifiers belongin… |
| 2026-11-26 04:17:10 | [CVE-2026-133205](https://nvd.nist.gov/vuln/detail/CVE-2026-133205) | Medium | 4.3 | In Revive Adserver through 6.0.9, an authenticated manager can supply another agency's advertiser or website identifier… |
| 2026-11-26 04:17:11 | [CVE-2026-133206](https://nvd.nist.gov/vuln/detail/CVE-2026-133206) | Medium | 4.3 | In Revive Adserver through 6.0.9, an advertiser can put XML syntax in fields of its own video creative. Unescaped Media… |
| 2026-11-26 04:17:11 | [CVE-2026-133207](https://nvd.nist.gov/vuln/detail/CVE-2026-133207) | Medium | 4.1 | In Revive Adserver through 6.0.9, user-controlled entity names in XLS report exports can be interpreted as spreadsheet… |
| 2026-11-26 04:17:11 | [CVE-2026-133208](https://nvd.nist.gov/vuln/detail/CVE-2026-133208) | Medium | 6.1 | In Revive Adserver through 6.0.9, unauthenticated request parameters in ad delivery can cause reflected cross-site scri… |
| 2026-11-26 04:17:11 | [CVE-2026-133209](https://nvd.nist.gov/vuln/detail/CVE-2026-133209) | Low | 3.1 | In Revive Adserver through 6.0.9, deleting an agency, advertiser, or publisher through affected API paths can leave the… |
| 2026-11-26 04:17:11 | [CVE-2026-133210](https://nvd.nist.gov/vuln/detail/CVE-2026-133210) | Medium | 6.5 | In Revive Adserver through 6.0.9, the zone banner-linking page (zone-include.php) does not cast the keys of the include… |
| 2026-11-26 04:17:11 | [CVE-2026-133211](https://nvd.nist.gov/vuln/detail/CVE-2026-133211) | Medium | 4.7 | In Revive Adserver through 6.0.9, the ct0 request parameter of the delivery scripts is only required to start with http… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
