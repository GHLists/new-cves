# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 14:21 UTC

New CVEs published between 2026-10-07 13:21 UTC and 2026-10-07 14:21 UTC.

[Full CSV](data/new-cves-2026-10-07T14-21-50-570429Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 14:17:07 | [CVE-2026-102257](https://nvd.nist.gov/vuln/detail/CVE-2026-102257) |  |  | A Zip Slip vulnerability in the in the SMA1000 Appliance Management Console (AMC) interface allows an attacker to extra… |
| 2026-10-07 14:17:07 | [CVE-2026-102258](https://nvd.nist.gov/vuln/detail/CVE-2026-102258) |  |  | Post-authentication Stored Cross-Site Scripting (XSS) vulnerability has been identified in the SMA1000 Appliance Manage… |
| 2026-10-07 14:17:08 | [CVE-2026-107181](https://nvd.nist.gov/vuln/detail/CVE-2026-107181) | High | 8.6 | Telegram Desktop before 7.2.9 contains an IPC record-separator injection vulnerability in Core::Sandbox that allows rem… |
| 2026-10-07 14:17:09 | [CVE-2026-107183](https://nvd.nist.gov/vuln/detail/CVE-2026-107183) | Critical | 9.2 | llama.cpp before b11393 contains a use-after-free and double free vulnerability in common_chat_peg_mapper::map that all… |
| 2026-10-07 14:17:09 | [CVE-2026-107194](https://nvd.nist.gov/vuln/detail/CVE-2026-107194) | Critical | 9.2 | Sungrow iSolarCloud before 2026 allows authentication bypass and account takeover via "login_type":"5" in a login reque… |
| 2026-10-07 14:17:09 | [CVE-2026-42616](https://nvd.nist.gov/vuln/detail/CVE-2026-42616) |  |  | In NTFS-3G before 2026.7.7, a heap buffer overflow exists in cat() in ntfscat.c that allows an attacker to corrupt heap… |
| 2026-10-07 14:17:09 | [CVE-2026-42617](https://nvd.nist.gov/vuln/detail/CVE-2026-42617) |  |  | In NTFS-3G before 2026.7.7, a heap buffer overflow exists in ntfs_ir_to_ib() in index.c that allows an attacker to corr… |
| 2026-10-07 14:17:09 | [CVE-2026-42618](https://nvd.nist.gov/vuln/detail/CVE-2026-42618) |  |  | In NTFS-3G before 2026.7.7, a heap buffer overflow exists in ntfs_decompress() in compress.c that allows an attacker to… |
| 2026-10-07 14:17:09 | [CVE-2026-43976](https://nvd.nist.gov/vuln/detail/CVE-2026-43976) | High | 7.1 | wger is a free, open-source workout and fitness manager. Prior to version 2.6, five gym management views in wger apply… |
| 2026-10-07 14:17:10 | [CVE-2026-45161](https://nvd.nist.gov/vuln/detail/CVE-2026-45161) | Medium | 5.4 | wger is a free, open-source workout and fitness manager. Prior to version 2.6, the `trainer_login` view in wger accepts… |
| 2026-10-07 14:17:10 | [CVE-2026-46434](https://nvd.nist.gov/vuln/detail/CVE-2026-46434) | High | 7.1 | wger is a free, open-source workout and fitness manager. Prior to version 2.6, a user with only the `gym_trainer` permi… |
| 2026-10-07 14:17:10 | [CVE-2026-46437](https://nvd.nist.gov/vuln/detail/CVE-2026-46437) | Medium | 4.8 | wger is a free, open-source workout and fitness manager. Versions prior to 2.6 have a vulnerability in the authenticati… |
| 2026-10-07 14:17:10 | [CVE-2026-46438](https://nvd.nist.gov/vuln/detail/CVE-2026-46438) | Medium | 6.5 | wger is a free, open-source workout and fitness manager. Prior to version 2.6, an authenticated attacker can inject arb… |
| 2026-10-07 14:17:10 | [CVE-2026-46569](https://nvd.nist.gov/vuln/detail/CVE-2026-46569) |  |  | In NTFS-3G before 2026.7.7, a heap buffer overflow exists in ntfs_ib_copy_tail(), in libntfs-3g/index.c, that allows an… |
| 2026-10-07 14:17:10 | [CVE-2026-46571](https://nvd.nist.gov/vuln/detail/CVE-2026-46571) |  |  | In NTFS-3G before 2026.7.7, a out-of-bounds read exists in ntfs_fix_file_name() in libntfs-3g/reparse.c that allows an… |
| 2026-10-07 14:17:11 | [CVE-2026-46572](https://nvd.nist.gov/vuln/detail/CVE-2026-46572) |  |  | In NTFS-3G before 2026.7.7, a heap buffer overflow exists in ntfs_ib_cut_tail() in libntfs-3g/index.c that allows an at… |
| 2026-10-07 14:17:11 | [CVE-2026-88514](https://nvd.nist.gov/vuln/detail/CVE-2026-88514) |  |  | An issue in iTerm2 macOS before 3.6.12 allows a local attacker to obtain sensitive information. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
