# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-11 01:19 UTC

New CVEs published between 2026-11-11 00:21 UTC and 2026-11-11 01:19 UTC.

[Full CSV](data/new-cves-2026-11-11T01-19-58-569847Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-11 01:17:14 | [CVE-2026-126495](https://nvd.nist.gov/vuln/detail/CVE-2026-126495) | Medium | 5.3 | MQTTX desktop through 1.13.3 contains a stored cross-site scripting vulnerability that allows attackers to inject scrip… |
| 2026-11-11 01:17:14 | [CVE-2026-126496](https://nvd.nist.gov/vuln/detail/CVE-2026-126496) | Medium | 5.3 | 1Panel-dev CordysCRM before 1.9.6 contains an authorization bypass vulnerability in CustomerContactController.get that… |
| 2026-11-11 01:17:14 | [CVE-2026-126497](https://nvd.nist.gov/vuln/detail/CVE-2026-126497) | High | 8.5 | LibreCAD through 2.2.1.6 contains a heap-based out-of-bounds write vulnerability in the bundled libdxfrw dwgReader18::p… |
| 2026-11-11 01:17:14 | [CVE-2026-126498](https://nvd.nist.gov/vuln/detail/CVE-2026-126498) | Medium | 5.1 | WriteFreely before 0.17.3 contains a stored cross-site scripting vulnerability that allows authenticated authors to inj… |
| 2026-11-11 01:17:14 | [CVE-2026-126499](https://nvd.nist.gov/vuln/detail/CVE-2026-126499) | High | 8.3 | Jellyfin before 12.0 contains a path traversal vulnerability in the DELETE /Library/VirtualFolders and POST /Library/Vi… |
| 2026-11-11 01:17:15 | [CVE-2026-126539](https://nvd.nist.gov/vuln/detail/CVE-2026-126539) | Critical | 9.2 | Directus before 12.1.0 contains an authorization bypass vulnerability that allows unauthenticated attackers to skip per… |
| 2026-11-11 01:17:15 | [CVE-2026-126541](https://nvd.nist.gov/vuln/detail/CVE-2026-126541) | High | 8.6 | WWBN AVideo through 29.7.1 contains a missing authorization vulnerability in Live plugin restream endpoints that allows… |
| 2026-11-11 01:17:15 | [CVE-2026-126542](https://nvd.nist.gov/vuln/detail/CVE-2026-126542) | Critical | 9.3 | WWBN AVideo 6.5 through 29.7.1 contains an authentication bypass vulnerability that allows unauthenticated attackers to… |
| 2026-11-11 01:17:15 | [CVE-2026-126543](https://nvd.nist.gov/vuln/detail/CVE-2026-126543) | High | 8.7 | WWBN AVideo through 29.7.1 contains an improper payment verification vulnerability in plugin/PayPalYPT/ipnV2.php that c… |
| 2026-11-11 01:17:15 | [CVE-2026-126544](https://nvd.nist.gov/vuln/detail/CVE-2026-126544) | Medium | 5.3 | WWBN AVideo 6.5 through 29.7.1 contains an email verification bypass vulnerability in User::verifyCode() in objects/use… |
| 2026-11-11 01:17:16 | [CVE-2026-126545](https://nvd.nist.gov/vuln/detail/CVE-2026-126545) | Medium | 5.3 | WWBN AVideo through 29.7.1 contains a missing authorization vulnerability in API::get_api_tags() in plugin/API/API.php… |
| 2026-11-11 01:17:16 | [CVE-2026-126546](https://nvd.nist.gov/vuln/detail/CVE-2026-126546) | Medium | 5.3 | Viber for iOS through 29.4.0.24 fails to validate the logical screen width and height in received GIF headers, allowing… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
