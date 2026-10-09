# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 19:18 UTC

New CVEs published between 2026-10-09 18:19 UTC and 2026-10-09 19:18 UTC.

[Full CSV](data/new-cves-2026-10-09T19-18-37-73871Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 19:16:42 | [CVE-2026-75351](https://nvd.nist.gov/vuln/detail/CVE-2026-75351) |  |  | OpENer v2.3/commit 76b95cf, contains an out-of-bounds read in the server-side EtherNet/IP ForwardOpen connection-path p… |
| 2026-10-09 19:16:42 | [CVE-2026-75352](https://nvd.nist.gov/vuln/detail/CVE-2026-75352) |  |  | OpENer v2.3/commit 76b95cf, contains an integer underflow in the server-side EtherNet/IP ForwardOpen connection-path pa… |
| 2026-10-09 19:16:42 | [CVE-2026-75353](https://nvd.nist.gov/vuln/detail/CVE-2026-75353) |  |  | OpENer v2.3/ commit 76b95cf, contains an out-of-bounds read in the server-side EtherNet/IP ForwardOpen connection-path… |
| 2026-10-09 19:16:42 | [CVE-2026-78835](https://nvd.nist.gov/vuln/detail/CVE-2026-78835) |  |  | Rocket Software Rocket Remote Desktop 18.0.8583.1 is vulnerable to Insufficiently Protected Credentials. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
