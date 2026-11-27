# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-27 17:19 UTC

New CVEs published between 2026-11-27 16:20 UTC and 2026-11-27 17:19 UTC.

[Full CSV](data/new-cves-2026-11-27T17-19-56-544936Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-27 17:17:56 | [CVE-2026-137684](https://nvd.nist.gov/vuln/detail/CVE-2026-137684) | Medium | 5.5 | A security flaw has been discovered in eosphoros-ai DB-GPT up to 0.8.3. This affects the function editor_sql_run of the… |
| 2026-11-27 17:17:58 | [CVE-2026-137992](https://nvd.nist.gov/vuln/detail/CVE-2026-137992) | High | 8.7 | libexpat through 2.11.0 contains a denial of service vulnerability in defineAttribute() of lib/xmlparse.c that fails to… |
| 2026-11-27 17:17:58 | [CVE-2026-137993](https://nvd.nist.gov/vuln/detail/CVE-2026-137993) | Medium | 6.3 | django-allauth 65.17.0 before 65.23.0 contains a denial of service vulnerability in truncate_ip() that collapses all IP… |
| 2026-11-27 17:17:58 | [CVE-2026-137994](https://nvd.nist.gov/vuln/detail/CVE-2026-137994) | High | 8.5 | Leo through 6.8.10 contains an insecure deserialization vulnerability that allows attackers to execute code by embeddin… |
| 2026-11-27 17:17:58 | [CVE-2026-137995](https://nvd.nist.gov/vuln/detail/CVE-2026-137995) | High | 7.0 | FOG Project before 1.6.0.119 contains an information disclosure vulnerability that allows unauthenticated attackers to… |
| 2026-11-27 17:17:58 | [CVE-2026-137996](https://nvd.nist.gov/vuln/detail/CVE-2026-137996) | Medium | 6.8 | Zettlr before 4.11.0 fails to validate URI schemes in Markdown link targets, allowing attackers to launch arbitrary reg… |
| 2026-11-27 17:17:59 | [CVE-2026-137997](https://nvd.nist.gov/vuln/detail/CVE-2026-137997) | High | 8.5 | HCIPy through 0.7.1 contains an insecure deserialization vulnerability that allows attackers to execute code by supplyi… |
| 2026-11-27 17:17:59 | [CVE-2026-137998](https://nvd.nist.gov/vuln/detail/CVE-2026-137998) | High | 8.5 | Detoxify 0.5.3 through 0.5.4 contains an insecure deserialization vulnerability in load_checkpoint that allows attacker… |
| 2026-11-27 17:17:59 | [CVE-2026-137999](https://nvd.nist.gov/vuln/detail/CVE-2026-137999) | High | 8.5 | JSONSchema2PoPo2 through 3.0.3 contains a code injection vulnerability that allows attackers to inject Python code by s… |
| 2026-11-27 17:18:01 | [CVE-2026-81041](https://nvd.nist.gov/vuln/detail/CVE-2026-81041) | High | 7.1 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Certificate Validatio… |
| 2026-11-27 17:18:01 | [CVE-2026-81042](https://nvd.nist.gov/vuln/detail/CVE-2026-81042) | Low | 3.3 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Insertion of Sensitive Informa… |
| 2026-11-27 17:18:01 | [CVE-2026-81044](https://nvd.nist.gov/vuln/detail/CVE-2026-81044) | Medium | 5.8 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Neutralization of Spe… |
| 2026-11-27 17:18:02 | [CVE-2026-81045](https://nvd.nist.gov/vuln/detail/CVE-2026-81045) | Medium | 6.8 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Certificate Validatio… |
| 2026-11-27 17:18:02 | [CVE-2026-81047](https://nvd.nist.gov/vuln/detail/CVE-2026-81047) | Medium | 6.8 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Authentication vulner… |
| 2026-11-27 17:18:02 | [CVE-2026-81050](https://nvd.nist.gov/vuln/detail/CVE-2026-81050) | Low | 2.9 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Insufficient Logging vulnerabi… |
| 2026-11-27 17:18:02 | [CVE-2026-81053](https://nvd.nist.gov/vuln/detail/CVE-2026-81053) | Medium | 6.7 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Concurrent Execution using Shar… |
| 2026-11-27 17:18:02 | [CVE-2026-81054](https://nvd.nist.gov/vuln/detail/CVE-2026-81054) | Medium | 5.5 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Insertion of Sensitive Informa… |
| 2026-11-27 17:18:02 | [CVE-2026-81055](https://nvd.nist.gov/vuln/detail/CVE-2026-81055) | Low | 2.9 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Observable Timing Discrepancy… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
