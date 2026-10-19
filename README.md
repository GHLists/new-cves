# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-19 12:18 UTC

New CVEs published between 2026-10-19 11:18 UTC and 2026-10-19 12:18 UTC.

[Full CSV](data/new-cves-2026-10-19T12-18-59-149828Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-19 12:17:00 | [CVE-2026-112107](https://nvd.nist.gov/vuln/detail/CVE-2026-112107) | Low | 2.1 | A flaw has been found in ztxz16 fastllm up to 1.8.2. Affected by this issue is the function SafeTensorItem::CreateBuffe… |
| 2026-10-19 12:17:01 | [CVE-2026-112108](https://nvd.nist.gov/vuln/detail/CVE-2026-112108) | Low | 2.1 | A vulnerability was determined in ztxz16 fastllm up to 0.1.8.2. This impacts the function GGUFBuffer::ReadString of the… |
| 2026-10-19 12:17:01 | [CVE-2026-112138](https://nvd.nist.gov/vuln/detail/CVE-2026-112138) | Low | 2.0 | A flaw has been found in diem-project diem up to 5.1.3. The impacted element is the function dmOs::join of the file dmF… |
| 2026-10-19 12:17:01 | [CVE-2026-112139](https://nvd.nist.gov/vuln/detail/CVE-2026-112139) | Medium | 5.5 | A vulnerability has been found in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a… |
| 2026-10-19 12:17:01 | [CVE-2026-112140](https://nvd.nist.gov/vuln/detail/CVE-2026-112140) | Low | 2.1 | A vulnerability was found in llSourcell Doctor-Dignity up to 3f2ffb6c892f13b50a708d05900d3227acb40ded. This impacts the… |
| 2026-10-19 12:17:01 | [CVE-2026-112210](https://nvd.nist.gov/vuln/detail/CVE-2026-112210) | Medium | 6.0 | A flaw was found in the rhc-canonical-facts.service systemd unit shipped with rhc. The service runs as root and operate… |
| 2026-10-19 12:17:11 | [CVE-2026-88900](https://nvd.nist.gov/vuln/detail/CVE-2026-88900) | High | 8.8 | Deserialization of Untrusted Data vulnerability in Apache Camel Camel-Jgroups component. This issue affects Apache Came… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
