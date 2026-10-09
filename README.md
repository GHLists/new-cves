# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 05:19 UTC

New CVEs published between 2026-10-09 04:18 UTC and 2026-10-09 05:19 UTC.

[Full CSV](data/new-cves-2026-10-09T05-19-10-816939Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 05:16:44 | [CVE-2026-107888](https://nvd.nist.gov/vuln/detail/CVE-2026-107888) | Medium | 5.1 | OpenPrinting CUPS before 2.4.20 contains a NULL pointer dereference in cupsdCheckJobs() when a job marked job-held-on-c… |
| 2026-10-09 05:16:44 | [CVE-2026-107889](https://nvd.nist.gov/vuln/detail/CVE-2026-107889) | Medium | 5.5 | A flaw was found in the login theme rendering component of Keycloak. The issue occurs because the security filter respo… |
| 2026-10-09 05:16:44 | [CVE-2026-107890](https://nvd.nist.gov/vuln/detail/CVE-2026-107890) | Low | 3.3 | OpenPrinting CUPS before 2.4.20 contains a NULL pointer dereference caused by repeated IPP group tags in job-creation r… |
| 2026-10-09 05:16:44 | [CVE-2026-5759](https://nvd.nist.gov/vuln/detail/CVE-2026-5759) | Critical | 9.3 | A double free and use-after-free vulnerability in the RdbLoadDeletedNodes function of the RDB graph decoders (src/seria… |
| 2026-10-09 05:16:45 | [CVE-2026-7826](https://nvd.nist.gov/vuln/detail/CVE-2026-7826) | High | 8.8 | A heap-based out-of-bounds read in the BufferSerializerIOv2_ReadBuffer function (src/serializers/serializer_io.c) in Fa… |
| 2026-10-09 05:16:45 | [CVE-2026-7827](https://nvd.nist.gov/vuln/detail/CVE-2026-7827) | Critical | 9.2 | A stack-based buffer overflow in the _RdbLoadEntity function of the RDB graph decoders (src/serializers/decoders/*/deco… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
