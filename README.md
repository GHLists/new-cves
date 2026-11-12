# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 14:18 UTC

New CVEs published between 2026-11-12 13:18 UTC and 2026-11-12 14:18 UTC.

[Full CSV](data/new-cves-2026-11-12T14-18-44-714271Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 14:17:22 | [CVE-2026-107484](https://nvd.nist.gov/vuln/detail/CVE-2026-107484) | High | 7.3 | An input and authorization validation vulnerability in Gaia Portal backend handlers could allow an authenticated, non-a… |
| 2026-11-12 14:17:23 | [CVE-2026-114466](https://nvd.nist.gov/vuln/detail/CVE-2026-114466) | Medium | 4.4 | Arbitrary data can be read or written through git-fast-import(1) and git-fast-export(1) features not marked unsafe |
| 2026-11-12 14:17:23 | [CVE-2026-114467](https://nvd.nist.gov/vuln/detail/CVE-2026-114467) | Low | 3.3 | Out-of-bounds write possible in Git when git-merge(1) used on tag with more than two GPG signatures |
| 2026-11-12 14:17:23 | [CVE-2026-114469](https://nvd.nist.gov/vuln/detail/CVE-2026-114469) | Medium | 4.4 | Out-of-bounds read can crash git-apply(1) when binary patch inflates to very large size |
| 2026-11-12 14:17:23 | [CVE-2026-116835](https://nvd.nist.gov/vuln/detail/CVE-2026-116835) | High | 8.7 | In affected versions of Octopus Server, insufficient validation of custom claims on OIDC accounts allowed a user with p… |
| 2026-11-12 14:17:23 | [CVE-2026-120490](https://nvd.nist.gov/vuln/detail/CVE-2026-120490) | Low | 3.8 | On Scalable Platforms, an administrator with permissions to edit and install the Access Control Policy and NAT rules ca… |
| 2026-11-12 14:17:23 | [CVE-2026-120869](https://nvd.nist.gov/vuln/detail/CVE-2026-120869) | Critical | 9.3 | An unauthenticated attacker can bypass authentication controls to access restricted resources on the Citrix NetScaler C… |
| 2026-11-12 14:17:24 | [CVE-2026-123039](https://nvd.nist.gov/vuln/detail/CVE-2026-123039) | High | 7.8 | The Gaia OS DynamicCLI daemon runs as root and listens on a world-writable local socket (/tmp/dynamic_socket) without a… |
| 2026-11-12 14:17:27 | [CVE-2026-124018](https://nvd.nist.gov/vuln/detail/CVE-2026-124018) | Medium | 5.3 | Gutenverse Form plugin for WordPress before 3.2.2 contains a CSV formula injection vulnerability that allows unauthenti… |
| 2026-11-12 14:17:28 | [CVE-2026-124627](https://nvd.nist.gov/vuln/detail/CVE-2026-124627) | High | 8.7 | In affected versions of Octopus Server, incorrect validation of the external identity linked to a newly registered user… |
| 2026-11-12 14:17:28 | [CVE-2026-124628](https://nvd.nist.gov/vuln/detail/CVE-2026-124628) | High | 8.7 | In affected versions of Octopus Server, incorrect validation of changes a user made to their own LDAP identity allowed… |
| 2026-11-12 14:17:28 | [CVE-2026-126995](https://nvd.nist.gov/vuln/detail/CVE-2026-126995) | Low | 2.1 | A vulnerability was found in tjake Jlama up to 0.8.4/0.9.0-beta. Affected by this vulnerability is the function SafeTen… |
| 2026-11-12 14:17:29 | [CVE-2026-127058](https://nvd.nist.gov/vuln/detail/CVE-2026-127058) | Medium | 6.9 | WonderCMS before 3.7.0 contains an unverified password change vulnerability in the saveAction functionality that allows… |
| 2026-11-12 14:17:30 | [CVE-2026-71367](https://nvd.nist.gov/vuln/detail/CVE-2026-71367) | Medium | 4.3 | An incorrect authorization vulnerability was found in AWX's WebSocket consumer. The consumer_access() function only enf… |
| 2026-11-12 14:17:30 | [CVE-2026-92083](https://nvd.nist.gov/vuln/detail/CVE-2026-92083) | High | 7.8 | Missing Authorization vulnerability in TÜBİTAK BİLGEM Yazılım Teknolojileri Araştırma Enstitüsü pardus-image-writer all… |
| 2026-11-12 14:17:30 | [CVE-2026-97845](https://nvd.nist.gov/vuln/detail/CVE-2026-97845) | Medium | 4.3 | An uncontrolled recursion vulnerability has been discovered in the Qt QXmlSimpleReader XML parsing functionality of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
