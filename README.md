# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 15:20 UTC

New CVEs published between 2026-11-24 14:18 UTC and 2026-11-24 15:20 UTC.

[Full CSV](data/new-cves-2026-11-24T15-20-03-842766Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 15:17:11 | [CVE-2026-116225](https://nvd.nist.gov/vuln/detail/CVE-2026-116225) | High | 8.7 | Improper Validation of Specified Quantity in Input vulnerability in the BER decoder in Erlang/OTP snmp allows an unauth… |
| 2026-11-24 15:17:12 | [CVE-2026-116293](https://nvd.nist.gov/vuln/detail/CVE-2026-116293) | High | 7.0 | Out-of-bounds Write vulnerability in the external term format decoder in Erlang OTP erts allows an attacker who control… |
| 2026-11-24 15:17:12 | [CVE-2026-116295](https://nvd.nist.gov/vuln/detail/CVE-2026-116295) | Low | 2.1 | Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Request/Response Splitting') vulnerability in Erlang O… |
| 2026-11-24 15:17:12 | [CVE-2026-116382](https://nvd.nist.gov/vuln/detail/CVE-2026-116382) | High | 8.2 | Allocation of Resources Without Limits or Throttling vulnerability in Erlang OTP inets (httpd_script_env module) allows… |
| 2026-11-24 15:17:13 | [CVE-2026-117642](https://nvd.nist.gov/vuln/detail/CVE-2026-117642) | Medium | 6.9 | Uncontrolled Recursion vulnerability in the external term format decoder in Erlang OTP erts allows an attacker who cont… |
| 2026-11-24 15:17:14 | [CVE-2026-119443](https://nvd.nist.gov/vuln/detail/CVE-2026-119443) | Medium | 6.9 | Improper Restriction of XML External Entity Reference vulnerability in xmerl_scan in Erlang OTP xmerl allows an attacke… |
| 2026-11-24 15:17:14 | [CVE-2026-120961](https://nvd.nist.gov/vuln/detail/CVE-2026-120961) | Medium | 6.9 | Out-of-bounds Read vulnerability in the external term format decoder in Erlang OTP erts allows an attacker who controls… |
| 2026-11-24 15:17:15 | [CVE-2026-124286](https://nvd.nist.gov/vuln/detail/CVE-2026-124286) | Critical | 9.1 | Improper Verification of Cryptographic Signature vulnerability in Erlang OTP ssl (ssl_handshake module) allows an on-pa… |
| 2026-11-24 15:17:18 | [CVE-2026-130411](https://nvd.nist.gov/vuln/detail/CVE-2026-130411) | Critical | 9.2 | Deserialization of Untrusted Data vulnerability in woylie flop allows a remote attacker to execute code on the server v… |
| 2026-11-24 15:17:19 | [CVE-2026-131902](https://nvd.nist.gov/vuln/detail/CVE-2026-131902) | Medium | 5.9 | XML Injection vulnerability in ex-aws ex_aws_s3 allows an attacker who controls an object version id passed to ExAws.S3… |
| 2026-11-24 15:17:20 | [CVE-2026-133555](https://nvd.nist.gov/vuln/detail/CVE-2026-133555) | High | 8.9 | Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection') vulnerability in elixir-ecto db_conn… |
| 2026-11-24 15:17:32 | [CVE-2026-135908](https://nvd.nist.gov/vuln/detail/CVE-2026-135908) | Medium | 5.3 | Rapid7 Metasploit Framework versions prior to 6.5.10 are vulnerable to an uncontrolled resource consumption issue in Re… |
| 2026-11-24 15:17:33 | [CVE-2026-136131](https://nvd.nist.gov/vuln/detail/CVE-2026-136131) | Medium | 6.0 | hping3 through commit 3547c76 contains an out-of-bounds write vulnerability in display_ipopt() that allows remote attac… |
| 2026-11-24 15:17:33 | [CVE-2026-136132](https://nvd.nist.gov/vuln/detail/CVE-2026-136132) | Critical | 9.2 | Pangolin before 1.21.0 contains an authentication bypass vulnerability in isPathAllowed() in server/lib/pathMatch.ts th… |
| 2026-11-24 15:17:33 | [CVE-2026-136133](https://nvd.nist.gov/vuln/detail/CVE-2026-136133) | Medium | 6.9 | NocoDB before 2026.10.2 contains a denial of service vulnerability in passwordForgot() that allows unauthenticated atta… |
| 2026-11-24 15:17:33 | [CVE-2026-136155](https://nvd.nist.gov/vuln/detail/CVE-2026-136155) | High | 8.8 | In Valkey 9.1.0 and 9.1.1, the Lua script debugger builds its command table once and caches it with a pointer to the Lu… |
| 2026-11-24 15:17:33 | [CVE-2026-136156](https://nvd.nist.gov/vuln/detail/CVE-2026-136156) | High | 8.8 | In Valkey before 7.2.15, 8.0.x before 8.0.12, 8.1.x before 8.1.11, 9.0.x before 9.0.7, 9.1.x before 9.1.3 and 9.2.0-rc1… |
| 2026-11-24 15:17:33 | [CVE-2026-136157](https://nvd.nist.gov/vuln/detail/CVE-2026-136157) | High | 7.5 | In Valkey 8.0.x before 8.0.11, 8.1.x before 8.1.10, 9.0.x before 9.0.6 and 9.1.x before 9.1.2, the RDMA transport's pen… |
| 2026-11-24 15:17:33 | [CVE-2026-136158](https://nvd.nist.gov/vuln/detail/CVE-2026-136158) | High | 8.8 | In Valkey JSON 1.0.0 through 1.0.2, a recursive JSONPath expression such as $..* returns both an array and elements nes… |
| 2026-11-24 15:17:34 | [CVE-2026-136159](https://nvd.nist.gov/vuln/detail/CVE-2026-136159) | High | 8.7 | TypiCMS Core before 17.0.46 contains an insufficiently protected credentials vulnerability that allows authenticated us… |
| 2026-11-24 15:17:34 | [CVE-2026-136160](https://nvd.nist.gov/vuln/detail/CVE-2026-136160) | High | 8.5 | Pyro through 1.9.2 contains an insecure deserialization vulnerability in ParamStoreDict.load() that calls torch.load wi… |
| 2026-11-24 15:17:34 | [CVE-2026-136165](https://nvd.nist.gov/vuln/detail/CVE-2026-136165) | Critical | 9.1 | Fider before 0.40.0 contains an account takeover vulnerability that allows unauthenticated attackers to sign in as exis… |
| 2026-11-24 15:17:34 | [CVE-2026-136166](https://nvd.nist.gov/vuln/detail/CVE-2026-136166) | Medium | 5.3 | Wallabag from 2.0.0-beta.1 before 2.6.16 contains a missing authorization vulnerability that allows authenticated users… |
| 2026-11-24 15:17:34 | [CVE-2026-136167](https://nvd.nist.gov/vuln/detail/CVE-2026-136167) | High | 8.5 | vedo through 2026.6.3 contains an insecure deserialization vulnerability that allows attackers to execute code by suppl… |
| 2026-11-24 15:17:34 | [CVE-2026-136168](https://nvd.nist.gov/vuln/detail/CVE-2026-136168) | High | 8.7 | RedVector before 8.1.0 contains a hard-coded credentials vulnerability that allows unauthenticated attackers to execute… |
| 2026-11-24 15:17:34 | [CVE-2026-136169](https://nvd.nist.gov/vuln/detail/CVE-2026-136169) | Medium | 5.1 | Cockpit CMS through 2.14.1 contains a stored cross-site scripting vulnerability that allows authenticated users with co… |
| 2026-11-24 15:17:35 | [CVE-2026-136170](https://nvd.nist.gov/vuln/detail/CVE-2026-136170) | High | 7.3 | Assimp through 6.0.6 contains a use-after-free and double free vulnerability in OpenGEXImporter.cpp because InternReadF… |
| 2026-11-24 15:17:35 | [CVE-2026-136171](https://nvd.nist.gov/vuln/detail/CVE-2026-136171) | Medium | 5.8 | Assimp through 6.0.6 contains a use-after-free vulnerability in BVHLoader.cpp that allows attackers to read freed aiNod… |
| 2026-11-24 15:17:36 | [CVE-2026-136172](https://nvd.nist.gov/vuln/detail/CVE-2026-136172) | High | 7.3 | Assimp through 6.0.6 contains a heap out-of-bounds write vulnerability in the OBJ exporter that allows attackers to cor… |
| 2026-11-24 15:17:37 | [CVE-2026-62273](https://nvd.nist.gov/vuln/detail/CVE-2026-62273) | Low | 2.1 | XML Injection vulnerability in ex-aws ex_aws_s3 allows an attacker who controls tag keys or values to inject forged tag… |
| 2026-11-24 15:17:37 | [CVE-2026-63581](https://nvd.nist.gov/vuln/detail/CVE-2026-63581) | Medium | 6.9 | XML Injection vulnerability in ex-aws ex_aws_s3 (ExAws.S3 module) allows an attacker to inject arbitrary XML configurat… |
| 2026-11-24 15:17:38 | [CVE-2026-63582](https://nvd.nist.gov/vuln/detail/CVE-2026-63582) | Medium | 5.8 | Externally Controlled Reference to a Resource in Another Sphere vulnerability in ex-aws ex_aws_s3 allows an attacker wh… |
| 2026-11-24 15:17:38 | [CVE-2026-63583](https://nvd.nist.gov/vuln/detail/CVE-2026-63583) | High | 7.0 | ExAws.S3.Utils.build_lifecycle_rule/1 in ex_aws_s3 interpolates caller-supplied lifecycle rule fields (the rule id, fil… |
| 2026-11-24 15:17:38 | [CVE-2026-63584](https://nvd.nist.gov/vuln/detail/CVE-2026-63584) | Low | 2.1 | Improper Neutralization of CRLF Sequences ('CRLF Injection') vulnerability in ex-aws ex_aws_s3 allows HTTP header injec… |
| 2026-11-24 15:17:38 | [CVE-2026-63585](https://nvd.nist.gov/vuln/detail/CVE-2026-63585) | Medium | 4.8 | ExAws.S3 constructs S3 ACL grant headers (such as x-amz-grant-read and x-amz-grant-full-control) in format_grant_header… |
| 2026-11-24 15:17:39 | [CVE-2026-65320](https://nvd.nist.gov/vuln/detail/CVE-2026-65320) | Critical | 9.2 | fastcore through 2.2.44 contains a path traversal vulnerability in the fastcore.xtras.untar_dir() archive extraction he… |
| 2026-11-24 15:17:39 | [CVE-2026-65621](https://nvd.nist.gov/vuln/detail/CVE-2026-65621) | Low | 2.1 | ex_aws_s3 builds x-amz-meta-* request headers by interpolating user-supplied object metadata directly into header names… |
| 2026-11-24 15:17:39 | [CVE-2026-65622](https://nvd.nist.gov/vuln/detail/CVE-2026-65622) | Medium | 5.9 | Improper Encoding or Escaping of Output vulnerability in ex-aws ex_aws_ses (ExAws.SES module) allows path injection int… |
| 2026-11-24 15:17:40 | [CVE-2026-75582](https://nvd.nist.gov/vuln/detail/CVE-2026-75582) | High | 7.1 | Frappe LMS before 2.65.0 contains an improper authorization vulnerability that allows Batch Evaluators to modify any ev… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
