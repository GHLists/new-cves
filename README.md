# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 14:18 UTC

New CVEs published between 2026-11-16 13:18 UTC and 2026-11-16 14:18 UTC.

[Full CSV](data/new-cves-2026-11-16T14-18-39-931333Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 14:17:05 | [CVE-2026-114737](https://nvd.nist.gov/vuln/detail/CVE-2026-114737) | Low | 2.3 | The fix for CVE-2026-23903 https://shiro.apache.org/security-reports.html#cve_2026_23903 was incomplete for manually-cr… |
| 2026-11-16 14:17:05 | [CVE-2026-124289](https://nvd.nist.gov/vuln/detail/CVE-2026-124289) | High | 7.5 | @fastify/multipart is the official Fastify plugin for handling multipart/form-data uploads. In versions 7.4.0 through 1… |
| 2026-11-16 14:17:06 | [CVE-2026-124724](https://nvd.nist.gov/vuln/detail/CVE-2026-124724) | High | 7.5 | @fastify/busboy is a streaming parser for multipart form data used by Fastify. In versions 1.0.0 through 3.2.5, when a… |
| 2026-11-16 14:17:06 | [CVE-2026-128835](https://nvd.nist.gov/vuln/detail/CVE-2026-128835) | High | 7.5 | @fastify/busboy is a streaming parser for multipart form data used by Fastify. In versions 1.0.0 through 3.2.5, a multi… |
| 2026-11-16 14:17:06 | [CVE-2026-128842](https://nvd.nist.gov/vuln/detail/CVE-2026-128842) | Medium | 5.3 | @fastify/busboy is a streaming parser for multipart and url-encoded form data used by Fastify. In versions 1.0.0 throug… |
| 2026-11-16 14:17:06 | [CVE-2026-128846](https://nvd.nist.gov/vuln/detail/CVE-2026-128846) | Low | 3.7 | @fastify/busboy is a streaming parser for multipart form data used by Fastify. In versions 3.2.1 through 3.2.5, the par… |
| 2026-11-16 14:17:06 | [CVE-2026-129320](https://nvd.nist.gov/vuln/detail/CVE-2026-129320) | Low | 2.1 | The shiro:principal tags in shiro-web (Jakarta Pages) and shiro-jakarta-ee (Jakarta Faces) did not escape their output,… |
| 2026-11-16 14:17:06 | [CVE-2026-129347](https://nvd.nist.gov/vuln/detail/CVE-2026-129347) | Low | 2.3 | `DefaultPasswordService` and `SimpleCredentialsMatcher` could treat an empty stored credential as a match for an empty… |
| 2026-11-16 14:17:07 | [CVE-2026-129348](https://nvd.nist.gov/vuln/detail/CVE-2026-129348) | Low | 2.3 | When PropertiesRealm reloads its properties file, removed users and narrowed permissions could remain in effect. This i… |
| 2026-11-16 14:17:07 | [CVE-2026-129690](https://nvd.nist.gov/vuln/detail/CVE-2026-129690) | High | 8.2 | The vulnerability enables any attacker with admin access to dump credentials of all accounts stored on the device, whic… |
| 2026-11-16 14:17:07 | [CVE-2026-129919](https://nvd.nist.gov/vuln/detail/CVE-2026-129919) | Low | 2.0 | Kunai, a security monitoring tool, contains a time-of-check to time-of-use (TOCTOU) race condition in its mount namespa… |
| 2026-11-16 14:17:08 | [CVE-2026-74762](https://nvd.nist.gov/vuln/detail/CVE-2026-74762) | Medium | 5.9 | Apache Shiro is vulnerable to session fixation when a user is authenticated via the "Remember me" functionality. In aff… |
| 2026-11-16 14:17:08 | [CVE-2026-74763](https://nvd.nist.gov/vuln/detail/CVE-2026-74763) | Medium | 6.3 | Authorization annotations, such as @RequiresRoles and @RequiresPermissions, are not always enforced in some class or in… |
| 2026-11-16 14:17:09 | [CVE-2026-88019](https://nvd.nist.gov/vuln/detail/CVE-2026-88019) | Medium | 6.0 | When Apache Shiro is used with the Jakarta EE integration module, the automatic form saving feature weakens the securit… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
