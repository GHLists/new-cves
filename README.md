# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-11 02:19 UTC

New CVEs published between 2026-10-11 01:18 UTC and 2026-10-11 02:19 UTC.

[Full CSV](data/new-cves-2026-10-11T02-19-56-87255Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-11 02:16:35 | [CVE-2026-108688](https://nvd.nist.gov/vuln/detail/CVE-2026-108688) | Medium | 5.3 | Eladmin through 2.7 contains a missing authorization vulnerability in the LocalStorageController uploadPicture handler… |
| 2026-10-11 02:16:36 | [CVE-2026-108689](https://nvd.nist.gov/vuln/detail/CVE-2026-108689) | Medium | 5.3 | Wukong AICRM through 20260610 contains a missing authorization vulnerability that allows authenticated users to write i… |
| 2026-10-11 02:16:37 | [CVE-2026-108690](https://nvd.nist.gov/vuln/detail/CVE-2026-108690) | Medium | 5.3 | mall4j through 4.0 contains an information disclosure vulnerability that allows authenticated customers to read other s… |
| 2026-10-11 02:16:37 | [CVE-2026-108691](https://nvd.nist.gov/vuln/detail/CVE-2026-108691) | Medium | 5.3 | mall4j through 4.0 contains an improper authorization vulnerability that allows authenticated storefront customers to d… |
| 2026-10-11 02:16:37 | [CVE-2026-108692](https://nvd.nist.gov/vuln/detail/CVE-2026-108692) | High | 7.1 | 1Panel-dev CordysCRM from 1.9.0 before 1.9.2 contains a missing authorization vulnerability in eight ModuleFieldControl… |
| 2026-10-11 02:16:37 | [CVE-2026-108693](https://nvd.nist.gov/vuln/detail/CVE-2026-108693) | High | 7.3 | ImageMagick on Windows through 7.1.2-33 and 6.9.13-58 contains an uncontrolled search path vulnerability in NTGhostscri… |
| 2026-10-11 02:16:37 | [CVE-2026-108694](https://nvd.nist.gov/vuln/detail/CVE-2026-108694) | High | 7.1 | ConvertX through 0.19.0 contains an arbitrary file read vulnerability that allows authenticated users to read server fi… |
| 2026-10-11 02:16:37 | [CVE-2026-108695](https://nvd.nist.gov/vuln/detail/CVE-2026-108695) | High | 7.1 | MultiVendorX WordPress plugin through 5.0.19 contains an incorrect authorization vulnerability that allows vendor accou… |
| 2026-10-11 02:16:38 | [CVE-2026-108696](https://nvd.nist.gov/vuln/detail/CVE-2026-108696) | Medium | 5.3 | CoreShop through 1.5.5 contains an authorization bypass vulnerability in the OrderController that allows authenticated… |
| 2026-10-11 02:16:38 | [CVE-2026-108700](https://nvd.nist.gov/vuln/detail/CVE-2026-108700) | High | 7.1 | 1Panel-dev CordysCRM before 1.9.2 contains a missing authorization vulnerability that allows authenticated users to lis… |
| 2026-10-11 02:16:38 | [CVE-2026-108701](https://nvd.nist.gov/vuln/detail/CVE-2026-108701) | Medium | 5.3 | 1Panel-dev CordysCRM before 1.9.2 contains a missing authorization vulnerability in the ContractController sortModule h… |
| 2026-10-11 02:16:38 | [CVE-2026-108702](https://nvd.nist.gov/vuln/detail/CVE-2026-108702) | Medium | 5.3 | 1Panel-dev CordysCRM through 1.9.3 lacks a PROCESS_SETTING permission check on POST /approval-flow/webhook/test, allowi… |
| 2026-10-11 02:16:38 | [CVE-2026-108703](https://nvd.nist.gov/vuln/detail/CVE-2026-108703) | Medium | 5.3 | CordysCRM through 1.9.3 contains a missing authorization vulnerability in POST /approval-resource/push that allows auth… |
| 2026-10-11 02:16:38 | [CVE-2026-108704](https://nvd.nist.gov/vuln/detail/CVE-2026-108704) | Medium | 5.3 | CordysCRM through 1.9.3 contains an authorization bypass vulnerability that allows low-privileged authenticated users t… |
| 2026-10-11 02:16:39 | [CVE-2026-108705](https://nvd.nist.gov/vuln/detail/CVE-2026-108705) | Medium | 5.3 | CordysCRM through 1.9.3 contains a missing authorization vulnerability in the POST /custom-form/data/import endpoint th… |
| 2026-10-11 02:16:39 | [CVE-2026-108706](https://nvd.nist.gov/vuln/detail/CVE-2026-108706) | Medium | 5.3 | eladmin through commit 55fbf70 contains a missing authorization vulnerability in the downloadS3Storage handler that all… |
| 2026-10-11 02:16:39 | [CVE-2026-108707](https://nvd.nist.gov/vuln/detail/CVE-2026-108707) | Critical | 9.3 | Wukong_HRM through commit 186115e contains an authentication bypass vulnerability in ParamAspect that allows unauthenti… |
| 2026-10-11 02:16:39 | [CVE-2026-108708](https://nvd.nist.gov/vuln/detail/CVE-2026-108708) | High | 8.7 | Wukong_HRM through commit 186115e contains a missing authorization vulnerability because EmployeeAspect assigns every c… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
