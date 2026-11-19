# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 14:21 UTC

New CVEs published between 2026-11-19 13:18 UTC and 2026-11-19 14:21 UTC.

[Full CSV](data/new-cves-2026-11-19T14-21-04-006508Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 14:17:23 | [CVE-2026-111506](https://nvd.nist.gov/vuln/detail/CVE-2026-111506) | High | 8.8 | Dell PowerStore contains a Missing Authentication vulnerability that a network-adjacent attacker could exploit to bypas… |
| 2026-11-19 14:17:26 | [CVE-2026-126824](https://nvd.nist.gov/vuln/detail/CVE-2026-126824) | Medium | 5.5 | A maliciously crafted SBSAR file, when imported or loaded through the Substance in 3ds Max plugin in Autodesk 3ds Max 2… |
| 2026-11-19 14:17:26 | [CVE-2026-126825](https://nvd.nist.gov/vuln/detail/CVE-2026-126825) | Medium | 5.5 | A maliciously crafted SBSAR file, when imported or loaded through the Substance in 3ds Max plugin in Autodesk 3ds Max 2… |
| 2026-11-19 14:17:27 | [CVE-2026-126826](https://nvd.nist.gov/vuln/detail/CVE-2026-126826) | High | 7.8 | A maliciously crafted SBSAR file, when imported or loaded through the Substance in 3ds Max plugin in Autodesk 3ds Max 2… |
| 2026-11-19 14:17:27 | [CVE-2026-126827](https://nvd.nist.gov/vuln/detail/CVE-2026-126827) | Medium | 5.5 | A maliciously crafted SBSAR file, when imported or loaded through the Substance in 3ds Max plugin in Autodesk 3ds Max 2… |
| 2026-11-19 14:17:28 | [CVE-2026-132858](https://nvd.nist.gov/vuln/detail/CVE-2026-132858) | High | 7.8 | A flaw was found in gdm. The CreateRemoteDisplay D-Bus method fails to perform proper authorization checks when initiat… |
| 2026-11-19 14:17:28 | [CVE-2026-133112](https://nvd.nist.gov/vuln/detail/CVE-2026-133112) | Low | 2.3 | modified eCommerce Shopsoftware through 3.3.0 contains a cross-site request forgery vulnerability in gv_send.php becaus… |
| 2026-11-19 14:17:28 | [CVE-2026-133113](https://nvd.nist.gov/vuln/detail/CVE-2026-133113) | High | 7.1 | Gogs through 0.14.4 contains an authorization bypass vulnerability that allows collaborators with write access to push… |
| 2026-11-19 14:17:28 | [CVE-2026-133114](https://nvd.nist.gov/vuln/detail/CVE-2026-133114) | Medium | 5.3 | Caddy – WooCommerce Side Cart & Free Shipping Bar plugin for WordPress 3.0.0 before 3.2.1 contains a missing authorizat… |
| 2026-11-19 14:17:28 | [CVE-2026-133115](https://nvd.nist.gov/vuln/detail/CVE-2026-133115) | Medium | 5.3 | Redmine 6.1.0 before 6.1.6 and 7.0.0 before 7.0.3 contains an incorrect authorization vulnerability that lets OAuth cli… |
| 2026-11-19 14:17:28 | [CVE-2026-133116](https://nvd.nist.gov/vuln/detail/CVE-2026-133116) | Medium | 5.3 | Termix 1.7.0 before 26.11.2 contains a path traversal vulnerability that allows authenticated users to write files outs… |
| 2026-11-19 14:17:29 | [CVE-2026-133157](https://nvd.nist.gov/vuln/detail/CVE-2026-133157) | Medium | 5.1 | flowintel contains a CSV injection vulnerability in its audit log CSV export functionality. Attacker-influenced text re… |
| 2026-11-19 14:17:29 | [CVE-2026-133163](https://nvd.nist.gov/vuln/detail/CVE-2026-133163) | Medium | 5.3 | MISP contains an authorization bypass affecting the event protection mechanism. In MISP, a protected event is designed… |
| 2026-11-19 14:17:29 | [CVE-2026-133165](https://nvd.nist.gov/vuln/detail/CVE-2026-133165) | Medium | 5.3 | MISP contains an authorization and scope flaw in the ObjectReference model's captureReference method. When a user saves… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
