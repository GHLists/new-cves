# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-11 18:19 UTC

New CVEs published between 2026-10-11 17:20 UTC and 2026-10-11 18:19 UTC.

[Full CSV](data/new-cves-2026-10-11T18-19-34-406043Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-11 18:16:58 | [CVE-2026-18418](https://nvd.nist.gov/vuln/detail/CVE-2026-18418) | Low | 3.4 | The zbus proxy agent IPC backend in subsys/zbus/proxy_agent/zbus_proxy_agent_ipc.c logged the channel name of a rejecte… |
| 2026-10-11 18:16:58 | [CVE-2026-19576](https://nvd.nist.gov/vuln/detail/CVE-2026-19576) | Medium | 6.8 | The Goodix GT9xx input driver in drivers/input/input_gt911.c reads the touch point count from the controller's status r… |
| 2026-10-11 18:16:58 | [CVE-2026-19577](https://nvd.nist.gov/vuln/detail/CVE-2026-19577) | High | 7.1 | net_route_ipv6_packet() in subsys/net/ip/route_ipv6.c resolved the nexthop's link-layer address with net_nbr_get_lladdr… |
| 2026-10-11 18:16:58 | [CVE-2026-19669](https://nvd.nist.gov/vuln/detail/CVE-2026-19669) | High | 7.8 | The user-mode syscall verifiers z_vrfy_fuel_gauge_get_props() and z_vrfy_fuel_gauge_set_props() in drivers/fuel_gauge/f… |
| 2026-10-11 18:16:58 | [CVE-2026-19735](https://nvd.nist.gov/vuln/detail/CVE-2026-19735) | Medium | 4.8 | The RFC 6528 initial-sequence-number implementation in subsys/net/ip/tcp.c derived every TCP ISN from SHA-256(unique_ke… |
| 2026-10-11 18:16:58 | [CVE-2026-19736](https://nvd.nist.gov/vuln/detail/CVE-2026-19736) | High | 7.8 | The NXP MCUX TRNG entropy driver in drivers/entropy/entropy_mcux_trng.c passed the caller's byte count straight to the… |
| 2026-10-11 18:16:58 | [CVE-2026-19737](https://nvd.nist.gov/vuln/detail/CVE-2026-19737) | Medium | 5.5 | i2s_esp32_trigger_check() in drivers/i2s/i2s_esp32.c validates the requested direction only for I2S_DIR_BOTH. The I2S_D… |
| 2026-10-11 18:16:59 | [CVE-2026-19738](https://nvd.nist.gov/vuln/detail/CVE-2026-19738) | Medium | 6.5 | The Bluetooth Link Layer Control Procedure (LLCP) implementation for Connected Isochronous Stream (CIS) creation retain… |
| 2026-10-11 18:16:59 | [CVE-2026-19739](https://nvd.nist.gov/vuln/detail/CVE-2026-19739) | Medium | 6.5 | The Bluetooth Link Layer control procedure code in subsys/bluetooth/controller/ll_sw/ull_llcp_conn_upd.c retains the re… |
| 2026-10-11 18:16:59 | [CVE-2026-19740](https://nvd.nist.gov/vuln/detail/CVE-2026-19740) | Medium | 6.5 | The Link Layer Control Procedure (LLCP) implementation of the Zephyr software Bluetooth LE Controller retains the recei… |
| 2026-10-11 18:16:59 | [CVE-2026-19935](https://nvd.nist.gov/vuln/detail/CVE-2026-19935) | High | 7.5 | The Bluetooth LE host queues received L2CAP connection-oriented channel (CoC) data for deferred processing through a st… |
| 2026-10-11 18:16:59 | [CVE-2026-59508](https://nvd.nist.gov/vuln/detail/CVE-2026-59508) | Medium | 5.9 | Improper neutralization of special elements used in an SQL command ('SQL injection') vulnerability in Interuse i-Bos. T… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
