# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 08:19 UTC

New CVEs published between 2026-10-15 07:20 UTC and 2026-10-15 08:19 UTC.

[Full CSV](data/new-cves-2026-10-15T08-19-17-355719Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 08:16:36 | [CVE-2026-101309](https://nvd.nist.gov/vuln/detail/CVE-2026-101309) |  |  | The xHCI (USB 3) device model did not validate or save the event ring size provided by the guest. The size was re-read… |
| 2026-10-15 08:16:36 | [CVE-2026-101310](https://nvd.nist.gov/vuln/detail/CVE-2026-101310) |  |  | The HDA audio device model did not check for zero-length Buffer Descriptor List (BDL) entries when starting a stream. A… |
| 2026-10-15 08:16:36 | [CVE-2026-101311](https://nvd.nist.gov/vuln/detail/CVE-2026-101311) |  |  | The framebuffer device model's maximum resolution constants were duplicated between the framebuffer and RFB modules and… |
| 2026-10-15 08:16:36 | [CVE-2026-102465](https://nvd.nist.gov/vuln/detail/CVE-2026-102465) | High | 8.2 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the Vert.x Redis clien… |
| 2026-10-15 08:16:36 | [CVE-2026-102467](https://nvd.nist.gov/vuln/detail/CVE-2026-102467) | High | 8.7 | In Eclipse Vert.x versions [4.0.0, 4.5.34] or [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the WebSocket implemen… |
| 2026-10-15 08:16:36 | [CVE-2026-102475](https://nvd.nist.gov/vuln/detail/CVE-2026-102475) | High | 8.7 | In Eclipse Vert.x versions [5.0.0,5.0.12] or [5.1.0,5.1.9] or [5.2.0, 5.2.0], the HTTP proxy provides a body transforme… |
| 2026-10-15 08:16:36 | [CVE-2026-108092](https://nvd.nist.gov/vuln/detail/CVE-2026-108092) | Medium | 4.3 | The Blog2Social – Social Media Auto Post & Scheduler plugin for WordPress is vulnerable to Insecure Direct Object Refer… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
