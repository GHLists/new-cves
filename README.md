# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-30 22:19 UTC

New CVEs published between 2026-10-30 21:20 UTC and 2026-10-30 22:19 UTC.

[Full CSV](data/new-cves-2026-10-30T22-19-42-855953Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-30 22:16:53 | [CVE-2026-111578](https://nvd.nist.gov/vuln/detail/CVE-2026-111578) | High | 7.5 | The PDF Invoices & Packing Slips for WooCommerce WordPress plugin from 5.16.2 before 5.16.5 does not properly escape se… |
| 2026-10-30 22:16:54 | [CVE-2026-118938](https://nvd.nist.gov/vuln/detail/CVE-2026-118938) | High | 8.8 | In Trail of Bits fickling through 0.1.12, a pickle STACK_GLOBAL operand carrying a dotted __qualname__ (for example "Va… |
| 2026-10-30 22:16:54 | [CVE-2026-16760](https://nvd.nist.gov/vuln/detail/CVE-2026-16760) | High | 8.8 | In Trail of Bits fickling through 0.1.12, the _process_import() method in fickle.py adds an imported name to the likely… |
| 2026-10-30 22:16:54 | [CVE-2026-55146](https://nvd.nist.gov/vuln/detail/CVE-2026-55146) | Medium | 4.3 | LORIS (Longitudinal Online Research and Imaging System) is a self-hosted web application that provides data- and projec… |
| 2026-10-30 22:16:54 | [CVE-2026-55147](https://nvd.nist.gov/vuln/detail/CVE-2026-55147) | Medium | 6.3 | LORIS (Longitudinal Online Research and Imaging System) is a self-hosted web application that provides data- and projec… |
| 2026-10-30 22:16:54 | [CVE-2026-55612](https://nvd.nist.gov/vuln/detail/CVE-2026-55612) | Low | 3.7 | uhttpd is a small HTTP server. In unpatched repository snapshots, `client_poll_post_data()` in `client.c` consumes an i… |
| 2026-10-30 22:16:55 | [CVE-2026-55613](https://nvd.nist.gov/vuln/detail/CVE-2026-55613) | Medium | 6.9 | uhttpd is a small HTTP server. In unpatched repository snapshots, `uh_ubus_data_send()` in `ubus.c` can desynchronize H… |
| 2026-10-30 22:16:55 | [CVE-2026-55614](https://nvd.nist.gov/vuln/detail/CVE-2026-55614) | Medium | 6.9 | uhttpd is a small HTTP server. In unpatched repository snapshots, `client_parse_header()` in `client.c` lowercases head… |
| 2026-10-30 22:16:56 | [CVE-2026-62277](https://nvd.nist.gov/vuln/detail/CVE-2026-62277) | Medium | 6.5 | LubeLogger is a self-hosted, open-source, web-based vehicle maintenance and fuel mileage tracker. Prior to 1.6.8, `Prin… |
| 2026-10-30 22:16:56 | [CVE-2026-62347](https://nvd.nist.gov/vuln/detail/CVE-2026-62347) | Medium | 5.9 | Element Call is a native Matrix video conferencing application. From 0.16.0 until 0.20.3, the standalone Element Call `… |
| 2026-10-30 22:16:57 | [CVE-2026-63115](https://nvd.nist.gov/vuln/detail/CVE-2026-63115) | Medium | 5.3 | ActivityPub is a multi-tenant ActivityPub server for Ghost, built with Fedify. From 1.0.0 until 1.2.6, the `Undo` handl… |
| 2026-10-30 22:16:58 | [CVE-2026-63121](https://nvd.nist.gov/vuln/detail/CVE-2026-63121) | Medium | 6.3 | Kubewarden policies is a collection of WebAssembly policies for securing and governing Kubernetes clusters. For version… |
| 2026-10-30 22:16:58 | [CVE-2026-63182](https://nvd.nist.gov/vuln/detail/CVE-2026-63182) | High | 8.1 | LightSAML implements SAML 2.0 data model classes, XML serialization and deserialization, XML security, certificate supp… |
| 2026-10-30 22:16:58 | [CVE-2026-63184](https://nvd.nist.gov/vuln/detail/CVE-2026-63184) | High | 7.1 | Refitter is a tool for generating a C# REST API client using the Refit library. Prior to 2.1.1, the `refitter` dotnet t… |
| 2026-10-30 22:16:58 | [CVE-2026-63201](https://nvd.nist.gov/vuln/detail/CVE-2026-63201) | High | 7.1 | Netopeer2 is a server for implementing network configuration management based on the `NETCONF` Protocol. In affected ve… |
| 2026-10-30 22:16:58 | [CVE-2026-63224](https://nvd.nist.gov/vuln/detail/CVE-2026-63224) | High | 7.2 | OpenRemote is an open-source internet-of-things platform. Prior to 1.26.0, the `datapoint export` API constructs `CSV c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
