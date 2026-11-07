# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-07 15:18 UTC

New CVEs published between 2026-11-07 14:21 UTC and 2026-11-07 15:18 UTC.

[Full CSV](data/new-cves-2026-11-07T15-18-46-568574Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-07 15:17:14 | [CVE-2026-123989](https://nvd.nist.gov/vuln/detail/CVE-2026-123989) | Medium | 5.3 | A vulnerability was found in ESEngine DeepSeek-Reasonix up to 1.33.0. Impacted is the function loadGitStatus of the fil… |
| 2026-11-07 15:17:14 | [CVE-2026-124307](https://nvd.nist.gov/vuln/detail/CVE-2026-124307) | Medium | 5.8 | Fraunhofer HHI VVdeC before 3.2.1 contains a heap use-after-free vulnerability that allows attackers to corrupt memory… |
| 2026-11-07 15:17:14 | [CVE-2026-124308](https://nvd.nist.gov/vuln/detail/CVE-2026-124308) | Medium | 5.8 | Fraunhofer HHI VVdeC before 3.2.1 contains a heap use-after-free vulnerability in DecLibRecon::createSubPicRefBufs beca… |
| 2026-11-07 15:17:14 | [CVE-2026-124309](https://nvd.nist.gov/vuln/detail/CVE-2026-124309) | Medium | 6.9 | Fraunhofer HHI VVdeC before 3.2.1 contains a heap out-of-bounds read vulnerability in SEIReader::xParseSEIScalableNesti… |
| 2026-11-07 15:17:14 | [CVE-2026-124310](https://nvd.nist.gov/vuln/detail/CVE-2026-124310) | Medium | 6.9 | Fraunhofer HHI VVdeC before 3.2.1 contains an out-of-bounds read vulnerability that allows attackers to crash the decod… |
| 2026-11-07 15:17:14 | [CVE-2026-124311](https://nvd.nist.gov/vuln/detail/CVE-2026-124311) | Medium | 6.8 | Fraunhofer HHI VVdeC through 3.2.1 contains a NULL pointer dereference vulnerability in InterPrediction::xPredInterBlk… |
| 2026-11-07 15:17:15 | [CVE-2026-124312](https://nvd.nist.gov/vuln/detail/CVE-2026-124312) | Medium | 5.7 | Fraunhofer HHI VVdeC through 3.2.1 contains a heap out-of-bounds read vulnerability that allows attackers to crash the… |
| 2026-11-07 15:17:15 | [CVE-2026-124313](https://nvd.nist.gov/vuln/detail/CVE-2026-124313) | Medium | 5.3 | Frappe ERPNext before 15.121.4 and 16.x before 16.36.0 contains a missing authorization vulnerability in the whiteliste… |
| 2026-11-07 15:17:15 | [CVE-2026-124314](https://nvd.nist.gov/vuln/detail/CVE-2026-124314) | High | 7.1 | Frappe ERPNext before 15.121.4 and 16.x before 16.36.0 contains a missing authorization vulnerability in erpnext.crm.ut… |
| 2026-11-07 15:17:15 | [CVE-2026-124315](https://nvd.nist.gov/vuln/detail/CVE-2026-124315) | High | 7.1 | Frappe ERPNext before 15.121.4 and 16.x before 16.36.0 contains a missing authorization vulnerability in the whiteliste… |
| 2026-11-07 15:17:15 | [CVE-2026-124316](https://nvd.nist.gov/vuln/detail/CVE-2026-124316) | Medium | 5.3 | Frappe ERPNext before 15.121.4 and 16.x before 16.36.0 contains a missing authorization vulnerability in the whiteliste… |
| 2026-11-07 15:17:16 | [CVE-2026-124317](https://nvd.nist.gov/vuln/detail/CVE-2026-124317) | Medium | 6.3 | libexpat through 2.10.0 contains an out-of-bounds read vulnerability in unknown_toUtf8() and unknown_toUtf16() in xmlto… |
| 2026-11-07 15:17:16 | [CVE-2026-124318](https://nvd.nist.gov/vuln/detail/CVE-2026-124318) | High | 8.6 | Treeio through 2.0 contains an insecure deserialization vulnerability in UpdateRecord.get_format_strings and ModuleSett… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
