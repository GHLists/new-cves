# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-22 22:19 UTC

New CVEs published between 2026-11-22 21:19 UTC and 2026-11-22 22:19 UTC.

[Full CSV](data/new-cves-2026-11-22T22-19-41-821946Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-22 22:17:31 | [CVE-2026-134761](https://nvd.nist.gov/vuln/detail/CVE-2026-134761) | Medium | 5.8 | libical before 4.0.7 contains a use-after-free and double free vulnerability in icalparser_clean() that allows attacker… |
| 2026-11-22 22:17:31 | [CVE-2026-134762](https://nvd.nist.gov/vuln/detail/CVE-2026-134762) | Low | 2.1 | ntop nDPI through 6.0 contains a heap out-of-bounds read and unsigned length underflow in ndpi_serializer_get_buffer()… |
| 2026-11-22 22:17:31 | [CVE-2026-134763](https://nvd.nist.gov/vuln/detail/CVE-2026-134763) | Low | 2.1 | FreeRDP before 3.33.1 contains a heap use-after-free vulnerability in the WinPR wLinkedList collection because LinkedLi… |
| 2026-11-22 22:17:31 | [CVE-2026-134764](https://nvd.nist.gov/vuln/detail/CVE-2026-134764) | Medium | 5.3 | Ground Station before 0.8.25 contains a path traversal vulnerability that allows authenticated non-administrator operat… |
| 2026-11-22 22:17:31 | [CVE-2026-134765](https://nvd.nist.gov/vuln/detail/CVE-2026-134765) | High | 8.7 | Kirby 5.0.0 before 5.6.4 contains a race condition in Kirby\Api\Upload::processChunk() that allows authenticated users… |
| 2026-11-22 22:17:32 | [CVE-2026-134793](https://nvd.nist.gov/vuln/detail/CVE-2026-134793) | High | 8.5 | Electerm before 5.9.0 on Windows contains an OS command injection vulnerability that allows attackers to execute PowerS… |
| 2026-11-22 22:17:32 | [CVE-2026-134794](https://nvd.nist.gov/vuln/detail/CVE-2026-134794) | High | 7.1 | HedgeDoc before 1.12.1 contains a prototype pollution vulnerability in the POST /history/:noteId endpoint that allows a… |
| 2026-11-22 22:17:32 | [CVE-2026-134795](https://nvd.nist.gov/vuln/detail/CVE-2026-134795) | Medium | 6.9 | graphql-core 3.2.12 before 3.2.14 and 3.3.0rc1 before 3.3.2 contains a denial of service vulnerability that allows unau… |
| 2026-11-22 22:17:32 | [CVE-2026-134796](https://nvd.nist.gov/vuln/detail/CVE-2026-134796) | Medium | 6.3 | Donetick before 0.1.86 contains a path traversal vulnerability in the GET /api/v1/assets/*filepath route that allows un… |
| 2026-11-22 22:17:32 | [CVE-2026-134797](https://nvd.nist.gov/vuln/detail/CVE-2026-134797) | Low | 2.3 | Donetick before 0.1.86 contains a path traversal vulnerability that allows authenticated users to delete other users' f… |
| 2026-11-22 22:17:33 | [CVE-2026-134798](https://nvd.nist.gov/vuln/detail/CVE-2026-134798) | Medium | 5.3 | Donetick through 0.1.86 contains a blind server-side request forgery vulnerability that allows self-registered users to… |
| 2026-11-22 22:17:33 | [CVE-2026-134799](https://nvd.nist.gov/vuln/detail/CVE-2026-134799) | Low | 2.3 | ByteStash 1.5.0 before 1.6.1 contains a login cross-site request forgery vulnerability in the /api/auth/oidc/callback h… |
| 2026-11-22 22:17:33 | [CVE-2026-134800](https://nvd.nist.gov/vuln/detail/CVE-2026-134800) | Low | 2.3 | VoidAuth before 1.19.2 contains an insufficient session expiration vulnerability that allows attackers to retain accoun… |
| 2026-11-22 22:17:33 | [CVE-2026-134801](https://nvd.nist.gov/vuln/detail/CVE-2026-134801) | Low | 2.3 | VoidAuth before 1.19.2 contains an improper verification vulnerability that allows authenticated users to retain the em… |
| 2026-11-22 22:17:33 | [CVE-2026-134802](https://nvd.nist.gov/vuln/detail/CVE-2026-134802) | High | 7.6 | VoidAuth before 1.19.2 contains an access control bypass vulnerability that allows authenticated users to evade stricte… |
| 2026-11-22 22:17:33 | [CVE-2026-134803](https://nvd.nist.gov/vuln/detail/CVE-2026-134803) | High | 7.2 | DBHub before 1.7.0 contains a read-only mode bypass vulnerability that allows MCP clients restricted to readonly execut… |
| 2026-11-22 22:17:34 | [CVE-2026-134804](https://nvd.nist.gov/vuln/detail/CVE-2026-134804) | High | 8.7 | Portainer 2.39.0 before 2.39.9, 2.40.0 before 2.45.4, and 3.0.0 before 3.1.0 contains an authorization bypass vulnerabi… |
| 2026-11-22 22:17:34 | [CVE-2026-134805](https://nvd.nist.gov/vuln/detail/CVE-2026-134805) | High | 7.0 | Zipline before 4.8.3 contains a server-side request forgery vulnerability that allows authenticated OIDC users to make… |
| 2026-11-22 22:17:34 | [CVE-2026-134806](https://nvd.nist.gov/vuln/detail/CVE-2026-134806) | Medium | 6.9 | Opencast before 20.6 contains a path traversal vulnerability in WorkspaceImpl.toWorkspaceFile that allows authenticated… |
| 2026-11-22 22:17:34 | [CVE-2026-134807](https://nvd.nist.gov/vuln/detail/CVE-2026-134807) | Medium | 6.3 | Reposilite 3.5.27 before 3.6.7 contains a brute-force protection bypass vulnerability that allows unauthenticated remot… |
| 2026-11-22 22:17:34 | [CVE-2026-134808](https://nvd.nist.gov/vuln/detail/CVE-2026-134808) | High | 7.7 | Gogs before 0.14.4 on Windows contains a path equivalence vulnerability in isRepositoryGitPath that allows authenticate… |
| 2026-11-22 22:17:34 | [CVE-2026-134809](https://nvd.nist.gov/vuln/detail/CVE-2026-134809) | Medium | 6.9 | OpenOLAT 20.2.2 before 20.3.12, 21.0.0 before 21.0.7, and 21.1.0 before 21.1.2 contains a missing authentication vulner… |
| 2026-11-22 22:17:35 | [CVE-2026-134810](https://nvd.nist.gov/vuln/detail/CVE-2026-134810) | High | 7.1 | diaspora* before 0.10.0 contains a path traversal (zip slip) vulnerability in ImportService#unzip_photos_file that allo… |
| 2026-11-22 22:17:35 | [CVE-2026-134811](https://nvd.nist.gov/vuln/detail/CVE-2026-134811) | Medium | 5.1 | diaspora* before 0.10.0 contains an HTML injection vulnerability in Notifier#invite that allows authenticated users to… |
| 2026-11-22 22:17:35 | [CVE-2026-134812](https://nvd.nist.gov/vuln/detail/CVE-2026-134812) | High | 8.7 | msgpackr before 2.1.4 contains an inefficient algorithmic complexity vulnerability that allows remote attackers to caus… |
| 2026-11-22 22:17:35 | [CVE-2026-134813](https://nvd.nist.gov/vuln/detail/CVE-2026-134813) | High | 8.7 | Faye websocket-driver 0.5.0 before 0.8.0, permessage-deflate before 0.2.0, and websocket-extensions before 0.2.0 contai… |
| 2026-11-22 22:17:35 | [CVE-2026-134814](https://nvd.nist.gov/vuln/detail/CVE-2026-134814) | Critical | 9.2 | binary-parser before 2.3.1 contains a code injection vulnerability that allows attackers controlling parser definitions… |
| 2026-11-22 22:17:35 | [CVE-2026-134815](https://nvd.nist.gov/vuln/detail/CVE-2026-134815) | Critical | 9.2 | simple-git before 4.1.0 contains an argument injection vulnerability that allows attackers to bypass the allowUnsafePac… |
| 2026-11-22 22:17:35 | [CVE-2026-134816](https://nvd.nist.gov/vuln/detail/CVE-2026-134816) | High | 8.2 | sigstore-js @sigstore/oci before 0.8.0 contains a credential exposure vulnerability that leaks registry credentials by… |
| 2026-11-22 22:17:36 | [CVE-2026-134817](https://nvd.nist.gov/vuln/detail/CVE-2026-134817) | High | 7.1 | mcp-server-kubernetes before 4.2.0 contains an argument injection vulnerability that allows remote MCP clients to injec… |
| 2026-11-22 22:17:36 | [CVE-2026-134818](https://nvd.nist.gov/vuln/detail/CVE-2026-134818) | High | 7.1 | oasdiff 1.24.0 before 1.34.1 fails to enforce --allow-external-refs=false when --open is used, because the recordingRea… |
| 2026-11-22 22:17:36 | [CVE-2026-134819](https://nvd.nist.gov/vuln/detail/CVE-2026-134819) | High | 7.1 | Delta Sharing reference server 1.4.0 before 1.5.0 contains an incorrect permission assignment vulnerability that allows… |
| 2026-11-22 22:17:36 | [CVE-2026-134820](https://nvd.nist.gov/vuln/detail/CVE-2026-134820) | Medium | 6.3 | Gunicorn 25.2.0 before 27.0.0 contains an HTTP request smuggling vulnerability in the pure-Python ASGI parser that allo… |
| 2026-11-22 22:17:36 | [CVE-2026-134821](https://nvd.nist.gov/vuln/detail/CVE-2026-134821) | High | 8.7 | Gunicorn 25.2.0 before 27.0.0 contains a memory exhaustion vulnerability in the pure-Python ASGI HTTP/1 parser that buf… |
| 2026-11-22 22:17:36 | [CVE-2026-134822](https://nvd.nist.gov/vuln/detail/CVE-2026-134822) | Medium | 5.1 | Sustainsys.Saml2 before 1.0.4 and 2.x before 2.11.1 contains an improper signature verification vulnerability that allo… |
| 2026-11-22 22:17:37 | [CVE-2026-134823](https://nvd.nist.gov/vuln/detail/CVE-2026-134823) | Medium | 4.8 | Kitty 0.43.0 before 0.51.0 contains a terminal escape sequence injection vulnerability that allows attackers to emit es… |
| 2026-11-22 22:17:37 | [CVE-2026-134824](https://nvd.nist.gov/vuln/detail/CVE-2026-134824) | Medium | 6.8 | Nektos act 0.2.92 before 0.2.98 contains a link following vulnerability that allows malicious repositories to read host… |
| 2026-11-22 22:17:37 | [CVE-2026-134825](https://nvd.nist.gov/vuln/detail/CVE-2026-134825) | High | 8.3 | Gradio 6.27.0 before 6.32.0 contains an authentication bypass vulnerability in gradio/history.py that allows remote una… |
| 2026-11-22 22:17:37 | [CVE-2026-134826](https://nvd.nist.gov/vuln/detail/CVE-2026-134826) | Medium | 6.9 | erxes before 3.4.14 contains a missing authentication vulnerability in the insurance_api plugin that allows unauthentic… |
| 2026-11-22 22:17:37 | [CVE-2026-134827](https://nvd.nist.gov/vuln/detail/CVE-2026-134827) | High | 8.3 | Lightdash before 3.212.0 contains an insufficiently protected credentials vulnerability in getGitlabInstallationRepoRea… |
| 2026-11-22 22:17:37 | [CVE-2026-134828](https://nvd.nist.gov/vuln/detail/CVE-2026-134828) | Medium | 5.1 | Penpot 2.18.0 before 2.19.1 contains a stored cross-site scripting vulnerability in the sanitize-svg function that allo… |
| 2026-11-22 22:17:38 | [CVE-2026-134829](https://nvd.nist.gov/vuln/detail/CVE-2026-134829) | High | 7.6 | Umami 3.3.0 before 3.5.0 contains a race condition in two-factor authentication attempt limiting that allows attackers… |
| 2026-11-22 22:17:38 | [CVE-2026-134830](https://nvd.nist.gov/vuln/detail/CVE-2026-134830) | High | 8.7 | Casdoor before 4.27.1 contains an uncontrolled resource consumption vulnerability in decodeSamlMessage that allows unau… |
| 2026-11-22 22:17:38 | [CVE-2026-134831](https://nvd.nist.gov/vuln/detail/CVE-2026-134831) | Medium | 6.9 | Chatwoot before 4.20.0 contains an information disclosure vulnerability that allows unauthenticated attackers to read u… |
| 2026-11-22 22:17:38 | [CVE-2026-134832](https://nvd.nist.gov/vuln/detail/CVE-2026-134832) | Medium | 4.8 | Vim 9.2.0405 before 9.2.1352 contains a security bypass vulnerability in expand_tag_fname() that allows attackers to ev… |
| 2026-11-22 22:17:38 | [CVE-2026-134833](https://nvd.nist.gov/vuln/detail/CVE-2026-134833) | Medium | 6.9 | RSSHub before 2026.11.01-8521.e529e9b contains a domain validation bypass in the javdb routes that allows unauthenticat… |
| 2026-11-22 22:17:38 | [CVE-2026-134834](https://nvd.nist.gov/vuln/detail/CVE-2026-134834) | Medium | 5.3 | Tandoor Recipes before 2.7.4 contains a path traversal vulnerability in Nextcloud.get_file that allows authenticated re… |
| 2026-11-22 22:17:39 | [CVE-2026-134835](https://nvd.nist.gov/vuln/detail/CVE-2026-134835) | Medium | 5.3 | Langfuse before 4.82.0 contains a server-side request forgery vulnerability that allows organization admins to target i… |
| 2026-11-22 22:17:39 | [CVE-2026-134836](https://nvd.nist.gov/vuln/detail/CVE-2026-134836) | High | 8.6 | Dashy 4.0.0 before 4.9.12 contains a credential disclosure vulnerability in isLocalRequest that attaches user credentia… |
| 2026-11-22 22:17:39 | [CVE-2026-134837](https://nvd.nist.gov/vuln/detail/CVE-2026-134837) | Medium | 5.1 | Frappe before 15.126.0 and 16.x before 16.55.0 contains a prototype pollution vulnerability that allows Dashboard Manag… |
| 2026-11-22 22:17:39 | [CVE-2026-134838](https://nvd.nist.gov/vuln/detail/CVE-2026-134838) | Critical | 9.1 | Weblate before 2026.11 contains an account takeover vulnerability in the reset_password view that allows unauthenticate… |
| 2026-11-22 22:17:39 | [CVE-2026-134839](https://nvd.nist.gov/vuln/detail/CVE-2026-134839) | Medium | 5.3 | Linkwarden before 2.17.0 contains an incorrect authorization vulnerability in the archive upload handler that allows co… |
| 2026-11-22 22:17:40 | [CVE-2026-134840](https://nvd.nist.gov/vuln/detail/CVE-2026-134840) | Medium | 5.3 | HumHub before 1.19.4 contains a missing authorization vulnerability in GroupController actionNewMemberSearch and action… |
| 2026-11-22 22:17:40 | [CVE-2026-134859](https://nvd.nist.gov/vuln/detail/CVE-2026-134859) | Medium | 6.9 | Assimp through 6.0.6 contains an out-of-bounds read vulnerability in PLYImporter::LoadFace and createFromeTriStrip that… |
| 2026-11-22 22:17:40 | [CVE-2026-134860](https://nvd.nist.gov/vuln/detail/CVE-2026-134860) | Medium | 6.9 | Assimp through 6.0.6 contains an out-of-bounds read vulnerability in ReadFloat in ColladaLoader.cpp because accessor st… |
| 2026-11-22 22:17:40 | [CVE-2026-134861](https://nvd.nist.gov/vuln/detail/CVE-2026-134861) | Medium | 6.9 | Assimp through 6.0.6 contains an out-of-bounds write vulnerability in glTFAsset.inl that allows attackers to corrupt me… |
| 2026-11-22 22:17:41 | [CVE-2026-134862](https://nvd.nist.gov/vuln/detail/CVE-2026-134862) | Medium | 6.9 | Assimp through 6.0.6 contains an out-of-bounds read vulnerability in glTFImporter::ImportMeshes that uses NORMAL and TE… |
| 2026-11-22 22:17:41 | [CVE-2026-134863](https://nvd.nist.gov/vuln/detail/CVE-2026-134863) | Medium | 6.8 | Assimp through 6.0.6 contains an invalid pointer dereference vulnerability in glTFImporter::ImportEmbeddedTextures that… |
| 2026-11-22 22:17:41 | [CVE-2026-134864](https://nvd.nist.gov/vuln/detail/CVE-2026-134864) | Medium | 6.8 | Assimp through 6.0.6 contains a use of uninitialized resource vulnerability in glTFImporter::ImportMeshes that builds T… |
| 2026-11-22 22:17:41 | [CVE-2026-134865](https://nvd.nist.gov/vuln/detail/CVE-2026-134865) | Medium | 6.9 | Assimp through 6.0.6 contains an out-of-bounds read vulnerability in ColladaParser::CopyVertex that allows attackers to… |
| 2026-11-22 22:17:41 | [CVE-2026-134866](https://nvd.nist.gov/vuln/detail/CVE-2026-134866) | Medium | 6.8 | Assimp 6.0.0 through 6.0.6 contains an infinite loop vulnerability in SkipLine that allows attackers to hang parsing by… |
| 2026-11-22 22:17:41 | [CVE-2026-134867](https://nvd.nist.gov/vuln/detail/CVE-2026-134867) | Medium | 6.8 | Assimp through 6.0.6 contains an uncontrolled memory allocation vulnerability in FBXConverter::GetRotationKeyframeList… |
| 2026-11-22 22:17:42 | [CVE-2026-134868](https://nvd.nist.gov/vuln/detail/CVE-2026-134868) | Medium | 6.8 | Assimp through 6.0.6 contains an infinite loop vulnerability in ColladaParser::ReadPrimitives that allows attackers to… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
