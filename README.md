# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-24 16:19 UTC

New CVEs published between 2026-09-24 15:19 UTC and 2026-09-24 16:19 UTC.

[Full CSV](data/new-cves-2026-09-24T16-19-42-958296Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-24 16:17:06 | [CVE-2025-32000](https://nvd.nist.gov/vuln/detail/CVE-2025-32000) | Medium | 4.3 | HCL Sametime is vulnerable to insufficient input sanitization. The application did not appropriately sanitize user inpu… |
| 2026-09-24 16:17:07 | [CVE-2026-56737](https://nvd.nist.gov/vuln/detail/CVE-2026-56737) | High | 8.1 | phpMyFAQ is an open source FAQ web application. Versions 3.2.0 through 4.1.5 contain an authentication bypass in its pu… |
| 2026-09-24 16:17:07 | [CVE-2026-56739](https://nvd.nist.gov/vuln/detail/CVE-2026-56739) | High | 8.5 | Logto is the modern, open-source auth infrastructure for SaaS and AI apps. Prior to 1.43.0, Logto fetches administrator… |
| 2026-09-24 16:17:08 | [CVE-2026-63203](https://nvd.nist.gov/vuln/detail/CVE-2026-63203) | High | 7.6 | Logto is the modern, open-source auth infrastructure for SaaS and AI apps. From 1.31.0 until 1.42.0, the Account API ha… |
| 2026-09-24 16:17:08 | [CVE-2026-63630](https://nvd.nist.gov/vuln/detail/CVE-2026-63630) | Low | 3.4 | BentoPDF is a client-side PDF toolkit that is self hostable. In 2.8.6 and earlier, deserializeWorkflow() accepts the Ti… |
| 2026-09-24 16:17:09 | [CVE-2026-67233](https://nvd.nist.gov/vuln/detail/CVE-2026-67233) | Medium | 6.0 | RabbitMQ is a messaging and streaming broker. Prior to versions 3.13.15, 4.0.20, 4.1.11, 4.2.6, and 4.3.1, The shovel m… |
| 2026-09-24 16:17:10 | [CVE-2026-75907](https://nvd.nist.gov/vuln/detail/CVE-2026-75907) |  |  | The door access control on a Norwegian Cruise Line asset grants entry based only on the credential's static 7-byte UID… |
| 2026-09-24 16:17:10 | [CVE-2026-76907](https://nvd.nist.gov/vuln/detail/CVE-2026-76907) | Medium | 6.5 | LaSuite Doc is a collaborative note taking, wiki and documentation platform. From 4.8.2 until 5.4.0, GET /api/v1.0/docu… |
| 2026-09-24 16:17:10 | [CVE-2026-77581](https://nvd.nist.gov/vuln/detail/CVE-2026-77581) | High | 8.6 | BentoPDF is a client-side PDF toolkit that is self hostable. In 2.8.6 and earlier, the certificate and timestamp CORS p… |
| 2026-09-24 16:17:11 | [CVE-2026-79758](https://nvd.nist.gov/vuln/detail/CVE-2026-79758) | Medium | 5.4 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 1.8.… |
| 2026-09-24 16:17:11 | [CVE-2026-79759](https://nvd.nist.gov/vuln/detail/CVE-2026-79759) | Medium | 4.3 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 1.7.… |
| 2026-09-24 16:17:11 | [CVE-2026-79760](https://nvd.nist.gov/vuln/detail/CVE-2026-79760) | Medium | 6.4 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 2.5.… |
| 2026-09-24 16:17:11 | [CVE-2026-79761](https://nvd.nist.gov/vuln/detail/CVE-2026-79761) | Medium | 6.6 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 1.7.… |
| 2026-09-24 16:17:12 | [CVE-2026-88355](https://nvd.nist.gov/vuln/detail/CVE-2026-88355) |  |  | An incorrect buffer size calculation vulnerability exists in tinyexpr commit 4a7456e in new_expr(). For arity-0 express… |
| 2026-09-24 16:17:12 | [CVE-2026-88357](https://nvd.nist.gov/vuln/detail/CVE-2026-88357) |  |  | nDPI 5.1.0 contains a memory access issue in the DNS dissector and serializer deserialization code. Specially crafted n… |
| 2026-09-24 16:17:13 | [CVE-2026-88358](https://nvd.nist.gov/vuln/detail/CVE-2026-88358) |  |  | simdjson 4.6.1 contains a one-byte out-of-bounds read vulnerability in dom::parser::parse_unpadded(). A specially craft… |
| 2026-09-24 16:17:13 | [CVE-2026-88361](https://nvd.nist.gov/vuln/detail/CVE-2026-88361) |  |  | SumatraPDF 3.6.1 contains an integer overflow vulnerability in EngineMupdf::BuildPageLabelRec() when parsing PDF PageLa… |
| 2026-09-24 16:17:13 | [CVE-2026-88362](https://nvd.nist.gov/vuln/detail/CVE-2026-88362) |  |  | MuJS e892c9fdb contains an incorrect numeric conversion vulnerability in jsR_isindex() in jsrun.c. A specially crafted… |
| 2026-09-24 16:17:13 | [CVE-2026-88365](https://nvd.nist.gov/vuln/detail/CVE-2026-88365) |  |  | minimp3 commit ea99364f contains an integer overflow vulnerability in mp3dec_skip_id3v1() when parsing the APEv2 tag-si… |
| 2026-09-24 16:17:13 | [CVE-2026-88366](https://nvd.nist.gov/vuln/detail/CVE-2026-88366) |  |  | NanoSVG commit 239e102ec contains an incorrect numeric conversion vulnerability in nsvg__pathArcTo() when parsing SVG a… |
| 2026-09-24 16:17:13 | [CVE-2026-88368](https://nvd.nist.gov/vuln/detail/CVE-2026-88368) |  |  | NanoSVG commit 239e102ec contains an incorrect numeric conversion vulnerability in the rasterizer's nsvg__addActive() f… |
| 2026-09-24 16:17:13 | [CVE-2026-88369](https://nvd.nist.gov/vuln/detail/CVE-2026-88369) |  |  | zserge jsmn commit 25647e6 is vulnerable to Buffer Overflow in example/jsondump.c dump(). |
| 2026-09-24 16:17:13 | [CVE-2026-88370](https://nvd.nist.gov/vuln/detail/CVE-2026-88370) |  |  | libconfini 1.16.4 contains a heap out-of-bounds write condition involving the bundled load_ini_buffer.h utility and str… |
| 2026-09-24 16:17:14 | [CVE-2026-88371](https://nvd.nist.gov/vuln/detail/CVE-2026-88371) |  |  | ZBar commit 2ea2ca58 contains an undefined-behavior vulnerability in the Code 128 decode6() function. When processing s… |
| 2026-09-24 16:17:14 | [CVE-2026-92680](https://nvd.nist.gov/vuln/detail/CVE-2026-92680) | Medium | 6.8 | Araxis Merge for Windows version 2011.4074 through 2026.0 stores user-configured credentials for remote servers in the… |
| 2026-09-24 16:17:14 | [CVE-2026-93205](https://nvd.nist.gov/vuln/detail/CVE-2026-93205) |  |  | In the Linux kernel, the following vulnerability has been resolved: iommu/arm-smmu-v3: Manage teardown with devm arm_sm… |
| 2026-09-24 16:17:14 | [CVE-2026-93206](https://nvd.nist.gov/vuln/detail/CVE-2026-93206) |  |  | In the Linux kernel, the following vulnerability has been resolved: PCI/proc: Use file_ns_capable() when checking confi… |
| 2026-09-24 16:17:15 | [CVE-2026-93207](https://nvd.nist.gov/vuln/detail/CVE-2026-93207) |  |  | In the Linux kernel, the following vulnerability has been resolved: SUNRPC: Zero rpc_gss_wire_cred at svcauth_gss_decod… |
| 2026-09-24 16:17:15 | [CVE-2026-93208](https://nvd.nist.gov/vuln/detail/CVE-2026-93208) |  |  | In the Linux kernel, the following vulnerability has been resolved: kasan: fix cache shrink race with CPU hotplug kasan… |
| 2026-09-24 16:17:15 | [CVE-2026-93209](https://nvd.nist.gov/vuln/detail/CVE-2026-93209) |  |  | In the Linux kernel, the following vulnerability has been resolved: Bluetooth: hci_core: use skb_get() instead of skb_c… |
| 2026-09-24 16:17:15 | [CVE-2026-93210](https://nvd.nist.gov/vuln/detail/CVE-2026-93210) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: harden DFS cache against invalid targe… |
| 2026-09-24 16:17:16 | [CVE-2026-93211](https://nvd.nist.gov/vuln/detail/CVE-2026-93211) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: initialize DRC hash table before registering… |
| 2026-09-24 16:17:16 | [CVE-2026-93212](https://nvd.nist.gov/vuln/detail/CVE-2026-93212) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: guard nfsd_serv deref in nfsd_file_net_dispos… |
| 2026-09-24 16:17:16 | [CVE-2026-93213](https://nvd.nist.gov/vuln/detail/CVE-2026-93213) |  |  | In the Linux kernel, the following vulnerability has been resolved: of: fix out-of-bounds read in of_alias_scan() stem… |
| 2026-09-24 16:17:16 | [CVE-2026-93214](https://nvd.nist.gov/vuln/detail/CVE-2026-93214) |  |  | In the Linux kernel, the following vulnerability has been resolved: usb: gadget: f_tcm: fix deadlock in usbg_make_tpg()… |
| 2026-09-24 16:17:16 | [CVE-2026-93215](https://nvd.nist.gov/vuln/detail/CVE-2026-93215) |  |  | In the Linux kernel, the following vulnerability has been resolved: cdx: Fix double free when sysfs file creation fails… |
| 2026-09-24 16:17:16 | [CVE-2026-93216](https://nvd.nist.gov/vuln/detail/CVE-2026-93216) |  |  | In the Linux kernel, the following vulnerability has been resolved: mm/page_owner: use memcg_data snapshot to avoid TOC… |
| 2026-09-24 16:17:16 | [CVE-2026-93217](https://nvd.nist.gov/vuln/detail/CVE-2026-93217) |  |  | In the Linux kernel, the following vulnerability has been resolved: mm/madvise: skip device-private PMDs in cold and pa… |
| 2026-09-24 16:17:16 | [CVE-2026-93218](https://nvd.nist.gov/vuln/detail/CVE-2026-93218) |  |  | In the Linux kernel, the following vulnerability has been resolved: mm/huge_memory: skip device-private PMDs in madvise… |
| 2026-09-24 16:17:17 | [CVE-2026-93219](https://nvd.nist.gov/vuln/detail/CVE-2026-93219) |  |  | In the Linux kernel, the following vulnerability has been resolved: clocksource/drivers/timer-sun4i: Advertise a real m… |
| 2026-09-24 16:17:17 | [CVE-2026-93220](https://nvd.nist.gov/vuln/detail/CVE-2026-93220) |  |  | In the Linux kernel, the following vulnerability has been resolved: sched_ext: Keep kick_sync waiting on the rq's own C… |
| 2026-09-24 16:17:17 | [CVE-2026-93221](https://nvd.nist.gov/vuln/detail/CVE-2026-93221) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: convert nfsd_net boolean flags to unsigned lo… |
| 2026-09-24 16:17:17 | [CVE-2026-93222](https://nvd.nist.gov/vuln/detail/CVE-2026-93222) |  |  | In the Linux kernel, the following vulnerability has been resolved: signal: avoid shared siginfo namespace rewrites sen… |
| 2026-09-24 16:17:17 | [CVE-2026-93223](https://nvd.nist.gov/vuln/detail/CVE-2026-93223) |  |  | In the Linux kernel, the following vulnerability has been resolved: staging: media: tegra-video: fix of_node_put() on V… |
| 2026-09-24 16:17:17 | [CVE-2026-93224](https://nvd.nist.gov/vuln/detail/CVE-2026-93224) |  |  | In the Linux kernel, the following vulnerability has been resolved: svcrdma: Fix unmatched rn_unregister on failed acce… |
| 2026-09-24 16:17:17 | [CVE-2026-93225](https://nvd.nist.gov/vuln/detail/CVE-2026-93225) |  |  | In the Linux kernel, the following vulnerability has been resolved: phy: fsl-imx8mq-usb: fix typec switch leak on probe… |
| 2026-09-24 16:17:17 | [CVE-2026-93226](https://nvd.nist.gov/vuln/detail/CVE-2026-93226) |  |  | In the Linux kernel, the following vulnerability has been resolved: ipv6: use RCU iterator to dump route exceptions rt6… |
| 2026-09-24 16:17:18 | [CVE-2026-93227](https://nvd.nist.gov/vuln/detail/CVE-2026-93227) |  |  | In the Linux kernel, the following vulnerability has been resolved: mm/mm_init: deferred_grow_zone(): fix out-of-range… |
| 2026-09-24 16:17:18 | [CVE-2026-93228](https://nvd.nist.gov/vuln/detail/CVE-2026-93228) |  |  | In the Linux kernel, the following vulnerability has been resolved: svcrdma: Reject Write/Reply chunks with segcount 0… |
| 2026-09-24 16:17:18 | [CVE-2026-93229](https://nvd.nist.gov/vuln/detail/CVE-2026-93229) |  |  | In the Linux kernel, the following vulnerability has been resolved: nfsd: add missing read barrier to rpc_status_get du… |
| 2026-09-24 16:17:18 | [CVE-2026-93230](https://nvd.nist.gov/vuln/detail/CVE-2026-93230) |  |  | In the Linux kernel, the following vulnerability has been resolved: mm/hugetlb: initialize gigantic bootmem hugepage st… |
| 2026-09-24 16:17:18 | [CVE-2026-93231](https://nvd.nist.gov/vuln/detail/CVE-2026-93231) |  |  | In the Linux kernel, the following vulnerability has been resolved: lockd: fix swapped arguments in nlmsvc_match_ip() W… |
| 2026-09-24 16:17:18 | [CVE-2026-93232](https://nvd.nist.gov/vuln/detail/CVE-2026-93232) |  |  | In the Linux kernel, the following vulnerability has been resolved: mm/hugetlb: fix boot panic with CONFIG_DEBUG_VM and… |
| 2026-09-24 16:17:18 | [CVE-2026-93233](https://nvd.nist.gov/vuln/detail/CVE-2026-93233) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/nouveau/dmem: fix callocated underflow on large… |
| 2026-09-24 16:17:19 | [CVE-2026-93234](https://nvd.nist.gov/vuln/detail/CVE-2026-93234) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/gud: validate TV mode names before creating enu… |
| 2026-09-24 16:17:19 | [CVE-2026-93235](https://nvd.nist.gov/vuln/detail/CVE-2026-93235) |  |  | In the Linux kernel, the following vulnerability has been resolved: f2fs: fix to zero post-EOF data when extending file… |
| 2026-09-24 16:17:19 | [CVE-2026-93236](https://nvd.nist.gov/vuln/detail/CVE-2026-93236) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: meson: vdec: fix NULL pointer deref in vdec_… |
| 2026-09-24 16:17:19 | [CVE-2026-93237](https://nvd.nist.gov/vuln/detail/CVE-2026-93237) |  |  | In the Linux kernel, the following vulnerability has been resolved: LoongArch: Add DIRECT_MAP_PHYSMEM_END definition ge… |
| 2026-09-24 16:17:19 | [CVE-2026-93238](https://nvd.nist.gov/vuln/detail/CVE-2026-93238) |  |  | In the Linux kernel, the following vulnerability has been resolved: s390/vfio-ap: fix potential use of uninitialized ap… |
| 2026-09-24 16:17:19 | [CVE-2026-93239](https://nvd.nist.gov/vuln/detail/CVE-2026-93239) |  |  | In the Linux kernel, the following vulnerability has been resolved: arm64: mm: Fix the lockless page-table walk in show… |
| 2026-09-24 16:17:19 | [CVE-2026-93240](https://nvd.nist.gov/vuln/detail/CVE-2026-93240) |  |  | In the Linux kernel, the following vulnerability has been resolved: memcg: make the v1 soft limit knob inert The v1 sof… |
| 2026-09-24 16:17:19 | [CVE-2026-93241](https://nvd.nist.gov/vuln/detail/CVE-2026-93241) |  |  | In the Linux kernel, the following vulnerability has been resolved: memcg: bypass the reclaim and oom killer for dying… |
| 2026-09-24 16:17:20 | [CVE-2026-93242](https://nvd.nist.gov/vuln/detail/CVE-2026-93242) |  |  | In the Linux kernel, the following vulnerability has been resolved: scsi: qla2xxx: Fix response queue over-consumption… |
| 2026-09-24 16:17:20 | [CVE-2026-93243](https://nvd.nist.gov/vuln/detail/CVE-2026-93243) |  |  | In the Linux kernel, the following vulnerability has been resolved: mm/secretmem: properly account locked pages secretm… |
| 2026-09-24 16:17:20 | [CVE-2026-93244](https://nvd.nist.gov/vuln/detail/CVE-2026-93244) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/sysfb: simpledrm: Improve stride validation Val… |
| 2026-09-24 16:17:20 | [CVE-2026-93245](https://nvd.nist.gov/vuln/detail/CVE-2026-93245) |  |  | In the Linux kernel, the following vulnerability has been resolved: apparmor: policy_int make sure list heads are initi… |
| 2026-09-24 16:17:20 | [CVE-2026-93246](https://nvd.nist.gov/vuln/detail/CVE-2026-93246) |  |  | In the Linux kernel, the following vulnerability has been resolved: octeontx2-af: fix out-of-bounds read setting MSI-X… |
| 2026-09-24 16:17:20 | [CVE-2026-93247](https://nvd.nist.gov/vuln/detail/CVE-2026-93247) |  |  | In the Linux kernel, the following vulnerability has been resolved: Bluetooth: mgmt: fix 'hdev->discovery.uuids' NULL d… |
| 2026-09-24 16:17:20 | [CVE-2026-93248](https://nvd.nist.gov/vuln/detail/CVE-2026-93248) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/xe: don't WARN on kernel job timeout when devic… |
| 2026-09-24 16:17:21 | [CVE-2026-93249](https://nvd.nist.gov/vuln/detail/CVE-2026-93249) |  |  | In the Linux kernel, the following vulnerability has been resolved: spi: amlogic-spisg: Make sure clk_init_data is full… |
| 2026-09-24 16:17:21 | [CVE-2026-93250](https://nvd.nist.gov/vuln/detail/CVE-2026-93250) |  |  | In the Linux kernel, the following vulnerability has been resolved: vxlan: mdb: Fix use-after-free in vxlan_mdb_flush()… |
| 2026-09-24 16:17:21 | [CVE-2026-93251](https://nvd.nist.gov/vuln/detail/CVE-2026-93251) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPI: bus: Introduce acpi_bus_get_primary_device()… |
| 2026-09-24 16:17:21 | [CVE-2026-93252](https://nvd.nist.gov/vuln/detail/CVE-2026-93252) |  |  | In the Linux kernel, the following vulnerability has been resolved: ocfs2: fix circular locking dependency in ocfs2_ini… |
| 2026-09-24 16:17:21 | [CVE-2026-93253](https://nvd.nist.gov/vuln/detail/CVE-2026-93253) |  |  | In the Linux kernel, the following vulnerability has been resolved: sched/isolation: Defer freeing of cpumask memblock… |
| 2026-09-24 16:17:21 | [CVE-2026-93254](https://nvd.nist.gov/vuln/detail/CVE-2026-93254) |  |  | In the Linux kernel, the following vulnerability has been resolved: arm64: entry: Avoid unnecessary local_irq_disable()… |
| 2026-09-24 16:17:22 | [CVE-2026-93255](https://nvd.nist.gov/vuln/detail/CVE-2026-93255) |  |  | In the Linux kernel, the following vulnerability has been resolved: btrfs: make sure EXTENT_BUFFER_READING is cleared u… |
| 2026-09-24 16:17:22 | [CVE-2026-93256](https://nvd.nist.gov/vuln/detail/CVE-2026-93256) |  |  | In the Linux kernel, the following vulnerability has been resolved: arm64: hibernate: mask DAIF before restoring hibern… |
| 2026-09-24 16:17:22 | [CVE-2026-93257](https://nvd.nist.gov/vuln/detail/CVE-2026-93257) |  |  | In the Linux kernel, the following vulnerability has been resolved: block: handle nogenerate/noverify properly in fs-in… |
| 2026-09-24 16:17:22 | [CVE-2026-93258](https://nvd.nist.gov/vuln/detail/CVE-2026-93258) |  |  | In the Linux kernel, the following vulnerability has been resolved: ocfs2: do not use make_bad_inode() in ocfs2_read_in… |
| 2026-09-24 16:17:22 | [CVE-2026-93259](https://nvd.nist.gov/vuln/detail/CVE-2026-93259) |  |  | In the Linux kernel, the following vulnerability has been resolved: powerpc/irq: Fix missing r2 clobber in PCREL inline… |
| 2026-09-24 16:17:22 | [CVE-2026-93260](https://nvd.nist.gov/vuln/detail/CVE-2026-93260) |  |  | In the Linux kernel, the following vulnerability has been resolved: powerpc/xive: propagate IPI init errors to prevent… |
| 2026-09-24 16:17:22 | [CVE-2026-93261](https://nvd.nist.gov/vuln/detail/CVE-2026-93261) |  |  | In the Linux kernel, the following vulnerability has been resolved: locking/lockdep: Fix NULL pointer dereference in __… |
| 2026-09-24 16:17:22 | [CVE-2026-93262](https://nvd.nist.gov/vuln/detail/CVE-2026-93262) |  |  | In the Linux kernel, the following vulnerability has been resolved: md/raid5-ppl: fix use-after-free in ppl_do_flush()… |
| 2026-09-24 16:17:23 | [CVE-2026-93263](https://nvd.nist.gov/vuln/detail/CVE-2026-93263) |  |  | In the Linux kernel, the following vulnerability has been resolved: clk: eswin: Zero-initialize stack-allocated clk_ini… |
| 2026-09-24 16:17:23 | [CVE-2026-93264](https://nvd.nist.gov/vuln/detail/CVE-2026-93264) |  |  | In the Linux kernel, the following vulnerability has been resolved: RDMA/efa: Fix PBL chunk length computation On regis… |
| 2026-09-24 16:17:23 | [CVE-2026-93265](https://nvd.nist.gov/vuln/detail/CVE-2026-93265) |  |  | In the Linux kernel, the following vulnerability has been resolved: PCI/pwrctrl: tc9563: Fix parsing the integrated Eth… |
| 2026-09-24 16:17:23 | [CVE-2026-93266](https://nvd.nist.gov/vuln/detail/CVE-2026-93266) |  |  | In the Linux kernel, the following vulnerability has been resolved: arm64: RSI: fix field-spanning write warning in att… |
| 2026-09-24 16:17:23 | [CVE-2026-93267](https://nvd.nist.gov/vuln/detail/CVE-2026-93267) |  |  | In the Linux kernel, the following vulnerability has been resolved: RDMA/core: Fix potential use after free in uverbs_f… |
| 2026-09-24 16:17:23 | [CVE-2026-93268](https://nvd.nist.gov/vuln/detail/CVE-2026-93268) |  |  | In the Linux kernel, the following vulnerability has been resolved: ext4: skip extra isize expansion during mount to pr… |
| 2026-09-24 16:17:23 | [CVE-2026-93269](https://nvd.nist.gov/vuln/detail/CVE-2026-93269) |  |  | In the Linux kernel, the following vulnerability has been resolved: ext4: fix circular lock dependency in ext4_ext_migr… |
| 2026-09-24 16:17:24 | [CVE-2026-93270](https://nvd.nist.gov/vuln/detail/CVE-2026-93270) |  |  | In the Linux kernel, the following vulnerability has been resolved: bpf: Disallow interpreter fallback for BPF_ADDR_PER… |
| 2026-09-24 16:17:24 | [CVE-2026-93271](https://nvd.nist.gov/vuln/detail/CVE-2026-93271) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: ath11k: cap out-of-range rx MCS instead of le… |
| 2026-09-24 16:17:24 | [CVE-2026-93272](https://nvd.nist.gov/vuln/detail/CVE-2026-93272) |  |  | In the Linux kernel, the following vulnerability has been resolved: remoteproc: qcom_wcnss: Fix handling the lack of PD… |
| 2026-09-24 16:17:24 | [CVE-2026-93273](https://nvd.nist.gov/vuln/detail/CVE-2026-93273) |  |  | In the Linux kernel, the following vulnerability has been resolved: regulator: tps6594: Fix device node reference leaks… |
| 2026-09-24 16:17:24 | [CVE-2026-93274](https://nvd.nist.gov/vuln/detail/CVE-2026-93274) |  |  | In the Linux kernel, the following vulnerability has been resolved: pinctrl: bcm2835: Don't remove an unregistered GPIO… |
| 2026-09-24 16:17:24 | [CVE-2026-93275](https://nvd.nist.gov/vuln/detail/CVE-2026-93275) |  |  | In the Linux kernel, the following vulnerability has been resolved: perf/x86/intel/pt: Fix stop/start with no update If… |
| 2026-09-24 16:17:24 | [CVE-2026-93276](https://nvd.nist.gov/vuln/detail/CVE-2026-93276) |  |  | In the Linux kernel, the following vulnerability has been resolved: phy: renesas: phy-rcar-gen3-usb2: Fix devm action r… |
| 2026-09-24 16:17:24 | [CVE-2026-93277](https://nvd.nist.gov/vuln/detail/CVE-2026-93277) |  |  | In the Linux kernel, the following vulnerability has been resolved: RDMA/bnxt_re: Validate udata before executing comma… |
| 2026-09-24 16:17:25 | [CVE-2026-93278](https://nvd.nist.gov/vuln/detail/CVE-2026-93278) |  |  | In the Linux kernel, the following vulnerability has been resolved: staging: octeon: add missing napi_disable in cvm_oc… |
| 2026-09-24 16:17:25 | [CVE-2026-93279](https://nvd.nist.gov/vuln/detail/CVE-2026-93279) |  |  | In the Linux kernel, the following vulnerability has been resolved: staging: octeon: add missing tasklet_kill in cvm_oc… |
| 2026-09-24 16:17:25 | [CVE-2026-93280](https://nvd.nist.gov/vuln/detail/CVE-2026-93280) |  |  | In the Linux kernel, the following vulnerability has been resolved: greybus: audio: bound the topology section sizes ag… |
| 2026-09-24 16:17:25 | [CVE-2026-93281](https://nvd.nist.gov/vuln/detail/CVE-2026-93281) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: rtw89: fix HE extended capability length chec… |
| 2026-09-24 16:17:25 | [CVE-2026-93282](https://nvd.nist.gov/vuln/detail/CVE-2026-93282) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: fix maximum allowed access checks The DACL p… |
| 2026-09-24 16:17:25 | [CVE-2026-93283](https://nvd.nist.gov/vuln/detail/CVE-2026-93283) |  |  | In the Linux kernel, the following vulnerability has been resolved: i3c: master: Fix device_register() error path When… |
| 2026-09-24 16:17:25 | [CVE-2026-93425](https://nvd.nist.gov/vuln/detail/CVE-2026-93425) | Critical | 9.9 | Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the patch.readRepoDirectories tRPC pro… |
| 2026-09-24 16:17:26 | [CVE-2026-93541](https://nvd.nist.gov/vuln/detail/CVE-2026-93541) | Medium | 6.5 | An out-of-bounds read in libXi's XQueryDeviceState() in libXi before 1.8.4 could be used by a |
| 2026-09-24 16:17:27 | [CVE-2026-96744](https://nvd.nist.gov/vuln/detail/CVE-2026-96744) | High | 7.1 | Improper neutralization of special elements in data query logic in the cache lock implementation of the MongoDB integra… |
| 2026-09-24 16:17:27 | [CVE-2026-96745](https://nvd.nist.gov/vuln/detail/CVE-2026-96745) | Medium | 6.3 | Deserialization of untrusted data in the command monitoring support of the MongoDB PHP Driver can cause class names emb… |
| 2026-09-24 16:17:27 | [CVE-2026-96746](https://nvd.nist.gov/vuln/detail/CVE-2026-96746) | High | 8.3 | An out-of-bounds write in the connection-monitoring logic of the MongoDB C Driver may allow an unauthenticated party wh… |
| 2026-09-24 16:17:27 | [CVE-2026-96750](https://nvd.nist.gov/vuln/detail/CVE-2026-96750) | High | 7.3 | MongoDB Compass can interpolate a database name without escaping into the initial input of its embedded MongoDB shell w… |
| 2026-09-24 16:17:28 | [CVE-2026-96873](https://nvd.nist.gov/vuln/detail/CVE-2026-96873) | Medium | 5.5 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Mediawiki - Cirru… |
| 2026-09-24 16:17:28 | [CVE-2026-97225](https://nvd.nist.gov/vuln/detail/CVE-2026-97225) | Medium | 5.3 | A flaw has been found in DbGate up to 7.2.5-beta.5. This affects an unknown function of the file packages/api/src/contr… |
| 2026-09-24 16:17:29 | [CVE-2026-97226](https://nvd.nist.gov/vuln/detail/CVE-2026-97226) | Medium | 5.3 | A vulnerability has been found in DbGate up to 7.2.5/7.3.1-premium-beta.1. This impacts the function fs.readFile of the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
