# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 12:18 UTC

New CVEs published between 2026-11-09 11:18 UTC and 2026-11-09 12:18 UTC.

[Full CSV](data/new-cves-2026-11-09T12-18-45-328409Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 12:16:35 | [CVE-2026-112172](https://nvd.nist.gov/vuln/detail/CVE-2026-112172) | High | 8.1 | CGM XDent and XMedical expose PHP synchronization endpoints that allow unauthenticated attackers to manipulate session… |
| 2026-11-09 12:16:36 | [CVE-2026-118450](https://nvd.nist.gov/vuln/detail/CVE-2026-118450) | Medium | 5.9 | Venere is installed outside Program Files and loads/registers unsigned components from locations where an unprivileged… |
| 2026-11-09 12:16:36 | [CVE-2026-118458](https://nvd.nist.gov/vuln/detail/CVE-2026-118458) | High | 8.1 | The shared AIS login routing selects a production-shipped test DAO and plaintext comparison for the H and V application… |
| 2026-11-09 12:16:36 | [CVE-2026-118459](https://nvd.nist.gov/vuln/detail/CVE-2026-118459) | Medium | 6.3 | A time-derived emergency password can be derived from publicly available application code, enabling authentication with… |
| 2026-11-09 12:16:36 | [CVE-2026-118460](https://nvd.nist.gov/vuln/detail/CVE-2026-118460) | High | 8.0 | Embedded private keys protected by a shared password can be used to sign practitioner assertions for arbitrary practiti… |
| 2026-11-09 12:16:37 | [CVE-2026-118462](https://nvd.nist.gov/vuln/detail/CVE-2026-118462) | Critical | 9.2 | Update components download and execute code without proper authenticity verification, relying on ignored hashes or forg… |
| 2026-11-09 12:16:37 | [CVE-2026-118464](https://nvd.nist.gov/vuln/detail/CVE-2026-118464) | Medium | 5.8 | Shared cryptographic services use fixed vendor-wide secrets, deterministic IVs, null salts, and reversible transformati… |
| 2026-11-09 12:16:37 | [CVE-2026-118465](https://nvd.nist.gov/vuln/detail/CVE-2026-118465) | Medium | 5.8 | Shared components expose hard-coded Access, workgroup, CCBasic, DBISAM, and related database credentials that are ident… |
| 2026-11-09 12:16:37 | [CVE-2026-118467](https://nvd.nist.gov/vuln/detail/CVE-2026-118467) | Medium | 4.3 | Shared telemetry and logging components store or transmit patient and doctor identifiers, clinical information, and low… |
| 2026-11-09 12:16:37 | [CVE-2026-118468](https://nvd.nist.gov/vuln/detail/CVE-2026-118468) | High | 7.2 | XML parsers process attacker-influenced update manifests or network responses with external entity resolution enabled,… |
| 2026-11-09 12:16:37 | [CVE-2026-121629](https://nvd.nist.gov/vuln/detail/CVE-2026-121629) | High | 7.5 | A flaw was found in GStreamer's adaptive streaming demuxers (HLS, DASH, MSS). When processing a media playlist or manif… |
| 2026-11-09 12:16:37 | [CVE-2026-118461](https://nvd.nist.gov/vuln/detail/CVE-2026-118461) | High | 8.0 | The shared client accepts caller-controlled doctor identifiers for read and write operations without requiring authenti… |
| 2026-11-09 12:16:38 | [CVE-2026-124684](https://nvd.nist.gov/vuln/detail/CVE-2026-124684) | Medium | 5.1 | Use after free vulnerability in Samsung Open Source Escargot allows Pointer Manipulation. This issue affects Escargot:… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
