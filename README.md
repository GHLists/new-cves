# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-18 11:22 UTC

New CVEs published between 2026-11-18 10:22 UTC and 2026-11-18 11:22 UTC.

[Full CSV](data/new-cves-2026-11-18T11-22-48-453709Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-18 11:17:35 | [CVE-2025-59906](https://nvd.nist.gov/vuln/detail/CVE-2025-59906) | Critical | 9.3 | Hardcoded credentials in the executable file. These can be extracted using the “Strings.exe” tool and could allow an at… |
| 2026-11-18 11:17:36 | [CVE-2025-59907](https://nvd.nist.gov/vuln/detail/CVE-2025-59907) | Critical | 9.3 | Hardcoded credentials in the executable file. These can be extracted using the “Strings.exe” tool and could allow an at… |
| 2026-11-18 11:17:37 | [CVE-2025-59908](https://nvd.nist.gov/vuln/detail/CVE-2025-59908) | High | 7.1 | Insecure Direct Object Reference (IDOR) vulnerability. Exploiting this vulnerability allows a user to view the names of… |
| 2026-11-18 11:17:37 | [CVE-2025-59909](https://nvd.nist.gov/vuln/detail/CVE-2025-59909) | High | 7.1 | Insecure Direct Object Reference (IDOR) vulnerability. Exploiting this vulnerability allows a user to view the names of… |
| 2026-11-18 11:17:37 | [CVE-2025-59910](https://nvd.nist.gov/vuln/detail/CVE-2025-59910) | High | 7.1 | Insecure Direct Object Reference (IDOR) vulnerability. Exploiting this vulnerability allows a user to view the names of… |
| 2026-11-18 11:17:37 | [CVE-2025-59911](https://nvd.nist.gov/vuln/detail/CVE-2025-59911) | High | 7.1 | Insecure Direct Object Reference (IDOR) vulnerability. Exploiting this vulnerability allows a user to view the names of… |
| 2026-11-18 11:17:37 | [CVE-2025-59912](https://nvd.nist.gov/vuln/detail/CVE-2025-59912) | High | 7.1 | Insecure Direct Object Reference (IDOR) vulnerability. Exploiting this vulnerability allows a user to view the names of… |
| 2026-11-18 11:17:37 | [CVE-2026-110486](https://nvd.nist.gov/vuln/detail/CVE-2026-110486) | Critical | 9.8 | In Eclipse Mosquitto versions 2.1 through 2.1.2, a listener configured with `protocol websockets` mishandles empty WebS… |
| 2026-11-18 11:17:38 | [CVE-2026-126706](https://nvd.nist.gov/vuln/detail/CVE-2026-126706) |  |  | In Eclipse Mosquitto versions 2.1.0 to 2.1.2, the mosquitto_ctrl utility would crash if attempting to interact with a h… |
| 2026-11-18 11:17:38 | [CVE-2026-129149](https://nvd.nist.gov/vuln/detail/CVE-2026-129149) |  |  | In Eclipse Mosquitto versions 2.1.0 to 2.1.2, using the mosquitto_ctrl utility in interactive shell mode to interact wi… |
| 2026-11-18 11:17:38 | [CVE-2026-132049](https://nvd.nist.gov/vuln/detail/CVE-2026-132049) | Medium | 4.3 | A flaw was found in lldpd. The service fails to verify that Link Layer Discovery Protocol - Media Endpoint Discovery (L… |
| 2026-11-18 11:17:38 | [CVE-2026-132069](https://nvd.nist.gov/vuln/detail/CVE-2026-132069) | Medium | 6.3 | MISP (Malware Information Sharing Platform) contains an authorization bypass in the SharingGroup model's captureSGExist… |
| 2026-11-18 11:17:39 | [CVE-2026-87850](https://nvd.nist.gov/vuln/detail/CVE-2026-87850) | Medium | 6.3 | nVision sends user's token via query parameters of GET requests. An attacker who obtains valid token can gain access to… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
