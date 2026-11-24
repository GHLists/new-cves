# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 20:22 UTC

New CVEs published between 2026-11-24 19:18 UTC and 2026-11-24 20:22 UTC.

[Full CSV](data/new-cves-2026-11-24T20-22-08-080483Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 20:18:21 | [CVE-2026-112732](https://nvd.nist.gov/vuln/detail/CVE-2026-112732) | Critical | 9.8 | Double free in Microsoft Office Visio allows an unauthorized attacker to execute code over a network. |
| 2026-11-24 20:18:45 | [CVE-2026-123215](https://nvd.nist.gov/vuln/detail/CVE-2026-123215) | Critical | 9.3 | Copeland XWEB Pro contains a missing authentication vulnerability. Fixed in 1.16.1. |
| 2026-11-24 20:18:46 | [CVE-2026-123216](https://nvd.nist.gov/vuln/detail/CVE-2026-123216) | High | 8.5 | Copeland XWEB Pro contains an OS command injection vulnerability that allows a remote, authenticated attacker to execut… |
| 2026-11-24 20:18:46 | [CVE-2026-123217](https://nvd.nist.gov/vuln/detail/CVE-2026-123217) | Low | 2.3 | Copeland XWEB Pro allows a remote, authenticated attacker to inject additional arguments into the wireless interface co… |
| 2026-11-24 20:18:47 | [CVE-2026-123340](https://nvd.nist.gov/vuln/detail/CVE-2026-123340) | High | 8.5 | Copeland XWEB Pro contains an OS command injection vulnerability that allows a remote, authenticated attacker to execut… |
| 2026-11-24 20:18:48 | [CVE-2026-126695](https://nvd.nist.gov/vuln/detail/CVE-2026-126695) | High | 8.7 | Use of hard-coded password vulnerability in Tibco Control Plane and Tibco Control Tower. This issue affects Control Pla… |
| 2026-11-24 20:18:52 | [CVE-2026-135046](https://nvd.nist.gov/vuln/detail/CVE-2026-135046) | High | 8.8 | Cross-Site Request Forgery (CSRF) vulnerability in Rymera Web Co Store Exporter woocommerce-exporter allows Cross Site… |
| 2026-11-24 20:18:52 | [CVE-2026-135414](https://nvd.nist.gov/vuln/detail/CVE-2026-135414) | Medium | 5.1 | Server-side request forgery in Amazon OpenSearch Service service software before R20260720 might allow an authenticated… |
| 2026-11-24 20:18:52 | [CVE-2026-135799](https://nvd.nist.gov/vuln/detail/CVE-2026-135799) | Low | 2.0 | A vulnerability was detected in flowable flowable-engine 8.0.0. This impacts the function createElContext/importFunctio… |
| 2026-11-24 20:18:53 | [CVE-2026-135800](https://nvd.nist.gov/vuln/detail/CVE-2026-135800) | Medium | 6.9 | A flaw has been found in hiyouga LLaMA-Factory up to 0.9.5. Affected is the function save_args/load_args of the file sr… |
| 2026-11-24 20:18:53 | [CVE-2026-136328](https://nvd.nist.gov/vuln/detail/CVE-2026-136328) | High | 7.8 | A flaw was found in the file-psd plugin in GIMP. When processing a specially crafted PSD (Photoshop Document) image fil… |
| 2026-11-24 20:18:53 | [CVE-2026-136452](https://nvd.nist.gov/vuln/detail/CVE-2026-136452) | Medium | 5.3 | browser-use before 1.0.0 contains a URL parser differential vulnerability in SecurityWatchdog that allows attackers to… |
| 2026-11-24 20:18:53 | [CVE-2026-136453](https://nvd.nist.gov/vuln/detail/CVE-2026-136453) | High | 7.1 | browser-use before 1.0.0 contains an allowlist bypass vulnerability in the SecurityWatchdog's _is_url_match function th… |
| 2026-11-24 20:18:53 | [CVE-2026-136455](https://nvd.nist.gov/vuln/detail/CVE-2026-136455) | High | 8.7 | borg-ui before 2.4.1 contains a privilege escalation vulnerability that allows a repository-scoped operator to escalate… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
