# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 00:19 UTC

New CVEs published between 2026-10-27 23:18 UTC and 2026-10-28 00:19 UTC.

[Full CSV](data/new-cves-2026-10-28T00-19-16-769592Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 00:17:10 | [CVE-2026-104016](https://nvd.nist.gov/vuln/detail/CVE-2026-104016) | High | 7.5 | ProtobufParser parses length-prefixed protobuf string and bytes fields by checking (_inputPtr + len) <= _inputEnd and t… |
| 2026-10-28 00:17:11 | [CVE-2026-104895](https://nvd.nist.gov/vuln/detail/CVE-2026-104895) | High | 7.5 | The asynchronous Smile parser (NonBlockingByteArrayParser) uses a raw-binary length prefix taken from untrusted input t… |
| 2026-10-28 00:17:11 | [CVE-2026-118129](https://nvd.nist.gov/vuln/detail/CVE-2026-118129) | Low | 2.1 | A vulnerability was found in jeremyckahn Chitchatter up to f82538633813c854a81a8b2112a2f6ba17b39cbc. The affected eleme… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
