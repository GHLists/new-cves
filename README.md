# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-10 21:21 UTC

New CVEs published between 2026-11-10 20:18 UTC and 2026-11-10 21:21 UTC.

[Full CSV](data/new-cves-2026-11-10T21-21-54-207578Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-10 20:18:51 | [CVE-2026-120808](https://nvd.nist.gov/vuln/detail/CVE-2026-120808) | Critical | 9.1 | An issue exists in MongoDB's macOS TLS client implementation where certificate chain-of-trust validation is bypassed fo… |
| 2026-11-10 20:18:51 | [CVE-2026-120809](https://nvd.nist.gov/vuln/detail/CVE-2026-120809) | Medium | 6.1 | A use-after-free read issue exists in MongoDB’s SBE (Slot-Based Execution) engine when processing aggregation pipelines… |
| 2026-11-10 20:18:51 | [CVE-2026-120810](https://nvd.nist.gov/vuln/detail/CVE-2026-120810) | High | 7.1 | An issue in MongoDB server’s aggregation framework allows an authenticated user with read privileges to cause a denial… |
| 2026-11-10 20:18:51 | [CVE-2026-120811](https://nvd.nist.gov/vuln/detail/CVE-2026-120811) | Medium | 6.0 | A use-after-free issue exists in the MongoDB server’s classic query engine plan cache. Under certain query conditions,… |
| 2026-11-10 20:18:51 | [CVE-2026-120812](https://nvd.nist.gov/vuln/detail/CVE-2026-120812) | Medium | 6.0 | An issue in MongoDB Server's query processing component allows an authenticated user with read privileges to cause a de… |
| 2026-11-10 20:18:51 | [CVE-2026-120813](https://nvd.nist.gov/vuln/detail/CVE-2026-120813) | High | 8.2 | An issue in MongoDB Server's client-side field-level encryption (CSFLE) schema processing component allows encryption m… |
| 2026-11-10 20:18:52 | [CVE-2026-120814](https://nvd.nist.gov/vuln/detail/CVE-2026-120814) | High | 7.5 | An improper privilege management issue in the sharding subsystem of MongoDB Server may allow a user holding certain sha… |
| 2026-11-10 20:18:52 | [CVE-2026-120815](https://nvd.nist.gov/vuln/detail/CVE-2026-120815) | High | 8.6 | An incorrect authorization check in the MongoDB Server authorization subsystem may allow an unauthenticated party with… |
| 2026-11-10 20:18:52 | [CVE-2026-120974](https://nvd.nist.gov/vuln/detail/CVE-2026-120974) | Medium | 6.9 | On affected platforms running Arista EOS with IPsec AutoVPN Feature configured with dynamic paths, the configured IPsec… |
| 2026-11-10 20:18:52 | [CVE-2026-120975](https://nvd.nist.gov/vuln/detail/CVE-2026-120975) | Low | 2.0 | On affected platforms running Arista EOS with automatic certificate management configured and automatic Certificate Aut… |
| 2026-11-10 20:18:52 | [CVE-2026-120976](https://nvd.nist.gov/vuln/detail/CVE-2026-120976) | High | 7.0 | On affected platforms running Arista EOS with IEEE 802.1X authentication and MACsec using dynamically derived keys, sen… |
| 2026-11-10 20:18:52 | [CVE-2026-120977](https://nvd.nist.gov/vuln/detail/CVE-2026-120977) | High | 7.1 | On affected platforms running Arista EOS with 802.1X with Dynamic Host Configuration Protocol (DHCP) device profiling e… |
| 2026-11-10 20:18:52 | [CVE-2026-120978](https://nvd.nist.gov/vuln/detail/CVE-2026-120978) | Medium | 6.0 | On affected Arista EOS platforms running Border Gateway Protocol with Link State ( BGP-LS) and configured with the Dyna… |
| 2026-11-10 20:18:53 | [CVE-2026-120979](https://nvd.nist.gov/vuln/detail/CVE-2026-120979) | Medium | 6.1 | This vulnerability affects customers using Arista Pathfinder for WAN path selection with Border Gateway Protocol-Link S… |
| 2026-11-10 20:18:53 | [CVE-2026-120980](https://nvd.nist.gov/vuln/detail/CVE-2026-120980) | Medium | 6.0 | On affected platforms running Arista EOS with VPLS-BGP enabled, an attacker who has established a BGP session with the… |
| 2026-11-10 20:18:53 | [CVE-2026-120981](https://nvd.nist.gov/vuln/detail/CVE-2026-120981) | Medium | 6.0 | On affected platforms running Arista EOS with VPLS-BGP enabled, an attacker who has established a BGP session with the… |
| 2026-11-10 20:18:53 | [CVE-2026-120982](https://nvd.nist.gov/vuln/detail/CVE-2026-120982) | High | 8.7 | On affected platforms running Arista EOS with Border Gateway Protocol (BGP) configured, An unauthenticated attacker who… |
| 2026-11-10 20:18:53 | [CVE-2026-120983](https://nvd.nist.gov/vuln/detail/CVE-2026-120983) | Medium | 6.1 | On affected EOS platforms where 802.1x is configured in multi-host authenticated mode and the device is configured with… |
| 2026-11-10 20:18:53 | [CVE-2026-121286](https://nvd.nist.gov/vuln/detail/CVE-2026-121286) | Medium | 6.0 | On affected platforms running Arista EOS in multi-agent routing model with BGP Segment Routing Traffic Engineering (SR-… |
| 2026-11-10 20:18:53 | [CVE-2026-121287](https://nvd.nist.gov/vuln/detail/CVE-2026-121287) | High | 7.7 | An unauthenticated attacker on an adjacent network segment can send crafted RIPv2 packets to a RIP-enabled interface on… |
| 2026-11-10 20:18:54 | [CVE-2026-121288](https://nvd.nist.gov/vuln/detail/CVE-2026-121288) | Medium | 6.1 | An unauthenticated attacker on an adjacent network segment can bypass MD5 authentication and have unauthorized RIP rout… |
| 2026-11-10 20:18:54 | [CVE-2026-121289](https://nvd.nist.gov/vuln/detail/CVE-2026-121289) | Critical | 9.3 | On affected platforms running Arista EOS with BGP configured, a specially crafted packet can cause the BGP agent to cra… |
| 2026-11-10 20:18:54 | [CVE-2026-121290](https://nvd.nist.gov/vuln/detail/CVE-2026-121290) | High | 8.3 | On affected platforms running Arista EOS with Border Gateway Protocol (BGP) changing the BGP listen port from its defau… |
| 2026-11-10 20:18:54 | [CVE-2026-121291](https://nvd.nist.gov/vuln/detail/CVE-2026-121291) | High | 8.3 | A crafted Error Report can leave EOS stuck believing that a cache reset is in progress, preventing ROA publication, wit… |
| 2026-11-10 20:18:54 | [CVE-2026-121292](https://nvd.nist.gov/vuln/detail/CVE-2026-121292) | High | 8.3 | A malformed Error Report can cause EOS to read beyond packet boundaries, potentially terminating the RPKI agent or expo… |
| 2026-11-10 20:18:55 | [CVE-2026-121293](https://nvd.nist.gov/vuln/detail/CVE-2026-121293) | Medium | 6.9 | On affected EOS-based platforms, an attacker who controls a Border Gateway Protocol (BGP) peer can send a crafted BGP m… |
| 2026-11-10 20:18:55 | [CVE-2026-121294](https://nvd.nist.gov/vuln/detail/CVE-2026-121294) | Medium | 6.9 | On affected platforms running Arista EOS with a S-BFD reflector proxy configured, an unauthenticated attacker could sen… |
| 2026-11-10 20:18:55 | [CVE-2026-121295](https://nvd.nist.gov/vuln/detail/CVE-2026-121295) | Critical | 9.2 | On affected platforms running Arista EOS configured as S-BFD peers, an unauthenticated attacker could send a crafted S-… |
| 2026-11-10 20:18:55 | [CVE-2026-121367](https://nvd.nist.gov/vuln/detail/CVE-2026-121367) | Medium | 6.1 | On affected Arista EOS platforms with Routing Information Protocol version 2 (RIPv2) configured, under certain conditio… |
| 2026-11-10 20:18:56 | [CVE-2026-121368](https://nvd.nist.gov/vuln/detail/CVE-2026-121368) | High | 8.9 | On affected platforms running Arista EOS with Bidirectional Forwarding Detection (BFD) configured to use keyed MD5 or k… |
| 2026-11-10 20:18:56 | [CVE-2026-121369](https://nvd.nist.gov/vuln/detail/CVE-2026-121369) | Medium | 6.7 | On affected platforms running Arista EOS under specific link configurations an attacker with direct connectivity to the… |
| 2026-11-10 20:18:56 | [CVE-2026-121370](https://nvd.nist.gov/vuln/detail/CVE-2026-121370) | Critical | 9.2 | On affected platforms running Arista EOS with Precision Time Protocol (PTP) configured, an unauthenticated attacker wit… |
| 2026-11-10 20:18:56 | [CVE-2026-121371](https://nvd.nist.gov/vuln/detail/CVE-2026-121371) | High | 8.7 | On affected EOS versions with the eAPI service enabled, a specially crafted HTTP request can allow an unauthenticated,… |
| 2026-11-10 20:18:56 | [CVE-2026-121529](https://nvd.nist.gov/vuln/detail/CVE-2026-121529) | Critical | 9.6 | A origin validation error vulnerability in Fortinet FortiClientMac 7.4.0 through 7.4.7, FortiClientWindows 7.4.0 throug… |
| 2026-11-10 20:18:56 | [CVE-2026-121530](https://nvd.nist.gov/vuln/detail/CVE-2026-121530) | Medium | 6.6 | A improper authentication vulnerability in Fortinet FortiOS 7.6.0 through 7.6.6 may allow a remote authenticated attack… |
| 2026-11-10 20:19:04 | [CVE-2026-124016](https://nvd.nist.gov/vuln/detail/CVE-2026-124016) | Medium | 6.9 | postal-mime before 4.2.1 contains an algorithmic complexity denial of service vulnerability that allows unauthenticated… |
| 2026-11-10 20:19:07 | [CVE-2026-124848](https://nvd.nist.gov/vuln/detail/CVE-2026-124848) | Medium | 6.8 | Incorrect default file permissions in Kiro CLI (formerly Amazon Q Developer CLI) before version 2.27.0 on macOS and Lin… |
| 2026-11-10 20:19:08 | [CVE-2026-125337](https://nvd.nist.gov/vuln/detail/CVE-2026-125337) | High | 8.3 | Winter CMS is a content management system built on the Laravel PHP framework. Prior to 1.2.14, the ImportExportControll… |
| 2026-11-10 20:19:08 | [CVE-2026-125338](https://nvd.nist.gov/vuln/detail/CVE-2026-125338) | Medium | 4.5 | Winter CMS is a content management system built on the Laravel PHP framework. Prior to 1.2.14, BrandSetting::renderCss(… |
| 2026-11-10 20:19:08 | [CVE-2026-125339](https://nvd.nist.gov/vuln/detail/CVE-2026-125339) | Medium | 6.1 | Winter CMS is a content management system built on the Laravel PHP framework. From 1.0.319 until 1.2.14, Backend\Classe… |
| 2026-11-10 20:19:08 | [CVE-2026-125340](https://nvd.nist.gov/vuln/detail/CVE-2026-125340) | Medium | 4.5 | Winter CMS is a content management system built on the Laravel PHP framework. From 1.0.420 until 1.2.14, the backend Ta… |
| 2026-11-10 20:19:08 | [CVE-2026-125341](https://nvd.nist.gov/vuln/detail/CVE-2026-125341) | Low | 2.0 | Winter CMS is a content management system built on the Laravel PHP framework. From 1.1.0 until 1.2.14, Backend\Widgets\… |
| 2026-11-10 20:19:09 | [CVE-2026-126061](https://nvd.nist.gov/vuln/detail/CVE-2026-126061) | Medium | 4.3 | Winter CMS is a content management system built on the Laravel PHP framework. From 1.2.13 until 1.2.14, the Backend\Con… |
| 2026-11-10 20:19:10 | [CVE-2026-126062](https://nvd.nist.gov/vuln/detail/CVE-2026-126062) | Low | 3.7 | Nokogiri is an open source XML and HTML library for the Ruby programming language. Prior to 1.19.5, on JRuby, applicati… |
| 2026-11-10 20:19:10 | [CVE-2026-14447](https://nvd.nist.gov/vuln/detail/CVE-2026-14447) |  |  | In ext_mem_obj_get_page of memss-mfw.c, there is a possible way to return an out of bounds physical address via an off-… |
| 2026-11-10 20:19:11 | [CVE-2026-26248](https://nvd.nist.gov/vuln/detail/CVE-2026-26248) | High | 8.8 | A improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Fortinet FortiS… |
| 2026-11-10 20:19:12 | [CVE-2026-50077](https://nvd.nist.gov/vuln/detail/CVE-2026-50077) | High | 7.7 | Invalid Memory Access via the MSI-X table in QVM could allow an attacker in the guest to execute arbitrary code in the… |
| 2026-11-10 20:19:12 | [CVE-2026-50078](https://nvd.nist.gov/vuln/detail/CVE-2026-50078) | Medium | 4.4 | Out-Of-Bounds Read in the MSI-X table in the QVM could allow an attacker in the guest to cause an information disclosur… |
| 2026-11-10 20:19:12 | [CVE-2026-50079](https://nvd.nist.gov/vuln/detail/CVE-2026-50079) | Low | 3.3 | Time-of-check Time-of-use (TOCTOU) Race Condition in the virtio network virtual device could allow an attacker in the g… |
| 2026-11-10 20:19:12 | [CVE-2026-50080](https://nvd.nist.gov/vuln/detail/CVE-2026-50080) | Low | 3.3 | Stack-based Buffer Overflow in the ACPI event handler of the QVM could allow an attacker in a guest to crash the QVM by… |
| 2026-11-10 20:19:12 | [CVE-2026-55297](https://nvd.nist.gov/vuln/detail/CVE-2026-55297) |  |  | In handle_chan_msg of tipc_virtio_dev.c, there is a possible way to bypass memory tag access controls via concurrent sh… |
| 2026-11-10 20:19:12 | [CVE-2026-55309](https://nvd.nist.gov/vuln/detail/CVE-2026-55309) |  |  | In multiple functions of verifier.rs, there is a possible way to bypass secure boot signature verification via fault in… |
| 2026-11-10 20:19:12 | [CVE-2026-55311](https://nvd.nist.gov/vuln/detail/CVE-2026-55311) |  |  | In N/A of gdmc/gsp/project/gdmc.mk, there is a possible Logic error due to a logic error in the code. This could lead t… |
| 2026-11-10 20:19:13 | [CVE-2026-55312](https://nvd.nist.gov/vuln/detail/CVE-2026-55312) |  |  | In insert_node of remap.c, there is a possible way to trigger an out of bounds write in the address remapping table due… |
| 2026-11-10 20:19:13 | [CVE-2026-55316](https://nvd.nist.gov/vuln/detail/CVE-2026-55316) |  |  | In handle_dpm_image of seclib.rs, there is a possible Logic error due to a logic error in the code. This could lead to… |
| 2026-11-10 20:19:13 | [CVE-2026-55319](https://nvd.nist.gov/vuln/detail/CVE-2026-55319) |  |  | In thread_free of thread.c, there is a possible way to corrupt kernel heap metadata on thread creation failure due to m… |
| 2026-11-10 20:19:13 | [CVE-2026-55321](https://nvd.nist.gov/vuln/detail/CVE-2026-55321) |  |  | In parse_prime256v1 of keymint_asn1.c, there is a possible Heap Buffer Overflow due to a logic error in the code. This… |
| 2026-11-10 20:19:13 | [CVE-2026-55335](https://nvd.nist.gov/vuln/detail/CVE-2026-55335) |  |  | In multiple locations, there is a possible use-after-free due to a logic error in the code. This could lead to remote c… |
| 2026-11-10 20:19:13 | [CVE-2026-55344](https://nvd.nist.gov/vuln/detail/CVE-2026-55344) |  |  | In TzSharedMemory of TzSharedMemory.c, there is a possible Heap buffer overflow due to a logic error in the code. This… |
| 2026-11-10 20:19:13 | [CVE-2026-55346](https://nvd.nist.gov/vuln/detail/CVE-2026-55346) |  |  | In km_read_data_response of keymaster.c, there is a possible way to trigger an out of bounds write on the heap due to a… |
| 2026-11-10 20:19:13 | [CVE-2026-55348](https://nvd.nist.gov/vuln/detail/CVE-2026-55348) |  |  | In GetSharedMemory of trusty_shared_memory_manager.cc, there is a possible way to trigger an out of bounds read via sig… |
| 2026-11-10 20:19:13 | [CVE-2026-55360](https://nvd.nist.gov/vuln/detail/CVE-2026-55360) |  |  | In secure_transport_usecase_handshake of secure_transport.c, there is a possible way to bypass secure transport channel… |
| 2026-11-10 20:19:13 | [CVE-2026-55362](https://nvd.nist.gov/vuln/detail/CVE-2026-55362) |  |  | In multiple files, there is a possible out-of-bounds write due to a missing bounds check. This could lead to remote cod… |
| 2026-11-10 20:19:14 | [CVE-2026-56884](https://nvd.nist.gov/vuln/detail/CVE-2026-56884) |  |  | In ac_set_ns_ipa_tbl of plat_trusty.c, there is a possible way to corrupt stream table entry configurations via unvalid… |
| 2026-11-10 20:19:14 | [CVE-2026-56897](https://nvd.nist.gov/vuln/detail/CVE-2026-56897) |  |  | In multiple functions of attestation_object.c, there is a possible way to disclose uninitialized secure element stack m… |
| 2026-11-10 20:19:14 | [CVE-2026-56898](https://nvd.nist.gov/vuln/detail/CVE-2026-56898) |  |  | In aes256_cmac_sw of aes.rs, there is a possible way to forge message authentication codes over multi-block messages du… |
| 2026-11-10 20:19:14 | [CVE-2026-56902](https://nvd.nist.gov/vuln/detail/CVE-2026-56902) |  |  | In multiple locations, there is a possible information disclosure due to a logic error in the code. This could lead to… |
| 2026-11-10 20:19:14 | [CVE-2026-56909](https://nvd.nist.gov/vuln/detail/CVE-2026-56909) |  |  | In multiple functions of sswrp_cpm.dtsi, there is a possible way to modify voltage control registers from non-secure so… |
| 2026-11-10 20:19:14 | [CVE-2026-56910](https://nvd.nist.gov/vuln/detail/CVE-2026-56910) |  |  | In multiple locations, there is a possible way to trigger an out of bounds read and write in shared memory due to an in… |
| 2026-11-10 20:19:15 | [CVE-2026-56911](https://nvd.nist.gov/vuln/detail/CVE-2026-56911) |  |  | In handle_fips_hmac_req of hwcrypto_proxy.c, there is a possible heap buffer overflow due to missing bounds check. This… |
| 2026-11-10 20:19:15 | [CVE-2026-56912](https://nvd.nist.gov/vuln/detail/CVE-2026-56912) |  |  | In ac_remove_smmu_prot_internal of acfw_smmu.c, there is a possible Logic error due to a logic error in the code. This… |
| 2026-11-10 20:19:15 | [CVE-2026-56916](https://nvd.nist.gov/vuln/detail/CVE-2026-56916) |  |  | In _vqueue_get_avail_buf_locked of trusty/kernel/lib/trusty/vqueue.c, there is a possible Double-read / TOCTOU due to a… |
| 2026-11-10 20:19:15 | [CVE-2026-56919](https://nvd.nist.gov/vuln/detail/CVE-2026-56919) |  |  | In PackageSignatureChecker of SystemUIGoogleModule.java, there is a possible background activity launch due to a confus… |
| 2026-11-10 20:19:15 | [CVE-2026-56926](https://nvd.nist.gov/vuln/detail/CVE-2026-56926) |  |  | In multiple functions of PssSubscriptionManager.java, there is a possible way to spoof subscription switch results and… |
| 2026-11-10 20:19:15 | [CVE-2026-56929](https://nvd.nist.gov/vuln/detail/CVE-2026-56929) |  |  | In TrustyKeyMintManager::VerifyHat of trusty_keymint_manager.cc, there is a possible Security check bypass due to a log… |
| 2026-11-10 20:19:15 | [CVE-2026-56930](https://nvd.nist.gov/vuln/detail/CVE-2026-56930) |  |  | In smmu_find_ste of smmu.c, there is a possible way to retain stale translation lookaside buffer entries across stream… |
| 2026-11-10 20:19:15 | [CVE-2026-56933](https://nvd.nist.gov/vuln/detail/CVE-2026-56933) |  |  | In RecordApTx of efw_ap_transport.c, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This could… |
| 2026-11-10 20:19:15 | [CVE-2026-56934](https://nvd.nist.gov/vuln/detail/CVE-2026-56934) |  |  | In arm_lpae_split_blk_unmap of drivers/iommu/io-pgtable-arm-common.c, there is a possible Logic error due to a logic er… |
| 2026-11-10 20:19:16 | [CVE-2026-56935](https://nvd.nist.gov/vuln/detail/CVE-2026-56935) |  |  | In km_os_regen_salt of storage.c, there is a possible way to recover deleted keys due to a logic error. This could lead… |
| 2026-11-10 20:19:16 | [CVE-2026-56938](https://nvd.nist.gov/vuln/detail/CVE-2026-56938) |  |  | In port_shutdown of ipc.c, there is a possible Use After Free due to a race condition. This could lead to local escalat… |
| 2026-11-10 20:19:16 | [CVE-2026-56943](https://nvd.nist.gov/vuln/detail/CVE-2026-56943) |  |  | In multiple locations, there is a possible way to trigger an out of bounds read via an attestation comparison oracle du… |
| 2026-11-10 20:19:16 | [CVE-2026-56944](https://nvd.nist.gov/vuln/detail/CVE-2026-56944) |  |  | In smmu_detach_dev of private/google-modules/iommu/arm-smmu-v3/drivers/iommu/arm/arm-smmu-v3/pkvm/arm-smmu-v3.c, there… |
| 2026-11-10 20:19:16 | [CVE-2026-56946](https://nvd.nist.gov/vuln/detail/CVE-2026-56946) |  |  | In smmu_unmap_visit_leaf of arm-smmu-v3.c, there is a possible way to release active direct memory access page referenc… |
| 2026-11-10 20:19:16 | [CVE-2026-56947](https://nvd.nist.gov/vuln/detail/CVE-2026-56947) |  |  | In getCarrierRestrictionStatus of PhoneInterfaceManager.java, there is a possible permission bypass due to a confused d… |
| 2026-11-10 20:19:16 | [CVE-2026-56949](https://nvd.nist.gov/vuln/detail/CVE-2026-56949) |  |  | In multiple locations, there is a possible way to modify authenticated coprocessor firmware in shared memory before loa… |
| 2026-11-10 20:19:16 | [CVE-2026-56951](https://nvd.nist.gov/vuln/detail/CVE-2026-56951) |  |  | In on_vkUpdateDescriptorSetWithTemplateSized2GOOGLE of vk_decoder_global_state.cpp, there is a possible way to leak hos… |
| 2026-11-10 20:19:17 | [CVE-2026-56956](https://nvd.nist.gov/vuln/detail/CVE-2026-56956) |  |  | In EncodeT140 of TextRtpPayloadEncoderNode.cpp, there is a possible Heap Buffer Overflow due to a logic error in the co… |
| 2026-11-10 20:19:17 | [CVE-2026-56966](https://nvd.nist.gov/vuln/detail/CVE-2026-56966) |  |  | In CommitToBuffer of hal_override_options.bundle.cc, there is a possible way to retain stale direct memory access mappi… |
| 2026-11-10 20:19:17 | [CVE-2026-56969](https://nvd.nist.gov/vuln/detail/CVE-2026-56969) |  |  | In edgetpu_group_clear_responses of edgetpu_group.c, there is a possible Use After Free due to a logic error in the cod… |
| 2026-11-10 20:19:17 | [CVE-2026-56971](https://nvd.nist.gov/vuln/detail/CVE-2026-56971) |  |  | In AudioSession::SendInternalEvent of AudioSession.cpp, there is a possible Double Free due to a logic error in the cod… |
| 2026-11-10 20:19:17 | [CVE-2026-56980](https://nvd.nist.gov/vuln/detail/CVE-2026-56980) |  |  | In createDataFlowAsync of data_flow_manager.cc, there is a possible way to trigger an out of bounds write in shared mem… |
| 2026-11-10 20:19:17 | [CVE-2026-56995](https://nvd.nist.gov/vuln/detail/CVE-2026-56995) |  |  | In multiple locations, there is a possible way to corrupt host allocator metadata in shared memory due to memory corrup… |
| 2026-11-10 20:19:17 | [CVE-2026-57004](https://nvd.nist.gov/vuln/detail/CVE-2026-57004) |  |  | In PresenceDecoderV1::DecodeDataElements of presence_decoder_v1.cc, there is a possible out-of-bounds write due to a mi… |
| 2026-11-10 20:19:17 | [CVE-2026-57005](https://nvd.nist.gov/vuln/detail/CVE-2026-57005) |  |  | In EuiccPort.buildUiccAccessRule of EuiccPort.java, there is a possible Confused Deputy due to a confused deputy. This… |
| 2026-11-10 20:19:17 | [CVE-2026-57009](https://nvd.nist.gov/vuln/detail/CVE-2026-57009) |  |  | In GC2AvcDec of GC2AvcDec.cpp, there is a possible Logic error due to a logic error in the code. This could lead to loc… |
| 2026-11-10 20:19:17 | [CVE-2026-57010](https://nvd.nist.gov/vuln/detail/CVE-2026-57010) |  |  | In EncodeLastScanBufferElement of data_manager.cc, there is a possible out-of-bounds write due to a logic error in the… |
| 2026-11-10 20:19:18 | [CVE-2026-57013](https://nvd.nist.gov/vuln/detail/CVE-2026-57013) |  |  | In access_control_enable of multiple files, there is a possible way to release secure coprocessors from reset via uncla… |
| 2026-11-10 20:19:18 | [CVE-2026-57036](https://nvd.nist.gov/vuln/detail/CVE-2026-57036) |  |  | In send_vdu_directive of gdmc/gsp/dev/bmsm/plat/lga/vdu.c, there is a possible Logic error due to a logic error in the… |
| 2026-11-10 20:19:18 | [CVE-2026-57037](https://nvd.nist.gov/vuln/detail/CVE-2026-57037) |  |  | In getChppAppState of chpp_init.cc, there is a possible way to trigger an out of bounds read and corrupt task control s… |
| 2026-11-10 20:19:18 | [CVE-2026-57043](https://nvd.nist.gov/vuln/detail/CVE-2026-57043) |  |  | In tipc_dev_probe of tipc_virtio_dev.c, there is a possible way to corrupt memory via an off-by-one cleanup loop on pro… |
| 2026-11-10 20:19:18 | [CVE-2026-57047](https://nvd.nist.gov/vuln/detail/CVE-2026-57047) |  |  | In __mfc_core_nal_q_get_dec_metadata_sei_nal of mfc_core_nal_q.c, there is a possible out-of-bounds write due to a miss… |
| 2026-11-10 20:19:18 | [CVE-2026-57048](https://nvd.nist.gov/vuln/detail/CVE-2026-57048) |  |  | In authenticate of verify_image, there is a possible Signature verification logic bypass due to a logic error in the co… |
| 2026-11-10 20:19:22 | [CVE-2026-58677](https://nvd.nist.gov/vuln/detail/CVE-2026-58677) |  |  | In get_secure_boot_mode of auth.rs, there is a possible way to bypass root signature verification via fault injection d… |
| 2026-11-10 20:19:23 | [CVE-2026-58680](https://nvd.nist.gov/vuln/detail/CVE-2026-58680) |  |  | In cpm_mbox_power_ctrl_sswrp of cpm_mbox.c, there is a possible permission bypass due to a precondition check failure.… |
| 2026-11-10 20:19:23 | [CVE-2026-58681](https://nvd.nist.gov/vuln/detail/CVE-2026-58681) |  |  | In multiple locations, there is a possible out-of-bounds write due to an integer overflow. This could lead to remote co… |
| 2026-11-10 20:19:23 | [CVE-2026-58684](https://nvd.nist.gov/vuln/detail/CVE-2026-58684) |  |  | In smmu_config_l3tt of smmu.c, there is a possible permission bypass due to a logic error in the code. This could lead… |
| 2026-11-10 20:19:23 | [CVE-2026-58690](https://nvd.nist.gov/vuln/detail/CVE-2026-58690) |  |  | In multiple functions of bitmap_image_buffer.h, there is a possible way to trigger an out of bounds write on the truste… |
| 2026-11-10 20:19:23 | [CVE-2026-58696](https://nvd.nist.gov/vuln/detail/CVE-2026-58696) |  |  | In multiple locations, there is a possible out-of-bounds write due to a heap buffer overflow. This could lead to local… |
| 2026-11-10 20:19:23 | [CVE-2026-58697](https://nvd.nist.gov/vuln/detail/CVE-2026-58697) |  |  | In codec3p_secure of codec3p_secure, there is a possible Heap Buffer Overflow due to a missing bounds check. This could… |
| 2026-11-10 20:19:23 | [CVE-2026-58702](https://nvd.nist.gov/vuln/detail/CVE-2026-58702) |  |  | In createIntent of TimerAgent.java, there is a possible permission bypass due to a confused deputy. This could lead to… |
| 2026-11-10 20:19:23 | [CVE-2026-58705](https://nvd.nist.gov/vuln/detail/CVE-2026-58705) |  |  | In handleEvent of gscan.cpp, there is a possible way to trigger an out of bounds write on the heap due to a missing bou… |
| 2026-11-10 20:19:24 | [CVE-2026-58722](https://nvd.nist.gov/vuln/detail/CVE-2026-58722) |  |  | In chppProcessDiscoverAllResponse of system/chre/chpp/clients/discovery.c, there is a possible Heap Buffer Overflow due… |
| 2026-11-10 20:19:24 | [CVE-2026-58729](https://nvd.nist.gov/vuln/detail/CVE-2026-58729) |  |  | In multiple files, there is a possible out-of-bounds write due to a missing bounds check. This could lead to local esca… |
| 2026-11-10 20:19:24 | [CVE-2026-58736](https://nvd.nist.gov/vuln/detail/CVE-2026-58736) |  |  | In NotifySipResponse of SessionEx.cpp, there is a possible way to corrupt memory via a dangling connection pointer in t… |
| 2026-11-10 20:19:24 | [CVE-2026-58740](https://nvd.nist.gov/vuln/detail/CVE-2026-58740) |  |  | In BitmapImageBuffer of bitmap_image_buffer.h, there is a possible out-of-bounds write due to an integer overflow. This… |
| 2026-11-10 20:19:24 | [CVE-2026-58752](https://nvd.nist.gov/vuln/detail/CVE-2026-58752) |  |  | In aoc_unlocked_ioctl_handle_ion_fd of aoc.c, there is a possible type confusion due to improper input validation. This… |
| 2026-11-10 20:19:24 | [CVE-2026-58757](https://nvd.nist.gov/vuln/detail/CVE-2026-58757) |  |  | In mfc_alloc_enc_roi_buffer of mfc_buf.c, there is a possible out-of-bounds write due to a heap buffer overflow. This c… |
| 2026-11-10 20:19:24 | [CVE-2026-58762](https://nvd.nist.gov/vuln/detail/CVE-2026-58762) |  |  | In ac_get_prot_config of plat_trusty.c, there is a possible memory corruption due to improper input validation. This co… |
| 2026-11-10 20:19:25 | [CVE-2026-58769](https://nvd.nist.gov/vuln/detail/CVE-2026-58769) |  |  | In multiple locations, there is a possible out-of-bounds read due to a missing bounds check. This could lead to local i… |
| 2026-11-10 20:19:25 | [CVE-2026-58778](https://nvd.nist.gov/vuln/detail/CVE-2026-58778) |  |  | In multiple locations, there is a possible use-after-free due to a race condition. This could lead to local escalation… |
| 2026-11-10 20:19:25 | [CVE-2026-58779](https://nvd.nist.gov/vuln/detail/CVE-2026-58779) |  |  | In multiple locations, there is a possible permission bypass due to a logic error in the code. This could lead to local… |
| 2026-11-10 20:19:25 | [CVE-2026-58780](https://nvd.nist.gov/vuln/detail/CVE-2026-58780) |  |  | In multiple locations, there is a possible out-of-bounds write due to an incorrect bounds check. This could lead to rem… |
| 2026-11-10 20:19:25 | [CVE-2026-58781](https://nvd.nist.gov/vuln/detail/CVE-2026-58781) |  |  | In HostLinkBase::chreIpiHandler of host_link.cc, there is a possible out-of-bounds write due to a missing bounds check.… |
| 2026-11-10 20:19:25 | [CVE-2026-58782](https://nvd.nist.gov/vuln/detail/CVE-2026-58782) |  |  | In multiple locations, there is a possible denial of service due to a logic error in the code. This could lead to local… |
| 2026-11-10 20:19:25 | [CVE-2026-58783](https://nvd.nist.gov/vuln/detail/CVE-2026-58783) |  |  | In multiple locations, there is a possible denial of service due to a logic error in the code. This could lead to local… |
| 2026-11-10 20:19:25 | [CVE-2026-58785](https://nvd.nist.gov/vuln/detail/CVE-2026-58785) |  |  | In update_user_consent of main.rs, there is a possible elevation of privilege due to uninitialized data. This could lea… |
| 2026-11-10 20:19:25 | [CVE-2026-58786](https://nvd.nist.gov/vuln/detail/CVE-2026-58786) |  |  | In cnm_memset of hevc_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This could lead t… |
| 2026-11-10 20:19:26 | [CVE-2026-58787](https://nvd.nist.gov/vuln/detail/CVE-2026-58787) |  |  | In chppWifiRangingEventNotification of clients/wifi.c, there is a possible Heap Buffer Overflow due to a logic error in… |
| 2026-11-10 20:19:26 | [CVE-2026-58788](https://nvd.nist.gov/vuln/detail/CVE-2026-58788) |  |  | In stpropnci_process_std of stpropnci_std.cc, there is a possible way to trigger an out of bounds write into global sta… |
| 2026-11-10 20:19:26 | [CVE-2026-58789](https://nvd.nist.gov/vuln/detail/CVE-2026-58789) |  |  | In s_gen_tile_param of multiple files, there is a possible way to trigger an out of bounds write in tile parameter arra… |
| 2026-11-10 20:19:26 | [CVE-2026-58790](https://nvd.nist.gov/vuln/detail/CVE-2026-58790) |  |  | In CMD_ENC_SET_PARAM of encoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This could lead… |
| 2026-11-10 20:19:26 | [CVE-2026-58791](https://nvd.nist.gov/vuln/detail/CVE-2026-58791) |  |  | In pic_timing of hevc_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This could lead t… |
| 2026-11-10 20:19:26 | [CVE-2026-58796](https://nvd.nist.gov/vuln/detail/CVE-2026-58796) |  |  | In multiple functions of AndroidManifest.xml, there is a possible way to trigger unauthorized firmware updates via expo… |
| 2026-11-10 20:19:26 | [CVE-2026-58797](https://nvd.nist.gov/vuln/detail/CVE-2026-58797) |  |  | In register_dump_dpa of sswrp_pcie.c, there is a possible Logic error due to a logic error in the code. This could lead… |
| 2026-11-10 20:19:26 | [CVE-2026-58798](https://nvd.nist.gov/vuln/detail/CVE-2026-58798) |  |  | In multiple functions of cn_Tai.cpp, there is a possible way to trigger an out of bounds write due to memory corruption… |
| 2026-11-10 20:19:26 | [CVE-2026-58799](https://nvd.nist.gov/vuln/detail/CVE-2026-58799) |  |  | In multiple functions of rmmi_utility.c, there is a possible way to trigger an out of bounds write due to a missing bou… |
| 2026-11-10 20:19:27 | [CVE-2026-58800](https://nvd.nist.gov/vuln/detail/CVE-2026-58800) |  |  | In IMG_vkCreateImageView of image_view.c, there is a possible way to trigger a use after free due to memory corruption.… |
| 2026-11-10 20:19:27 | [CVE-2026-58801](https://nvd.nist.gov/vuln/detail/CVE-2026-58801) |  |  | In smmu_domain_config_s1 of arm-smmu-v3.c, there is a possible way to access stale stream table entries across reassign… |
| 2026-11-10 20:19:27 | [CVE-2026-58803](https://nvd.nist.gov/vuln/detail/CVE-2026-58803) |  |  | In bytes_are_equal of lib.rs, there is a possible way to recover authentication keys due to side channel information di… |
| 2026-11-10 20:19:27 | [CVE-2026-58804](https://nvd.nist.gov/vuln/detail/CVE-2026-58804) |  |  | In ExecuteGraphCommand of multiple files, there is a possible way to trigger an out of bounds write via an oversized sc… |
| 2026-11-10 20:19:27 | [CVE-2026-58805](https://nvd.nist.gov/vuln/detail/CVE-2026-58805) |  |  | In multiple locations, there is a possible way to zero arbitrary secure memory via unvalidated image body addresses due… |
| 2026-11-10 20:19:27 | [CVE-2026-58806](https://nvd.nist.gov/vuln/detail/CVE-2026-58806) |  |  | In get_sswrp_state of cpm_mbox_srv/main.c, there is a possible Logic error due to a logic error in the code. This could… |
| 2026-11-10 20:19:27 | [CVE-2026-58807](https://nvd.nist.gov/vuln/detail/CVE-2026-58807) |  |  | In Retry_MtsMessageInPending of MtsMessageController.cpp, there is a possible way to trigger memory exhaustion via leak… |
| 2026-11-10 20:19:27 | [CVE-2026-58808](https://nvd.nist.gov/vuln/detail/CVE-2026-58808) |  |  | In multiple locations, there is a possible way to dump secure cache lines into non-secure memory on warm reset due to a… |
| 2026-11-10 20:19:27 | [CVE-2026-58809](https://nvd.nist.gov/vuln/detail/CVE-2026-58809) |  |  | In smmu_domain_config_s1 of arm-smmu-v3.c, there is a possible OOB Write due to a missing bounds check. This could lead… |
| 2026-11-10 20:19:28 | [CVE-2026-58810](https://nvd.nist.gov/vuln/detail/CVE-2026-58810) |  |  | In multiple functions of simd_ctx.c, there is a possible way to disclose secure vector predicate and fault registers to… |
| 2026-11-10 20:19:28 | [CVE-2026-58811](https://nvd.nist.gov/vuln/detail/CVE-2026-58811) |  |  | In smmu_get_mair_idx of smmu.c, there is a possible way to apply incorrect memory attributes to direct memory access ma… |
| 2026-11-10 20:19:28 | [CVE-2026-58812](https://nvd.nist.gov/vuln/detail/CVE-2026-58812) |  |  | In decode of fw_vp9_dec_pic.c, there is a possible Logic error due to a logic error in the code. This could lead to loc… |
| 2026-11-10 20:19:28 | [CVE-2026-58813](https://nvd.nist.gov/vuln/detail/CVE-2026-58813) |  |  | In mmap of mman.c, there is a possible way to trigger an out of bounds read and write via mapping size truncation due t… |
| 2026-11-10 20:19:28 | [CVE-2026-59573](https://nvd.nist.gov/vuln/detail/CVE-2026-59573) |  |  | In max_num_ref_frames of avc_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This could… |
| 2026-11-10 20:19:28 | [CVE-2026-59574](https://nvd.nist.gov/vuln/detail/CVE-2026-59574) |  |  | In notifyPollingLoopFrames of hal_fwlog.cc, there is a possible way to trigger an out of bounds read and write when for… |
| 2026-11-10 20:19:28 | [CVE-2026-59575](https://nvd.nist.gov/vuln/detail/CVE-2026-59575) |  |  | In stpropnci_cb_observe_mode_suspend of stpropnci_prop_android.cc, there is a possible way to trigger an out of bounds… |
| 2026-11-10 20:19:28 | [CVE-2026-59578](https://nvd.nist.gov/vuln/detail/CVE-2026-59578) |  |  | In s_check_valid_tile_param_custom_tile of av1_encoder, there is a possible Non-Heap Buffer Overflow due to a buffer ov… |
| 2026-11-10 20:19:29 | [CVE-2026-59579](https://nvd.nist.gov/vuln/detail/CVE-2026-59579) |  |  | In getUserDataPayload of GC2UserData.cpp, there is a possible Logic error due to a logic error in the code. This could… |
| 2026-11-10 20:19:29 | [CVE-2026-59580](https://nvd.nist.gov/vuln/detail/CVE-2026-59580) |  |  | In trusty_context_switch of services/spd/trusty/trusty.c, there is a possible Secure world register state leak due to a… |
| 2026-11-10 20:19:29 | [CVE-2026-59582](https://nvd.nist.gov/vuln/detail/CVE-2026-59582) |  |  | In StartTimer of UcePublishManager.cpp, there is a possible way to trigger a process abort during timer calculation due… |
| 2026-11-10 20:19:29 | [CVE-2026-59583](https://nvd.nist.gov/vuln/detail/CVE-2026-59583) |  |  | In FormCredentials of SipAuHelper.cpp, there is a possible way to disclose authentication credentials in cleartext via… |
| 2026-11-10 20:19:29 | [CVE-2026-59585](https://nvd.nist.gov/vuln/detail/CVE-2026-59585) |  |  | In SetDisplayName of RegInfoContact.cpp, there is a possible denial of service due to a missing null check. This could… |
| 2026-11-10 20:19:29 | [CVE-2026-59586](https://nvd.nist.gov/vuln/detail/CVE-2026-59586) |  |  | In multiple locations, there is a possible way to recover cryptographic keys and forge authentication tags due to impro… |
| 2026-11-10 20:19:29 | [CVE-2026-59587](https://nvd.nist.gov/vuln/detail/CVE-2026-59587) |  |  | In stpropnci_prop_st_build_set_custom_polling_cmd of stpropnci_prop_st.cc, there is a possible way to trigger an out of… |
| 2026-11-10 20:19:29 | [CVE-2026-59589](https://nvd.nist.gov/vuln/detail/CVE-2026-59589) |  |  | In s_av1_dec_metadata_scalability of av1_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow… |
| 2026-11-10 20:19:29 | [CVE-2026-59593](https://nvd.nist.gov/vuln/detail/CVE-2026-59593) |  |  | In tile_info of av1_decoder, there is a possible Heap Buffer Overflow due to a heap buffer overflow. This could lead to… |
| 2026-11-10 20:19:30 | [CVE-2026-59594](https://nvd.nist.gov/vuln/detail/CVE-2026-59594) |  |  | In spm_alloc of encoder, there is a possible Heap Buffer Overflow due to a heap buffer overflow. This could lead to loc… |
| 2026-11-10 20:19:30 | [CVE-2026-59595](https://nvd.nist.gov/vuln/detail/CVE-2026-59595) |  |  | In DecodeHeaderComponent of SipStack.cpp, there is a possible way to trigger stack exhaustion via unbounded mutual recu… |
| 2026-11-10 20:19:30 | [CVE-2026-59596](https://nvd.nist.gov/vuln/detail/CVE-2026-59596) |  |  | In multiple functions of mpu.c, there is a possible way to execute code from non-secure memory in the security coproces… |
| 2026-11-10 20:19:30 | [CVE-2026-59597](https://nvd.nist.gov/vuln/detail/CVE-2026-59597) |  |  | In bindDataService of DataServiceManager.java, there is a possible way to retain privileged tunnel management permissio… |
| 2026-11-10 20:19:30 | [CVE-2026-59598](https://nvd.nist.gov/vuln/detail/CVE-2026-59598) |  |  | In platform_rio_ncp_wdt_handler of edgetpu_rio.c, there is a possible Use After Free due to a use after free. This coul… |
| 2026-11-10 20:19:30 | [CVE-2026-59599](https://nvd.nist.gov/vuln/detail/CVE-2026-59599) |  |  | Android on supported Pixel devices before security patch level 2026-11-05 allows elevation of privilege in the hypervis… |
| 2026-11-10 20:19:30 | [CVE-2026-59601](https://nvd.nist.gov/vuln/detail/CVE-2026-59601) |  |  | In CalculateSampleRate of cldma_alcedo.cc, there is a possible Heap Buffer Overflow due to a logic error in the code. T… |
| 2026-11-10 20:19:30 | [CVE-2026-59603](https://nvd.nist.gov/vuln/detail/CVE-2026-59603) |  |  | In RespondReceivedMessage of MtsMessageController.cpp, there is a possible way to trigger a double free and process abo… |
| 2026-11-10 20:19:30 | [CVE-2026-59604](https://nvd.nist.gov/vuln/detail/CVE-2026-59604) |  |  | In multiple locations, there is a possible way to trigger an unbounded loop in video decoder firmware due to a logic er… |
| 2026-11-10 20:19:30 | [CVE-2026-59606](https://nvd.nist.gov/vuln/detail/CVE-2026-59606) |  |  | In multiple functions of sswrp_cpm.dtsi, there is a possible way to modify global reset registers from non-secure softw… |
| 2026-11-10 20:19:31 | [CVE-2026-59607](https://nvd.nist.gov/vuln/detail/CVE-2026-59607) |  |  | In TzPipelineInputExtractor of TzPipelineInputExtractor.cpp, there is a possible Logic check bypass due to a logic erro… |
| 2026-11-10 20:19:31 | [CVE-2026-59608](https://nvd.nist.gov/vuln/detail/CVE-2026-59608) |  |  | In tone_mapping_info of hevc_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This could… |
| 2026-11-10 20:19:31 | [CVE-2026-59609](https://nvd.nist.gov/vuln/detail/CVE-2026-59609) |  |  | In fence_manager_extract_iif of fence_manager.c, there is a possible way to corrupt kernel memory via fence identifier… |
| 2026-11-10 20:19:31 | [CVE-2026-59611](https://nvd.nist.gov/vuln/detail/CVE-2026-59611) |  |  | In multiple locations, there is a possible way to trigger a temporary denial of service via an integer overflow trap du… |
| 2026-11-10 20:19:31 | [CVE-2026-59612](https://nvd.nist.gov/vuln/detail/CVE-2026-59612) |  |  | In buffering_period of avc_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This could l… |
| 2026-11-10 20:19:31 | [CVE-2026-59613](https://nvd.nist.gov/vuln/detail/CVE-2026-59613) |  |  | In multiple locations, there is a possible way to trigger an out of bounds read and temporary denial of service due to… |
| 2026-11-10 20:19:31 | [CVE-2026-59614](https://nvd.nist.gov/vuln/detail/CVE-2026-59614) |  |  | In multiple functions of oem_svc_setup.c, there is a possible way to dump secure cache lines into non-secure memory on… |
| 2026-11-10 20:19:31 | [CVE-2026-59616](https://nvd.nist.gov/vuln/detail/CVE-2026-59616) |  |  | In prev_run_vcore of hwcodec_firmware, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This coul… |
| 2026-11-10 20:19:31 | [CVE-2026-59618](https://nvd.nist.gov/vuln/detail/CVE-2026-59618) |  |  | In smfc_v4l2_s_selection of smfc-v4l2-ioctls.c, there is a possible way to trigger an out of bounds read from adjacent… |
| 2026-11-10 20:19:32 | [CVE-2026-59619](https://nvd.nist.gov/vuln/detail/CVE-2026-59619) |  |  | In getCodecQp of GC2AV1Enc.cpp, there is a possible way to trigger an out of bounds read during quantization table look… |
| 2026-11-10 20:19:32 | [CVE-2026-59623](https://nvd.nist.gov/vuln/detail/CVE-2026-59623) |  |  | In CompareTelUris of SipAddress.cpp, there is a possible way to trigger an unhandled out of range exception and process… |
| 2026-11-10 20:19:32 | [CVE-2026-59624](https://nvd.nist.gov/vuln/detail/CVE-2026-59624) |  |  | In multiple locations, there is a possible way to trigger an out of bounds read via direct memory access in video decod… |
| 2026-11-10 20:19:32 | [CVE-2026-59625](https://nvd.nist.gov/vuln/detail/CVE-2026-59625) |  |  | In GetTwiddledMiptreeSparsePageMap of texmgmt.c, there is a possible way to trigger an out of bounds write due to a log… |
| 2026-11-10 20:19:32 | [CVE-2026-59626](https://nvd.nist.gov/vuln/detail/CVE-2026-59626) |  |  | In SendInfo of UssiController.cpp, there is a possible way to corrupt memory via a dangling connection listener pointer… |
| 2026-11-10 20:19:32 | [CVE-2026-59628](https://nvd.nist.gov/vuln/detail/CVE-2026-59628) |  |  | In s_copy_host_apb_param of multiple files, there is a possible way to trigger an out of bounds read in the video decod… |
| 2026-11-10 20:19:32 | [CVE-2026-59630](https://nvd.nist.gov/vuln/detail/CVE-2026-59630) |  |  | In check_constraint_monotonicity of lib.rs, there is a possible way to downgrade stored security policies and bypass ro… |
| 2026-11-10 20:19:32 | [CVE-2026-59631](https://nvd.nist.gov/vuln/detail/CVE-2026-59631) |  |  | In s_inter_rps_pred of hevc_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This could… |
| 2026-11-10 20:19:32 | [CVE-2026-59632](https://nvd.nist.gov/vuln/detail/CVE-2026-59632) |  |  | In RespondReceivedMessage of MtsMessageController.cpp, there is a possible way to trigger memory exhaustion via an undr… |
| 2026-11-10 20:19:32 | [CVE-2026-59635](https://nvd.nist.gov/vuln/detail/CVE-2026-59635) |  |  | In cpb_cnt of avc_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This could lead to lo… |
| 2026-11-10 20:19:33 | [CVE-2026-59636](https://nvd.nist.gov/vuln/detail/CVE-2026-59636) |  |  | In has_booted_successfully of sys_state_setup_otp_ta.c, there is a possible way to trigger a permanent denial of servic… |
| 2026-11-10 20:19:33 | [CVE-2026-59637](https://nvd.nist.gov/vuln/detail/CVE-2026-59637) |  |  | In userdata_report of hwcodec_firmware, there is a possible Logic error due to a logic error in the code. This could le… |
| 2026-11-10 20:19:47 | [CVE-2026-95397](https://nvd.nist.gov/vuln/detail/CVE-2026-95397) |  |  | In sub_layer_hrd_parameters of hevc_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. Thi… |
| 2026-11-10 20:19:47 | [CVE-2026-95399](https://nvd.nist.gov/vuln/detail/CVE-2026-95399) |  |  | In multiple functions of face_status.h, there is a possible way to modify verified biometric enrollment data in shared… |
| 2026-11-10 20:19:47 | [CVE-2026-95400](https://nvd.nist.gov/vuln/detail/CVE-2026-95400) |  |  | In StNfc_hal_write of hal_st21nfc.cc, there is a possible way to trigger an out of bounds write into global memory due… |
| 2026-11-10 20:19:48 | [CVE-2026-95401](https://nvd.nist.gov/vuln/detail/CVE-2026-95401) |  |  | In knee_function_info of hevc_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This coul… |
| 2026-11-10 20:19:48 | [CVE-2026-95402](https://nvd.nist.gov/vuln/detail/CVE-2026-95402) |  |  | In slice_header of hevc_decoder, there is a possible Non-Heap Buffer Overflow due to a buffer overflow. This could lead… |
| 2026-11-10 20:19:48 | [CVE-2026-95403](https://nvd.nist.gov/vuln/detail/CVE-2026-95403) |  |  | In multiple locations, there is a possible way to trigger an out of bounds write in the shared memory tracking bitmap d… |
| 2026-11-10 20:19:48 | [CVE-2026-95404](https://nvd.nist.gov/vuln/detail/CVE-2026-95404) |  |  | In multiple locations, there is a possible way to modify coprocessor instruction and data memory from non-secure softwa… |

_Showing the first 200 of 306 CVEs; see the [full CSV](data/new-cves-2026-11-10T21-21-54-207578Z.csv)._

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
