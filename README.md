# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-11 16:20 UTC

New CVEs published between 2026-11-11 15:19 UTC and 2026-11-11 16:20 UTC.

[Full CSV](data/new-cves-2026-11-11T16-20-15-435284Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-11 16:17:24 | [CVE-2026-100290](https://nvd.nist.gov/vuln/detail/CVE-2026-100290) | Low | 3.7 | The regcomp and regexec functions in the GNU C Library version 2.3 to version 2.44 may read freed memory and free the s… |
| 2026-11-11 16:17:24 | [CVE-2026-105440](https://nvd.nist.gov/vuln/detail/CVE-2026-105440) | High | 8.3 | Missing authorization in the JSON-RPC web services interface of Extreme Networks Switch Engine (EXOS) allows an authent… |
| 2026-11-11 16:17:24 | [CVE-2026-115819](https://nvd.nist.gov/vuln/detail/CVE-2026-115819) | Medium | 4.8 | Calling the wide scanf family of functions (swscanf, fwscanf, wscanf, vswscanf, vfwscanf and vwscanf) with a %s or %[ c… |
| 2026-11-11 16:17:25 | [CVE-2026-124686](https://nvd.nist.gov/vuln/detail/CVE-2026-124686) | Medium | 5.4 | In Progress® Kendo® UI for jQuery versions prior to 2026.4.1111, kendo.init() compiles data-* attribute values with new… |
| 2026-11-11 16:17:25 | [CVE-2026-64855](https://nvd.nist.gov/vuln/detail/CVE-2026-64855) | High | 8.2 | soapbar is a SOAP library for Python — client, server, and WSDL handling. Prior to version 0.13.0, verify_envelope_bsp(… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
