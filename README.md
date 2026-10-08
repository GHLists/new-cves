# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 09:19 UTC

New CVEs published between 2026-10-08 08:18 UTC and 2026-10-08 09:19 UTC.

[Full CSV](data/new-cves-2026-10-08T09-19-36-111999Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 09:16:40 | [CVE-2026-105110](https://nvd.nist.gov/vuln/detail/CVE-2026-105110) | Critical | 9.3 | OS Command Injection in the login.xgi CGI endpoint in Iskratel Innbox GPON ONT devices allows an unauthenticated remote… |
| 2026-10-08 09:16:41 | [CVE-2026-12260](https://nvd.nist.gov/vuln/detail/CVE-2026-12260) | Critical | 10.0 | SQL injection in the NetBoard CRM demo platform; specifically, the vulnerable component is the ‘user-name’ POST paramet… |
| 2026-10-08 09:16:41 | [CVE-2026-4894](https://nvd.nist.gov/vuln/detail/CVE-2026-4894) | Medium | 6.9 | A vulnerability has been identified regarding insufficient validation in the Frappe Cloud/ERPNext authentication proces… |
| 2026-10-08 09:16:41 | [CVE-2026-66082](https://nvd.nist.gov/vuln/detail/CVE-2026-66082) |  |  | An authorization bypass vulnerability in Apache DolphinScheduler allows authenticated users to perform unauthorized ope… |
| 2026-10-08 09:16:41 | [CVE-2026-66084](https://nvd.nist.gov/vuln/detail/CVE-2026-66084) |  |  | An authorization bypass vulnerability in Apache DolphinScheduler allows authenticated users to modify task definitions… |
| 2026-10-08 09:16:41 | [CVE-2026-66087](https://nvd.nist.gov/vuln/detail/CVE-2026-66087) |  |  | An authorization bypass vulnerability in Apache DolphinScheduler allows authenticated users to operate task instance in… |
| 2026-10-08 09:16:42 | [CVE-2026-71183](https://nvd.nist.gov/vuln/detail/CVE-2026-71183) |  |  | An authorization vulnerability in Apache DolphinScheduler allows authenticated users to obtain information about data s… |
| 2026-10-08 09:16:42 | [CVE-2026-71895](https://nvd.nist.gov/vuln/detail/CVE-2026-71895) |  |  | An authorization vulnerability in Apache DolphinScheduler allows authenticated non-admin users to retrieve Kubernetes c… |
| 2026-10-08 09:16:42 | [CVE-2026-71896](https://nvd.nist.gov/vuln/detail/CVE-2026-71896) |  |  | An authorization vulnerability in Apache DolphinScheduler allows authenticated users to retrieve other users' account i… |
| 2026-10-08 09:16:42 | [CVE-2026-89191](https://nvd.nist.gov/vuln/detail/CVE-2026-89191) | Medium | 6.8 | Unsanitised input in the "template name" field of SQLView KRIS's Workflow Template feature is rendered in "onclick" att… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
