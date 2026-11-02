# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 16:19 UTC

New CVEs published between 2026-11-02 15:19 UTC and 2026-11-02 16:19 UTC.

[Full CSV](data/new-cves-2026-11-02T16-19-26-45928Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 16:17:22 | [CVE-2026-104080](https://nvd.nist.gov/vuln/detail/CVE-2026-104080) | High | 8.6 | Control Web Panel (CWP) before webpanel_version 1.30 contains an OS command injection vulnerability in the loopback API… |
| 2026-11-02 16:17:26 | [CVE-2026-109140](https://nvd.nist.gov/vuln/detail/CVE-2026-109140) | High | 8.4 | The vulnerability is that Krill encrypts every login-session token with a nonce built from a counter that is reset to 0… |
| 2026-11-02 16:17:27 | [CVE-2026-109141](https://nvd.nist.gov/vuln/detail/CVE-2026-109141) | High | 8.4 | The vulnerability gives a role that is restricted to a list of CAs (cas = [...]) its full permission set for every requ… |
| 2026-11-02 16:17:27 | [CVE-2026-109142](https://nvd.nist.gov/vuln/detail/CVE-2026-109142) | High | 8.4 | When a CA's parent lives on the same Krill server: instead of building and verifying a signed CMS message, it runs the… |
| 2026-11-02 16:17:27 | [CVE-2026-114408](https://nvd.nist.gov/vuln/detail/CVE-2026-114408) | High | 8.7 | In Eclipse ThreadX NetX Duo versions 6.4.5.202504 through 6.5.2.202603a, built with IPv6 path MTU discovery, the ICMPv6… |
| 2026-11-02 16:17:28 | [CVE-2026-115653](https://nvd.nist.gov/vuln/detail/CVE-2026-115653) | High | 7.0 | In Eclipse ThreadX versions 6.0.1 through 6.5.2.202603, the PendSV handler of the Cortex-M module ports saves a preempt… |
| 2026-11-02 16:17:28 | [CVE-2026-115654](https://nvd.nist.gov/vuln/detail/CVE-2026-115654) | Medium | 6.9 | In Eclipse ThreadX versions 6.0.1 through 6.5.2.202603, the Module Manager's thread-control services do not check that… |
| 2026-11-02 16:17:34 | [CVE-2026-120500](https://nvd.nist.gov/vuln/detail/CVE-2026-120500) | Medium | 5.3 | An Otter Wiki before 2.26.2 contains a stored cross-site scripting vulnerability in OtterwikiMdRenderer.block_code that… |
| 2026-11-02 16:17:34 | [CVE-2026-120501](https://nvd.nist.gov/vuln/detail/CVE-2026-120501) | Medium | 6.9 | An Otter Wiki 2.20.1 before 2.26.2 contains a file disclosure vulnerability in the DataTable embedding that allows atta… |
| 2026-11-02 16:17:34 | [CVE-2026-16306](https://nvd.nist.gov/vuln/detail/CVE-2026-16306) |  |  | Remote Code Execution in the `IModular.exe` URI handler in INFINITT Healthcare Co., Ltd. INFINITT PACS allows a remote… |
| 2026-11-02 16:17:40 | [CVE-2026-2102](https://nvd.nist.gov/vuln/detail/CVE-2026-2102) | Medium | 6.1 | wrensec-commons contains a reflected cross-site scripting (XSS) vulnerability in the CREST framework's HTTP binding. Th… |
| 2026-11-02 16:17:43 | [CVE-2026-77876](https://nvd.nist.gov/vuln/detail/CVE-2026-77876) | Critical | 9.3 | Control Web Panel (CWP) before webpanel_version 1.16 contains an OS command injection vulnerability in the protected_di… |
| 2026-11-02 16:17:43 | [CVE-2026-77877](https://nvd.nist.gov/vuln/detail/CVE-2026-77877) | High | 8.6 | Control Web Panel (CWP) before webpanel_version 1.30 contains a missing authentication vulnerability that allows attack… |
| 2026-11-02 16:17:43 | [CVE-2026-77878](https://nvd.nist.gov/vuln/detail/CVE-2026-77878) | High | 8.6 | Control Web Panel (CWP) before webpanel_version 1.30 contains an OS command injection vulnerability in the loopback API… |
| 2026-11-02 16:17:43 | [CVE-2026-77879](https://nvd.nist.gov/vuln/detail/CVE-2026-77879) | High | 8.5 | Control Web Panel (CWP) before webpanel_version 1.16 contains a SQL injection vulnerability in the loopback API authent… |
| 2026-11-02 16:17:43 | [CVE-2026-77880](https://nvd.nist.gov/vuln/detail/CVE-2026-77880) | High | 8.6 | Control Web Panel (CWP) before webpanel_version 1.16 contains an OS command injection vulnerability in the loopback API… |
| 2026-11-02 16:17:44 | [CVE-2026-77881](https://nvd.nist.gov/vuln/detail/CVE-2026-77881) | Medium | 6.9 | Control Web Panel (CWP) before webpanel_version 1.30 contains a blind SQL injection vulnerability in an unauthenticated… |
| 2026-11-02 16:17:44 | [CVE-2026-88809](https://nvd.nist.gov/vuln/detail/CVE-2026-88809) | High | 7.6 | A security vulnerability exists in the SUSE Rancher Manager meta proxy endpoint (/meta/proxy). This endpoint is intende… |
| 2026-11-02 16:17:45 | [CVE-2026-94290](https://nvd.nist.gov/vuln/detail/CVE-2026-94290) | Critical | 9.1 | SUSE Rancher Fleet clusters reference a kubeconfig secret that the controller uses to install and manage a Fleet agent… |
| 2026-11-02 16:17:45 | [CVE-2026-99217](https://nvd.nist.gov/vuln/detail/CVE-2026-99217) |  |  | In the Linux kernel, the following vulnerability has been resolved: fork: release the files of a failed fork after sche… |
| 2026-11-02 16:17:45 | [CVE-2026-99218](https://nvd.nist.gov/vuln/detail/CVE-2026-99218) | High | 7.0 | In the Linux kernel, the following vulnerability has been resolved: coredump: hold RCU while releasing parked threads c… |
| 2026-11-02 16:17:45 | [CVE-2026-99219](https://nvd.nist.gov/vuln/detail/CVE-2026-99219) |  |  | In the Linux kernel, the following vulnerability has been resolved: ftrace: Initialize modname and offset in print_rec(… |
| 2026-11-02 16:17:46 | [CVE-2026-99220](https://nvd.nist.gov/vuln/detail/CVE-2026-99220) |  |  | In the Linux kernel, the following vulnerability has been resolved: asymmetric_keys: reject trust keys without IDs The… |
| 2026-11-02 16:17:46 | [CVE-2026-99221](https://nvd.nist.gov/vuln/detail/CVE-2026-99221) |  |  | In the Linux kernel, the following vulnerability has been resolved: keys/trusted_keys: return immediately after TPM uns… |
| 2026-11-02 16:17:46 | [CVE-2026-99222](https://nvd.nist.gov/vuln/detail/CVE-2026-99222) |  |  | In the Linux kernel, the following vulnerability has been resolved: keys: Protect the read method check against type re… |
| 2026-11-02 16:17:46 | [CVE-2026-99223](https://nvd.nist.gov/vuln/detail/CVE-2026-99223) |  |  | In the Linux kernel, the following vulnerability has been resolved: keys: make keyring indexes independent of kernel ad… |
| 2026-11-02 16:17:46 | [CVE-2026-99224](https://nvd.nist.gov/vuln/detail/CVE-2026-99224) | High | 7.0 | In the Linux kernel, the following vulnerability has been resolved: keys: Protect the type name while describing a key… |
| 2026-11-02 16:17:47 | [CVE-2026-99225](https://nvd.nist.gov/vuln/detail/CVE-2026-99225) |  |  | In the Linux kernel, the following vulnerability has been resolved: keys: Check the authorization payload in process ke… |
| 2026-11-02 16:17:47 | [CVE-2026-99226](https://nvd.nist.gov/vuln/detail/CVE-2026-99226) |  |  | In the Linux kernel, the following vulnerability has been resolved: keys: Avoid the owner account dereference in named… |
| 2026-11-02 16:17:47 | [CVE-2026-99227](https://nvd.nist.gov/vuln/detail/CVE-2026-99227) | High | 7.8 | In the Linux kernel, the following vulnerability has been resolved: io_uring/waitid: prevent cancel reference wrap io_w… |
| 2026-11-02 16:17:47 | [CVE-2026-99228](https://nvd.nist.gov/vuln/detail/CVE-2026-99228) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/io-wq: don't lose the signal that ends wor… |
| 2026-11-02 16:17:47 | [CVE-2026-99229](https://nvd.nist.gov/vuln/detail/CVE-2026-99229) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/wait: don't spin on a stuck overflow list… |
| 2026-11-02 16:17:47 | [CVE-2026-99230](https://nvd.nist.gov/vuln/detail/CVE-2026-99230) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/cmd: don't leave list poison in ->hash_nod… |
| 2026-11-02 16:17:48 | [CVE-2026-99231](https://nvd.nist.gov/vuln/detail/CVE-2026-99231) | High | 7.8 | In the Linux kernel, the following vulnerability has been resolved: io_uring/waitid: own the request before clearing ->… |
| 2026-11-02 16:17:48 | [CVE-2026-99232](https://nvd.nist.gov/vuln/detail/CVE-2026-99232) |  |  | In the Linux kernel, the following vulnerability has been resolved: tracing/syscalls: Use copy_from_user for the faulta… |
| 2026-11-02 16:17:48 | [CVE-2026-99233](https://nvd.nist.gov/vuln/detail/CVE-2026-99233) | High | 7.8 | In the Linux kernel, the following vulnerability has been resolved: tracing/histograms: Verify event_call identity when… |
| 2026-11-02 16:17:48 | [CVE-2026-99234](https://nvd.nist.gov/vuln/detail/CVE-2026-99234) |  |  | In the Linux kernel, the following vulnerability has been resolved: tracing: Unregister field variable histograms when… |
| 2026-11-02 16:17:48 | [CVE-2026-99235](https://nvd.nist.gov/vuln/detail/CVE-2026-99235) | High | 7.8 | In the Linux kernel, the following vulnerability has been resolved: tracing: Save the event file instead of the compati… |
| 2026-11-02 16:17:49 | [CVE-2026-99236](https://nvd.nist.gov/vuln/detail/CVE-2026-99236) | High | 7.8 | In the Linux kernel, the following vulnerability has been resolved: tracing: Reject incomplete event filter expressions… |
| 2026-11-02 16:17:49 | [CVE-2026-99237](https://nvd.nist.gov/vuln/detail/CVE-2026-99237) | High | 7.8 | In the Linux kernel, the following vulnerability has been resolved: tracing: Hold trace_types_lock when resetting last… |
| 2026-11-02 16:17:49 | [CVE-2026-99238](https://nvd.nist.gov/vuln/detail/CVE-2026-99238) | High | 7.8 | In the Linux kernel, the following vulnerability has been resolved: tracing: Hold trace_types_lock when updating module… |
| 2026-11-02 16:17:49 | [CVE-2026-99239](https://nvd.nist.gov/vuln/detail/CVE-2026-99239) | High | 7.8 | In the Linux kernel, the following vulnerability has been resolved: Bluetooth: L2CAP: refuse __l2cap_chan_add if chan a… |
| 2026-11-02 16:17:49 | [CVE-2026-99240](https://nvd.nist.gov/vuln/detail/CVE-2026-99240) |  |  | In the Linux kernel, the following vulnerability has been resolved: mm/damon/core: error damos_commit_quota_goal() for… |
| 2026-11-02 16:17:49 | [CVE-2026-99241](https://nvd.nist.gov/vuln/detail/CVE-2026-99241) |  |  | In the Linux kernel, the following vulnerability has been resolved: ntfs: take invalidate_lock in ntfs_filemap_page_mkw… |
| 2026-11-02 16:17:50 | [CVE-2026-99242](https://nvd.nist.gov/vuln/detail/CVE-2026-99242) |  |  | In the Linux kernel, the following vulnerability has been resolved: ntfs: fix race between fallocate and mmap reads The… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
