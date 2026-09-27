# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-27 02:19 UTC

New CVEs published between 2026-09-27 01:19 UTC and 2026-09-27 02:19 UTC.

[Full CSV](data/new-cves-2026-09-27T02-19-14-865172Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-27 02:17:11 | [CVE-2025-71422](https://nvd.nist.gov/vuln/detail/CVE-2025-71422) | Medium | 6.9 | Contrast is a Kubernetes runtime for confidential containers. In versions before 1.12.1, the secure persistent volume f… |
| 2026-09-27 02:17:15 | [CVE-2025-71423](https://nvd.nist.gov/vuln/detail/CVE-2025-71423) | High | 8.5 | Edgelesssys Contrast is a confidential-computing runtime for Kubernetes. In versions 1.9.0 before 1.12.2, the initializ… |
| 2026-09-27 02:17:16 | [CVE-2025-71424](https://nvd.nist.gov/vuln/detail/CVE-2025-71424) | Medium | 5.1 | Contrast, Edgeless Systems' runtime for confidential containers on Kubernetes, is affected in versions up to and includ… |
| 2026-09-27 02:17:16 | [CVE-2025-71425](https://nvd.nist.gov/vuln/detail/CVE-2025-71425) | High | 8.5 | Contrast (Edgeless Systems) before 1.8.1 logs the workload secret to stderr, and thus to Kubernetes logs, when the Cont… |
| 2026-09-27 02:17:17 | [CVE-2025-71426](https://nvd.nist.gov/vuln/detail/CVE-2025-71426) | High | 7.1 | Contrast is a confidential-computing runtime for Kubernetes. In versions before 1.4.1, a recovering Coordinator does no… |
| 2026-09-27 02:17:17 | [CVE-2026-100721](https://nvd.nist.gov/vuln/detail/CVE-2026-100721) | Critical | 9.5 | vm2 before 3.12.2 contains an authorization bypass in the NodeVM external-module resolver. When an embedder configures… |
| 2026-09-27 02:17:18 | [CVE-2026-100722](https://nvd.nist.gov/vuln/detail/CVE-2026-100722) | High | 8.9 | vm2 before 3.12.2 does not apply host-side Promise rejection handling in the sandbox-to-host construct trap. In BaseHan… |
| 2026-09-27 02:17:19 | [CVE-2026-100723](https://nvd.nist.gov/vuln/detail/CVE-2026-100723) | Medium | 6.9 | vm2 before 3.12.2 does not apply its Buffer backing-store ownership invariant (byteOffset === 0 and buffer.byteLength =… |
| 2026-09-27 02:17:20 | [CVE-2026-100724](https://nvd.nist.gov/vuln/detail/CVE-2026-100724) | Medium | 6.3 | http4k (Maven package org.http4k:http4k-core) before 6.49.0.0, 5.42.0.0 and 4.51.0.0 uses substring (Contains) matching… |
| 2026-09-27 02:17:20 | [CVE-2026-100725](https://nvd.nist.gov/vuln/detail/CVE-2026-100725) | High | 8.3 | http4k (Maven artifact org.http4k:http4k-core) before 6.48.0.0, 5.42.0.0, and 4.51.0.0 ships a BasicCookieStorage (clie… |
| 2026-09-27 02:17:20 | [CVE-2026-100744](https://nvd.nist.gov/vuln/detail/CVE-2026-100744) | Medium | 5.5 | A flaw has been found in coollabsio Coolify up to 4.1.2. The affected element is an unknown function of the file app/Ht… |
| 2026-09-27 02:17:21 | [CVE-2026-100745](https://nvd.nist.gov/vuln/detail/CVE-2026-100745) | Low | 2.1 | A vulnerability has been found in Edimax BR-6428nC 1.16. The impacted element is an unknown function of the file /gofor… |
| 2026-09-27 02:17:21 | [CVE-2026-100833](https://nvd.nist.gov/vuln/detail/CVE-2026-100833) | High | 7.6 | Contrast (edgelesssys/contrast) versions 1.14.0 before 1.23.1 generate runtime policies that fail to detect all contain… |
| 2026-09-27 02:17:21 | [CVE-2026-100834](https://nvd.nist.gov/vuln/detail/CVE-2026-100834) | High | 8.2 | http4k's Digest authentication module (org.http4k:http4k-security-digest) before versions 6.48.0.0, 5.42.0.0 and 4.51.0… |
| 2026-09-27 02:17:21 | [CVE-2026-100835](https://nvd.nist.gov/vuln/detail/CVE-2026-100835) | Critical | 9.1 | Contrast before 1.16.0 is susceptible to remote attestation relay attacks. Contrast accepted any TEE attestation report… |
| 2026-09-27 02:17:21 | [CVE-2026-100836](https://nvd.nist.gov/vuln/detail/CVE-2026-100836) | Medium | 5.3 | Contrast through 1.20.0 contains a panic vulnerability in the transit-engine endpoint's ciphertextContainer.UnmarshalJS… |
| 2026-09-27 02:17:21 | [CVE-2026-100837](https://nvd.nist.gov/vuln/detail/CVE-2026-100837) | Medium | 6.3 | Contrast (Edgeless Systems) through 1.20.0 performs unanchored suffix matching when selecting per-registry configuratio… |
| 2026-09-27 02:17:22 | [CVE-2026-100838](https://nvd.nist.gov/vuln/detail/CVE-2026-100838) | High | 8.6 | Contrast is a confidential-computing runtime for Kubernetes. In versions before 1.19.1, the Kata agent policies generat… |
| 2026-09-27 02:17:22 | [CVE-2026-100839](https://nvd.nist.gov/vuln/detail/CVE-2026-100839) | High | 8.4 | Contrast is a confidential-computing runtime for Kubernetes. In versions before 1.18.0, the guest kernel's ACPI/AML han… |
| 2026-09-27 02:17:22 | [CVE-2026-100840](https://nvd.nist.gov/vuln/detail/CVE-2026-100840) | High | 8.5 | MONAI through 1.6.0 contains a remote code execution vulnerability in the bundle configuration engine that resolves _ta… |
| 2026-09-27 02:17:22 | [CVE-2026-100841](https://nvd.nist.gov/vuln/detail/CVE-2026-100841) | High | 8.5 | In MONAI 1.6.0, PersistentDataset (monai/data/dataset.py) explicitly rejects the combination track_meta=True with weigh… |
| 2026-09-27 02:17:22 | [CVE-2026-100842](https://nvd.nist.gov/vuln/detail/CVE-2026-100842) | High | 7.3 | MONAI through 1.6.0 contains an eval injection vulnerability in _get_fake_spatial_shape() in monai/bundle/scripts.py. T… |
| 2026-09-27 02:17:22 | [CVE-2026-100843](https://nvd.nist.gov/vuln/detail/CVE-2026-100843) | High | 8.5 | MONAI versions before 1.6.0 contain a remote code execution vulnerability in the algo_from_pickle() function due to uns… |
| 2026-09-27 02:17:22 | [CVE-2026-100844](https://nvd.nist.gov/vuln/detail/CVE-2026-100844) | High | 8.6 | MONAI before 1.6.0 is vulnerable to OS command injection in the nnUNetV2Runner component (monai.apps.nnunet.nnunetv2_ru… |
| 2026-09-27 02:17:23 | [CVE-2026-100845](https://nvd.nist.gov/vuln/detail/CVE-2026-100845) | High | 8.5 | MONAI before 1.6.0 contains an unsafe deserialization vulnerability in the NumpyReader class that unconditionally uses… |
| 2026-09-27 02:17:23 | [CVE-2026-100846](https://nvd.nist.gov/vuln/detail/CVE-2026-100846) | High | 8.8 | MONAI before 1.5.2 contains a deserialization of untrusted data vulnerability in the algo_from_pickle function in monai… |
| 2026-09-27 02:17:23 | [CVE-2026-100847](https://nvd.nist.gov/vuln/detail/CVE-2026-100847) | High | 8.7 | AzuraCast before 0.23.8 contains a DQL injection vulnerability in the sortOrder API parameter of AbstractSearchableList… |
| 2026-09-27 02:17:23 | [CVE-2026-100848](https://nvd.nist.gov/vuln/detail/CVE-2026-100848) | High | 7.1 | AzuraCast (Composer package azuracast/azuracast) before 0.23.8 validates a station's "Remote Relay" URL only for URL sy… |
| 2026-09-27 02:17:23 | [CVE-2026-100849](https://nvd.nist.gov/vuln/detail/CVE-2026-100849) | High | 7.1 | AzuraCast is a self-hosted web radio management suite. In AzuraCast before 0.23.8, the station webhook URL validation i… |
| 2026-09-27 02:17:24 | [CVE-2026-100850](https://nvd.nist.gov/vuln/detail/CVE-2026-100850) | Medium | 4.8 | AzuraCast before 0.23.8 contains a server-side request forgery and local file read vulnerability in the AutoDJ remote p… |
| 2026-09-27 02:17:24 | [CVE-2026-100851](https://nvd.nist.gov/vuln/detail/CVE-2026-100851) | High | 7.2 | AzuraCast before 0.23.8 contains a broken access control vulnerability in the GET /api/station/{id}/vue/profile endpoin… |
| 2026-09-27 02:17:24 | [CVE-2026-100852](https://nvd.nist.gov/vuln/detail/CVE-2026-100852) | High | 8.7 | AzuraCast through 0.23.x contains a command injection vulnerability in the Liquidsoap config generation for live record… |
| 2026-09-27 02:17:24 | [CVE-2026-100853](https://nvd.nist.gov/vuln/detail/CVE-2026-100853) | High | 8.2 | In AzuraCast before 0.23.8, the public On-Demand download endpoint fails to verify playlist-level access controls, allo… |
| 2026-09-27 02:17:24 | [CVE-2026-100854](https://nvd.nist.gov/vuln/detail/CVE-2026-100854) | Medium | 5.3 | AzuraCast before 0.23.6 lacks RequireInternalConnection middleware on the Liquidsoap API endpoint and incorrectly deriv… |
| 2026-09-27 02:17:24 | [CVE-2026-100855](https://nvd.nist.gov/vuln/detail/CVE-2026-100855) | High | 7.1 | AzuraCast before 0.23.6 contains a missing permission check vulnerability in the GET /api/station/{station_id}/file/{id… |
| 2026-09-27 02:17:25 | [CVE-2026-100856](https://nvd.nist.gov/vuln/detail/CVE-2026-100856) | High | 8.7 | AzuraCast before 0.23.6 contains a code injection vulnerability in the remote relay password field due to incomplete mi… |
| 2026-09-27 02:17:25 | [CVE-2026-100857](https://nvd.nist.gov/vuln/detail/CVE-2026-100857) | High | 8.6 | AzuraCast before 0.23.4 contains a code injection vulnerability in the ConfigWriter::cleanUpString() method that fails… |
| 2026-09-27 02:17:25 | [CVE-2026-100858](https://nvd.nist.gov/vuln/detail/CVE-2026-100858) | High | 7.6 | heym before 0.0.109 contains a server-side request forgery vulnerability in the Slack, Discord, and Crawler workflow no… |
| 2026-09-27 02:17:25 | [CVE-2026-100859](https://nvd.nist.gov/vuln/detail/CVE-2026-100859) | High | 7.1 | Heym before 0.0.106 contains a credential exfiltration vulnerability in the POST /api/credentials/test endpoint that al… |
| 2026-09-27 02:17:25 | [CVE-2026-100860](https://nvd.nist.gov/vuln/detail/CVE-2026-100860) | Medium | 6.8 | heym before 0.0.105 does not act on the result of the credential authorization lookup in the Redis workflow node (backe… |
| 2026-09-27 02:17:25 | [CVE-2026-100861](https://nvd.nist.gov/vuln/detail/CVE-2026-100861) | Medium | 5.3 | heym before 0.0.105 fails to apply egress guards to integration services that use credential-supplied base URLs, allowi… |
| 2026-09-27 02:17:25 | [CVE-2026-100862](https://nvd.nist.gov/vuln/detail/CVE-2026-100862) | Medium | 6.9 | heym, a workflow automation platform, stores and returns multiple capability secrets in plaintext in versions prior to… |
| 2026-09-27 02:17:26 | [CVE-2026-100863](https://nvd.nist.gov/vuln/detail/CVE-2026-100863) | Medium | 5.3 | Heym versions 0.0.90 and earlier contain two server-side request forgery (SSRF) egress gaps, both remediated in app/ser… |
| 2026-09-27 02:17:26 | [CVE-2026-100864](https://nvd.nist.gov/vuln/detail/CVE-2026-100864) | High | 8.7 | heym before 0.0.91 contains a sandbox escape vulnerability in the expression engine's DotList map/filter and fallback r… |
| 2026-09-27 02:17:26 | [CVE-2026-100865](https://nvd.nist.gov/vuln/detail/CVE-2026-100865) | High | 8.7 | Heym before 0.0.53 contains multiple independent vulnerabilities. (1) The workflow condition evaluator uses Python eval… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
