# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-20 10:20 UTC

New CVEs published between 2026-10-20 09:18 UTC and 2026-10-20 10:20 UTC.

[Full CSV](data/new-cves-2026-10-20T10-20-47-963266Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-20 10:17:01 | [CVE-2026-111844](https://nvd.nist.gov/vuln/detail/CVE-2026-111844) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Brizy Brizy brizy… |
| 2026-10-20 10:17:03 | [CVE-2026-112064](https://nvd.nist.gov/vuln/detail/CVE-2026-112064) | High | 7.1 | The backend module for reviewing the consent history accepted sorting, grouping and index options from the request and… |
| 2026-10-20 10:17:03 | [CVE-2026-112065](https://nvd.nist.gov/vuln/detail/CVE-2026-112065) | Medium | 5.3 | The routes that provide consent history and statistics data did not check whether the backend user had access to the mo… |
| 2026-10-20 10:17:03 | [CVE-2026-112066](https://nvd.nist.gov/vuln/detail/CVE-2026-112066) | High | 7.1 | The JSON import of the cookie consent configuration did not respect the backend user's permissions. Non-admin backend u… |
| 2026-10-20 10:17:03 | [CVE-2026-112067](https://nvd.nist.gov/vuln/detail/CVE-2026-112067) | Medium | 6.9 | The extension hides the correct answer to each CAPTCHA inside the image data of the CAPTCHA itself. Anyone who can requ… |
| 2026-10-20 10:17:04 | [CVE-2026-112068](https://nvd.nist.gov/vuln/detail/CVE-2026-112068) | Medium | 5.3 | The backend module does not check whether a backend user has access to the requested site. Users with access to the mod… |
| 2026-10-20 10:17:04 | [CVE-2026-112069](https://nvd.nist.gov/vuln/detail/CVE-2026-112069) | Medium | 6.3 | The extension no longer applied its access protection to files in file storages that use a non-default relative base pa… |
| 2026-10-20 10:17:04 | [CVE-2026-112070](https://nvd.nist.gov/vuln/detail/CVE-2026-112070) | Medium | 5.3 | The AJAX routes of the extension do not check whether a backend user has access to the related module or dashboard widg… |
| 2026-10-20 10:17:04 | [CVE-2026-112071](https://nvd.nist.gov/vuln/detail/CVE-2026-112071) | Medium | 6.9 | The order cancellation function accepts an order identifier from the request and acts on that order without checking th… |
| 2026-10-20 10:17:04 | [CVE-2026-112237](https://nvd.nist.gov/vuln/detail/CVE-2026-112237) | Medium | 6.9 | The extension provides a public proxy endpoint that fetches a URL on behalf of the visitor. For one HTTP request method… |
| 2026-10-20 10:17:04 | [CVE-2026-112238](https://nvd.nist.gov/vuln/detail/CVE-2026-112238) | High | 8.7 | The file search of the extension builds its database conditions by wrapping the search term in quotes itself. Only the… |
| 2026-10-20 10:17:04 | [CVE-2026-112239](https://nvd.nist.gov/vuln/detail/CVE-2026-112239) | High | 7.2 | The extension provides a backend endpoint that writes a submitted value into a submitted field of a submitted page reco… |
| 2026-10-20 10:17:04 | [CVE-2026-112240](https://nvd.nist.gov/vuln/detail/CVE-2026-112240) | Medium | 6.3 | The download link for files uploaded through a form relied on a token that could be predicted. The file name in the req… |
| 2026-10-20 10:17:05 | [CVE-2026-113378](https://nvd.nist.gov/vuln/detail/CVE-2026-113378) | Low | 1.9 | A security flaw has been discovered in mcollina mcp-ripgrep up to 0.4.0. Affected is an unknown function of the file sr… |
| 2026-10-20 10:17:05 | [CVE-2026-113381](https://nvd.nist.gov/vuln/detail/CVE-2026-113381) | Medium | 5.5 | A weakness has been identified in Osclass up to 8.3.1. Affected by this vulnerability is the function Item::findUserIte… |
| 2026-10-20 10:17:05 | [CVE-2026-113442](https://nvd.nist.gov/vuln/detail/CVE-2026-113442) | Medium | 5.3 | Values entered by visitors were placed into the HTML summary email without being escaped. An unauthenticated attacker c… |
| 2026-10-20 10:17:05 | [CVE-2026-113459](https://nvd.nist.gov/vuln/detail/CVE-2026-113459) | High | 7.1 | In versions running on TYPO3 10 and 11, the configured OpenAI API key is embedded in every backend page, so that the ed… |
| 2026-10-20 10:17:05 | [CVE-2026-113468](https://nvd.nist.gov/vuln/detail/CVE-2026-113468) | Medium | 6.9 | The payment notification endpoint for PayPal accepts incoming data without verifying that it comes from the payment pro… |
| 2026-10-20 10:17:05 | [CVE-2026-43849](https://nvd.nist.gov/vuln/detail/CVE-2026-43849) | Medium | 6.9 | A heap memory read vulnerability could allow an attacker to exfiltrate sensitive data. |
| 2026-10-20 10:17:05 | [CVE-2026-43850](https://nvd.nist.gov/vuln/detail/CVE-2026-43850) | High | 8.6 | A command injection vulnerability could allow an authenticated attacker to achieve root-level code execution on the sys… |
| 2026-10-20 10:17:06 | [CVE-2026-43851](https://nvd.nist.gov/vuln/detail/CVE-2026-43851) | High | 8.2 | A path traversal vulnerability could allow an authenticated attacker to read arbitrary files on the system. |
| 2026-10-20 10:17:06 | [CVE-2026-43852](https://nvd.nist.gov/vuln/detail/CVE-2026-43852) | High | 8.2 | A vulnerability could allow an authenticated attacker to write files to arbitrary locations on the system. |
| 2026-10-20 10:17:06 | [CVE-2026-43853](https://nvd.nist.gov/vuln/detail/CVE-2026-43853) | High | 8.2 | A vulnerability could allow an attacker to send a crafted message to trigger an assertion fault, causing the service to… |
| 2026-10-20 10:17:06 | [CVE-2026-43854](https://nvd.nist.gov/vuln/detail/CVE-2026-43854) | Medium | 6.3 | A vulnerability could allow an attacker with access to an encrypted project file to retrieve administrator credentials… |
| 2026-10-20 10:17:06 | [CVE-2026-43855](https://nvd.nist.gov/vuln/detail/CVE-2026-43855) | High | 7.5 | A heap-based buffer overflow vulnerability could allow a remote authenticated attacker to achieve arbitrary code execut… |
| 2026-10-20 10:17:06 | [CVE-2026-43856](https://nvd.nist.gov/vuln/detail/CVE-2026-43856) | High | 8.6 | A stack-based buffer overflow vulnerability in the FileProcess::CheckDir function could allow a remote authenticated at… |
| 2026-10-20 10:17:06 | [CVE-2026-43857](https://nvd.nist.gov/vuln/detail/CVE-2026-43857) | High | 8.6 | A vulnerability could allow a remote authenticated attacker to achieve arbitrary code execution with privileges on the… |
| 2026-10-20 10:17:06 | [CVE-2026-43858](https://nvd.nist.gov/vuln/detail/CVE-2026-43858) | High | 8.6 | A stack-based buffer overflow vulnerability could allow a remote authenticated attacker to achieve arbitrary code execu… |
| 2026-10-20 10:17:07 | [CVE-2026-85267](https://nvd.nist.gov/vuln/detail/CVE-2026-85267) | High | 8.7 | A Cross-Site WebSocket Hijacking vulnerability in Cloud Shell prior to 2026-07-22 on Google Cloud Platform allows an un… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
