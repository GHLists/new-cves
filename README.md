# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-16 22:18 UTC

New CVEs published between 2026-10-16 21:19 UTC and 2026-10-16 22:18 UTC.

[Full CSV](data/new-cves-2026-10-16T22-18-33-87171Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-16 21:21:02 | [CVE-2026-96542](https://nvd.nist.gov/vuln/detail/CVE-2026-96542) | Medium | 5.0 | Incorrect permission assignment (CWE-732) in the standalone installer for EA Javelin Anticheat (versions 1.0.14329371,… |
| 2026-10-16 22:17:14 | [CVE-2026-108372](https://nvd.nist.gov/vuln/detail/CVE-2026-108372) | High | 7.1 | Open and provider-neutral, LoopX is a lightweight state kernel and local-first control plane for loop engineering. From… |
| 2026-10-16 22:17:20 | [CVE-2026-111044](https://nvd.nist.gov/vuln/detail/CVE-2026-111044) | High | 7.6 | Sunshine is a self-hosted game stream host for Moonlight. From 2026.329.165800 until 2026.906.222525, Sunshine accepted… |
| 2026-10-16 22:17:23 | [CVE-2026-49410](https://nvd.nist.gov/vuln/detail/CVE-2026-49410) | High | 8.1 | OpenHuman is an open-source agent harness available as a desktop application and Rust library. Versions before 0.56.0 a… |
| 2026-10-16 22:17:24 | [CVE-2026-62438](https://nvd.nist.gov/vuln/detail/CVE-2026-62438) | Medium | 6.1 | A flaw was found in GIMP. An attacker can cause a Denial of Service (DoS) or potentially disclose sensitive memory cont… |
| 2026-10-16 22:17:24 | [CVE-2026-62439](https://nvd.nist.gov/vuln/detail/CVE-2026-62439) | High | 7.0 | A flaw was found in GIMP. An integer overflow occurs in the file-pvr plug-in when calculating memory buffer sizes for i… |
| 2026-10-16 22:17:25 | [CVE-2026-68498](https://nvd.nist.gov/vuln/detail/CVE-2026-68498) | High | 7.5 | StreamReadConstraints.maxNameLength (default 50,000 characters) is intended to bound how much memory a single JSON Obje… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
