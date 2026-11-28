# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-28 03:20 UTC

New CVEs published between 2026-11-28 02:20 UTC and 2026-11-28 03:20 UTC.

[Full CSV](data/new-cves-2026-11-28T03-20-35-851327Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-28 03:17:06 | [CVE-2026-138154](https://nvd.nist.gov/vuln/detail/CVE-2026-138154) | Critical | 9.3 | POSTAL 2 before build 26810491 contains a sandbox escape vulnerability that allows malicious Steam Workshop mods to exe… |
| 2026-11-28 03:17:07 | [CVE-2026-138158](https://nvd.nist.gov/vuln/detail/CVE-2026-138158) | High | 7.0 | libgphoto2 through 2.5.34 contains a stack buffer overflow in sierra_get_string_register() that lets a malicious sierra… |
| 2026-11-28 03:17:07 | [CVE-2026-138159](https://nvd.nist.gov/vuln/detail/CVE-2026-138159) | High | 7.7 | edbrowse through 3.8.19 contains an integer overflow in stringAndBytes() that allows malicious servers to write past a… |
| 2026-11-28 03:17:07 | [CVE-2026-138160](https://nvd.nist.gov/vuln/detail/CVE-2026-138160) | High | 8.5 | Gammu before 1.45.2 contains a stack-based buffer overflow vulnerability in ReadBackupTextLen() that allows attackers t… |
| 2026-11-28 03:17:08 | [CVE-2026-138161](https://nvd.nist.gov/vuln/detail/CVE-2026-138161) | High | 8.5 | Gammu before 1.45.2 contains a buffer overflow vulnerability in LoadBackup() that allows attackers to corrupt memory by… |
| 2026-11-28 03:17:08 | [CVE-2026-138162](https://nvd.nist.gov/vuln/detail/CVE-2026-138162) | High | 7.3 | Gammu before 1.45.2 contains a stack-based buffer overflow vulnerability in ALCATEL_EncodeString() that allows attacker… |
| 2026-11-28 03:17:08 | [CVE-2026-138163](https://nvd.nist.gov/vuln/detail/CVE-2026-138163) | High | 8.5 | Gammu before 1.45.2 contains a heap-based buffer overflow in ReadWAPSettingsEntry() that allows attackers to corrupt he… |
| 2026-11-28 03:17:08 | [CVE-2026-138164](https://nvd.nist.gov/vuln/detail/CVE-2026-138164) | Medium | 4.8 | Gammu before 1.45.2 contains a stack-based buffer overflow vulnerability in SaveBackupText() in backtext.c that allows… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
