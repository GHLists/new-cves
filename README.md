# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 21:21 UTC

New CVEs published between 2026-11-23 20:20 UTC and 2026-11-23 21:21 UTC.

[Full CSV](data/new-cves-2026-11-23T21-21-51-189121Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 21:16:52 | [CVE-2026-115291](https://nvd.nist.gov/vuln/detail/CVE-2026-115291) | Medium | 6.5 | Missing authorization in Kibana Security AI Assistant conversation deletion can allow an authenticated user with access… |
| 2026-11-23 21:16:55 | [CVE-2026-129976](https://nvd.nist.gov/vuln/detail/CVE-2026-129976) | Medium | 6.5 | Memory Allocation with Excessive Size Value (CWE-789) in Packetbeat can lead to denial of service via a specially craft… |
| 2026-11-23 21:16:56 | [CVE-2026-130164](https://nvd.nist.gov/vuln/detail/CVE-2026-130164) | High | 7.8 | Hermes Agent is an open-source autonomous AI agent built by Nous Research for running tool-using workflows across CLI,… |
| 2026-11-23 21:16:57 | [CVE-2026-133857](https://nvd.nist.gov/vuln/detail/CVE-2026-133857) | Medium | 6.5 | Uncontrolled resource allocation in Kibana exception-list filter creation can lead to denial of service. An authenticat… |
| 2026-11-23 21:16:57 | [CVE-2026-133858](https://nvd.nist.gov/vuln/detail/CVE-2026-133858) | Medium | 6.5 | Certain Fleet APIs in Kibana expose stored credentials to authenticated users who do not have the Fleet Settings: Read… |
| 2026-11-23 21:16:57 | [CVE-2026-133860](https://nvd.nist.gov/vuln/detail/CVE-2026-133860) | Medium | 4.9 | An issue in Kibana allows Elasticsearch transforms in directly uploaded integration packages to run with Kibana's inter… |
| 2026-11-23 21:16:57 | [CVE-2026-133891](https://nvd.nist.gov/vuln/detail/CVE-2026-133891) | Medium | 4.3 | Incorrect authorization in Elasticsearch columnar indices can bypass field-level security for geo_shape values. An auth… |
| 2026-11-23 21:16:57 | [CVE-2026-133917](https://nvd.nist.gov/vuln/detail/CVE-2026-133917) | Medium | 4.3 | Elasticsearch ES\|QL query responses can disclose dataset storage locations and provider identity details to users who a… |
| 2026-11-23 21:16:58 | [CVE-2026-133918](https://nvd.nist.gov/vuln/detail/CVE-2026-133918) | Medium | 4.4 | Elasticsearch ES\|QL data-source and dataset registration can write storage credentials or pre-signed URL signatures to… |
| 2026-11-23 21:16:58 | [CVE-2026-133919](https://nvd.nist.gov/vuln/detail/CVE-2026-133919) | Medium | 4.9 | Uncontrolled resource allocation in Elasticsearch mapping updates can lead to denial of service. An authenticated user… |
| 2026-11-23 21:16:58 | [CVE-2026-133925](https://nvd.nist.gov/vuln/detail/CVE-2026-133925) | Medium | 6.5 | Uncontrolled resource consumption in Elasticsearch query parsing can lead to denial of service. An authenticated user w… |
| 2026-11-23 21:16:58 | [CVE-2026-133926](https://nvd.nist.gov/vuln/detail/CVE-2026-133926) | Medium | 4.3 | An issue was discovered in Kibana where a user with the Synthetics All privilege in one space can access Fleet agent po… |
| 2026-11-23 21:16:58 | [CVE-2026-133935](https://nvd.nist.gov/vuln/detail/CVE-2026-133935) | Medium | 6.8 | Unconstrained S3 endpoint settings in Elasticsearch ES\|QL data sources can cause requests containing storage credential… |
| 2026-11-23 21:16:58 | [CVE-2026-133984](https://nvd.nist.gov/vuln/detail/CVE-2026-133984) | Medium | 4.2 | Missing authorization in Kibana Cases alert attachments can allow an authenticated user with permission to add case com… |
| 2026-11-23 21:16:59 | [CVE-2026-134059](https://nvd.nist.gov/vuln/detail/CVE-2026-134059) | Medium | 6.5 | A relative path traversal vulnerability in Kibana Fleet and Elastic Agent allows an authenticated user with both Fleet… |
| 2026-11-23 21:17:01 | [CVE-2026-135128](https://nvd.nist.gov/vuln/detail/CVE-2026-135128) | Low | 2.1 | A vulnerability was detected in FredrikNoren ungit 1.5.30. This vulnerability affects unknown code of the file source/g… |
| 2026-11-23 21:17:02 | [CVE-2026-135472](https://nvd.nist.gov/vuln/detail/CVE-2026-135472) | Medium | 5.9 | open62541 1.5.0 through 1.5.10 contains a use-after-free and double free vulnerability in the lookupRefType() function… |
| 2026-11-23 21:17:02 | [CVE-2026-135617](https://nvd.nist.gov/vuln/detail/CVE-2026-135617) | Medium | 6.9 | Lookyloo is a web-based URL capture and analysis platform. Prior to the fix, the authorization mechanism for private ca… |
| 2026-11-23 21:17:06 | [CVE-2026-82303](https://nvd.nist.gov/vuln/detail/CVE-2026-82303) | High | 7.5 | A buffer over-read vulnerability in Elasticsearch transport decompression can expose data from other requests. The LZ4… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
