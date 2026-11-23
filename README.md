# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 14:18 UTC

New CVEs published between 2026-11-23 13:19 UTC and 2026-11-23 14:18 UTC.

[Full CSV](data/new-cves-2026-11-23T14-18-43-629654Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 14:17:22 | [CVE-2026-119068](https://nvd.nist.gov/vuln/detail/CVE-2026-119068) | High | 8.4 | An rsync server can send diagnostic data to the client which is mirrored to stdout and collected by Routinator line by… |
| 2026-11-23 14:17:22 | [CVE-2026-119069](https://nvd.nist.gov/vuln/detail/CVE-2026-119069) | High | 8.4 | When rejecting a publication point midway during processing amd falling back to the stored version of the publication p… |
| 2026-11-23 14:17:23 | [CVE-2026-132856](https://nvd.nist.gov/vuln/detail/CVE-2026-132856) | High | 7.8 | A vulnerability was discovered in the ZoneAlarm client for Windows that allows a low-privileged local user to run code… |
| 2026-11-23 14:17:25 | [CVE-2026-134927](https://nvd.nist.gov/vuln/detail/CVE-2026-134927) | Medium | 4.8 | A weakness has been identified in phpBB up to 3.3.19. Affected by this vulnerability is the function phpbb_get_user_ran… |
| 2026-11-23 14:17:27 | [CVE-2026-93585](https://nvd.nist.gov/vuln/detail/CVE-2026-93585) | High | 8.8 | An improper authorization vulnerability in the EV Reach Client Agent allows authenticated users with low privileges to… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
