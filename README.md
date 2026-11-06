# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 22:19 UTC

New CVEs published between 2026-11-06 21:18 UTC and 2026-11-06 22:19 UTC.

[Full CSV](data/new-cves-2026-11-06T22-19-25-722177Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 22:17:49 | [CVE-2026-103022](https://nvd.nist.gov/vuln/detail/CVE-2026-103022) | Medium | 5.3 | Urwid is a console user interface library for Python. Prior to 4.0.7, handle_short_request() in urwid/display/web.py pe… |
| 2026-11-06 22:17:50 | [CVE-2026-104254](https://nvd.nist.gov/vuln/detail/CVE-2026-104254) | Medium | 5.3 | liboqs is a C-language cryptographic library that provides implementations of post-quantum cryptography algorithms. Fro… |
| 2026-11-06 22:17:50 | [CVE-2026-104267](https://nvd.nist.gov/vuln/detail/CVE-2026-104267) | Medium | 4.1 | Botan is a C++ cryptography library. From 2.7.0 until 3.13.0, Botan's Scrypt implementation on 32-bit platforms compute… |
| 2026-11-06 22:17:50 | [CVE-2026-119800](https://nvd.nist.gov/vuln/detail/CVE-2026-119800) | Medium | 4.3 | Ryot is a self-hosted personal tracking application. Prior to 10.5.6, the collectionContents GraphQL query implemented… |
| 2026-11-06 22:17:50 | [CVE-2026-123788](https://nvd.nist.gov/vuln/detail/CVE-2026-123788) | Medium | 5.3 | A security vulnerability has been detected in chenyme grok2api up to 3.1.6. The impacted element is an unknown function… |
| 2026-11-06 22:17:50 | [CVE-2026-123791](https://nvd.nist.gov/vuln/detail/CVE-2026-123791) | Medium | 5.5 | A vulnerability was detected in OpenBMB Internet of Agents up to 9d78e88e47160eb42ee1ee8538c05e1c2c47877a. This affects… |
| 2026-11-06 22:17:51 | [CVE-2026-44519](https://nvd.nist.gov/vuln/detail/CVE-2026-44519) | Medium | 5.1 | liboqs is a C-language cryptographic library that provides implementations of post-quantum cryptography algorithms. Pri… |
| 2026-11-06 22:17:51 | [CVE-2026-47738](https://nvd.nist.gov/vuln/detail/CVE-2026-47738) | Medium | 5.3 | liboqs is a C-language cryptographic library that provides implementations of post-quantum cryptography algorithms. Pri… |
| 2026-11-06 22:17:53 | [CVE-2026-48057](https://nvd.nist.gov/vuln/detail/CVE-2026-48057) | Low | 2.1 | Botan is a C++ cryptography library. Prior to 3.13.0, Botan's X.509 Distinguished Name decoder flattens the Attribute-V… |
| 2026-11-06 22:17:58 | [CVE-2026-50240](https://nvd.nist.gov/vuln/detail/CVE-2026-50240) | High | 8.8 | A flaw was found in OpenShift Pipelines-as-Code (PAC). PAC does not verify whether the creator of a Repository custom r… |
| 2026-11-06 22:17:59 | [CVE-2026-59104](https://nvd.nist.gov/vuln/detail/CVE-2026-59104) | Critical | 9.3 | UgCS server before 6.2 contains an authentication bypass in the HCI protocol login handler (LoginHandler) exposed on TC… |
| 2026-11-06 22:17:59 | [CVE-2026-68933](https://nvd.nist.gov/vuln/detail/CVE-2026-68933) | High | 7.5 | Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create… |
| 2026-11-06 22:17:59 | [CVE-2026-68935](https://nvd.nist.gov/vuln/detail/CVE-2026-68935) | Critical | 9.1 | Chartbrew is an open-source web application for creating charts from databases and APIs. In versions 4.8.5 through 5.2.… |
| 2026-11-06 22:17:59 | [CVE-2026-69128](https://nvd.nist.gov/vuln/detail/CVE-2026-69128) | Medium | 4.6 | Chartbrew is an open-source web application that can connect directly to databases and APIs and use the data to create… |
| 2026-11-06 22:17:59 | [CVE-2026-77442](https://nvd.nist.gov/vuln/detail/CVE-2026-77442) | Medium | 5.9 | Ryot is a self-hosted personal tracking application. Prior to 10.4.0, the createOrUpdateUserIntegration GraphQL mutatio… |
| 2026-11-06 22:18:00 | [CVE-2026-94618](https://nvd.nist.gov/vuln/detail/CVE-2026-94618) | Medium | 5.4 | FileGator is a multi-user file manager. Prior to 7.15.0, GET /batchdownload in backend/Controllers/DownloadController.p… |
| 2026-11-06 22:18:00 | [CVE-2026-94619](https://nvd.nist.gov/vuln/detail/CVE-2026-94619) | Medium | 5.9 | FileGator is a multi-user file manager. Prior to 7.15.0, POST /upload in backend/Controllers/UploadController.php uses… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
