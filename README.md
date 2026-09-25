# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-25 03:19 UTC

New CVEs published between 2026-09-25 02:20 UTC and 2026-09-25 03:19 UTC.

[Full CSV](data/new-cves-2026-09-25T03-19-43-665702Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-25 03:16:59 | [CVE-2026-97650](https://nvd.nist.gov/vuln/detail/CVE-2026-97650) | Low | 2.1 | A vulnerability has been found in ningzichun student-management-system up to 98760f5711cf6dc8b4adca53a9e207ca49b02ebf.… |
| 2026-09-25 03:16:59 | [CVE-2026-97724](https://nvd.nist.gov/vuln/detail/CVE-2026-97724) | Medium | 5.3 | A prototype pollution vulnerability in Software Mansion React Native Worklets before 0.12.2 allows an attacker-controll… |
| 2026-09-25 03:16:59 | [CVE-2026-97730](https://nvd.nist.gov/vuln/detail/CVE-2026-97730) | High | 8.5 | In Netgate pfSense Plus before 26.07 and pfSense CE before 2.9.0, a Local File Inclusion (LFI) vulnerability in the Das… |
| 2026-09-25 03:16:59 | [CVE-2026-97731](https://nvd.nist.gov/vuln/detail/CVE-2026-97731) | High | 7.1 | MinIO through 7aac2a2 does not verify that every x-amz-* header present on a request also appears in the client-supplie… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
