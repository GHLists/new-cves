# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 19:22 UTC

New CVEs published between 2026-11-23 18:22 UTC and 2026-11-23 19:22 UTC.

[Full CSV](data/new-cves-2026-11-23T19-22-08-360664Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 19:17:27 | [CVE-2026-100374](https://nvd.nist.gov/vuln/detail/CVE-2026-100374) | High | 7.8 | The system call verification handlers for smbus_block_read() and smbus_block_pcall() in drivers/smbus/smbus_handlers.c… |
| 2026-11-23 19:17:27 | [CVE-2026-102948](https://nvd.nist.gov/vuln/detail/CVE-2026-102948) | Medium | 5.3 | Several Bluetooth LE Audio services in subsys/bluetooth/audio register global connection and authentication callbacks b… |
| 2026-11-23 19:17:27 | [CVE-2026-102949](https://nvd.nist.gov/vuln/detail/CVE-2026-102949) | Medium | 6.4 | The Intel SEDI I2C controller driver (drivers/i2c/i2c_sedi.c, used on Intel ISH platforms) waits for each asynchronous… |
| 2026-11-23 19:17:28 | [CVE-2026-102950](https://nvd.nist.gov/vuln/detail/CVE-2026-102950) | Medium | 5.9 | The mount-time recovery scan of the Zephyr Memory Storage (ZMS) key-value store, zms_recover_last_ate() in subsys/kvss/… |
| 2026-11-23 19:17:28 | [CVE-2026-102951](https://nvd.nist.gov/vuln/detail/CVE-2026-102951) | Medium | 6.6 | The Intel SoC FPGA Agilex5 SoC's static MMU region table in soc/intel/intel_socfpga/agilex5/mmu_regions.c mapped the Sy… |
| 2026-11-23 19:17:28 | [CVE-2026-102952](https://nvd.nist.gov/vuln/detail/CVE-2026-102952) | Medium | 4.8 | The Zephyr TFTP client in subsys/net/lib/tftp/tftp_client.c does not check where the reply to its request comes from. A… |
| 2026-11-23 19:17:28 | [CVE-2026-102953](https://nvd.nist.gov/vuln/detail/CVE-2026-102953) | Medium | 6.0 | usbh_req_setup() in subsys/usb/host/usbh_ch9.c returns -ETIMEDOUT as soon as a control request times out, even though t… |
| 2026-11-23 19:17:28 | [CVE-2026-102954](https://nvd.nist.gov/vuln/detail/CVE-2026-102954) | Medium | 6.8 | The STM32 SMBus driver (drivers/smbus/smbus_stm32.c) implements smbus_block_read() and smbus_block_pcall() by issuing a… |
| 2026-11-23 19:17:28 | [CVE-2026-102955](https://nvd.nist.gov/vuln/detail/CVE-2026-102955) | Low | 3.1 | The OpenThread PSA crypto platform backend in modules/openthread/platform/crypto_psa.c only supported PSA key reference… |
| 2026-11-23 19:17:28 | [CVE-2026-102956](https://nvd.nist.gov/vuln/detail/CVE-2026-102956) | Low | 3.1 | ethernet_send() in subsys/net/l2/ethernet/ethernet.c dropped the caller's reference on an IPv4 packet whenever net_arp_… |
| 2026-11-23 19:17:34 | [CVE-2026-135088](https://nvd.nist.gov/vuln/detail/CVE-2026-135088) | Low | 2.0 | A vulnerability has been found in ONLYOFFICE onlyoffice-humhub up to 4.0.0. This impacts the function html of the file… |
| 2026-11-23 19:17:35 | [CVE-2026-135089](https://nvd.nist.gov/vuln/detail/CVE-2026-135089) | Low | 2.0 | A vulnerability was found in humhub questions up to 1.1.5. Affected is an unknown function of the file widgets/views/an… |
| 2026-11-23 19:17:35 | [CVE-2026-135090](https://nvd.nist.gov/vuln/detail/CVE-2026-135090) | Low | 2.0 | A vulnerability was determined in humhub lets-meet up to 1.2.1. Affected by this vulnerability is the function NewInvit… |
| 2026-11-23 19:17:35 | [CVE-2026-135091](https://nvd.nist.gov/vuln/detail/CVE-2026-135091) | Low | 1.9 | A security flaw has been discovered in humhub rest up to 0.12.6. This affects an unknown part of the file views/admin/b… |
| 2026-11-23 19:17:36 | [CVE-2026-135452](https://nvd.nist.gov/vuln/detail/CVE-2026-135452) | High | 8.4 | A potential security vulnerability has been identified in the HP Hotkey UWP Service, which might allow escalation of pr… |
| 2026-11-23 19:17:37 | [CVE-2026-49960](https://nvd.nist.gov/vuln/detail/CVE-2026-49960) | High | 7.1 | DreameHome cloud API before 2026-10-14 contained an insecure direct object reference vulnerability in the POST /smart-a… |
| 2026-11-23 19:17:38 | [CVE-2026-49961](https://nvd.nist.gov/vuln/detail/CVE-2026-49961) | High | 7.1 | DreameHome MQTT broker before 2026-10-26 contained an incorrect authorization vulnerability that allows authenticated a… |
| 2026-11-23 19:17:38 | [CVE-2026-49962](https://nvd.nist.gov/vuln/detail/CVE-2026-49962) | High | 7.1 | DreameHome device sharing and MQTT broker before 2026-10-26 contained an incorrect authorization vulnerability that all… |
| 2026-11-23 19:17:38 | [CVE-2026-49963](https://nvd.nist.gov/vuln/detail/CVE-2026-49963) | High | 7.6 | DreameHome for Android (com.dreame.smartlife) before 2.6.4.0 contains a download of code without integrity check vulner… |
| 2026-11-23 19:17:38 | [CVE-2026-49964](https://nvd.nist.gov/vuln/detail/CVE-2026-49964) | High | 7.1 | DreameHome cloud API before 2026-10-14 contained an insecure direct object reference vulnerability in the POST /dreame-… |
| 2026-11-23 19:17:38 | [CVE-2026-49965](https://nvd.nist.gov/vuln/detail/CVE-2026-49965) | High | 7.1 | DreameHome cloud API before 2026-11-19 contained an insecure direct object reference vulnerability in the POST /smart-a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
