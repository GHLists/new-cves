# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-30 02:18 UTC

New CVEs published between 2026-10-30 01:19 UTC and 2026-10-30 02:18 UTC.

[Full CSV](data/new-cves-2026-10-30T02-18-59-931411Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-30 02:17:08 | [CVE-2026-112922](https://nvd.nist.gov/vuln/detail/CVE-2026-112922) | Low | 3.3 | A flaw was found in Ghostscript. A remote attacker could exploit this vulnerability by enticing a user to process a spe… |
| 2026-10-30 02:17:08 | [CVE-2026-118475](https://nvd.nist.gov/vuln/detail/CVE-2026-118475) | Low | 3.6 | A flaw was found in Eye of GNOME. When parsing a specially crafted PNG image containing malformed color profile metadat… |
| 2026-10-30 02:17:08 | [CVE-2026-15466](https://nvd.nist.gov/vuln/detail/CVE-2026-15466) |  |  | Software installed and run as a non-privileged user may conduct improper GPU system calls to cause race condition in ha… |
| 2026-10-30 02:17:09 | [CVE-2026-18629](https://nvd.nist.gov/vuln/detail/CVE-2026-18629) |  |  | A web page that contains unusual GPU shader code is loaded into the GPU compiler process and can lead memory allocation… |
| 2026-10-30 02:17:09 | [CVE-2026-19199](https://nvd.nist.gov/vuln/detail/CVE-2026-19199) |  |  | Software installed and run as a non-privileged user may conduct improper system calls to allocate physical memory. A 32… |
| 2026-10-30 02:17:09 | [CVE-2026-65584](https://nvd.nist.gov/vuln/detail/CVE-2026-65584) |  |  | Software installed and run as a non-privileged user may conduct improper GPU system calls causing a stack overflow in t… |
| 2026-10-30 02:17:09 | [CVE-2026-65586](https://nvd.nist.gov/vuln/detail/CVE-2026-65586) |  |  | Software installed and run as a non-privileged user may conduct improper GPU system calls to free memory in still in us… |
| 2026-10-30 02:17:09 | [CVE-2026-65587](https://nvd.nist.gov/vuln/detail/CVE-2026-65587) |  |  | A web page that contains unusual WebGPU content loaded into the GPU GLES render process can trigger an OOB write in the… |
| 2026-10-30 02:17:09 | [CVE-2026-74912](https://nvd.nist.gov/vuln/detail/CVE-2026-74912) |  |  | On GPU systems with the security vulnerability fix for CVE-2026-49746 applied, the mapping range of graphics buffers is… |
| 2026-10-30 02:17:09 | [CVE-2026-74915](https://nvd.nist.gov/vuln/detail/CVE-2026-74915) |  |  | A web page that contains unusual WebGPU content loaded into the GPU GLES render process can trigger a OOB read and/or w… |
| 2026-10-30 02:17:10 | [CVE-2026-91920](https://nvd.nist.gov/vuln/detail/CVE-2026-91920) | Medium | 6.5 | A flaw was found in the ChunkReader component of the Undertow web server, which is used to handle chunked transfer enco… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
