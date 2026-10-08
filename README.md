# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 19:18 UTC

New CVEs published between 2026-10-08 18:18 UTC and 2026-10-08 19:18 UTC.

[Full CSV](data/new-cves-2026-10-08T19-18-32-213986Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 19:16:56 | [CVE-2026-101998](https://nvd.nist.gov/vuln/detail/CVE-2026-101998) | Medium | 5.9 | Docker Sandboxes could fail open while masking credentials in protected proxy responses. When a response-body read retu… |
| 2026-10-08 19:16:56 | [CVE-2026-105452](https://nvd.nist.gov/vuln/detail/CVE-2026-105452) | Medium | 5.9 | Docker Sandboxes could forward a client-supplied credential alongside a credential injected by the host egress proxy. T… |
| 2026-10-08 19:16:57 | [CVE-2026-105570](https://nvd.nist.gov/vuln/detail/CVE-2026-105570) | Medium | 6.7 | Docker Sandboxes compared OAuth token-endpoint hostnames case-sensitively when deciding whether to mask managed credent… |
| 2026-10-08 19:16:58 | [CVE-2026-106428](https://nvd.nist.gov/vuln/detail/CVE-2026-106428) | Medium | 6.3 | An out-of-bounds read in SCRAM authentication response parsing in the MongoDB C Driver can read one byte beyond a fixed… |
| 2026-10-08 19:16:58 | [CVE-2026-106429](https://nvd.nist.gov/vuln/detail/CVE-2026-106429) | High | 7.1 | An integer underflow in the KMS endpoint-parsing logic of MongoDB libmongocrypt can cause an allocation failure that te… |
| 2026-10-08 19:16:58 | [CVE-2026-106430](https://nvd.nist.gov/vuln/detail/CVE-2026-106430) | Medium | 6.0 | The MongoDB C++ Driver discards content after an embedded NUL byte in certain field and collection names accepted by th… |
| 2026-10-08 19:16:59 | [CVE-2026-106431](https://nvd.nist.gov/vuln/detail/CVE-2026-106431) | Medium | 5.9 | An off-by-one error in the BSON bulk document writer in the MongoDB C Driver can write one zero byte immediately past a… |
| 2026-10-08 19:16:59 | [CVE-2026-106433](https://nvd.nist.gov/vuln/detail/CVE-2026-106433) | High | 8.7 | Improper state management in MongoDB libmongocrypt can cause provider-specific data to be treated as an incompatible ty… |
| 2026-10-08 19:16:59 | [CVE-2026-106434](https://nvd.nist.gov/vuln/detail/CVE-2026-106434) | Medium | 5.3 | The explicit decryption component of MongoDB libmongocrypt can return an unrecognized encrypted payload unchanged inste… |
| 2026-10-08 19:16:59 | [CVE-2026-106437](https://nvd.nist.gov/vuln/detail/CVE-2026-106437) | Medium | 5.9 | The BSON buffer-reservation API in the MongoDB C Driver can record a length smaller than the five-byte BSON minimum. La… |
| 2026-10-08 19:16:59 | [CVE-2026-106438](https://nvd.nist.gov/vuln/detail/CVE-2026-106438) | Medium | 5.1 | An incorrect calculation in Decimal128 string parsing in the MongoDB C Driver can accept certain over-precision inputs… |
| 2026-10-08 19:16:59 | [CVE-2026-107322](https://nvd.nist.gov/vuln/detail/CVE-2026-107322) | High | 8.5 | An incomplete list of disallowed inputs in Amazon Agent Plugins for AWS databases-on-aws plugin before 1.7.1 might allo… |
| 2026-10-08 19:17:00 | [CVE-2026-107324](https://nvd.nist.gov/vuln/detail/CVE-2026-107324) | High | 8.2 | An integer overflow in BSON value-length handling in the MongoDB Go Driver can cause a runtime panic when an applicatio… |
| 2026-10-08 19:17:00 | [CVE-2026-107325](https://nvd.nist.gov/vuln/detail/CVE-2026-107325) | High | 8.2 | Improper validation of a BSON array length in the MongoDB Go Driver can cause an out-of-bounds index and runtime panic… |
| 2026-10-08 19:17:00 | [CVE-2026-107382](https://nvd.nist.gov/vuln/detail/CVE-2026-107382) | Medium | 5.9 | MariaDB Connector/Node.js is used to connect applications developed on Node.js to MariaDB and MySQL databases. From 3.3… |
| 2026-10-08 19:17:00 | [CVE-2026-107383](https://nvd.nist.gov/vuln/detail/CVE-2026-107383) | High | 7.5 | MariaDB Connector/Node.js is used to connect applications developed on Node.js to MariaDB and MySQL databases. Prior to… |
| 2026-10-08 19:17:00 | [CVE-2026-107384](https://nvd.nist.gov/vuln/detail/CVE-2026-107384) | High | 8.1 | MariaDB Connector/Node.js is used to connect applications developed on Node.js to MariaDB and MySQL databases. From 3.2… |
| 2026-10-08 19:17:01 | [CVE-2026-107385](https://nvd.nist.gov/vuln/detail/CVE-2026-107385) | High | 7.4 | MariaDB Connector/Node.js is used to connect applications developed on Node.js to MariaDB and MySQL databases. Prior to… |
| 2026-10-08 19:17:01 | [CVE-2026-107386](https://nvd.nist.gov/vuln/detail/CVE-2026-107386) | Medium | 6.3 | amqp091-go is a Go AMQP 0.9.1 client. From 1.13.0 until 1.14.0, the frame-size mitigation from the prior allocation adv… |
| 2026-10-08 19:17:01 | [CVE-2026-107387](https://nvd.nist.gov/vuln/detail/CVE-2026-107387) | Medium | 6.2 | music-metadata is a metadata parser for audio and video media files. Prior to 11.16.0, the APEv2 parser reads an attack… |
| 2026-10-08 19:17:01 | [CVE-2026-107388](https://nvd.nist.gov/vuln/detail/CVE-2026-107388) | Medium | 6.2 | music-metadata is a metadata parser for audio and video media files. Prior to 11.16.0, the ID3v2 parser trusts the sync… |
| 2026-10-08 19:17:01 | [CVE-2026-107699](https://nvd.nist.gov/vuln/detail/CVE-2026-107699) | Critical | 9.3 | ppt2png through 0.0.6 contains an OS command injection vulnerability that allows attackers to execute operating system… |
| 2026-10-08 19:17:02 | [CVE-2026-107700](https://nvd.nist.gov/vuln/detail/CVE-2026-107700) | Critical | 9.3 | dot-access 0.0.3 through 1.0.0 contains a code injection vulnerability that allows remote attackers to execute JavaScri… |
| 2026-10-08 19:17:02 | [CVE-2026-107701](https://nvd.nist.gov/vuln/detail/CVE-2026-107701) | High | 8.8 | dot-access through 1.0.0 contains a prototype pollution vulnerability that allows attackers to modify Object.prototype… |
| 2026-10-08 19:17:02 | [CVE-2026-107703](https://nvd.nist.gov/vuln/detail/CVE-2026-107703) | Critical | 9.3 | @enmaso/node-convert through 1.0.0 contains an OS command injection vulnerability in convert.js that allows attackers t… |
| 2026-10-08 19:17:02 | [CVE-2026-107704](https://nvd.nist.gov/vuln/detail/CVE-2026-107704) | Critical | 9.3 | The image_optimizer Ruby gem 1.3.0 through 1.9.0 contains an OS command injection vulnerability in ImageOptimizer#ident… |
| 2026-10-08 19:17:05 | [CVE-2026-40804](https://nvd.nist.gov/vuln/detail/CVE-2026-40804) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Kodezen LLC aBloc… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
