# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-19 00:21 UTC

New CVEs published between 2026-11-18 23:20 UTC and 2026-11-19 00:21 UTC.

[Full CSV](data/new-cves-2026-11-19T00-21-53-726548Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-19 00:17:41 | [CVE-2026-127039](https://nvd.nist.gov/vuln/detail/CVE-2026-127039) | Medium | 5.9 | The certificate authentication info handling in gnutls from 2.5.9 up to 3.8.13 does not reset the certificate count and… |
| 2026-11-19 00:17:41 | [CVE-2026-127040](https://nvd.nist.gov/vuln/detail/CVE-2026-127040) | Medium | 5.9 | The RSA-PSK ClientKeyExchange handler in gnutls before 3.8.14 does not return after detecting a memory allocation failu… |
| 2026-11-19 00:17:41 | [CVE-2026-127231](https://nvd.nist.gov/vuln/detail/CVE-2026-127231) | Medium | 5.9 | A double free in the X.509 name constraints enforcement of GnuTLS 3.8.13 on all platforms allows a remote attacker to c… |
| 2026-11-19 00:17:41 | [CVE-2026-132281](https://nvd.nist.gov/vuln/detail/CVE-2026-132281) | Low | 2.1 | A vulnerability was found in elunez eladmin up to 2.7. This affects the function SqlUtils.batchExecute of the file /api… |
| 2026-11-19 00:17:42 | [CVE-2026-132282](https://nvd.nist.gov/vuln/detail/CVE-2026-132282) | Low | 2.1 | A vulnerability was determined in elunez eladmin up to 2.7. This vulnerability affects the function FileUtil.upload of… |
| 2026-11-19 00:17:42 | [CVE-2026-132283](https://nvd.nist.gov/vuln/detail/CVE-2026-132283) | Medium | 6.9 | A vulnerability was identified in Directus up to 12.7.0. This issue affects the function AuthenticationService.refresh… |
| 2026-11-19 00:17:42 | [CVE-2026-132745](https://nvd.nist.gov/vuln/detail/CVE-2026-132745) | High | 7.1 | Vtiger CRM through 8.4.0 contains a blind SQL injection vulnerability that allows authenticated non-administrative user… |
| 2026-11-19 00:17:42 | [CVE-2026-132746](https://nvd.nist.gov/vuln/detail/CVE-2026-132746) | High | 7.1 | Vtiger CRM through 8.4.0 contains a blind SQL injection vulnerability that allows authenticated low-privileged users to… |
| 2026-11-19 00:17:42 | [CVE-2026-132747](https://nvd.nist.gov/vuln/detail/CVE-2026-132747) | High | 7.1 | Vtiger CRM through 8.4.0 contains an SQL injection vulnerability that allows authenticated users with export access to… |
| 2026-11-19 00:17:42 | [CVE-2026-132748](https://nvd.nist.gov/vuln/detail/CVE-2026-132748) | High | 8.6 | Vtiger CRM through 8.4.0 contains a PHP code injection vulnerability that allows authenticated administrators to inject… |
| 2026-11-19 00:17:43 | [CVE-2026-132749](https://nvd.nist.gov/vuln/detail/CVE-2026-132749) | High | 7.1 | Vtiger CRM through 8.4.0 contains a blind SQL injection vulnerability in ReportRun::generateAdvFilterSql() that allows… |
| 2026-11-19 00:17:43 | [CVE-2026-132750](https://nvd.nist.gov/vuln/detail/CVE-2026-132750) | High | 7.1 | Meilisearch before 1.55.1 and 1.56.x before 1.56.1 contains a quadratic memory consumption vulnerability in filter-pars… |
| 2026-11-19 00:17:43 | [CVE-2026-132751](https://nvd.nist.gov/vuln/detail/CVE-2026-132751) | High | 8.5 | yt through 4.4.4 contains a code injection vulnerability that allows attackers to execute Python code by supplying a cr… |
| 2026-11-19 00:17:43 | [CVE-2026-132752](https://nvd.nist.gov/vuln/detail/CVE-2026-132752) | Medium | 5.1 | ScreenTinker before 3.2.4 contains a stored cross-site scripting vulnerability in the GET /api/kiosk/:id/render endpoin… |
| 2026-11-19 00:17:43 | [CVE-2026-132753](https://nvd.nist.gov/vuln/detail/CVE-2026-132753) | Medium | 6.8 | MP4v2 through 2.1.0 contains a NULL pointer dereference vulnerability in MP4RtpHintTrack::GetPayload() in src/rtphint.c… |
| 2026-11-19 00:17:43 | [CVE-2026-132754](https://nvd.nist.gov/vuln/detail/CVE-2026-132754) | Medium | 6.9 | MediaInfoLib before 26.10 contains an out-of-bounds read vulnerability in File_Mpeg4::meta_iloc that allows attackers t… |
| 2026-11-19 00:17:44 | [CVE-2026-132756](https://nvd.nist.gov/vuln/detail/CVE-2026-132756) | High | 8.5 | Geany through 2.1.0 contains an OS command injection vulnerability that allows attackers to run shell commands by embed… |
| 2026-11-19 00:17:44 | [CVE-2026-132757](https://nvd.nist.gov/vuln/detail/CVE-2026-132757) | Medium | 6.8 | GPAC before 26.07.0 contains a NULL pointer dereference vulnerability in DoWriteMeta() in src/isomedia/isom_store.c tha… |
| 2026-11-19 00:17:44 | [CVE-2026-132758](https://nvd.nist.gov/vuln/detail/CVE-2026-132758) | Medium | 6.8 | GPAC MP4Box before 26.07.0 contains a NULL pointer dereference vulnerability in xmt_node_end() that allows attackers to… |
| 2026-11-19 00:17:44 | [CVE-2026-132759](https://nvd.nist.gov/vuln/detail/CVE-2026-132759) | Medium | 6.9 | GPAC MP4Box before 26.07.0 contains a use-after-free vulnerability because gf_node_free() frees nodes without detaching… |
| 2026-11-19 00:17:44 | [CVE-2026-132760](https://nvd.nist.gov/vuln/detail/CVE-2026-132760) | Medium | 6.8 | GPAC before 26.07.0 contains a NULL pointer dereference vulnerability in gf_isom_get_meta() in src/isomedia/meta.c that… |
| 2026-11-19 00:17:44 | [CVE-2026-132755](https://nvd.nist.gov/vuln/detail/CVE-2026-132755) | Medium | 6.9 | MediaInfoLib before 26.10 contains a heap-based buffer over-read vulnerability in tfsxml_leave() caused by an off-by-on… |
| 2026-11-19 00:17:45 | [CVE-2026-132761](https://nvd.nist.gov/vuln/detail/CVE-2026-132761) | Medium | 6.8 | GPAC before 26.07.0 contains a use-after-free vulnerability in gf_node_try_destroy that allows attackers to crash MP4Bo… |
| 2026-11-19 00:17:45 | [CVE-2026-132762](https://nvd.nist.gov/vuln/detail/CVE-2026-132762) | Medium | 6.8 | GPAC MP4Box before 26.07.0 contains a divide by zero vulnerability in DumpTrackInfo() in applications/mp4box/filedump.c… |
| 2026-11-19 00:17:45 | [CVE-2026-132763](https://nvd.nist.gov/vuln/detail/CVE-2026-132763) | Medium | 6.9 | GPAC before 26.07.0 contains an integer underflow vulnerability in gf_xml_sax_peek_node() that allows attackers to writ… |
| 2026-11-19 00:17:45 | [CVE-2026-132764](https://nvd.nist.gov/vuln/detail/CVE-2026-132764) | Medium | 6.9 | GPAC before 26.07.0 contains a use-after-free vulnerability in the XMT loader that leaves ROUTE commands of a discarded… |
| 2026-11-19 00:17:45 | [CVE-2026-132765](https://nvd.nist.gov/vuln/detail/CVE-2026-132765) | Medium | 6.9 | GPAC MP4Box through 26.07.0 contains a use-after-free vulnerability in gf_node_try_destroy because Conditional node com… |
| 2026-11-19 00:17:45 | [CVE-2026-132766](https://nvd.nist.gov/vuln/detail/CVE-2026-132766) | Medium | 6.9 | GPAC before 26.07.0 contains a use-after-free vulnerability in MP4Box because gf_sg_reset frees DEF'd proto sub-graph n… |
| 2026-11-19 00:17:46 | [CVE-2026-132767](https://nvd.nist.gov/vuln/detail/CVE-2026-132767) | Medium | 6.8 | GPAC before 26.07.0 contains a NULL pointer dereference vulnerability in xmt_parse_command() in loader_xmt.c that allow… |
| 2026-11-19 00:17:46 | [CVE-2026-132768](https://nvd.nist.gov/vuln/detail/CVE-2026-132768) | Medium | 6.8 | GPAC MP4Box before 26.07.0 contains a use-after-free vulnerability in xmt_find_node() in loader_xmt.c that leaves freed… |
| 2026-11-19 00:17:46 | [CVE-2026-132769](https://nvd.nist.gov/vuln/detail/CVE-2026-132769) | Medium | 6.9 | GPAC before 26.07.0 contains a type confusion vulnerability in xmt_parse_script_field() that allows attackers to trigge… |
| 2026-11-19 00:17:46 | [CVE-2026-132770](https://nvd.nist.gov/vuln/detail/CVE-2026-132770) | Medium | 6.8 | GPAC MP4Box before 26.07.0 contains a NULL pointer dereference vulnerability in xmt_parse_proto() in loader_xmt.c that… |
| 2026-11-19 00:17:46 | [CVE-2026-132771](https://nvd.nist.gov/vuln/detail/CVE-2026-132771) | Medium | 6.8 | GPAC before 26.07.0 contains a use-after-free vulnerability in ReplaceDEFNode that allows attackers to crash MP4Box by… |
| 2026-11-19 00:17:46 | [CVE-2026-132772](https://nvd.nist.gov/vuln/detail/CVE-2026-132772) | Medium | 6.9 | GPAC MP4Box before 26.07.0 contains a use-after-free vulnerability in the XMT parser that leaves parser->command_buffer… |
| 2026-11-19 00:17:46 | [CVE-2026-132773](https://nvd.nist.gov/vuln/detail/CVE-2026-132773) | High | 7.1 | Attendize through 2.8.0 contains an authorization bypass vulnerability in EventOrdersController::postCancelOrder() that… |
| 2026-11-19 00:17:47 | [CVE-2026-132774](https://nvd.nist.gov/vuln/detail/CVE-2026-132774) | Medium | 5.3 | Attendize through 2.8.0 contains a cross-account authorization bypass vulnerability in EventAttendeesController::postMe… |
| 2026-11-19 00:17:47 | [CVE-2026-132775](https://nvd.nist.gov/vuln/detail/CVE-2026-132775) | Medium | 6.9 | GPAC before 26.07.0 contains a use-after-free vulnerability in xmt_node_end() that allows attackers to corrupt memory b… |
| 2026-11-19 00:17:47 | [CVE-2026-132776](https://nvd.nist.gov/vuln/detail/CVE-2026-132776) | Medium | 6.8 | GPAC MP4Box before 26.07.0 contains a use-after-free vulnerability in the XMT loader that allows attackers to crash the… |
| 2026-11-19 00:17:47 | [CVE-2026-132777](https://nvd.nist.gov/vuln/detail/CVE-2026-132777) | Medium | 6.9 | GPAC MP4Box before 26.07.0 contains a use-after-free vulnerability in Conditional_execute() because SetupConditional()… |
| 2026-11-19 00:17:47 | [CVE-2026-132778](https://nvd.nist.gov/vuln/detail/CVE-2026-132778) | Medium | 6.8 | GPAC before 26.07.0 contains an uncontrolled recursion vulnerability in gf_sg_proto_field_is_sftime_offset() in src/sce… |
| 2026-11-19 00:17:48 | [CVE-2026-91138](https://nvd.nist.gov/vuln/detail/CVE-2026-91138) | Medium | 6.9 | The Deco BE65 v3 firmware contains a shared hard-coded password hash for the root account in /etc/shadow. Where the cor… |
| 2026-11-19 00:17:48 | [CVE-2026-91139](https://nvd.nist.gov/vuln/detail/CVE-2026-91139) | Medium | 6.1 | Deco BE65 firmware contains a cryptographic weakness in the local web-management authentication flow due to the use of… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
