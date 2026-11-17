# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-17 14:18 UTC

New CVEs published between 2026-11-17 13:19 UTC and 2026-11-17 14:18 UTC.

[Full CSV](data/new-cves-2026-11-17T14-18-19-643532Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-17 14:17:32 | [CVE-2026-107190](https://nvd.nist.gov/vuln/detail/CVE-2026-107190) | High | 7.0 | Bludit is vulnerable to Path Traversal in the page deletion functionality. An authenticated user with the Author role c… |
| 2026-11-17 14:17:44 | [CVE-2026-130385](https://nvd.nist.gov/vuln/detail/CVE-2026-130385) | Low | 2.3 | Weblate 2026.11 through 2026.11.2 contains a time-of-check time-of-use race condition in the GET /api/tasks/{pk}/ endpo… |
| 2026-11-17 14:17:44 | [CVE-2026-130386](https://nvd.nist.gov/vuln/detail/CVE-2026-130386) | High | 8.3 | Contiki-NG through 5.2 contains an out-of-bounds access vulnerability in buffer_reclaim() and domain_set_free() in mpl.… |
| 2026-11-17 14:17:44 | [CVE-2026-130387](https://nvd.nist.gov/vuln/detail/CVE-2026-130387) | Medium | 6.9 | Contiki-NG through 5.2 contains an out-of-bounds read vulnerability in coap_remove_observer_by_uri() that allows unauth… |
| 2026-11-17 14:17:44 | [CVE-2026-130583](https://nvd.nist.gov/vuln/detail/CVE-2026-130583) | Critical | 9.2 | Rootways Authorize.net CIM Pro extension for Magento 2 before 4.1.5 contains an unauthenticated server-side request for… |
| 2026-11-17 14:17:45 | [CVE-2026-130584](https://nvd.nist.gov/vuln/detail/CVE-2026-130584) | High | 8.7 | Xibo CMS before 4.5.3 contains an insecure direct object reference vulnerability that allows authenticated users to acc… |
| 2026-11-17 14:17:45 | [CVE-2026-130585](https://nvd.nist.gov/vuln/detail/CVE-2026-130585) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-17 14:17:45 | [CVE-2026-130586](https://nvd.nist.gov/vuln/detail/CVE-2026-130586) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-17 14:17:45 | [CVE-2026-130587](https://nvd.nist.gov/vuln/detail/CVE-2026-130587) | Critical | 9.4 | OpenFunction through 1.2.0 contains a privilege escalation vulnerability that allows namespace tenants to create privil… |
| 2026-11-17 14:17:45 | [CVE-2026-130588](https://nvd.nist.gov/vuln/detail/CVE-2026-130588) | High | 7.1 | OpenFunction through 1.2.0 contains a NULL pointer dereference vulnerability in getServingRun that allows users permitt… |
| 2026-11-17 14:17:45 | [CVE-2026-130589](https://nvd.nist.gov/vuln/detail/CVE-2026-130589) | High | 8.6 | Emitter through 3.1 contains a privilege escalation vulnerability that allows any channel key holder to forge a master… |
| 2026-11-17 14:17:45 | [CVE-2026-130590](https://nvd.nist.gov/vuln/detail/CVE-2026-130590) | Medium | 5.3 | react-native-webview 11.25.1 through 17.1.0 on Android contains a denial of service vulnerability that allows web conte… |
| 2026-11-17 14:17:46 | [CVE-2026-130591](https://nvd.nist.gov/vuln/detail/CVE-2026-130591) | High | 8.7 | 53AIHub before 0.5.5 contains a missing authentication vulnerability that allows unauthenticated attackers to read file… |
| 2026-11-17 14:17:46 | [CVE-2026-130592](https://nvd.nist.gov/vuln/detail/CVE-2026-130592) | Medium | 5.1 | phpMyFAQ 4.0.12 through 4.0.19, 4.1.x before 4.1.12, and 4.2.0 pre-releases before 4.2.0-RC.1 contain a stored cross-si… |
| 2026-11-17 14:17:46 | [CVE-2026-130593](https://nvd.nist.gov/vuln/detail/CVE-2026-130593) | Medium | 5.1 | Scalar scalar-ninja 0.1.0 before 0.3.3 contains a cross-site scripting vulnerability in get_scalar_api_reference() that… |
| 2026-11-17 14:17:46 | [CVE-2026-130594](https://nvd.nist.gov/vuln/detail/CVE-2026-130594) | Medium | 5.1 | Scalar scalar-ninja 0.1.0 before 0.3.3 contains a cross-site scripting vulnerability that allows attackers to inject sc… |
| 2026-11-17 14:17:46 | [CVE-2026-130595](https://nvd.nist.gov/vuln/detail/CVE-2026-130595) | Medium | 6.0 | SQLBot 1.10.0 through 1.10.3 fails to apply its PostgreSQL dangerous-function denylist because DS_SPECIFIC_DANGEROUS_FU… |
| 2026-11-17 14:17:46 | [CVE-2026-130596](https://nvd.nist.gov/vuln/detail/CVE-2026-130596) | Medium | 6.3 | FusionPBX through 5.6.5 contains a path traversal vulnerability in app/fax/fax_emails.php that allows unauthenticated r… |
| 2026-11-17 14:17:47 | [CVE-2026-130603](https://nvd.nist.gov/vuln/detail/CVE-2026-130603) | Critical | 9.3 | Eclipse Zenoh's zenoh-pico implementation, versions 0.7.2-rc up to but excluding 1.10.2, does not validate the Zenoh id… |
| 2026-11-17 14:17:47 | [CVE-2026-130608](https://nvd.nist.gov/vuln/detail/CVE-2026-130608) | High | 8.1 | When using the admin area profile form to change ones profile details *except* the password (so, email or username), th… |
| 2026-11-17 14:17:47 | [CVE-2026-130615](https://nvd.nist.gov/vuln/detail/CVE-2026-130615) | High | 7.6 | Flowise through 3.1.4 contains a server-side request forgery vulnerability that allows authenticated users to reach int… |
| 2026-11-17 14:17:47 | [CVE-2026-82025](https://nvd.nist.gov/vuln/detail/CVE-2026-82025) | High | 8.6 | WP File Manager before 8.0.7 contains a file upload restriction bypass vulnerability that allows authenticated administ… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
