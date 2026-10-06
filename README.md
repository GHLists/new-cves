# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-06 21:19 UTC

New CVEs published between 2026-10-06 20:19 UTC and 2026-10-06 21:19 UTC.

[Full CSV](data/new-cves-2026-10-06T21-19-10-235829Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-06 21:17:02 | [CVE-2026-101258](https://nvd.nist.gov/vuln/detail/CVE-2026-101258) | High | 7.8 | A flaw was found in Ghostscript. When Ghostscript renders a crafted PostScript or EPS document, it can bypass the -dSAF… |
| 2026-10-06 21:17:04 | [CVE-2026-104045](https://nvd.nist.gov/vuln/detail/CVE-2026-104045) | Medium | 4.7 | A flaw was found in SSSD. A local user can trigger a Denial of Service (DoS) by exploiting a race condition in the auto… |
| 2026-10-06 21:17:04 | [CVE-2026-104046](https://nvd.nist.gov/vuln/detail/CVE-2026-104046) | Medium | 6.2 | A flaw was found in SSSD (System Security Services Daemon). When Identity Provider (IdP) authentication is enabled, pre… |
| 2026-10-06 21:17:04 | [CVE-2026-105811](https://nvd.nist.gov/vuln/detail/CVE-2026-105811) | High | 7.1 | Authorization bypass through a user-controlled key in the optional Amazon Q Business Lambda hook sample ( q-business-la… |
| 2026-10-06 21:17:04 | [CVE-2026-105812](https://nvd.nist.gov/vuln/detail/CVE-2026-105812) | High | 8.8 | Improper control of code generation in the agent import functionality of Amazon Bedrock AgentCore Starter Toolkit befor… |
| 2026-10-06 21:17:04 | [CVE-2026-106032](https://nvd.nist.gov/vuln/detail/CVE-2026-106032) | Medium | 5.7 | Server-side request forgery in the OpenAPI schema processing of the agent import functionality in Amazon Bedrock AgentC… |
| 2026-10-06 21:17:04 | [CVE-2026-106062](https://nvd.nist.gov/vuln/detail/CVE-2026-106062) | High | 7.8 | A heap-based buffer overflow was found in GIMP’s DirectDraw Surface (DDS) loader. When loading a crafted DDS image, buf… |
| 2026-10-06 21:17:15 | [CVE-2026-106455](https://nvd.nist.gov/vuln/detail/CVE-2026-106455) | High | 7.7 | Backstage is an open framework for building developer portals. From 0.11.12 until 1.14.7 and 1.15.5, the @backstage/plu… |
| 2026-10-06 21:17:15 | [CVE-2026-106456](https://nvd.nist.gov/vuln/detail/CVE-2026-106456) | Medium | 4.8 | Backstage is an open framework for building developer portals. From 0.5.0 until 0.6.18, the @backstage/plugin-proxy-bac… |
| 2026-10-06 21:17:16 | [CVE-2026-106457](https://nvd.nist.gov/vuln/detail/CVE-2026-106457) | Medium | 6.8 | Backstage is an open framework for building developer portals. From 0.1.0 until 0.5.0, the @backstage/plugin-auth-backe… |
| 2026-10-06 21:17:16 | [CVE-2026-106458](https://nvd.nist.gov/vuln/detail/CVE-2026-106458) | Medium | 6.5 | Backstage is an open framework for building developer portals. From 0.4.0 until 0.5.15, the @backstage/plugin-catalog-b… |
| 2026-10-06 21:17:16 | [CVE-2026-106459](https://nvd.nist.gov/vuln/detail/CVE-2026-106459) | High | 8.5 | Backstage is an open framework for building developer portals. From 0.3.0 until 0.3.8, the @backstage/plugin-scaffolder… |
| 2026-10-06 21:17:16 | [CVE-2026-106460](https://nvd.nist.gov/vuln/detail/CVE-2026-106460) | Medium | 6.8 | Backstage is an open framework for building developer portals. From 0.3.0 until 0.6.15 and 0.7.5, the @backstage/plugin… |
| 2026-10-06 21:17:16 | [CVE-2026-106461](https://nvd.nist.gov/vuln/detail/CVE-2026-106461) | Medium | 4.3 | Backstage is an open framework for building developer portals. Prior to 4.1.0, the @backstage/plugin-scaffolder-backend… |
| 2026-10-06 21:17:17 | [CVE-2026-106462](https://nvd.nist.gov/vuln/detail/CVE-2026-106462) | Medium | 6.4 | Backstage is an open framework for building developer portals. Prior to 1.54.6, scaffolder source-control actions may n… |
| 2026-10-06 21:17:17 | [CVE-2026-106463](https://nvd.nist.gov/vuln/detail/CVE-2026-106463) | Medium | 5.4 | Backstage is an open framework for building developer portals. Prior to 0.8.7, the @backstage/plugin-catalog-backend-mo… |
| 2026-10-06 21:17:17 | [CVE-2026-106486](https://nvd.nist.gov/vuln/detail/CVE-2026-106486) | High | 8.5 | Backstage is an open framework for building developer portals. Prior to 0.3.10 in @backstage/plugin-scaffolder-backend-… |
| 2026-10-06 21:17:17 | [CVE-2026-106487](https://nvd.nist.gov/vuln/detail/CVE-2026-106487) | Low | 3.5 | Backstage is an open framework for building developer portals. Prior to 0.21.10, the @backstage/plugin-kubernetes-backe… |
| 2026-10-06 21:17:17 | [CVE-2026-106488](https://nvd.nist.gov/vuln/detail/CVE-2026-106488) | High | 8.1 | Backstage is an open framework for building developer portals. Prior to 0.4.20, the @backstage/plugin-auth-backend-modu… |
| 2026-10-06 21:17:17 | [CVE-2026-106489](https://nvd.nist.gov/vuln/detail/CVE-2026-106489) | Medium | 6.5 | Backstage is an open framework for building developer portals. Prior to 2.2.4, the @backstage/plugin-techdocs-backend p… |
| 2026-10-06 21:17:17 | [CVE-2026-106490](https://nvd.nist.gov/vuln/detail/CVE-2026-106490) | Medium | 6.5 | Backstage is an open framework for building developer portals. Prior to 2.2.4, the @backstage/plugin-techdocs-backend p… |
| 2026-10-06 21:17:18 | [CVE-2026-106491](https://nvd.nist.gov/vuln/detail/CVE-2026-106491) | Medium | 6.4 | Backstage is an open framework for building developer portals. Prior to 0.6.17, the @backstage/plugin-proxy-backend pac… |
| 2026-10-06 21:17:18 | [CVE-2026-106492](https://nvd.nist.gov/vuln/detail/CVE-2026-106492) | High | 7.6 | Backstage is an open framework for building developer portals. Prior to 0.16.1 and 0.17.8, the @backstage/backend-defau… |
| 2026-10-06 21:17:18 | [CVE-2026-106493](https://nvd.nist.gov/vuln/detail/CVE-2026-106493) | Low | 3.0 | Backstage is an open framework for building developer portals. Prior to 1.54.6, cloud storage catalog providers did not… |
| 2026-10-06 21:17:18 | [CVE-2026-106494](https://nvd.nist.gov/vuln/detail/CVE-2026-106494) | Medium | 4.4 | Backstage is an open framework for building developer portals. Prior to 0.17.8, the @backstage/backend-defaults package… |
| 2026-10-06 21:17:18 | [CVE-2026-106547](https://nvd.nist.gov/vuln/detail/CVE-2026-106547) | High | 8.5 | A heap-based buffer overflow in H5VM_array_fill() in src/H5VM.c in HDF5 before 2.2.0 lets a remote attacker cause an ap… |
| 2026-10-06 21:17:18 | [CVE-2026-106550](https://nvd.nist.gov/vuln/detail/CVE-2026-106550) |  |  | Mozilla's Node-convict (version 6.2.2 and later) is vulnerable to a Denial of Service vulnerability caused by incomplet… |
| 2026-10-06 21:17:18 | [CVE-2026-106552](https://nvd.nist.gov/vuln/detail/CVE-2026-106552) | Medium | 4.2 | In sftp in OpenSSH before 10.6, a server can trigger directory traversal (causing files to be written to unintended loc… |
| 2026-10-06 21:17:19 | [CVE-2026-106553](https://nvd.nist.gov/vuln/detail/CVE-2026-106553) | Low | 2.2 | In sshd in OpenSSH before 10.6, credentials can incorrectly persist after failure of a GSSAPIAuthentication authenticat… |
| 2026-10-06 21:17:19 | [CVE-2026-106555](https://nvd.nist.gov/vuln/detail/CVE-2026-106555) | Low | 2.2 | In sshd in OpenSSH before 10.6, GSSAPIAuthentication authentication state can incorrectly be persisted across authentic… |
| 2026-10-06 21:17:19 | [CVE-2026-106582](https://nvd.nist.gov/vuln/detail/CVE-2026-106582) | Low | 3.7 | In sshd and ssh in OpenSSH before 10.6, an LZ77 dictionary coder can be used even though this is contraindicated by the… |
| 2026-10-06 21:17:19 | [CVE-2026-106584](https://nvd.nist.gov/vuln/detail/CVE-2026-106584) | Low | 2.5 | In ssh-keygen in OpenSSH before 10.6, certificates could have incorrect expiration times because of Daylight Saving mis… |
| 2026-10-06 21:17:19 | [CVE-2026-106585](https://nvd.nist.gov/vuln/detail/CVE-2026-106585) | Medium | 6.5 | In sshd and ssh in OpenSSH before 10.6, there is no check for whether the maximum packet length is exceeded during deco… |
| 2026-10-06 21:17:19 | [CVE-2026-106586](https://nvd.nist.gov/vuln/detail/CVE-2026-106586) | Low | 2.5 | In sshd in OpenSSH before 10.6, the restrict keyword (in authorized_keys) was supposed to be applicable to tunnel forwa… |
| 2026-10-06 21:17:20 | [CVE-2026-19029](https://nvd.nist.gov/vuln/detail/CVE-2026-19029) | Medium | 6.8 | A heap-based buffer over-read in H5Z__filter_scaleoffset() in src/H5Zscaleoffset.c in HDF5 through 2.2.0 lets an attack… |
| 2026-10-06 21:17:20 | [CVE-2026-43598](https://nvd.nist.gov/vuln/detail/CVE-2026-43598) | High | 7.7 | Improper input validation in the AMD ROCm Communication Collectives Library (RCCL) could allow a compromised peer rank… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
