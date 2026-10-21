# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 21:20 UTC

New CVEs published between 2026-10-21 20:18 UTC and 2026-10-21 21:20 UTC.

[Full CSV](data/new-cves-2026-10-21T21-20-04-311885Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 21:17:55 | [CVE-2026-113811](https://nvd.nist.gov/vuln/detail/CVE-2026-113811) |  |  | Algorithm::UrataniTakeda versions from 0.1.5 before 0.1.7 for Perl allow memory exhaustion via a never-cleared failure… |
| 2026-10-21 21:17:56 | [CVE-2026-114137](https://nvd.nist.gov/vuln/detail/CVE-2026-114137) | High | 7.4 | Django REST framework is a toolkit for building Web APIs. From 3.12.0 until 3.18.2, TokenProxy.delete() in rest_framewo… |
| 2026-10-21 21:17:56 | [CVE-2026-114138](https://nvd.nist.gov/vuln/detail/CVE-2026-114138) | High | 7.5 | Django REST framework is a toolkit for building Web APIs. Prior to 3.18.2, DefaultContentNegotiation.get_accept_list in… |
| 2026-10-21 21:17:56 | [CVE-2026-114139](https://nvd.nist.gov/vuln/detail/CVE-2026-114139) | Critical | 9.1 | Sentry-Javascript is an official Sentry SDKs for JavaScript. From 9.36.0 until 9.47.2, 10.75.2, and 11.0.0-rc.1, the we… |
| 2026-10-21 21:17:56 | [CVE-2026-114140](https://nvd.nist.gov/vuln/detail/CVE-2026-114140) | High | 8.8 | The nbconvert tool, jupyter nbconvert, converts Jupyter notebooks to various other formats via Jinja templates. From 5.… |
| 2026-10-21 21:17:56 | [CVE-2026-114141](https://nvd.nist.gov/vuln/detail/CVE-2026-114141) | High | 8.7 | toml-node is a TOML parser for Node.js and the browser. Prior to 5.0.1, the toml.parse() compiler's addTableArray() fun… |
| 2026-10-21 21:17:56 | [CVE-2026-114142](https://nvd.nist.gov/vuln/detail/CVE-2026-114142) | High | 8.8 | toml-node is a TOML parser for Node.js and the browser. Prior to 5.0.1, toml.parse() can write attacker-controlled prop… |
| 2026-10-21 21:17:56 | [CVE-2026-114143](https://nvd.nist.gov/vuln/detail/CVE-2026-114143) | High | 8.7 | toml-node is a TOML parser for Node.js and the browser. Prior to 5.0.1, toml.parse() repeatedly slices and rejoins ever… |
| 2026-10-21 21:17:57 | [CVE-2026-114144](https://nvd.nist.gov/vuln/detail/CVE-2026-114144) | High | 7.5 | toml-node is a TOML parser for Node.js and the browser. Prior to 5.0.1, toml.parse() passes unbounded hexadecimal, octa… |
| 2026-10-21 21:17:57 | [CVE-2026-114145](https://nvd.nist.gov/vuln/detail/CVE-2026-114145) | High | 7.5 | GitPython is a python library used to interact with Git repositories. Prior to 3.2.1, create_submodule() in git/objects… |
| 2026-10-21 21:17:57 | [CVE-2026-114377](https://nvd.nist.gov/vuln/detail/CVE-2026-114377) | Low | 2.0 | A security vulnerability has been detected in leomoon-studios wiki-go up to 1.9.1. Affected by this issue is the functi… |
| 2026-10-21 21:17:57 | [CVE-2026-114378](https://nvd.nist.gov/vuln/detail/CVE-2026-114378) | Low | 2.1 | A vulnerability was detected in itsourcecode Online Cake Ordering System 1.0. This affects an unknown part of the file… |
| 2026-10-21 21:17:57 | [CVE-2026-114379](https://nvd.nist.gov/vuln/detail/CVE-2026-114379) | Medium | 5.3 | A flaw has been found in EKKOLearnAI ekko-studio up to 1.0.6. This vulnerability affects the function saveGeneratedImag… |
| 2026-10-21 21:17:58 | [CVE-2026-114380](https://nvd.nist.gov/vuln/detail/CVE-2026-114380) | Low | 2.1 | A vulnerability was found in itsourcecode Online Cake Ordering System 1.0. Impacted is an unknown function of the file… |
| 2026-10-21 21:17:58 | [CVE-2026-114406](https://nvd.nist.gov/vuln/detail/CVE-2026-114406) | Medium | 6.8 | The system certificate authority (CA) store in Red Hat products, distributed via ca-certificates RPM packages, included… |
| 2026-10-21 21:17:59 | [CVE-2026-29001](https://nvd.nist.gov/vuln/detail/CVE-2026-29001) | High | 8.6 | TastyIgniter through 4.4.5 contain a PHP object injection vulnerability that allows authenticated administrators to ach… |
| 2026-10-21 21:19:17 | [CVE-2026-82987](https://nvd.nist.gov/vuln/detail/CVE-2026-82987) |  |  | There exists a screen capture endpoint in vCast media streaming service in ViewSonic ViewBoard unknown allows a remote,… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
