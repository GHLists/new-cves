# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 04:18 UTC

New CVEs published between 2026-11-24 03:18 UTC and 2026-11-24 04:18 UTC.

[Full CSV](data/new-cves-2026-11-24T04-18-39-368544Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 04:17:22 | [CVE-2026-128791](https://nvd.nist.gov/vuln/detail/CVE-2026-128791) | Critical | 10.0 | Any WiFi client can send HTTP DELETE to /meeting-recording/delete to permanently delete files without authentication. |
| 2026-11-24 04:17:26 | [CVE-2026-134880](https://nvd.nist.gov/vuln/detail/CVE-2026-134880) |  |  | XML::Sig versions before 0.74 for Perl allow code execution via a document's Algorithm attribute that verify resolves t… |
| 2026-11-24 04:17:26 | [CVE-2026-135455](https://nvd.nist.gov/vuln/detail/CVE-2026-135455) | Low | 2.0 | A vulnerability was determined in amirhamza05 Student-Management-System up to 449397e35d42e3779f14f0bfc654ab307103f7e3.… |
| 2026-11-24 04:17:26 | [CVE-2026-135456](https://nvd.nist.gov/vuln/detail/CVE-2026-135456) | Low | 2.1 | A vulnerability was identified in amirhamza05 Student-Management-System up to 449397e35d42e3779f14f0bfc654ab307103f7e3.… |
| 2026-11-24 04:17:26 | [CVE-2026-135703](https://nvd.nist.gov/vuln/detail/CVE-2026-135703) | Medium | 4.8 | FFmpeg before 9.1 contains an uninitialized memory use vulnerability in asfrtp_parse_packet() in libavformat/rtpdec_asf… |
| 2026-11-24 04:17:26 | [CVE-2026-135704](https://nvd.nist.gov/vuln/detail/CVE-2026-135704) | Medium | 4.8 | FFmpeg before 9.1 contains an information disclosure vulnerability in the MXG demuxer's mxg_read_packet() that allows a… |
| 2026-11-24 04:17:27 | [CVE-2026-135705](https://nvd.nist.gov/vuln/detail/CVE-2026-135705) | Medium | 6.9 | FFmpeg before 9.1 contains a stack out-of-bounds read vulnerability in ff_h264_parse_framesize() in libavformat/rtpdec_… |
| 2026-11-24 04:17:27 | [CVE-2026-135706](https://nvd.nist.gov/vuln/detail/CVE-2026-135706) | High | 7.3 | FFmpeg before 9.1 contains a heap buffer overflow vulnerability in modplug_read_header() in libavformat/libmodplug.c th… |
| 2026-11-24 04:17:27 | [CVE-2026-135707](https://nvd.nist.gov/vuln/detail/CVE-2026-135707) | Medium | 4.8 | FFmpeg before 9.1 contains an uninitialized memory vulnerability in nist_read_header() in libavformat/nistspheredec.c,… |
| 2026-11-24 04:17:27 | [CVE-2026-135708](https://nvd.nist.gov/vuln/detail/CVE-2026-135708) | Medium | 6.8 | FFmpeg 8.0 before 9.1 contains an improper URL scheme validation vulnerability in the WHIP muxer that allows malicious… |
| 2026-11-24 04:17:27 | [CVE-2026-135709](https://nvd.nist.gov/vuln/detail/CVE-2026-135709) | High | 7.3 | FFmpeg before 9.1 contains an out-of-bounds write vulnerability in ogg_buffer_data() in libavformat/oggenc.c because og… |
| 2026-11-24 04:17:28 | [CVE-2026-135710](https://nvd.nist.gov/vuln/detail/CVE-2026-135710) | Medium | 4.8 | FFmpeg before 9.1 contains an uninitialized memory disclosure vulnerability in vmd_read_packet() in libavformat/sierrav… |
| 2026-11-24 04:17:28 | [CVE-2026-135711](https://nvd.nist.gov/vuln/detail/CVE-2026-135711) | Medium | 4.8 | FFmpeg before 9.1 contains an XML injection vulnerability in ttml_write_header() in libavformat/ttmlenc.c that writes s… |
| 2026-11-24 04:17:28 | [CVE-2026-135712](https://nvd.nist.gov/vuln/detail/CVE-2026-135712) | Medium | 6.9 | FFmpeg before 9.1 contains an integer overflow vulnerability in the split_planes size check of write_packet() in libavf… |
| 2026-11-24 04:17:28 | [CVE-2026-135713](https://nvd.nist.gov/vuln/detail/CVE-2026-135713) | Medium | 6.8 | FFmpeg before 9.1 contains a NULL pointer dereference vulnerability in libavformat/mmst.c that allows malicious MMS ser… |
| 2026-11-24 04:17:28 | [CVE-2026-135714](https://nvd.nist.gov/vuln/detail/CVE-2026-135714) | Medium | 4.8 | FFmpeg before 9.1 contains an information disclosure vulnerability in amf_get_field_value2() in libavformat/rtmppkt.c t… |
| 2026-11-24 04:17:28 | [CVE-2026-135715](https://nvd.nist.gov/vuln/detail/CVE-2026-135715) | Medium | 6.8 | FFmpeg before 9.1 contains a NULL pointer dereference vulnerability in the AVIF muxer in libavformat/movenc.c that allo… |
| 2026-11-24 04:17:29 | [CVE-2026-135716](https://nvd.nist.gov/vuln/detail/CVE-2026-135716) | Medium | 6.9 | FFmpeg before 9.1 contains an out-of-bounds write vulnerability in build_frame_code() in libavformat/nutenc.c that allo… |
| 2026-11-24 04:17:29 | [CVE-2026-135717](https://nvd.nist.gov/vuln/detail/CVE-2026-135717) | Low | 2.0 | FFmpeg 8.0 before 9.1 contains a use of uninitialized memory vulnerability in opus_parse_packet() in libavformat/rtpdec… |
| 2026-11-24 04:17:29 | [CVE-2026-135718](https://nvd.nist.gov/vuln/detail/CVE-2026-135718) | Medium | 6.8 | FFmpeg 7.0 before 9.1 contains an out-of-bounds read vulnerability in dvdvideo_audio_stream_add_all() in libavformat/dv… |
| 2026-11-24 04:17:29 | [CVE-2026-135719](https://nvd.nist.gov/vuln/detail/CVE-2026-135719) | Low | 2.0 | FFmpeg before 9.1 contains an uninitialized memory disclosure vulnerability in dxa_read_packet() in libavformat/dxa.c t… |
| 2026-11-24 04:17:29 | [CVE-2026-135720](https://nvd.nist.gov/vuln/detail/CVE-2026-135720) | Medium | 6.8 | FFmpeg 9.0 before 9.1 contains a NULL pointer dereference vulnerability in dash_read_header() in libavformat/dashdec.c… |
| 2026-11-24 04:17:29 | [CVE-2026-135721](https://nvd.nist.gov/vuln/detail/CVE-2026-135721) | Medium | 6.8 | FFmpeg before 9.1 contains an infinite loop vulnerability in ff_rtp_send_vc2hq() in libavformat/rtpenc_vc2hq.c that acc… |
| 2026-11-24 04:17:30 | [CVE-2026-135722](https://nvd.nist.gov/vuln/detail/CVE-2026-135722) | High | 8.5 | FFmpeg before 9.1 contains a heap-based buffer overflow vulnerability in peak_init_writer() and wav_write_packet() in l… |
| 2026-11-24 04:17:30 | [CVE-2026-135723](https://nvd.nist.gov/vuln/detail/CVE-2026-135723) | High | 7.3 | FFmpeg before 9.1 contains a double free vulnerability in the fill_marker() function of libavformat/imf_cpl.c that free… |
| 2026-11-24 04:17:30 | [CVE-2026-135724](https://nvd.nist.gov/vuln/detail/CVE-2026-135724) | Medium | 5.7 | FFmpeg before 9.1 contains a NULL pointer dereference vulnerability in avformat_stream_group_create() in libavformat/op… |
| 2026-11-24 04:17:30 | [CVE-2026-135725](https://nvd.nist.gov/vuln/detail/CVE-2026-135725) | High | 8.5 | FFmpeg before 9.1 contains a stack-based buffer overflow vulnerability in ff_rtmp_packet_write() in libavformat/rtmppkt… |
| 2026-11-24 04:17:30 | [CVE-2026-135726](https://nvd.nist.gov/vuln/detail/CVE-2026-135726) | Medium | 6.8 | FFmpeg before 9.1 contains a NULL pointer dereference vulnerability in rdt_parse_packet() in libavformat/rdt.c that all… |
| 2026-11-24 04:17:30 | [CVE-2026-135727](https://nvd.nist.gov/vuln/detail/CVE-2026-135727) | Medium | 4.8 | FFmpeg before 9.1 contains an uninitialized memory disclosure vulnerability in rfc4175_handle_packet() in libavformat/r… |
| 2026-11-24 04:17:31 | [CVE-2026-135729](https://nvd.nist.gov/vuln/detail/CVE-2026-135729) | Medium | 4.8 | FFmpeg before 9.1 contains an XML injection vulnerability in write_adaptation_set() in libavformat/webmdashenc.c that w… |
| 2026-11-24 04:17:31 | [CVE-2026-135730](https://nvd.nist.gov/vuln/detail/CVE-2026-135730) | Medium | 4.8 | FFmpeg before 9.1 contains an uninitialized memory vulnerability in vpk_read_header() in libavformat/vpk.c that compute… |
| 2026-11-24 04:17:31 | [CVE-2026-135731](https://nvd.nist.gov/vuln/detail/CVE-2026-135731) | Medium | 6.8 | FFmpeg before 9.1 contains an integer overflow in send_picture() of libavformat/rtpenc_vc2hq.c that leaves the bit read… |
| 2026-11-24 04:17:31 | [CVE-2026-135732](https://nvd.nist.gov/vuln/detail/CVE-2026-135732) | Medium | 6.9 | FFmpeg before 9.1 contains an out-of-bounds read vulnerability in mxf_write_d10_audio_packet() in libavformat/mxfenc.c… |
| 2026-11-24 04:17:31 | [CVE-2026-135733](https://nvd.nist.gov/vuln/detail/CVE-2026-135733) | Medium | 6.9 | FFmpeg through 9.1 contains an insecure default configuration in the zmq and azmq filters of libavfilter/f_zmq.c that b… |
| 2026-11-24 04:17:31 | [CVE-2026-135728](https://nvd.nist.gov/vuln/detail/CVE-2026-135728) | Medium | 5.7 | FFmpeg before 9.1 contains a signed integer overflow vulnerability in libavformat/dashdec.c that allows attackers to cr… |
| 2026-11-24 04:17:32 | [CVE-2026-135734](https://nvd.nist.gov/vuln/detail/CVE-2026-135734) | High | 8.5 | FFmpeg before 9.1 contains a heap out-of-bounds write vulnerability in the deflicker filter that lets attackers corrupt… |
| 2026-11-24 04:17:32 | [CVE-2026-135735](https://nvd.nist.gov/vuln/detail/CVE-2026-135735) | Medium | 6.9 | FFmpeg before 9.1 contains a heap out-of-bounds read vulnerability in filter_slice_rgba_planar() that allows attackers… |
| 2026-11-24 04:17:32 | [CVE-2026-135736](https://nvd.nist.gov/vuln/detail/CVE-2026-135736) | Critical | 9.2 | FFmpeg 4.4 before 9.1 contains a heap out-of-bounds read and write vulnerability in libavfilter/vf_deband.c that allows… |
| 2026-11-24 04:17:32 | [CVE-2026-135737](https://nvd.nist.gov/vuln/detail/CVE-2026-135737) | High | 8.5 | FFmpeg before 9.1 contains a heap out-of-bounds write and read vulnerability in the tmidequalizer filter that allows at… |
| 2026-11-24 04:17:32 | [CVE-2026-135738](https://nvd.nist.gov/vuln/detail/CVE-2026-135738) | High | 8.5 | FFmpeg before 9.1 contains a heap out-of-bounds write vulnerability in libavfilter/vf_signalstats.c that allows attacke… |
| 2026-11-24 04:17:32 | [CVE-2026-135739](https://nvd.nist.gov/vuln/detail/CVE-2026-135739) | High | 8.3 | FFmpeg 7.1 before 9.1 contains an out-of-bounds read vulnerability in libavfilter/vf_scale.c that allows attackers to r… |
| 2026-11-24 04:17:33 | [CVE-2026-135740](https://nvd.nist.gov/vuln/detail/CVE-2026-135740) | High | 8.5 | FFmpeg before 9.1 contains a heap out-of-bounds write vulnerability in libavfilter/vf_readeia608.c because build_histog… |
| 2026-11-24 04:17:33 | [CVE-2026-135741](https://nvd.nist.gov/vuln/detail/CVE-2026-135741) | Medium | 5.8 | FFmpeg before 9.1 contains a heap out-of-bounds read vulnerability in libavfilter/vf_lut2.c because the second input's… |
| 2026-11-24 04:17:33 | [CVE-2026-135742](https://nvd.nist.gov/vuln/detail/CVE-2026-135742) | High | 8.7 | FFmpeg before 9.1 contains a heap buffer overflow vulnerability in recv_msg() of the zmq and azmq filters that allows u… |
| 2026-11-24 04:17:33 | [CVE-2026-135743](https://nvd.nist.gov/vuln/detail/CVE-2026-135743) | Critical | 9.2 | FFmpeg 4.3 before 9.1 contains a heap out-of-bounds read and write vulnerability in the dynaudnorm filter because cqueu… |
| 2026-11-24 04:17:33 | [CVE-2026-135744](https://nvd.nist.gov/vuln/detail/CVE-2026-135744) | Medium | 5.8 | FFmpeg before 9.1 contains an out-of-bounds read vulnerability in the lut1d filter in libavfilter/vf_lut3d.c that allow… |
| 2026-11-24 04:17:33 | [CVE-2026-135745](https://nvd.nist.gov/vuln/detail/CVE-2026-135745) | Medium | 6.9 | FFmpeg before 9.1 contains a heap out-of-bounds read vulnerability in the curves filter in libavfilter/vf_curves.c that… |
| 2026-11-24 04:17:34 | [CVE-2026-135746](https://nvd.nist.gov/vuln/detail/CVE-2026-135746) | Medium | 6.8 | An off-by-one error in String::WriteOneByte() in Samsung lwnode can cause a one-byte out-of-bounds write when copying a… |
| 2026-11-24 04:17:38 | [CVE-2026-9790](https://nvd.nist.gov/vuln/detail/CVE-2026-9790) | Critical | 10.0 | Endpoints accessible without authentication from any WiFi client (e.g., /user/hasSimCard, /user/pooling, /api/device-in… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
