# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-22 18:18 UTC

New CVEs published between 2026-10-22 17:22 UTC and 2026-10-22 18:18 UTC.

[Full CSV](data/new-cves-2026-10-22T18-18-42-394412Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-22 18:17:26 | [CVE-2026-108357](https://nvd.nist.gov/vuln/detail/CVE-2026-108357) | High | 8.8 | PhpSpreadsheet is a pure PHP library for reading and writing spreadsheet files. From 3.3.0 until 3.10.8 and 5.10.0, Rea… |
| 2026-10-22 18:17:26 | [CVE-2026-108358](https://nvd.nist.gov/vuln/detail/CVE-2026-108358) | High | 8.8 | PhpSpreadsheet is a pure PHP library for reading and writing spreadsheet files. Prior to 1.30.7, 2.1.19, 2.4.8, 3.10.8,… |
| 2026-10-22 18:17:26 | [CVE-2026-108359](https://nvd.nist.gov/vuln/detail/CVE-2026-108359) | High | 8.7 | PhpSpreadsheet is a pure PHP library for reading and writing spreadsheet files. Prior to 1.30.7, 2.1.19, 2.4.8, 3.10.8,… |
| 2026-10-22 18:17:26 | [CVE-2026-108360](https://nvd.nist.gov/vuln/detail/CVE-2026-108360) | Medium | 6.4 | PhpSpreadsheet is a pure PHP library for reading and writing spreadsheet files. Prior to 1.30.7, 2.1.19, 2.4.8, 3.10.8,… |
| 2026-10-22 18:17:27 | [CVE-2026-113873](https://nvd.nist.gov/vuln/detail/CVE-2026-113873) | High | 8.7 | SmileCDR HAPI FHIR does not properly handle highly compressed data, allowing an unauthenticated attacker to send compre… |
| 2026-10-22 18:17:27 | [CVE-2026-113874](https://nvd.nist.gov/vuln/detail/CVE-2026-113874) | High | 8.6 | SmileCDR HAPI FHIR allows an untrusted bundle body to replace a partition identity previously established by a trusted… |
| 2026-10-22 18:17:28 | [CVE-2026-114609](https://nvd.nist.gov/vuln/detail/CVE-2026-114609) | Medium | 5.8 | fpdf2 is a PDF creation library for Python. Prior to 2.8.8, fpdf2's shared image loader automatically dereferences atta… |
| 2026-10-22 18:17:28 | [CVE-2026-114610](https://nvd.nist.gov/vuln/detail/CVE-2026-114610) | Medium | 6.5 | fpdf2 is a PDF creation library for Python. From 2.5.0 until 2.8.8, fpdf2's SVGObject.build_xref() passes nested SVG <u… |
| 2026-10-22 18:17:28 | [CVE-2026-114611](https://nvd.nist.gov/vuln/detail/CVE-2026-114611) | Critical | 9.1 | OCO-Server is a self-hosted endpoint management application for computer inventory, software deployment, and mobile dev… |
| 2026-10-22 18:17:28 | [CVE-2026-115516](https://nvd.nist.gov/vuln/detail/CVE-2026-115516) | Medium | 6.9 | An incorrect authorization issue exposes basic account information to unauthorized remote users in KNIME Business Hub S… |
| 2026-10-22 18:17:28 | [CVE-2026-13599](https://nvd.nist.gov/vuln/detail/CVE-2026-13599) | Medium | 5.8 | Missing authentication for critical function vulnerability in ABB Ability Edgenius. This issue affects Ability Edgenius… |
| 2026-10-22 18:17:28 | [CVE-2026-54238](https://nvd.nist.gov/vuln/detail/CVE-2026-54238) | Low | 3.1 | Supabase Realtime provides Broadcast, Presence, and Postgres Changes via WebSockets. Prior to version 2.103.1, the REST… |
| 2026-10-22 18:17:29 | [CVE-2026-54532](https://nvd.nist.gov/vuln/detail/CVE-2026-54532) | Medium | 6.9 | CloudPirates Open Source Helm Charts is a collection of Helm charts. Prior to commit 271d415, pull_request_target workf… |
| 2026-10-22 18:17:29 | [CVE-2026-77156](https://nvd.nist.gov/vuln/detail/CVE-2026-77156) | Medium | 6.3 | Incomplete validation of extracted archive entry paths in ast-cli's tar extraction logic on Linux and macOS (used when… |
| 2026-10-22 18:17:29 | [CVE-2026-77157](https://nvd.nist.gov/vuln/detail/CVE-2026-77157) | Medium | 6.3 | ast-cli downloads two helper binaries, the Vorpal ASCA real-time engine and the SCA Resolver, from "download.checkmarx.… |
| 2026-10-22 18:17:32 | [CVE-2026-93336](https://nvd.nist.gov/vuln/detail/CVE-2026-93336) | High | 7.1 | Missing authorization in the unit resources download route in Canonical Juju 4.0 through 4.0.15 allows a controller-aut… |
| 2026-10-22 18:17:32 | [CVE-2026-97635](https://nvd.nist.gov/vuln/detail/CVE-2026-97635) | High | 8.6 | The Agent Zero Web UI before 1.15 does not correctly sanitize user-provided input in chat messages or file uploads. Whe… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
