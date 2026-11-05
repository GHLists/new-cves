# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 12:19 UTC

New CVEs published between 2026-11-05 11:18 UTC and 2026-11-05 12:19 UTC.

[Full CSV](data/new-cves-2026-11-05T12-19-01-476482Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 12:17:49 | [CVE-2026-121489](https://nvd.nist.gov/vuln/detail/CVE-2026-121489) | Critical | 10.0 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in Apache Juneau. The micr… |
| 2026-11-05 12:17:49 | [CVE-2026-123018](https://nvd.nist.gov/vuln/detail/CVE-2026-123018) | Medium | 5.5 | A security flaw has been discovered in eosphoros-ai DB-GPT up to 0.8.2. This issue affects the function execute_code of… |
| 2026-11-05 12:17:50 | [CVE-2026-123019](https://nvd.nist.gov/vuln/detail/CVE-2026-123019) | Medium | 5.5 | A weakness has been identified in eosphoros-ai DB-GPT up to 0.8.2. Impacted is the function exec_module of the file hf_… |
| 2026-11-05 12:17:50 | [CVE-2026-73095](https://nvd.nist.gov/vuln/detail/CVE-2026-73095) | High | 8.7 | Allocation of Resources Without Limits or Throttling vulnerability in Apache Juneau. The MessagePack parser, which the… |
| 2026-11-05 12:17:50 | [CVE-2026-73098](https://nvd.nist.gov/vuln/detail/CVE-2026-73098) | Critical | 10.0 | Improper control of dynamically-loaded code vulnerability in Apache Juneau. When Apache Juneau parses a value into a pr… |
| 2026-11-05 12:17:50 | [CVE-2026-73099](https://nvd.nist.gov/vuln/detail/CVE-2026-73099) | Critical | 10.0 | Cross-Site Request Forgery (CSRF) vulnerability in Apache Juneau. The REST server accepts a "content" query parameter t… |
| 2026-11-05 12:17:51 | [CVE-2026-73100](https://nvd.nist.gov/vuln/detail/CVE-2026-73100) | Critical | 10.0 | Insertion of Sensitive Information into Log File vulnerability in Apache Juneau. The default REST server call logger re… |
| 2026-11-05 12:17:51 | [CVE-2026-73101](https://nvd.nist.gov/vuln/detail/CVE-2026-73101) | Critical | 10.0 | Generation of Error Message Containing Sensitive Information vulnerability in Apache Juneau. The REST server sends the… |
| 2026-11-05 12:17:51 | [CVE-2026-73116](https://nvd.nist.gov/vuln/detail/CVE-2026-73116) | Critical | 10.0 | Insufficiently Protected Credentials vulnerability in Apache Juneau. The Apache Juneau RestClient followed HTTP redirec… |
| 2026-11-05 12:17:51 | [CVE-2026-73117](https://nvd.nist.gov/vuln/detail/CVE-2026-73117) | Critical | 10.0 | Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Response Splitting') vulnerability in Apache Juneau. T… |
| 2026-11-05 12:17:51 | [CVE-2026-96677](https://nvd.nist.gov/vuln/detail/CVE-2026-96677) | Critical | 10.0 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Apache Juneau. HT… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
