# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-22 02:19 UTC

New CVEs published between 2026-11-22 01:18 UTC and 2026-11-22 02:19 UTC.

[Full CSV](data/new-cves-2026-11-22T02-19-00-019956Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-22 02:16:58 | [CVE-2026-134568](https://nvd.nist.gov/vuln/detail/CVE-2026-134568) | Low | 2.1 | A flaw has been found in itsourcecode E-Logbook with Health Monitoring System 1.0. This affects an unknown function of… |
| 2026-11-22 02:17:00 | [CVE-2026-134569](https://nvd.nist.gov/vuln/detail/CVE-2026-134569) | Low | 2.1 | A vulnerability has been found in itsourcecode Banking Management System 1.0. This impacts an unknown function of the f… |
| 2026-11-22 02:17:00 | [CVE-2026-134570](https://nvd.nist.gov/vuln/detail/CVE-2026-134570) | Low | 2.1 | A vulnerability was found in itsourcecode Banking Management System 1.0. Affected is an unknown function of the file ma… |
| 2026-11-22 02:17:00 | [CVE-2026-134571](https://nvd.nist.gov/vuln/detail/CVE-2026-134571) | Low | 2.0 | A vulnerability was determined in itsourcecode Insurance Management System 1.0. Affected by this vulnerability is an un… |
| 2026-11-22 02:17:00 | [CVE-2026-134654](https://nvd.nist.gov/vuln/detail/CVE-2026-134654) | High | 8.6 | Mailflare before 48957fb contains a host header injection vulnerability in the password-reset request handler that allo… |
| 2026-11-22 02:17:00 | [CVE-2026-134655](https://nvd.nist.gov/vuln/detail/CVE-2026-134655) | Low | 2.3 | Open5GS AMF through 2.8.0 contains a missing resource release vulnerability that allows authenticated UEs to orphan SMF… |
| 2026-11-22 02:17:01 | [CVE-2026-134656](https://nvd.nist.gov/vuln/detail/CVE-2026-134656) | Medium | 5.3 | OpenAirInterface CN5G SMF through 2.2.2 contains a missing resource release vulnerability in handle_pdu_session_release… |
| 2026-11-22 02:17:01 | [CVE-2026-134657](https://nvd.nist.gov/vuln/detail/CVE-2026-134657) | Medium | 5.3 | OpenAirInterface CN5G PCF through 2.2.2 contains a memory leak vulnerability in pcf_smpc::delete_sm_policy_handler() th… |
| 2026-11-22 02:17:01 | [CVE-2026-134658](https://nvd.nist.gov/vuln/detail/CVE-2026-134658) | Low | 2.3 | free5GC SMF through 1.4.6 contains a missing resource release vulnerability in HandlePDUSessionSMContextCreate that lea… |
| 2026-11-22 02:17:01 | [CVE-2026-134659](https://nvd.nist.gov/vuln/detail/CVE-2026-134659) | Low | 2.3 | OpenAirInterface CN5G AMF before 2.2.2 contains a missing resource release vulnerability in amf_sbi::handle_itti_messag… |
| 2026-11-22 02:17:01 | [CVE-2026-134660](https://nvd.nist.gov/vuln/detail/CVE-2026-134660) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a type confusion vulnerability in xmt_parse_command() in src/scene_manager/loader_… |
| 2026-11-22 02:17:01 | [CVE-2026-134661](https://nvd.nist.gov/vuln/detail/CVE-2026-134661) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a NULL pointer dereference vulnerability in gf_odf_encode_ui_config() in src/odf/d… |
| 2026-11-22 02:17:02 | [CVE-2026-134662](https://nvd.nist.gov/vuln/detail/CVE-2026-134662) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a double free vulnerability in the XMT-A scene loader that leaves a stale GF_Comma… |
| 2026-11-22 02:17:02 | [CVE-2026-134663](https://nvd.nist.gov/vuln/detail/CVE-2026-134663) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in the XMT scene loader that retains a pointer to a… |
| 2026-11-22 02:17:02 | [CVE-2026-134664](https://nvd.nist.gov/vuln/detail/CVE-2026-134664) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a NULL pointer dereference vulnerability in src/compositor/mpeg4_sensors.c that al… |
| 2026-11-22 02:17:02 | [CVE-2026-134665](https://nvd.nist.gov/vuln/detail/CVE-2026-134665) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in the XMT scene loader that allows attackers to ac… |
| 2026-11-22 02:17:02 | [CVE-2026-134666](https://nvd.nist.gov/vuln/detail/CVE-2026-134666) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in the XMT-A scene loader because xmt_node_end() fr… |
| 2026-11-22 02:17:03 | [CVE-2026-134667](https://nvd.nist.gov/vuln/detail/CVE-2026-134667) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a stack-based buffer overflow vulnerability in xmt_resolve_od_links() that allows… |
| 2026-11-22 02:17:03 | [CVE-2026-134668](https://nvd.nist.gov/vuln/detail/CVE-2026-134668) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in the XMT scene loader that allows attackers to co… |
| 2026-11-22 02:17:03 | [CVE-2026-134669](https://nvd.nist.gov/vuln/detail/CVE-2026-134669) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a heap-based buffer over-read vulnerability in gf_xml_sax_peek_node() in src/utils… |
| 2026-11-22 02:17:03 | [CVE-2026-134670](https://nvd.nist.gov/vuln/detail/CVE-2026-134670) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in xmt_node_end() in src/scene_manager/loader_xmt.c… |
| 2026-11-22 02:17:03 | [CVE-2026-134671](https://nvd.nist.gov/vuln/detail/CVE-2026-134671) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in the XMT-A scene loader that allows attackers to… |
| 2026-11-22 02:17:03 | [CVE-2026-134672](https://nvd.nist.gov/vuln/detail/CVE-2026-134672) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains an uncontrolled recursion vulnerability in xmt_discard_subtree() in src/scene_mana… |
| 2026-11-22 02:17:04 | [CVE-2026-134673](https://nvd.nist.gov/vuln/detail/CVE-2026-134673) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in xmt_resolve_od_links() in loader_xmt.c that allo… |
| 2026-11-22 02:17:04 | [CVE-2026-134674](https://nvd.nist.gov/vuln/detail/CVE-2026-134674) | Medium | 5.3 | Freedit before 0.9.9 contains an authorization bypass vulnerability in the post_lock, post_hide, post_pin and comment_h… |
| 2026-11-22 02:17:04 | [CVE-2026-134675](https://nvd.nist.gov/vuln/detail/CVE-2026-134675) | High | 7.1 | Servas before 1.2.0 contains a missing authorization vulnerability that allows authenticated users to modify and delete… |
| 2026-11-22 02:17:04 | [CVE-2026-134676](https://nvd.nist.gov/vuln/detail/CVE-2026-134676) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a heap use-after-free vulnerability in gf_odm_disconnect() in src/compositor/objec… |
| 2026-11-22 02:17:04 | [CVE-2026-134677](https://nvd.nist.gov/vuln/detail/CVE-2026-134677) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in the XMT scene loader that allows attackers to ac… |
| 2026-11-22 02:17:04 | [CVE-2026-134678](https://nvd.nist.gov/vuln/detail/CVE-2026-134678) | High | 7.1 | Freedit before 0.9.9 contains an authorization bypass vulnerability in the edit_post_post handler for POST /post/edit/:… |
| 2026-11-22 02:17:05 | [CVE-2026-134679](https://nvd.nist.gov/vuln/detail/CVE-2026-134679) | High | 8.7 | WeddingShare through 1.8.2 contains a missing authorization vulnerability in the anonymous MediaViewerController.Galler… |
| 2026-11-22 02:17:05 | [CVE-2026-134680](https://nvd.nist.gov/vuln/detail/CVE-2026-134680) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a NULL pointer dereference vulnerability in TraverseForm() in src/compositor/mpeg4… |
| 2026-11-22 02:17:05 | [CVE-2026-134681](https://nvd.nist.gov/vuln/detail/CVE-2026-134681) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains an uncontrolled recursion vulnerability in gf_sg_proto_instantiate() in src/sceneg… |
| 2026-11-22 02:17:05 | [CVE-2026-134682](https://nvd.nist.gov/vuln/detail/CVE-2026-134682) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in scene graph teardown that allows attackers to tr… |
| 2026-11-22 02:17:05 | [CVE-2026-134683](https://nvd.nist.gov/vuln/detail/CVE-2026-134683) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains an uncontrolled recursion vulnerability in xmt_remove_od_links_recursive() in load… |
| 2026-11-22 02:17:05 | [CVE-2026-134684](https://nvd.nist.gov/vuln/detail/CVE-2026-134684) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a heap use-after-free vulnerability in the XMT loader that leaves freed node URL f… |
| 2026-11-22 02:17:06 | [CVE-2026-134685](https://nvd.nist.gov/vuln/detail/CVE-2026-134685) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a heap use-after-free vulnerability in load_xmt_done() in src/scene_manager/loader… |
| 2026-11-22 02:17:06 | [CVE-2026-134686](https://nvd.nist.gov/vuln/detail/CVE-2026-134686) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a type confusion vulnerability in gf_sg_command_apply() in src/scenegraph/commands… |
| 2026-11-22 02:17:06 | [CVE-2026-134687](https://nvd.nist.gov/vuln/detail/CVE-2026-134687) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a NULL pointer dereference vulnerability in gf_sg_command_apply() in src/scenegrap… |
| 2026-11-22 02:17:06 | [CVE-2026-134688](https://nvd.nist.gov/vuln/detail/CVE-2026-134688) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in the BT/XMT context loader that frees an interact… |
| 2026-11-22 02:17:06 | [CVE-2026-134689](https://nvd.nist.gov/vuln/detail/CVE-2026-134689) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a NULL pointer dereference vulnerability in JSScript_LoadVRML() in src/scenegraph/… |
| 2026-11-22 02:17:07 | [CVE-2026-134690](https://nvd.nist.gov/vuln/detail/CVE-2026-134690) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a NULL pointer dereference vulnerability that allows attackers to crash the applic… |
| 2026-11-22 02:17:07 | [CVE-2026-134691](https://nvd.nist.gov/vuln/detail/CVE-2026-134691) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a heap use-after-free vulnerability in gf_event_target_get_node() because destroye… |
| 2026-11-22 02:17:07 | [CVE-2026-134692](https://nvd.nist.gov/vuln/detail/CVE-2026-134692) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability because xmt_find_node() in loader_xmt.c resolves DE… |
| 2026-11-22 02:17:07 | [CVE-2026-134693](https://nvd.nist.gov/vuln/detail/CVE-2026-134693) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a NULL pointer dereference vulnerability in gf_sg_proto_create_node() in src/scene… |
| 2026-11-22 02:17:07 | [CVE-2026-134694](https://nvd.nist.gov/vuln/detail/CVE-2026-134694) | High | 8.5 | Gammapy through 2.1 contains a code injection vulnerability in WcsGeom.from_header() that passes the WCSSHAPE FITS head… |
| 2026-11-22 02:17:07 | [CVE-2026-134695](https://nvd.nist.gov/vuln/detail/CVE-2026-134695) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains an out-of-bounds read vulnerability in avi_parse_input_file() in src/media_tools/a… |
| 2026-11-22 02:17:08 | [CVE-2026-134696](https://nvd.nist.gov/vuln/detail/CVE-2026-134696) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in gf_sg_proto_del that allows attackers to free PR… |
| 2026-11-22 02:17:08 | [CVE-2026-134697](https://nvd.nist.gov/vuln/detail/CVE-2026-134697) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a NULL pointer dereference vulnerability in gf_sg_command_apply() that allows atta… |
| 2026-11-22 02:17:08 | [CVE-2026-134698](https://nvd.nist.gov/vuln/detail/CVE-2026-134698) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a type confusion vulnerability in ctxload_process() in src/filters/load_bt_xmt.c t… |
| 2026-11-22 02:17:08 | [CVE-2026-134699](https://nvd.nist.gov/vuln/detail/CVE-2026-134699) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a type confusion vulnerability in src/compositor/mpeg4_text.c that allows heap out… |
| 2026-11-22 02:17:08 | [CVE-2026-134700](https://nvd.nist.gov/vuln/detail/CVE-2026-134700) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in the XMT loader that allows scene commands to ref… |
| 2026-11-22 02:17:09 | [CVE-2026-134701](https://nvd.nist.gov/vuln/detail/CVE-2026-134701) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a heap use-after-free vulnerability in xmt_node_end() that leaves freed child node… |
| 2026-11-22 02:17:09 | [CVE-2026-134702](https://nvd.nist.gov/vuln/detail/CVE-2026-134702) | Medium | 6.8 | GPAC MP4Box through 26.07.0 contains a type confusion vulnerability in curve2d_check_changes() that casts a Curve2D poi… |
| 2026-11-22 02:17:09 | [CVE-2026-134703](https://nvd.nist.gov/vuln/detail/CVE-2026-134703) | Medium | 6.3 | libexpat through 2.10.0 contains an improper Unicode handling vulnerability in DEFINE_UTF16_TO_UTF16 conversion functio… |
| 2026-11-22 02:17:09 | [CVE-2026-134704](https://nvd.nist.gov/vuln/detail/CVE-2026-134704) | High | 8.5 | OpenShot Video Editor (openshot-qt) through 4.1.1 contains an unsafe deserialization vulnerability in ProjectDataStore.… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
