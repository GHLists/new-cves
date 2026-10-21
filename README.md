# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 20:18 UTC

New CVEs published between 2026-10-21 19:23 UTC and 2026-10-21 20:18 UTC.

[Full CSV](data/new-cves-2026-10-21T20-18-59-980374Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 20:17:22 | [CVE-2026-111805](https://nvd.nist.gov/vuln/detail/CVE-2026-111805) | High | 7.7 | Apache Traffic Server can be used to exhaust an HTTP/1.1 origin's worker pool via a truncated HTTP/2 Content-Length val… |
| 2026-10-21 20:17:22 | [CVE-2026-111808](https://nvd.nist.gov/vuln/detail/CVE-2026-111808) | High | 7.7 | Apache Traffic Server can be used to exhaust an HTTP/1.1 origin's worker pool via a malformed padded HTTP/2 DATA frame.… |
| 2026-10-21 20:17:22 | [CVE-2026-111809](https://nvd.nist.gov/vuln/detail/CVE-2026-111809) | Medium | 6.9 | Apache Traffic Server allows request smuggling via HEAD requests that carry Content-Length or Transfer-Encoding. This i… |
| 2026-10-21 20:17:22 | [CVE-2026-111810](https://nvd.nist.gov/vuln/detail/CVE-2026-111810) | High | 8.7 | Apache Traffic Server 9.2.15, 10.1.4 and 10.2.0 write one unthrottled diagnostic log line for every internal @ header t… |
| 2026-10-21 20:17:22 | [CVE-2026-111811](https://nvd.nist.gov/vuln/detail/CVE-2026-111811) | Critical | 9.4 | Apache Traffic Server's experimental tsmemcache plugin allows unauthenticated network read, write, and deletion of the… |
| 2026-10-21 20:17:23 | [CVE-2026-111812](https://nvd.nist.gov/vuln/detail/CVE-2026-111812) | High | 7.0 | Apache Traffic Server's origin_server_auth plugin lets a client force signing of attacker-chosen AWS request headers un… |
| 2026-10-21 20:17:23 | [CVE-2026-111814](https://nvd.nist.gov/vuln/detail/CVE-2026-111814) | High | 7.8 | Apache Traffic Server's default outbound session-sharing policy can reuse a pooled TLS session authenticated with one c… |
| 2026-10-21 20:17:23 | [CVE-2026-111815](https://nvd.nist.gov/vuln/detail/CVE-2026-111815) | High | 7.8 | Apache Traffic Server can resume a TLS session across SNI virtual hosts without re-verifying a client certificate requi… |
| 2026-10-21 20:17:23 | [CVE-2026-111817](https://nvd.nist.gov/vuln/detail/CVE-2026-111817) | Medium | 6.9 | Apache Traffic Server can stall a chunked transfer that it passes through with its trailers removed (proxy.config.http.… |
| 2026-10-21 20:17:23 | [CVE-2026-112381](https://nvd.nist.gov/vuln/detail/CVE-2026-112381) | High | 8.2 | Apache Traffic Server can crash with a null pointer dereference when a client POST request is torn down via half-close… |
| 2026-10-21 20:17:23 | [CVE-2026-112408](https://nvd.nist.gov/vuln/detail/CVE-2026-112408) | Critical | 9.4 | Missing verification of source of a communication channel in the default_bucket() function in Amazon SageMaker Python S… |
| 2026-10-21 20:17:25 | [CVE-2026-114135](https://nvd.nist.gov/vuln/detail/CVE-2026-114135) | High | 8.8 | Jupyter Server is the backend for Jupyter web applications. From 2.0.0 until 2.6.0, enabling GatewayClient.url replaced… |
| 2026-10-21 20:17:25 | [CVE-2026-114136](https://nvd.nist.gov/vuln/detail/CVE-2026-114136) | High | 7.5 | Django REST framework is a toolkit for building Web APIs. From 3.6.4 until 3.18.2, JSONParser.parse in rest_framework/p… |
| 2026-10-21 20:17:25 | [CVE-2026-114362](https://nvd.nist.gov/vuln/detail/CVE-2026-114362) | Medium | 5.3 | A flaw has been found in HarnessRouter up to 0.31.12. This impacts an unknown function of the file gateway/app.py of th… |
| 2026-10-21 20:17:25 | [CVE-2026-114374](https://nvd.nist.gov/vuln/detail/CVE-2026-114374) | Low | 2.1 | A vulnerability was identified in leomoon-studios wiki-go up to 1.9.1. This impacts an unknown function of the file int… |
| 2026-10-21 20:17:26 | [CVE-2026-114375](https://nvd.nist.gov/vuln/detail/CVE-2026-114375) | Low | 2.1 | A security flaw has been discovered in leomoon-studios wiki-go up to 1.9.1. Affected is the function RenameFileHandler… |
| 2026-10-21 20:17:26 | [CVE-2026-114376](https://nvd.nist.gov/vuln/detail/CVE-2026-114376) | Low | 2.1 | A weakness has been identified in leomoon-studios wiki-go up to 1.9.1. Affected by this vulnerability is the function S… |
| 2026-10-21 20:17:26 | [CVE-2026-114438](https://nvd.nist.gov/vuln/detail/CVE-2026-114438) | Medium | 4.2 | A flaw was found in the Update User Locale required action of the Keycloak identity and access management solution. Whe… |
| 2026-10-21 20:17:27 | [CVE-2026-85518](https://nvd.nist.gov/vuln/detail/CVE-2026-85518) | Medium | 6.1 | A flaw was found in OpenSCAP. When decomposing a Source DataStream (SDS) file, the application does not properly valida… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
