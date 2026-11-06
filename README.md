# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 16:18 UTC

New CVEs published between 2026-11-06 15:18 UTC and 2026-11-06 16:18 UTC.

[Full CSV](data/new-cves-2026-11-06T16-18-46-776199Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 16:17:37 | [CVE-2026-111573](https://nvd.nist.gov/vuln/detail/CVE-2026-111573) | Medium | 6.3 | Incorrect permissions on the Checkmk Windows agent's data directory, caused by a race condition that discards the permi… |
| 2026-11-06 16:17:52 | [CVE-2026-121623](https://nvd.nist.gov/vuln/detail/CVE-2026-121623) | High | 8.2 | The Symfony Serializer component DataUriNormalizer::denormalize() matches the data: scheme with a case-sensitive regula… |
| 2026-11-06 16:17:52 | [CVE-2026-121880](https://nvd.nist.gov/vuln/detail/CVE-2026-121880) | Medium | 4.7 | Authorization bypass through user-controlled key in the localhost port-proxy (/p/<token>/) in Posit Software, PBC RStud… |
| 2026-11-06 16:17:53 | [CVE-2026-121881](https://nvd.nist.gov/vuln/detail/CVE-2026-121881) | Medium | 5.7 | SQL injection vulnerability in the get_last_seen code-server session-state RPC in Posit Software, PBC Posit Workbench b… |
| 2026-11-06 16:17:54 | [CVE-2026-123623](https://nvd.nist.gov/vuln/detail/CVE-2026-123623) | High | 8.2 | Grida through 0.0.24 contains a missing authorization vulnerability in the Forms file-preview API routes that allows un… |
| 2026-11-06 16:17:54 | [CVE-2026-123675](https://nvd.nist.gov/vuln/detail/CVE-2026-123675) | Medium | 5.5 | A flaw has been found in OpenBMB Internet of Agents up to 9d78e88e47160eb42ee1ee8538c05e1c2c47877a. This affects the fu… |
| 2026-11-06 16:17:54 | [CVE-2026-123676](https://nvd.nist.gov/vuln/detail/CVE-2026-123676) | Medium | 5.5 | A vulnerability has been found in xxyopen/201206030 novel up to 3.5.0. This impacts the function BookServiceImpl.getBoo… |
| 2026-11-06 16:17:55 | [CVE-2026-123677](https://nvd.nist.gov/vuln/detail/CVE-2026-123677) | Low | 2.1 | A vulnerability was found in xxyopen/201206030 novel up to 3.5.0. Affected is the function getBookChapter of the file s… |
| 2026-11-06 16:17:55 | [CVE-2026-123792](https://nvd.nist.gov/vuln/detail/CVE-2026-123792) | High | 8.7 | The Symfony Yaml components Inline and Parser, parse some YAML documents inefficiently, so that a small crafted documen… |
| 2026-11-06 16:17:55 | [CVE-2026-12067](https://nvd.nist.gov/vuln/detail/CVE-2026-12067) |  |  | Missing exception handlers in AvastSvc native message dispatcher (ashServ.dll) on Windows allow a local, unprivileged a… |
| 2026-11-06 16:17:56 | [CVE-2026-21834](https://nvd.nist.gov/vuln/detail/CVE-2026-21834) | Low | 3.1 | HCL AION is affected by a vulnerability where the Content-Security-Policy (CSP) security response header was missing fr… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
