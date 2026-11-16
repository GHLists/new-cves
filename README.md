# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 10:18 UTC

New CVEs published between 2026-11-16 09:22 UTC and 2026-11-16 10:18 UTC.

[Full CSV](data/new-cves-2026-11-16T10-18-21-783762Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 10:16:45 | [CVE-2026-102448](https://nvd.nist.gov/vuln/detail/CVE-2026-102448) | High | 7.8 | A vulnerability has been identified in Rexroth IndraWorks. This flaw allows an attacker to execute arbitrary code on th… |
| 2026-11-16 10:16:45 | [CVE-2026-115690](https://nvd.nist.gov/vuln/detail/CVE-2026-115690) |  |  | Apache WSS4J remembers the UsernameToken Nonce, the Timestamp and signature of a signed message, and the ID of a SAML 2… |
| 2026-11-16 10:16:46 | [CVE-2026-128841](https://nvd.nist.gov/vuln/detail/CVE-2026-128841) |  |  | ** UNSUPPORTED WHEN ASSIGNED ** Missing authentication for critical function vulnerability in Apache Griffin Web Servic… |
| 2026-11-16 10:17:00 | [CVE-2026-99289](https://nvd.nist.gov/vuln/detail/CVE-2026-99289) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: fix app-instance non-durable supersede sessi… |
| 2026-11-16 10:17:01 | [CVE-2026-99290](https://nvd.nist.gov/vuln/detail/CVE-2026-99290) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: fix use-after-free after a failed durable re… |
| 2026-11-16 10:17:01 | [CVE-2026-99291](https://nvd.nist.gov/vuln/detail/CVE-2026-99291) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: fix SMB2 CREATE response buffer overflow smb… |
| 2026-11-16 10:17:01 | [CVE-2026-99292](https://nvd.nist.gov/vuln/detail/CVE-2026-99292) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: fix slab-out-of-bounds write in id_mod… |
| 2026-11-16 10:17:01 | [CVE-2026-99293](https://nvd.nist.gov/vuln/detail/CVE-2026-99293) |  |  | In the Linux kernel, the following vulnerability has been resolved: fuse: don't BUG when the copy buffer is exhausted f… |
| 2026-11-16 10:17:02 | [CVE-2026-99294](https://nvd.nist.gov/vuln/detail/CVE-2026-99294) |  |  | In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_fwd_netdev: use recursion counter in… |
| 2026-11-16 10:17:02 | [CVE-2026-99295](https://nvd.nist.gov/vuln/detail/CVE-2026-99295) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: stop processing a read response after… |
| 2026-11-16 10:17:02 | [CVE-2026-99296](https://nvd.nist.gov/vuln/detail/CVE-2026-99296) |  |  | In the Linux kernel, the following vulnerability has been resolved: libceph: bound mon_command ack decode to front len… |
| 2026-11-16 10:17:02 | [CVE-2026-99297](https://nvd.nist.gov/vuln/detail/CVE-2026-99297) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: em28xx: fix double free in em28xx_alloc_urbs… |
| 2026-11-16 10:17:03 | [CVE-2026-99298](https://nvd.nist.gov/vuln/detail/CVE-2026-99298) |  |  | In the Linux kernel, the following vulnerability has been resolved: net: ipv4: add zero check for snd_cwnd_clamp When R… |
| 2026-11-16 10:17:03 | [CVE-2026-99299](https://nvd.nist.gov/vuln/detail/CVE-2026-99299) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: em28xx: reject audio endpoint with zero pack… |
| 2026-11-16 10:17:03 | [CVE-2026-99300](https://nvd.nist.gov/vuln/detail/CVE-2026-99300) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: go7007: only set audio_enabled if go7007_snd… |
| 2026-11-16 10:17:03 | [CVE-2026-99301](https://nvd.nist.gov/vuln/detail/CVE-2026-99301) |  |  | In the Linux kernel, the following vulnerability has been resolved: virtio_net: atomically disable rx mode work virtio-… |
| 2026-11-16 10:17:04 | [CVE-2026-99302](https://nvd.nist.gov/vuln/detail/CVE-2026-99302) |  |  | In the Linux kernel, the following vulnerability has been resolved: nvmet-rdma: reject short connection requests nvmet_… |
| 2026-11-16 10:17:04 | [CVE-2026-99303](https://nvd.nist.gov/vuln/detail/CVE-2026-99303) |  |  | In the Linux kernel, the following vulnerability has been resolved: speakup: Fix NULL pointer dereference on VT switch… |
| 2026-11-16 10:17:04 | [CVE-2026-99304](https://nvd.nist.gov/vuln/detail/CVE-2026-99304) |  |  | In the Linux kernel, the following vulnerability has been resolved: ceph: fix integer overflow in the snap trace bounds… |
| 2026-11-16 10:17:05 | [CVE-2026-99305](https://nvd.nist.gov/vuln/detail/CVE-2026-99305) |  |  | In the Linux kernel, the following vulnerability has been resolved: fbdev: udlfb: don't rebuild the mode list while the… |
| 2026-11-16 10:17:05 | [CVE-2026-99306](https://nvd.nist.gov/vuln/detail/CVE-2026-99306) |  |  | In the Linux kernel, the following vulnerability has been resolved: ceph: reject mdsmaps that claim more than CEPH_MAX_… |
| 2026-11-16 10:17:05 | [CVE-2026-99307](https://nvd.nist.gov/vuln/detail/CVE-2026-99307) |  |  | In the Linux kernel, the following vulnerability has been resolved: ceph: require the dentry lease record to cover stru… |
| 2026-11-16 10:17:05 | [CVE-2026-99308](https://nvd.nist.gov/vuln/detail/CVE-2026-99308) |  |  | In the Linux kernel, the following vulnerability has been resolved: usb: xhci: Fix bounce buffer overflow High-speed de… |
| 2026-11-16 10:17:06 | [CVE-2026-99309](https://nvd.nist.gov/vuln/detail/CVE-2026-99309) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: fix overflow in dacloffset bounds check in b… |
| 2026-11-16 10:17:06 | [CVE-2026-99310](https://nvd.nist.gov/vuln/detail/CVE-2026-99310) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: hold cl_lock in client_has_openowners() clien… |
| 2026-11-16 10:17:06 | [CVE-2026-99311](https://nvd.nist.gov/vuln/detail/CVE-2026-99311) |  |  | In the Linux kernel, the following vulnerability has been resolved: udf: fix return value for non-recorded-allocated ex… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
