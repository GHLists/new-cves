# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-09 11:19 UTC

New CVEs published between 2026-10-09 10:18 UTC and 2026-10-09 11:19 UTC.

[Full CSV](data/new-cves-2026-10-09T11-19-18-353753Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-09 11:17:01 | [CVE-2026-100227](https://nvd.nist.gov/vuln/detail/CVE-2026-100227) |  |  | Improper Verification of Cryptographic Signature vulnerability in Apache CXF's JAX-RS XML Security module. The JAX-RS X… |
| 2026-10-09 11:17:02 | [CVE-2026-107937](https://nvd.nist.gov/vuln/detail/CVE-2026-107937) |  |  | In Apache CXF, the parser for multipart/MTOM attachment part headers did not fully enforce the configured attachment-ma… |
| 2026-10-09 11:17:02 | [CVE-2026-107938](https://nvd.nist.gov/vuln/detail/CVE-2026-107938) |  |  | In Apache CXF, the Netty-based HTTP client transport (cxf-rt-transports-http-netty-client) did not verify that the host… |
| 2026-10-09 11:17:02 | [CVE-2026-108039](https://nvd.nist.gov/vuln/detail/CVE-2026-108039) |  |  | By default, StaxUtils placed no limit on the total number of elements or the total number of characters in an XML docum… |
| 2026-10-09 11:17:02 | [CVE-2026-71575](https://nvd.nist.gov/vuln/detail/CVE-2026-71575) |  |  | The max_age authentication-freshness check in OidcClientCodeRequestFilter was inoperative due to a milliseconds/seconds… |
| 2026-10-09 11:17:02 | [CVE-2026-73179](https://nvd.nist.gov/vuln/detail/CVE-2026-73179) |  |  | Improper enforcement of single-use authorization code semantics in the JPA OAuth2 authorization code grant provider in… |
| 2026-10-09 11:17:02 | [CVE-2026-78384](https://nvd.nist.gov/vuln/detail/CVE-2026-78384) |  |  | CompressionUtils.inflate() decompressed attacker-controlled DEFLATE data with no output-size cap. A small (~KB) crafted… |
| 2026-10-09 11:17:03 | [CVE-2026-79650](https://nvd.nist.gov/vuln/detail/CVE-2026-79650) |  |  | Apache CXF’s OIDC relying-party component could redirect users to an attacker-controlled URL after successful authentic… |
| 2026-10-09 11:17:03 | [CVE-2026-86463](https://nvd.nist.gov/vuln/detail/CVE-2026-86463) |  |  | Apache CXF's FIQL query parser has a vulnerability in how it searches for operators in query expressions. The search pa… |
| 2026-10-09 11:17:03 | [CVE-2026-97468](https://nvd.nist.gov/vuln/detail/CVE-2026-97468) |  |  | Apache CXF's STSTokenValidator and Security Token Service (STS) cached validated security tokens under a non-cryptograp… |
| 2026-10-09 11:17:03 | [CVE-2026-97791](https://nvd.nist.gov/vuln/detail/CVE-2026-97791) |  |  | In Apache CXF, STSTokenValidator checks whether a SAML assertion is signed by a trusted certificate before deciding to… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
