# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-27 21:18 UTC

New CVEs published between 2026-10-27 20:18 UTC and 2026-10-27 21:18 UTC.

[Full CSV](data/new-cves-2026-10-27T21-18-46-731201Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-27 21:18:05 | [CVE-2026-116692](https://nvd.nist.gov/vuln/detail/CVE-2026-116692) | Critical | 9.8 | MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. From 3… |
| 2026-10-27 21:18:05 | [CVE-2026-116693](https://nvd.nist.gov/vuln/detail/CVE-2026-116693) | High | 8.7 | dd-trace is the Datadog APM client for Node.js. From 2.0.0 until 5.131.1 and 6.20.1, the default DD_TRACE_OBFUSCATION_Q… |
| 2026-10-27 21:18:05 | [CVE-2026-116694](https://nvd.nist.gov/vuln/detail/CVE-2026-116694) | Medium | 6.3 | OpenTelemetry Python provides the Python API and SDK for OpenTelemetry. Prior to 1.45.0, JaegerPropagator.extract() in… |
| 2026-10-27 21:18:05 | [CVE-2026-116695](https://nvd.nist.gov/vuln/detail/CVE-2026-116695) | Medium | 5.3 | Crass is a Ruby CSS parser that is compliant with the CSS Syntax Level 3 specification. Prior to 1.0.8, Crass incorrect… |
| 2026-10-27 21:18:05 | [CVE-2026-116696](https://nvd.nist.gov/vuln/detail/CVE-2026-116696) | Low | 3.3 | russh is a Rust SSH client and server library that includes an SSH agent protocol implementation. Prior to 0.65.0, russ… |
| 2026-10-27 21:18:05 | [CVE-2026-116773](https://nvd.nist.gov/vuln/detail/CVE-2026-116773) | Medium | 4.3 | russh is a Rust SSH client and server library that includes an SSH agent protocol implementation. Prior to 0.65.0, the… |
| 2026-10-27 21:18:05 | [CVE-2026-116774](https://nvd.nist.gov/vuln/detail/CVE-2026-116774) | Medium | 4.3 | russh is a Rust SSH client and server library that includes an SSH agent protocol implementation. From 0.60.0 until 0.6… |
| 2026-10-27 21:18:06 | [CVE-2026-116775](https://nvd.nist.gov/vuln/detail/CVE-2026-116775) | Low | 2.3 | pageant provides a PageantStream type that implements AsyncRead and AsyncWrite traits and can be used to communicate wi… |
| 2026-10-27 21:18:06 | [CVE-2026-39928](https://nvd.nist.gov/vuln/detail/CVE-2026-39928) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-10-27 21:18:06 | [CVE-2026-57195](https://nvd.nist.gov/vuln/detail/CVE-2026-57195) | High | 7.5 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |
| 2026-10-27 21:18:06 | [CVE-2026-57200](https://nvd.nist.gov/vuln/detail/CVE-2026-57200) | High | 7.5 | Asterisk is an open source private branch exchange and telephony toolkit. Prior to Asterisk 20.20.1, 21.12.3, 22.10.1,… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
