# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 05:19 UTC

New CVEs published between 2026-11-01 04:18 UTC and 2026-11-01 05:19 UTC.

[Full CSV](data/new-cves-2026-11-01T05-19-55-985307Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 04:18:46 | [CVE-2026-120195](https://nvd.nist.gov/vuln/detail/CVE-2026-120195) | Critical | 9.3 | A security vulnerability has been detected in WAVLINK WL-WN579A3-A 2026-03-10-94f93d4. The impacted element is the func… |
| 2026-11-01 04:18:46 | [CVE-2026-120196](https://nvd.nist.gov/vuln/detail/CVE-2026-120196) | High | 8.6 | A vulnerability was detected in WAVLINK WN579X3-D V250402. This affects the function port_forward of the file /cgi-bin/… |
| 2026-11-01 04:18:47 | [CVE-2026-120197](https://nvd.nist.gov/vuln/detail/CVE-2026-120197) | High | 8.6 | A flaw has been found in WAVLINK WL-WN530HG4B M_V260724. This impacts the function port_forward of the file /cgi-bin/wa… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
