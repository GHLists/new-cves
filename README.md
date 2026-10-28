# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 15:19 UTC

New CVEs published between 2026-10-28 14:18 UTC and 2026-10-28 15:19 UTC.

[Full CSV](data/new-cves-2026-10-28T15-19-41-204096Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 15:17:02 | [CVE-2026-106971](https://nvd.nist.gov/vuln/detail/CVE-2026-106971) |  |  | An integer overflow in the MessagePack\BufferUnpacker component of rybakit/msgpack v0.11.0 allows attackers to cause a… |
| 2026-10-28 15:17:02 | [CVE-2026-106972](https://nvd.nist.gov/vuln/detail/CVE-2026-106972) |  |  | An uncontrolled recursion in the MessagePack\BufferUnpacker::unpack() component of rybakit/msgpack v0.11.0 allows attac… |
| 2026-10-28 15:17:04 | [CVE-2026-115402](https://nvd.nist.gov/vuln/detail/CVE-2026-115402) | Medium | 5.7 | OpenVPN ovpn-dco-win 0.6.5 through 2.8.13 allows unprivileged local users to cause a denial of service (system crash) v… |
| 2026-10-28 15:17:10 | [CVE-2026-93518](https://nvd.nist.gov/vuln/detail/CVE-2026-93518) | High | 7.8 | An integer truncation issue in XkbResizeKeyType() that could lead to a heap buffer overflow by authenticated X clients… |
| 2026-10-28 15:17:10 | [CVE-2026-93519](https://nvd.nist.gov/vuln/detail/CVE-2026-93519) | High | 7.8 | A buffer overflow when handling pointer barriers in the XFIXES extension in X.Org X server before 21.1.25 and XWayland… |
| 2026-10-28 15:17:10 | [CVE-2026-93520](https://nvd.nist.gov/vuln/detail/CVE-2026-93520) | High | 7.8 | A heap buffer overflow caused by mismatching size calculations between XkbAllocNames and ChangeKeycodeRange in X.org X… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
