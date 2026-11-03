# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 12:19 UTC

New CVEs published between 2026-11-03 11:18 UTC and 2026-11-03 12:19 UTC.

[Full CSV](data/new-cves-2026-11-03T12-19-36-797213Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 12:17:30 | [CVE-2026-99243](https://nvd.nist.gov/vuln/detail/CVE-2026-99243) |  |  | In the Linux kernel, the following vulnerability has been resolved: io-wq: order the exit bit against worker creation t… |
| 2026-11-03 12:17:30 | [CVE-2026-99244](https://nvd.nist.gov/vuln/detail/CVE-2026-99244) |  |  | In the Linux kernel, the following vulnerability has been resolved: pid_namespace: prevent TIF_NOTIFY_SIGNAL from inter… |
| 2026-11-03 12:17:30 | [CVE-2026-99245](https://nvd.nist.gov/vuln/detail/CVE-2026-99245) |  |  | In the Linux kernel, the following vulnerability has been resolved: KEYS: Fix key_reject_and_link() race with keyring r… |
| 2026-11-03 12:17:31 | [CVE-2026-99246](https://nvd.nist.gov/vuln/detail/CVE-2026-99246) |  |  | In the Linux kernel, the following vulnerability has been resolved: tipc: protect node reset trace dump with node lock… |
| 2026-11-03 12:17:31 | [CVE-2026-99247](https://nvd.nist.gov/vuln/detail/CVE-2026-99247) |  |  | In the Linux kernel, the following vulnerability has been resolved: tracing: Do not initialize tracefs work if tracing… |
| 2026-11-03 12:17:31 | [CVE-2026-99248](https://nvd.nist.gov/vuln/detail/CVE-2026-99248) |  |  | In the Linux kernel, the following vulnerability has been resolved: i2c: xiic: restore non-managed runtime PM to fix cl… |
| 2026-11-03 12:17:31 | [CVE-2026-99249](https://nvd.nist.gov/vuln/detail/CVE-2026-99249) |  |  | In the Linux kernel, the following vulnerability has been resolved: pid_namespace: make zap_pid_ns_processes() freezabl… |
| 2026-11-03 12:17:31 | [CVE-2026-99250](https://nvd.nist.gov/vuln/detail/CVE-2026-99250) |  |  | In the Linux kernel, the following vulnerability has been resolved: printk: Postpone kthread startup There have been va… |
| 2026-11-03 12:17:31 | [CVE-2026-99251](https://nvd.nist.gov/vuln/detail/CVE-2026-99251) |  |  | In the Linux kernel, the following vulnerability has been resolved: Drivers: hv: Avoid infinite retry loop in init_vp_i… |
| 2026-11-03 12:17:31 | [CVE-2026-99252](https://nvd.nist.gov/vuln/detail/CVE-2026-99252) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/mpscq: disable preemption while pushing A… |
| 2026-11-03 12:17:32 | [CVE-2026-99253](https://nvd.nist.gov/vuln/detail/CVE-2026-99253) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/cancel: rearm local work wake up before sl… |
| 2026-11-03 12:17:32 | [CVE-2026-99254](https://nvd.nist.gov/vuln/detail/CVE-2026-99254) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring: don't flood a cancelling task with task_w… |
| 2026-11-03 12:17:32 | [CVE-2026-99255](https://nvd.nist.gov/vuln/detail/CVE-2026-99255) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/io-wq: don't hide a link from cancellation… |
| 2026-11-03 12:17:32 | [CVE-2026-99256](https://nvd.nist.gov/vuln/detail/CVE-2026-99256) |  |  | In the Linux kernel, the following vulnerability has been resolved: dm cache: fix issue with background work locking dm… |
| 2026-11-03 12:17:32 | [CVE-2026-99257](https://nvd.nist.gov/vuln/detail/CVE-2026-99257) |  |  | In the Linux kernel, the following vulnerability has been resolved: gpio: shared: gracefully handle no-device lookup of… |
| 2026-11-03 12:17:32 | [CVE-2026-99258](https://nvd.nist.gov/vuln/detail/CVE-2026-99258) |  |  | In the Linux kernel, the following vulnerability has been resolved: x86/hyperv: Avoid using per-cpu output page in hv_a… |
| 2026-11-03 12:17:32 | [CVE-2026-99259](https://nvd.nist.gov/vuln/detail/CVE-2026-99259) |  |  | In the Linux kernel, the following vulnerability has been resolved: soc/tegra: pmc: Fix uninitialised clock rate For le… |
| 2026-11-03 12:17:32 | [CVE-2026-99260](https://nvd.nist.gov/vuln/detail/CVE-2026-99260) |  |  | In the Linux kernel, the following vulnerability has been resolved: ntfs: fix resident conversion in ntfs_new_attr_flag… |
| 2026-11-03 12:17:33 | [CVE-2026-99261](https://nvd.nist.gov/vuln/detail/CVE-2026-99261) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdgpu: correct reservation fence slots for use… |
| 2026-11-03 12:17:33 | [CVE-2026-99262](https://nvd.nist.gov/vuln/detail/CVE-2026-99262) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/timeout: don't lose a cancel as io-wq arms… |
| 2026-11-03 12:17:33 | [CVE-2026-99263](https://nvd.nist.gov/vuln/detail/CVE-2026-99263) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/poll: avoid retry wakeup loss when droppin… |
| 2026-11-03 12:17:33 | [CVE-2026-99264](https://nvd.nist.gov/vuln/detail/CVE-2026-99264) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/net: don't retry recv on uncommitted buffe… |
| 2026-11-03 12:17:33 | [CVE-2026-99265](https://nvd.nist.gov/vuln/detail/CVE-2026-99265) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/openclose: keep the lock in io_pipe_fixed(… |
| 2026-11-03 12:17:33 | [CVE-2026-99266](https://nvd.nist.gov/vuln/detail/CVE-2026-99266) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/zcrx: fix buffer offsets in areas above 4G… |
| 2026-11-03 12:17:33 | [CVE-2026-99267](https://nvd.nist.gov/vuln/detail/CVE-2026-99267) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring/napi: make stale entries time out after 60… |
| 2026-11-03 12:17:33 | [CVE-2026-99268](https://nvd.nist.gov/vuln/detail/CVE-2026-99268) |  |  | In the Linux kernel, the following vulnerability has been resolved: io_uring: wake ring pollers for local task_work Wit… |
| 2026-11-03 12:17:34 | [CVE-2026-99269](https://nvd.nist.gov/vuln/detail/CVE-2026-99269) |  |  | In the Linux kernel, the following vulnerability has been resolved: sched_ext: Wait for SCX_OPSS_DISPATCHING before mov… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
