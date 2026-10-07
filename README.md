# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 06:22 UTC

New CVEs published between 2026-10-07 05:19 UTC and 2026-10-07 06:22 UTC.

[Full CSV](data/new-cves-2026-10-07T06-22-07-258448Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 06:16:33 | [CVE-2026-102173](https://nvd.nist.gov/vuln/detail/CVE-2026-102173) | High | 7.2 | The Kirki – Freeform Page Builder, Website Builder & Customizer plugin for WordPress is vulnerable to Stored Cross-Site… |
| 2026-10-07 06:16:35 | [CVE-2026-103869](https://nvd.nist.gov/vuln/detail/CVE-2026-103869) | Medium | 6.5 | A flaw was found in pulp-ansible's bearer-token refresh for collection remotes. The access token is kept in one module-… |
| 2026-10-07 06:16:35 | [CVE-2026-103870](https://nvd.nist.gov/vuln/detail/CVE-2026-103870) | Medium | 5.0 | A flaw was found in pulp-rpm when it publishes a distribution tree. Addon and variant ids from .treeinfo are used as di… |
| 2026-10-07 06:16:35 | [CVE-2026-59346](https://nvd.nist.gov/vuln/detail/CVE-2026-59346) | Critical | 9.3 | VMware Workstation and Fusion contain an integer-overflow vulnerability. A malicious actor with local administrative pr… |
| 2026-10-07 06:16:35 | [CVE-2026-59347](https://nvd.nist.gov/vuln/detail/CVE-2026-59347) | High | 8.1 | VMware Workstation and Fusion contain a stack-based buffer-overflow vulnerability in HGFS. A malicious actor with local… |
| 2026-10-07 06:16:35 | [CVE-2026-103868](https://nvd.nist.gov/vuln/detail/CVE-2026-103868) | Medium | 6.5 | A flaw was found in pulp-container when it authenticates to an upstream registry. Basic and bearer credentials from one… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
