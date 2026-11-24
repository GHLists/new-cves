# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 01:19 UTC

New CVEs published between 2026-11-24 00:18 UTC and 2026-11-24 01:19 UTC.

[Full CSV](data/new-cves-2026-11-24T01-19-42-734706Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 01:17:22 | [CVE-2026-132270](https://nvd.nist.gov/vuln/detail/CVE-2026-132270) | Medium | 4.3 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-24 01:17:23 | [CVE-2026-133448](https://nvd.nist.gov/vuln/detail/CVE-2026-133448) | High | 7.1 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-24 01:17:31 | [CVE-2026-135419](https://nvd.nist.gov/vuln/detail/CVE-2026-135419) | Low | 2.1 | A vulnerability was determined in itsourcecode Airline Reservation System 1.0. This affects an unknown part of the file… |
| 2026-11-24 01:17:31 | [CVE-2026-135684](https://nvd.nist.gov/vuln/detail/CVE-2026-135684) | Low | 2.3 | SparkyFitness before 1.12.0 contains a missing ownership check in getNutritionixHeaders that allows authenticated users… |
| 2026-11-24 01:17:31 | [CVE-2026-135685](https://nvd.nist.gov/vuln/detail/CVE-2026-135685) | Low | 2.3 | SparkyFitness before 1.12.0 contains a weak password change vulnerability that allows attackers with a victim's session… |
| 2026-11-24 01:17:31 | [CVE-2026-135686](https://nvd.nist.gov/vuln/detail/CVE-2026-135686) | Critical | 9.1 | Trilium through 0.107.0 contains an sql injection vulnerability in updateNormalEntity() that allows malicious sync part… |
| 2026-11-24 01:17:32 | [CVE-2026-135687](https://nvd.nist.gov/vuln/detail/CVE-2026-135687) | Low | 2.3 | Arcane before 3.0.0 fails to enforce the requiresPasswordChange account flag on the server, allowing attackers with ini… |
| 2026-11-24 01:17:32 | [CVE-2026-135688](https://nvd.nist.gov/vuln/detail/CVE-2026-135688) | Medium | 6.9 | Idno through 1.6.4 contains an unauthenticated blind server-side request forgery vulnerability in the /webmention/ endp… |
| 2026-11-24 01:17:32 | [CVE-2026-135689](https://nvd.nist.gov/vuln/detail/CVE-2026-135689) | High | 8.6 | Community Store for Concrete CMS before 2.8.0 contains a stored cross-site scripting vulnerability that allows unauthen… |
| 2026-11-24 01:17:32 | [CVE-2026-135690](https://nvd.nist.gov/vuln/detail/CVE-2026-135690) | Medium | 6.3 | CivetWeb through 1.16 built with USE_HTTP2 and enable_http2 contains a heap out-of-bounds read vulnerability in hpack_d… |
| 2026-11-24 01:17:32 | [CVE-2026-135691](https://nvd.nist.gov/vuln/detail/CVE-2026-135691) | High | 8.7 | Open5GS WebUI through 2.8.0 contains an incorrect authorization vulnerability in webui/server/routes/db.js that allows… |
| 2026-11-24 01:17:32 | [CVE-2026-135692](https://nvd.nist.gov/vuln/detail/CVE-2026-135692) | High | 8.7 | rConfig Core 8.0.0 before 8.2.17 and rConfig Pro before 8.4.0 contain a PHP object injection vulnerability in app/Casts… |
| 2026-11-24 01:17:33 | [CVE-2026-135693](https://nvd.nist.gov/vuln/detail/CVE-2026-135693) | Critical | 9.3 | rConfig Core 8.0.0 before 8.2.17 and rConfig Pro before 8.4.0 contain a stored cross-site scripting vulnerability in th… |
| 2026-11-24 01:17:33 | [CVE-2026-135694](https://nvd.nist.gov/vuln/detail/CVE-2026-135694) | High | 7.1 | rConfig Core 8.1.0 before 8.2.20 and rConfig Pro before 8.4.0 contain a missing authorization vulnerability in ExportCo… |
| 2026-11-24 01:17:33 | [CVE-2026-135695](https://nvd.nist.gov/vuln/detail/CVE-2026-135695) | High | 8.7 | rConfig Core 8.0.0 before 8.2.13 and rConfig Pro before 8.4.0 contain an authorization bypass vulnerability in the user… |
| 2026-11-24 01:17:33 | [CVE-2026-135696](https://nvd.nist.gov/vuln/detail/CVE-2026-135696) | High | 7.7 | rConfig Core 8.2.19 before 8.2.22 contains a server-side request forgery vulnerability that allows authenticated users… |
| 2026-11-24 01:17:33 | [CVE-2026-135697](https://nvd.nist.gov/vuln/detail/CVE-2026-135697) | Medium | 6.9 | CleverReach WP before 1.5.28 contains a missing authorization vulnerability in the Article_Search controller that allow… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
