# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 20:19 UTC

New CVEs published between 2026-11-09 19:18 UTC and 2026-11-09 20:19 UTC.

[Full CSV](data/new-cves-2026-11-09T20-19-28-48934Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 20:18:04 | [CVE-2026-119078](https://nvd.nist.gov/vuln/detail/CVE-2026-119078) |  |  | Apache Commons Codec's Blake3 class documented the output of its doFinalize methods as depending on any previously fina… |
| 2026-11-09 20:18:10 | [CVE-2026-123805](https://nvd.nist.gov/vuln/detail/CVE-2026-123805) | High | 7.5 | SIPSorcery is a WebRTC, SIP, and VoIP library for C# and .NET. Prior to 10.0.14, SctpSackChunk.ParseChunk reads the num… |
| 2026-11-09 20:18:10 | [CVE-2026-124077](https://nvd.nist.gov/vuln/detail/CVE-2026-124077) |  |  | The GitIdentifiers class in Apache Commons Codec did not reject NUL bytes in tree entry names. Because Git uses a NUL b… |
| 2026-11-09 20:18:10 | [CVE-2026-124834](https://nvd.nist.gov/vuln/detail/CVE-2026-124834) | Medium | 6.3 | A security vulnerability has been detected in iomad up to 4.5.15/5.0.11/5.1.8/5.2.4. Affected by this issue is the func… |
| 2026-11-09 20:18:10 | [CVE-2026-124987](https://nvd.nist.gov/vuln/detail/CVE-2026-124987) | Low | 2.1 | A vulnerability has been found in mikefarah yq up to 4.53.3. This affects the function Encode of the file pkg/yqlib/enc… |
| 2026-11-09 20:18:11 | [CVE-2026-125252](https://nvd.nist.gov/vuln/detail/CVE-2026-125252) | Medium | 5.7 | FFmpeg through 9.0.2 contains a memory leak vulnerability in libavcodec/vaapi_decode.c that allows attackers to exhaust… |
| 2026-11-09 20:18:11 | [CVE-2026-125253](https://nvd.nist.gov/vuln/detail/CVE-2026-125253) | Medium | 5.8 | FFmpeg through 9.0.2 contains an integer overflow in cbs_vp9_split_fragment() in libavcodec/cbs_vp9.c that wraps the su… |
| 2026-11-09 20:18:11 | [CVE-2026-125254](https://nvd.nist.gov/vuln/detail/CVE-2026-125254) | Medium | 6.8 | FFmpeg through 9.0.2 contains a division by zero vulnerability in the VVC decoder because ff_vvc_slice_rpl() fails to v… |
| 2026-11-09 20:18:11 | [CVE-2026-125255](https://nvd.nist.gov/vuln/detail/CVE-2026-125255) | Medium | 5.8 | FFmpeg through 9.0.2 contains a use after free vulnerability in libavcodec/mjpegdec.c that allows attackers to trigger… |
| 2026-11-09 20:18:11 | [CVE-2026-125256](https://nvd.nist.gov/vuln/detail/CVE-2026-125256) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in ff_llvidenc_diff_bytes_rvv() that allows attacker… |
| 2026-11-09 20:18:11 | [CVE-2026-125257](https://nvd.nist.gov/vuln/detail/CVE-2026-125257) | High | 7.3 | FFmpeg through 9.0.2 contains an off-by-one heap overflow vulnerability in get_exponent_dynamic() in libavcodec/nellymo… |
| 2026-11-09 20:18:12 | [CVE-2026-125258](https://nvd.nist.gov/vuln/detail/CVE-2026-125258) | Medium | 5.7 | FFmpeg through 9.0.2 contains a division by zero vulnerability in dovi_configure_ext() in libavcodec/dovi_rpuenc.c that… |
| 2026-11-09 20:18:12 | [CVE-2026-125259](https://nvd.nist.gov/vuln/detail/CVE-2026-125259) | High | 8.5 | FFmpeg through 9.0.2 contains an integer overflow vulnerability in ff_prores_kostya_encode_init() that miscalculates fr… |
| 2026-11-09 20:18:12 | [CVE-2026-125260](https://nvd.nist.gov/vuln/detail/CVE-2026-125260) | High | 7.3 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in libavcodec/exrenc.c that allows attackers to corr… |
| 2026-11-09 20:18:12 | [CVE-2026-125261](https://nvd.nist.gov/vuln/detail/CVE-2026-125261) | Medium | 6.9 | FFmpeg through 9.0.2 contains an out-of-bounds read vulnerability in the SGI encoder's encode_frame() in libavcodec/sgi… |
| 2026-11-09 20:18:12 | [CVE-2026-125262](https://nvd.nist.gov/vuln/detail/CVE-2026-125262) | High | 8.5 | FFmpeg through 9.0.2 contains a heap buffer overflow vulnerability in libavcodec/lcevcdec.c because LCEVC output pictur… |
| 2026-11-09 20:18:12 | [CVE-2026-125263](https://nvd.nist.gov/vuln/detail/CVE-2026-125263) | Medium | 5.7 | FFmpeg 9.0 through 9.0.2 built with liblcevc_dec fails to validate LCEVC enhanced output dimensions against max_pixels… |
| 2026-11-09 20:18:12 | [CVE-2026-125264](https://nvd.nist.gov/vuln/detail/CVE-2026-125264) | Medium | 6.8 | FFmpeg through 9.0.2 contains an uncontrolled resource consumption vulnerability in parse_frame_header() in libavcodec/… |
| 2026-11-09 20:18:13 | [CVE-2026-125265](https://nvd.nist.gov/vuln/detail/CVE-2026-125265) | Medium | 5.8 | FFmpeg through 9.0.2 contains a use-after-free vulnerability in libavcodec/nvdec.c because ff_nvdec_start_frame() fails… |
| 2026-11-09 20:18:13 | [CVE-2026-125266](https://nvd.nist.gov/vuln/detail/CVE-2026-125266) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized stack memory disclosure vulnerability in old_codec23() of libavcodec/san… |
| 2026-11-09 20:18:13 | [CVE-2026-125267](https://nvd.nist.gov/vuln/detail/CVE-2026-125267) | High | 8.5 | FFmpeg before 8.1.3 and 9.x before 9.0.2 contains a heap out-of-bounds write vulnerability in the APAC decoder in libav… |
| 2026-11-09 20:18:13 | [CVE-2026-125268](https://nvd.nist.gov/vuln/detail/CVE-2026-125268) | Medium | 4.8 | FFmpeg through 9.0.2 contains an uninitialized memory disclosure vulnerability in the CineForm HD decoder that allows a… |
| 2026-11-09 20:18:13 | [CVE-2026-125269](https://nvd.nist.gov/vuln/detail/CVE-2026-125269) | High | 7.3 | FFmpeg through 9.0.2 contains a double free vulnerability in libavcodec/cbs_sei.c where cbs_sei_delete_message() leaves… |
| 2026-11-09 20:18:13 | [CVE-2026-125270](https://nvd.nist.gov/vuln/detail/CVE-2026-125270) | Medium | 5.8 | FFmpeg through 9.0.2 contains a heap out-of-bounds read vulnerability in v4l2_buffer_swframe_to_buf() in libavcodec/v4l… |
| 2026-11-09 20:18:14 | [CVE-2026-87857](https://nvd.nist.gov/vuln/detail/CVE-2026-87857) | Medium | 5.3 | Temporal Server does not bind a workflow-history pagination token to the namespace and workflow named in the request th… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
