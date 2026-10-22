# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 16:21 UTC

New CVEs published between 2026-10-22 15:18 UTC and 2026-10-22 16:21 UTC.

[Full CSV](data/new-cves-2026-10-22T16-21-09-065205Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 16:17:34 | [CVE-2026-114485](https://nvd.nist.gov/vuln/detail/CVE-2026-114485) |  |  | Insufficient protection of sensitive information in the user list endpoint in Devolutions Server 2026.3.10.0 and earlie… |
| 2026-10-22 16:17:34 | [CVE-2026-114486](https://nvd.nist.gov/vuln/detail/CVE-2026-114486) |  |  | Incorrect authorization in the Devolutions Gateway token generation in Devolutions Server 2026.3.10.0 and earlier allow… |
| 2026-10-22 16:17:34 | [CVE-2026-114487](https://nvd.nist.gov/vuln/detail/CVE-2026-114487) |  |  | Missing authorization in the PAM AD computer import endpoint in Devolutions Server 2026.3.5.0 through 2026.3.10.0 and 2… |
| 2026-10-22 16:17:34 | [CVE-2026-114603](https://nvd.nist.gov/vuln/detail/CVE-2026-114603) | Medium | 5.3 | OpenTelemetry Python provides the Python API and SDK for OpenTelemetry. Prior to 1.45.1, the opentelemetry-api function… |
| 2026-10-22 16:17:35 | [CVE-2026-115450](https://nvd.nist.gov/vuln/detail/CVE-2026-115450) | High | 7.1 | External Control of Assumed-Immutable Web Parameter (CWE-472) in the cart and checkout flow of MarcosCamara01 Ecommerce… |
| 2026-10-22 16:17:35 | [CVE-2026-115453](https://nvd.nist.gov/vuln/detail/CVE-2026-115453) | High | 7.1 | Authorization Bypass Through User-Controlled Key (CWE-639) in the cart and wishlist repositories of MarcosCamara01 Ecom… |
| 2026-10-22 16:17:35 | [CVE-2026-115454](https://nvd.nist.gov/vuln/detail/CVE-2026-115454) | Medium | 5.3 | An excessive resource allocation issue in the remote workflow editing capabilities of KNIME Business Hub prior to versi… |
| 2026-10-22 16:17:35 | [CVE-2026-115482](https://nvd.nist.gov/vuln/detail/CVE-2026-115482) | High | 7.5 | In lsquic before 4.9.0, the HTTP/3 implementation can use an excessive amount of memory because the number of buffered… |
| 2026-10-22 16:17:35 | [CVE-2026-115494](https://nvd.nist.gov/vuln/detail/CVE-2026-115494) | Medium | 5.3 | A flaw in the cross-site request forgery (CSRF) prevention of KNIME Business Hub prior to version 1.19.0 allows an auth… |
| 2026-10-22 16:17:35 | [CVE-2026-115496](https://nvd.nist.gov/vuln/detail/CVE-2026-115496) | Medium | 6.9 | Overly informative error messages in the catalog functionality of KNIME Business Hub prior to version 1.18.5 may allow… |
| 2026-10-22 16:17:36 | [CVE-2026-51954](https://nvd.nist.gov/vuln/detail/CVE-2026-51954) |  |  | An issue in Webasyst Framework 4.0.3 and before allows a remote attacker to execute arbitrary code via a crafted OAuth… |
| 2026-10-22 16:19:16 | [CVE-2026-94482](https://nvd.nist.gov/vuln/detail/CVE-2026-94482) | High | 8.2 | Next.js is a React framework for building full-stack web applications. From 13.0.0 until 15.5.28 and 16.4.1, crafted re… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
