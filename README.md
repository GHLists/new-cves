# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 16:20 UTC

New CVEs published between 2026-11-19 15:20 UTC and 2026-11-19 16:20 UTC.

[Full CSV](data/new-cves-2026-11-19T16-20-55-118062Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 16:18:14 | [CVE-2025-71472](https://nvd.nist.gov/vuln/detail/CVE-2025-71472) | Medium | 6.8 | littlefs 2.8.0 through 2.11.3 contains a divide-by-zero vulnerability in lfs_mount_() that allows attackers to crash pr… |
| 2026-11-19 16:18:15 | [CVE-2026-102770](https://nvd.nist.gov/vuln/detail/CVE-2026-102770) | Medium | 5.1 | Improper neutralization of special elements in data query logic (Cypher injection) in the fulltext and vector index que… |
| 2026-11-19 16:18:30 | [CVE-2026-109920](https://nvd.nist.gov/vuln/detail/CVE-2026-109920) | Medium | 5.5 | Use of uninitialized memory when processing certain font files in X.Org libXfont before 2.0.10 could be used by authent… |
| 2026-11-19 16:19:27 | [CVE-2026-121592](https://nvd.nist.gov/vuln/detail/CVE-2026-121592) | Medium | 6.5 | Mattermost Plugins versions <=12.-1 11.0.11 11.11.7 11.2.10.0 fail to check for a nil result after decoding the HTTP re… |
| 2026-11-19 16:19:27 | [CVE-2026-121593](https://nvd.nist.gov/vuln/detail/CVE-2026-121593) | Medium | 5.0 | Mattermost Plugins versions <=12.-1 11.0.11 11.11.7 11.2.10.0 fail to verify that the caller can post in a run's channe… |
| 2026-11-19 16:19:27 | [CVE-2026-121594](https://nvd.nist.gov/vuln/detail/CVE-2026-121594) | Medium | 5.3 | Mattermost Plugins versions <=12.-1 11.11.7 11.2.10 11.1.11.0 fail to enforce the GitLab project permission check for c… |
| 2026-11-19 16:19:32 | [CVE-2026-123146](https://nvd.nist.gov/vuln/detail/CVE-2026-123146) |  |  | Rejected reason: Inline mitigations exists. |
| 2026-11-19 16:19:45 | [CVE-2026-127925](https://nvd.nist.gov/vuln/detail/CVE-2026-127925) |  |  | Rejected reason: Inline mitigations exists. |
| 2026-11-19 16:19:45 | [CVE-2026-128884](https://nvd.nist.gov/vuln/detail/CVE-2026-128884) |  |  | Rejected reason: Inline mitigations exists. |
| 2026-11-19 16:20:09 | [CVE-2026-131807](https://nvd.nist.gov/vuln/detail/CVE-2026-131807) | High | 7.5 | United Chargers Grizzl-E Smart 40A OCPP GetConfiguration Stack-based Buffer Overflow Remote Code Execution Vulnerabilit… |
| 2026-11-19 16:20:09 | [CVE-2026-131808](https://nvd.nist.gov/vuln/detail/CVE-2026-131808) | Medium | 6.3 | United Chargers Grizzl-E Smart 40A Wi-Fi Configuration Server Missing Authentication Vulnerability. This vulnerability… |
| 2026-11-19 16:20:09 | [CVE-2026-131809](https://nvd.nist.gov/vuln/detail/CVE-2026-131809) | High | 7.6 | United Chargers Grizzl-E Smart 40A OCPP Backend Configuration Authentication Bypass Vulnerability. This vulnerability a… |
| 2026-11-19 16:20:09 | [CVE-2026-131810](https://nvd.nist.gov/vuln/detail/CVE-2026-131810) | High | 7.5 | United Chargers Grizzl-E Smart 40A Download of Code Without Integrity Check Remote Code Execution Vulnerability. This v… |
| 2026-11-19 16:20:09 | [CVE-2026-131811](https://nvd.nist.gov/vuln/detail/CVE-2026-131811) | High | 7.6 | United Chargers Grizzl-E Smart 40A OCPP Backend Configuration Hard-Coded Credentials Authentication Bypass Vulnerabilit… |
| 2026-11-19 16:20:09 | [CVE-2026-131812](https://nvd.nist.gov/vuln/detail/CVE-2026-131812) | High | 7.5 | United Chargers Grizzl-E Smart 40A FTP URL Path Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability… |
| 2026-11-19 16:20:10 | [CVE-2026-131813](https://nvd.nist.gov/vuln/detail/CVE-2026-131813) | High | 7.5 | United Chargers Grizzl-E Smart 40A OCPP UpdateFirmware Out-Of-Bounds Write Remote Code Execution Vulnerability. This vu… |
| 2026-11-19 16:20:13 | [CVE-2026-132151](https://nvd.nist.gov/vuln/detail/CVE-2026-132151) |  |  | Rejected reason: Reason for rejection. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
