# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-27 06:18 UTC

New CVEs published between 2026-11-27 05:20 UTC and 2026-11-27 06:18 UTC.

[Full CSV](data/new-cves-2026-11-27T06-18-55-510095Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-27 06:17:08 | [CVE-2026-124802](https://nvd.nist.gov/vuln/detail/CVE-2026-124802) |  |  | The Dilemma Lite WordPress plugin through 1.1.1 does not sanitise or escape the choices of dilemmas submitted by visito… |
| 2026-11-27 06:17:08 | [CVE-2026-125627](https://nvd.nist.gov/vuln/detail/CVE-2026-125627) | Medium | 6.5 | A **NULL pointer dereference** flaw has been found in the vlv_value_compare() function in vlv_pagination.c of the Virtu… |
| 2026-11-27 06:17:08 | [CVE-2026-137685](https://nvd.nist.gov/vuln/detail/CVE-2026-137685) | Low | 1.9 | A weakness has been identified in WazirX App up to 4.4.2 on Android. This impacts an unknown function. Executing a mani… |
| 2026-11-27 06:17:09 | [CVE-2026-137687](https://nvd.nist.gov/vuln/detail/CVE-2026-137687) | Medium | 6.9 | A security vulnerability has been detected in WOW-CMS BlizzCMS up to 1.2.1. Affected is the function Home::setconfig of… |
| 2026-11-27 06:17:09 | [CVE-2026-137689](https://nvd.nist.gov/vuln/detail/CVE-2026-137689) | Medium | 6.9 | A vulnerability was detected in bayang jelu up to 0.88.2. Affected by this vulnerability is the function addResourceHan… |
| 2026-11-27 06:17:09 | [CVE-2026-137721](https://nvd.nist.gov/vuln/detail/CVE-2026-137721) | Critical | 10.0 | A vulnerability in the Platform component of Mitel OpenScape 4000 and OpenScape 4000 Manager could allow an attacker to… |
| 2026-11-27 06:17:09 | [CVE-2026-137723](https://nvd.nist.gov/vuln/detail/CVE-2026-137723) | Critical | 9.6 | A vulnerability in the Platform component of Mitel OpenScape 4000 and OpenScape 4000 Manager could allow an attacker to… |
| 2026-11-27 06:17:09 | [CVE-2026-137724](https://nvd.nist.gov/vuln/detail/CVE-2026-137724) | Critical | 10.0 | A vulnerability in the Platform component of Mitel OpenScape 4000, and OpenScape 4000 Manager could allow an unauthenti… |
| 2026-11-27 06:17:09 | [CVE-2026-137738](https://nvd.nist.gov/vuln/detail/CVE-2026-137738) | Critical | 9.8 | In RealVNC Server before 7.19.1, UDP-based connections could potentially be exploited without authentication to execute… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
