# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 09:18 UTC

New CVEs published between 2026-11-12 08:18 UTC and 2026-11-12 09:18 UTC.

[Full CSV](data/new-cves-2026-11-12T09-18-42-578252Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 09:16:39 | [CVE-2026-110003](https://nvd.nist.gov/vuln/detail/CVE-2026-110003) | Critical | 9.3 | A vulnerability in the administration REST interface of Azul Payara allows a remote, unauthenticated attacker to bypass… |
| 2026-11-12 09:16:40 | [CVE-2026-126642](https://nvd.nist.gov/vuln/detail/CVE-2026-126642) | Medium | 6.5 | An incorrect authorization flaw was found in AWX, the automation controller component of Red Hat Ansible Automation Pla… |
| 2026-11-12 09:16:40 | [CVE-2026-90908](https://nvd.nist.gov/vuln/detail/CVE-2026-90908) | Critical | 9.3 | A vulnerability in the GenericAdminAuthenticator component of Azul Payara Server and Azul Payara Micro allows a remote,… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
