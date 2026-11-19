# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 21:22 UTC

New CVEs published between 2026-11-19 20:21 UTC and 2026-11-19 21:22 UTC.

[Full CSV](data/new-cves-2026-11-19T21-22-09-45235Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 21:17:39 | [CVE-2026-102884](https://nvd.nist.gov/vuln/detail/CVE-2026-102884) | Medium | 6.3 | Connaisseur is an admission controller that integrates container image signature verification into a Kubernetes cluster… |
| 2026-11-19 21:17:40 | [CVE-2026-102945](https://nvd.nist.gov/vuln/detail/CVE-2026-102945) | Medium | 4.9 | Aether Project AMF supports termination of NAS signalling, NAS ciphering & integrity protection, registration managemen… |
| 2026-11-19 21:17:40 | [CVE-2026-103033](https://nvd.nist.gov/vuln/detail/CVE-2026-103033) | Medium | 5.3 | ALTCHA is a Go library for creating and verifying ALTCHA challenges. Prior to 2.1.0, parseServerSignature can leave Ser… |
| 2026-11-19 21:17:41 | [CVE-2026-104773](https://nvd.nist.gov/vuln/detail/CVE-2026-104773) | Medium | 6.8 | CKAN is an open-source data management system for data hubs and data portals. Prior to 2.10.11 and 2.11.6, the web user… |
| 2026-11-19 21:17:51 | [CVE-2026-129931](https://nvd.nist.gov/vuln/detail/CVE-2026-129931) | Medium | 5.7 | A component of the MongoDB Java Driver that processes connection configuration places credential values taken from that… |
| 2026-11-19 21:17:51 | [CVE-2026-129932](https://nvd.nist.gov/vuln/detail/CVE-2026-129932) | Critical | 9.1 | The MongoDB Java driver applies its DNS seedlist domain restriction to a record value that is later re-interpreted diff… |
| 2026-11-19 21:17:51 | [CVE-2026-129933](https://nvd.nist.gov/vuln/detail/CVE-2026-129933) | Medium | 6.3 | The MongoDB Java Driver does not neutralize NUL characters in the user name and password values it places into the mess… |
| 2026-11-19 21:17:52 | [CVE-2026-130151](https://nvd.nist.gov/vuln/detail/CVE-2026-130151) | High | 8.5 | Okta Privileged Access (OPA) Gateway includes a version of the FreeRDP library affected by memory management issues in… |
| 2026-11-19 21:17:53 | [CVE-2026-130153](https://nvd.nist.gov/vuln/detail/CVE-2026-130153) | Medium | 4.7 | The Okta Client SDK for Python (okta-client-python) includes client authentication values (client_secret or JWT asserti… |
| 2026-11-19 21:17:53 | [CVE-2026-130163](https://nvd.nist.gov/vuln/detail/CVE-2026-130163) | Medium | 5.9 | Collabora Online is a collaborative online office suite based on LibreOffice technology. Prior to 24.04.19.3, 25.04.13.… |
| 2026-11-19 21:17:53 | [CVE-2026-130179](https://nvd.nist.gov/vuln/detail/CVE-2026-130179) | High | 8.5 | The Okta .NET SDK Abstractions library systematically writes per-request authentication credentials to a shared HTTP cl… |
| 2026-11-19 21:17:53 | [CVE-2026-130233](https://nvd.nist.gov/vuln/detail/CVE-2026-130233) | Medium | 6.8 | The Okta .NET SDK Abstractions library improperly synchronizes authentication credentials set on a shared HTTP client d… |
| 2026-11-19 21:17:53 | [CVE-2026-130234](https://nvd.nist.gov/vuln/detail/CVE-2026-130234) | High | 8.0 | The Okta Swift Management SDK does not percent-encode forward slash (/) characters during path parameter interpolation.… |
| 2026-11-19 21:17:53 | [CVE-2026-130235](https://nvd.nist.gov/vuln/detail/CVE-2026-130235) | High | 8.7 | In the Okta .NET SDK Abstractions library, outbound HTTP requests are not restricted to the configured Okta organizatio… |
| 2026-11-19 21:17:54 | [CVE-2026-130236](https://nvd.nist.gov/vuln/detail/CVE-2026-130236) | High | 8.5 | In the Auth0 Authorization Extension, request authentication handling can process claims from query parameters independ… |
| 2026-11-19 21:17:57 | [CVE-2026-132607](https://nvd.nist.gov/vuln/detail/CVE-2026-132607) | Medium | 6.0 | Insufficient verification of data authenticity in the decryption component of Amazon S3 Encryption Client for PHP in AW… |
| 2026-11-19 21:18:00 | [CVE-2026-133201](https://nvd.nist.gov/vuln/detail/CVE-2026-133201) | High | 8.7 | A vulnerability was determined in smartalock wireguard-lwip up to cfba91666590e86bd67842c71cedf9a423be823a. Impacted is… |
| 2026-11-19 21:18:01 | [CVE-2026-14879](https://nvd.nist.gov/vuln/detail/CVE-2026-14879) | Medium | 6.5 | IBM watsonx.data 2.4.0 through 2.4.0 patch 8 does not invalidate session after a logout which could allow an authentica… |
| 2026-11-19 21:18:01 | [CVE-2026-14880](https://nvd.nist.gov/vuln/detail/CVE-2026-14880) | Medium | 5.3 | IBM watsonx.data 2.4.0 through 2.4.0 patch 8 could allow unauthorized network access due to insufficient network segmen… |
| 2026-11-19 21:18:01 | [CVE-2026-14885](https://nvd.nist.gov/vuln/detail/CVE-2026-14885) | Medium | 4.8 | IBM watsonx.data 2.4.0 through 2.4.0 patch 8 could allow a remote attacker to obtain sensitive information due to impro… |
| 2026-11-19 21:18:02 | [CVE-2026-16319](https://nvd.nist.gov/vuln/detail/CVE-2026-16319) | Medium | 4.3 | IBM API Connect 10.0.8.0 through 10.0.8.13 could allow a remote authenticated attacker to delete API keys belonging to… |
| 2026-11-19 21:18:02 | [CVE-2026-53526](https://nvd.nist.gov/vuln/detail/CVE-2026-53526) | Medium | 5.7 | Reposilite is lightweight and easy-to-use repository management software dedicated to Maven-based artifacts in the JVM… |
| 2026-11-19 21:18:03 | [CVE-2026-62955](https://nvd.nist.gov/vuln/detail/CVE-2026-62955) | High | 7.2 | baserCMS is a website development framework. From 5.2.3 until 5.3.0, BcThemeFileService::getFullpath() in plugins/bc-th… |
| 2026-11-19 21:18:03 | [CVE-2026-63012](https://nvd.nist.gov/vuln/detail/CVE-2026-63012) | Medium | 6.5 | baserCMS is a website development framework. Prior to 5.3.0, getAuthenticationService permits an Api/Admin session auth… |
| 2026-11-19 21:18:03 | [CVE-2026-75801](https://nvd.nist.gov/vuln/detail/CVE-2026-75801) | Medium | 6.2 | IBM watsonx.data 2.4.0 through 2.4.0 patch 8 could allow a local attacker to obtain sensitive credentials due to the us… |
| 2026-11-19 21:18:05 | [CVE-2026-82339](https://nvd.nist.gov/vuln/detail/CVE-2026-82339) | Critical | 9.1 | IBM Guardium Data Protection 12.2 is vulnerable to missing authentication in the SharePoint S-TAP RelayService, allowin… |
| 2026-11-19 21:18:05 | [CVE-2026-82342](https://nvd.nist.gov/vuln/detail/CVE-2026-82342) | High | 8.1 | IBM Guardium Data Protection 12.2 is vulnerable to a stack-based buffer overflow when processing a specially crafted PR… |
| 2026-11-19 21:18:05 | [CVE-2026-83631](https://nvd.nist.gov/vuln/detail/CVE-2026-83631) | Medium | 6.8 | On Intel-based macOS systems, the Okta Device Access (ODA) component of Okta Verify for macOS configures a LaunchDaemon… |
| 2026-11-19 21:18:05 | [CVE-2026-84065](https://nvd.nist.gov/vuln/detail/CVE-2026-84065) | Medium | 6.5 | IBM Guardium Data Protection 12.2 could allow a remote attacker to obtain sensitive information or cause a denial of se… |
| 2026-11-19 21:18:05 | [CVE-2026-84087](https://nvd.nist.gov/vuln/detail/CVE-2026-84087) | High | 7.8 | IBM Guardium Data Protection 12.2 is vulnerable to local privilege escalation via the SUID-root podman_wrapper binary o… |
| 2026-11-19 21:18:05 | [CVE-2026-84211](https://nvd.nist.gov/vuln/detail/CVE-2026-84211) | Medium | 5.9 | IBM Guardium Data Protection 12.2 could allow a remote attacker to inject forged audit records due to improper output n… |
| 2026-11-19 21:18:06 | [CVE-2026-84236](https://nvd.nist.gov/vuln/detail/CVE-2026-84236) | Critical | 9.8 | IBM Guardium Data Protection 12.2 is vulnerable to insecure deserialization in the SharePoint Tap MulticastTransceiver… |
| 2026-11-19 21:18:06 | [CVE-2026-84273](https://nvd.nist.gov/vuln/detail/CVE-2026-84273) | High | 8.1 | IBM Guardium Data Protection 12.2 is vulnerable to path traversal in the datasource functionality. An authenticated att… |
| 2026-11-19 21:18:06 | [CVE-2026-85018](https://nvd.nist.gov/vuln/detail/CVE-2026-85018) | High | 8.1 | IBM Guardium Data Protection 12.2 is vulnerable to improper TLS certificate validation in the GDP Terraform provider, a… |
| 2026-11-19 21:18:06 | [CVE-2026-87977](https://nvd.nist.gov/vuln/detail/CVE-2026-87977) | Critical | 9.8 | IBM Guardium Data Protection 12.2 is vulnerable to SQL injection in the edge-controller component. An unauthenticated r… |
| 2026-11-19 21:18:06 | [CVE-2026-92906](https://nvd.nist.gov/vuln/detail/CVE-2026-92906) | Medium | 5.5 | IBM watsonx.data 2.4.0 through 2.4.0 patch 8 could allow a remote authenticated attacker to cause a denial of service d… |
| 2026-11-19 21:18:06 | [CVE-2026-92907](https://nvd.nist.gov/vuln/detail/CVE-2026-92907) | Medium | 4.3 | IBM watsonx.data 2.4.0 through 2.4.0 patch 8 could allow a remote authenticated attacker to conduct a server-side reque… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
