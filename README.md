# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-23 20:18 UTC

New CVEs published between 2026-10-23 19:18 UTC and 2026-10-23 20:18 UTC.

[Full CSV](data/new-cves-2026-10-23T20-18-57-7319Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-23 20:17:20 | [CVE-2026-115572](https://nvd.nist.gov/vuln/detail/CVE-2026-115572) | High | 7.1 | pypdf is a free and open-source pure-python PDF library. Prior to 6.21.2, an attacker can craft a PDF that repeatedly r… |
| 2026-10-23 20:17:21 | [CVE-2026-115580](https://nvd.nist.gov/vuln/detail/CVE-2026-115580) | High | 7.1 | pypdf is a free and open-source pure-python PDF library. Prior to 6.21.2, an attacker can craft a PDF with a standard c… |
| 2026-10-23 20:17:21 | [CVE-2026-115585](https://nvd.nist.gov/vuln/detail/CVE-2026-115585) | High | 7.1 | pypdf is a free and open-source pure-python PDF library. Prior to 6.21.2, an incomplete remediation for repeated malfor… |
| 2026-10-23 20:17:21 | [CVE-2026-115586](https://nvd.nist.gov/vuln/detail/CVE-2026-115586) | High | 7.1 | virtualenv is a tool for creating isolated virtual python environments. From 21.14.9 until 21.14.13, the bash bin/activ… |
| 2026-10-23 20:17:21 | [CVE-2026-115796](https://nvd.nist.gov/vuln/detail/CVE-2026-115796) | Low | 2.1 | A security flaw has been discovered in Tenda F6 12.02.01.73. This impacts an unknown function of the component Web Mana… |
| 2026-10-23 20:17:21 | [CVE-2026-115797](https://nvd.nist.gov/vuln/detail/CVE-2026-115797) | Low | 2.9 | A weakness has been identified in Tenda F6 12.02.01.73. Affected is an unknown function of the component Web Management… |
| 2026-10-23 20:17:21 | [CVE-2026-19741](https://nvd.nist.gov/vuln/detail/CVE-2026-19741) | High | 7.5 | Zephyr's OpenThread integration defined CONFIG_OPENTHREAD_JOINER_PSKD with default "J01NME" in modules/openthread/Kconf… |
| 2026-10-23 20:17:27 | [CVE-2026-79977](https://nvd.nist.gov/vuln/detail/CVE-2026-79977) | High | 8.2 | The WireGuard VPN service in subsys/net/lib/wireguard/wg.c updated the peer endpoint from a message it could not authen… |
| 2026-10-23 20:17:27 | [CVE-2026-79978](https://nvd.nist.gov/vuln/detail/CVE-2026-79978) | Low | 3.6 | The RTIO streaming completion callback adxl345_process_fifo_samples_cb() in drivers/sensor/adi/adxl345/adxl345_stream.c… |
| 2026-10-23 20:17:27 | [CVE-2026-79979](https://nvd.nist.gov/vuln/detail/CVE-2026-79979) | High | 7.8 | The arm64 MMU backend invalidates a single virtual address from the TLB with invalidate_tlb_page() in arch/arm64/core/m… |
| 2026-10-23 20:17:27 | [CVE-2026-79980](https://nvd.nist.gov/vuln/detail/CVE-2026-79980) | Medium | 5.6 | The DHCPv4 client in subsys/net/lib/dhcpv4/dhcpv4.c maintained its transaction identifier (iface->config.dhcpv4.xid) as… |
| 2026-10-23 20:17:28 | [CVE-2026-79981](https://nvd.nist.gov/vuln/detail/CVE-2026-79981) | Medium | 6.5 | The DNS stub resolver in subsys/net/lib/dns/resolve.c binds one UDP socket per configured server when the resolver cont… |
| 2026-10-23 20:17:28 | [CVE-2026-79982](https://nvd.nist.gov/vuln/detail/CVE-2026-79982) | High | 8.8 | The Bluetooth HCI USB transport class of the new USB device stack, subsys/usb/device_next/class/bt_hci.c, copies every… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
