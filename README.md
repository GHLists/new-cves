# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 21:19 UTC

New CVEs published between 2026-11-25 20:21 UTC and 2026-11-25 21:19 UTC.

[Full CSV](data/new-cves-2026-11-25T21-19-08-980693Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 21:17:15 | [CVE-2026-102957](https://nvd.nist.gov/vuln/detail/CVE-2026-102957) | High | 7.7 | z_impl_pwm_capture_cycles() in drivers/pwm/pwm_capture.c stores its capture context (struct z_pwm_capture_cb_data, incl… |
| 2026-11-25 21:17:15 | [CVE-2026-102959](https://nvd.nist.gov/vuln/detail/CVE-2026-102959) | Medium | 6.4 | The Grow R502-A fingerprint sensor driver (drivers/sensor/grow_r502a/grow_r502a.c) points drv_data->rx_buf.data at an r… |
| 2026-11-25 21:17:16 | [CVE-2026-102960](https://nvd.nist.gov/vuln/detail/CVE-2026-102960) | Medium | 6.8 | The Grow R502-A fingerprint sensor driver (drivers/sensor/grow_r502a/grow_r502a.c) receives sensor responses in the UAR… |
| 2026-11-25 21:17:16 | [CVE-2026-123879](https://nvd.nist.gov/vuln/detail/CVE-2026-123879) | High | 7.2 | In authd before 0.7.2, an improper access control vulnerability allows an authenticated remote attacker to complete a f… |
| 2026-11-25 21:17:16 | [CVE-2026-131814](https://nvd.nist.gov/vuln/detail/CVE-2026-131814) | High | 7.8 | ChargePoint Home Flex dwnldlogsm tar Command Injection Local Privilege Escalation Vulnerability. This vulnerability all… |
| 2026-11-25 21:17:16 | [CVE-2026-131815](https://nvd.nist.gov/vuln/detail/CVE-2026-131815) | High | 7.8 | ChargePoint Home Flex uploadsm filetype Link Following Local Privilege Escalation Vulnerability. This vulnerability all… |
| 2026-11-25 21:17:16 | [CVE-2026-131816](https://nvd.nist.gov/vuln/detail/CVE-2026-131816) | Medium | 6.3 | ChargePoint Home Flex ssh Hard-coded Credentials Authentication Bypass Vulnerability. This vulnerability allows network… |
| 2026-11-25 21:17:16 | [CVE-2026-131817](https://nvd.nist.gov/vuln/detail/CVE-2026-131817) | High | 8.8 | ChargePoint Home Flex wpa_passphrase Command Injection Remote Code Execution Vulnerability. This vulnerability allows n… |
| 2026-11-25 21:17:16 | [CVE-2026-131818](https://nvd.nist.gov/vuln/detail/CVE-2026-131818) | High | 7.8 | ChargePoint Home Flex busybox Unnecessary Privileges Local Privilege Escalation Vulnerability. This vulnerability allow… |
| 2026-11-25 21:17:17 | [CVE-2026-131819](https://nvd.nist.gov/vuln/detail/CVE-2026-131819) | Medium | 4.3 | ChargePoint Home Flex Debug Interface With Improper Access Control Authentication Bypass Vulnerability. This vulnerabil… |
| 2026-11-25 21:17:17 | [CVE-2026-131827](https://nvd.nist.gov/vuln/detail/CVE-2026-131827) | High | 7.8 | RustDesk Client for Windows reg_recovery Missing Authorization Local Privilege Escalation Vulnerability. This vulnerabi… |
| 2026-11-25 21:17:17 | [CVE-2026-132102](https://nvd.nist.gov/vuln/detail/CVE-2026-132102) | Medium | 5.3 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 14.4 before 19.4.11, 19.5 before 19.5.9, and… |
| 2026-11-25 21:17:17 | [CVE-2026-132794](https://nvd.nist.gov/vuln/detail/CVE-2026-132794) | Medium | 4.3 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 18.10 before 19.4.11, 19.5 before 19.5.9, an… |
| 2026-11-25 21:17:18 | [CVE-2026-133451](https://nvd.nist.gov/vuln/detail/CVE-2026-133451) | Medium | 4.3 | AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agen… |
| 2026-11-25 21:17:19 | [CVE-2026-136821](https://nvd.nist.gov/vuln/detail/CVE-2026-136821) | High | 8.6 | A flaw has been found in D-Link R32 1.10B02. The affected element is the function SetTimeSettings of the component DHMA… |
| 2026-11-25 21:17:19 | [CVE-2026-136822](https://nvd.nist.gov/vuln/detail/CVE-2026-136822) | High | 8.6 | A vulnerability has been found in D-Link R32 1.10B02. The impacted element is the function SetDeviceSettings of the fil… |
| 2026-11-25 21:17:20 | [CVE-2026-67209](https://nvd.nist.gov/vuln/detail/CVE-2026-67209) | High | 7.1 | metasfresh through 5.175 contains a SQL injection vulnerability in the stressTest_massCacheInvalidation handler of Debu… |
| 2026-11-25 21:17:20 | [CVE-2026-67210](https://nvd.nist.gov/vuln/detail/CVE-2026-67210) | Medium | 6.9 | diaspora* through 0.10.1, using the diaspora_federation gem through 1.2.0, contains a server-side request forgery vulne… |
| 2026-11-25 21:17:20 | [CVE-2026-81336](https://nvd.nist.gov/vuln/detail/CVE-2026-81336) | Medium | 6.5 | GitLab has remediated an issue in GitLab CE/EE affecting all versions from 12.8 before 19.4.11, 19.5 before 19.5.9, and… |
| 2026-11-25 21:17:20 | [CVE-2026-90592](https://nvd.nist.gov/vuln/detail/CVE-2026-90592) | Medium | 4.6 | The ITE it51xxx I2C driver, when operating as an I2C target (slave) in buffer mode (CONFIG_I2C_TARGET + CONFIG_I2C_TARG… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
