# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 07:20 UTC

New CVEs published between 2026-10-15 06:19 UTC and 2026-10-15 07:20 UTC.

[Full CSV](data/new-cves-2026-10-15T07-20-52-469231Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 07:17:55 | [CVE-2025-29895](https://nvd.nist.gov/vuln/detail/CVE-2025-29895) | Low | 0.6 | A NULL pointer dereference vulnerability has been reported to affect Qsync Central. If a remote attacker gains a user a… |
| 2026-10-15 07:17:55 | [CVE-2025-29896](https://nvd.nist.gov/vuln/detail/CVE-2025-29896) | Low | 0.6 | A NULL pointer dereference vulnerability has been reported to affect Qsync Central. If a remote attacker gains a user a… |
| 2026-10-15 07:17:56 | [CVE-2025-29897](https://nvd.nist.gov/vuln/detail/CVE-2025-29897) | Low | 0.6 | A buffer copy without checking size of input vulnerability has been reported to affect Qsync Central. If a remote attac… |
| 2026-10-15 07:17:56 | [CVE-2025-66272](https://nvd.nist.gov/vuln/detail/CVE-2025-66272) | Medium | 5.2 | A path traversal vulnerability has been reported to affect Video Station. If a remote attacker gains a user account, th… |
| 2026-10-15 07:17:56 | [CVE-2025-66275](https://nvd.nist.gov/vuln/detail/CVE-2025-66275) | Medium | 5.2 | A path traversal vulnerability has been reported to affect Video Station. If a remote attacker gains a user account, th… |
| 2026-10-15 07:17:57 | [CVE-2025-68404](https://nvd.nist.gov/vuln/detail/CVE-2025-68404) | Medium | 4.8 | A time-of-check time-of-use (toctou) race condition vulnerability has been reported to affect QuRouter. If exploited, t… |
| 2026-10-15 07:17:57 | [CVE-2026-101302](https://nvd.nist.gov/vuln/detail/CVE-2026-101302) |  |  | TLS 1.3 embeds the actual record type as the last non-zero byte of the decrypted payload, optionally followed by zero p… |
| 2026-10-15 07:17:57 | [CVE-2026-101303](https://nvd.nist.gov/vuln/detail/CVE-2026-101303) |  |  | The IPv6 UDP send path for unconnected sockets did not apply the jail policy of rewriting a loopback destination addres… |
| 2026-10-15 07:17:57 | [CVE-2026-101304](https://nvd.nist.gov/vuln/detail/CVE-2026-101304) |  |  | When fdescfs(4) was mounted in a jail with the "nodup" option, opening /dev/fd/N returned a descriptor that did not inh… |
| 2026-10-15 07:17:57 | [CVE-2026-101305](https://nvd.nist.gov/vuln/detail/CVE-2026-101305) |  |  | renameat(2) did not enforce FD_RESOLVE_BENEATH on its directory arguments. A jailed process could rename a directory re… |
| 2026-10-15 07:17:57 | [CVE-2026-101306](https://nvd.nist.gov/vuln/detail/CVE-2026-101306) |  |  | SCM_RIGHTS file descriptor passing did not preserve FD_RESOLVE_BENEATH when a descriptor was transferred. A process cou… |
| 2026-10-15 07:17:57 | [CVE-2026-101307](https://nvd.nist.gov/vuln/detail/CVE-2026-101307) |  |  | When the PCM sample array needs to grow, the RACK stack doubles a 16-bit allocation counter. Repeated doublings caused… |
| 2026-10-15 07:17:57 | [CVE-2025-68403](https://nvd.nist.gov/vuln/detail/CVE-2025-68403) | Low | 1.0 | An external control of system or configuration setting vulnerability has been reported to affect QuRouter. If a local a… |
| 2026-10-15 07:17:58 | [CVE-2026-101308](https://nvd.nist.gov/vuln/detail/CVE-2026-101308) |  |  | When an audio channel's buffer needs to be resized, the sound(4) driver checks that the buffer is not memory-mapped and… |
| 2026-10-15 07:17:58 | [CVE-2026-103304](https://nvd.nist.gov/vuln/detail/CVE-2026-103304) |  |  | The eaSYNC Booking WordPress plugin before 1.3.31 does not perform authorization or nonce checks on several of its canc… |
| 2026-10-15 07:17:58 | [CVE-2026-103324](https://nvd.nist.gov/vuln/detail/CVE-2026-103324) | Medium | 5.3 | The Cardinity Payment Gateway for WooCommerce WordPress plugin before 3.4.2 does not properly verify the authenticity o… |
| 2026-10-15 07:17:58 | [CVE-2026-104643](https://nvd.nist.gov/vuln/detail/CVE-2026-104643) |  |  | The Easy HTTPS Redirection (SSL) WordPress plugin before 2.0.2 does not perform capability checks in some of its AJAX a… |
| 2026-10-15 07:17:58 | [CVE-2026-106031](https://nvd.nist.gov/vuln/detail/CVE-2026-106031) |  |  | The Spin Wheel WordPress plugin before 2.2.1 does not verify that a visitor actually performed a legitimate spin before… |
| 2026-10-15 07:17:58 | [CVE-2026-109145](https://nvd.nist.gov/vuln/detail/CVE-2026-109145) |  |  | The User Rights Access Manager WordPress plugin through 1.1.3 does not restrict access to one of its AJAX account-regis… |
| 2026-10-15 07:17:58 | [CVE-2026-110933](https://nvd.nist.gov/vuln/detail/CVE-2026-110933) | Medium | 4.4 | Uncaught exception vulnerability in Samsung Open Source Vyond allows Input Data Manipulation. This issue affects Vyond:… |
| 2026-10-15 07:17:58 | [CVE-2026-110934](https://nvd.nist.gov/vuln/detail/CVE-2026-110934) | Medium | 4.4 | Improper validation of array index vulnerability in Samsung Open Source Vyond allows Input Data Manipulation. This issu… |
| 2026-10-15 07:17:58 | [CVE-2026-11905](https://nvd.nist.gov/vuln/detail/CVE-2026-11905) | Medium | 4.3 | The Elementor Website Builder – more than just a page builder plugin for WordPress is vulnerable to Sensitive Informati… |
| 2026-10-15 07:17:59 | [CVE-2026-19377](https://nvd.nist.gov/vuln/detail/CVE-2026-19377) | Medium | 6.0 | Improper certificate validation in the tunnel handshake in Cato Client allows a man-in-the-middle attacker to impersona… |
| 2026-10-15 07:17:59 | [CVE-2026-22896](https://nvd.nist.gov/vuln/detail/CVE-2026-22896) | Low | 2.2 | A cross-site scripting (XSS) vulnerability has been reported to affect Network & Virtual Switch. If a remote attacker g… |
| 2026-10-15 07:17:59 | [CVE-2026-24715](https://nvd.nist.gov/vuln/detail/CVE-2026-24715) | Low | 1.3 | An observable timing discrepancy vulnerability has been reported to affect QuRouter. If exploited, the vulnerability co… |
| 2026-10-15 07:17:59 | [CVE-2026-24718](https://nvd.nist.gov/vuln/detail/CVE-2026-24718) | Low | 1.3 | A path traversal vulnerability has been reported to affect Qsync Central. If a remote attacker gains a user account, th… |
| 2026-10-15 07:17:59 | [CVE-2026-24721](https://nvd.nist.gov/vuln/detail/CVE-2026-24721) | Low | 1.3 | A NULL pointer dereference vulnerability has been reported to affect File Station 5. If a remote attacker gains a user… |
| 2026-10-15 07:17:59 | [CVE-2026-24722](https://nvd.nist.gov/vuln/detail/CVE-2026-24722) | Low | 1.3 | A NULL pointer dereference vulnerability has been reported to affect File Station 5. If a remote attacker gains a user… |
| 2026-10-15 07:18:00 | [CVE-2026-24723](https://nvd.nist.gov/vuln/detail/CVE-2026-24723) | Low | 1.3 | A NULL pointer dereference vulnerability has been reported to affect File Station 5. If a remote attacker gains a user… |
| 2026-10-15 07:18:00 | [CVE-2026-39993](https://nvd.nist.gov/vuln/detail/CVE-2026-39993) | Medium | 6.3 | A relative path traversal vulnerability has been reported to affect Download Station. If a remote attacker gains a user… |
| 2026-10-15 07:18:00 | [CVE-2026-41544](https://nvd.nist.gov/vuln/detail/CVE-2026-41544) | Medium | 6.3 | A path traversal vulnerability has been reported to affect QcalAgent. If a remote attacker gains a user account, they c… |
| 2026-10-15 07:18:02 | [CVE-2026-58098](https://nvd.nist.gov/vuln/detail/CVE-2026-58098) |  |  | When semop(2) blocks waiting for a semaphore condition, it releases the per-set lock and sleeps. Upon waking, it checks… |
| 2026-10-15 07:18:02 | [CVE-2026-58099](https://nvd.nist.gov/vuln/detail/CVE-2026-58099) |  |  | When copying knotes from a parent kqueue to a child, the copy code did not correctly exclude marker knotes (used intern… |
| 2026-10-15 07:18:02 | [CVE-2026-58100](https://nvd.nist.gov/vuln/detail/CVE-2026-58100) |  |  | kqueue_fork_copy_knote() indexed into the child's file descriptor table using a knote's file descriptor number without… |
| 2026-10-15 07:18:02 | [CVE-2026-74920](https://nvd.nist.gov/vuln/detail/CVE-2026-74920) |  |  | The Document Gallery WordPress plugin through 5.1.1 does not properly sanitise and escape user input before reflecting… |
| 2026-10-15 07:18:02 | [CVE-2026-76668](https://nvd.nist.gov/vuln/detail/CVE-2026-76668) | Medium | 6.3 | A security vulnerability in HPE NonStop Kernel may allow user space access to privileged or unmapped data. |
| 2026-10-15 07:18:02 | [CVE-2026-79821](https://nvd.nist.gov/vuln/detail/CVE-2026-79821) | High | 8.2 | A security vulnerability in HPE NonStop SOAP 4.0 may cause memory corruption resulting in a system down. |
| 2026-10-15 07:18:02 | [CVE-2026-79822](https://nvd.nist.gov/vuln/detail/CVE-2026-79822) | High | 7.1 | A security vulnerability in HPE NonStop TNS/X Native Inspect may cause corruption of address and potentially redirect e… |
| 2026-10-15 07:18:03 | [CVE-2026-81534](https://nvd.nist.gov/vuln/detail/CVE-2026-81534) | High | 8.8 | The Email Customizer for WooCommerce (Pro) plugin for WordPress is vulnerable to Remote Code Execution in versions up t… |
| 2026-10-15 07:18:03 | [CVE-2026-92428](https://nvd.nist.gov/vuln/detail/CVE-2026-92428) | Medium | 5.3 | The Rede Itaú for WooCommerce WordPress plugin before 5.5.3 does not verify the authenticity of a payment gateway webho… |
| 2026-10-15 07:18:03 | [CVE-2026-92429](https://nvd.nist.gov/vuln/detail/CVE-2026-92429) | Medium | 5.3 | The Rede Itaú for WooCommerce WordPress plugin before 5.5.3 does not verify the authenticity of a payment gateway webho… |
| 2026-10-15 07:18:03 | [CVE-2026-96537](https://nvd.nist.gov/vuln/detail/CVE-2026-96537) |  |  | The Tutor LMS WordPress plugin before 4.1.1 does not perform a capability check in a routine that regenerates its manag… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
