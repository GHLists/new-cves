# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-26 21:19 UTC

New CVEs published between 2026-09-26 20:19 UTC and 2026-09-26 21:19 UTC.

[Full CSV](data/new-cves-2026-09-26T21-19-13-400189Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-26 21:16:55 | [CVE-2026-72662](https://nvd.nist.gov/vuln/detail/CVE-2026-72662) | Medium | 6.3 | Authorization Bypass Through User-Controlled Key (CWE-639) in Kibana can lead to unauthorized disclosure, modification,… |
| 2026-09-26 21:16:55 | [CVE-2026-72668](https://nvd.nist.gov/vuln/detail/CVE-2026-72668) | High | 7.3 | Unintended Proxy or Intermediary ('Confused Deputy') (CWE-441) in Kibana Agent Builder can lead to privilege escalation… |
| 2026-09-26 21:16:55 | [CVE-2026-78582](https://nvd.nist.gov/vuln/detail/CVE-2026-78582) | Medium | 6.5 | Missing Authorization (CWE-862) in Kibana can lead to unauthorized deletion of data via Exploiting Incorrectly Configur… |
| 2026-09-26 21:16:55 | [CVE-2026-82294](https://nvd.nist.gov/vuln/detail/CVE-2026-82294) | Medium | 6.5 | Uncontrolled Resource Consumption (CWE-400) in Elasticsearch can lead to denial of service via Excessive Allocation (CA… |
| 2026-09-26 21:16:55 | [CVE-2026-82300](https://nvd.nist.gov/vuln/detail/CVE-2026-82300) | Medium | 6.5 | Uncontrolled Resource Consumption (CWE-400) in Elasticsearch can lead to denial of service via Excessive Allocation (CA… |
| 2026-09-26 21:16:56 | [CVE-2026-94396](https://nvd.nist.gov/vuln/detail/CVE-2026-94396) | Medium | 6.5 | Uncontrolled Resource Consumption (CWE-400) in Elasticsearch can lead denial of service via Excessive Allocation (CAPEC… |
| 2026-09-26 21:16:56 | [CVE-2026-94397](https://nvd.nist.gov/vuln/detail/CVE-2026-94397) | Medium | 6.5 | Uncontrolled Resource Consumption (CWE-400) in Elasticsearch can lead denial of service via Excessive Allocation (CAPEC… |
| 2026-09-26 21:16:56 | [CVE-2026-94398](https://nvd.nist.gov/vuln/detail/CVE-2026-94398) | Medium | 6.5 | Uncontrolled Resource Consumption (CWE-400) in Elasticsearch can lead denial of service via Excessive Allocation (CAPEC… |
| 2026-09-26 21:16:56 | [CVE-2026-94399](https://nvd.nist.gov/vuln/detail/CVE-2026-94399) | Medium | 6.5 | Uncontrolled Resource Consumption (CWE-400) in Elasticsearch can lead denial of service via Excessive Allocation (CAPEC… |
| 2026-09-26 21:16:56 | [CVE-2026-94400](https://nvd.nist.gov/vuln/detail/CVE-2026-94400) | Medium | 6.5 | Uncontrolled Resource Consumption (CWE-400) in Kibana can lead denial of service via Excessive Allocation (CAPEC-130) |
| 2026-09-26 21:16:56 | [CVE-2026-94408](https://nvd.nist.gov/vuln/detail/CVE-2026-94408) | Medium | 4.9 | Uncontrolled Resource Consumption (CWE-400) in Elasticsearch can lead denial of service via Excessive Allocation (CAPEC… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
