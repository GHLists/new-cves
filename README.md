# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-08 14:22 UTC

New CVEs published between 2026-10-08 13:19 UTC and 2026-10-08 14:22 UTC.

[Full CSV](data/new-cves-2026-10-08T14-22-42-82899Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-08 14:16:46 | [CVE-2026-103663](https://nvd.nist.gov/vuln/detail/CVE-2026-103663) | Critical | 9.4 | Ollama is vulnerable to path traversal in the `/api/pull` endpoint due to insufficient validation of layer digests by t… |
| 2026-10-08 14:16:46 | [CVE-2026-104634](https://nvd.nist.gov/vuln/detail/CVE-2026-104634) | Low | 2.3 | Incorrect Type Conversion or Cast vulnerability in BeamMCP.Server in ScriptKittyOS beam_mcp allows an MCP client's JSON… |
| 2026-10-08 14:16:49 | [CVE-2026-107611](https://nvd.nist.gov/vuln/detail/CVE-2026-107611) | High | 7.1 | An out-of-bounds read vulnerability in the ZRLE decoder of GlavSoft TightVNC Viewer for Windows before 2.8.88 allows a… |
| 2026-10-08 14:16:49 | [CVE-2026-107612](https://nvd.nist.gov/vuln/detail/CVE-2026-107612) | High | 7.8 | Incorrect permission assignment in GlavSoft TightVNC Server for Windows before 2.8.88 allows a local authenticated user… |
| 2026-10-08 14:16:50 | [CVE-2026-107613](https://nvd.nist.gov/vuln/detail/CVE-2026-107613) | Medium | 5.9 | A NULL pointer dereference vulnerability in the Win8ScreenDriver component of GlavSoft TightVNC Server for Windows befo… |
| 2026-10-08 14:16:50 | [CVE-2026-107614](https://nvd.nist.gov/vuln/detail/CVE-2026-107614) | Medium | 6.1 | An integer underflow in WinCursorShapeUtils::trimTransparent() in GlavSoft TightVNC Server for Windows before 2.8.88 al… |
| 2026-10-08 14:16:50 | [CVE-2026-107615](https://nvd.nist.gov/vuln/detail/CVE-2026-107615) | High | 7.8 | An uncontrolled search path element vulnerability in GlavSoft TightVNC Server for Windows before 2.8.88 allows a local… |
| 2026-10-08 14:16:51 | [CVE-2026-14990](https://nvd.nist.gov/vuln/detail/CVE-2026-14990) | Critical | 9.3 | IBM DataPower Gateway 10.6.0.0 through 10.6.0.10 is vulnerable to cross-site scripting. This vulnerability allows an un… |
| 2026-10-08 14:16:51 | [CVE-2026-14991](https://nvd.nist.gov/vuln/detail/CVE-2026-14991) | Critical | 9.8 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:51 | [CVE-2026-15762](https://nvd.nist.gov/vuln/detail/CVE-2026-15762) | Critical | 9.8 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:52 | [CVE-2026-15781](https://nvd.nist.gov/vuln/detail/CVE-2026-15781) | High | 8.0 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:52 | [CVE-2026-15784](https://nvd.nist.gov/vuln/detail/CVE-2026-15784) | High | 8.1 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:52 | [CVE-2026-15819](https://nvd.nist.gov/vuln/detail/CVE-2026-15819) | High | 7.5 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:52 | [CVE-2026-15822](https://nvd.nist.gov/vuln/detail/CVE-2026-15822) | High | 7.5 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:52 | [CVE-2026-15824](https://nvd.nist.gov/vuln/detail/CVE-2026-15824) | High | 8.2 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:52 | [CVE-2026-16111](https://nvd.nist.gov/vuln/detail/CVE-2026-16111) | High | 7.5 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:52 | [CVE-2026-16159](https://nvd.nist.gov/vuln/detail/CVE-2026-16159) | High | 8.6 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:53 | [CVE-2026-16161](https://nvd.nist.gov/vuln/detail/CVE-2026-16161) | High | 7.5 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:53 | [CVE-2026-16163](https://nvd.nist.gov/vuln/detail/CVE-2026-16163) | High | 8.6 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:53 | [CVE-2026-16164](https://nvd.nist.gov/vuln/detail/CVE-2026-16164) | High | 7.5 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:53 | [CVE-2026-16165](https://nvd.nist.gov/vuln/detail/CVE-2026-16165) | High | 7.5 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:53 | [CVE-2026-16167](https://nvd.nist.gov/vuln/detail/CVE-2026-16167) | High | 7.5 | IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 throu… |
| 2026-10-08 14:16:54 | [CVE-2026-27420](https://nvd.nist.gov/vuln/detail/CVE-2026-27420) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Katie Seaborn Zot… |
| 2026-10-08 14:16:54 | [CVE-2026-42698](https://nvd.nist.gov/vuln/detail/CVE-2026-42698) | Medium | 5.3 | Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition') vulnerability in Themeum Tu… |
| 2026-10-08 14:17:01 | [CVE-2026-88257](https://nvd.nist.gov/vuln/detail/CVE-2026-88257) | Medium | 5.3 | Improper Input Validation vulnerability in BeamMCP.Schema in ScriptKittyOS beam_mcp allows an MCP client to reach a too… |
| 2026-10-08 14:17:02 | [CVE-2026-89290](https://nvd.nist.gov/vuln/detail/CVE-2026-89290) | Low | 3.5 | Improper neutralization of Script-Related HTML tags in a web page (basic XSS) vulnerability in İzometri IT Services Dom… |
| 2026-10-08 14:17:02 | [CVE-2026-91844](https://nvd.nist.gov/vuln/detail/CVE-2026-91844) | High | 7.3 | Unrestricted upload of file with dangerous type vulnerability in İzometri IT Services Domestic and Foreign Trade Co. Lt… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
