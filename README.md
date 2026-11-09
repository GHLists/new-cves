# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 19:18 UTC

New CVEs published between 2026-11-09 18:19 UTC and 2026-11-09 19:18 UTC.

[Full CSV](data/new-cves-2026-11-09T19-18-19-602895Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 19:16:39 | [CVE-2026-112314](https://nvd.nist.gov/vuln/detail/CVE-2026-112314) | High | 7.5 | clnttcp_call() in lib/rpc/clnt_tcp.c in MIT Kerberos 5 (aka krb5) does not free the RPC reply verifier between retries,… |
| 2026-11-09 19:16:40 | [CVE-2026-112315](https://nvd.nist.gov/vuln/detail/CVE-2026-112315) | Medium | 5.3 | The RPCSEC_GSS authentication routines in lib/rpc/authgss_prot.c in MIT Kerberos 5 (aka krb5) 1.4 and later do not free… |
| 2026-11-09 19:16:40 | [CVE-2026-112316](https://nvd.nist.gov/vuln/detail/CVE-2026-112316) | Medium | 6.5 | xdr_krb5_tl_data() in lib/kadm5/kadm_rpc_xdr.c in MIT Kerberos 5 (aka krb5) does not free partially decoded data on fai… |
| 2026-11-09 19:16:40 | [CVE-2026-112317](https://nvd.nist.gov/vuln/detail/CVE-2026-112317) | Medium | 5.3 | krb5_ktkdb_get_entry() in lib/kdb/keytab.c in MIT Kerberos 5 (aka krb5) 1.2.8 and later does not free decrypted key mat… |
| 2026-11-09 19:16:40 | [CVE-2026-112318](https://nvd.nist.gov/vuln/detail/CVE-2026-112318) | Medium | 6.5 | The policy RPC stubs in kadmin/server/server_stubs.c in MIT Kerberos 5 (aka krb5) 1.5.3 and later do not reject a NULL… |
| 2026-11-09 19:16:40 | [CVE-2026-112319](https://nvd.nist.gov/vuln/detail/CVE-2026-112319) | Medium | 6.5 | The GSS-RPC layer in MIT Kerberos 5 (aka krb5) does not enforce size limits on XDR-decoded data, which allows remote au… |
| 2026-11-09 19:16:40 | [CVE-2026-112320](https://nvd.nist.gov/vuln/detail/CVE-2026-112320) | High | 7.5 | The GSS-RPC transport layer in MIT Kerberos 5 (aka krb5) 1.4 and later does not release the previous authentication con… |
| 2026-11-09 19:16:41 | [CVE-2026-112321](https://nvd.nist.gov/vuln/detail/CVE-2026-112321) | High | 7.5 | The AUTH_GSSAPI handler in lib/rpc/svc_auth_gssapi.c in MIT Kerberos 5 (aka krb5) does not free decoded arguments on ce… |
| 2026-11-09 19:16:41 | [CVE-2026-112322](https://nvd.nist.gov/vuln/detail/CVE-2026-112322) | High | 7.5 | clean_client() in lib/rpc/svc_auth_gssapi.c in MIT Kerberos 5 (aka krb5) restarts its scan from the head of the client… |
| 2026-11-09 19:16:41 | [CVE-2026-112323](https://nvd.nist.gov/vuln/detail/CVE-2026-112323) | High | 7.5 | The AUTH_GSSAPI handler in lib/rpc/svc_auth_gssapi.c in MIT Kerberos 5 (aka krb5) 1.5.2 and later allows remote attacke… |
| 2026-11-09 19:16:43 | [CVE-2026-119079](https://nvd.nist.gov/vuln/detail/CVE-2026-119079) | High | 7.5 | decode_sequence_of() in lib/krb5/asn.1/asn1_encode.c in MIT Kerberos 5 (aka krb5) 1.11 and later grows the decoded elem… |
| 2026-11-09 19:16:44 | [CVE-2026-120834](https://nvd.nist.gov/vuln/detail/CVE-2026-120834) | High | 7.3 | Incorrect Privilege Assignment vulnerability in Tobias WP2LEADS wp2leads allows Privilege Escalation.This issue affects… |
| 2026-11-09 19:16:45 | [CVE-2026-121573](https://nvd.nist.gov/vuln/detail/CVE-2026-121573) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Melapress WP Acti… |
| 2026-11-09 19:16:46 | [CVE-2026-121769](https://nvd.nist.gov/vuln/detail/CVE-2026-121769) | High | 8.5 | Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in axew3.com WP w3al… |
| 2026-11-09 19:16:46 | [CVE-2026-123798](https://nvd.nist.gov/vuln/detail/CVE-2026-123798) | High | 8.1 | SuperTokens Core is an open source authentication server. From 11.3.0 until 11.3.7, 11.4.7, and 12.0.10, SAML.verifySam… |
| 2026-11-09 19:16:46 | [CVE-2026-123799](https://nvd.nist.gov/vuln/detail/CVE-2026-123799) | High | 7.4 | SuperTokens Core is an open source authentication server. From 11.0.0 until 11.0.9, 11.1.4, 11.2.4, 11.3.8, 11.4.8, 12.… |
| 2026-11-09 19:16:46 | [CVE-2026-123800](https://nvd.nist.gov/vuln/detail/CVE-2026-123800) | Critical | 9.9 | SuperTokens Core is an open source authentication server. From 6.0.0 until 6.0.24, 7.0.23, 8.0.7, 9.0.6, 9.1.6, 9.2.7,… |
| 2026-11-09 19:16:46 | [CVE-2026-123801](https://nvd.nist.gov/vuln/detail/CVE-2026-123801) | High | 7.4 | SuperTokens Core is an open source authentication server. From 11.3.0 until 11.3.8, 11.4.8, 12.0.11, 12.1.2, 12.2.1, an… |
| 2026-11-09 19:16:47 | [CVE-2026-123802](https://nvd.nist.gov/vuln/detail/CVE-2026-123802) | High | 8.1 | SuperTokens Core is an open source authentication server. From 11.3.0 until 11.3.8, 11.4.8, 12.0.11, 12.1.2, 12.2.1, an… |
| 2026-11-09 19:16:47 | [CVE-2026-123803](https://nvd.nist.gov/vuln/detail/CVE-2026-123803) | High | 8.1 | SuperTokens Core is an open source authentication server. From 10.1.0 until 11.0.9, 11.1.4, 11.2.4, 11.3.8, 11.4.8, 12.… |
| 2026-11-09 19:16:47 | [CVE-2026-123804](https://nvd.nist.gov/vuln/detail/CVE-2026-123804) | Medium | 6.8 | SuperTokens Core is an open source authentication server. From 7.0.0 until 11.0.9, 11.1.4, 11.2.4, 11.3.8, 11.4.8, 12.0… |
| 2026-11-09 19:16:47 | [CVE-2026-123999](https://nvd.nist.gov/vuln/detail/CVE-2026-123999) | High | 8.7 | NASA JPL ION-DTN 3.6.2 through 4.2.0 contains a heap-based buffer overflow in the Network Management daemon (nm_mgr) st… |
| 2026-11-09 19:16:47 | [CVE-2026-124000](https://nvd.nist.gov/vuln/detail/CVE-2026-124000) | Medium | 6.9 | NASA JPL ION-DTN 2.1.0 through 4.2.0 contains a heap buffer under-allocation vulnerability in the Asynchronous Message… |
| 2026-11-09 19:16:48 | [CVE-2026-124001](https://nvd.nist.gov/vuln/detail/CVE-2026-124001) | Critical | 9.2 | NASA JPL ION-DTN 2.2.1b through 4.2.0 contains an integer overflow vulnerability in the Datagram Retransmission (DGR) c… |
| 2026-11-09 19:16:48 | [CVE-2026-125040](https://nvd.nist.gov/vuln/detail/CVE-2026-125040) | Medium | 6.5 | A flaw was found in the SRT and WebVTT subtitle parser in GStreamer's gst-plugins-base. While sanitizing inline subtitl… |
| 2026-11-09 19:16:48 | [CVE-2026-125041](https://nvd.nist.gov/vuln/detail/CVE-2026-125041) | Medium | 5.5 | A flaw was found in GStreamer's gst-plugins-good MOV/MP4 demuxer. When processing an uncompressed video track, qtdemux… |
| 2026-11-09 19:16:48 | [CVE-2026-125064](https://nvd.nist.gov/vuln/detail/CVE-2026-125064) | Medium | 6.8 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in g726_decode_frame() in libavcodec/g726.c beca… |
| 2026-11-09 19:16:48 | [CVE-2026-125065](https://nvd.nist.gov/vuln/detail/CVE-2026-125065) | Medium | 6.8 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in tgv_decode_inter() in libavcodec/eatgv.c that… |
| 2026-11-09 19:16:48 | [CVE-2026-125066](https://nvd.nist.gov/vuln/detail/CVE-2026-125066) | Medium | 6.8 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in the Cirrus Logic AccuPak (CLJR) decoder in li… |
| 2026-11-09 19:16:49 | [CVE-2026-125067](https://nvd.nist.gov/vuln/detail/CVE-2026-125067) | Medium | 6.8 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in vble_decode_frame() in libavcodec/vble.c beca… |
| 2026-11-09 19:16:49 | [CVE-2026-125068](https://nvd.nist.gov/vuln/detail/CVE-2026-125068) | Medium | 6.8 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in the Bink video decoder because decode_frame()… |
| 2026-11-09 19:16:49 | [CVE-2026-125069](https://nvd.nist.gov/vuln/detail/CVE-2026-125069) | Medium | 5.7 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in the Motion Pixels decoder because mp_decode_f… |
| 2026-11-09 19:16:49 | [CVE-2026-125070](https://nvd.nist.gov/vuln/detail/CVE-2026-125070) | Medium | 6.8 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in tqi_decode_frame() in libavcodec/eatqi.c, whi… |
| 2026-11-09 19:16:49 | [CVE-2026-125071](https://nvd.nist.gov/vuln/detail/CVE-2026-125071) | Medium | 5.7 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in libavcodec/jvdec.c that allows attackers to c… |
| 2026-11-09 19:16:49 | [CVE-2026-125072](https://nvd.nist.gov/vuln/detail/CVE-2026-125072) | Medium | 5.7 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in mp_decode_frame() in libavcodec/mpegaudiodec_… |
| 2026-11-09 19:16:50 | [CVE-2026-125073](https://nvd.nist.gov/vuln/detail/CVE-2026-125073) | Medium | 6.8 | FFmpeg through 9.0.2 contains an infinite loop vulnerability in bit_allocation() in libavcodec/imc.c that allows attack… |
| 2026-11-09 19:16:50 | [CVE-2026-125095](https://nvd.nist.gov/vuln/detail/CVE-2026-125095) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory use vulnerability in the C93 video decoder in libavcodec/c93.c, w… |
| 2026-11-09 19:16:50 | [CVE-2026-125096](https://nvd.nist.gov/vuln/detail/CVE-2026-125096) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory disclosure vulnerability in libavcodec/tiertexseqv.c that allows… |
| 2026-11-09 19:16:50 | [CVE-2026-125097](https://nvd.nist.gov/vuln/detail/CVE-2026-125097) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory disclosure vulnerability in raw_decode() in libavcodec/rawdec.c t… |
| 2026-11-09 19:16:50 | [CVE-2026-125098](https://nvd.nist.gov/vuln/detail/CVE-2026-125098) | Medium | 4.8 | FFmpeg through 9.0.2 contains an information disclosure vulnerability in vp8_lossy_decode_alpha() in libavcodec/webp.c… |
| 2026-11-09 19:16:50 | [CVE-2026-125099](https://nvd.nist.gov/vuln/detail/CVE-2026-125099) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory disclosure vulnerability in the GEM raster image decoder in libav… |
| 2026-11-09 19:16:51 | [CVE-2026-125100](https://nvd.nist.gov/vuln/detail/CVE-2026-125100) | Medium | 4.8 | FFmpeg through 9.0.2 contains an integer overflow vulnerability in the OpenEXR decoder's decode_frame() in libavcodec/e… |
| 2026-11-09 19:16:51 | [CVE-2026-125101](https://nvd.nist.gov/vuln/detail/CVE-2026-125101) | Medium | 4.8 | FFmpeg through 9.0.2 contains an information disclosure vulnerability in the VMnc decoder in libavcodec/vmnc.c that res… |
| 2026-11-09 19:16:51 | [CVE-2026-125102](https://nvd.nist.gov/vuln/detail/CVE-2026-125102) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory disclosure vulnerability in tak_decode_frame() in libavcodec/takd… |
| 2026-11-09 19:16:51 | [CVE-2026-125103](https://nvd.nist.gov/vuln/detail/CVE-2026-125103) | Medium | 4.8 | FFmpeg through 9.0.2 contains an information disclosure vulnerability in ff_mlz_decompression() in libavcodec/mlz.c, wh… |
| 2026-11-09 19:16:51 | [CVE-2026-125104](https://nvd.nist.gov/vuln/detail/CVE-2026-125104) | Medium | 6.8 | FFmpeg through 9.0.2 contains a memory exhaustion vulnerability in ape_decode_frame() in libavcodec/apedec.c that fails… |
| 2026-11-09 19:16:51 | [CVE-2026-125170](https://nvd.nist.gov/vuln/detail/CVE-2026-125170) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory disclosure vulnerability in targa_decode_rle() in libavcodec/targ… |
| 2026-11-09 19:16:51 | [CVE-2026-125171](https://nvd.nist.gov/vuln/detail/CVE-2026-125171) | Medium | 6.9 | FFmpeg through 9.0.2 contains an out-of-bounds read vulnerability in the Musepack SV7 decoder because mpc7_decode_init(… |
| 2026-11-09 19:16:52 | [CVE-2026-125172](https://nvd.nist.gov/vuln/detail/CVE-2026-125172) | Medium | 6.9 | FFmpeg through 9.0.2 contains an out-of-bounds read vulnerability in libxevd_receive_frame() in libavcodec/libxevd.c th… |
| 2026-11-09 19:16:52 | [CVE-2026-125173](https://nvd.nist.gov/vuln/detail/CVE-2026-125173) | Medium | 6.8 | FFmpeg through 9.0.2 contains a memory leak vulnerability in libxevd_receive_frame() in libavcodec/libxevd.c that fails… |
| 2026-11-09 19:16:52 | [CVE-2026-125174](https://nvd.nist.gov/vuln/detail/CVE-2026-125174) | Medium | 6.8 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains a NULL pointer dereference vulnerability in ff_hap_set_chunk_count()… |
| 2026-11-09 19:16:52 | [CVE-2026-125175](https://nvd.nist.gov/vuln/detail/CVE-2026-125175) | Medium | 4.8 | FFmpeg through 9.0.2 contains an information disclosure vulnerability in flashsv_decode_block() in libavcodec/flashsv.c… |
| 2026-11-09 19:16:52 | [CVE-2026-125176](https://nvd.nist.gov/vuln/detail/CVE-2026-125176) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory read vulnerability in decode_hybrid() in libavcodec/flashsv.c tha… |
| 2026-11-09 19:16:52 | [CVE-2026-125177](https://nvd.nist.gov/vuln/detail/CVE-2026-125177) | Medium | 4.8 | FFmpeg through 9.0.2 contains an information disclosure vulnerability in the MSCC/SRGC decoder in libavcodec/mscc.c tha… |
| 2026-11-09 19:16:52 | [CVE-2026-125178](https://nvd.nist.gov/vuln/detail/CVE-2026-125178) | Medium | 6.9 | FFmpeg through 9.0.2 contains an out-of-bounds heap read vulnerability in tdsc_load_cursor() in libavcodec/tdsc.c, whic… |
| 2026-11-09 19:16:53 | [CVE-2026-125179](https://nvd.nist.gov/vuln/detail/CVE-2026-125179) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory vulnerability in the VQA video decoder in libavcodec/vqavideo.c t… |
| 2026-11-09 19:16:53 | [CVE-2026-125180](https://nvd.nist.gov/vuln/detail/CVE-2026-125180) | Medium | 6.8 | FFmpeg 8.1 through 9.0.2 contains a memory exhaustion vulnerability in the libavcodec/exif.c parser that allows attacke… |
| 2026-11-09 19:16:53 | [CVE-2026-125181](https://nvd.nist.gov/vuln/detail/CVE-2026-125181) | High | 7.3 | FFmpeg through 9.0.2 contains an out-of-bounds write vulnerability in flic_decode_frame_15_16BPP() in libavcodec/flicvi… |
| 2026-11-09 19:16:53 | [CVE-2026-125182](https://nvd.nist.gov/vuln/detail/CVE-2026-125182) | Medium | 4.8 | FFmpeg through 9.0.2 contains an out-of-bounds read vulnerability in the Cook decoder joint_decode() function because c… |
| 2026-11-09 19:16:53 | [CVE-2026-125183](https://nvd.nist.gov/vuln/detail/CVE-2026-125183) | Medium | 6.8 | FFmpeg through 9.0.2 contains a denial of service vulnerability in pps_3d_extension() in libavcodec/hevc/ps.c that allo… |
| 2026-11-09 19:16:53 | [CVE-2026-125184](https://nvd.nist.gov/vuln/detail/CVE-2026-125184) | Medium | 4.8 | FFmpeg 6.1 through 9.0.2 contains an information disclosure vulnerability in the CamStudio decoder (libavcodec/cscd.c)… |
| 2026-11-09 19:16:54 | [CVE-2026-125185](https://nvd.nist.gov/vuln/detail/CVE-2026-125185) | Medium | 6.8 | FFmpeg through 9.0.2 contains a division by zero vulnerability in ff_aom_parse_film_grain_sets() that fails to reject A… |
| 2026-11-09 19:16:54 | [CVE-2026-125186](https://nvd.nist.gov/vuln/detail/CVE-2026-125186) | Medium | 5.7 | FFmpeg through 9.0.2 contains an uncontrolled resource consumption vulnerability in the dts2pts bitstream filter that a… |
| 2026-11-09 19:16:54 | [CVE-2026-125187](https://nvd.nist.gov/vuln/detail/CVE-2026-125187) | Medium | 6.8 | FFmpeg through 9.0.2 contains a reachable assertion vulnerability in the TTA encoder's tta_encode_frame() in libavcodec… |
| 2026-11-09 19:16:54 | [CVE-2026-125188](https://nvd.nist.gov/vuln/detail/CVE-2026-125188) | Low | 2.0 | FFmpeg through 9.0.2 contains a heap out-of-bounds read vulnerability in libavcodec/proresenc_anatoliy.c that occurs wh… |
| 2026-11-09 19:16:54 | [CVE-2026-125189](https://nvd.nist.gov/vuln/detail/CVE-2026-125189) | Medium | 5.7 | FFmpeg 8.1 through 9.0.2 contains a denial of service vulnerability in the lcevc_metadata bitstream filter caused by a… |
| 2026-11-09 19:16:54 | [CVE-2026-125190](https://nvd.nist.gov/vuln/detail/CVE-2026-125190) | Medium | 4.8 | FFmpeg through 9.0.2 contains an information disclosure vulnerability in decode_mvc2() in libavcodec/mvcdec.c that leak… |
| 2026-11-09 19:16:54 | [CVE-2026-125191](https://nvd.nist.gov/vuln/detail/CVE-2026-125191) | Medium | 5.7 | FFmpeg through 9.0.2 contains a reference count leak in libavcodec/v4l2_buffers.c that allows attackers to deadlock the… |
| 2026-11-09 19:16:55 | [CVE-2026-125192](https://nvd.nist.gov/vuln/detail/CVE-2026-125192) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory vulnerability in the DXA decoder in libavcodec/dxa.c that allows… |
| 2026-11-09 19:16:55 | [CVE-2026-125193](https://nvd.nist.gov/vuln/detail/CVE-2026-125193) | Medium | 6.9 | FFmpeg through 9.0.2 contains an out-of-bounds read vulnerability in bitpacked_decode_uyvy422() in libavcodec/bitpacked… |
| 2026-11-09 19:16:55 | [CVE-2026-125194](https://nvd.nist.gov/vuln/detail/CVE-2026-125194) | Medium | 6.8 | FFmpeg through 9.0.2 contains an out-of-bounds read vulnerability in pcm_dvd_encode_frame() in libavcodec/pcm-dvdenc.c… |
| 2026-11-09 19:16:55 | [CVE-2026-125195](https://nvd.nist.gov/vuln/detail/CVE-2026-125195) | Low | 2.0 | FFmpeg through 9.0.2 contains an uninitialized memory disclosure vulnerability in adpcm_encode_frame() in libavcodec/ad… |
| 2026-11-09 19:16:55 | [CVE-2026-125196](https://nvd.nist.gov/vuln/detail/CVE-2026-125196) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in liboapve_encode() in libavcodec/liboapvenc.c that… |
| 2026-11-09 19:16:55 | [CVE-2026-125197](https://nvd.nist.gov/vuln/detail/CVE-2026-125197) | Medium | 6.9 | FFmpeg through 9.0.2 contains an integer underflow in decode_frame() in libavcodec/lcldec.c that allows attackers to tr… |
| 2026-11-09 19:16:55 | [CVE-2026-125198](https://nvd.nist.gov/vuln/detail/CVE-2026-125198) | Low | 2.0 | FFmpeg through 9.0.2 contains a memory leak vulnerability in mediaformat_jni_setBuffer() in libavcodec/mediacodec_wrapp… |
| 2026-11-09 19:16:56 | [CVE-2026-125199](https://nvd.nist.gov/vuln/detail/CVE-2026-125199) | Medium | 6.8 | FFmpeg through 9.0.2 contains a memory leak vulnerability in vc1_decode_frame() in libavcodec/vc1dec.c that leaks slice… |
| 2026-11-09 19:16:56 | [CVE-2026-125200](https://nvd.nist.gov/vuln/detail/CVE-2026-125200) | Medium | 6.8 | FFmpeg through 9.0.2 contains a memory leak vulnerability in libavcodec/libx265.c because libx265_encode_frame() never… |
| 2026-11-09 19:16:56 | [CVE-2026-125201](https://nvd.nist.gov/vuln/detail/CVE-2026-125201) | High | 7.3 | FFmpeg 7.0 before 8.1.3 and 9.x before 9.0.2 contains a heap out-of-bounds write vulnerability in vk_av1_decode_slice()… |
| 2026-11-09 19:16:56 | [CVE-2026-125202](https://nvd.nist.gov/vuln/detail/CVE-2026-125202) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in vaapi_hevc_start_frame() in libavcodec/vaapi_hevc… |
| 2026-11-09 19:16:56 | [CVE-2026-125203](https://nvd.nist.gov/vuln/detail/CVE-2026-125203) | High | 8.5 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains a heap buffer overflow vulnerability in the Cook multichannel decoder… |
| 2026-11-09 19:16:56 | [CVE-2026-125204](https://nvd.nist.gov/vuln/detail/CVE-2026-125204) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow in ff_libwebp_get_frame() in libwebpenc_common.c that lets attacke… |
| 2026-11-09 19:16:57 | [CVE-2026-125205](https://nvd.nist.gov/vuln/detail/CVE-2026-125205) | Medium | 6.8 | FFmpeg through 9.0.2 contains an unbounded memory allocation vulnerability in the av1_frame_merge bitstream filter that… |
| 2026-11-09 19:16:57 | [CVE-2026-125206](https://nvd.nist.gov/vuln/detail/CVE-2026-125206) | Low | 2.0 | FFmpeg through 9.0.2 contains an out-of-bounds read vulnerability in the prores_ks encoder's get_alpha_data() that read… |
| 2026-11-09 19:16:57 | [CVE-2026-125207](https://nvd.nist.gov/vuln/detail/CVE-2026-125207) | Medium | 6.8 | FFmpeg through 9.0.2 contains an uncontrolled memory allocation vulnerability in the Interplay ACM decoder that allows… |
| 2026-11-09 19:16:57 | [CVE-2026-125208](https://nvd.nist.gov/vuln/detail/CVE-2026-125208) | High | 7.3 | FFmpeg through 9.0.2 contains an out-of-bounds write vulnerability in v4l2_buffer_swframe_to_buf() in libavcodec/v4l2_b… |
| 2026-11-09 19:16:57 | [CVE-2026-125209](https://nvd.nist.gov/vuln/detail/CVE-2026-125209) | High | 8.5 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains a heap buffer overflow vulnerability in the DVD subtitle encoder that… |
| 2026-11-09 19:16:57 | [CVE-2026-125210](https://nvd.nist.gov/vuln/detail/CVE-2026-125210) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in aribcaption_trans_text_subtitle() in libavcodec/l… |
| 2026-11-09 19:16:57 | [CVE-2026-125211](https://nvd.nist.gov/vuln/detail/CVE-2026-125211) | High | 7.3 | FFmpeg through 9.0.2 contains an out-of-bounds read and invalid free vulnerability in aribcaption_trans_ass_subtitle()… |
| 2026-11-09 19:16:58 | [CVE-2026-125212](https://nvd.nist.gov/vuln/detail/CVE-2026-125212) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in libavcodec/videotoolboxenc.c that copies frames l… |
| 2026-11-09 19:16:58 | [CVE-2026-125213](https://nvd.nist.gov/vuln/detail/CVE-2026-125213) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in the PSD decoder in libavcodec/psd.c that allows a… |
| 2026-11-09 19:16:58 | [CVE-2026-125214](https://nvd.nist.gov/vuln/detail/CVE-2026-125214) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in pcm_bluray_decode_frame() in libavcodec/pcm-blura… |
| 2026-11-09 19:16:58 | [CVE-2026-125215](https://nvd.nist.gov/vuln/detail/CVE-2026-125215) | Medium | 5.7 | FFmpeg 7.1 through 9.0.2 contains a NULL pointer dereference vulnerability in ff_dovi_rpu_generate() in libavcodec/dovi… |
| 2026-11-09 19:16:58 | [CVE-2026-125216](https://nvd.nist.gov/vuln/detail/CVE-2026-125216) | Medium | 6.8 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in libavcodec/dpxenc.c that allows attackers to… |
| 2026-11-09 19:16:58 | [CVE-2026-125217](https://nvd.nist.gov/vuln/detail/CVE-2026-125217) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory use vulnerability in roq_dpcm_encode_frame() in libavcodec/roqaud… |
| 2026-11-09 19:16:59 | [CVE-2026-125218](https://nvd.nist.gov/vuln/detail/CVE-2026-125218) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in the APNG encoder's encode_apng() function in liba… |
| 2026-11-09 19:16:59 | [CVE-2026-125219](https://nvd.nist.gov/vuln/detail/CVE-2026-125219) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in vdpau_hevc_start_frame() in libavcodec/vdpau_hevc… |
| 2026-11-09 19:16:59 | [CVE-2026-125220](https://nvd.nist.gov/vuln/detail/CVE-2026-125220) | Medium | 6.8 | FFmpeg through 9.0.2 contains a deadlock vulnerability in mimic_decode_frame() in libavcodec/mimic.c that fails to repo… |
| 2026-11-09 19:16:59 | [CVE-2026-125221](https://nvd.nist.gov/vuln/detail/CVE-2026-125221) | Medium | 6.8 | FFmpeg through 9.0.2 contains an uncontrolled recursion vulnerability in score_header() in libavcodec/flac_parser.c tha… |
| 2026-11-09 19:16:59 | [CVE-2026-125222](https://nvd.nist.gov/vuln/detail/CVE-2026-125222) | High | 7.3 | FFmpeg through 9.0.2 contains an integer overflow vulnerability in hap_parse_frame_header() in libavcodec/hapdec.c that… |
| 2026-11-09 19:16:59 | [CVE-2026-125223](https://nvd.nist.gov/vuln/detail/CVE-2026-125223) | Medium | 5.7 | FFmpeg 8.0 through 9.0.2 contains a memory leak vulnerability in the VP9 decoder that allows attackers to exhaust memor… |
| 2026-11-09 19:16:59 | [CVE-2026-125224](https://nvd.nist.gov/vuln/detail/CVE-2026-125224) | Medium | 6.8 | FFmpeg through 9.0.2 contains a denial of service vulnerability in libavcodec/vorbis_parser.c that re-parses invalid ex… |
| 2026-11-09 19:17:00 | [CVE-2026-125225](https://nvd.nist.gov/vuln/detail/CVE-2026-125225) | Medium | 6.8 | FFmpeg through 9.0.2 contains a NULL pointer dereference vulnerability in aac_adtstoasc_filter() that allows attackers… |
| 2026-11-09 19:17:00 | [CVE-2026-125226](https://nvd.nist.gov/vuln/detail/CVE-2026-125226) | Medium | 6.8 | FFmpeg through 9.0.2 contains an uncontrolled memory allocation vulnerability in sbg_read_header() in libavformat/sbgde… |
| 2026-11-09 19:17:00 | [CVE-2026-125227](https://nvd.nist.gov/vuln/detail/CVE-2026-125227) | High | 7.3 | FFmpeg through 9.0.2 contains an integer overflow in cbs_jpeg_write_scan() in libavcodec/cbs_jpeg.c that causes a heap… |
| 2026-11-09 19:17:00 | [CVE-2026-125228](https://nvd.nist.gov/vuln/detail/CVE-2026-125228) | Medium | 5.8 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains an out-of-bounds read vulnerability in put_vector() in libavcodec/vor… |
| 2026-11-09 19:17:00 | [CVE-2026-125229](https://nvd.nist.gov/vuln/detail/CVE-2026-125229) | High | 8.5 | FFmpeg through 9.0.2 contains an out-of-bounds memory access vulnerability in the encode_frame() function of libavcodec… |
| 2026-11-09 19:17:00 | [CVE-2026-125230](https://nvd.nist.gov/vuln/detail/CVE-2026-125230) | Medium | 6.8 | FFmpeg through 9.0.2 contains an integer overflow vulnerability in the pcm_rechunk bitstream filter that allows attacke… |
| 2026-11-09 19:17:00 | [CVE-2026-125231](https://nvd.nist.gov/vuln/detail/CVE-2026-125231) | Medium | 6.8 | FFmpeg 4.4 through 9.0.2 contains a NULL pointer dereference vulnerability in libavcodec/adxdec.c because adx_decode_he… |
| 2026-11-09 19:17:01 | [CVE-2026-125232](https://nvd.nist.gov/vuln/detail/CVE-2026-125232) | Medium | 6.8 | FFmpeg through 9.0.2 contains a division by zero vulnerability in estimate_motion_b() in libavcodec/motion_est.c, cause… |
| 2026-11-09 19:17:01 | [CVE-2026-125233](https://nvd.nist.gov/vuln/detail/CVE-2026-125233) | High | 8.5 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in dvbsub_encode() in libavcodec/dvbsubenc.c that un… |
| 2026-11-09 19:17:01 | [CVE-2026-125234](https://nvd.nist.gov/vuln/detail/CVE-2026-125234) | Medium | 6.8 | FFmpeg through 9.0.2 contains an integer overflow vulnerability in wavpack_encode_init() in libavcodec/wavpackenc.c tha… |
| 2026-11-09 19:17:01 | [CVE-2026-125235](https://nvd.nist.gov/vuln/detail/CVE-2026-125235) | High | 7.3 | FFmpeg through 9.0.2 contains a heap overflow vulnerability in libavcodec/qsvenc.c that allows attackers to corrupt mem… |
| 2026-11-09 19:17:01 | [CVE-2026-125236](https://nvd.nist.gov/vuln/detail/CVE-2026-125236) | Medium | 4.8 | FFmpeg through 9.0.2 contains a memory leak vulnerability in alloc_frame() in libavcodec/vvc/refs.c that leaks SPS and… |
| 2026-11-09 19:17:01 | [CVE-2026-125237](https://nvd.nist.gov/vuln/detail/CVE-2026-125237) | Medium | 5.7 | FFmpeg 8.1 through 9.0.2 contains a denial of service vulnerability in libavcodec/dpx.c that leaves dpx->hwaccel_pictur… |
| 2026-11-09 19:17:02 | [CVE-2026-125238](https://nvd.nist.gov/vuln/detail/CVE-2026-125238) | Medium | 6.8 | FFmpeg through 9.0.2 contains a reachable assertion vulnerability in libxevd_receive_frame() in libavcodec/libxevd.c th… |
| 2026-11-09 19:17:02 | [CVE-2026-125239](https://nvd.nist.gov/vuln/detail/CVE-2026-125239) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in ff_dxva2_hevc_fill_picture_parameters() that allo… |
| 2026-11-09 19:17:02 | [CVE-2026-125240](https://nvd.nist.gov/vuln/detail/CVE-2026-125240) | Medium | 6.8 | FFmpeg through 9.0.2 contains a resource leak vulnerability in svt_jpegxs_dec_decode() in libsvtjpegxsdec.c that leaks… |
| 2026-11-09 19:17:02 | [CVE-2026-125241](https://nvd.nist.gov/vuln/detail/CVE-2026-125241) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in libavcodec/flicvideo.c that allows attackers to w… |
| 2026-11-09 19:17:02 | [CVE-2026-125242](https://nvd.nist.gov/vuln/detail/CVE-2026-125242) | Medium | 5.7 | FFmpeg through 9.0.2 contains a memory leak vulnerability in libavcodec/vdpau.c that allows attackers to exhaust heap m… |
| 2026-11-09 19:17:02 | [CVE-2026-125243](https://nvd.nist.gov/vuln/detail/CVE-2026-125243) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory disclosure vulnerability in ff_jpegls_decode_picture() in libavco… |
| 2026-11-09 19:17:02 | [CVE-2026-125244](https://nvd.nist.gov/vuln/detail/CVE-2026-125244) | High | 8.5 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains an out-of-bounds write vulnerability in the VVC decoder's sh_entry_po… |
| 2026-11-09 19:17:03 | [CVE-2026-125245](https://nvd.nist.gov/vuln/detail/CVE-2026-125245) | Medium | 5.7 | FFmpeg through 9.0.2 contains a memory leak vulnerability in ff_mjpeg_decode_sof() in libavcodec/mjpegdec.c, which over… |
| 2026-11-09 19:17:03 | [CVE-2026-125246](https://nvd.nist.gov/vuln/detail/CVE-2026-125246) | Medium | 5.7 | FFmpeg through 9.0.2 contains a denial of service vulnerability in cbs_jpeg_assemble_fragment() that miscounts 0xff stu… |
| 2026-11-09 19:17:03 | [CVE-2026-125247](https://nvd.nist.gov/vuln/detail/CVE-2026-125247) | Medium | 4.8 | FFmpeg through 9.0.2 contains an integer overflow vulnerability in dng_decode_tiles() that allows attackers to leak uni… |
| 2026-11-09 19:17:03 | [CVE-2026-125248](https://nvd.nist.gov/vuln/detail/CVE-2026-125248) | High | 7.3 | FFmpeg 9.0 through 9.0.2 contains an integer overflow vulnerability in libavcodec/ffv1enc_vulkan.c that undersizes the… |
| 2026-11-09 19:17:03 | [CVE-2026-125249](https://nvd.nist.gov/vuln/detail/CVE-2026-125249) | High | 7.3 | FFmpeg 7.1 through 9.0.2 contains an integer overflow in ff_vk_decode_add_slice() in libavcodec/vulkan_decode.c that mi… |
| 2026-11-09 19:17:03 | [CVE-2026-125250](https://nvd.nist.gov/vuln/detail/CVE-2026-125250) | High | 8.5 | FFmpeg through 9.0.2 contains a heap buffer overflow in the GIF encoder's gif_image_write_image() in libavcodec/gif.c b… |
| 2026-11-09 19:17:04 | [CVE-2026-125251](https://nvd.nist.gov/vuln/detail/CVE-2026-125251) | High | 7.3 | FFmpeg through 9.0.2 contains an integer overflow vulnerability in the VVC decoder alloc_frame() function in libavcodec… |
| 2026-11-09 19:17:04 | [CVE-2026-12977](https://nvd.nist.gov/vuln/detail/CVE-2026-12977) | High | 8.8 | A flaw was found in the deployment-operation family of WildFly Core. Certain handlers, such as upload-deployment-url, l… |
| 2026-11-09 19:17:05 | [CVE-2026-70555](https://nvd.nist.gov/vuln/detail/CVE-2026-70555) | High | 7.1 | rConfig Core 8.2.3 before 8.2.13 contains an information disclosure vulnerability that allows authenticated users to re… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
