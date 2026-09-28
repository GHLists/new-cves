# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 16:18 UTC

New CVEs published between 2026-09-28 15:19 UTC and 2026-09-28 16:18 UTC.

[Full CSV](data/new-cves-2026-09-28T16-18-56-233619Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 16:17:11 | [CVE-2026-101076](https://nvd.nist.gov/vuln/detail/CVE-2026-101076) | Critical | 9.3 | A vulnerability was detected in Netcore NR289-GE 1.4.5102. This affects the function system of the file /set_ntp_server… |
| 2026-09-28 16:17:12 | [CVE-2026-101077](https://nvd.nist.gov/vuln/detail/CVE-2026-101077) | Critical | 9.3 | A flaw has been found in Netcore NR289-GE 1.4.5102. This impacts the function process_request of the component boa_temp… |
| 2026-09-28 16:17:12 | [CVE-2026-101078](https://nvd.nist.gov/vuln/detail/CVE-2026-101078) | Low | 1.9 | A vulnerability has been found in deepseek-ai deepseek-harness up to 0.1.7-rc.2. Affected is an unknown function of the… |
| 2026-09-28 16:17:12 | [CVE-2026-101079](https://nvd.nist.gov/vuln/detail/CVE-2026-101079) | Low | 0.9 | A vulnerability was found in agentverus agentverus-scanner up to 0.8.1. Affected by this vulnerability is the function… |
| 2026-09-28 16:17:12 | [CVE-2026-101080](https://nvd.nist.gov/vuln/detail/CVE-2026-101080) | Low | 0.9 | A vulnerability was identified in Tencent AI-Infra-Guard up to 4.5.2/4.6.2. This affects the function startsWith of the… |
| 2026-09-28 16:17:13 | [CVE-2026-101861](https://nvd.nist.gov/vuln/detail/CVE-2026-101861) | Low | 2.1 | Langflow 1.0.16 before 1.12.0 and 0.0.94 before 1.12.0 contain an unsafe eval() vulnerability in schema.py that allows… |
| 2026-09-28 16:17:13 | [CVE-2026-12342](https://nvd.nist.gov/vuln/detail/CVE-2026-12342) | Critical | 9.6 | This vulnerability impacts all versions of IdentityIQ and allows an unauthenticated user remote code execution on the I… |
| 2026-09-28 16:17:15 | [CVE-2026-88804](https://nvd.nist.gov/vuln/detail/CVE-2026-88804) | Critical | 9.6 | An unauthenticated update of public UI settings could be used by remote attackers to execute a stored cross-site script… |
| 2026-09-28 16:17:16 | [CVE-2026-88805](https://nvd.nist.gov/vuln/detail/CVE-2026-88805) | High | 8.1 | Incorrect credential cleaning on logout could be used by remote attackers to keep access credentials even after the acc… |
| 2026-09-28 16:17:16 | [CVE-2026-88808](https://nvd.nist.gov/vuln/detail/CVE-2026-88808) | High | 8.8 | A vulnerability has been identified within Rancher Manager where the Fleet agent wrote resources to downstream clusters… |
| 2026-09-28 16:17:17 | [CVE-2026-91154](https://nvd.nist.gov/vuln/detail/CVE-2026-91154) | Medium | 6.9 | Missing Authentication for Critical Function (CWE-306) in the product cache revalidation Server Action (src/app/actions… |
| 2026-09-28 16:17:17 | [CVE-2026-93348](https://nvd.nist.gov/vuln/detail/CVE-2026-93348) | High | 8.6 | Unsloth Zoo versions 2025.9.9 before 2026.8.14, as implemented in Unsloth 2025.9.9 through 2026.8.19, contains a code i… |
| 2026-09-28 16:17:18 | [CVE-2026-97399](https://nvd.nist.gov/vuln/detail/CVE-2026-97399) | Low | 3.7 | The strncasecmp function in the GNU C Library 2.24 and later optimized for the Power8 architecture may read one byte be… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
