# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-13 12:18 UTC

New CVEs published between 2026-10-13 11:20 UTC and 2026-10-13 12:18 UTC.

[Full CSV](data/new-cves-2026-10-13T12-18-36-073876Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-13 12:17:13 | [CVE-2026-109189](https://nvd.nist.gov/vuln/detail/CVE-2026-109189) | Low | 2.1 | A vulnerability was detected in fit2cloud MeterSphere up to 3.6.9-lts. The affected element is the function Swagger3Par… |
| 2026-10-13 12:17:13 | [CVE-2026-109190](https://nvd.nist.gov/vuln/detail/CVE-2026-109190) | Low | 2.1 | A vulnerability has been found in conductor-oss conductor 3.31.2. This affects the function ListApiToolsTask.start of t… |
| 2026-10-13 12:17:13 | [CVE-2026-109402](https://nvd.nist.gov/vuln/detail/CVE-2026-109402) | Low | 2.1 | A vulnerability was found in conductor-oss conductor 3.22.0. Affected is the function MCPService.listTools of the file… |
| 2026-10-13 12:17:14 | [CVE-2026-109832](https://nvd.nist.gov/vuln/detail/CVE-2026-109832) | High | 7.5 | A flaw was found in gnome-remote-desktop as shipped in Red Hat Enterprise Linux. In the VNC TLS I/O handlers, retryable… |
| 2026-10-13 12:17:14 | [CVE-2026-63316](https://nvd.nist.gov/vuln/detail/CVE-2026-63316) | High | 8.7 | A SQL injection vulnerability has been identified in Payload CMS. Improper neutralization of input provided by user int… |
| 2026-10-13 12:17:15 | [CVE-2026-89279](https://nvd.nist.gov/vuln/detail/CVE-2026-89279) | Medium | 6.5 | Cross-Site request forgery (CSRF) vulnerability in AuthTake Technology Inc. Authtake allows Encryption Brute Forcing. T… |
| 2026-10-13 12:17:15 | [CVE-2026-94410](https://nvd.nist.gov/vuln/detail/CVE-2026-94410) | Medium | 5.3 | A low privileged remote attacker is able to view a list of roles that should only be accessible to administrators. This… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
