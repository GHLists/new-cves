# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 11:18 UTC

New CVEs published between 2026-11-16 10:18 UTC and 2026-11-16 11:18 UTC.

[Full CSV](data/new-cves-2026-11-16T11-18-19-300334Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 11:16:45 | [CVE-2026-129784](https://nvd.nist.gov/vuln/detail/CVE-2026-129784) | High | 8.5 | The httpx Ruby gem parses JSON response bodies through its transcoder layer. HTTPX::Response#json delegates to Transcod… |
| 2026-11-16 11:16:46 | [CVE-2026-63245](https://nvd.nist.gov/vuln/detail/CVE-2026-63245) | High | 7.3 | A local privilege escalation (LPE) vulnerability in the Audigy Rx driver’s Emupia2k.sys file could allow a local attack… |
| 2026-11-16 11:16:46 | [CVE-2026-85240](https://nvd.nist.gov/vuln/detail/CVE-2026-85240) | Medium | 6.5 | Mattermost Desktop App versions <=6.3 6.0.3 6.3.2.0 fail to handle filesystem errors that can occur when finalizing cer… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
