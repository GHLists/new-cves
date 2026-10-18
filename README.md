# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-18 13:20 UTC

New CVEs published between 2026-10-18 12:18 UTC and 2026-10-18 13:20 UTC.

[Full CSV](data/new-cves-2026-10-18T13-20-22-723986Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-18 13:16:35 | [CVE-2026-111986](https://nvd.nist.gov/vuln/detail/CVE-2026-111986) | Low | 2.1 | A vulnerability was determined in AUTOMATIC1111 stable-diffusion-webui up to 1.10.1. Affected is the function get_obj_f… |
| 2026-10-18 13:16:36 | [CVE-2026-112046](https://nvd.nist.gov/vuln/detail/CVE-2026-112046) | Medium | 6.8 | OW2 ASM 9.11 before 9.11.1 contains an infinite loop vulnerability in Label.resolve() caused by 16-bit forward-referenc… |
| 2026-10-18 13:16:36 | [CVE-2026-112047](https://nvd.nist.gov/vuln/detail/CVE-2026-112047) | Medium | 5.3 | OneUptime 14.0.2 before 14.0.69 contains an incorrect authorization vulnerability that allows authenticated project mem… |
| 2026-10-18 13:16:36 | [CVE-2026-112048](https://nvd.nist.gov/vuln/detail/CVE-2026-112048) | Medium | 6.9 | libspatialite through 5.1.0 fails to validate the polygon ring count in ParseWkbPolygon, allowing attackers to trigger… |
| 2026-10-18 13:16:36 | [CVE-2026-112049](https://nvd.nist.gov/vuln/detail/CVE-2026-112049) | Medium | 6.7 | Vita3K before build 4187 contains a path traversal (zip slip) vulnerability in install_archive_content() that allows at… |
| 2026-10-18 13:16:37 | [CVE-2026-112050](https://nvd.nist.gov/vuln/detail/CVE-2026-112050) | Low | 2.3 | Gitify before 7.10.0 contains a login cross-site request forgery vulnerability that allows remote attackers to bind a v… |
| 2026-10-18 13:16:37 | [CVE-2026-112051](https://nvd.nist.gov/vuln/detail/CVE-2026-112051) | High | 8.3 | Xinference through 4.0.1 contains a path traversal vulnerability on Windows that allows unauthenticated attackers to wr… |
| 2026-10-18 13:16:37 | [CVE-2026-112052](https://nvd.nist.gov/vuln/detail/CVE-2026-112052) | Medium | 6.9 | libspatialite through 5.1.0 contains an integer overflow vulnerability in the WKB point and vertex count size guard of… |
| 2026-10-18 13:16:37 | [CVE-2026-112053](https://nvd.nist.gov/vuln/detail/CVE-2026-112053) | Medium | 6.8 | Schroedinger libschroedinger through 1.0.11 contains an out-of-bounds read vulnerability that allows attackers to read… |
| 2026-10-18 13:16:37 | [CVE-2026-112054](https://nvd.nist.gov/vuln/detail/CVE-2026-112054) | Medium | 6.8 | Schroedinger libschroedinger through 1.0.11 contains a divide by zero vulnerability that allows attackers to crash appl… |
| 2026-10-18 13:16:37 | [CVE-2026-112055](https://nvd.nist.gov/vuln/detail/CVE-2026-112055) | Medium | 6.8 | wvWare wv through 1.2.9 contains a stack-based out-of-bounds read vulnerability in wvGetPAPX_FKP and wvGetCHPX_FKP caus… |
| 2026-10-18 13:16:37 | [CVE-2026-112056](https://nvd.nist.gov/vuln/detail/CVE-2026-112056) | Medium | 6.8 | wvWare wv through 1.2.9 contains a heap-based out-of-bounds read vulnerability in wvGetSTSH in stylesheet.c that allows… |
| 2026-10-18 13:16:38 | [CVE-2026-112057](https://nvd.nist.gov/vuln/detail/CVE-2026-112057) | Medium | 6.8 | libdvdnav before 7.0.0 contains a heap out-of-bounds read vulnerability in dvdnav_describe_title_chapters that allows a… |
| 2026-10-18 13:16:38 | [CVE-2026-112058](https://nvd.nist.gov/vuln/detail/CVE-2026-112058) | Medium | 6.8 | VideoLAN libdvdnav through 7.0.0 contains an out-of-bounds read vulnerability in set_PTT that allows attackers to crash… |
| 2026-10-18 13:16:38 | [CVE-2026-112059](https://nvd.nist.gov/vuln/detail/CVE-2026-112059) | Medium | 6.9 | libLAS through 1.8.1 contains a heap out-of-bounds write vulnerability in the point record reader caused by truncating… |
| 2026-10-18 13:16:38 | [CVE-2026-112060](https://nvd.nist.gov/vuln/detail/CVE-2026-112060) | Medium | 6.1 | librtmp in RTMPDump through 2.6 contains an out-of-bounds read and heap out-of-bounds write vulnerability because AMF3_… |
| 2026-10-18 13:16:38 | [CVE-2026-112061](https://nvd.nist.gov/vuln/detail/CVE-2026-112061) | Medium | 5.3 | librtmp (RTMPDump) through 2.6 contains a heap out-of-bounds read vulnerability in AMFProp_Decode that reads an AMF0 st… |
| 2026-10-18 13:16:38 | [CVE-2026-112062](https://nvd.nist.gov/vuln/detail/CVE-2026-112062) | Medium | 6.0 | lwIP through 2.2.1 contains a stack out-of-bounds write vulnerability in mdns_handle_response that allows adjacent atta… |
| 2026-10-18 13:16:38 | [CVE-2026-112063](https://nvd.nist.gov/vuln/detail/CVE-2026-112063) | Medium | 6.0 | libstrophe through 0.14.0 contains a stack-based buffer overflow vulnerability in SCRAM_Hi that allows malicious XMPP s… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
