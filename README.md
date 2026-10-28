# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-28 18:20 UTC

New CVEs published between 2026-10-28 17:20 UTC and 2026-10-28 18:20 UTC.

[Full CSV](data/new-cves-2026-10-28T18-20-12-790705Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-28 18:17:02 | [CVE-2026-105612](https://nvd.nist.gov/vuln/detail/CVE-2026-105612) | Low | 3.5 | PostgreSQL Anonymizer contains a vulnerability that data-modifying CTEs to bypass the read-only restriction of masked r… |
| 2026-10-28 18:17:03 | [CVE-2026-105614](https://nvd.nist.gov/vuln/detail/CVE-2026-105614) | Medium | 4.7 | PostgreSQL Anonymizer's `anon.image_blur()` function doesn't check the declared dimension of the provided image, allowi… |
| 2026-10-28 18:17:03 | [CVE-2026-105615](https://nvd.nist.gov/vuln/detail/CVE-2026-105615) | Low | 3.5 | PostgreSQL's optimized statistics on a table are visible as long as you have SELECT privilege on said table. A masked r… |
| 2026-10-28 18:17:03 | [CVE-2026-105616](https://nvd.nist.gov/vuln/detail/CVE-2026-105616) | Medium | 5.7 | PostgreSQL restricts acces to the salt and shift via the `SHOW` command for users not member of `pg_read_all_settings`.… |
| 2026-10-28 18:17:03 | [CVE-2026-105617](https://nvd.nist.gov/vuln/detail/CVE-2026-105617) | Medium | 6.5 | PostgreSQL Anonymizer doesn't invalidate plans prepared after a rule was added or a role changed. Users using such plan… |
| 2026-10-28 18:17:03 | [CVE-2026-105618](https://nvd.nist.gov/vuln/detail/CVE-2026-105618) | Medium | 5.7 | PostgreSQL Anonymizer's documentation recommends applying rules on partitions and inheritance tables. Direct access to… |
| 2026-10-28 18:17:03 | [CVE-2026-105619](https://nvd.nist.gov/vuln/detail/CVE-2026-105619) | Medium | 4.8 | PostgreSQL Anonymizer doesn't mask data accessed thru a security_invoker view. The problem is resolved in PostgreSQL An… |
| 2026-10-28 18:17:03 | [CVE-2026-105613](https://nvd.nist.gov/vuln/detail/CVE-2026-105613) | Medium | 4.7 | PostgreSQL Anonymizer's range-based dummy functions dont constraint the range size. This vulnerability can be exploited… |
| 2026-10-28 18:17:04 | [CVE-2026-105620](https://nvd.nist.gov/vuln/detail/CVE-2026-105620) | Medium | 6.5 | PostgreSQL Anonymizer doesn't mask data returned by a sub-query in a rule. The problem is resolved in PostgreSQL Anonym… |
| 2026-10-28 18:17:05 | [CVE-2026-110181](https://nvd.nist.gov/vuln/detail/CVE-2026-110181) | Medium | 6.5 | PostgreSQL Anonymizer contains a vulnerability related to anonymization functions defined using SQL-standard function b… |
| 2026-10-28 18:17:05 | [CVE-2026-110182](https://nvd.nist.gov/vuln/detail/CVE-2026-110182) | Medium | 4.3 | PostgreSQL Anonymizer contains a vulnerability related to the anon.partial() and anon.partial_email() functions. These… |
| 2026-10-28 18:17:05 | [CVE-2026-110183](https://nvd.nist.gov/vuln/detail/CVE-2026-110183) | Medium | 4.3 | PostgreSQL Anonymizer contains a vulnerability related to static masking and statistics persistence. Statistics pertain… |
| 2026-10-28 18:17:12 | [CVE-2026-116131](https://nvd.nist.gov/vuln/detail/CVE-2026-116131) |  |  | HTTP::Body versions before 1.23_01 for Perl allow memory and temporary file exhaustion via an unlimited number of form… |
| 2026-10-28 18:17:12 | [CVE-2026-116132](https://nvd.nist.gov/vuln/detail/CVE-2026-116132) |  |  | HTTP::Body versions before 1.23_01 for Perl leave the temporary file of an incomplete multipart upload on disk. The mul… |
| 2026-10-28 18:17:12 | [CVE-2026-116133](https://nvd.nist.gov/vuln/detail/CVE-2026-116133) |  |  | HTTP::Body versions before 1.23_01 for Perl allow CPU exhaustion via quadratic rescanning of a multipart body with a mi… |
| 2026-10-28 18:17:12 | [CVE-2026-116134](https://nvd.nist.gov/vuln/detail/CVE-2026-116134) |  |  | HTTP::Body versions before 1.23_01 for Perl allow memory exhaustion via an unbounded multipart part header block. The m… |
| 2026-10-28 18:17:12 | [CVE-2026-116135](https://nvd.nist.gov/vuln/detail/CVE-2026-116135) |  |  | HTTP::Body versions before 1.23_01 for Perl drop mixed-case percent escapes from urlencoded form fields instead of deco… |
| 2026-10-28 18:17:12 | [CVE-2026-116264](https://nvd.nist.gov/vuln/detail/CVE-2026-116264) |  |  | MIME::Field::ParamVal versions before 5.521 for Perl allow one invalid Content-Type parameter to hide the parameters af… |
| 2026-10-28 18:17:12 | [CVE-2026-116265](https://nvd.nist.gov/vuln/detail/CVE-2026-116265) |  |  | MIME::Field::ParamVal versions before 5.521 for Perl do not flag an ambiguous multipart boundary written as RFC 2231 co… |
| 2026-10-28 18:17:13 | [CVE-2026-116266](https://nvd.nist.gov/vuln/detail/CVE-2026-116266) |  |  | MIME::Head versions from 5.518 before 5.521 for Perl decode a partly encoded multipart boundary without flagging the pa… |
| 2026-10-28 18:17:13 | [CVE-2026-116267](https://nvd.nist.gov/vuln/detail/CVE-2026-116267) |  |  | MIME::Parser versions before 5.521 for Perl allow memory exhaustion via indented error messages from a truncated, deepl… |
| 2026-10-28 18:17:13 | [CVE-2026-116268](https://nvd.nist.gov/vuln/detail/CVE-2026-116268) |  |  | MIME::Field::ParamVal versions before 5.521 for Perl allow CPU exhaustion via unclosed comments in header parameters. T… |
| 2026-10-28 18:17:13 | [CVE-2026-116269](https://nvd.nist.gov/vuln/detail/CVE-2026-116269) |  |  | MIME::Field::ParamVal versions before 5.521 for Perl turn an RFC 2231 filename with a hyphenated language tag into an e… |
| 2026-10-28 18:17:13 | [CVE-2026-116270](https://nvd.nist.gov/vuln/detail/CVE-2026-116270) |  |  | MIME::Words versions before 5.521 for Perl allow memory exhaustion via repeated "=?" sequences in decode_mimewords. For… |
| 2026-10-28 18:17:13 | [CVE-2026-116271](https://nvd.nist.gov/vuln/detail/CVE-2026-116271) |  |  | MIME::Parser::FileUnder versions before 5.521 for Perl reuse a pre-created output directory and follow symlinks in it,… |
| 2026-10-28 18:17:13 | [CVE-2026-116272](https://nvd.nist.gov/vuln/detail/CVE-2026-116272) |  |  | MIME::Field::ParamVal versions before 5.521 for Perl do not flag a duplicate boundary parameter whose name contains a n… |
| 2026-10-28 18:17:13 | [CVE-2026-116273](https://nvd.nist.gov/vuln/detail/CVE-2026-116273) |  |  | MIME::Parser versions before 5.521 for Perl set no limit on the number of message parts by default, allowing memory exh… |
| 2026-10-28 18:17:13 | [CVE-2026-116285](https://nvd.nist.gov/vuln/detail/CVE-2026-116285) |  |  | HTTP::Body versions before 1.23_01 for Perl allow CPU exhaustion via quadratic regex backtracking when parsing chunked… |
| 2026-10-28 18:17:14 | [CVE-2026-116531](https://nvd.nist.gov/vuln/detail/CVE-2026-116531) |  |  | HTTP::Body versions before 1.23_01 for Perl lose track of chunk boundaries in chunked request bodies when a read ends i… |
| 2026-10-28 18:17:14 | [CVE-2026-116794](https://nvd.nist.gov/vuln/detail/CVE-2026-116794) | High | 8.3 | russh is a Rust SSH client and server library that includes an SSH agent protocol implementation. From 0.50.0-beta.12 u… |
| 2026-10-28 18:17:14 | [CVE-2026-116795](https://nvd.nist.gov/vuln/detail/CVE-2026-116795) | High | 7.5 | RE2JS is the JavaScript port of RE2, a regular expression engine that provides linear time matching. From 2.2.0 until 2… |
| 2026-10-28 18:17:14 | [CVE-2026-116796](https://nvd.nist.gov/vuln/detail/CVE-2026-116796) | High | 7.2 | Highcharts JS is a JavaScript charting library based on SVG. From 10.3.2 until 11.4.9, 12.6.2, and 13.1.1, Highcharts a… |
| 2026-10-28 18:17:14 | [CVE-2026-116797](https://nvd.nist.gov/vuln/detail/CVE-2026-116797) | High | 8.5 | Highcharts JS is a JavaScript charting library based on SVG. From 2.0.0 until 3.2.0, Highcharts Grid Pro input renderer… |
| 2026-10-28 18:17:14 | [CVE-2026-117500](https://nvd.nist.gov/vuln/detail/CVE-2026-117500) |  |  | HTTP::Body versions before 1.24_01 for Perl allow CPU exhaustion via regex backtracking on the filename of a multipart… |
| 2026-10-28 18:17:14 | [CVE-2026-117501](https://nvd.nist.gov/vuln/detail/CVE-2026-117501) |  |  | HTTP::Body versions before 1.24_01 for Perl allow memory exhaustion via unbounded buffering of chunked request bodies.… |
| 2026-10-28 18:17:14 | [CVE-2026-118242](https://nvd.nist.gov/vuln/detail/CVE-2026-118242) | High | 8.5 | Highcharts JS is a JavaScript charting library based on SVG. From 2.3.0 until 3.2.0, Highcharts Grid creates SVG path e… |
| 2026-10-28 18:17:15 | [CVE-2026-118243](https://nvd.nist.gov/vuln/detail/CVE-2026-118243) | Medium | 5.3 | Highcharts JS is a JavaScript charting library based on SVG. From 1.0.0 until 4.2.2, Highcharts Dashboards stores DataC… |
| 2026-10-28 18:17:15 | [CVE-2026-118244](https://nvd.nist.gov/vuln/detail/CVE-2026-118244) | High | 7.2 | Highcharts JS is a JavaScript charting library based on SVG. From 12.0.0 until 12.6.1 and 13.1.0, Highcharts falls back… |
| 2026-10-28 18:17:15 | [CVE-2026-118245](https://nvd.nist.gov/vuln/detail/CVE-2026-118245) | High | 8.6 | Highcharts JS is a JavaScript charting library based on SVG. From 1.0.0 until 4.2.2, Highcharts Dashboards uses chartCo… |
| 2026-10-28 18:17:15 | [CVE-2026-118246](https://nvd.nist.gov/vuln/detail/CVE-2026-118246) | High | 8.4 | Highcharts JS is a JavaScript charting library based on SVG. From 10.0.0 until 11.4.9, 12.6.1, and 13.1.0, Highcharts a… |
| 2026-10-28 18:17:15 | [CVE-2026-118247](https://nvd.nist.gov/vuln/detail/CVE-2026-118247) | Medium | 6.9 | Highcharts JS is a JavaScript charting library based on SVG. From 1.0.0 until Dashboards 4.2.2, and from 2.0.0 until Gr… |
| 2026-10-28 18:17:15 | [CVE-2026-118248](https://nvd.nist.gov/vuln/detail/CVE-2026-118248) | Medium | 6.9 | Highcharts JS is a JavaScript charting library based on SVG. From 1.0.0 until 4.2.2, Highcharts Dashboards edit mode wa… |
| 2026-10-28 18:17:16 | [CVE-2026-118249](https://nvd.nist.gov/vuln/detail/CVE-2026-118249) | High | 7.2 | Highcharts JS is a JavaScript charting library based on SVG. From 13.0.0 until 13.1.0, Highcharts builds series data co… |
| 2026-10-28 18:17:16 | [CVE-2026-118250](https://nvd.nist.gov/vuln/detail/CVE-2026-118250) | High | 7.2 | Highcharts JS is a JavaScript charting library based on SVG. From 6.1.0 until 11.4.9, 12.6.1, and 3.1.0, Highcharts fol… |
| 2026-10-28 18:17:20 | [CVE-2026-58458](https://nvd.nist.gov/vuln/detail/CVE-2026-58458) | Medium | 6.9 | Don't Starve Together (Steam AppID 322330) through build 747465 contains a memory-corruption vulnerability in the nativ… |
| 2026-10-28 18:17:20 | [CVE-2026-79656](https://nvd.nist.gov/vuln/detail/CVE-2026-79656) | Medium | 6.0 | A user with read access to Grafana's server logs, or to a log store they are shipped to, can recover the OAuth and OIDC… |
| 2026-10-28 18:17:20 | [CVE-2026-84725](https://nvd.nist.gov/vuln/detail/CVE-2026-84725) | High | 8.1 | when EAP runs with -secmgr, the openjdk-orb's JDKBridge honours attacker-supplied CDR codebase URLs during object unmar… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
