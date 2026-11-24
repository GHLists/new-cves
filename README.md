# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 11:18 UTC

New CVEs published between 2026-11-24 10:18 UTC and 2026-11-24 11:18 UTC.

[Full CSV](data/new-cves-2026-11-24T11-18-32-218693Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 11:17:05 | [CVE-2026-108368](https://nvd.nist.gov/vuln/detail/CVE-2026-108368) |  |  | Missing authorization in the workflow compiling service of Apache Texera allows a logged-in user to read the column nam… |
| 2026-11-24 11:17:06 | [CVE-2026-108765](https://nvd.nist.gov/vuln/detail/CVE-2026-108765) |  |  | Missing authorization in the workflow export service of Apache Texera allows a logged-in user to potentially read the r… |
| 2026-11-24 11:17:06 | [CVE-2026-112788](https://nvd.nist.gov/vuln/detail/CVE-2026-112788) |  |  | Missing Authentication for Critical Function in Apache Texera (incubating). The Python virtual environment (PVE) manage… |
| 2026-11-24 11:17:08 | [CVE-2026-124829](https://nvd.nist.gov/vuln/detail/CVE-2026-124829) | Medium | 6.3 | Stored Cross-Site Scripting (XSS) in 'carta_presentacion[contenido]' field in the POST request to '/personas/{persona_i… |
| 2026-11-24 11:17:08 | [CVE-2026-124830](https://nvd.nist.gov/vuln/detail/CVE-2026-124830) | Medium | 6.3 | Uploading PDF files with active content to the languages form. The POST endpoint ‘/people/{person_id}/languages’ checks… |
| 2026-11-24 11:17:08 | [CVE-2026-124831](https://nvd.nist.gov/vuln/detail/CVE-2026-124831) | Medium | 6.3 | Stored Cross-Site Scripting (XSS) in 'experiencia_laboral[descripcion]' field in the POST request to '/personas/{person… |
| 2026-11-24 11:17:08 | [CVE-2026-124832](https://nvd.nist.gov/vuln/detail/CVE-2026-124832) | Medium | 6.3 | Stored Cross-Site Scripting (XSS) in 'activity[description]' field in the POST request to '/people/{person_id}/cvs/{cv_… |
| 2026-11-24 11:17:09 | [CVE-2026-127180](https://nvd.nist.gov/vuln/detail/CVE-2026-127180) | Medium | 5.0 | The SUSE NeuVector image scanner before version 4.331 writes each per-scan task request to a temporary file on disk wit… |
| 2026-11-24 11:17:09 | [CVE-2026-127182](https://nvd.nist.gov/vuln/detail/CVE-2026-127182) | High | 8.8 | A stack buffer overflow in DLP/WAF in the enforcer dataplane of SUSE NeuVector before 5.5, 5.5 before 5.5.6, 5.6.0 befo… |
| 2026-11-24 11:17:09 | [CVE-2026-127183](https://nvd.nist.gov/vuln/detail/CVE-2026-127183) | High | 7.5 | Various memory-safety issues in dataplane of SUSE Neuvector before 5.5, 5.5.0 before 5.5.6, 5.6.0 before 5.6.5 could be… |
| 2026-11-24 11:17:20 | [CVE-2026-59415](https://nvd.nist.gov/vuln/detail/CVE-2026-59415) | Critical | 10.0 | TypesenseVectorStore is vulnerable to a document ID injection in its delete operation that can cause unintended documen… |
| 2026-11-24 11:17:20 | [CVE-2026-82442](https://nvd.nist.gov/vuln/detail/CVE-2026-82442) |  |  | Description `HostURLFilter.configure` reads the `ignoreOutsideDomain` parameter but tests the node belonging to `ignore… |
| 2026-11-24 11:17:21 | [CVE-2026-82444](https://nvd.nist.gov/vuln/detail/CVE-2026-82444) |  |  | Description `CookieConverter.getCookies` decides which stored cookies to attach to an outbound request. The applicabili… |
| 2026-11-24 11:17:21 | [CVE-2026-82445](https://nvd.nist.gov/vuln/detail/CVE-2026-82445) |  |  | Description The SQL status backend serialises per-URL metadata into a single column by concatenating a tabulation, the… |
| 2026-11-24 11:17:21 | [CVE-2026-82446](https://nvd.nist.gov/vuln/detail/CVE-2026-82446) |  |  | Description When StormCrawler fetches a host's `/robots.txt` and receives a redirect, `HttpRobotRulesParser` resolves t… |
| 2026-11-24 11:17:21 | [CVE-2026-96296](https://nvd.nist.gov/vuln/detail/CVE-2026-96296) |  |  | An API which can allow a user to delete any workflow execution results is missing authentication. This means that any w… |
| 2026-11-24 11:17:21 | [CVE-2026-96298](https://nvd.nist.gov/vuln/detail/CVE-2026-96298) |  |  | Missing Authorization vulnerability in the computing unit workflow websocket of Apache Texera (incubating) allows an au… |
| 2026-11-24 11:17:21 | [CVE-2026-96353](https://nvd.nist.gov/vuln/detail/CVE-2026-96353) |  |  | Missing Authorization vulnerability in the project REST API of Apache Texera (incubating). The project API did not chec… |
| 2026-11-24 11:17:21 | [CVE-2026-96354](https://nvd.nist.gov/vuln/detail/CVE-2026-96354) |  |  | Missing Authorization vulnerability in the public project REST API of Apache Texera (incubating). The public project AP… |
| 2026-11-24 11:17:22 | [CVE-2026-97893](https://nvd.nist.gov/vuln/detail/CVE-2026-97893) | Medium | 6.6 | A Denial of Service (DoS) vulnerability exists in the ARQ SPARQL Query Optimiser in Apache Jena ARQ prior to version 6.… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
