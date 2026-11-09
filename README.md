# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 03:21 UTC

New CVEs published between 2026-11-09 02:18 UTC and 2026-11-09 03:21 UTC.

[Full CSV](data/new-cves-2026-11-09T03-21-06-959425Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 03:16:36 | [CVE-2026-121825](https://nvd.nist.gov/vuln/detail/CVE-2026-121825) | Medium | 5.1 | OpenAM (OpenAM Consortium Edition) 14.0.5 and earlier contains an open redirect vulnerability (CWE-601) in the Liberty… |
| 2026-11-09 03:16:37 | [CVE-2026-124556](https://nvd.nist.gov/vuln/detail/CVE-2026-124556) | Low | 2.1 | A security vulnerability has been detected in kekingcn kkFileView up to 5.0.3. This issue affects the function BaseUrlF… |
| 2026-11-09 03:16:37 | [CVE-2026-124557](https://nvd.nist.gov/vuln/detail/CVE-2026-124557) | Medium | 5.5 | A vulnerability was detected in OtterMind Chat2DB up to 5.3.8. Impacted is the function DbMybatisGenerateServiceImpl.ge… |
| 2026-11-09 03:16:37 | [CVE-2026-124558](https://nvd.nist.gov/vuln/detail/CVE-2026-124558) | Medium | 5.5 | A vulnerability has been found in DataLinkDC Dinky up to 1.2.5. The impacted element is the function SqlGateway.onOpen… |
| 2026-11-09 03:16:38 | [CVE-2026-124560](https://nvd.nist.gov/vuln/detail/CVE-2026-124560) | High | 8.9 | A vulnerability was found in D-Link DIR-878 1.20B05. This affects the function GetCAPTCHAsetting of the file bin/prog.c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
