# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-06 07:18 UTC

New CVEs published between 2026-11-06 06:18 UTC and 2026-11-06 07:18 UTC.

[Full CSV](data/new-cves-2026-11-06T07-18-47-133207Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-06 07:17:06 | [CVE-2026-120749](https://nvd.nist.gov/vuln/detail/CVE-2026-120749) | Medium | 6.2 | A flaw was found in D-Bus. With a privileged Monitoring client attached (for example dbus-monitor or busctl monitor), a… |
| 2026-11-06 07:17:28 | [CVE-2026-73471](https://nvd.nist.gov/vuln/detail/CVE-2026-73471) | Medium | 6.1 | A flaw was found in GStreamer gst-plugins-good (avidemux). In the Nikon metadata tag parser, a pointer can be dereferen… |
| 2026-11-06 07:17:34 | [CVE-2026-73472](https://nvd.nist.gov/vuln/detail/CVE-2026-73472) | Medium | 6.1 | A flaw was found in GStreamer gst-plugins-good (avidemux). In the superindex and subindex parsers, integer overflow can… |
| 2026-11-06 07:17:40 | [CVE-2026-73473](https://nvd.nist.gov/vuln/detail/CVE-2026-73473) | Medium | 5.5 | A flaw was found in GStreamer gst-plugins-good (avidemux). In the subindex parser, missing validation of the entry coun… |
| 2026-11-06 07:17:52 | [CVE-2026-83493](https://nvd.nist.gov/vuln/detail/CVE-2026-83493) |  |  | A flaw was found in distributed-workloads. A remote attacker could exploit a vulnerability in the pull_request_target w… |
| 2026-11-06 07:17:57 | [CVE-2026-83494](https://nvd.nist.gov/vuln/detail/CVE-2026-83494) |  |  | A flaw was found in the training-operator. An incorrect object casting in the PyTorchJob ValidateUpdate webhook allows… |
| 2026-11-06 07:18:06 | [CVE-2026-9797](https://nvd.nist.gov/vuln/detail/CVE-2026-9797) | Medium | 6.5 | A flaw was found in Keycloak's administrative services (org.keycloak.services.resources.admin). A highly privileged att… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
