# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 00:18 UTC

New CVEs published between 2026-10-20 23:19 UTC and 2026-10-21 00:18 UTC.

[Full CSV](data/new-cves-2026-10-21T00-18-59-744614Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 00:17:17 | [CVE-2026-109681](https://nvd.nist.gov/vuln/detail/CVE-2026-109681) | Medium | 4.7 | The FTP client trusts the server's PASV response IP:port without validation against the control connection target. A ro… |
| 2026-10-21 00:17:18 | [CVE-2026-109682](https://nvd.nist.gov/vuln/detail/CVE-2026-109682) | Medium | 4.7 | Metasploit Framework versions before 6.5.7 allow HTTP requests made through send_request_cgi! to follow redirects to a… |
| 2026-10-21 00:17:48 | [CVE-2026-113706](https://nvd.nist.gov/vuln/detail/CVE-2026-113706) | Medium | 5.1 | A vulnerability was identified in a2aproject a2a-rs up to 0.4.3. Impacted is an unknown function of the file a2a-server… |
| 2026-10-21 00:17:49 | [CVE-2026-113707](https://nvd.nist.gov/vuln/detail/CVE-2026-113707) | Medium | 5.3 | A security flaw has been discovered in a2aproject a2a-rs up to 0.4.4. The affected element is the function InMemoryTask… |
| 2026-10-21 00:17:49 | [CVE-2026-113735](https://nvd.nist.gov/vuln/detail/CVE-2026-113735) | Low | 2.9 | A vulnerability was determined in D-Link DCS-6501LH 3.03.02. Affected by this vulnerability is the function mydlink_set… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
