# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-31 21:18 UTC

New CVEs published between 2026-10-31 20:18 UTC and 2026-10-31 21:18 UTC.

[Full CSV](data/new-cves-2026-10-31T21-18-59-485954Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-31 21:16:53 | [CVE-2026-118636](https://nvd.nist.gov/vuln/detail/CVE-2026-118636) | Critical | 9.8 | **UNSUPPORTED WHEN ASSIGNED** JavaNativeMessageDecoder in the MINA 3.0 codec module calls ObjectInputStream.readObject(… |
| 2026-10-31 21:16:53 | [CVE-2026-120135](https://nvd.nist.gov/vuln/detail/CVE-2026-120135) | High | 8.2 | Uncontrolled Recursion vulnerability in Apache Thrift Java bindings. This issue affects Apache Thrift: before 0.24.0. U… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
