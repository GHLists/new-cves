# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 11:18 UTC

New CVEs published between 2026-11-10 10:19 UTC and 2026-11-10 11:18 UTC.

[Full CSV](data/new-cves-2026-11-10T11-18-52-072925Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 11:16:40 | [CVE-2026-119446](https://nvd.nist.gov/vuln/detail/CVE-2026-119446) | Critical | 9.4 | Session Fixation vulnerability in the CLI login flow in nerves-hub nerves_hub_web allows an unauthenticated attacker to… |
| 2026-11-10 11:16:41 | [CVE-2026-120286](https://nvd.nist.gov/vuln/detail/CVE-2026-120286) | Medium | 5.3 | Missing Authorization vulnerability in the device and deployment group pages in nerves-hub nerves_hub_web allows an aut… |
| 2026-11-10 11:16:41 | [CVE-2026-120295](https://nvd.nist.gov/vuln/detail/CVE-2026-120295) | High | 7.1 | Incorrect Authorization vulnerability in the devices page bulk move in nerves-hub nerves_hub_web allows an authenticate… |
| 2026-11-10 11:16:42 | [CVE-2026-120730](https://nvd.nist.gov/vuln/detail/CVE-2026-120730) | High | 8.6 | Improperly Controlled Modification of Dynamically-Determined Object Attributes vulnerability in the device API, device… |
| 2026-11-10 11:16:42 | [CVE-2026-120997](https://nvd.nist.gov/vuln/detail/CVE-2026-120997) | Low | 2.3 | Improper Session Invalidation vulnerability in the dashboard pages, device console and local shell channels in nerves-h… |
| 2026-11-10 11:16:42 | [CVE-2026-120999](https://nvd.nist.gov/vuln/detail/CVE-2026-120999) | High | 7.4 | Improper Authentication vulnerability in Google sign-in and email confirmation in nerves-hub nerves_hub_web allows an a… |
| 2026-11-10 11:16:43 | [CVE-2026-125672](https://nvd.nist.gov/vuln/detail/CVE-2026-125672) | Medium | 6.6 | A flaw was found in cockpit-storaged. A Tang keyserver address read from a clevis token in a LUKS header is concatenate… |
| 2026-11-10 11:16:43 | [CVE-2026-125703](https://nvd.nist.gov/vuln/detail/CVE-2026-125703) | Medium | 5.5 | A flaw was found in the GStreamer gst-plugins-bad MXF plugin. Insufficient bounds checks when parsing crafted VANC data… |
| 2026-11-10 11:16:43 | [CVE-2026-125704](https://nvd.nist.gov/vuln/detail/CVE-2026-125704) | High | 7.5 | A use-after-free flaw was found in GStreamer core buffer value deserialization. When crafted serialized buffer data con… |
| 2026-11-10 11:16:43 | [CVE-2026-95646](https://nvd.nist.gov/vuln/detail/CVE-2026-95646) | High | 8.0 | Zoho Corporation ManageEngine DDI Central versions 6500 and below are vulnerable to a Unicode-based command injection v… |
| 2026-11-10 11:16:43 | [CVE-2026-95651](https://nvd.nist.gov/vuln/detail/CVE-2026-95651) | High | 7.5 | Zoho Corporation ManageEngine DDI Central versions 6500 and below are vulnerable to an unauthenticated GSS-TSIG keytab… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
