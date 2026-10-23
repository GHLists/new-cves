# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 22:18 UTC

New CVEs published between 2026-10-23 21:19 UTC and 2026-10-23 22:18 UTC.

[Full CSV](data/new-cves-2026-10-23T22-18-40-874758Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 22:16:57 | [CVE-2026-115801](https://nvd.nist.gov/vuln/detail/CVE-2026-115801) | Low | 1.9 | A security flaw has been discovered in Kakao khaiii up to 0.4. The impacted element is the function khaiii::nn::Linear:… |
| 2026-10-23 22:16:57 | [CVE-2026-115883](https://nvd.nist.gov/vuln/detail/CVE-2026-115883) | Medium | 6.0 | LangGraph checkpoint savers provide Postgres- and SQLite-backed state persistence for LangGraph workflows and agents. P… |
| 2026-10-23 22:16:57 | [CVE-2026-115885](https://nvd.nist.gov/vuln/detail/CVE-2026-115885) | Medium | 4.1 | The LangGraph CLI is the official command-line interface for LangGraph. From 0.4.15 until 0.4.32, langgraph deploy --ve… |
| 2026-10-23 22:16:58 | [CVE-2026-115886](https://nvd.nist.gov/vuln/detail/CVE-2026-115886) | Medium | 6.5 | MLflow is an open source AI engineering platform for agents, large language models, and machine learning models. From 3… |
| 2026-10-23 22:16:58 | [CVE-2026-115887](https://nvd.nist.gov/vuln/detail/CVE-2026-115887) | High | 7.5 | GraphQL Scalars is a library of custom GraphQL scalars for creating precise type-safe GraphQL schemas. From 1.24.1 unti… |
| 2026-10-23 22:16:58 | [CVE-2026-115889](https://nvd.nist.gov/vuln/detail/CVE-2026-115889) | Critical | 9.9 | Wasmtime is a runtime for WebAssembly. Prior to 36.0.19 and 43.0.0, the Cranelift compiler backend bit-packs SSA value… |
| 2026-10-23 22:16:58 | [CVE-2026-115892](https://nvd.nist.gov/vuln/detail/CVE-2026-115892) | Medium | 5.7 | Wasmtime is a runtime for WebAssembly. From 46.0.0 until 48.0.7 and 49.0.4, lowering a host-created component-model str… |
| 2026-10-23 22:16:58 | [CVE-2026-115893](https://nvd.nist.gov/vuln/detail/CVE-2026-115893) | Critical | 9.9 | Wasmtime is a runtime for WebAssembly. Prior to 36.0.19, 48.0.7, and 49.0.4, the Cranelift compiler backend on aarch64… |
| 2026-10-23 22:16:58 | [CVE-2026-115895](https://nvd.nist.gov/vuln/detail/CVE-2026-115895) | High | 8.8 | Happy DOM is a JavaScript implementation of a web browser without its graphical user interface. From 17.0.0 until 21.0.… |
| 2026-10-23 22:16:59 | [CVE-2026-115897](https://nvd.nist.gov/vuln/detail/CVE-2026-115897) | Low | 2.1 | Serialize JavaScript serializes JavaScript values to a superset of JSON that includes regular expressions and functions… |
| 2026-10-23 22:16:59 | [CVE-2026-115935](https://nvd.nist.gov/vuln/detail/CVE-2026-115935) | High | 8.7 | The app/process-api-response-headers action accepts fake Craft API response headers from any authenticated control pane… |
| 2026-10-23 22:16:59 | [CVE-2026-115937](https://nvd.nist.gov/vuln/detail/CVE-2026-115937) | High | 8.7 | The Mollie webhook endpoint accepts two independent, attacker-controlled parameters and never verifies that they belong… |
| 2026-10-23 22:16:59 | [CVE-2026-115938](https://nvd.nist.gov/vuln/detail/CVE-2026-115938) | High | 8.7 | Craft CMS allows any authenticated control panel user to submit an element-search condition whose element selector is e… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
