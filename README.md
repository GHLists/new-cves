# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 03:18 UTC

New CVEs published between 2026-11-25 02:21 UTC and 2026-11-25 03:18 UTC.

[Full CSV](data/new-cves-2026-11-25T03-18-52-530941Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 03:17:28 | [CVE-2026-125734](https://nvd.nist.gov/vuln/detail/CVE-2026-125734) | Medium | 6.5 | A flaw was found in GStreamer gst-plugins-bad mxfdemux handling of MXF Index Table Segment data. Crafted index metadata… |
| 2026-11-25 03:17:29 | [CVE-2026-129832](https://nvd.nist.gov/vuln/detail/CVE-2026-129832) | Medium | 5.5 | A flaw was found in rsyslog. When process identification (PID) rewriting is enabled in the imuxsock module, a local att… |
| 2026-11-25 03:17:29 | [CVE-2026-129839](https://nvd.nist.gov/vuln/detail/CVE-2026-129839) | Medium | 5.3 | A flaw was found in rsyslog. When processing log entries using certain JSON (JavaScript Object Notation) formatting tem… |
| 2026-11-25 03:17:29 | [CVE-2026-135328](https://nvd.nist.gov/vuln/detail/CVE-2026-135328) | Medium | 5.8 | A flaw was found in kubevirt Containerized Data Importer (CDI). The CDI clone controller derives the CommonName of a CD… |
| 2026-11-25 03:17:29 | [CVE-2026-135813](https://nvd.nist.gov/vuln/detail/CVE-2026-135813) | Medium | 6.0 | A flaw was found in Red Hat Enterprise Linux's qemu-kvm virtualization software. A privileged user inside a guest virtu… |
| 2026-11-25 03:17:29 | [CVE-2026-136446](https://nvd.nist.gov/vuln/detail/CVE-2026-136446) | Low | 2.0 | A vulnerability has been found in JaguarJack catch-admin up to 5.4.1. This affects the function update of the file modu… |
| 2026-11-25 03:17:30 | [CVE-2026-136447](https://nvd.nist.gov/vuln/detail/CVE-2026-136447) | Low | 1.9 | A vulnerability was found in browser-use 0.13.13/0.13.14. This impacts the function load_and_migrate_config of the file… |
| 2026-11-25 03:17:30 | [CVE-2026-136448](https://nvd.nist.gov/vuln/detail/CVE-2026-136448) | Medium | 5.5 | A vulnerability was identified in nliautaud pico-content-editor up to 02d5ad6c820c5050c542ab9505819b5e0a0ba1af. Affecte… |
| 2026-11-25 03:17:30 | [CVE-2026-136451](https://nvd.nist.gov/vuln/detail/CVE-2026-136451) | Medium | 6.8 | A flaw was found in the Keycloak Operator. Deterministic hashes derived from Kubernetes Secrets are published in genera… |
| 2026-11-25 03:17:30 | [CVE-2026-136615](https://nvd.nist.gov/vuln/detail/CVE-2026-136615) | Medium | 6.3 | league/commonmark 2.6.0 before 2.10.8 contains a denial of service vulnerability in DelimiterStack::push() that miscoun… |
| 2026-11-25 03:17:31 | [CVE-2026-136616](https://nvd.nist.gov/vuln/detail/CVE-2026-136616) | Low | 2.3 | COVESA Open1722 before 0.9.8 contains an out-of-bounds read vulnerability in Avtp_Vss_CalcVssPathLength in src/avtp/acf… |
| 2026-11-25 03:17:31 | [CVE-2026-136617](https://nvd.nist.gov/vuln/detail/CVE-2026-136617) | Medium | 6.3 | Shopify async-memcached before 0.11.0 contains a command injection vulnerability in Client::validate_meta_flags that al… |
| 2026-11-25 03:17:32 | [CVE-2026-136618](https://nvd.nist.gov/vuln/detail/CVE-2026-136618) | Medium | 5.3 | Karakeep before 0.35.0 contains an improper access control vulnerability in ManualList.mergeInto that allows list owner… |
| 2026-11-25 03:17:32 | [CVE-2026-136619](https://nvd.nist.gov/vuln/detail/CVE-2026-136619) | Medium | 5.3 | Karakeep before 0.35.0 contains an information disclosure vulnerability that allows shared-list collaborators to learn… |
| 2026-11-25 03:17:33 | [CVE-2026-136620](https://nvd.nist.gov/vuln/detail/CVE-2026-136620) | Medium | 6.9 | pain001-mcp 0.0.72 before 0.0.80 contains a path traversal vulnerability in the commit_payment_batch MCP tool that allo… |
| 2026-11-25 03:17:33 | [CVE-2026-136621](https://nvd.nist.gov/vuln/detail/CVE-2026-136621) | Medium | 6.9 | LTplus-AG ifc-lite @ifc-lite/export before 4.13.1 and ifc-lite-export before 27.0.0 contain a STEP record injection vul… |
| 2026-11-25 03:17:33 | [CVE-2026-136622](https://nvd.nist.gov/vuln/detail/CVE-2026-136622) | Medium | 6.9 | WeKan before 12.78 contains an information disclosure vulnerability in Exporter.buildStream() that lets attackers retri… |
| 2026-11-25 03:17:34 | [CVE-2026-136623](https://nvd.nist.gov/vuln/detail/CVE-2026-136623) | Medium | 6.9 | WeKan before 12.78 contains an access control bypass in Exporter.buildCsvStream() that ignores the Disable all export a… |
| 2026-11-25 03:17:35 | [CVE-2026-136625](https://nvd.nist.gov/vuln/detail/CVE-2026-136625) | Medium | 5.2 | ai-memory 2.6.0 before 3.3.2 contains a symlink following vulnerability in the ai-memory-wikisync companion that allows… |
| 2026-11-25 03:17:35 | [CVE-2026-136624](https://nvd.nist.gov/vuln/detail/CVE-2026-136624) | High | 7.1 | lightNVR before 0.44.3 contains an authorization bypass vulnerability in go2rtc_proxy_authorize_request() that allows a… |
| 2026-11-25 03:17:48 | [CVE-2026-136626](https://nvd.nist.gov/vuln/detail/CVE-2026-136626) | High | 8.8 | SRS 4.0.0 before 6.0.194, 7.0.0 before 7.0.214, and 8.0.0 before 8.0.73 contains a heap-based buffer overflow in SrsRtc… |
| 2026-11-25 03:17:49 | [CVE-2026-136627](https://nvd.nist.gov/vuln/detail/CVE-2026-136627) | High | 8.7 | SRS 4.0.0 before 6.0.194, 7.0.0 before 7.0.214, and 8.0.0 before 8.0.73 contains a reachable assertion in RTCP decoding… |
| 2026-11-25 03:17:49 | [CVE-2026-136628](https://nvd.nist.gov/vuln/detail/CVE-2026-136628) | High | 7.6 | Wails before 2.17.1 on Linux contains an origin validation error in the sendMessageToBackend WebKitGTK handler that all… |
| 2026-11-25 03:17:49 | [CVE-2026-136629](https://nvd.nist.gov/vuln/detail/CVE-2026-136629) | High | 8.5 | Nektos act 0.2.92 before 0.2.95 contains an argument injection vulnerability in readProjectArgsFile and projectFlag tha… |
| 2026-11-25 03:17:49 | [CVE-2026-136630](https://nvd.nist.gov/vuln/detail/CVE-2026-136630) | High | 7.7 | Electerm before 5.9.0 contains an origin validation vulnerability in the MCP Server widget that allows remote attackers… |
| 2026-11-25 03:17:49 | [CVE-2026-136631](https://nvd.nist.gov/vuln/detail/CVE-2026-136631) | High | 7.6 | Mastodon 4.7.4 and 4.8.0-alpha.3 before 5.0.0-beta.1 contains an authentication bypass vulnerability in authenticate_wi… |
| 2026-11-25 03:17:50 | [CVE-2026-136632](https://nvd.nist.gov/vuln/detail/CVE-2026-136632) | High | 7.2 | OpenProject 17.2.0 before 17.5.2, 17.6.0 before 17.6.1, 17.7.0 before 17.7.3, 17.8.0 before 17.8.2, and 17.9.0 before 1… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
