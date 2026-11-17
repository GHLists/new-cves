# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-17 15:18 UTC

New CVEs published between 2026-11-17 14:18 UTC and 2026-11-17 15:18 UTC.

[Full CSV](data/new-cves-2026-11-17T15-18-18-902549Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-17 15:17:32 | [CVE-2026-118789](https://nvd.nist.gov/vuln/detail/CVE-2026-118789) | High | 8.1 | Farmasimplex retrieves a CIP News file over HTTP and executes embedded SQL statements against the local FarmaCIP databa… |
| 2026-11-17 15:17:33 | [CVE-2026-123050](https://nvd.nist.gov/vuln/detail/CVE-2026-123050) | High | 7.1 | Multiple Farmasimplex healthcare integration modules do not properly validate TLS certificates, allowing an attacker wh… |
| 2026-11-17 15:17:33 | [CVE-2026-123051](https://nvd.nist.gov/vuln/detail/CVE-2026-123051) | Low | 1.2 | The REV.exe module distributed with Farmasimplex contains embedded OAuth client credentials for integration with the IZ… |
| 2026-11-17 15:17:34 | [CVE-2026-123052](https://nvd.nist.gov/vuln/detail/CVE-2026-123052) | Medium | 4.7 | The CeliachiaRL integration component distributed with Farmasimplex uses shared OAuth credentials across multiple custo… |
| 2026-11-17 15:17:40 | [CVE-2026-130626](https://nvd.nist.gov/vuln/detail/CVE-2026-130626) | High | 7.5 | The core JDK HTTP client (a2a-java-sdk-http-client) applies the GHSA-9rhm redirect-neutralization only to the POST path… |
| 2026-11-17 15:17:40 | [CVE-2026-130627](https://nvd.nist.gov/vuln/detail/CVE-2026-130627) | High | 7.5 | The Vert.x HTTP client transport (a2a-java-sdk-http-client-vertx) hand-rolls a POST redirect follower that, when the do… |
| 2026-11-17 15:17:40 | [CVE-2026-130628](https://nvd.nist.gov/vuln/detail/CVE-2026-130628) | Medium | 5.3 | react-native-webview 13.7.0 through 17.1.0 on Windows contains an unrestricted URI scheme launch vulnerability in the W… |
| 2026-11-17 15:17:40 | [CVE-2026-130629](https://nvd.nist.gov/vuln/detail/CVE-2026-130629) | Low | 2.3 | react-native-webview 13.8.0 through 17.1.0 contains a code injection vulnerability that allows attackers to execute Jav… |
| 2026-11-17 15:17:40 | [CVE-2026-130630](https://nvd.nist.gov/vuln/detail/CVE-2026-130630) | Medium | 6.8 | GPAC 26.02.0 contains a NULL pointer dereference vulnerability in dasher_configure_pid() in src/filters/dasher.c that d… |
| 2026-11-17 15:17:40 | [CVE-2026-130631](https://nvd.nist.gov/vuln/detail/CVE-2026-130631) | Medium | 6.8 | GPAC before 26.07.0 contains an uninitialized pointer access vulnerability in GetESD() in src/isomedia/track.c that all… |
| 2026-11-17 15:17:40 | [CVE-2026-130632](https://nvd.nist.gov/vuln/detail/CVE-2026-130632) | Medium | 6.8 | GPAC before 26.02.0 contains an out-of-bounds read vulnerability in m2tsdmx_send_packet() in src/filters/dmx_m2ts.c cau… |
| 2026-11-17 15:17:41 | [CVE-2026-130633](https://nvd.nist.gov/vuln/detail/CVE-2026-130633) | Medium | 6.8 | GPAC before 26.02.0 contains a use-after-free vulnerability in gf_filter_pid_set_args_internal() that leaves a stale po… |
| 2026-11-17 15:17:41 | [CVE-2026-130634](https://nvd.nist.gov/vuln/detail/CVE-2026-130634) | Medium | 6.8 | GPAC before 26.07.0 contains a heap-based buffer overflow in gf_mpd_resolve_url() in src/media_tools/mpd.c that allows… |
| 2026-11-17 15:17:41 | [CVE-2026-130635](https://nvd.nist.gov/vuln/detail/CVE-2026-130635) | Medium | 6.8 | GPAC before 26.07.0 contains an uncontrolled recursion vulnerability in dasher_gather_deps() in src/filters/dasher.c th… |
| 2026-11-17 15:17:42 | [CVE-2026-77224](https://nvd.nist.gov/vuln/detail/CVE-2026-77224) | High | 8.7 | Camunda 7.24.0 before 7.24.14 and 7.23.0 before 7.23.17 contains an XML External Entity (XXE) injection vulnerability i… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
