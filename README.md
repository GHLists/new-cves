# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-24 17:19 UTC

New CVEs published between 2026-09-24 16:19 UTC and 2026-09-24 17:19 UTC.

[Full CSV](data/new-cves-2026-09-24T17-19-40-778412Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-24 17:17:04 | [CVE-2026-26054](https://nvd.nist.gov/vuln/detail/CVE-2026-26054) | Medium | 6.8 | SumatraPDF is a multi-format reader for Windows. Prior to 3.6, the MobiDoc::ParseHeader function in src/MobiDoc.cpp val… |
| 2026-09-24 17:17:04 | [CVE-2026-47132](https://nvd.nist.gov/vuln/detail/CVE-2026-47132) | Medium | 5.4 | phpMyFAQ is an open source FAQ web application. Prior to version 4.2.0-alpha, an authenticated SQL LIKE wildcard inject… |
| 2026-09-24 17:17:04 | [CVE-2026-56738](https://nvd.nist.gov/vuln/detail/CVE-2026-56738) | High | 8.5 | phpMyFAQ is an open source FAQ web application. The `StopWords::add()` method inversions prior to 4.1.6 builds a SQL `I… |
| 2026-09-24 17:17:05 | [CVE-2026-56744](https://nvd.nist.gov/vuln/detail/CVE-2026-56744) | High | 8.7 | `@bsv/wallet-toolbox` provides BRC-100 wallet signing and storage components, while `@bsv/wallet-toolbox-client` and `@… |
| 2026-09-24 17:17:05 | [CVE-2026-62368](https://nvd.nist.gov/vuln/detail/CVE-2026-62368) | High | 8.1 | Snipe-IT is an IT asset/license management system. Prior to 8.7.0, a user with the customfields.create permission can s… |
| 2026-09-24 17:17:05 | [CVE-2026-63493](https://nvd.nist.gov/vuln/detail/CVE-2026-63493) | High | 8.6 | Snipe-IT is an IT asset/license management system. Prior to 8.7.0, a password-authenticated session for an account with… |
| 2026-09-24 17:17:05 | [CVE-2026-63498](https://nvd.nist.gov/vuln/detail/CVE-2026-63498) | High | 8.7 | Snipe-IT is an IT asset/license management system. Prior to 8.7.0, the uploaded-files API endpoint GET /api/v1/{object_… |
| 2026-09-24 17:17:06 | [CVE-2026-79762](https://nvd.nist.gov/vuln/detail/CVE-2026-79762) | Medium | 5.5 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 1.7.… |
| 2026-09-24 17:17:06 | [CVE-2026-79763](https://nvd.nist.gov/vuln/detail/CVE-2026-79763) | Medium | 5.3 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 2.4.… |
| 2026-09-24 17:17:06 | [CVE-2026-79764](https://nvd.nist.gov/vuln/detail/CVE-2026-79764) | High | 7.7 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 2.5.… |
| 2026-09-24 17:17:06 | [CVE-2026-79766](https://nvd.nist.gov/vuln/detail/CVE-2026-79766) | Critical | 9.1 | Termix is a web-based server management platform with SSH terminal, tunneling, and file editing capabilities. From 2.4.… |
| 2026-09-24 17:17:06 | [CVE-2026-84302](https://nvd.nist.gov/vuln/detail/CVE-2026-84302) | Medium | 4.2 | Discourse is an open-source discussion platform. Prior to 2026.1.6, 2026.5.2, 2026.6.1, and 2026.7.0, Discourse AI revi… |
| 2026-09-24 17:17:06 | [CVE-2026-88367](https://nvd.nist.gov/vuln/detail/CVE-2026-88367) |  |  | NanoSVG 239e102ec contains an incorrect numeric conversion vulnerability in nsvg__curveDivs() during SVG stroke rasteri… |
| 2026-09-24 17:17:07 | [CVE-2026-88372](https://nvd.nist.gov/vuln/detail/CVE-2026-88372) |  |  | libsndfile 1.2.2 contains an integer overflow vulnerability in mat4_read_header() when parsing crafted MAT4 (MATLAB v4)… |
| 2026-09-24 17:17:07 | [CVE-2026-88373](https://nvd.nist.gov/vuln/detail/CVE-2026-88373) |  |  | libde265 commit 4d45a6b contains a NULL pointer dereference vulnerability in the NAL parsing path. When de265_push_NAL(… |
| 2026-09-24 17:17:07 | [CVE-2026-88376](https://nvd.nist.gov/vuln/detail/CVE-2026-88376) |  |  | Bento4 1.6.0.0 contains an integer underflow vulnerability in AP4_AvccAtom::Create() and AP4_HvccAtom::Create(). A spec… |
| 2026-09-24 17:17:07 | [CVE-2026-88377](https://nvd.nist.gov/vuln/detail/CVE-2026-88377) |  |  | Bento4 1.6.0.0 contains an integer underflow vulnerability in the avcC and hvcC configuration atom parsers. A specially… |
| 2026-09-24 17:17:07 | [CVE-2026-88378](https://nvd.nist.gov/vuln/detail/CVE-2026-88378) |  |  | QuickJS commit 04be24600 contains a heap out-of-bounds write condition in JS_ReadFunctionTag(). |
| 2026-09-24 17:17:07 | [CVE-2026-88382](https://nvd.nist.gov/vuln/detail/CVE-2026-88382) |  |  | hiredis commit 29ea279 (post-v1.5.0) contains an uncontrolled memory allocation vulnerability in its RESP aggregate par… |
| 2026-09-24 17:17:07 | [CVE-2026-88383](https://nvd.nist.gov/vuln/detail/CVE-2026-88383) |  |  | libical 4.0.6 contains an incompatible function pointer in icalparameter_string_to_kind(). When parsing iCalendar data… |
| 2026-09-24 17:17:07 | [CVE-2026-88384](https://nvd.nist.gov/vuln/detail/CVE-2026-88384) |  |  | OpenEXR 3.4.14 contains a NULL Pointer Dereference in the C++ attribute parsing path. A specially crafted EXR file cont… |
| 2026-09-24 17:17:08 | [CVE-2026-88385](https://nvd.nist.gov/vuln/detail/CVE-2026-88385) |  |  | Mini-XML 4.0.5 contains a memory leak vulnerability in mxml_load_data() during malformed XML parsing. Specially crafted… |
| 2026-09-24 17:17:08 | [CVE-2026-88390](https://nvd.nist.gov/vuln/detail/CVE-2026-88390) |  |  | An out-of-bounds write vulnerability in jslGetTokenValueAsString() in Espruino 2v29 (commit bffc6d0) allows crafted Jav… |
| 2026-09-24 17:17:08 | [CVE-2026-91122](https://nvd.nist.gov/vuln/detail/CVE-2026-91122) | High | 8.7 | Discourse is an open-source discussion platform. Prior to 2026.1.8, 2026.6.3, 2026.7.2, and 2026.8.0, the video placeho… |
| 2026-09-24 17:17:08 | [CVE-2026-91123](https://nvd.nist.gov/vuln/detail/CVE-2026-91123) | High | 7.2 | Discourse is an open-source discussion platform. Prior to 2026.1.8, 2026.6.3, 2026.7.2, and 2026.8.0, the iframe src tr… |
| 2026-09-24 17:17:08 | [CVE-2026-91132](https://nvd.nist.gov/vuln/detail/CVE-2026-91132) | Medium | 4.3 | Discourse is an open-source discussion platform. Prior to 2026.1.8, 2026.6.3, 2026.7.2, and 2026.8.0, sites using wildc… |
| 2026-09-24 17:17:08 | [CVE-2026-91133](https://nvd.nist.gov/vuln/detail/CVE-2026-91133) | Medium | 6.5 | Discourse is an open-source discussion platform. Prior to 2026.1.8, 2026.6.3, 2026.7.2, and 2026.8.0, authenticated use… |
| 2026-09-24 17:17:09 | [CVE-2026-91134](https://nvd.nist.gov/vuln/detail/CVE-2026-91134) | Medium | 5.4 | Discourse is an open-source discussion platform. Prior to 2026.1.8, 2026.6.3, 2026.7.2, and 2026.8.0, the Discourse pos… |
| 2026-09-24 17:17:09 | [CVE-2026-91160](https://nvd.nist.gov/vuln/detail/CVE-2026-91160) | High | 8.2 | OpenWA is a free, open source, self-hosted WhatsApp API gateway. Prior to 0.23.5, the /events WebSocket gateway deliver… |
| 2026-09-24 17:17:09 | [CVE-2026-91161](https://nvd.nist.gov/vuln/detail/CVE-2026-91161) | Medium | 6.4 | OpenWA is a free, open source, self-hosted WhatsApp API gateway. Prior to 0.23.5, the GET /api/sessions/{sessionId}/gro… |
| 2026-09-24 17:17:09 | [CVE-2026-93284](https://nvd.nist.gov/vuln/detail/CVE-2026-93284) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/pagemap: dma-unmap pages before handling migrat… |
| 2026-09-24 17:17:09 | [CVE-2026-93285](https://nvd.nist.gov/vuln/detail/CVE-2026-93285) |  |  | In the Linux kernel, the following vulnerability has been resolved: f2fs: embed f2fs_gc_kthread in f2fs_sb_info Instead… |
| 2026-09-24 17:17:09 | [CVE-2026-93286](https://nvd.nist.gov/vuln/detail/CVE-2026-93286) |  |  | In the Linux kernel, the following vulnerability has been resolved: net: appletalk: fix NULL pointer dereference in aar… |
| 2026-09-24 17:17:09 | [CVE-2026-93287](https://nvd.nist.gov/vuln/detail/CVE-2026-93287) |  |  | In the Linux kernel, the following vulnerability has been resolved: i2c: smbus: reject oversized block transfers in the… |
| 2026-09-24 17:17:10 | [CVE-2026-93288](https://nvd.nist.gov/vuln/detail/CVE-2026-93288) |  |  | In the Linux kernel, the following vulnerability has been resolved: netfilter: nfnetlink_log: wait for rcu grace period… |
| 2026-09-24 17:17:10 | [CVE-2026-93542](https://nvd.nist.gov/vuln/detail/CVE-2026-93542) | Medium | 6.5 | An out-of-bounds read in libXi's XI2 class parsing via size_classes() and copy_classes() in libXi before 1.8.4 could be… |
| 2026-09-24 17:17:10 | [CVE-2026-93543](https://nvd.nist.gov/vuln/detail/CVE-2026-93543) | High | 7.4 | An out-of-bounds read in libXi's XI2 class parser in libXi before 1.8.4 could be used by malicious X servers to crash a… |
| 2026-09-24 17:17:10 | [CVE-2026-93544](https://nvd.nist.gov/vuln/detail/CVE-2026-93544) | Medium | 6.5 | An out-of-bounds read in libXi's XI2 XIQueryDevice reply parsing in libXi before 1.8.4 can be used by a malicious X ser… |
| 2026-09-24 17:17:10 | [CVE-2026-93545](https://nvd.nist.gov/vuln/detail/CVE-2026-93545) | Medium | 6.5 | An out-of-bounds read in libXi's XListInputDevices() in libXi before 1.8.4 could be used by malicious X servers to cras… |
| 2026-09-24 17:17:10 | [CVE-2026-93781](https://nvd.nist.gov/vuln/detail/CVE-2026-93781) |  |  | In the Linux kernel, the following vulnerability has been resolved: scsi: core: Do not block on tag allocation in scsi_… |
| 2026-09-24 17:17:10 | [CVE-2026-93782](https://nvd.nist.gov/vuln/detail/CVE-2026-93782) |  |  | In the Linux kernel, the following vulnerability has been resolved: vhost-scsi: flush backend after device ioctls vhost… |
| 2026-09-24 17:17:10 | [CVE-2026-93783](https://nvd.nist.gov/vuln/detail/CVE-2026-93783) |  |  | In the Linux kernel, the following vulnerability has been resolved: Bluetooth: RFCOMM: validate skb length in rfcomm_re… |
| 2026-09-24 17:17:11 | [CVE-2026-93784](https://nvd.nist.gov/vuln/detail/CVE-2026-93784) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: cfg80211: validate IEs in cfg80211_wext_siwge… |
| 2026-09-24 17:17:11 | [CVE-2026-93785](https://nvd.nist.gov/vuln/detail/CVE-2026-93785) |  |  | In the Linux kernel, the following vulnerability has been resolved: cifs: validate idmap key payload length The cifs.id… |
| 2026-09-24 17:17:11 | [CVE-2026-93786](https://nvd.nist.gov/vuln/detail/CVE-2026-93786) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: preserve VFS inherited POSIX ACL mask The VF… |
| 2026-09-24 17:17:11 | [CVE-2026-93787](https://nvd.nist.gov/vuln/detail/CVE-2026-93787) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: bound dirent name against end of SMB r… |
| 2026-09-24 17:17:11 | [CVE-2026-93788](https://nvd.nist.gov/vuln/detail/CVE-2026-93788) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: acpi: validate WGDS table revision i… |
| 2026-09-24 17:17:11 | [CVE-2026-93789](https://nvd.nist.gov/vuln/detail/CVE-2026-93789) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: bound aligned TLV advance in FW pars… |
| 2026-09-24 17:17:11 | [CVE-2026-93790](https://nvd.nist.gov/vuln/detail/CVE-2026-93790) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: mvm: fix out-of-bounds tid_data acce… |
| 2026-09-24 17:17:11 | [CVE-2026-93791](https://nvd.nist.gov/vuln/detail/CVE-2026-93791) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: mvm: add a check on the tid coming f… |
| 2026-09-24 17:17:11 | [CVE-2026-93792](https://nvd.nist.gov/vuln/detail/CVE-2026-93792) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: mvm: fix a possible underflow We sho… |
| 2026-09-24 17:17:12 | [CVE-2026-93793](https://nvd.nist.gov/vuln/detail/CVE-2026-93793) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: mvm: validate TX_CMD response layout… |
| 2026-09-24 17:17:12 | [CVE-2026-93794](https://nvd.nist.gov/vuln/detail/CVE-2026-93794) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb/client: flush dirty data before punching a hole… |
| 2026-09-24 17:17:12 | [CVE-2026-93795](https://nvd.nist.gov/vuln/detail/CVE-2026-93795) |  |  | In the Linux kernel, the following vulnerability has been resolved: blk-cgroup: fix leaks and online flag on radix_tree… |
| 2026-09-24 17:17:12 | [CVE-2026-93796](https://nvd.nist.gov/vuln/detail/CVE-2026-93796) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: pcie: null RX pointers after free Wh… |
| 2026-09-24 17:17:12 | [CVE-2026-93797](https://nvd.nist.gov/vuln/detail/CVE-2026-93797) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: mvm: fix an off-by-1 boundary check… |
| 2026-09-24 17:17:12 | [CVE-2026-93798](https://nvd.nist.gov/vuln/detail/CVE-2026-93798) |  |  | In the Linux kernel, the following vulnerability has been resolved: btrfs: fix reloc root cleanup in merge_reloc_roots(… |
| 2026-09-24 17:17:12 | [CVE-2026-93799](https://nvd.nist.gov/vuln/detail/CVE-2026-93799) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: mvm: validate sta_id in BA window st… |
| 2026-09-24 17:17:12 | [CVE-2026-93800](https://nvd.nist.gov/vuln/detail/CVE-2026-93800) |  |  | In the Linux kernel, the following vulnerability has been resolved: btrfs: fix use-after-free on reloc root after error… |
| 2026-09-24 17:17:13 | [CVE-2026-93801](https://nvd.nist.gov/vuln/detail/CVE-2026-93801) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb/client: zero-initialize stack-allocated cifs_op… |
| 2026-09-24 17:17:13 | [CVE-2026-93802](https://nvd.nist.gov/vuln/detail/CVE-2026-93802) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: rsi: validate beacon length before fixed buff… |
| 2026-09-24 17:17:13 | [CVE-2026-93803](https://nvd.nist.gov/vuln/detail/CVE-2026-93803) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: libipw: fix key index receive bound checks li… |
| 2026-09-24 17:17:13 | [CVE-2026-93804](https://nvd.nist.gov/vuln/detail/CVE-2026-93804) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: mac80211: ibss: wait for in-flight TX on disc… |
| 2026-09-24 17:17:13 | [CVE-2026-93805](https://nvd.nist.gov/vuln/detail/CVE-2026-93805) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: cfg80211: validate rx/tx MLME callback frame… |
| 2026-09-24 17:17:13 | [CVE-2026-93806](https://nvd.nist.gov/vuln/detail/CVE-2026-93806) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: cfg80211: validate assoc response length befo… |
| 2026-09-24 17:17:13 | [CVE-2026-93807](https://nvd.nist.gov/vuln/detail/CVE-2026-93807) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: rsi: avoid reading TKIP MIC keys for non-TKIP… |
| 2026-09-24 17:17:13 | [CVE-2026-93808](https://nvd.nist.gov/vuln/detail/CVE-2026-93808) |  |  | In the Linux kernel, the following vulnerability has been resolved: ALSA: usb-audio: caiaq: validate EP1 reply lengths… |
| 2026-09-24 17:17:13 | [CVE-2026-93809](https://nvd.nist.gov/vuln/detail/CVE-2026-93809) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdgpu: flush pending RCU callbacks on module u… |
| 2026-09-24 17:17:14 | [CVE-2026-93810](https://nvd.nist.gov/vuln/detail/CVE-2026-93810) |  |  | In the Linux kernel, the following vulnerability has been resolved: cachefiles: Fix double fput Fix a double fput() in… |
| 2026-09-24 17:17:14 | [CVE-2026-93811](https://nvd.nist.gov/vuln/detail/CVE-2026-93811) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: Fix acl.sd_buf memory leak and invalid sd_si… |
| 2026-09-24 17:17:14 | [CVE-2026-93812](https://nvd.nist.gov/vuln/detail/CVE-2026-93812) |  |  | In the Linux kernel, the following vulnerability has been resolved: ksmbd: fix sd_ndr.data memory leak in ksmbd_vfs_set… |
| 2026-09-24 17:17:14 | [CVE-2026-93813](https://nvd.nist.gov/vuln/detail/CVE-2026-93813) |  |  | In the Linux kernel, the following vulnerability has been resolved: btrfs: tree-checker: validate INODE_REF's namelen [… |
| 2026-09-24 17:17:14 | [CVE-2026-93814](https://nvd.nist.gov/vuln/detail/CVE-2026-93814) |  |  | In the Linux kernel, the following vulnerability has been resolved: spi: core: Abort active target transfer on controll… |
| 2026-09-24 17:17:15 | [CVE-2026-93815](https://nvd.nist.gov/vuln/detail/CVE-2026-93815) |  |  | In the Linux kernel, the following vulnerability has been resolved: net: au1000: move free_irq out of the close-time sp… |
| 2026-09-24 17:17:15 | [CVE-2026-93816](https://nvd.nist.gov/vuln/detail/CVE-2026-93816) |  |  | In the Linux kernel, the following vulnerability has been resolved: f2fs: validate inline dentry name lengths before co… |
| 2026-09-24 17:17:15 | [CVE-2026-93817](https://nvd.nist.gov/vuln/detail/CVE-2026-93817) |  |  | In the Linux kernel, the following vulnerability has been resolved: perf: Fix addr_filter_ranges lifetime Lee Jia Jie r… |
| 2026-09-24 17:17:15 | [CVE-2026-93818](https://nvd.nist.gov/vuln/detail/CVE-2026-93818) |  |  | In the Linux kernel, the following vulnerability has been resolved: PCI: plda: Protect root bus removal with rescan loc… |
| 2026-09-24 17:17:15 | [CVE-2026-93819](https://nvd.nist.gov/vuln/detail/CVE-2026-93819) |  |  | In the Linux kernel, the following vulnerability has been resolved: PCI: mediatek: Protect root bus removal with rescan… |
| 2026-09-24 17:17:15 | [CVE-2026-93820](https://nvd.nist.gov/vuln/detail/CVE-2026-93820) |  |  | In the Linux kernel, the following vulnerability has been resolved: PCI: rockchip: Protect root bus removal with rescan… |
| 2026-09-24 17:17:15 | [CVE-2026-93821](https://nvd.nist.gov/vuln/detail/CVE-2026-93821) |  |  | In the Linux kernel, the following vulnerability has been resolved: PCI: altera: Protect root bus removal with rescan l… |
| 2026-09-24 17:17:15 | [CVE-2026-93822](https://nvd.nist.gov/vuln/detail/CVE-2026-93822) |  |  | In the Linux kernel, the following vulnerability has been resolved: PCI: iproc: Protect root bus removal with rescan lo… |
| 2026-09-24 17:17:15 | [CVE-2026-93823](https://nvd.nist.gov/vuln/detail/CVE-2026-93823) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdkfd: Let driver decide buffer size at AMDKFD… |
| 2026-09-24 17:17:16 | [CVE-2026-93824](https://nvd.nist.gov/vuln/detail/CVE-2026-93824) |  |  | In the Linux kernel, the following vulnerability has been resolved: tls: reject the combination of TLS and sockmap TLS… |
| 2026-09-24 17:17:16 | [CVE-2026-93825](https://nvd.nist.gov/vuln/detail/CVE-2026-93825) |  |  | In the Linux kernel, the following vulnerability has been resolved: spi: Add NULL check for spi_get_device_id() in spi_… |
| 2026-09-24 17:17:16 | [CVE-2026-93826](https://nvd.nist.gov/vuln/detail/CVE-2026-93826) |  |  | In the Linux kernel, the following vulnerability has been resolved: HID: hidpp: fix potential UAF in hidpp_connect_even… |
| 2026-09-24 17:17:16 | [CVE-2026-93827](https://nvd.nist.gov/vuln/detail/CVE-2026-93827) |  |  | In the Linux kernel, the following vulnerability has been resolved: virtio-fs: avoid double-free on failed queue setup… |
| 2026-09-24 17:17:16 | [CVE-2026-93828](https://nvd.nist.gov/vuln/detail/CVE-2026-93828) |  |  | In the Linux kernel, the following vulnerability has been resolved: exfat: fix handling of damaged volume in exfat_crea… |
| 2026-09-24 17:17:16 | [CVE-2026-93829](https://nvd.nist.gov/vuln/detail/CVE-2026-93829) |  |  | In the Linux kernel, the following vulnerability has been resolved: smb: client: fix races in cifsd thread creation The… |
| 2026-09-24 17:17:16 | [CVE-2026-93830](https://nvd.nist.gov/vuln/detail/CVE-2026-93830) |  |  | In the Linux kernel, the following vulnerability has been resolved: net: stmmac: xgmac2: disable RBUE in default RX int… |
| 2026-09-24 17:17:16 | [CVE-2026-94281](https://nvd.nist.gov/vuln/detail/CVE-2026-94281) | Medium | 6.5 | An out-of-bounds read in libXi's XListInputDevices() class parsing in libXi before 1.8.4 could be used by malicious X s… |
| 2026-09-24 17:17:16 | [CVE-2026-94604](https://nvd.nist.gov/vuln/detail/CVE-2026-94604) |  |  | Rejected reason: This CVE is a duplicate of another CVE. |
| 2026-09-24 17:17:17 | [CVE-2026-94606](https://nvd.nist.gov/vuln/detail/CVE-2026-94606) | High | 8.9 | authentik is an open-source identity provider. Prior to 2026.2.7, 2026.5.7, and 2026.8.2, authentik email authenticator… |
| 2026-09-24 17:17:17 | [CVE-2026-94609](https://nvd.nist.gov/vuln/detail/CVE-2026-94609) | High | 8.8 | authentik is an open-source identity provider. Prior to 2026.2.7, 2026.5.7, and 2026.8.2, an account with delegated per… |
| 2026-09-24 17:17:17 | [CVE-2026-94611](https://nvd.nist.gov/vuln/detail/CVE-2026-94611) | High | 8.1 | authentik is an open-source identity provider. Prior to 2026.2.7, 2026.5.7, and 2026.8.2, authentik API serializers ret… |
| 2026-09-24 17:17:17 | [CVE-2026-94612](https://nvd.nist.gov/vuln/detail/CVE-2026-94612) | High | 7.4 | authentik is an open-source identity provider. Prior to 2026.2.7, 2026.5.7, and 2026.8.2, an authentik SAML Source veri… |
| 2026-09-24 17:17:17 | [CVE-2026-94613](https://nvd.nist.gov/vuln/detail/CVE-2026-94613) | High | 7.5 | authentik is an open-source identity provider. Prior to 2026.2.7, 2026.5.7, and 2026.8.2, an unauthenticated attacker c… |
| 2026-09-24 17:17:18 | [CVE-2026-97231](https://nvd.nist.gov/vuln/detail/CVE-2026-97231) | Medium | 5.5 | A vulnerability was found in volotat Anagnorisis up to 0.3.1/0.4.0. Affected is an unknown function of the file app.py… |
| 2026-09-24 17:17:18 | [CVE-2026-97407](https://nvd.nist.gov/vuln/detail/CVE-2026-97407) |  |  | In the Linux kernel, the following vulnerability has been resolved: ASoC: rockchip: rockchip_pdm: Handle runtime PM res… |
| 2026-09-24 17:17:18 | [CVE-2026-97408](https://nvd.nist.gov/vuln/detail/CVE-2026-97408) |  |  | In the Linux kernel, the following vulnerability has been resolved: Bluetooth: L2CAP: validate connectionless PSM lengt… |
| 2026-09-24 17:17:18 | [CVE-2026-97409](https://nvd.nist.gov/vuln/detail/CVE-2026-97409) |  |  | In the Linux kernel, the following vulnerability has been resolved: nvme-fc: Do not cancel requests in io target before… |
| 2026-09-24 17:17:18 | [CVE-2026-97410](https://nvd.nist.gov/vuln/detail/CVE-2026-97410) |  |  | In the Linux kernel, the following vulnerability has been resolved: netconsole: take target_cleanup_list_lock in drop_n… |
| 2026-09-24 17:17:18 | [CVE-2026-97411](https://nvd.nist.gov/vuln/detail/CVE-2026-97411) |  |  | In the Linux kernel, the following vulnerability has been resolved: net: ibm: emac: mal: fix potential system hang in m… |
| 2026-09-24 17:17:18 | [CVE-2026-97412](https://nvd.nist.gov/vuln/detail/CVE-2026-97412) |  |  | In the Linux kernel, the following vulnerability has been resolved: pds_core: quiesce DMA before freeing resources pdsc… |
| 2026-09-24 17:17:18 | [CVE-2026-97413](https://nvd.nist.gov/vuln/detail/CVE-2026-97413) |  |  | In the Linux kernel, the following vulnerability has been resolved: RDMA/rtrs-srv: Fix integer underflow in process_rea… |
| 2026-09-24 17:17:19 | [CVE-2026-97414](https://nvd.nist.gov/vuln/detail/CVE-2026-97414) |  |  | In the Linux kernel, the following vulnerability has been resolved: ASoC: mediatek: mt8365-afe-pcm: fix possible NULL-p… |
| 2026-09-24 17:17:19 | [CVE-2026-97415](https://nvd.nist.gov/vuln/detail/CVE-2026-97415) |  |  | In the Linux kernel, the following vulnerability has been resolved: btrfs: tree-checker: validate names in ROOT_REF and… |
| 2026-09-24 17:17:19 | [CVE-2026-97416](https://nvd.nist.gov/vuln/detail/CVE-2026-97416) |  |  | In the Linux kernel, the following vulnerability has been resolved: btrfs: balance: fix potential bg lookup failure in… |
| 2026-09-24 17:17:19 | [CVE-2026-97417](https://nvd.nist.gov/vuln/detail/CVE-2026-97417) |  |  | In the Linux kernel, the following vulnerability has been resolved: netfilter: nf_conntrack: use get_unaligned_be32() i… |
| 2026-09-24 17:17:19 | [CVE-2026-97418](https://nvd.nist.gov/vuln/detail/CVE-2026-97418) |  |  | In the Linux kernel, the following vulnerability has been resolved: ALSA: es18xx: check control allocation before priva… |
| 2026-09-24 17:17:19 | [CVE-2026-97419](https://nvd.nist.gov/vuln/detail/CVE-2026-97419) |  |  | In the Linux kernel, the following vulnerability has been resolved: hsr: broadcast netlink notifications in the device'… |
| 2026-09-24 17:17:19 | [CVE-2026-97420](https://nvd.nist.gov/vuln/detail/CVE-2026-97420) |  |  | In the Linux kernel, the following vulnerability has been resolved: bpf: NUL-terminate replaced sysctl value When writi… |
| 2026-09-24 17:17:19 | [CVE-2026-97421](https://nvd.nist.gov/vuln/detail/CVE-2026-97421) |  |  | In the Linux kernel, the following vulnerability has been resolved: RDMA/umem: Be careful about boundary conditions in… |
| 2026-09-24 17:17:20 | [CVE-2026-97422](https://nvd.nist.gov/vuln/detail/CVE-2026-97422) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdkfd: fix SMI event cross-process information… |
| 2026-09-24 17:17:20 | [CVE-2026-97423](https://nvd.nist.gov/vuln/detail/CVE-2026-97423) |  |  | In the Linux kernel, the following vulnerability has been resolved: cxl/region: Validate partition index before array a… |
| 2026-09-24 17:17:20 | [CVE-2026-97424](https://nvd.nist.gov/vuln/detail/CVE-2026-97424) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdgpu/ras: add ras_suspend callback and use it… |
| 2026-09-24 17:17:20 | [CVE-2026-97425](https://nvd.nist.gov/vuln/detail/CVE-2026-97425) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdgpu: fix buffer overflow during vBIOS update… |
| 2026-09-24 17:17:20 | [CVE-2026-97426](https://nvd.nist.gov/vuln/detail/CVE-2026-97426) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdgpu/pm: fix SmartShift bias sysfs store PM r… |
| 2026-09-24 17:17:20 | [CVE-2026-97427](https://nvd.nist.gov/vuln/detail/CVE-2026-97427) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amd/pm: bound pp_dpm_set_pp_table() memcpy The… |
| 2026-09-24 17:17:20 | [CVE-2026-97428](https://nvd.nist.gov/vuln/detail/CVE-2026-97428) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdgpu: harden FRU PIA parsing with bounded hel… |
| 2026-09-24 17:17:20 | [CVE-2026-97429](https://nvd.nist.gov/vuln/detail/CVE-2026-97429) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdkfd: fix UAF race in destroy_queue_cpsch wai… |
| 2026-09-24 17:17:21 | [CVE-2026-97430](https://nvd.nist.gov/vuln/detail/CVE-2026-97430) |  |  | In the Linux kernel, the following vulnerability has been resolved: xhci: Prevent queuing new commands if xhci is inacc… |
| 2026-09-24 17:17:21 | [CVE-2026-97431](https://nvd.nist.gov/vuln/detail/CVE-2026-97431) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amd/display: Avoid DPMS-on for phantom stream [… |
| 2026-09-24 17:17:21 | [CVE-2026-97432](https://nvd.nist.gov/vuln/detail/CVE-2026-97432) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: mvm: fix P2P-Device binding handling… |
| 2026-09-24 17:17:21 | [CVE-2026-97433](https://nvd.nist.gov/vuln/detail/CVE-2026-97433) |  |  | In the Linux kernel, the following vulnerability has been resolved: nvme: validate FDP configuration descriptor sizes V… |
| 2026-09-24 17:17:21 | [CVE-2026-97434](https://nvd.nist.gov/vuln/detail/CVE-2026-97434) |  |  | In the Linux kernel, the following vulnerability has been resolved: dpaa2-switch: fix handling of NAPI on the remove pa… |
| 2026-09-24 17:17:21 | [CVE-2026-97435](https://nvd.nist.gov/vuln/detail/CVE-2026-97435) |  |  | In the Linux kernel, the following vulnerability has been resolved: net: dsa: sja1105: flower: reject cross-chip redire… |
| 2026-09-24 17:17:21 | [CVE-2026-97436](https://nvd.nist.gov/vuln/detail/CVE-2026-97436) |  |  | In the Linux kernel, the following vulnerability has been resolved: dpaa2-switch: rework FDB management on the bridge l… |
| 2026-09-24 17:17:21 | [CVE-2026-97437](https://nvd.nist.gov/vuln/detail/CVE-2026-97437) |  |  | In the Linux kernel, the following vulnerability has been resolved: ntfs3: fix out-of-bounds read in ntfs_dir_emit() an… |
| 2026-09-24 17:17:21 | [CVE-2026-97438](https://nvd.nist.gov/vuln/detail/CVE-2026-97438) |  |  | In the Linux kernel, the following vulnerability has been resolved: fs/ntfs3: validate index entry key bounds [BUG] A m… |
| 2026-09-24 17:17:22 | [CVE-2026-97439](https://nvd.nist.gov/vuln/detail/CVE-2026-97439) |  |  | In the Linux kernel, the following vulnerability has been resolved: fs/ntfs3: preserve non-DOS attribute bits in system… |
| 2026-09-24 17:17:22 | [CVE-2026-97440](https://nvd.nist.gov/vuln/detail/CVE-2026-97440) |  |  | In the Linux kernel, the following vulnerability has been resolved: net: qrtr: fix node refcount leak on ctrl packet al… |
| 2026-09-24 17:17:22 | [CVE-2026-97441](https://nvd.nist.gov/vuln/detail/CVE-2026-97441) |  |  | In the Linux kernel, the following vulnerability has been resolved: ata: ahci: fail probe if BAR too small for claimed… |
| 2026-09-24 17:17:22 | [CVE-2026-97442](https://nvd.nist.gov/vuln/detail/CVE-2026-97442) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: ath11k: fix invalid data access in ath11k_dp_… |
| 2026-09-24 17:17:22 | [CVE-2026-97443](https://nvd.nist.gov/vuln/detail/CVE-2026-97443) |  |  | In the Linux kernel, the following vulnerability has been resolved: perf/ftrace: Fix WARNING in __unregister_ftrace_fun… |
| 2026-09-24 17:17:22 | [CVE-2026-97444](https://nvd.nist.gov/vuln/detail/CVE-2026-97444) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: add boundary checks in two places Add bound… |
| 2026-09-24 17:17:22 | [CVE-2026-97445](https://nvd.nist.gov/vuln/detail/CVE-2026-97445) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: Enhance buffer validation in acpi_ut_walk_a… |
| 2026-09-24 17:17:22 | [CVE-2026-97446](https://nvd.nist.gov/vuln/detail/CVE-2026-97446) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: Fix NULL pointer dereference in acpi_ns_cus… |
| 2026-09-24 17:17:22 | [CVE-2026-97447](https://nvd.nist.gov/vuln/detail/CVE-2026-97447) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: Enhance OEM ID and Table ID validation in a… |
| 2026-09-24 17:17:23 | [CVE-2026-97448](https://nvd.nist.gov/vuln/detail/CVE-2026-97448) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: Add validation for node in acpi_ns_build_no… |
| 2026-09-24 17:17:23 | [CVE-2026-97449](https://nvd.nist.gov/vuln/detail/CVE-2026-97449) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: Add package limit checks in parser function… |
| 2026-09-24 17:17:23 | [CVE-2026-97450](https://nvd.nist.gov/vuln/detail/CVE-2026-97450) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: validate handler object type in two places… |
| 2026-09-24 17:17:23 | [CVE-2026-97451](https://nvd.nist.gov/vuln/detail/CVE-2026-97451) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: Fix integer overflow in acpi_ex_opcode_3A_1… |
| 2026-09-24 17:17:23 | [CVE-2026-97452](https://nvd.nist.gov/vuln/detail/CVE-2026-97452) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: Prevent adding invalid references Prevent a… |
| 2026-09-24 17:17:23 | [CVE-2026-97453](https://nvd.nist.gov/vuln/detail/CVE-2026-97453) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: validate byte_count in acpi_ps_get_next_pac… |
| 2026-09-24 17:17:23 | [CVE-2026-97454](https://nvd.nist.gov/vuln/detail/CVE-2026-97454) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: add boundary checks in acpi_ps_get_next_fie… |
| 2026-09-24 17:17:23 | [CVE-2026-97455](https://nvd.nist.gov/vuln/detail/CVE-2026-97455) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: Fix use-after-free in acpi_ds_terminate_con… |
| 2026-09-24 17:17:24 | [CVE-2026-97456](https://nvd.nist.gov/vuln/detail/CVE-2026-97456) |  |  | In the Linux kernel, the following vulnerability has been resolved: ACPICA: Fix condition check in acpi_ps_parse_loop()… |
| 2026-09-24 17:17:24 | [CVE-2026-97472](https://nvd.nist.gov/vuln/detail/CVE-2026-97472) |  |  | In the Linux kernel, the following vulnerability has been resolved: ipv6: addrconf: fix temp address generation after p… |
| 2026-09-24 17:17:24 | [CVE-2026-97473](https://nvd.nist.gov/vuln/detail/CVE-2026-97473) |  |  | In the Linux kernel, the following vulnerability has been resolved: powercap: intel_rapl: Fix memory leak in rapl_add_p… |
| 2026-09-24 17:17:24 | [CVE-2026-97474](https://nvd.nist.gov/vuln/detail/CVE-2026-97474) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: iwlwifi: mld: purge async notifications upon… |
| 2026-09-24 17:17:24 | [CVE-2026-97475](https://nvd.nist.gov/vuln/detail/CVE-2026-97475) |  |  | In the Linux kernel, the following vulnerability has been resolved: thermal/drivers/tegra/soctherma: Switch to devm coo… |
| 2026-09-24 17:17:24 | [CVE-2026-97476](https://nvd.nist.gov/vuln/detail/CVE-2026-97476) |  |  | In the Linux kernel, the following vulnerability has been resolved: rds: filter RDS_INFO_* getsockopt by caller's netns… |
| 2026-09-24 17:17:25 | [CVE-2026-97477](https://nvd.nist.gov/vuln/detail/CVE-2026-97477) |  |  | In the Linux kernel, the following vulnerability has been resolved: RDMA/counter: Fix num_counters leak on bind_qp fail… |
| 2026-09-24 17:17:25 | [CVE-2026-97478](https://nvd.nist.gov/vuln/detail/CVE-2026-97478) |  |  | In the Linux kernel, the following vulnerability has been resolved: virt: acrn: Fix irqfd use-after-free during eventfd… |
| 2026-09-24 17:17:25 | [CVE-2026-97479](https://nvd.nist.gov/vuln/detail/CVE-2026-97479) |  |  | In the Linux kernel, the following vulnerability has been resolved: driver core: Avoid warning when removing a device w… |
| 2026-09-24 17:17:25 | [CVE-2026-97480](https://nvd.nist.gov/vuln/detail/CVE-2026-97480) |  |  | In the Linux kernel, the following vulnerability has been resolved: tty: serial: 8250: protect against NULL uart->port.… |
| 2026-09-24 17:17:25 | [CVE-2026-97481](https://nvd.nist.gov/vuln/detail/CVE-2026-97481) |  |  | In the Linux kernel, the following vulnerability has been resolved: serial: 8250: fix possible ISR soft lockup There ar… |
| 2026-09-24 17:17:25 | [CVE-2026-97482](https://nvd.nist.gov/vuln/detail/CVE-2026-97482) |  |  | In the Linux kernel, the following vulnerability has been resolved: usb: gadget: goku_udc: avoid NULL deref of dev->dri… |
| 2026-09-24 17:17:25 | [CVE-2026-97483](https://nvd.nist.gov/vuln/detail/CVE-2026-97483) |  |  | In the Linux kernel, the following vulnerability has been resolved: usb: core: hcd: fix possible deadlock in rh control… |
| 2026-09-24 17:17:25 | [CVE-2026-97484](https://nvd.nist.gov/vuln/detail/CVE-2026-97484) |  |  | In the Linux kernel, the following vulnerability has been resolved: usbip: vhci_hcd: fix NULL deref in status_show_vhci… |
| 2026-09-24 17:17:26 | [CVE-2026-97485](https://nvd.nist.gov/vuln/detail/CVE-2026-97485) |  |  | In the Linux kernel, the following vulnerability has been resolved: omfs: handle set_blocksize failures omfs uses buffe… |
| 2026-09-24 17:17:26 | [CVE-2026-97486](https://nvd.nist.gov/vuln/detail/CVE-2026-97486) |  |  | In the Linux kernel, the following vulnerability has been resolved: hpfs: handle set_blocksize failures hpfs uses buffe… |
| 2026-09-24 17:17:26 | [CVE-2026-97487](https://nvd.nist.gov/vuln/detail/CVE-2026-97487) |  |  | In the Linux kernel, the following vulnerability has been resolved: jfs: handle set_blocksize failures jfs uses buffer_… |
| 2026-09-24 17:17:26 | [CVE-2026-97488](https://nvd.nist.gov/vuln/detail/CVE-2026-97488) |  |  | In the Linux kernel, the following vulnerability has been resolved: qnx4: handle set_blocksize failures qnx4 uses buffe… |
| 2026-09-24 17:17:26 | [CVE-2026-97489](https://nvd.nist.gov/vuln/detail/CVE-2026-97489) |  |  | In the Linux kernel, the following vulnerability has been resolved: bfs: handle set_blocksize failures bfs uses buffer_… |
| 2026-09-24 17:17:26 | [CVE-2026-97490](https://nvd.nist.gov/vuln/detail/CVE-2026-97490) |  |  | In the Linux kernel, the following vulnerability has been resolved: affs: handle set_blocksize failures affs uses buffe… |
| 2026-09-24 17:17:26 | [CVE-2026-97491](https://nvd.nist.gov/vuln/detail/CVE-2026-97491) |  |  | In the Linux kernel, the following vulnerability has been resolved: net/rds: Don't sleep inside rds_ib_conn_path_shutdo… |
| 2026-09-24 17:17:26 | [CVE-2026-97492](https://nvd.nist.gov/vuln/detail/CVE-2026-97492) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: mac80211: don't call ieee80211_handle_reconfi… |
| 2026-09-24 17:17:26 | [CVE-2026-97493](https://nvd.nist.gov/vuln/detail/CVE-2026-97493) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdgpu: Bound GPIO I2C table entry count from V… |
| 2026-09-24 17:17:27 | [CVE-2026-97494](https://nvd.nist.gov/vuln/detail/CVE-2026-97494) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdgpu: validate and share PSP fw_pri_buf copie… |
| 2026-09-24 17:17:27 | [CVE-2026-97495](https://nvd.nist.gov/vuln/detail/CVE-2026-97495) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdkfd: Check bounds on allocate_doorbell alloc… |
| 2026-09-24 17:17:27 | [CVE-2026-97496](https://nvd.nist.gov/vuln/detail/CVE-2026-97496) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdkfd: Fix OOB memory exposure in get_wave_sta… |
| 2026-09-24 17:17:27 | [CVE-2026-97497](https://nvd.nist.gov/vuln/detail/CVE-2026-97497) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdkfd: Check bounds for allocate_sdma_queue re… |
| 2026-09-24 17:17:27 | [CVE-2026-97498](https://nvd.nist.gov/vuln/detail/CVE-2026-97498) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/amdgpu/userq: pin mqd and fw object bo to avoid… |
| 2026-09-24 17:17:27 | [CVE-2026-97499](https://nvd.nist.gov/vuln/detail/CVE-2026-97499) |  |  | In the Linux kernel, the following vulnerability has been resolved: coresight: perf: Retrieve path and source from even… |
| 2026-09-24 17:17:27 | [CVE-2026-97500](https://nvd.nist.gov/vuln/detail/CVE-2026-97500) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: rtw89: phy: check length before parsing PHY s… |
| 2026-09-24 17:17:27 | [CVE-2026-97501](https://nvd.nist.gov/vuln/detail/CVE-2026-97501) |  |  | In the Linux kernel, the following vulnerability has been resolved: pinctrl: mediatek: paris: bypass pinctrl GPIO layer… |
| 2026-09-24 17:17:27 | [CVE-2026-97502](https://nvd.nist.gov/vuln/detail/CVE-2026-97502) |  |  | In the Linux kernel, the following vulnerability has been resolved: mmc: davinci: avoid NULL deref of host->data in IRQ… |
| 2026-09-24 17:17:28 | [CVE-2026-97503](https://nvd.nist.gov/vuln/detail/CVE-2026-97503) |  |  | In the Linux kernel, the following vulnerability has been resolved: genirq/proc: Size interrupt directory names for 10-… |
| 2026-09-24 17:17:28 | [CVE-2026-97504](https://nvd.nist.gov/vuln/detail/CVE-2026-97504) |  |  | In the Linux kernel, the following vulnerability has been resolved: watchdog: lenovo_se10_wdt: Fix use-after-free and r… |
| 2026-09-24 17:17:28 | [CVE-2026-97505](https://nvd.nist.gov/vuln/detail/CVE-2026-97505) |  |  | In the Linux kernel, the following vulnerability has been resolved: PCI/sysfs: Add CAP_SYS_ADMIN check to __resource_re… |
| 2026-09-24 17:17:28 | [CVE-2026-97506](https://nvd.nist.gov/vuln/detail/CVE-2026-97506) |  |  | In the Linux kernel, the following vulnerability has been resolved: crypto: ixp4xx - fix buffer chain unwind on allocat… |
| 2026-09-24 17:17:28 | [CVE-2026-97507](https://nvd.nist.gov/vuln/detail/CVE-2026-97507) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: dm1105: fix missing error check for dma_allo… |
| 2026-09-24 17:17:28 | [CVE-2026-97508](https://nvd.nist.gov/vuln/detail/CVE-2026-97508) |  |  | In the Linux kernel, the following vulnerability has been resolved: thunderbolt: Set tb->root_switch to NULL when domai… |
| 2026-09-24 17:17:28 | [CVE-2026-97509](https://nvd.nist.gov/vuln/detail/CVE-2026-97509) |  |  | In the Linux kernel, the following vulnerability has been resolved: thunderbolt: Keep XDomain reference during the life… |
| 2026-09-24 17:17:28 | [CVE-2026-97510](https://nvd.nist.gov/vuln/detail/CVE-2026-97510) |  |  | In the Linux kernel, the following vulnerability has been resolved: thunderbolt: Release request if tb_cfg_request() fa… |
| 2026-09-24 17:17:28 | [CVE-2026-97511](https://nvd.nist.gov/vuln/detail/CVE-2026-97511) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: mac80211: avoid out-of-bounds access in monit… |
| 2026-09-24 17:17:29 | [CVE-2026-97512](https://nvd.nist.gov/vuln/detail/CVE-2026-97512) |  |  | In the Linux kernel, the following vulnerability has been resolved: spi: spi-qcom-qspi: Fix incomplete error handling i… |
| 2026-09-24 17:17:29 | [CVE-2026-97513](https://nvd.nist.gov/vuln/detail/CVE-2026-97513) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: chips-media: wave5: Release m2m_ctx after In… |
| 2026-09-24 17:17:29 | [CVE-2026-97514](https://nvd.nist.gov/vuln/detail/CVE-2026-97514) |  |  | In the Linux kernel, the following vulnerability has been resolved: media: chips-media: wave5: Fix Reports from Kernel… |
| 2026-09-24 17:17:29 | [CVE-2026-97515](https://nvd.nist.gov/vuln/detail/CVE-2026-97515) |  |  | In the Linux kernel, the following vulnerability has been resolved: i3c: master: svc: Prevent IRQ storm from false SLVS… |
| 2026-09-24 17:17:29 | [CVE-2026-97516](https://nvd.nist.gov/vuln/detail/CVE-2026-97516) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: rtw88: Add NULL check for chip->edcca_th in r… |
| 2026-09-24 17:17:29 | [CVE-2026-97517](https://nvd.nist.gov/vuln/detail/CVE-2026-97517) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: nl80211: reject beacons with bad HE operation… |
| 2026-09-24 17:17:29 | [CVE-2026-97518](https://nvd.nist.gov/vuln/detail/CVE-2026-97518) |  |  | In the Linux kernel, the following vulnerability has been resolved: wifi: cfg80211: reject duplicate wiphy cipher suite… |
| 2026-09-24 17:17:29 | [CVE-2026-97519](https://nvd.nist.gov/vuln/detail/CVE-2026-97519) |  |  | In the Linux kernel, the following vulnerability has been resolved: drm/xe: Fix null pointer dereference in devcoredump… |
| 2026-09-24 17:17:30 | [CVE-2026-97520](https://nvd.nist.gov/vuln/detail/CVE-2026-97520) |  |  | In the Linux kernel, the following vulnerability has been resolved: gfs2: move quota_init qc iterator increment Move qc… |
| 2026-09-24 17:17:30 | [CVE-2026-97521](https://nvd.nist.gov/vuln/detail/CVE-2026-97521) |  |  | In the Linux kernel, the following vulnerability has been resolved: gfs2: fix quota init duplicate scan gfs2_quota_init… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
