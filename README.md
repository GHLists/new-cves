# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 09:18 UTC

New CVEs published between 2026-11-09 08:18 UTC and 2026-11-09 09:18 UTC.

[Full CSV](data/new-cves-2026-11-09T09-18-22-620958Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 09:16:58 | [CVE-2026-116337](https://nvd.nist.gov/vuln/detail/CVE-2026-116337) | Low | 0.6 | Uncontrolled resource consumption vulnerability in the Qt Framework HTTP response handling functionality of the Qt Netw… |
| 2026-11-09 09:16:58 | [CVE-2026-123870](https://nvd.nist.gov/vuln/detail/CVE-2026-123870) | Critical | 9.5 | The otterdog webapp evaluates a format-string built from the incoming GitHub webhook JSON body using Python's eval(). W… |
| 2026-11-09 09:16:58 | [CVE-2026-124581](https://nvd.nist.gov/vuln/detail/CVE-2026-124581) | Medium | 5.5 | A vulnerability was determined in itsourcecode Airline Reservation System 1.0. Affected is an unknown function of the f… |
| 2026-11-09 09:16:59 | [CVE-2026-124582](https://nvd.nist.gov/vuln/detail/CVE-2026-124582) | Low | 2.1 | A vulnerability was identified in WebTorrent up to 2.8.5/3.0.21. Affected by this vulnerability is the function getFile… |
| 2026-11-09 09:16:59 | [CVE-2026-124584](https://nvd.nist.gov/vuln/detail/CVE-2026-124584) | Medium | 4.8 | A vulnerability has been found in wummel patool 4.1.0. This vulnerability affects the function extract_gzip of the file… |
| 2026-11-09 09:16:59 | [CVE-2026-124585](https://nvd.nist.gov/vuln/detail/CVE-2026-124585) | High | 8.6 | A vulnerability was found in Chengdu Feiyuxing Technology VW2100 and VEC10GP 1.0 B-MB3W202-210825-r11775. This issue af… |
| 2026-11-09 09:16:59 | [CVE-2026-92606](https://nvd.nist.gov/vuln/detail/CVE-2026-92606) | Medium | 6.0 | Time-of-check time-of-use (TOCTOU) race condition vulnerability in TÜBİTAK BİLGEM Software Technologies Research Instit… |
| 2026-11-09 09:16:59 | [CVE-2026-94249](https://nvd.nist.gov/vuln/detail/CVE-2026-94249) | High | 8.1 | Missing Authorization vulnerability in TÜBİTAK BİLGEM Software Technologies Research Institute Liderahenk allows Privil… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
