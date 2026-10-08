# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 16:18 UTC

New CVEs published between 2026-10-08 15:20 UTC and 2026-10-08 16:18 UTC.

[Full CSV](data/new-cves-2026-10-08T16-18-34-061382Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 16:17:01 | [CVE-2026-106177](https://nvd.nist.gov/vuln/detail/CVE-2026-106177) | Medium | 6.4 | A kernel buffer overflow vulnerability in HP Sure Click versions prior to 4.4.33 may allow local privilege escalation o… |
| 2026-10-08 16:17:03 | [CVE-2026-107287](https://nvd.nist.gov/vuln/detail/CVE-2026-107287) | Medium | 6.5 | Pydantic AI is a Python agent framework for building applications and workflows with Generative AI. From 1.77.0 until 1… |
| 2026-10-08 16:17:04 | [CVE-2026-107288](https://nvd.nist.gov/vuln/detail/CVE-2026-107288) | Low | 3.7 | Pydantic AI is a Python agent framework for building applications and workflows with Generative AI. From 1.77.0 until 1… |
| 2026-10-08 16:17:04 | [CVE-2026-107289](https://nvd.nist.gov/vuln/detail/CVE-2026-107289) | Medium | 6.8 | Pydantic AI is a Python agent framework for building applications and workflows with Generative AI. From 1.56.0 until 1… |
| 2026-10-08 16:17:04 | [CVE-2026-107660](https://nvd.nist.gov/vuln/detail/CVE-2026-107660) | Medium | 6.3 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains an improper certificate validation vulnerability in tls_open() of lib… |
| 2026-10-08 16:17:05 | [CVE-2026-107675](https://nvd.nist.gov/vuln/detail/CVE-2026-107675) | Medium | 6.0 | FFmpeg through 9.0.2 contains a missing host key verification vulnerability in the libssh-based sftp protocol handler t… |
| 2026-10-08 16:17:05 | [CVE-2026-107676](https://nvd.nist.gov/vuln/detail/CVE-2026-107676) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory disclosure vulnerability in av_dynamic_hdr_plus_to_t35() that lea… |
| 2026-10-08 16:17:05 | [CVE-2026-107677](https://nvd.nist.gov/vuln/detail/CVE-2026-107677) | Medium | 5.7 | FFmpeg through 9.0.2 contains a denial of service vulnerability in the DASH demuxer that allows attackers to trigger an… |
| 2026-10-08 16:17:05 | [CVE-2026-107678](https://nvd.nist.gov/vuln/detail/CVE-2026-107678) | Medium | 5.7 | FFmpeg through 9.0.2 contains a stack exhaustion vulnerability in av_encryption_init_info_free() in libavutil/encryptio… |
| 2026-10-08 16:17:10 | [CVE-2026-19585](https://nvd.nist.gov/vuln/detail/CVE-2026-19585) | Medium | 5.3 | HashiCorp go-getter versions before 1.8.10 and go-getter/v2 versions before 2.2.5 are vulnerable to path traversal duri… |
| 2026-10-08 16:18:01 | [CVE-2026-95208](https://nvd.nist.gov/vuln/detail/CVE-2026-95208) |  |  | An issue in the ConfirmNameConstraints() function (wolfcrypt/src/asn.c) of wolfSSL v5.9.1 and v5.9.2 allows attackers t… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
