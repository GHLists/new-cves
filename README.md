# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 23:19 UTC

New CVEs published between 2026-09-27 22:21 UTC and 2026-09-27 23:19 UTC.

[Full CSV](data/new-cves-2026-09-27T23-19-02-907395Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 23:16:58 | [CVE-2026-100883](https://nvd.nist.gov/vuln/detail/CVE-2026-100883) | Low | 2.1 | A flaw has been found in Krayin laravel-crm up to 2.2.5. The affected element is an unknown function of the file packag… |
| 2026-09-27 23:16:58 | [CVE-2026-100884](https://nvd.nist.gov/vuln/detail/CVE-2026-100884) | Low | 2.1 | A vulnerability has been found in Krayin laravel-crm up to 2.2.5. The impacted element is the function Storage::downloa… |
| 2026-09-27 23:16:58 | [CVE-2026-100885](https://nvd.nist.gov/vuln/detail/CVE-2026-100885) | Medium | 5.5 | A vulnerability was found in Krayin laravel-crm up to 2.2.4. This affects an unknown function of the file packages/Webk… |
| 2026-09-27 23:16:59 | [CVE-2026-100886](https://nvd.nist.gov/vuln/detail/CVE-2026-100886) | Critical | 9.3 | A vulnerability was identified in Seetong T8108, T8108P, T8116 and T8232 4.6.1.4-build202604241011. The affected elemen… |
| 2026-09-27 23:17:01 | [CVE-2026-96284](https://nvd.nist.gov/vuln/detail/CVE-2026-96284) | Low | 2.5 | A malicious user can get read-access to files in the flatpak-system-helper context if a system OCI repository is config… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
