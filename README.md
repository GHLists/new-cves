# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-26 23:18 UTC

New CVEs published between 2026-11-26 22:20 UTC and 2026-11-26 23:18 UTC.

[Full CSV](data/new-cves-2026-11-26T23-18-47-875835Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-26 23:17:01 | [CVE-2026-135107](https://nvd.nist.gov/vuln/detail/CVE-2026-135107) | Medium | 6.5 | An **uncontrolled memory allocation** flaw has been found in the smbd_smb2_ioctl_pipe_write_done() function in source3/… |
| 2026-11-26 23:17:01 | [CVE-2026-137596](https://nvd.nist.gov/vuln/detail/CVE-2026-137596) | Medium | 5.0 | A server-side request forgery (SSRF) flaw was found in KubeVirt's decentralized live migration. The connectURL field of… |
| 2026-11-26 23:17:01 | [CVE-2026-137602](https://nvd.nist.gov/vuln/detail/CVE-2026-137602) | Medium | 5.3 | A flaw was found in Keycloak. This vulnerability enables information disclosure when the parameterized-scopes feature i… |
| 2026-11-26 23:17:01 | [CVE-2026-137653](https://nvd.nist.gov/vuln/detail/CVE-2026-137653) | Medium | 6.5 | A flaw was found in spice-server. A malicious SPICE client can send a message header declaring an arbitrarily large mes… |
| 2026-11-26 23:17:01 | [CVE-2026-137660](https://nvd.nist.gov/vuln/detail/CVE-2026-137660) | Medium | 6.9 | A vulnerability has been found in stylefeng Guns up to 2.2. Affected by this issue is the function TokenAndPermissionIn… |
| 2026-11-26 23:17:03 | [CVE-2026-7181](https://nvd.nist.gov/vuln/detail/CVE-2026-7181) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
