# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-28 22:22 UTC

New CVEs published between 2026-09-28 21:19 UTC and 2026-09-28 22:22 UTC.

[Full CSV](data/new-cves-2026-09-28T22-22-17-367671Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-28 22:17:28 | [CVE-2024-42002](https://nvd.nist.gov/vuln/detail/CVE-2024-42002) | High | 8.6 | A code injection vulnerability has been discovered in the Robot Operating System 2 (ROS 2) 'ros2topic' command-line too… |
| 2026-09-28 22:17:29 | [CVE-2024-58386](https://nvd.nist.gov/vuln/detail/CVE-2024-58386) | High | 7.1 | ZoneMinder versions 1.37.0 before 1.38.0 contain a path traversal vulnerability in the files view that allows authentic… |
| 2026-09-28 22:17:30 | [CVE-2026-101091](https://nvd.nist.gov/vuln/detail/CVE-2026-101091) | High | 7.1 | SiYuan versions before v3.8.4 fail to properly validate SQL statements in block query embed blocks executed against siy… |
| 2026-09-28 22:17:30 | [CVE-2026-101092](https://nvd.nist.gov/vuln/detail/CVE-2026-101092) | Medium | 6.9 | SiYuan before v3.8.4 fails to enforce publish-access checks in the getCurrentAttrViewImages endpoint, allowing publish… |
| 2026-09-28 22:17:30 | [CVE-2026-101093](https://nvd.nist.gov/vuln/detail/CVE-2026-101093) | Medium | 5.3 | Cotonti through 1.0.0 contains a cross-site request forgery vulnerability in admin.users.php that allows attackers to d… |
| 2026-09-28 22:17:31 | [CVE-2026-101188](https://nvd.nist.gov/vuln/detail/CVE-2026-101188) | Medium | 5.5 | A security vulnerability has been detected in Netcore POWER13 2.0.240730.162638. This issue affects the function router… |
| 2026-09-28 22:17:31 | [CVE-2026-101202](https://nvd.nist.gov/vuln/detail/CVE-2026-101202) | Low | 2.1 | A flaw has been found in FastStone Image Viewer up to 8.3. The affected element is an unknown function of the component… |
| 2026-09-28 22:17:31 | [CVE-2026-101203](https://nvd.nist.gov/vuln/detail/CVE-2026-101203) | Low | 2.1 | A vulnerability has been found in FastStone Image Viewer up to 8.3. The impacted element is an unknown function of the… |
| 2026-09-28 22:17:31 | [CVE-2026-101204](https://nvd.nist.gov/vuln/detail/CVE-2026-101204) | Low | 2.1 | A vulnerability was found in FastStone Image Viewer up to 8.3. This affects an unknown function of the file FSViewer.ex… |
| 2026-09-28 22:17:31 | [CVE-2026-101205](https://nvd.nist.gov/vuln/detail/CVE-2026-101205) | Low | 2.1 | A vulnerability was determined in FastStone Image Viewer up to 8.3. This impacts an unknown function of the component P… |
| 2026-09-28 22:17:32 | [CVE-2026-102281](https://nvd.nist.gov/vuln/detail/CVE-2026-102281) | High | 7.5 | Nest is a framework for building scalable Node.js server-side applications. Prior to 11.2.4 and 12.0.2, a single messag… |
| 2026-09-28 22:17:32 | [CVE-2026-102296](https://nvd.nist.gov/vuln/detail/CVE-2026-102296) | High | 8.3 | ZoneMinder before 1.38.4 contains static buffer overflow vulnerabilities in RemoteCameraHttp::GetResponse() that allow… |
| 2026-09-28 22:17:32 | [CVE-2026-102297](https://nvd.nist.gov/vuln/detail/CVE-2026-102297) | Medium | 5.3 | ZoneMinder before 1.38.4 fails to apply per-monitor access restrictions in the FramesController index endpoint. Authent… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
