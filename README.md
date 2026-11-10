# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 15:22 UTC

New CVEs published between 2026-11-10 14:18 UTC and 2026-11-10 15:22 UTC.

[Full CSV](data/new-cves-2026-11-10T15-22-02-956607Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 15:17:12 | [CVE-2026-111263](https://nvd.nist.gov/vuln/detail/CVE-2026-111263) |  |  | Authentication configured for an EJB JAX-WS endpoint in the TomEE deployment descriptor is not enforced when the endpoi… |
| 2026-11-10 15:17:12 | [CVE-2026-111264](https://nvd.nist.gov/vuln/detail/CVE-2026-111264) |  |  | The security constraint generated for EJB JAX-WS endpoints with configured authentication protects only some HTTP metho… |
| 2026-11-10 15:17:12 | [CVE-2026-113422](https://nvd.nist.gov/vuln/detail/CVE-2026-113422) | High | 7.7 | In Eclipse Kura versions 5.0.0 through 5.6.2, the Wire Graph update functionality of the Kura Web UI, and the Wire Serv… |
| 2026-11-10 15:17:12 | [CVE-2026-114359](https://nvd.nist.gov/vuln/detail/CVE-2026-114359) | High | 7.0 | Eclipse Kura downloads deployment packages (DPs) from a remote URL without any limit on the size of the data it receive… |
| 2026-11-10 15:17:12 | [CVE-2026-111262](https://nvd.nist.gov/vuln/detail/CVE-2026-111262) |  |  | The Jakarta Security LDAP identity store does not neutralize special characters in the caller name before using it in d… |
| 2026-11-10 15:17:15 | [CVE-2026-121885](https://nvd.nist.gov/vuln/detail/CVE-2026-121885) | Medium | 6.5 | A flaw was found in Podman. An attacker can trigger a Denial of Service (DoS) by supplying a container image containing… |
| 2026-11-10 15:17:16 | [CVE-2026-123082](https://nvd.nist.gov/vuln/detail/CVE-2026-123082) | Medium | 5.7 | Docker Desktop before version 4.94.0 could write the signed-in user's Docker Hub access token (a JWT) in cleartext to a… |
| 2026-11-10 15:17:30 | [CVE-2026-86532](https://nvd.nist.gov/vuln/detail/CVE-2026-86532) |  |  | The bundled JAAS login modules leak whether a username exists and compare credentials in a non-constant-time manner. A… |
| 2026-11-10 15:17:30 | [CVE-2026-86811](https://nvd.nist.gov/vuln/detail/CVE-2026-86811) |  |  | The stateful session bean passivation mechanism derives the on-disk file name from a client-supplied identifier without… |
| 2026-11-10 15:17:30 | [CVE-2026-87755](https://nvd.nist.gov/vuln/detail/CVE-2026-87755) |  |  | Stateful session bean identifiers are not generated from a cryptographically secure random source. A remote attacker wi… |
| 2026-11-10 15:17:30 | [CVE-2026-87756](https://nvd.nist.gov/vuln/detail/CVE-2026-87756) |  |  | The internal system EJBs used for remote deployment and configuration did not enforce their administrative role check w… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
