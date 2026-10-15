# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-15 17:19 UTC

New CVEs published between 2026-10-15 16:22 UTC and 2026-10-15 17:19 UTC.

[Full CSV](data/new-cves-2026-10-15T17-19-09-282702Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-15 17:17:07 | [CVE-2026-100353](https://nvd.nist.gov/vuln/detail/CVE-2026-100353) | High | 7.5 | kin-openapi is a Go project for handling OpenAPI files. From 0.136.0 until 0.149.0, three openapi3filter decoder paths… |
| 2026-10-15 17:17:07 | [CVE-2026-100354](https://nvd.nist.gov/vuln/detail/CVE-2026-100354) | High | 7.5 | kin-openapi is a Go project for handling OpenAPI files. Prior to 0.149.0, runtime request, response, and direct schema… |
| 2026-10-15 17:17:07 | [CVE-2026-100409](https://nvd.nist.gov/vuln/detail/CVE-2026-100409) | High | 7.5 | OpenNext Cloudflare is an open Next.js adapter for Cloudflare. From 0.3.0 until 1.20.2, applications that enable enable… |
| 2026-10-15 17:17:08 | [CVE-2026-102527](https://nvd.nist.gov/vuln/detail/CVE-2026-102527) | Medium | 6.9 | Nuxt OG Image generates OG Images with Vue templates in Nuxt. From 6.2.5 until 6.7.0, the dynamic /_og/d/*.png route ac… |
| 2026-10-15 17:17:10 | [CVE-2026-102631](https://nvd.nist.gov/vuln/detail/CVE-2026-102631) | Medium | 5.9 | In authd before 0.7.1, the user identity matching in UpdateUser (internal/users/manager.go) resolves an incoming login… |
| 2026-10-15 17:17:12 | [CVE-2026-105065](https://nvd.nist.gov/vuln/detail/CVE-2026-105065) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in 8theme.com XStore… |
| 2026-10-15 17:17:16 | [CVE-2026-110812](https://nvd.nist.gov/vuln/detail/CVE-2026-110812) | Critical | 9.4 | Deserialization of untrusted data in the Gremlin graph data import component in Amazon Neptune engine might allow an au… |
| 2026-10-15 17:17:23 | [CVE-2026-57568](https://nvd.nist.gov/vuln/detail/CVE-2026-57568) | Medium | 5.7 | Lychee is a free, open-source photo-management tool. Prior to 7.6.0, Lychee permits an authenticated user with album-ed… |
| 2026-10-15 17:17:24 | [CVE-2026-57569](https://nvd.nist.gov/vuln/detail/CVE-2026-57569) | Low | 2.3 | Lychee is a free, open-source photo-management tool. Prior to 7.6.0, the POST /api/v2/Photo::fromUrl flow validates a h… |
| 2026-10-15 17:17:26 | [CVE-2026-61610](https://nvd.nist.gov/vuln/detail/CVE-2026-61610) | Low | 2.3 | Lychee is a free, open-source photo-management tool. Prior to 7.6.1, when photos_star_visibility is set to anonymous, P… |
| 2026-10-15 17:17:26 | [CVE-2026-61611](https://nvd.nist.gov/vuln/detail/CVE-2026-61611) | High | 7.5 | Lychee is a free, open-source photo-management tool. Prior to 7.6.1, POST /api/v2/Album::unlock has no throttle, attemp… |
| 2026-10-15 17:17:26 | [CVE-2026-61838](https://nvd.nist.gov/vuln/detail/CVE-2026-61838) | High | 8.2 | Lychee is a free, open-source photo-management tool. Prior to 7.6.3, GET /api/v2/Zip authorizes album and photo archive… |
| 2026-10-15 17:17:26 | [CVE-2026-62679](https://nvd.nist.gov/vuln/detail/CVE-2026-62679) | High | 8.9 | Lychee is a free, open-source photo-management tool. Prior to 7.6.4, SecurePathController, which serves GET /image/{pat… |
| 2026-10-15 17:17:27 | [CVE-2026-77466](https://nvd.nist.gov/vuln/detail/CVE-2026-77466) | High | 8.3 | Lychee is a free, open-source photo-management tool. Prior to 7.7.0, Lychee hides the Omnipay Dummy test provider from… |
| 2026-10-15 17:17:27 | [CVE-2026-77467](https://nvd.nist.gov/vuln/detail/CVE-2026-77467) | High | 7.1 | Lychee is a free, open-source photo-management tool. Prior to 7.7.0, Lychee enables ImageMagick PDF support with Ghosts… |
| 2026-10-15 17:17:27 | [CVE-2026-77468](https://nvd.nist.gov/vuln/detail/CVE-2026-77468) | Medium | 6.9 | Lychee is a free, open-source photo-management tool. Prior to 7.7.0, GET /docs/api exposes the Scramble-generated OpenA… |
| 2026-10-15 17:17:27 | [CVE-2026-77470](https://nvd.nist.gov/vuln/detail/CVE-2026-77470) | High | 8.3 | Lychee is a free, open-source photo-management tool. Prior to 7.7.1, the Supporter or Pro webshop POST /api/v2/Shop/Che… |
| 2026-10-15 17:17:28 | [CVE-2026-78850](https://nvd.nist.gov/vuln/detail/CVE-2026-78850) |  |  | An issue in Matomo v.5.11.2 allows a remote attacker to obtain sensitive information via the SiteContentDetector / Site… |
| 2026-10-15 17:17:28 | [CVE-2026-78851](https://nvd.nist.gov/vuln/detail/CVE-2026-78851) |  |  | Directory Traversal vulnerability in Grav CMS 2.0.3 through 2.0.6 allows a remote attacker to obtain sensitive informat… |
| 2026-10-15 17:17:29 | [CVE-2026-85634](https://nvd.nist.gov/vuln/detail/CVE-2026-85634) | High | 8.8 | A flaw was found in the ContentRepositoryImpl.copyExplodedContent function of the wildfly-core library, which is used b… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
