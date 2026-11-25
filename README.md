# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 22:20 UTC

New CVEs published between 2026-11-25 21:19 UTC and 2026-11-25 22:20 UTC.

[Full CSV](data/new-cves-2026-11-25T22-20-00-619268Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 22:17:16 | [CVE-2026-116681](https://nvd.nist.gov/vuln/detail/CVE-2026-116681) | High | 7.5 | NocoDB is software for building databases as spreadsheets. Prior to 2026.08.0, the row-scoped endpoints of a public sha… |
| 2026-11-25 22:17:16 | [CVE-2026-127930](https://nvd.nist.gov/vuln/detail/CVE-2026-127930) | Medium | 5.8 | Incorrect authorization in affected versions of network-manager in Ubuntu allows a local attacker with code execution a… |
| 2026-11-25 22:17:16 | [CVE-2026-133445](https://nvd.nist.gov/vuln/detail/CVE-2026-133445) | High | 7.3 | In gdm3 before 51.2, an improper privilege management vulnerability allows an unprivileged local attacker with an activ… |
| 2026-11-25 22:17:20 | [CVE-2026-135153](https://nvd.nist.gov/vuln/detail/CVE-2026-135153) |  |  | Rejected reason: ** REJECT ** DO NOT USE THIS CANDIDATE NUMBER. Reason: This candidate was issued in error. Notes: All… |
| 2026-11-25 22:17:20 | [CVE-2026-136823](https://nvd.nist.gov/vuln/detail/CVE-2026-136823) | Critical | 9.3 | A vulnerability was found in D-Link R32 1.10B02. This affects an unknown function of the file /usr/bin/httpd of the com… |
| 2026-11-25 22:17:20 | [CVE-2026-136831](https://nvd.nist.gov/vuln/detail/CVE-2026-136831) | Low | 2.1 | A vulnerability was determined in WPExperts New User Approve Plugin up to 3.3 on WordPress. Impacted is the function up… |
| 2026-11-25 22:17:21 | [CVE-2026-66052](https://nvd.nist.gov/vuln/detail/CVE-2026-66052) | High | 8.7 | Comviva Revenue Plus (MobiLytix Customer Value Management) 3.0.0 contains an expression language injection vulnerabilit… |
| 2026-11-25 22:17:21 | [CVE-2026-69695](https://nvd.nist.gov/vuln/detail/CVE-2026-69695) | High | 8.7 | Handesk through 1.5 contains an unrestricted file upload vulnerability in Attachment::storeAttachmentFromRequest() that… |
| 2026-11-25 22:17:21 | [CVE-2026-69696](https://nvd.nist.gov/vuln/detail/CVE-2026-69696) | Medium | 6.3 | Handesk through 1.5 contains a missing authentication vulnerability in the POST /webhook/bitbucket route, which is excl… |
| 2026-11-25 22:17:22 | [CVE-2026-69697](https://nvd.nist.gov/vuln/detail/CVE-2026-69697) | Medium | 6.9 | Faveo Helpdesk (Community) through 2.0.3 and 2.0.4.RC.1 contains a server-side request forgery vulnerability in ApiExce… |
| 2026-11-25 22:17:22 | [CVE-2026-69698](https://nvd.nist.gov/vuln/detail/CVE-2026-69698) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-25 22:17:22 | [CVE-2026-71296](https://nvd.nist.gov/vuln/detail/CVE-2026-71296) | Medium | 6.8 | A flaw was found in maestro. A remote attacker could exploit a misconfiguration in the gRPC server where authentication… |
| 2026-11-25 22:17:22 | [CVE-2026-74025](https://nvd.nist.gov/vuln/detail/CVE-2026-74025) | Medium | 6.9 | A flaw was found in ironic-image. The scripts responsible for constructing kernel parameters for CoreOS root file syste… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
