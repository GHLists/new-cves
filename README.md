# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-26 21:18 UTC

New CVEs published between 2026-11-26 20:19 UTC and 2026-11-26 21:18 UTC.

[Full CSV](data/new-cves-2026-11-26T21-18-45-19127Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-26 21:17:15 | [CVE-2026-126139](https://nvd.nist.gov/vuln/detail/CVE-2026-126139) | Medium | 5.3 | Docker Sandboxes re-resolves saved mount paths when replacing a sandbox container during kit changes or restarting a sa… |
| 2026-11-26 21:17:15 | [CVE-2026-137618](https://nvd.nist.gov/vuln/detail/CVE-2026-137618) | Low | 1.9 | A vulnerability was identified in RT-Thread up to 5.3.0. This impacts the function hpm_adc_enabled of the file bsp/hpmi… |
| 2026-11-26 21:17:16 | [CVE-2026-137620](https://nvd.nist.gov/vuln/detail/CVE-2026-137620) | Medium | 5.2 | A security flaw has been discovered in RT-Thread up to 5.3.0. Affected is the function davinci_spi_get_prescale of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
