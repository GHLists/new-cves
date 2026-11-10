# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 23:18 UTC

New CVEs published between 2026-11-10 22:18 UTC and 2026-11-10 23:18 UTC.

[Full CSV](data/new-cves-2026-11-10T23-18-51-625567Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 22:19:17 | [CVE-2026-67175](https://nvd.nist.gov/vuln/detail/CVE-2026-67175) | Medium | 5.1 | Chargemap contains a stored cross-site scripting vulnerability that allows a remote, authenticated attacker to craft a… |
| 2026-11-10 22:19:17 | [CVE-2026-67176](https://nvd.nist.gov/vuln/detail/CVE-2026-67176) | Medium | 5.1 | Chargemap contains an open redirect vulnerability in the authentication login endpoint. A remote, unauthenticated attac… |
| 2026-11-10 22:19:18 | [CVE-2026-67177](https://nvd.nist.gov/vuln/detail/CVE-2026-67177) | Medium | 5.1 | Chargemap contains a stored cross site scripting vulnerability. A remote, unauthenticated attacker could craft a payloa… |
| 2026-11-10 22:20:53 | [CVE-2026-77685](https://nvd.nist.gov/vuln/detail/CVE-2026-77685) | High | 8.3 | The RFCOMM multiplexer control-channel handler in subsys/bluetooth/host/classic/rfcomm.c computed the echo length for a… |
| 2026-11-10 22:21:05 | [CVE-2026-82391](https://nvd.nist.gov/vuln/detail/CVE-2026-82391) | Critical | 9.1 | The HTTP/2 front-end of the Zephyr HTTP server aliased connection receive state as a scratch output. In subsys/net/lib/… |
| 2026-11-10 22:21:12 | [CVE-2026-87042](https://nvd.nist.gov/vuln/detail/CVE-2026-87042) | Medium | 6.5 | The IEEE 1588 (PTP) port implementation in subsys/net/lib/ptp/port.c adopted the logMessageInterval field of a received… |
| 2026-11-10 22:21:14 | [CVE-2026-89324](https://nvd.nist.gov/vuln/detail/CVE-2026-89324) | Critical | 9.8 | The Basel Post Types plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including,… |
| 2026-11-10 22:21:14 | [CVE-2026-90832](https://nvd.nist.gov/vuln/detail/CVE-2026-90832) | Medium | 4.3 | bt_hci_le_per_adv_report_common() in subsys/bluetooth/host/scan.c handles the HCI_LE_Periodic_Advertising_Report (and _… |
| 2026-11-10 22:21:14 | [CVE-2026-90833](https://nvd.nist.gov/vuln/detail/CVE-2026-90833) | High | 7.8 | The simulated EEPROM driver validated access ranges in eeprom_range_is_valid() (drivers/eeprom/eeprom_simulator.c) with… |
| 2026-11-10 22:21:14 | [CVE-2026-90834](https://nvd.nist.gov/vuln/detail/CVE-2026-90834) | Medium | 5.5 | The user-mode syscall verifiers for the 16-bit ("wide data") UART API in drivers/serial/uart_handlers.c validated the w… |
| 2026-11-10 22:21:14 | [CVE-2026-91000](https://nvd.nist.gov/vuln/detail/CVE-2026-91000) | High | 8.4 | Missing authentication for critical function vulnerability in N-able N-central allows Privilege Escalation. This issue… |
| 2026-11-10 22:21:14 | [CVE-2026-92439](https://nvd.nist.gov/vuln/detail/CVE-2026-92439) | High | 7.8 | The SAML plugin in Kong Gateway Enterprise does not enforce AudienceRestriction, allowing a valid assertion issued for… |
| 2026-11-10 22:21:14 | [CVE-2026-92441](https://nvd.nist.gov/vuln/detail/CVE-2026-92441) | High | 7.8 | Kong Gateway Enterprise and Kong AI Gateway include decoded CR/LF characters from the request path in the X-Forwarded-P… |
| 2026-11-10 22:21:14 | [CVE-2026-92442](https://nvd.nist.gov/vuln/detail/CVE-2026-92442) | High | 8.3 | The graphql-proxy-cache-advanced plugin in Kong Gateway Enterprise omits the caller's identity from the cache key, allo… |
| 2026-11-10 22:21:15 | [CVE-2026-92443](https://nvd.nist.gov/vuln/detail/CVE-2026-92443) | High | 8.2 | The caching plugins in Kong Gateway Enterprise and Kong AI Gateway may serve a response cached for a request carrying a… |
| 2026-11-10 22:21:15 | [CVE-2026-92545](https://nvd.nist.gov/vuln/detail/CVE-2026-92545) | High | 8.7 | The proxy-cache and proxy-cache-advanced plugins in Kong Gateway Enterprise and Kong AI Gateway omit the request hostna… |
| 2026-11-10 22:21:15 | [CVE-2026-92558](https://nvd.nist.gov/vuln/detail/CVE-2026-92558) | Medium | 6.3 | The proxy-cache and proxy-cache-advanced plugins in Kong Gateway Enterprise and Kong AI Gateway do not escape separator… |
| 2026-11-10 22:21:17 | [CVE-2026-96437](https://nvd.nist.gov/vuln/detail/CVE-2026-96437) | High | 8.2 | The ai-azure-content-safety plugin in Kong Gateway Enterprise skips inspection of request bodies larger than the in-mem… |
| 2026-11-10 23:17:18 | [CVE-2024-36309](https://nvd.nist.gov/vuln/detail/CVE-2024-36309) | Medium | 4.6 | Missing Lock Bit Protection in the Northbridge IO (NBIO) could allow a privileged attacker to use an intentionally disa… |
| 2026-11-10 23:17:18 | [CVE-2025-0008](https://nvd.nist.gov/vuln/detail/CVE-2025-0008) | High | 8.4 | Insufficient verification of data authenticity may allow a local attacker to bypass Secure Debug Unlock (SDU), potentia… |
| 2026-11-10 23:17:18 | [CVE-2025-29941](https://nvd.nist.gov/vuln/detail/CVE-2025-29941) | Medium | 6.0 | Incorrect usage of seeds in pseudo-random number generator in the Secure Encrypted Virtualization (SEV) firmware could… |
| 2026-11-10 23:17:19 | [CVE-2025-48504](https://nvd.nist.gov/vuln/detail/CVE-2025-48504) | Medium | 6.8 | Operation on a resource after expiration or release in the Secure Encrypted Virtualization (SEV) firmware could allow a… |
| 2026-11-10 23:17:19 | [CVE-2026-0003](https://nvd.nist.gov/vuln/detail/CVE-2026-0003) | Medium | 5.9 | Use of a per-part static key in the ASP Bootloader could allow an attacker to downgrade the Secure Encrypted Virtualiza… |
| 2026-11-10 23:17:19 | [CVE-2026-0435](https://nvd.nist.gov/vuln/detail/CVE-2026-0435) | Medium | 6.0 | Operation on a resource after expiration or release in the AMD Secure Encrypted Virtualization (SEV) firmware could all… |
| 2026-11-10 23:17:19 | [CVE-2026-0454](https://nvd.nist.gov/vuln/detail/CVE-2026-0454) | Medium | 4.6 | An out-of-bounds write in the AMD Secure Encrypted Virtualization (SEV) firmware could allow a malicious hypervisor to… |
| 2026-11-10 23:17:19 | [CVE-2026-0480](https://nvd.nist.gov/vuln/detail/CVE-2026-0480) | Medium | 6.0 | Missing Authentication for Critical Function in AMD Secure Encrypted Virtualization (SEV) firmware could allow a malici… |
| 2026-11-10 23:17:19 | [CVE-2026-123084](https://nvd.nist.gov/vuln/detail/CVE-2026-123084) | Medium | 6.5 | An **expression language injection** has been found in the HeaderContentGuard.permit function in publication.py of the… |
| 2026-11-10 23:17:20 | [CVE-2026-126187](https://nvd.nist.gov/vuln/detail/CVE-2026-126187) | Critical | 9.5 | React is a JavaScript library for building user interfaces. From 19.0.0 until 19.0.9, 19.1.10, 19.2.9, and 19.3.1, the… |
| 2026-11-10 23:17:20 | [CVE-2026-126261](https://nvd.nist.gov/vuln/detail/CVE-2026-126261) | Critical | 9.8 | A improper authorization vulnerability in Fortinet FortiManager 8.0.0, FortiManager 7.6.0 through 7.6.7, FortiManager 7… |
| 2026-11-10 23:17:21 | [CVE-2026-20183](https://nvd.nist.gov/vuln/detail/CVE-2026-20183) | Medium | 4.3 | A vulnerability in the web-based management interface of Cisco Identity Services Engine (ISE) could allow an authentica… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
