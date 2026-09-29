# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 21:22 UTC

New CVEs published between 2026-09-29 20:19 UTC and 2026-09-29 21:22 UTC.

[Full CSV](data/new-cves-2026-09-29T21-22-21-242162Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 21:17:13 | [CVE-2026-102253](https://nvd.nist.gov/vuln/detail/CVE-2026-102253) | High | 8.7 | iperf3 versions prior to 3.22 contains a denial of service vulnerability that allows unauthenticated remote attackers t… |
| 2026-09-29 21:17:18 | [CVE-2026-102620](https://nvd.nist.gov/vuln/detail/CVE-2026-102620) | Low | 1.9 | A vulnerability was determined in Freedesktop Poppler 26.06.0/26.07.0/26.08.0. This impacts the function FoFiTrueType::… |
| 2026-09-29 21:17:18 | [CVE-2026-102904](https://nvd.nist.gov/vuln/detail/CVE-2026-102904) | Medium | 5.4 | JupyterLab is an extensible environment for interactive and reproducible computing, based on the Jupyter Notebook Archi… |
| 2026-09-29 21:17:18 | [CVE-2026-102925](https://nvd.nist.gov/vuln/detail/CVE-2026-102925) | High | 7.8 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.7.13, the generated activate (bash… |
| 2026-09-29 21:17:18 | [CVE-2026-102930](https://nvd.nist.gov/vuln/detail/CVE-2026-102930) | High | 7.7 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.7.12, download_wheel() accepts pip… |
| 2026-09-29 21:17:18 | [CVE-2026-102937](https://nvd.nist.gov/vuln/detail/CVE-2026-102937) | High | 7.3 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.7.12, BatchActivator.quote() return… |
| 2026-09-29 21:17:19 | [CVE-2026-102938](https://nvd.nist.gov/vuln/detail/CVE-2026-102938) | Medium | 5.8 | virtualenv is a tool for creating isolated virtual python environments. Prior to 21.7.11, PyEnvCfg.write() writes promp… |
| 2026-09-29 21:19:31 | [CVE-2026-81841](https://nvd.nist.gov/vuln/detail/CVE-2026-81841) | Medium | 5.3 | Pausing a shared (public) dashboard did not revoke its access token for the endpoints that serve frontend bootstrap dat… |
| 2026-09-29 21:19:31 | [CVE-2026-81842](https://nvd.nist.gov/vuln/detail/CVE-2026-81842) | Medium | 4.3 | An authenticated user with edit permission on one folder can move a library panel into another folder where they only h… |
| 2026-09-29 21:19:39 | [CVE-2026-93853](https://nvd.nist.gov/vuln/detail/CVE-2026-93853) | High | 7.2 | Unverified ownership in Barman snapshot backup deletion allows a principal who can write the backup catalog to cause Ba… |
| 2026-09-29 21:19:39 | [CVE-2026-94204](https://nvd.nist.gov/vuln/detail/CVE-2026-94204) | High | 8.7 | The central cloud storage backend for the entire dashcam platform is misconfigured with public-read permissions, allowi… |
| 2026-09-29 21:19:39 | [CVE-2026-94952](https://nvd.nist.gov/vuln/detail/CVE-2026-94952) |  |  | A stack-based buffer overflow vulnerability exists in the web management interface of TOTOLINK N150RT (NTR150) firmware… |
| 2026-09-29 21:19:39 | [CVE-2026-96587](https://nvd.nist.gov/vuln/detail/CVE-2026-96587) | Critical | 10.0 | The Viidure Android application embeds permanent, plaintext cloud storage credentials within its compiled code. These c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
