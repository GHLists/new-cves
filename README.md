# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 01:20 UTC

New CVEs published between 2026-10-28 00:19 UTC and 2026-10-28 01:20 UTC.

[Full CSV](data/new-cves-2026-10-28T01-20-52-97827Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 01:16:55 | [CVE-2026-110747](https://nvd.nist.gov/vuln/detail/CVE-2026-110747) | High | 7.5 | ProtobufParser._readStringKey() reads the length prefix of a protobuf map entry's string key into an attacker-controlle… |
| 2026-10-28 01:16:55 | [CVE-2026-110879](https://nvd.nist.gov/vuln/detail/CVE-2026-110879) | Critical | 9.8 | jackson-databind validates the outer class of a class-name type ID but accepts attacker-selected classes inside its gen… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
