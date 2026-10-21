# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 14:20 UTC

New CVEs published between 2026-10-21 13:20 UTC and 2026-10-21 14:20 UTC.

[Full CSV](data/new-cves-2026-10-21T14-20-06-359341Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 13:20:56 | [CVE-2026-90484](https://nvd.nist.gov/vuln/detail/CVE-2026-90484) |  |  | The MySQL client response parser in Apache bRPC dereferences a null pointer when the server peer sends a zero-payload-l… |
| 2026-10-21 13:21:08 | [CVE-2026-94300](https://nvd.nist.gov/vuln/detail/CVE-2026-94300) | High | 8.1 | Replaying GSS-TSIG signed UDP messages can result in memory corruption in "`named`". An attacker who can capture a prev… |
| 2026-10-21 13:21:08 | [CVE-2026-96888](https://nvd.nist.gov/vuln/detail/CVE-2026-96888) | High | 7.5 | A BIND resolver that is configured with both a "redirect" zone and "qname-minimization strict" may abort with an assert… |
| 2026-10-21 13:21:09 | [CVE-2026-97313](https://nvd.nist.gov/vuln/detail/CVE-2026-97313) | High | 7.5 | A recursive BIND server that receives a query with recursion desired (RD=1) followed by a non-recursive query (RD=0) ma… |
| 2026-10-21 14:17:04 | [CVE-2024-4989](https://nvd.nist.gov/vuln/detail/CVE-2024-4989) | Medium | 5.4 | The callback URL parameter in WSO2 API Manager fails to validate user-supplied input, allowing it to be controlled by m… |
| 2026-10-21 14:17:04 | [CVE-2024-5139](https://nvd.nist.gov/vuln/detail/CVE-2024-5139) | Medium | 6.1 | The Authentication Endpoint accepts user-supplied input without sufficient encoding, allowing for the injection of mali… |
| 2026-10-21 14:17:05 | [CVE-2024-5563](https://nvd.nist.gov/vuln/detail/CVE-2024-5563) | Medium | 4.8 | Due to an incomplete implementation, reCaptcha is not applied to certain authentication flows even when the reCaptcha o… |
| 2026-10-21 14:17:05 | [CVE-2024-6423](https://nvd.nist.gov/vuln/detail/CVE-2024-6423) | Medium | 4.0 | The product failed to enforce validation constraints on user-supplied input in URL parameters, allowing sensitive data… |
| 2026-10-21 14:17:06 | [CVE-2024-7478](https://nvd.nist.gov/vuln/detail/CVE-2024-7478) | Medium | 5.8 | When a WSO2 product is configured to use an external user store, the system fails to adequately obscure the existence o… |
| 2026-10-21 14:17:06 | [CVE-2025-0326](https://nvd.nist.gov/vuln/detail/CVE-2025-0326) |  |  | The system fails to invalidate existing access tokens associated with sub-organization users during sensitive account m… |
| 2026-10-21 14:17:06 | [CVE-2025-60479](https://nvd.nist.gov/vuln/detail/CVE-2025-60479) |  |  | A NULL pointer dereference in the StatSFVec2f function (/scene_manager/scene_stats.c) of GPAC Project/MP4Box before 2.5… |
| 2026-10-21 14:17:07 | [CVE-2025-60489](https://nvd.nist.gov/vuln/detail/CVE-2025-60489) |  |  | A NULL pointer dereference in the dasher_insert_timeline_entry function (/filters/dasher.c) of GPAC Project/MP4Box befo… |
| 2026-10-21 14:17:07 | [CVE-2025-71438](https://nvd.nist.gov/vuln/detail/CVE-2025-71438) |  |  | An out-of-bounds read in gf_odf_ac4_cfg_dsi_v1 (/odf/descriptors.c) in GPAC Project/MP4Box before v26.07.0 allows attac… |
| 2026-10-21 14:17:08 | [CVE-2026-104947](https://nvd.nist.gov/vuln/detail/CVE-2026-104947) | Medium | 5.3 | WarehousePG (WHPG) 7.2.1 through 7.6.0 is affected by a missing authorization vulnerability (CWE-862) in the built-in f… |
| 2026-10-21 14:17:09 | [CVE-2026-104948](https://nvd.nist.gov/vuln/detail/CVE-2026-104948) | High | 7.1 | WarehousePG (WHPG) 6.27.1 through 6.27.6 and 7.2.1 through 7.6.0 are affected by a missing authorization vulnerability… |
| 2026-10-21 14:17:09 | [CVE-2026-104949](https://nvd.nist.gov/vuln/detail/CVE-2026-104949) | Low | 2.3 | WarehousePG (WHPG) 6.27.1 through 6.27.6 and 7.2.1 through 7.6.0 are affected by a missing authorization vulnerability… |
| 2026-10-21 14:17:09 | [CVE-2026-109618](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) | Critical | 9.2 | PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some c… |
| 2026-10-21 14:17:09 | [CVE-2026-109619](https://nvd.nist.gov/vuln/detail/CVE-2026-109619) | Critical | 9.2 | PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be co… |
| 2026-10-21 14:17:13 | [CVE-2026-114249](https://nvd.nist.gov/vuln/detail/CVE-2026-114249) | Medium | 5.5 | A vulnerability was detected in dhikshitha29 Insurance-Management-System 91de5edda5baa109ad8e9baf03ce6a3ceda84183/12536… |
| 2026-10-21 14:17:14 | [CVE-2026-114437](https://nvd.nist.gov/vuln/detail/CVE-2026-114437) | Medium | 6.3 | In the Golang Chi web framework, the ClientIPFromXFF middleware skips any X-Forwarded-For entry in a configured trusted… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
