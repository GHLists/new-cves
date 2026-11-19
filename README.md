# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 09:22 UTC

New CVEs published between 2026-11-19 08:19 UTC and 2026-11-19 09:22 UTC.

[Full CSV](data/new-cves-2026-11-19T09-22-38-128648Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 09:17:37 | [CVE-2026-101167](https://nvd.nist.gov/vuln/detail/CVE-2026-101167) | Medium | 6.5 | Missing Authorization vulnerability in Dataprom Bilişim Teknolojileri LTD. ŞTİ. DataPer Access Control and Security Sys… |
| 2026-11-19 09:17:43 | [CVE-2026-132043](https://nvd.nist.gov/vuln/detail/CVE-2026-132043) | Medium | 6.3 | In Eclipse Yasson versions 3.0 to 3.0.5, a race condition (CWE-362) exists in the handling of @JsonbNumberFormat. Yasso… |
| 2026-11-19 09:18:18 | [CVE-2026-99320](https://nvd.nist.gov/vuln/detail/CVE-2026-99320) |  |  | In the Linux kernel, the following vulnerability has been resolved: ipv6: raw: fix use-after-free in rawv6_send_hdrinc(… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
