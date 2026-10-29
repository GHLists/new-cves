# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 18:20 UTC

New CVEs published between 2026-10-29 17:18 UTC and 2026-10-29 18:20 UTC.

[Full CSV](data/new-cves-2026-10-29T18-20-42-343789Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 18:17:21 | [CVE-2026-102260](https://nvd.nist.gov/vuln/detail/CVE-2026-102260) | Medium | 4.3 | HashiCorp Nomad and Nomad Enterprise are vulnerable to cross-namespace authorization bypasses in several read-only API… |
| 2026-10-29 18:17:21 | [CVE-2026-107347](https://nvd.nist.gov/vuln/detail/CVE-2026-107347) | High | 8.4 | HashiCorp Nomad and Nomad Enterprise are vulnerable to symlink following during dispatch payload and executor log write… |
| 2026-10-29 18:17:24 | [CVE-2026-116566](https://nvd.nist.gov/vuln/detail/CVE-2026-116566) | Medium | 5.3 | socket.getaddrinfo() previously accepted null bytes within *host* and *port* parameters which can cause the values to b… |
| 2026-10-29 18:17:28 | [CVE-2026-118766](https://nvd.nist.gov/vuln/detail/CVE-2026-118766) | Medium | 6.1 | Botan is a C++ cryptography library. Prior to 3.13.0, Botan's online OCSP client allowed a single HTTP redirect while p… |
| 2026-10-29 18:17:28 | [CVE-2026-118767](https://nvd.nist.gov/vuln/detail/CVE-2026-118767) | Medium | 4.8 | Botan is a C++ cryptography library. From 1.11.22 until 3.13.0, Botan's Python binding converted Python strings contain… |
| 2026-10-29 18:17:28 | [CVE-2026-118768](https://nvd.nist.gov/vuln/detail/CVE-2026-118768) | Medium | 5.9 | Botan is a C++ cryptography library. From 1.11.34 until 3.13.0, the botan ocsp_check command requested an OCSP response… |
| 2026-10-29 18:17:29 | [CVE-2026-118769](https://nvd.nist.gov/vuln/detail/CVE-2026-118769) | Critical | 9.2 | Botan is a C++ cryptography library. From 2.1.0 until 3.13.0, the Botan C API function botan_block_cipher_block_size co… |
| 2026-10-29 18:17:32 | [CVE-2026-51851](https://nvd.nist.gov/vuln/detail/CVE-2026-51851) |  |  | modelscope agent-zero 1.7, 1.8, 1.9, and 1.10 is vulnerable to Directory Traversal in python/helpers/file_browser.py:Fi… |
| 2026-10-29 18:17:32 | [CVE-2026-51863](https://nvd.nist.gov/vuln/detail/CVE-2026-51863) |  |  | DB-GPT v0.7.5 and 0.8.0 contains directory traversal in use_example_file (packages/dbgpt-app/src/dbgpt_app/openapi/api_… |
| 2026-10-29 18:17:32 | [CVE-2026-51902](https://nvd.nist.gov/vuln/detail/CVE-2026-51902) |  |  | SuperAGI up to v0.0.14 contains an improper access control vulnerability. The agent controller endpoint /api/agents/get… |
| 2026-10-29 18:17:32 | [CVE-2026-51903](https://nvd.nist.gov/vuln/detail/CVE-2026-51903) |  |  | SuperAGI v0.0.14 contains an improper access control vulnerability in get_agent_by_latest_execution in superagi/control… |
| 2026-10-29 18:17:32 | [CVE-2026-51905](https://nvd.nist.gov/vuln/detail/CVE-2026-51905) |  |  | TransformerOptimus SuperAGI v0.0.14 is vulnerable to Incorrect Access Control in get_agent_execution_configuration in s… |
| 2026-10-29 18:17:32 | [CVE-2026-51912](https://nvd.nist.gov/vuln/detail/CVE-2026-51912) |  |  | OpenBMB XAgent v1.0.0 contains directory traversal vulnerability in main-upload_file-the-preserved-live-upload-file-wit… |
| 2026-10-29 18:17:33 | [CVE-2026-60111](https://nvd.nist.gov/vuln/detail/CVE-2026-60111) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
