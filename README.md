# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 19:23 UTC

New CVEs published between 2026-10-21 18:20 UTC and 2026-10-21 19:23 UTC.

[Full CSV](data/new-cves-2026-10-21T19-23-30-823014Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 19:16:47 | [CVE-2025-31699](https://nvd.nist.gov/vuln/detail/CVE-2025-31699) | Critical | 9.1 | Apache Traffic Server can return an origin connection to the shared pool while the origin is still waiting on a request… |
| 2026-10-21 19:16:48 | [CVE-2025-55702](https://nvd.nist.gov/vuln/detail/CVE-2025-55702) | High | 7.0 | When a client sends a POST with Expect: 100-continue and the origin answers before reading the body, Apache Traffic Ser… |
| 2026-10-21 19:16:55 | [CVE-2026-105931](https://nvd.nist.gov/vuln/detail/CVE-2026-105931) | Low | 2.3 | The Apache Pulsar broker exposes a transaction administration REST API under /admin/v3/transactions. When authenticatio… |
| 2026-10-21 19:16:55 | [CVE-2026-105932](https://nvd.nist.gov/vuln/detail/CVE-2026-105932) | Low | 2.3 | The Apache Pulsar broker admin REST API provides endpoints to read, set and remove the topic-level entry filter policy… |
| 2026-10-21 19:16:55 | [CVE-2026-105933](https://nvd.nist.gov/vuln/detail/CVE-2026-105933) | Low | 2.3 | Apache Pulsar allows an administrator to require end-to-end message encryption for all topics in a namespace by setting… |
| 2026-10-21 19:16:56 | [CVE-2026-105934](https://nvd.nist.gov/vuln/detail/CVE-2026-105934) | High | 7.2 | The Apache Pulsar broker admin REST API provides a truncate operation for persistent topics (DELETE /admin/v2/persisten… |
| 2026-10-21 19:16:56 | [CVE-2026-105935](https://nvd.nist.gov/vuln/detail/CVE-2026-105935) | Medium | 4.9 | The Pulsar Functions Worker provides a REST API endpoint for triggering a function, which publishes a caller-supplied v… |
| 2026-10-21 19:16:56 | [CVE-2026-105936](https://nvd.nist.gov/vuln/detail/CVE-2026-105936) | Medium | 5.3 | The Pulsar Functions worker REST API provides two endpoints that return the catalog of Pulsar IO connectors installed o… |
| 2026-10-21 19:16:56 | [CVE-2026-105937](https://nvd.nist.gov/vuln/detail/CVE-2026-105937) | High | 8.7 | Apache Pulsar shadow topics (PIP-180) are topics that read the stored messages of a source topic from that topic's mana… |
| 2026-10-21 19:16:56 | [CVE-2026-105938](https://nvd.nist.gov/vuln/detail/CVE-2026-105938) | Low | 2.3 | Apache Pulsar namespaces can restrict which roles may use a subscription, either with the Prefix subscription authentic… |
| 2026-10-21 19:16:57 | [CVE-2026-105942](https://nvd.nist.gov/vuln/detail/CVE-2026-105942) | High | 7.7 | When a configured proxy role sends a request to the broker on behalf of another user (the original principal), the brok… |
| 2026-10-21 19:16:57 | [CVE-2026-105944](https://nvd.nist.gov/vuln/detail/CVE-2026-105944) | Critical | 10.0 | Apache Pulsar Manager is a web console for administering Apache Pulsar clusters. It has its own user accounts and login… |
| 2026-10-21 19:16:57 | [CVE-2026-105945](https://nvd.nist.gov/vuln/detail/CVE-2026-105945) | High | 7.7 | The Pulsar Packages Management Service can be configured to store packages on the local filesystem of the broker by usi… |
| 2026-10-21 19:16:57 | [CVE-2026-107588](https://nvd.nist.gov/vuln/detail/CVE-2026-107588) | High | 8.4 | Vaadin Charts renders charts with the Highcharts library and pins an exact version of it, 9.2.2 in Vaadin 22 to 24 and… |
| 2026-10-21 19:16:58 | [CVE-2026-110803](https://nvd.nist.gov/vuln/detail/CVE-2026-110803) | High | 8.7 | VaadinService.requestEnd() in Vaadin Framework 8 locks the session and then reads the v-uiId request parameter outside… |
| 2026-10-21 19:16:58 | [CVE-2026-111401](https://nvd.nist.gov/vuln/detail/CVE-2026-111401) | Medium | 6.5 | Cross-Site Request Forgery (CSRF) vulnerability in Tailored Media Tailored Tools tailored-tools allows Cross Site Reque… |
| 2026-10-21 19:16:59 | [CVE-2026-111804](https://nvd.nist.gov/vuln/detail/CVE-2026-111804) | High | 8.8 | Apache Traffic Server's experimental wasm plugin has a use-after-free in its transaction-close handler and forwards unv… |
| 2026-10-21 19:16:59 | [CVE-2026-111813](https://nvd.nist.gov/vuln/detail/CVE-2026-111813) | Critical | 10.0 | Apache Traffic Server's experimental magick plugin lets an unauthenticated client control ImageMagick convert arguments… |
| 2026-10-21 19:16:59 | [CVE-2026-111816](https://nvd.nist.gov/vuln/detail/CVE-2026-111816) | Critical | 9.2 | Apache Traffic Server forwarded a malformed 302 response that should have been rejected as a parse error, because the T… |
| 2026-10-21 19:16:59 | [CVE-2026-113461](https://nvd.nist.gov/vuln/detail/CVE-2026-113461) | Medium | 5.2 | Local privilege escalation in Checkmk 2.5.0p14 allows a local user with write access to the Oracle client library direc… |
| 2026-10-21 19:17:00 | [CVE-2026-113870](https://nvd.nist.gov/vuln/detail/CVE-2026-113870) | High | 8.6 | MongoDB Compass improperly escapes certain BSON values when converting a stored view’s aggregation pipeline into editab… |
| 2026-10-21 19:17:00 | [CVE-2026-114266](https://nvd.nist.gov/vuln/detail/CVE-2026-114266) | Low | 2.1 | A security vulnerability has been detected in ProjectWorlds Advanced Library Management System 1.0. This impacts the fu… |
| 2026-10-21 19:17:00 | [CVE-2026-114267](https://nvd.nist.gov/vuln/detail/CVE-2026-114267) | Medium | 5.5 | A vulnerability was detected in SourceCodester Food Order Management System 1.0. Affected is an unknown function of the… |
| 2026-10-21 19:17:00 | [CVE-2026-114268](https://nvd.nist.gov/vuln/detail/CVE-2026-114268) | High | 8.6 | A flaw has been found in Tenda BE3L Pro 16.03.60.62. Affected by this vulnerability is the function formWifiBasicSet of… |
| 2026-10-21 19:17:00 | [CVE-2026-114361](https://nvd.nist.gov/vuln/detail/CVE-2026-114361) | Medium | 6.3 | A vulnerability was detected in HarnessRouter up to 0.31.10. This affects an unknown function of the file gateway/app.p… |
| 2026-10-21 19:17:02 | [CVE-2026-18748](https://nvd.nist.gov/vuln/detail/CVE-2026-18748) | Low | 3.5 | The Bluetooth Classic A2DP host stores a codec Information Element (IE) in struct bt_a2dp_codec_ie, a one-byte len fiel… |
| 2026-10-21 19:17:02 | [CVE-2026-19676](https://nvd.nist.gov/vuln/detail/CVE-2026-19676) | High | 7.8 | The user-mode verifier for the peci_transfer() system call, z_vrfy_peci_transfer() in drivers/peci/peci_handlers.c, che… |
| 2026-10-21 19:17:02 | [CVE-2026-19947](https://nvd.nist.gov/vuln/detail/CVE-2026-19947) | Medium | 5.3 | The device multiplexer pseudo-driver in drivers/misc/devmux/devmux.c exposes two system calls, devmux_select_get() and… |
| 2026-10-21 19:17:03 | [CVE-2026-78116](https://nvd.nist.gov/vuln/detail/CVE-2026-78116) | Medium | 5.2 | The Broadcom AFBR-S50 time-of-flight sensor driver double-completes an RTIO submission when sensor data evaluation fail… |
| 2026-10-21 19:17:03 | [CVE-2026-78117](https://nvd.nist.gov/vuln/detail/CVE-2026-78117) | Medium | 4.2 | The Infineon PSOC 6 BLESS HCI driver in drivers/bluetooth/hci/hci_infineon_psoc6_bless.c stored the outgoing HCI packet… |
| 2026-10-21 19:17:03 | [CVE-2026-78118](https://nvd.nist.gov/vuln/detail/CVE-2026-78118) | High | 7.0 | The kernel helper z_waitq_head() (kernel/include/wait_q.h) reads the head of a thread wait queue, but on SMP systems it… |
| 2026-10-21 19:17:03 | [CVE-2026-78119](https://nvd.nist.gov/vuln/detail/CVE-2026-78119) | Medium | 6.3 | The Nuvoton NPCX eSPI driver parses Target-Attached-Flash (TAF) requests in espi_taf_parse() (drivers/espi/espi_npcx.c)… |
| 2026-10-21 19:17:04 | [CVE-2026-79976](https://nvd.nist.gov/vuln/detail/CVE-2026-79976) | High | 7.1 | The MCTP-over-I2C+GPIO target binding in subsys/pmci/mctp/mctp_i2c_gpio_target.c emulates a small pseudo-register file,… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
