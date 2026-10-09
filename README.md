# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 08:20 UTC

New CVEs published between 2026-10-09 07:19 UTC and 2026-10-09 08:20 UTC.

[Full CSV](data/new-cves-2026-10-09T08-20-27-12262Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 08:16:54 | [CVE-2025-14123](https://nvd.nist.gov/vuln/detail/CVE-2025-14123) | Medium | 6.8 | The Redux Framework plugin for WordPress is vulnerable to privilege escalation in all versions up to, and including, 4.… |
| 2026-10-09 08:16:54 | [CVE-2026-106145](https://nvd.nist.gov/vuln/detail/CVE-2026-106145) | High | 7.1 | In Progress® Telerik® Report Server prior to version 12.2.26.1007, incorrect privilege assignment in the service-agent… |
| 2026-10-09 08:16:54 | [CVE-2026-106155](https://nvd.nist.gov/vuln/detail/CVE-2026-106155) | High | 8.9 | In Progress® Telerik® Report Server prior to version 12.2.26.1007, a stored cross-site scripting vulnerability in the s… |
| 2026-10-09 08:16:54 | [CVE-2026-19569](https://nvd.nist.gov/vuln/detail/CVE-2026-19569) | High | 8.8 | dynamic_object_create() in kernel/userspace/userspace.c computed the backing allocation for a dynamically allocated ker… |
| 2026-10-09 08:16:54 | [CVE-2026-19570](https://nvd.nist.gov/vuln/detail/CVE-2026-19570) | High | 8.8 | The LE Audio Broadcast Sink in subsys/bluetooth/audio/bap_broadcast_sink.c copies subgroup metadata from a received Bas… |
| 2026-10-09 08:16:54 | [CVE-2026-19571](https://nvd.nist.gov/vuln/detail/CVE-2026-19571) | Medium | 6.7 | The ITE IT8xxx2 SHI host-command backend (subsys/mgmt/ec_host_cmd/backends/ec_host_cmd_backend_shi_ite.c) copied the 8-… |
| 2026-10-09 08:16:54 | [CVE-2026-19574](https://nvd.nist.gov/vuln/detail/CVE-2026-19574) | High | 7.0 | The ARM64 MMU back-end allocated address space identifiers (ASIDs) for memory domains with a bare round-robin counter i… |
| 2026-10-09 08:16:55 | [CVE-2026-19575](https://nvd.nist.gov/vuln/detail/CVE-2026-19575) | High | 7.8 | The user-mode verification handler for the device_deinit() system call, z_vrfy_device_deinit() in kernel/device.c, vali… |
| 2026-10-09 08:16:55 | [CVE-2026-4264](https://nvd.nist.gov/vuln/detail/CVE-2026-4264) | Medium | 5.1 | Reflected Cross-Site Scripting (XSS) on the BeeTienda e-commerce platform, specifically in the latest demo version. The… |
| 2026-10-09 08:16:55 | [CVE-2026-97075](https://nvd.nist.gov/vuln/detail/CVE-2026-97075) | Medium | 6.5 | Missing Authorization vulnerability in WP Media WP Rocket wp-rocket allows Exploiting Incorrectly Configured Access Con… |
| 2026-10-09 08:16:55 | [CVE-2026-98375](https://nvd.nist.gov/vuln/detail/CVE-2026-98375) |  |  | In the Linux kernel, the following vulnerability has been resolved: xen/netfront: drop RX packets with a short Ethernet… |
| 2026-10-09 08:16:55 | [CVE-2026-98376](https://nvd.nist.gov/vuln/detail/CVE-2026-98376) |  |  | In the Linux kernel, the following vulnerability has been resolved: bpf: Use array_map_meta_equal for percpu array inne… |
| 2026-10-09 08:16:56 | [CVE-2026-98377](https://nvd.nist.gov/vuln/detail/CVE-2026-98377) |  |  | In the Linux kernel, the following vulnerability has been resolved: vlan: require the MAC header to be present in __vla… |
| 2026-10-09 08:16:56 | [CVE-2026-98378](https://nvd.nist.gov/vuln/detail/CVE-2026-98378) |  |  | In the Linux kernel, the following vulnerability has been resolved: bpf: Skip unsettled links in link iterator bpf_link… |
| 2026-10-09 08:16:56 | [CVE-2026-98379](https://nvd.nist.gov/vuln/detail/CVE-2026-98379) |  |  | In the Linux kernel, the following vulnerability has been resolved: netfilter: ip6t_rpfilter: reject routes without ine… |
| 2026-10-09 08:16:56 | [CVE-2026-98380](https://nvd.nist.gov/vuln/detail/CVE-2026-98380) |  |  | In the Linux kernel, the following vulnerability has been resolved: net/sched: reject IDR error pointers when deleting… |
| 2026-10-09 08:16:56 | [CVE-2026-98381](https://nvd.nist.gov/vuln/detail/CVE-2026-98381) |  |  | In the Linux kernel, the following vulnerability has been resolved: veth: manage XDP program pointers during channel re… |
| 2026-10-09 08:16:56 | [CVE-2026-98382](https://nvd.nist.gov/vuln/detail/CVE-2026-98382) |  |  | In the Linux kernel, the following vulnerability has been resolved: bpf: Reject dev-bound-only programs on other device… |
| 2026-10-09 08:16:56 | [CVE-2026-98383](https://nvd.nist.gov/vuln/detail/CVE-2026-98383) |  |  | In the Linux kernel, the following vulnerability has been resolved: bpf: Disallow bpf_skb_pull_data() for LWT_SEG6LOCAL… |
| 2026-10-09 08:16:56 | [CVE-2026-98384](https://nvd.nist.gov/vuln/detail/CVE-2026-98384) |  |  | In the Linux kernel, the following vulnerability has been resolved: bpf: Fix out-of-bounds read of sk_protocol in bpf_s… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
