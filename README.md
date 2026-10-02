# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 20:18 UTC

New CVEs published between 2026-10-02 19:20 UTC and 2026-10-02 20:18 UTC.

[Full CSV](data/new-cves-2026-10-02T20-18-36-254386Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 20:16:59 | [CVE-2026-103036](https://nvd.nist.gov/vuln/detail/CVE-2026-103036) | Medium | 6.5 | oRPC is a tool that helps build APIs that are end-to-end type-safe and adhere to OpenAPI standards. Prior to 1.14.9, th… |
| 2026-10-02 20:17:00 | [CVE-2026-103918](https://nvd.nist.gov/vuln/detail/CVE-2026-103918) | Medium | 6.5 | oRPC is a tool that helps build APIs that are end-to-end type-safe and adhere to OpenAPI standards. Prior to 1.14.10, t… |
| 2026-10-02 20:17:00 | [CVE-2026-104019](https://nvd.nist.gov/vuln/detail/CVE-2026-104019) | Critical | 9.3 | OS command injection in the Studio Space startup validation script in Amazon SageMaker Distribution 2.x before 2.14.12,… |
| 2026-10-02 20:17:00 | [CVE-2026-104871](https://nvd.nist.gov/vuln/detail/CVE-2026-104871) | Medium | 6.3 | The Angular SSR is a server-rise rendering tool for Angular applications. Prior to versions 20.3.36, 21.2.23, and 22.1.… |
| 2026-10-02 20:17:01 | [CVE-2026-104872](https://nvd.nist.gov/vuln/detail/CVE-2026-104872) | Medium | 5.8 | OpenTelemetry JavaScript Contrib provides instrumentation libraries for collecting telemetry from JavaScript applicatio… |
| 2026-10-02 20:17:01 | [CVE-2026-104873](https://nvd.nist.gov/vuln/detail/CVE-2026-104873) | High | 7.6 | LangGraph Python SDK is used to connect to running LangGraph API servers, manage assistants, threads and stream runs fr… |
| 2026-10-02 20:17:01 | [CVE-2026-104988](https://nvd.nist.gov/vuln/detail/CVE-2026-104988) | High | 8.1 | A flaw was found in Dogtag PKI (pki-core). The CMCAuthForEST authentication plugin fails open when an EST fullcmc enrol… |
| 2026-10-02 20:17:01 | [CVE-2026-104991](https://nvd.nist.gov/vuln/detail/CVE-2026-104991) | High | 7.1 | Phproject before 1.8.7 contains a missing object-level authorization vulnerability in the REST API issue endpoints (sin… |
| 2026-10-02 20:17:01 | [CVE-2026-104994](https://nvd.nist.gov/vuln/detail/CVE-2026-104994) | Low | 2.5 | Trivy before 0.71.0 allows directory traversal in Terraform filesystem functions when they try to access pathnames abov… |
| 2026-10-02 20:17:01 | [CVE-2026-12392](https://nvd.nist.gov/vuln/detail/CVE-2026-12392) | Medium | 5.3 | An information exposure vulnerability in Canonical MAAS prior to versions 3.4.10, 3.5.14, 3.6.5, 3.7.3, and 3.8.0 allow… |
| 2026-10-02 20:17:02 | [CVE-2026-39718](https://nvd.nist.gov/vuln/detail/CVE-2026-39718) | High | 8.8 | Cross-Site Request Forgery (CSRF) vulnerability in Webriti Wallstreet wallstreet allows Cross Site Request Forgery.This… |
| 2026-10-02 20:17:04 | [CVE-2026-82039](https://nvd.nist.gov/vuln/detail/CVE-2026-82039) | High | 8.7 | UTMStack before 11.2.16 contains a SQL injection vulnerability in UtmAssetGroupService.searchQueryBuilder() that allows… |
| 2026-10-02 20:17:04 | [CVE-2026-82040](https://nvd.nist.gov/vuln/detail/CVE-2026-82040) | Medium | 5.3 | UTMStack before 11.2.16 contains a server-side request forgery vulnerability in IdentityProviderService.validateMetadat… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
