# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-05 15:18 UTC

New CVEs published between 2026-10-05 14:19 UTC and 2026-10-05 15:18 UTC.

[Full CSV](data/new-cves-2026-10-05T15-18-39-059388Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-05 15:17:21 | [CVE-2026-105421](https://nvd.nist.gov/vuln/detail/CVE-2026-105421) | Medium | 5.3 | Missing Authorization vulnerability in Kit Kit (formerly ConvertKit) for WooCommerce convertkit-for-woocommerce allows… |
| 2026-10-05 15:17:22 | [CVE-2026-79820](https://nvd.nist.gov/vuln/detail/CVE-2026-79820) | Critical | 9.0 | A remote user validation failure vulnerability exists in HPE Integrated Lights-Out (iLO) 7 firmware. |
| 2026-10-05 15:17:22 | [CVE-2026-88391](https://nvd.nist.gov/vuln/detail/CVE-2026-88391) |  |  | Northstar (dromara/northstar, quantitative trading platform) <= 9.1.1 enables the H2 Console but its auth interceptor o… |
| 2026-10-05 15:17:22 | [CVE-2026-88392](https://nvd.nist.gov/vuln/detail/CVE-2026-88392) |  |  | Unimall v4 is vulnerable to Directory Traversal in FileUploadController.local(). This allows an attacker to execute arb… |
| 2026-10-05 15:17:22 | [CVE-2026-88394](https://nvd.nist.gov/vuln/detail/CVE-2026-88394) |  |  | WookTeam v1.6.6 and before is vulnerable to a Directory Traversal. The project task export endpoint /api/project/task/e… |
| 2026-10-05 15:17:23 | [CVE-2026-89039](https://nvd.nist.gov/vuln/detail/CVE-2026-89039) | Medium | 6.5 | The convert_playwright_script prompt in the k6 MCP server accepts a file path as its playwright_script argument. Paths… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
