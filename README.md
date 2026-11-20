# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 01:18 UTC

New CVEs published between 2026-11-20 00:18 UTC and 2026-11-20 01:18 UTC.

[Full CSV](data/new-cves-2026-11-20T01-18-47-106296Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 01:17:07 | [CVE-2025-71473](https://nvd.nist.gov/vuln/detail/CVE-2025-71473) | Medium | 6.9 | lwext4 through 1.0.0 contains a heap buffer overflow in ext4_fs_init_inode_bitmap() in src/ext4_fs.c because it does no… |
| 2026-11-20 01:17:08 | [CVE-2025-71474](https://nvd.nist.gov/vuln/detail/CVE-2025-71474) | Medium | 6.9 | lwext4 through 1.0.0 contains an out-of-bounds write vulnerability in ext4_fs_init_block_bitmap() that allows attackers… |
| 2026-11-20 01:17:08 | [CVE-2026-126540](https://nvd.nist.gov/vuln/detail/CVE-2026-126540) |  |  | Convert::ASN1 versions before 0.37 for Perl allow CPU exhaustion via quadratic bigint loop in os2ip. Every INTEGER or E… |
| 2026-11-20 01:17:08 | [CVE-2026-126568](https://nvd.nist.gov/vuln/detail/CVE-2026-126568) |  |  | Convert::ASN1 versions before 0.37 for Perl allow memory exhaustion via unbounded MSG_PEEK buffer doubling in asn_recv.… |
| 2026-11-20 01:17:09 | [CVE-2026-126576](https://nvd.nist.gov/vuln/detail/CVE-2026-126576) |  |  | Convert::ASN1 versions before 0.37 for Perl allow CPU exhaustion via unchecked exponent length in binary REAL decoding.… |
| 2026-11-20 01:17:09 | [CVE-2026-126682](https://nvd.nist.gov/vuln/detail/CVE-2026-126682) |  |  | Convert::ASN1 versions before 0.37 for Perl allow CPU exhaustion via exponent-notation string in INTEGER encoding. The… |
| 2026-11-20 01:17:09 | [CVE-2026-126819](https://nvd.nist.gov/vuln/detail/CVE-2026-126819) |  |  | Convert::ASN1 versions before 0.37 for Perl allow memory exhaustion via zero-length BIT STRING content. A BIT STRING wi… |
| 2026-11-20 01:17:09 | [CVE-2026-126956](https://nvd.nist.gov/vuln/detail/CVE-2026-126956) |  |  | Convert::ASN1 versions before 0.37 for Perl allow memory exhaustion via unlimited recursion depth in constructed-form s… |
| 2026-11-20 01:17:09 | [CVE-2026-131868](https://nvd.nist.gov/vuln/detail/CVE-2026-131868) |  |  | Convert::ASN1 versions before 0.37 for Perl allow memory exhaustion via a declared element length passed unchecked to s… |
| 2026-11-20 01:17:09 | [CVE-2026-131877](https://nvd.nist.gov/vuln/detail/CVE-2026-131877) |  |  | Convert::ASN1 versions before 0.37 for Perl allow CPU exhaustion via unbounded arc length in OBJECT IDENTIFIER decoding… |
| 2026-11-20 01:17:09 | [CVE-2026-133406](https://nvd.nist.gov/vuln/detail/CVE-2026-133406) | Medium | 4.8 | A vulnerability was determined in aoiflux mutant 2.3.0/2.4.0/2.5.0. This vulnerability affects unknown code of the file… |
| 2026-11-20 01:17:10 | [CVE-2026-133519](https://nvd.nist.gov/vuln/detail/CVE-2026-133519) | Medium | 6.8 | FFmpeg 7.0 through 9.0.2 contains an out-of-bounds read vulnerability in dvdvideo_menu_next_ps_block() in libavformat/d… |
| 2026-11-20 01:17:10 | [CVE-2026-133520](https://nvd.nist.gov/vuln/detail/CVE-2026-133520) | Medium | 5.3 | Dokploy 0.28.0 before 0.31.1 contains a path traversal vulnerability in the patch.readRepoDirectories tRPC procedure th… |
| 2026-11-20 01:17:10 | [CVE-2026-133521](https://nvd.nist.gov/vuln/detail/CVE-2026-133521) | Medium | 5.3 | Bar Assistant 3.0.0 before 6.11.0 contains an authorization bypass vulnerability in BarController::join that allows aut… |
| 2026-11-20 01:17:10 | [CVE-2026-133528](https://nvd.nist.gov/vuln/detail/CVE-2026-133528) | Critical | 9.3 | BeamNG.drive before 0.40.6 contains an out-of-bounds write vulnerability because JIT-compiled LuaJIT traces omit FFI ar… |
| 2026-11-20 01:17:10 | [CVE-2026-82091](https://nvd.nist.gov/vuln/detail/CVE-2026-82091) | Low | 3.2 | The Canva Desktop App before 1.128.0 stores encrypted application state on disk. The encryption key is hardcoded as a p… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
