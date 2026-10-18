# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-18 12:18 UTC

New CVEs published between 2026-10-18 11:18 UTC and 2026-10-18 12:18 UTC.

[Full CSV](data/new-cves-2026-10-18T12-18-25-180489Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-18 12:17:11 | [CVE-2026-111984](https://nvd.nist.gov/vuln/detail/CVE-2026-111984) | Low | 2.1 | A vulnerability has been found in AUTOMATIC1111 stable-diffusion-webui up to 1.10.1. This affects the function create_i… |
| 2026-10-18 12:17:11 | [CVE-2026-111985](https://nvd.nist.gov/vuln/detail/CVE-2026-111985) | Low | 2.1 | A vulnerability was found in AUTOMATIC1111 stable-diffusion-webui up to 1.10.1. This impacts the function read_metadata… |
| 2026-10-18 12:17:11 | [CVE-2026-111998](https://nvd.nist.gov/vuln/detail/CVE-2026-111998) | Critical | 9.3 | Vanus 0.8.0 through 0.9.0 contains a default credentials vulnerability that allows unauthenticated remote attackers to… |
| 2026-10-18 12:17:11 | [CVE-2026-111999](https://nvd.nist.gov/vuln/detail/CVE-2026-111999) | High | 8.7 | Vanus 0.8.0 through 0.9.0 contains a missing authentication vulnerability that allows unauthenticated remote attackers… |
| 2026-10-18 12:17:12 | [CVE-2026-112000](https://nvd.nist.gov/vuln/detail/CVE-2026-112000) | High | 7.2 | Vanus 0.8.0 through 0.9.0 contains a missing authorization vulnerability in the gateway that allows any authenticated u… |
| 2026-10-18 12:17:12 | [CVE-2026-112001](https://nvd.nist.gov/vuln/detail/CVE-2026-112001) | High | 8.6 | ProjectSend 2.0.0 before 2.7.0 contains an incorrect authorization vulnerability that allows restricted API token holde… |
| 2026-10-18 12:17:12 | [CVE-2026-112002](https://nvd.nist.gov/vuln/detail/CVE-2026-112002) | High | 7.6 | ProjectSend 2.5.0 before 2.7.0 contains an unverified password change vulnerability in PasswordController::update() tha… |
| 2026-10-18 12:17:12 | [CVE-2026-112003](https://nvd.nist.gov/vuln/detail/CVE-2026-112003) | Medium | 6.0 | ProjectSend 2.0.0 before 2.7.0 contains a path validation flaw in OrphanFileScanner::isOrphan() that allows staff with… |
| 2026-10-18 12:17:12 | [CVE-2026-112004](https://nvd.nist.gov/vuln/detail/CVE-2026-112004) | Low | 2.3 | Teable before 2026-10-12T12-45-53Z.3331 contains an authorization bypass vulnerability that allows authenticated users… |
| 2026-10-18 12:17:12 | [CVE-2026-112005](https://nvd.nist.gov/vuln/detail/CVE-2026-112005) | Critical | 9.2 | WhoDB 0.104.0 before 0.135.0 contains a path traversal vulnerability that allows remote attackers to read and write arb… |
| 2026-10-18 12:17:12 | [CVE-2026-112006](https://nvd.nist.gov/vuln/detail/CVE-2026-112006) | High | 8.3 | OpenTelemetry opentelemetry-exporter-otlp-proto-http 1.5.0 before 1.45.0 contains an improper certificate validation vu… |
| 2026-10-18 12:17:13 | [CVE-2026-112007](https://nvd.nist.gov/vuln/detail/CVE-2026-112007) | Medium | 6.9 | Schism Tracker through 20260524 contains a heap out-of-bounds write vulnerability in fmt_ult_load_song() in fmt/ult.c t… |
| 2026-10-18 12:17:13 | [CVE-2026-112008](https://nvd.nist.gov/vuln/detail/CVE-2026-112008) | Medium | 6.9 | libmng through 2.0.3 contains a heap-based buffer overflow vulnerability in mng_read_ordr() that allows attackers to co… |
| 2026-10-18 12:17:13 | [CVE-2026-112009](https://nvd.nist.gov/vuln/detail/CVE-2026-112009) | Medium | 6.8 | smpeg through 2.0.0 contains a heap out-of-bounds read vulnerability in MPEGsystem::FillBuffer() that allows attackers… |
| 2026-10-18 12:17:13 | [CVE-2026-112010](https://nvd.nist.gov/vuln/detail/CVE-2026-112010) | Medium | 6.8 | smpeg through 2.0.0 contains an integer underflow vulnerability in stream_header() in MPEGsystem.cpp that allows attack… |
| 2026-10-18 12:17:13 | [CVE-2026-112011](https://nvd.nist.gov/vuln/detail/CVE-2026-112011) | Medium | 5.8 | libtta through 2.3 contains an integer overflow vulnerability in tta_decoder_init_get_info() that allows attackers to c… |
| 2026-10-18 12:17:13 | [CVE-2026-112012](https://nvd.nist.gov/vuln/detail/CVE-2026-112012) | Medium | 4.8 | libtta through 2.3 contains a stack out-of-bounds read and write vulnerability in tta_decoder_process_stream() and tta_… |
| 2026-10-18 12:17:14 | [CVE-2026-112013](https://nvd.nist.gov/vuln/detail/CVE-2026-112013) | Medium | 6.8 | libtta through 2.3 contains a divide-by-zero vulnerability in tta_decoder_init_get_info() that allows attackers to cras… |
| 2026-10-18 12:17:14 | [CVE-2026-112014](https://nvd.nist.gov/vuln/detail/CVE-2026-112014) | Medium | 6.8 | LobsterAI before 2026.10.16 contains a hardcoded password vulnerability that allows attackers to decrypt exported provi… |
| 2026-10-18 12:17:14 | [CVE-2026-112015](https://nvd.nist.gov/vuln/detail/CVE-2026-112015) | High | 7.7 | Omnigent 0.3.0 before 0.14.0 contains a path traversal vulnerability that allows authenticated users to escape the work… |
| 2026-10-18 12:17:14 | [CVE-2026-112016](https://nvd.nist.gov/vuln/detail/CVE-2026-112016) | Medium | 6.9 | Netcore NR256CN through 1.5.140116 contains an unauthenticated file write vulnerability in the Boa-derived /bin/boa web… |
| 2026-10-18 12:17:14 | [CVE-2026-112017](https://nvd.nist.gov/vuln/detail/CVE-2026-112017) | High | 7.1 | JeecgBoot before 3.9.5 contains an sql injection vulnerability that allows authenticated attackers to bypass the SqlInj… |
| 2026-10-18 12:17:14 | [CVE-2026-112018](https://nvd.nist.gov/vuln/detail/CVE-2026-112018) | High | 7.3 | cgltf through 1.15 contains a heap out-of-bounds write vulnerability in cgltf_accessor_unpack_floats() that allows atta… |
| 2026-10-18 12:17:14 | [CVE-2026-112019](https://nvd.nist.gov/vuln/detail/CVE-2026-112019) | Medium | 6.9 | cgltf through 1.15 contains a heap out-of-bounds read vulnerability in cgltf_accessor_unpack_floats() that advances the… |
| 2026-10-18 12:17:15 | [CVE-2026-112020](https://nvd.nist.gov/vuln/detail/CVE-2026-112020) | Medium | 6.9 | LodePNG through 20261006 contains a heap out-of-bounds read vulnerability in lodepng::getFilterTypesInterlaced() in lod… |
| 2026-10-18 12:17:15 | [CVE-2026-112021](https://nvd.nist.gov/vuln/detail/CVE-2026-112021) | High | 8.7 | snac2 before 2.93 contains a heap-based buffer overflow vulnerability in _xs_json_load_lexer() that allows unauthentica… |
| 2026-10-18 12:17:15 | [CVE-2026-78497](https://nvd.nist.gov/vuln/detail/CVE-2026-78497) |  |  | JQ::Lite versions before 2.51 for Perl execute Perl code embedded in a query's regular expression by compiling it with… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
