# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 13:21 UTC

New CVEs published between 2026-11-09 12:18 UTC and 2026-11-09 13:21 UTC.

[Full CSV](data/new-cves-2026-11-09T13-21-06-675249Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 13:17:03 | [CVE-2026-110468](https://nvd.nist.gov/vuln/detail/CVE-2026-110468) | Critical | 10.0 | WidzialniCMS is vulnerable to Unrestricted File Upload in the /panel/controllers/save_photo.php endpoint. Due to a clie… |
| 2026-11-09 13:17:03 | [CVE-2026-110469](https://nvd.nist.gov/vuln/detail/CVE-2026-110469) | Critical | 10.0 | WidzialniCMS is vulnerable to Unrestricted File Upload in the /panel/upload.php endpoint. Due to a client-controlled pe… |
| 2026-11-09 13:17:04 | [CVE-2026-112168](https://nvd.nist.gov/vuln/detail/CVE-2026-112168) | Medium | 6.0 | The Magistra software uses weak custom encryption, relies on an outdated compression algorithm to protect the database,… |
| 2026-11-09 13:17:04 | [CVE-2026-112169](https://nvd.nist.gov/vuln/detail/CVE-2026-112169) | Medium | 6.1 | Magistra software contains undocumented backdoor functionality that allows authentication bypass and the creation of a… |
| 2026-11-09 13:17:04 | [CVE-2026-112170](https://nvd.nist.gov/vuln/detail/CVE-2026-112170) | Medium | 6.3 | The software downloads upgrade files without performing integrity checks, allowing the installation of tampered updates. |
| 2026-11-09 13:17:04 | [CVE-2026-112171](https://nvd.nist.gov/vuln/detail/CVE-2026-112171) | Medium | 4.4 | An attacker can inject malicious SQL statements through user-controlled input, allowing unauthorized access to, modific… |
| 2026-11-09 13:17:04 | [CVE-2026-112204](https://nvd.nist.gov/vuln/detail/CVE-2026-112204) | Medium | 5.1 | WidzialniCMS is vulnerable to Reflected XSS in the /index.php endpoint. An attacker can prepare an URL that, when opene… |
| 2026-11-09 13:17:04 | [CVE-2026-112205](https://nvd.nist.gov/vuln/detail/CVE-2026-112205) | Medium | 6.9 | WidzialniCMS is vulnerable to Bruteforce Protection Bypass in the login functionality. The cookie-based lockout can be… |
| 2026-11-09 13:17:05 | [CVE-2026-118790](https://nvd.nist.gov/vuln/detail/CVE-2026-118790) | High | 7.2 | Multiple hardcoded credentials are embedded within product components and administrative functionalities. These credent… |
| 2026-11-09 13:17:05 | [CVE-2026-118791](https://nvd.nist.gov/vuln/detail/CVE-2026-118791) | High | 7.2 | The application implements software update functionality without adequate authenticity and integrity validation, allowi… |
| 2026-11-09 13:17:05 | [CVE-2026-118792](https://nvd.nist.gov/vuln/detail/CVE-2026-118792) | Medium | 6.1 | Default credentials permit access through AcuXDBC. |
| 2026-11-09 13:17:05 | [CVE-2026-118795](https://nvd.nist.gov/vuln/detail/CVE-2026-118795) | Medium | 5.9 | Administrative roles and module permissions are stored in mutable local database fields, allowing privilege escalation… |
| 2026-11-09 13:17:05 | [CVE-2026-118798](https://nvd.nist.gov/vuln/detail/CVE-2026-118798) | Medium | 4.4 | Multiple sensitive authentication data, including credentials, OAuth-related secrets, session information, and authenti… |
| 2026-11-09 13:17:05 | [CVE-2026-119610](https://nvd.nist.gov/vuln/detail/CVE-2026-119610) | High | 8.2 | A flaw was found in GStreamer's gst-plugins-good, specifically in the H.264 RTP depayloader element. When processing MT… |
| 2026-11-09 13:17:06 | [CVE-2026-119613](https://nvd.nist.gov/vuln/detail/CVE-2026-119613) | Medium | 5.3 | Generation of Error Message Containing Sensitive Information vulnerability in ash-project ash_ai allows a caller of an… |
| 2026-11-09 13:17:06 | [CVE-2026-120854](https://nvd.nist.gov/vuln/detail/CVE-2026-120854) | High | 7.5 | Allocation of Resources Without Limits or Throttling vulnerability in iubenda iubenda iubenda-cookie-law-solution allow… |
| 2026-11-09 13:17:06 | [CVE-2026-120856](https://nvd.nist.gov/vuln/detail/CVE-2026-120856) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Rymera Web Co Inv… |
| 2026-11-09 13:17:06 | [CVE-2026-121601](https://nvd.nist.gov/vuln/detail/CVE-2026-121601) | Medium | 6.1 | A flaw was found in GStreamer's MXF demuxer plugin (gst-plugins-bad). When processing a specially crafted MXF media fil… |
| 2026-11-09 13:17:07 | [CVE-2026-121611](https://nvd.nist.gov/vuln/detail/CVE-2026-121611) | Medium | 6.5 | A flaw was found in GStreamer's gst-plugins-bad package. A use of uninitialized memory vulnerability exists in the H.26… |
| 2026-11-09 13:17:07 | [CVE-2026-122673](https://nvd.nist.gov/vuln/detail/CVE-2026-122673) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Wpmet ShopEngine… |
| 2026-11-09 13:17:07 | [CVE-2026-124079](https://nvd.nist.gov/vuln/detail/CVE-2026-124079) | Critical | 9.3 | rConfig Core 8.0.0 before 8.2.19 and rConfig Pro before 8.4.1 contain a deserialization of untrusted data vulnerability… |
| 2026-11-09 13:17:07 | [CVE-2026-124622](https://nvd.nist.gov/vuln/detail/CVE-2026-124622) | Medium | 4.8 | A vulnerability was identified in olivier-ls PHP-FTS up to 1.1.3. This impacts the function TrigramIndex::open of the f… |
| 2026-11-09 13:17:07 | [CVE-2026-124623](https://nvd.nist.gov/vuln/detail/CVE-2026-124623) | Low | 2.0 | A security flaw has been discovered in PipraPay 3.0.0. Affected is the function system-settings-import of the file /sum… |
| 2026-11-09 13:17:09 | [CVE-2026-94434](https://nvd.nist.gov/vuln/detail/CVE-2026-94434) | High | 8.8 | Improper neutralization of special elements used in an OS command ('OS command injection') vulnerability in TÜBİTAK BİL… |
| 2026-11-09 13:17:09 | [CVE-2026-95648](https://nvd.nist.gov/vuln/detail/CVE-2026-95648) | High | 8.1 | Improperly controlled modification of Dynamically-Determined object attributes vulnerability in C-Prot Inc. C-Prot AppD… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
