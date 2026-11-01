# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 23:18 UTC

New CVEs published between 2026-11-01 22:18 UTC and 2026-11-01 23:18 UTC.

[Full CSV](data/new-cves-2026-11-01T23-18-59-21002Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 23:17:28 | [CVE-2026-111089](https://nvd.nist.gov/vuln/detail/CVE-2026-111089) | High | 7.6 | Apache Wicket reads texts from the application's resource bundles — a localized label, a css class name — and writes so… |
| 2026-11-01 23:17:28 | [CVE-2026-120275](https://nvd.nist.gov/vuln/detail/CVE-2026-120275) | Medium | 5.1 | A security flaw has been discovered in Shanghai Xi Yu Ji Zhi Technology Minimax Code 0.5.8. This affects an unknown par… |
| 2026-11-01 23:17:29 | [CVE-2026-82956](https://nvd.nist.gov/vuln/detail/CVE-2026-82956) | High | 7.6 | Improper neutralization of input during web page generation in Apache Wicket. org.apache.wicket.ajax.AjaxNewWindowNotif… |
| 2026-11-01 23:17:29 | [CVE-2026-83539](https://nvd.nist.gov/vuln/detail/CVE-2026-83539) | High | 7.4 | Improper neutralization of input during web page generation in Apache Wicket. org.apache.wicket.extensions.markup.html.… |
| 2026-11-01 23:17:29 | [CVE-2026-83559](https://nvd.nist.gov/vuln/detail/CVE-2026-83559) | High | 7.4 | Improper encoding or escaping of output in Apache Wicket. org.apache.wicket.core.util.string.JavaScriptUtils#escapeQuot… |
| 2026-11-01 23:17:29 | [CVE-2026-83594](https://nvd.nist.gov/vuln/detail/CVE-2026-83594) | High | 8.3 | Memory allocation with an excessive size value in Apache Wicket. org.apache.wicket.markup.html.form.upload.resource.Fil… |
| 2026-11-01 23:17:29 | [CVE-2026-84170](https://nvd.nist.gov/vuln/detail/CVE-2026-84170) | High | 8.3 | Allocation of resources without limits or throttling in Apache Wicket. org.apache.wicket.markup.html.form.upload.resour… |
| 2026-11-01 23:17:30 | [CVE-2026-84172](https://nvd.nist.gov/vuln/detail/CVE-2026-84172) | Medium | 6.3 | Files accessible to external parties in Apache Wicket. org.apache.wicket.markup.html.PackageResourceGuard decides wheth… |
| 2026-11-01 23:17:30 | [CVE-2026-84177](https://nvd.nist.gov/vuln/detail/CVE-2026-84177) | Medium | 6.3 | Incorrect behavior order in Apache Wicket: a file path is validated before the framework appends the attributes that co… |
| 2026-11-01 23:17:30 | [CVE-2026-84231](https://nvd.nist.gov/vuln/detail/CVE-2026-84231) | High | 7.4 | Improper neutralization of input during web page generation in Apache Wicket. org.apache.wicket.markup.html.link.Extern… |
| 2026-11-01 23:17:30 | [CVE-2026-87718](https://nvd.nist.gov/vuln/detail/CVE-2026-87718) | Low | 2.3 | Apache Wicket 10.10.0, 10.11.0 and 9.24.0 do not set the Content-Security-Policy headers on a page whose render request… |
| 2026-11-01 23:17:30 | [CVE-2026-95863](https://nvd.nist.gov/vuln/detail/CVE-2026-95863) | High | 7.6 | Improper neutralization of input during web page generation in Apache Wicket. Apache Wicket generates JavaScript that r… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
