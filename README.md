# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-15 16:20 UTC

New CVEs published between 2026-11-15 15:19 UTC and 2026-11-15 16:20 UTC.

[Full CSV](data/new-cves-2026-11-15T16-20-16-034082Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-15 16:16:55 | [CVE-2025-71466](https://nvd.nist.gov/vuln/detail/CVE-2025-71466) | Medium | 6.8 | GPAC before 26.02.0 contains a NULL pointer dereference vulnerability in m2tsdmx_update_sdt() in src/filters/dmx_m2ts.c… |
| 2026-11-15 16:16:55 | [CVE-2025-71467](https://nvd.nist.gov/vuln/detail/CVE-2025-71467) | Medium | 6.8 | GPAC before 26.02.0 contains a NULL pointer dereference vulnerability in gf_node_get_field_by_name() in src/scenegraph/… |
| 2026-11-15 16:16:55 | [CVE-2025-71468](https://nvd.nist.gov/vuln/detail/CVE-2025-71468) | Medium | 6.8 | GPAC before 26.02.0 contains a NULL pointer dereference vulnerability in gf_dash_group_get_audio_channels() in src/medi… |
| 2026-11-15 16:16:56 | [CVE-2025-71470](https://nvd.nist.gov/vuln/detail/CVE-2025-71470) | Medium | 6.8 | MicroQuickJS (mquickjs) before commit 99eed3f contains an out-of-bounds read vulnerability because JS_Call() raises exc… |
| 2026-11-15 16:16:56 | [CVE-2026-129484](https://nvd.nist.gov/vuln/detail/CVE-2026-129484) | Medium | 5.3 | Kroki before 0.36.0 contains a reflected cross-site scripting vulnerability that allows unauthenticated attackers to in… |
| 2026-11-15 16:16:56 | [CVE-2026-129485](https://nvd.nist.gov/vuln/detail/CVE-2026-129485) | Medium | 6.9 | Kroki before 0.36.0 contains a server-side request forgery vulnerability in the BlockDiag family of engines that allows… |
| 2026-11-15 16:16:56 | [CVE-2026-129490](https://nvd.nist.gov/vuln/detail/CVE-2026-129490) | Medium | 6.8 | littlefs through 2.11.3, when built with LFS_MIGRATE, contains a type confusion vulnerability in lfs_dir_traverse() tha… |
| 2026-11-15 16:16:56 | [CVE-2025-71469](https://nvd.nist.gov/vuln/detail/CVE-2025-71469) | Medium | 6.8 | GPAC before 26.02.0 contains a type confusion vulnerability in ctxload_process() that passes non-object descriptors to… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
