# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-26 23:20 UTC

New CVEs published between 2026-10-26 22:18 UTC and 2026-10-26 23:20 UTC.

[Full CSV](data/new-cves-2026-10-26T23-20-06-232597Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-26 23:16:59 | [CVE-2026-116554](https://nvd.nist.gov/vuln/detail/CVE-2026-116554) | Low | 2.0 | A flaw has been found in Argilla up to 2.8.0. The affected element is the function Dataset.from_disk of the file argill… |
| 2026-10-26 23:16:59 | [CVE-2026-116555](https://nvd.nist.gov/vuln/detail/CVE-2026-116555) | Low | 1.9 | A vulnerability has been found in Argilla up to 2.8.0. The impacted element is an unknown function of the file argilla-… |
| 2026-10-26 23:16:59 | [CVE-2026-116556](https://nvd.nist.gov/vuln/detail/CVE-2026-116556) | Low | 1.9 | A vulnerability was found in Argilla up to 2.8.0. This affects an unknown function of the file argilla-frontend/compone… |
| 2026-10-26 23:16:59 | [CVE-2026-116602](https://nvd.nist.gov/vuln/detail/CVE-2026-116602) | Medium | 5.5 | A vulnerability was detected in SourceCodester Online Food Ordering System 1.0. This issue affects the function unlink… |
| 2026-10-26 23:17:00 | [CVE-2026-2270](https://nvd.nist.gov/vuln/detail/CVE-2026-2270) | Medium | 5.9 | A confused deputy attack exists in the StatefulSet controller that allows a user with namespace-scoped write permission… |
| 2026-10-26 23:17:09 | [CVE-2026-76654](https://nvd.nist.gov/vuln/detail/CVE-2026-76654) | Medium | 5.8 | An NTLM coercion vulnerability exists on Windows nodes when the subPath supplied in a pod's volumeMounts is set to a sy… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
