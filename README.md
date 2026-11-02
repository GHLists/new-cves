# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 11:18 UTC

New CVEs published between 2026-11-02 10:18 UTC and 2026-11-02 11:18 UTC.

[Full CSV](data/new-cves-2026-11-02T11-18-13-553543Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 11:17:28 | [CVE-2024-2372](https://nvd.nist.gov/vuln/detail/CVE-2024-2372) | Medium | 5.4 | The affected components accept user-supplied input for constructing redirection URLs without enforcing expected validat… |
| 2026-11-02 11:17:30 | [CVE-2025-12544](https://nvd.nist.gov/vuln/detail/CVE-2025-12544) | Medium | 4.8 | The Publisher portal fails to enforce proper validation on uploaded SVG files, allowing users with the Publisher role t… |
| 2026-11-02 11:17:30 | [CVE-2026-117518](https://nvd.nist.gov/vuln/detail/CVE-2026-117518) | High | 8.2 | @fastify/reply-from is a Fastify plugin that forwards requests to an upstream HTTP server. In versions up to and includ… |
| 2026-11-02 11:17:30 | [CVE-2026-117531](https://nvd.nist.gov/vuln/detail/CVE-2026-117531) | Medium | 5.9 | @fastify/multipart is the multipart form-data and file upload plugin for the Fastify web framework. In versions 5.3.0 t… |
| 2026-11-02 11:17:30 | [CVE-2026-117549](https://nvd.nist.gov/vuln/detail/CVE-2026-117549) | Medium | 4.2 | @fastify/secure-session is a session plugin for Fastify that stores an encrypted session in a cookie. In versions 7.5.0… |
| 2026-11-02 11:17:31 | [CVE-2026-120213](https://nvd.nist.gov/vuln/detail/CVE-2026-120213) | Critical | 9.1 | @fastify/http-proxy is a Fastify plugin that proxies HTTP requests to an upstream server under a configured prefix. In… |
| 2026-11-02 11:17:31 | [CVE-2026-120214](https://nvd.nist.gov/vuln/detail/CVE-2026-120214) | Medium | 5.9 | @fastify/http-proxy is a Fastify plugin that proxies HTTP requests to an upstream server under a configured prefix. In… |
| 2026-11-02 11:17:31 | [CVE-2026-120215](https://nvd.nist.gov/vuln/detail/CVE-2026-120215) | Low | 3.7 | @fastify/cors is the CORS plugin for the Fastify web framework. In versions 8.2.0 through 11.3.x, an application that r… |
| 2026-11-02 11:17:31 | [CVE-2026-120216](https://nvd.nist.gov/vuln/detail/CVE-2026-120216) | Medium | 5.9 | fastify is a web framework for Node.js. In versions 5.8.0 through 5.12.7, when the server is configured with a nonzero… |
| 2026-11-02 11:17:31 | [CVE-2026-2613](https://nvd.nist.gov/vuln/detail/CVE-2026-2613) | High | 8.7 | The Admin REST API accepts user-supplied input without adequately sanitizing it, allowing it to be included in the stru… |
| 2026-11-02 11:17:33 | [CVE-2026-8923](https://nvd.nist.gov/vuln/detail/CVE-2026-8923) | High | 8.7 | Zohocorp ManageEngine Eventlog Analyzer and ManageEngine Log360 versions before 13062 are vulnerable to Authenticated R… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
