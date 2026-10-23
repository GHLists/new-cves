# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 17:20 UTC

New CVEs published between 2026-10-23 16:18 UTC and 2026-10-23 17:20 UTC.

[Full CSV](data/new-cves-2026-10-23T17-20-52-951331Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 17:17:19 | [CVE-2026-105481](https://nvd.nist.gov/vuln/detail/CVE-2026-105481) | Medium | 6.5 | A flaw in Node.js HTTP Agent connection reuse can cause a client to accept as valid a response that was sent before the… |
| 2026-10-23 17:17:19 | [CVE-2026-105482](https://nvd.nist.gov/vuln/detail/CVE-2026-105482) | High | 7.4 | A flaw in Node.js DNS resolution allows hostnames containing a NUL byte to be silently truncated by the dns.resolve*()… |
| 2026-10-23 17:17:19 | [CVE-2026-105483](https://nvd.nist.gov/vuln/detail/CVE-2026-105483) | High | 7.4 | A flaw in Node.js TLS hostname verification allows a certificate without a matching IP address SAN to authenticate a co… |
| 2026-10-23 17:17:19 | [CVE-2026-106069](https://nvd.nist.gov/vuln/detail/CVE-2026-106069) | High | 7.4 | A flaw in Node.js TLS hostname verification can cause a server certificate to be validated against a different IP addre… |
| 2026-10-23 17:17:19 | [CVE-2026-106070](https://nvd.nist.gov/vuln/detail/CVE-2026-106070) | Low | 3.7 | A flaw in the Node.js `zlib.ZipFile` API can cause it to return bytes that do not belong to the requested entry after t… |
| 2026-10-23 17:17:20 | [CVE-2026-106071](https://nvd.nist.gov/vuln/detail/CVE-2026-106071) | Low | 3.6 | A flaw in Node.js Permission Model filesystem enforcement can grant access to paths that do not match a wildcard `--all… |
| 2026-10-23 17:17:20 | [CVE-2026-106072](https://nvd.nist.gov/vuln/detail/CVE-2026-106072) | Medium | 6.7 | A flaw in Node.js TLS hostname verification allows a certificate with only a DNS SAN to authenticate an IP endpoint whe… |
| 2026-10-23 17:17:20 | [CVE-2026-106073](https://nvd.nist.gov/vuln/detail/CVE-2026-106073) | Low | 3.3 | A flaw in Node.js Permission Model filesystem enforcement leaves `fs.realpathSync()` without the required read permissi… |
| 2026-10-23 17:17:20 | [CVE-2026-106074](https://nvd.nist.gov/vuln/detail/CVE-2026-106074) | Medium | 4.8 | A flaw in Node.js `crypto` causes the internal entropy caches used by `crypto.randomUUID()`, `crypto.randomUUIDv7()`, a… |
| 2026-10-23 17:17:21 | [CVE-2026-115810](https://nvd.nist.gov/vuln/detail/CVE-2026-115810) | Medium | 6.3 | Tandoor Recipes before 2.7.0 contains a server-side request forgery vulnerability in the Pestle importer that allows au… |
| 2026-10-23 17:17:22 | [CVE-2026-87901](https://nvd.nist.gov/vuln/detail/CVE-2026-87901) | High | 8.3 | Improper sanitization in the registration module allows reflected Cross-Site Scripting. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
