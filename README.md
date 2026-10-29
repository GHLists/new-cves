# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 07:19 UTC

New CVEs published between 2026-10-29 06:18 UTC and 2026-10-29 07:19 UTC.

[Full CSV](data/new-cves-2026-10-29T07-19-05-531863Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 07:16:44 | [CVE-2026-117548](https://nvd.nist.gov/vuln/detail/CVE-2026-117548) | Medium | 6.5 | A NULL pointer dereference flaw was found in 389-ds-base. This flaw occurs when a ModifyDN (rename) operation uses an a… |
| 2026-10-29 07:16:44 | [CVE-2026-117627](https://nvd.nist.gov/vuln/detail/CVE-2026-117627) | Medium | 5.4 | A flaw was found in the JWT Authorization Grant implementation of the keycloak-services component. When an OIDC or Goog… |
| 2026-10-29 07:16:44 | [CVE-2026-117688](https://nvd.nist.gov/vuln/detail/CVE-2026-117688) | Medium | 5.3 | A flaw was found in the client registration component of Keycloak, an open-source identity and access management soluti… |
| 2026-10-29 07:16:44 | [CVE-2026-117859](https://nvd.nist.gov/vuln/detail/CVE-2026-117859) | Medium | 5.4 | A flaw was found in the Pushed Authorization Request PAR implementation of the keycloak-services component. The issue o… |
| 2026-10-29 07:16:44 | [CVE-2026-118030](https://nvd.nist.gov/vuln/detail/CVE-2026-118030) | Medium | 4.2 | A flaw was found in the HOTP authentication mechanism of the keycloak-services component, which provides identity and a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
