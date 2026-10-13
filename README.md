# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-13 00:18 UTC

New CVEs published between 2026-10-12 23:18 UTC and 2026-10-13 00:18 UTC.

[Full CSV](data/new-cves-2026-10-13T00-18-33-750975Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-13 00:17:00 | [CVE-2026-108939](https://nvd.nist.gov/vuln/detail/CVE-2026-108939) | Medium | 5.5 | A vulnerability has been found in EricLBuehler mistral.rs up to 0.9.3. Impacted is the function is_global_ip of the fil… |
| 2026-10-13 00:17:00 | [CVE-2026-108940](https://nvd.nist.gov/vuln/detail/CVE-2026-108940) | Medium | 5.5 | A vulnerability was found in EricLBuehler Mistral.rs up to 0.9.3. The affected element is the function calibration_appl… |
| 2026-10-13 00:17:00 | [CVE-2026-108941](https://nvd.nist.gov/vuln/detail/CVE-2026-108941) | Low | 2.4 | A vulnerability was identified in Linketic CityGaussian up to 2.0. This affects the function parse_cfg_args of the file… |
| 2026-10-13 00:17:00 | [CVE-2026-17484](https://nvd.nist.gov/vuln/detail/CVE-2026-17484) | Medium | 5.3 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a local attacker to cause a denial of service due to improper access control. |
| 2026-10-13 00:17:01 | [CVE-2026-17487](https://nvd.nist.gov/vuln/detail/CVE-2026-17487) | Medium | 5.3 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a remote attacker to enumerate user profiles due to the return of distinct err… |
| 2026-10-13 00:17:01 | [CVE-2026-18318](https://nvd.nist.gov/vuln/detail/CVE-2026-18318) | Medium | 5.3 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a remote attacker to perform brute-force attacks to obtain credentials due to… |
| 2026-10-13 00:17:01 | [CVE-2026-18343](https://nvd.nist.gov/vuln/detail/CVE-2026-18343) | Medium | 4.4 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a local attacker to modify the BOOTP table due to improper authorization. |
| 2026-10-13 00:17:01 | [CVE-2026-19936](https://nvd.nist.gov/vuln/detail/CVE-2026-19936) | Medium | 4.8 | The Bluetooth Mesh Access-layer delayable message queue in subsys/bluetooth/mesh/delayable_msg.c shares three intrusive… |
| 2026-10-13 00:17:01 | [CVE-2026-19937](https://nvd.nist.gov/vuln/detail/CVE-2026-19937) | Medium | 5.7 | The Bluetooth Mesh Access layer delayable-message machinery in subsys/bluetooth/mesh/delayable_msg.c manages a static p… |
| 2026-10-13 00:17:01 | [CVE-2026-19938](https://nvd.nist.gov/vuln/detail/CVE-2026-19938) | Medium | 5.9 | The Bluetooth host's ATT transmit path releases a buffer it does not own when signing fails. chan_send() in subsys/blue… |
| 2026-10-13 00:17:01 | [CVE-2026-81858](https://nvd.nist.gov/vuln/detail/CVE-2026-81858) | Medium | 5.4 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a remote authenticated attacker to cause a denial of service and obtain inform… |
| 2026-10-13 00:17:01 | [CVE-2026-93886](https://nvd.nist.gov/vuln/detail/CVE-2026-93886) | High | 8.3 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a remote authenticated attacker to execute arbitrary script code due to improp… |
| 2026-10-13 00:17:02 | [CVE-2026-96119](https://nvd.nist.gov/vuln/detail/CVE-2026-96119) | Critical | 9.9 | IBM i 7.3, 7.4, 7.5, and 7.6 could allow a remote authenticated attacker to obtain sensitive information or execute arb… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
