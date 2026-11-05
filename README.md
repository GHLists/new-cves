# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 23:18 UTC

New CVEs published between 2026-11-05 22:21 UTC and 2026-11-05 23:18 UTC.

[Full CSV](data/new-cves-2026-11-05T23-18-47-035759Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 23:16:49 | [CVE-2026-102943](https://nvd.nist.gov/vuln/detail/CVE-2026-102943) | Medium | 6.5 | Dagu is a workflow engine with a built-in Web user interface. Prior to version 2.11.0, its MCP dagu_read operation with… |
| 2026-11-05 23:16:50 | [CVE-2026-110390](https://nvd.nist.gov/vuln/detail/CVE-2026-110390) | Medium | 6.9 | Missing authentication in the FlexNet Beacon component of Flexera One and FlexNet Manager Suite allows unauthenticated… |
| 2026-11-05 23:16:50 | [CVE-2026-113663](https://nvd.nist.gov/vuln/detail/CVE-2026-113663) | High | 8.8 | AG2 is an open-source AgentOS. From 0.13.2 until ag2 1.1.1, and from autogen 0.13.2 to 0.14.1, SandboxShellTool configu… |
| 2026-11-05 23:16:50 | [CVE-2026-16579](https://nvd.nist.gov/vuln/detail/CVE-2026-16579) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-05 23:16:56 | [CVE-2026-68509](https://nvd.nist.gov/vuln/detail/CVE-2026-68509) | Medium | 6.3 | FairEmail is a fully featured, open source, privacy-friendly email app for Android. Prior to 1.2325, shared attachment… |
| 2026-11-05 23:17:00 | [CVE-2026-77596](https://nvd.nist.gov/vuln/detail/CVE-2026-77596) | Critical | 9.6 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, th… |
| 2026-11-05 23:17:00 | [CVE-2026-85068](https://nvd.nist.gov/vuln/detail/CVE-2026-85068) | Low | 2.4 | Network UPS Tools is a collection of programs which provide a common interface for monitoring and administering UPS, PD… |
| 2026-11-05 23:17:01 | [CVE-2026-88979](https://nvd.nist.gov/vuln/detail/CVE-2026-88979) | Medium | 5.8 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. From 2.17.0 until 2… |
| 2026-11-05 23:17:01 | [CVE-2026-88980](https://nvd.nist.gov/vuln/detail/CVE-2026-88980) | High | 8.6 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, th… |
| 2026-11-05 23:17:01 | [CVE-2026-88981](https://nvd.nist.gov/vuln/detail/CVE-2026-88981) | High | 8.6 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, th… |
| 2026-11-05 23:17:01 | [CVE-2026-88982](https://nvd.nist.gov/vuln/detail/CVE-2026-88982) | Medium | 5.4 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.18.0, th… |
| 2026-11-05 23:17:01 | [CVE-2026-88984](https://nvd.nist.gov/vuln/detail/CVE-2026-88984) | High | 7.2 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.16.1, th… |
| 2026-11-05 23:17:01 | [CVE-2026-92693](https://nvd.nist.gov/vuln/detail/CVE-2026-92693) | High | 8.2 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, parse_raw_packet_to_simple_pac… |
| 2026-11-05 23:17:02 | [CVE-2026-92694](https://nvd.nist.gov/vuln/detail/CVE-2026-92694) | Medium | 5.9 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, FastNetMon's IPv6 top-talkers… |
| 2026-11-05 23:17:02 | [CVE-2026-92695](https://nvd.nist.gov/vuln/detail/CVE-2026-92695) | High | 8.2 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, the live parse_packet() callba… |
| 2026-11-05 23:17:02 | [CVE-2026-92697](https://nvd.nist.gov/vuln/detail/CVE-2026-92697) | High | 7.5 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, the NetFlow v9 collector calls… |
| 2026-11-05 23:17:02 | [CVE-2026-92698](https://nvd.nist.gov/vuln/detail/CVE-2026-92698) | High | 8.2 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, process_sflow_flow_sample() in… |
| 2026-11-05 23:17:02 | [CVE-2026-93424](https://nvd.nist.gov/vuln/detail/CVE-2026-93424) | High | 7.5 | FastNetMon is a high-performance DDoS detector and sensor. In version 1.2.9 and earlier, peer_find_template() in src/ne… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
