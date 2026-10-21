# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 09:18 UTC

New CVEs published between 2026-10-21 08:18 UTC and 2026-10-21 09:18 UTC.

[Full CSV](data/new-cves-2026-10-21T09-18-59-214559Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 09:17:05 | [CVE-2026-101138](https://nvd.nist.gov/vuln/detail/CVE-2026-101138) | Medium | 5.3 | The CMP – Coming Soon & Maintenance WordPress plugin before 4.1.21 does not correctly apply maintenance mode to pages a… |
| 2026-10-21 09:17:05 | [CVE-2026-103301](https://nvd.nist.gov/vuln/detail/CVE-2026-103301) | Medium | 5.3 | The Payment Gateway for Telcell WordPress plugin before 2.0.5 does not verify the authenticity of incoming payment noti… |
| 2026-10-21 09:17:05 | [CVE-2026-104641](https://nvd.nist.gov/vuln/detail/CVE-2026-104641) | Medium | 5.3 | The Simple Shopping Cart WordPress plugin before 5.3.3 does not verify that a PayPal payment notification is for a paym… |
| 2026-10-21 09:17:06 | [CVE-2026-104642](https://nvd.nist.gov/vuln/detail/CVE-2026-104642) | Low | 2.7 | The Simple Shopping Cart WordPress plugin before 5.3.3 does not verify submitted product prices against a value only th… |
| 2026-10-21 09:17:06 | [CVE-2026-105256](https://nvd.nist.gov/vuln/detail/CVE-2026-105256) | Medium | 5.3 | The LatePoint WordPress plugin before 5.7.5 does not validate the client-supplied value that determines how much is cha… |
| 2026-10-21 09:17:06 | [CVE-2026-107447](https://nvd.nist.gov/vuln/detail/CVE-2026-107447) | Medium | 5.3 | The Contest Gallery WordPress plugin before 34.0.1 does not reliably validate the visitor identity used to enforce its… |
| 2026-10-21 09:17:06 | [CVE-2026-109125](https://nvd.nist.gov/vuln/detail/CVE-2026-109125) | Medium | 5.3 | In NLnet Labs Unbound up to and including version 1.26.1, an observable cache-level side-channel can be exposed with 'u… |
| 2026-10-21 09:17:06 | [CVE-2026-110938](https://nvd.nist.gov/vuln/detail/CVE-2026-110938) | High | 8.7 | In Eclipse OpenJ9 versions up to 0.63.0, the JITServer component is vulnerable to denial of service due to improper bou… |
| 2026-10-21 09:17:06 | [CVE-2026-114236](https://nvd.nist.gov/vuln/detail/CVE-2026-114236) | Low | 3.3 | storage/pkg/archive.ApplyLayer and ApplyUncompressedLayer may, when processing corrupt or malicious inputs, leak a file… |
| 2026-10-21 09:17:07 | [CVE-2026-14556](https://nvd.nist.gov/vuln/detail/CVE-2026-14556) | Medium | 5.4 | The HappyForms WordPress plugin before 1.26.15 does not sanitise or escape a user-controlled referral value before embe… |
| 2026-10-21 09:17:07 | [CVE-2026-35501](https://nvd.nist.gov/vuln/detail/CVE-2026-35501) | Low | 3.7 | When NLnet Labs Unbound 1.0.1 up to and including version 1.26.1 is configured with both a root trust anchor and an add… |
| 2026-10-21 09:17:07 | [CVE-2026-50106](https://nvd.nist.gov/vuln/detail/CVE-2026-50106) | Medium | 6.5 | When NLnet Labs Unbound up to and including version 1.26.1 is configured with both a root trust anchor and an additiona… |
| 2026-10-21 09:17:07 | [CVE-2026-70386](https://nvd.nist.gov/vuln/detail/CVE-2026-70386) | High | 8.5 | Improper neutralization of special elements used in an OS command ('OS command injection') and Missing Authorization vu… |
| 2026-10-21 09:17:07 | [CVE-2026-70387](https://nvd.nist.gov/vuln/detail/CVE-2026-70387) | High | 8.4 | Exposed dangerous method or function and Incorrect Authorization vulnerability in OnePlus OxygenOS on Android. The olc2… |
| 2026-10-21 09:17:08 | [CVE-2026-85683](https://nvd.nist.gov/vuln/detail/CVE-2026-85683) | High | 8.8 | The Jane Menu WordPress plugin before 1.5.1 does not have any capability or nonce checks on one of its form handlers, w… |
| 2026-10-21 09:17:08 | [CVE-2026-96405](https://nvd.nist.gov/vuln/detail/CVE-2026-96405) | Medium | 5.3 | NLnet Labs Unbound up to and including version 1.26.1 limits compression-pointer traversal for each individual domain-n… |
| 2026-10-21 09:17:08 | [CVE-2026-97206](https://nvd.nist.gov/vuln/detail/CVE-2026-97206) | High | 7.5 | NLnet Labs Unbound, 1.22.0 up to and including version 1.26.1, contains a DNS-over-QUIC (DoQ) lifetime bug reachable by… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
