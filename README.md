# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 02:21 UTC

New CVEs published between 2026-11-13 01:19 UTC and 2026-11-13 02:21 UTC.

[Full CSV](data/new-cves-2026-11-13T02-21-18-489547Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 02:18:49 | [CVE-2026-107407](https://nvd.nist.gov/vuln/detail/CVE-2026-107407) | Critical | 9.3 | Memory overflow in SMPP traffic can lead to unpredictable or erroneous behavior or Denial of Service in NetScaler ADC a… |
| 2026-11-13 02:18:49 | [CVE-2026-107408](https://nvd.nist.gov/vuln/detail/CVE-2026-107408) | Critical | 9.3 | Memory corruption in DNS / DNS-over-HTTPS (DoH) can lead to unpredictable or erroneous behavior or Denial of Service in… |
| 2026-11-13 02:18:49 | [CVE-2026-107409](https://nvd.nist.gov/vuln/detail/CVE-2026-107409) | Critical | 9.3 | Memory corruption in DNS-over-HTTPS (DoH) can lead to unpredictable or erroneous behavior or a Denial of Service in Net… |
| 2026-11-13 02:18:49 | [CVE-2026-107410](https://nvd.nist.gov/vuln/detail/CVE-2026-107410) | Critical | 9.3 | Memory overflow in NetScaler Push can lead to unpredictable or erroneous behavior or Denial of Service in NetScaler ADC… |
| 2026-11-13 02:18:54 | [CVE-2026-127276](https://nvd.nist.gov/vuln/detail/CVE-2026-127276) | Low | 2.9 | A vulnerability was identified in Linksys EA8100 1.0.3.216940. Impacted is an unknown function of the component Web UI.… |
| 2026-11-13 02:18:54 | [CVE-2026-127277](https://nvd.nist.gov/vuln/detail/CVE-2026-127277) | Critical | 9.3 | A security flaw has been discovered in Linksys EA8100 1.0.3.216940. The affected element is an unknown function of the… |
| 2026-11-13 02:18:54 | [CVE-2026-127278](https://nvd.nist.gov/vuln/detail/CVE-2026-127278) | Medium | 5.5 | A weakness has been identified in AIP-PUB ACPs-community up to 2.2.0. The impacted element is the function send_verific… |
| 2026-11-13 02:18:54 | [CVE-2026-127279](https://nvd.nist.gov/vuln/detail/CVE-2026-127279) | Medium | 5.5 | A vulnerability was detected in AIP-PUB ACPs-community up to 2.2.0. This impacts an unknown function of the file discov… |
| 2026-11-13 02:18:55 | [CVE-2026-127281](https://nvd.nist.gov/vuln/detail/CVE-2026-127281) | Medium | 5.5 | A vulnerability was found in lanyulei ferry 1.0.0-beta.1/1.0.0. Affected is an unknown function of the file middleware/… |
| 2026-11-13 02:18:55 | [CVE-2026-127282](https://nvd.nist.gov/vuln/detail/CVE-2026-127282) | Low | 2.1 | A vulnerability was determined in SourceCodester Smart Attendance System with QR Code Scanner 1.0. Affected by this vul… |
| 2026-11-13 02:18:55 | [CVE-2026-127283](https://nvd.nist.gov/vuln/detail/CVE-2026-127283) | Medium | 5.5 | A vulnerability was identified in SourceCodester Food Ordering System 1.0. Affected by this issue is some unknown funct… |
| 2026-11-13 02:18:55 | [CVE-2026-127284](https://nvd.nist.gov/vuln/detail/CVE-2026-127284) | Medium | 5.5 | A security flaw has been discovered in SourceCodester Food Ordering System 1.0. This affects an unknown part of the fil… |
| 2026-11-13 02:18:55 | [CVE-2026-127915](https://nvd.nist.gov/vuln/detail/CVE-2026-127915) | Low | 2.0 | The MCUboot TLV iterator bootutil_tlv_iter_next() in boot/bootutil/src/tlv.c walks image trailer TLVs with a single loo… |
| 2026-11-13 02:18:55 | [CVE-2026-127916](https://nvd.nist.gov/vuln/detail/CVE-2026-127916) | Low | 2.9 | bootutil_img_hash() computes the image digest over ih_hdr_size + ih_img_size + ih_protect_tlv_size bytes, all three tak… |
| 2026-11-13 02:18:56 | [CVE-2026-127928](https://nvd.nist.gov/vuln/detail/CVE-2026-127928) | Low | 2.0 | In MCUboot's serial-recovery encrypted-image support (boot/boot_serial/src/boot_serial_encryption.c), decrypt_image_inp… |
| 2026-11-13 02:18:56 | [CVE-2026-128091](https://nvd.nist.gov/vuln/detail/CVE-2026-128091) | Low | 2.0 | When MCUboot is built with the TinyCrypt crypto backend (MCUBOOT_USE_TINYCRYPT), bootutil_aes_ctr_drop() in boot/bootut… |
| 2026-11-13 02:18:56 | [CVE-2026-128321](https://nvd.nist.gov/vuln/detail/CVE-2026-128321) |  |  | Tight JPEG decoding in TightVNC and UltraVNC viewers contains a heap-based buffer overflow because an attacker-controll… |
| 2026-11-13 02:18:56 | [CVE-2026-15465](https://nvd.nist.gov/vuln/detail/CVE-2026-15465) |  |  | Software installed and run as a non-privileged user may conduct improper GPU system calls through the DDK kernel module… |
| 2026-11-13 02:18:56 | [CVE-2026-16659](https://nvd.nist.gov/vuln/detail/CVE-2026-16659) | Medium | 4.0 | MCUboot's serial-recovery image-upload handler bs_upload() in boot/boot_serial/src/boot_serial.c declares const struct… |
| 2026-11-13 02:18:57 | [CVE-2026-16662](https://nvd.nist.gov/vuln/detail/CVE-2026-16662) | Low | 2.4 | boot_save_boot_status() in boot/bootutil/src/boot_record.c reads the image's EXPECTED_HASH_TLV into a stack buffer imag… |
| 2026-11-13 02:18:57 | [CVE-2026-16664](https://nvd.nist.gov/vuln/detail/CVE-2026-16664) | Medium | 5.1 | MCUboot's Zephyr serial-recovery upload handler bs_upload() in boot/boot_serial/src/boot_serial.c decodes the host-supp… |
| 2026-11-13 02:18:57 | [CVE-2026-16671](https://nvd.nist.gov/vuln/detail/CVE-2026-16671) | Low | 2.9 | split_image_check() in boot/bootutil/src/loader.c declares a fixed uint8_t loader_hash[32] buffer and passes it as the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
