# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 02:22 UTC

New CVEs published between 2026-10-08 01:20 UTC and 2026-10-08 02:22 UTC.

[Full CSV](data/new-cves-2026-10-08T02-22-24-186775Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 02:16:53 | [CVE-2026-102488](https://nvd.nist.gov/vuln/detail/CVE-2026-102488) | High | 8.7 | In affected versions, Octopus Server incorrectly evaluates multiple scoped permission assignments, allowing a highly pr… |
| 2026-10-08 02:16:54 | [CVE-2026-82627](https://nvd.nist.gov/vuln/detail/CVE-2026-82627) | High | 7.5 | The Uncanny Automator – AI + Automation for WordPress \| AI Agent, AI Page Builder, Free AI Usage Included plugin for Wo… |
| 2026-10-08 02:16:54 | [CVE-2026-87682](https://nvd.nist.gov/vuln/detail/CVE-2026-87682) | High | 8.6 | Multiple OS Command Injection vulnerabilities exist in the management interface and session processing routines of Broc… |
| 2026-10-08 02:16:54 | [CVE-2026-87683](https://nvd.nist.gov/vuln/detail/CVE-2026-87683) | High | 8.6 | Multiple stack-based buffer overflow vulnerabilities exist in the REST API management component of Brocade Fabric OS ve… |
| 2026-10-08 02:16:54 | [CVE-2026-87726](https://nvd.nist.gov/vuln/detail/CVE-2026-87726) | Low | 3.9 | Insufficient API bounds checking in phalFelica in NXP NXPNfcRdLib RC663 through 07.14.00_Pub may allow an attacker with… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
