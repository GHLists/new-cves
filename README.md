# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-27 09:19 UTC

New CVEs published between 2026-11-27 08:21 UTC and 2026-11-27 09:19 UTC.

[Full CSV](data/new-cves-2026-11-27T09-19-37-020706Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-27 09:17:00 | [CVE-2026-115835](https://nvd.nist.gov/vuln/detail/CVE-2026-115835) | Medium | 6.5 | A flaw was found in sequoia-openpgp. The ASCII-armor reader does not limit the length of a line. Parsing an armored mes… |
| 2026-11-27 09:17:00 | [CVE-2026-115836](https://nvd.nist.gov/vuln/detail/CVE-2026-115836) | Low | 3.7 | A flaw was found in sequoia-openpgp. The default ASCII-armor parser accepts Unicode dash characters in armor framing an… |
| 2026-11-27 09:17:00 | [CVE-2026-115841](https://nvd.nist.gov/vuln/detail/CVE-2026-115841) | Medium | 5.3 | A flaw was found in sequoia-openpgp. DSA signature verification does not reject a public key with generator 1 and publi… |
| 2026-11-27 09:17:01 | [CVE-2026-132890](https://nvd.nist.gov/vuln/detail/CVE-2026-132890) | High | 8.3 | In Eclipse Dataspace Components (EDC) Connector 1.0.0-RC2 through 1.0.0-RC7, the HashiCorp Vault extension does not rej… |
| 2026-11-27 09:17:01 | [CVE-2026-133842](https://nvd.nist.gov/vuln/detail/CVE-2026-133842) | High | 8.2 | A flaw was found in Flatpak’s flatpak-system-helper. When a system-wide app, runtime, or extension uses the extra-data… |
| 2026-11-27 09:17:01 | [CVE-2026-133845](https://nvd.nist.gov/vuln/detail/CVE-2026-133845) | High | 7.3 | A flaw was found in Flatpak’s flatpak-portal. When a sandboxed application invokes Spawn() and maps two different file… |
| 2026-11-27 09:17:01 | [CVE-2026-133938](https://nvd.nist.gov/vuln/detail/CVE-2026-133938) | High | 8.6 | The backend language switch action (quick_change_language) of the JTL-Shop administration backend is executed without a… |
| 2026-11-27 09:17:01 | [CVE-2026-133939](https://nvd.nist.gov/vuln/detail/CVE-2026-133939) | High | 8.6 | The OPC (OnPage Composer) start menu, which JTL-Shop shows to logged-in backend users on storefront pages, writes the c… |
| 2026-11-27 09:17:01 | [CVE-2026-133940](https://nvd.nist.gov/vuln/detail/CVE-2026-133940) | High | 8.2 | The access rules of JTL-Shop (export/.htaccess and export/backup/.htaccess) release files with the extensions gz and zi… |
| 2026-11-27 09:17:02 | [CVE-2026-133941](https://nvd.nist.gov/vuln/detail/CVE-2026-133941) | High | 8.6 | The country manager page of the JTL-Shop administration backend (/admin/countries) writes the request parameter activeS… |
| 2026-11-27 09:17:02 | [CVE-2026-137609](https://nvd.nist.gov/vuln/detail/CVE-2026-137609) | Medium | 5.3 | In Eclipse Krazo Extensions up to and including 3.0.0, AsciiDocViewEngine passes MVC model values to Asciidoctor as doc… |
| 2026-11-27 09:17:02 | [CVE-2026-59103](https://nvd.nist.gov/vuln/detail/CVE-2026-59103) | Critical | 9.3 | MONEO ERP exposes the Ping method of its _slave JSON-RPC service over WebSocket as @rpc.openpublic, so it can be called… |
| 2026-11-27 09:17:02 | [CVE-2026-80244](https://nvd.nist.gov/vuln/detail/CVE-2026-80244) | Medium | 5.5 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Insertion of Sensitive Informa… |
| 2026-11-27 09:17:02 | [CVE-2026-80245](https://nvd.nist.gov/vuln/detail/CVE-2026-80245) | Medium | 6.3 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Buffer Copy without Checking Si… |
| 2026-11-27 09:17:02 | [CVE-2026-80246](https://nvd.nist.gov/vuln/detail/CVE-2026-80246) | Medium | 5.1 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Stack-based Buffer Overflow vul… |
| 2026-11-27 09:17:03 | [CVE-2026-80248](https://nvd.nist.gov/vuln/detail/CVE-2026-80248) | Medium | 5.5 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Cryptographic… |
| 2026-11-27 09:17:03 | [CVE-2026-80268](https://nvd.nist.gov/vuln/detail/CVE-2026-80268) | High | 7.8 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Exposure of Resource to Wrong… |
| 2026-11-27 09:17:03 | [CVE-2026-80447](https://nvd.nist.gov/vuln/detail/CVE-2026-80447) | Low | 3.3 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Use of Validation Fra… |
| 2026-11-27 09:17:03 | [CVE-2026-80448](https://nvd.nist.gov/vuln/detail/CVE-2026-80448) | High | 7.7 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Server-Side Request Forgery (SS… |
| 2026-11-27 09:17:03 | [CVE-2026-80449](https://nvd.nist.gov/vuln/detail/CVE-2026-80449) | Low | 3.6 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Neutralization of Spe… |
| 2026-11-27 09:17:03 | [CVE-2026-80450](https://nvd.nist.gov/vuln/detail/CVE-2026-80450) | High | 7.7 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Improper Certificate Validatio… |
| 2026-11-27 09:17:03 | [CVE-2026-80451](https://nvd.nist.gov/vuln/detail/CVE-2026-80451) | High | 7.8 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Use of Hard-coded Cryptographic… |
| 2026-11-27 09:17:03 | [CVE-2026-80452](https://nvd.nist.gov/vuln/detail/CVE-2026-80452) | Medium | 5.5 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Insertion of Sensitive Informa… |
| 2026-11-27 09:17:04 | [CVE-2026-80453](https://nvd.nist.gov/vuln/detail/CVE-2026-80453) | High | 8.4 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Download of Code Without Integr… |
| 2026-11-27 09:17:04 | [CVE-2026-80454](https://nvd.nist.gov/vuln/detail/CVE-2026-80454) | Low | 3.6 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Concurrent Execution using Shar… |
| 2026-11-27 09:17:04 | [CVE-2026-80455](https://nvd.nist.gov/vuln/detail/CVE-2026-80455) | Low | 2.9 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains a Missing Release of Memory after… |
| 2026-11-27 09:17:04 | [CVE-2026-80456](https://nvd.nist.gov/vuln/detail/CVE-2026-80456) | Medium | 6.6 | Dell Secure Connect Gateway - Virtual Edition, versions prior to 5.36.00.16, contains an Incorrect Permission Assignmen… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
