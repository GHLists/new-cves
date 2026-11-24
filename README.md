# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 09:20 UTC

New CVEs published between 2026-11-24 08:21 UTC and 2026-11-24 09:20 UTC.

[Full CSV](data/new-cves-2026-11-24T09-20-27-913579Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 09:17:05 | [CVE-2026-120933](https://nvd.nist.gov/vuln/detail/CVE-2026-120933) | High | 7.0 | A cleartext transmission of sensitive information vulnerability in the ADM Notifications allows network eavesdroppers o… |
| 2026-11-24 09:17:06 | [CVE-2026-120941](https://nvd.nist.gov/vuln/detail/CVE-2026-120941) | High | 8.3 | An improper certificate validation vulnerability exists in ADM App Central, due to disabled peer verification within th… |
| 2026-11-24 09:17:06 | [CVE-2026-120942](https://nvd.nist.gov/vuln/detail/CVE-2026-120942) | Medium | 6.7 | A path traversal vulnerability in the regional options of ADM allows attackers to read arbitrary files on the system. T… |
| 2026-11-24 09:17:06 | [CVE-2026-120943](https://nvd.nist.gov/vuln/detail/CVE-2026-120943) | High | 7.7 | An improper TLS certificate validation vulnerability exists in the ADM online update service. An unauthenticated attack… |
| 2026-11-24 09:17:06 | [CVE-2026-120944](https://nvd.nist.gov/vuln/detail/CVE-2026-120944) | High | 8.6 | A stack-based buffer overflow vulnerability in the ADM allows remote authenticated administrators to cause a denial of… |
| 2026-11-24 09:17:06 | [CVE-2026-120945](https://nvd.nist.gov/vuln/detail/CVE-2026-120945) | High | 8.3 | A relative path traversal vulnerability in the FTP Backup of ADM, allows an attacker controlling a configured FTP serve… |
| 2026-11-24 09:17:06 | [CVE-2026-120950](https://nvd.nist.gov/vuln/detail/CVE-2026-120950) | Medium | 5.1 | A stack-based buffer overflow vulnerability exists in the IP block management component of ADM due to insufficient inpu… |
| 2026-11-24 09:17:06 | [CVE-2026-133774](https://nvd.nist.gov/vuln/detail/CVE-2026-133774) | Medium | 6.3 | A live component protected by #[IsGranted], on its class or on its default action, can be rendered by a caller who is n… |
| 2026-11-24 09:17:07 | [CVE-2026-133775](https://nvd.nist.gov/vuln/detail/CVE-2026-133775) | Medium | 5.3 | The fix for CVE-2026-55877 (GHSA-6v8j-33hc-mv84) sanitizes the SVG of icons before they are rendered inline. It removes… |
| 2026-11-24 09:17:07 | [CVE-2026-133776](https://nvd.nist.gov/vuln/detail/CVE-2026-133776) | Medium | 5.3 | The fix for CVE-2026-55877 (GHSA-6v8j-33hc-mv84) sanitizes the SVG of icons before they are rendered inline. When the s… |
| 2026-11-24 09:17:07 | [CVE-2026-133777](https://nvd.nist.gov/vuln/detail/CVE-2026-133777) | Medium | 5.3 | The fix for CVE-2026-55877 (GHSA-6v8j-33hc-mv84) sanitizes the SVG of icons before they are rendered inline. Browsers p… |
| 2026-11-24 09:17:07 | [CVE-2026-133778](https://nvd.nist.gov/vuln/detail/CVE-2026-133778) | Medium | 6.3 | #[AsLiveComponent(route: '...')] makes a live component send its requests to another route. The documentation suggests… |
| 2026-11-24 09:17:07 | [CVE-2026-133779](https://nvd.nist.gov/vuln/detail/CVE-2026-133779) | Medium | 5.3 | The fix for CVE-2026-55877 (GHSA-6v8j-33hc-mv84) sanitizes the SVG of icons before they are rendered inline. The checks… |
| 2026-11-24 09:17:07 | [CVE-2026-133780](https://nvd.nist.gov/vuln/detail/CVE-2026-133780) | High | 7.3 | The @symfony/stimulus-bridge npm package includes a Webpack loader called lazy-controller-loader that supports "magic c… |
| 2026-11-24 09:17:07 | [CVE-2026-133781](https://nvd.nist.gov/vuln/detail/CVE-2026-133781) | High | 7.3 | The controllers.json loader of @symfony/stimulus-bridge loads the package.json file of each package listed in controlle… |
| 2026-11-24 09:17:08 | [CVE-2026-134895](https://nvd.nist.gov/vuln/detail/CVE-2026-134895) | High | 8.2 | A path traversal vulnerability in the File Explorer share-link upload component allows a remote attacker with a folder-… |
| 2026-11-24 09:17:08 | [CVE-2026-134898](https://nvd.nist.gov/vuln/detail/CVE-2026-134898) | High | 8.7 | A path traversal vulnerability in the File Explorer share-link folder-listing endpoint allows a remote attacker with a… |
| 2026-11-24 09:17:08 | [CVE-2026-135801](https://nvd.nist.gov/vuln/detail/CVE-2026-135801) |  |  | Since the fix for CVE-2025-64500, Request::getPathInfo() strips the script name from the start of the URL. It does so e… |
| 2026-11-24 09:17:08 | [CVE-2026-135802](https://nvd.nist.gov/vuln/detail/CVE-2026-135802) |  |  | When Request::getBaseUrl() does not find the script name at the start of the request URI, it looks for it further into… |
| 2026-11-24 09:17:08 | [CVE-2026-135803](https://nvd.nist.gov/vuln/detail/CVE-2026-135803) |  |  | Most methods of Symfony\Component\Filesystem\Path rely on Path::split(), which takes everything before the first :// as… |
| 2026-11-24 09:17:08 | [CVE-2026-135804](https://nvd.nist.gov/vuln/detail/CVE-2026-135804) |  |  | The fix for CVE-2026-45756 lowers pcre.backtrack_limit to 10000 around each preg_match() call of the match() and search… |
| 2026-11-24 09:17:09 | [CVE-2026-78338](https://nvd.nist.gov/vuln/detail/CVE-2026-78338) | Medium | 6.3 | Missing authentication in the conversation session resource handling of Unblu inc. Unblu Spark 7.0 through 7.57.10 and… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
