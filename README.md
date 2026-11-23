# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 08:20 UTC

New CVEs published between 2026-11-23 07:18 UTC and 2026-11-23 08:20 UTC.

[Full CSV](data/new-cves-2026-11-23T08-20-28-450281Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 08:17:13 | [CVE-2026-115232](https://nvd.nist.gov/vuln/detail/CVE-2026-115232) | Low | 2.1 | In iceoryx2 versions from 0.6.0 to 0.10.0, The C API getters that copy a service's hash into a caller-provided buffer (… |
| 2026-11-23 08:17:14 | [CVE-2026-118887](https://nvd.nist.gov/vuln/detail/CVE-2026-118887) | Medium | 6.8 | ZTE Z80 Ultra is affected by an unauthorized access vulnerability. Successful exploitation of this vulnerability could… |
| 2026-11-23 08:17:14 | [CVE-2026-120382](https://nvd.nist.gov/vuln/detail/CVE-2026-120382) | Critical | 9.8 | An improper neutralization of argument delimiters in a command vulnerability in the OAuth API in Synology DiskStation M… |
| 2026-11-23 08:17:14 | [CVE-2026-121456](https://nvd.nist.gov/vuln/detail/CVE-2026-121456) | Medium | 5.8 | A privilege escalation vulnerability in the Axivion Suite ApiToken permission restriction for OIDC and SAML users of th… |
| 2026-11-23 08:17:14 | [CVE-2026-134881](https://nvd.nist.gov/vuln/detail/CVE-2026-134881) | Low | 2.0 | A security flaw has been discovered in HuLaSpark HuLa up to 3.0.9. This vulnerability affects the function showMsg of t… |
| 2026-11-23 08:17:14 | [CVE-2026-134935](https://nvd.nist.gov/vuln/detail/CVE-2026-134935) | High | 7.0 | The dell-xps-touchpad-haptics package before 1.0.0-4 for Omarchy allows local users to change ownership of a root-owned… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
