# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 19:19 UTC

New CVEs published between 2026-09-29 18:18 UTC and 2026-09-29 19:19 UTC.

[Full CSV](data/new-cves-2026-09-29T19-19-50-551352Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 19:17:19 | [CVE-2026-102616](https://nvd.nist.gov/vuln/detail/CVE-2026-102616) | Medium | 5.5 | A vulnerability was detected in risesoft-y9 WorkFlow-Engine up to 9.6.10. Impacted is the function getByIdAndYear of th… |
| 2026-09-29 19:17:23 | [CVE-2026-102820](https://nvd.nist.gov/vuln/detail/CVE-2026-102820) | Medium | 6.2 | pageant provides a [PageantStream] type that implements [AsyncRead] and [AsyncWrite] traits and can be used to talk to… |
| 2026-09-29 19:17:23 | [CVE-2026-102821](https://nvd.nist.gov/vuln/detail/CVE-2026-102821) | Medium | 6.5 | Russh is a Rust SSH client and server library. Prior to 0.63.2, an authenticated remote peer can send SSH_MSG_KEXINIT w… |
| 2026-09-29 19:17:24 | [CVE-2026-102822](https://nvd.nist.gov/vuln/detail/CVE-2026-102822) | Low | 3.7 | Russh is a Rust SSH client and server library. Prior to 0.63.1, a connection configured to permit mac=none can negotiat… |
| 2026-09-29 19:17:24 | [CVE-2026-102823](https://nvd.nist.gov/vuln/detail/CVE-2026-102823) | High | 7.5 | Russh is a Rust SSH client and server library. Prior to 0.63.1, client_read_authenticated in russh/src/client/encrypted… |
| 2026-09-29 19:17:24 | [CVE-2026-102824](https://nvd.nist.gov/vuln/detail/CVE-2026-102824) | Medium | 4.3 | Russh is a Rust SSH client and server library. Prior to 0.63.0, the hybrid ML-KEM 768 and X25519 implementation in russ… |
| 2026-09-29 19:17:24 | [CVE-2026-102825](https://nvd.nist.gov/vuln/detail/CVE-2026-102825) | Low | 3.7 | Russh is a Rust SSH client and server library. Prior to 0.62.6, the USERAUTH_REQUEST path reached from server::run_stre… |
| 2026-09-29 19:17:24 | [CVE-2026-102826](https://nvd.nist.gov/vuln/detail/CVE-2026-102826) | High | 8.1 | simple-git, an interface for running git commands in any node.js application, enables applications to execute Git opera… |
| 2026-09-29 19:17:25 | [CVE-2026-102827](https://nvd.nist.gov/vuln/detail/CVE-2026-102827) | High | 8.1 | simple-git, an interface for running git commands in any node.js application, enables applications to execute Git opera… |
| 2026-09-29 19:17:25 | [CVE-2026-102828](https://nvd.nist.gov/vuln/detail/CVE-2026-102828) | Critical | 9.2 | simple-git, an interface for running git commands in any node.js application, enables applications to execute Git opera… |
| 2026-09-29 19:17:25 | [CVE-2026-102829](https://nvd.nist.gov/vuln/detail/CVE-2026-102829) | Critical | 9.2 | simple-git, an interface for running git commands in any node.js application, enables applications to execute Git opera… |
| 2026-09-29 19:17:25 | [CVE-2026-102830](https://nvd.nist.gov/vuln/detail/CVE-2026-102830) | Medium | 6.8 | JupyterLab is an extensible environment for interactive and reproducible computing, based on the Jupyter Notebook Archi… |
| 2026-09-29 19:17:25 | [CVE-2026-102831](https://nvd.nist.gov/vuln/detail/CVE-2026-102831) | High | 8.1 | JupyterLab is an extensible environment for interactive and reproducible computing, based on the Jupyter Notebook Archi… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
