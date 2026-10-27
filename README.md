# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 13:18 UTC

New CVEs published between 2026-10-27 12:18 UTC and 2026-10-27 13:18 UTC.

[Full CSV](data/new-cves-2026-10-27T13-18-38-53355Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 13:16:54 | [CVE-2026-100164](https://nvd.nist.gov/vuln/detail/CVE-2026-100164) | High | 7.5 | Observable response discrepancy vulnerability in Rolantis Information Technologies Tourism Industry and Trade Co. Ltd.… |
| 2026-10-27 13:16:54 | [CVE-2026-107590](https://nvd.nist.gov/vuln/detail/CVE-2026-107590) | Low | 1.9 | An out-of-bounds write vulnerability in the Qt QTextCodec iconv-based encoding of the Qt 5 Compatibility APIs module (Q… |
| 2026-10-27 13:16:56 | [CVE-2026-114409](https://nvd.nist.gov/vuln/detail/CVE-2026-114409) | Medium | 5.7 | Docker Desktop before version 4.97.0 could write third-party API keys and OAuth access tokens in cleartext to local app… |
| 2026-10-27 13:16:56 | [CVE-2026-116627](https://nvd.nist.gov/vuln/detail/CVE-2026-116627) |  |  | Improper neutralization of input during web page generation ('Cross-site Scripting') in the notifications feature in De… |
| 2026-10-27 13:16:56 | [CVE-2026-15586](https://nvd.nist.gov/vuln/detail/CVE-2026-15586) | Medium | 5.3 | Improper restriction of excessive authentication attempts vulnerability in İdvlabs Software and Consulting Services Inc… |
| 2026-10-27 13:16:57 | [CVE-2026-24269](https://nvd.nist.gov/vuln/detail/CVE-2026-24269) | High | 7.1 | NVIDIA TensorRT-LLM contains a vulnerability where an attacker could cause a server-side request forgery. A successful… |
| 2026-10-27 13:16:57 | [CVE-2026-47486](https://nvd.nist.gov/vuln/detail/CVE-2026-47486) | High | 7.8 | NVIDIA PhysX for all platforms contains a vulnerability where an attacker could cause an out-of-bounds write. A success… |
| 2026-10-27 13:16:59 | [CVE-2026-65119](https://nvd.nist.gov/vuln/detail/CVE-2026-65119) | High | 8.4 | NVIDIA TensorRT-LLM for any platform contains a vulnerability in KvCacheAwareRouter tokenizer loading, where an attacke… |
| 2026-10-27 13:16:59 | [CVE-2026-65120](https://nvd.nist.gov/vuln/detail/CVE-2026-65120) | High | 7.1 | NVIDIA TensorRT-LLM contains a vulnerability where an attacker could cause a server-side request forgery. A successful… |
| 2026-10-27 13:16:59 | [CVE-2026-65145](https://nvd.nist.gov/vuln/detail/CVE-2026-65145) | Critical | 10.0 | NVIDIA NeMo Agent Toolkit contains a vulnerability where a attacker could cause a missing authentication issue. This vu… |
| 2026-10-27 13:16:59 | [CVE-2026-65151](https://nvd.nist.gov/vuln/detail/CVE-2026-65151) | High | 8.4 | NVIDIA NeMo Agent Toolkit contains vulnerability where an attacker could cause a SQL injection issue. A successful expl… |
| 2026-10-27 13:17:02 | [CVE-2026-92546](https://nvd.nist.gov/vuln/detail/CVE-2026-92546) | High | 7.5 | Authentication bypass by spoofing vulnerability in Keepnet Labs Cybersecurity Inc. Agentic AI / Agentic Ally allows Aut… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
