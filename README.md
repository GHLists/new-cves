# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-02 19:20 UTC

New CVEs published between 2026-10-02 18:19 UTC and 2026-10-02 19:20 UTC.

[Full CSV](data/new-cves-2026-10-02T19-20-05-15076Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-02 19:16:37 | [CVE-2014-125130](https://nvd.nist.gov/vuln/detail/CVE-2014-125130) | High | 8.7 | CodeArt Google MP3 Audio Player plugin (google-mp3-audio-player) for WordPress through 1.0.11 contains an unauthenticat… |
| 2026-10-02 19:16:38 | [CVE-2020-37278](https://nvd.nist.gov/vuln/detail/CVE-2020-37278) | High | 8.7 | Weaver e-Bridge contains an unauthenticated arbitrary file read vulnerability that allows remote attackers to access ar… |
| 2026-10-02 19:16:38 | [CVE-2023-54405](https://nvd.nist.gov/vuln/detail/CVE-2023-54405) | Critical | 9.3 | H3C CVM, the Cloud Virtualization Management component of the H3C CAS cloud platform, contains an unauthenticated arbit… |
| 2026-10-02 19:16:39 | [CVE-2026-103956](https://nvd.nist.gov/vuln/detail/CVE-2026-103956) | Critical | 10.0 | Missing authentication for critical function in the authentication dependency in Loom for AWS before 1.6.1 allowed remo… |
| 2026-10-02 19:16:39 | [CVE-2026-103957](https://nvd.nist.gov/vuln/detail/CVE-2026-103957) | High | 8.2 | Server-side request forgery in the OAuth2 discovery handling in Loom for AWS before 1.7.0 might allow an authenticated… |
| 2026-10-02 19:16:40 | [CVE-2026-103958](https://nvd.nist.gov/vuln/detail/CVE-2026-103958) | High | 8.3 | Server-side request forgery in the tool server and remote agent connection handling in Loom for AWS before 1.7.0 might… |
| 2026-10-02 19:16:41 | [CVE-2026-19856](https://nvd.nist.gov/vuln/detail/CVE-2026-19856) | Medium | 6.5 | The All in One SEO WordPress plugin before 5.0.2.1 does not correctly determine which shortcodes are present in content… |
| 2026-10-02 19:16:43 | [CVE-2026-96940](https://nvd.nist.gov/vuln/detail/CVE-2026-96940) | High | 8.8 | Weak authorization in Microsoft Exchange Server allows an authenticated attacker to elevate privileges over a network. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
