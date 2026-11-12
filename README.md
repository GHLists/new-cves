# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 23:19 UTC

New CVEs published between 2026-11-12 22:19 UTC and 2026-11-12 23:19 UTC.

[Full CSV](data/new-cves-2026-11-12T23-19-12-178268Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 22:19:18 | [CVE-2026-126210](https://nvd.nist.gov/vuln/detail/CVE-2026-126210) | Medium | 5.3 | @hono/node-server allows running the Hono application on Node.js. Prior to 1.19.18 and from 2.0.0 until 2.1.6, the serv… |
| 2026-11-12 22:19:19 | [CVE-2026-126343](https://nvd.nist.gov/vuln/detail/CVE-2026-126343) | Medium | 5.3 | @hono/node-server allows running the Hono application on Node.js. From 2.0.0 until 2.1.6, the WebSocket upgrade handler… |
| 2026-11-12 22:19:19 | [CVE-2026-126344](https://nvd.nist.gov/vuln/detail/CVE-2026-126344) | Medium | 5.4 | @hono/node-server allows running the Hono application on Node.js. From 2.0.0 until 2.1.6, the WebSocket upgrade path re… |
| 2026-11-12 22:19:19 | [CVE-2026-126345](https://nvd.nist.gov/vuln/detail/CVE-2026-126345) | Medium | 5.3 | basic-ftp is an FTP client for Node.js. Prior to 6.2.4, the MLSD directory-listing parser in src/parseListMLSD.ts uses… |
| 2026-11-12 22:19:19 | [CVE-2026-126346](https://nvd.nist.gov/vuln/detail/CVE-2026-126346) | Medium | 5.9 | basic-ftp is an FTP client for Node.js. Prior to 6.2.3, FTPContext.send() throws when a command contains carriage retur… |
| 2026-11-12 22:19:19 | [CVE-2026-126347](https://nvd.nist.gov/vuln/detail/CVE-2026-126347) | Low | 3.1 | Tornado is a Python web framework and asynchronous networking library. In versions through 6.6.0, applications using to… |
| 2026-11-12 22:19:19 | [CVE-2026-126348](https://nvd.nist.gov/vuln/detail/CVE-2026-126348) | Medium | 4.3 | Addressable is an alternative implementation to the URI implementation that is part of Ruby's standard library. From 2.… |
| 2026-11-12 22:19:20 | [CVE-2026-126349](https://nvd.nist.gov/vuln/detail/CVE-2026-126349) | Low | 3.1 | Addressable is an alternative implementation to the URI implementation that is part of Ruby's standard library. From 2.… |
| 2026-11-12 22:19:20 | [CVE-2026-126350](https://nvd.nist.gov/vuln/detail/CVE-2026-126350) | Medium | 5.9 | Addressable is an alternative implementation to the URI implementation that is part of Ruby's standard library. From 2.… |
| 2026-11-12 22:19:20 | [CVE-2026-126351](https://nvd.nist.gov/vuln/detail/CVE-2026-126351) | Medium | 5.9 | Addressable is an alternative implementation to the URI implementation that is part of Ruby's standard library. Prior t… |
| 2026-11-12 22:19:20 | [CVE-2026-126352](https://nvd.nist.gov/vuln/detail/CVE-2026-126352) | Medium | 5.9 | Addressable is an alternative implementation to the URI implementation that is part of Ruby's standard library. From 2.… |
| 2026-11-12 22:19:20 | [CVE-2026-126353](https://nvd.nist.gov/vuln/detail/CVE-2026-126353) | Medium | 5.9 | Addressable is an alternative implementation to the URI implementation that is part of Ruby's standard library. From 2.… |
| 2026-11-12 22:19:20 | [CVE-2026-126354](https://nvd.nist.gov/vuln/detail/CVE-2026-126354) | Medium | 4.8 | Addressable is an alternative implementation to the URI implementation that is part of Ruby's standard library. From 2.… |
| 2026-11-12 22:19:21 | [CVE-2026-126823](https://nvd.nist.gov/vuln/detail/CVE-2026-126823) | High | 7.3 | A local user with an ordinary account on the same host can place a file in a shared temporary location that the JDBC dr… |
| 2026-11-12 22:19:21 | [CVE-2026-127209](https://nvd.nist.gov/vuln/detail/CVE-2026-127209) | Medium | 5.1 | Xiaomi Mi Browser Android Application (com.mi.globalbrowser) before 14.66.0-gn contains a path traversal vulnerability… |
| 2026-11-12 22:19:21 | [CVE-2026-127211](https://nvd.nist.gov/vuln/detail/CVE-2026-127211) | High | 7.1 | MultiVendorX plugin for WordPress before 5.0.22 contains a broken access control vulnerability in the /wp-json/multiven… |
| 2026-11-12 22:19:29 | [CVE-2026-91141](https://nvd.nist.gov/vuln/detail/CVE-2026-91141) |  |  | A vulnerability in the default configuration of vsomeip allows a remote, unauthenticated attacker to trigger massive me… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
