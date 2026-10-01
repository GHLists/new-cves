# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-01 22:18 UTC

New CVEs published between 2026-10-01 21:18 UTC and 2026-10-01 22:18 UTC.

[Full CSV](data/new-cves-2026-10-01T22-18-45-912735Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-01 22:17:00 | [CVE-2026-104002](https://nvd.nist.gov/vuln/detail/CVE-2026-104002) | Medium | 6.0 | A fail-open error handling issue within the data masking utility of Powertools for AWS Lambda (Python) might allow acto… |
| 2026-10-01 22:17:00 | [CVE-2026-104051](https://nvd.nist.gov/vuln/detail/CVE-2026-104051) | High | 8.8 | PictShare before 3.7.1 contains an information disclosure vulnerability that allows unauthenticated attackers to obtain… |
| 2026-10-01 22:17:00 | [CVE-2026-104356](https://nvd.nist.gov/vuln/detail/CVE-2026-104356) | High | 8.2 | PictShare before version 3.7.1 contains a weak randomness vulnerability where the getRandomString() function uses the n… |
| 2026-10-01 22:17:01 | [CVE-2026-18397](https://nvd.nist.gov/vuln/detail/CVE-2026-18397) | Critical | 9.4 | This vulnerability enables unauthenticated remote code execution (RCE) on a victim's machine by exploiting a combinatio… |
| 2026-10-01 22:17:01 | [CVE-2026-27873](https://nvd.nist.gov/vuln/detail/CVE-2026-27873) | Medium | 5.6 | - Use of Hard-coded Credentials vulnerability in Johnson Controls EasyIO FG allows - Pasword Spraying. This issue affec… |
| 2026-10-01 22:17:01 | [CVE-2026-34493](https://nvd.nist.gov/vuln/detail/CVE-2026-34493) | High | 7.2 | - On-Chip Debug Interface vulnerability in Johnson Controls EasyIO FS32 allows Collect Data from Common Resource Locati… |
| 2026-10-01 22:17:01 | [CVE-2026-34494](https://nvd.nist.gov/vuln/detail/CVE-2026-34494) | High | 7.2 | - On-Chip Debug Interface vulnerability in Johnson Controls Neo Series MVP2 allows Collect Data from Common Resource Lo… |
| 2026-10-01 22:17:02 | [CVE-2026-51873](https://nvd.nist.gov/vuln/detail/CVE-2026-51873) |  |  | Devika v1.0 is vulnerable to Directory Traversal in the Coder.save_code_to_project function, which allows attackers to… |
| 2026-10-01 22:17:02 | [CVE-2026-51874](https://nvd.nist.gov/vuln/detail/CVE-2026-51874) |  |  | In Devika v1.0, the Patcher Agent save_code_to_project function contains a path traversal vulnerability that allows att… |
| 2026-10-01 22:17:02 | [CVE-2026-51875](https://nvd.nist.gov/vuln/detail/CVE-2026-51875) |  |  | In Devika v1.0, the Feature Agent save_code_to_project function contains a path traversal vulnerability that allows att… |
| 2026-10-01 22:17:02 | [CVE-2026-51876](https://nvd.nist.gov/vuln/detail/CVE-2026-51876) |  |  | DeepTutor 1.4.0 contains an authorization bypass vulnerability in the book confirmation flow. An unauthenticated or una… |
| 2026-10-01 22:17:02 | [CVE-2026-51878](https://nvd.nist.gov/vuln/detail/CVE-2026-51878) |  |  | deeptutor 1.4.0 contains an authorization bypass through a user-controlled object identifier in TurnRuntimeManager.rege… |
| 2026-10-01 22:17:02 | [CVE-2026-51879](https://nvd.nist.gov/vuln/detail/CVE-2026-51879) |  |  | deeptutor 1.4.0 contains an authorization bypass through a user-controlled object identifier in TutorBotManager.write_b… |
| 2026-10-01 22:17:02 | [CVE-2026-51880](https://nvd.nist.gov/vuln/detail/CVE-2026-51880) |  |  | deeptutor 1.4.0 contains a path traversal issue in EditFileTool.execute. Through the live tutorbot WebSocket interface,… |
| 2026-10-01 22:17:02 | [CVE-2026-51881](https://nvd.nist.gov/vuln/detail/CVE-2026-51881) |  |  | deeptutor 1.4.0 contains code injection in ExecTool.execute. Through the live tutorbot WebSocket interface, a remote ca… |
| 2026-10-01 22:17:03 | [CVE-2026-51882](https://nvd.nist.gov/vuln/detail/CVE-2026-51882) |  |  | The OpenAI-compatible file upload endpoint `/v1/files` in Langchain-Chatchat 0.3.0 is vulnerable to path traversal. An… |
| 2026-10-01 22:17:03 | [CVE-2026-51883](https://nvd.nist.gov/vuln/detail/CVE-2026-51883) |  |  | The knowledge base creation and document upload interfaces in Langchain-Chatchat 0.3.0;0.3.1 is vulnerable to path trav… |
| 2026-10-01 22:17:03 | [CVE-2026-51884](https://nvd.nist.gov/vuln/detail/CVE-2026-51884) |  |  | The /knowledge_base/upload_temp_docs temporary document upload endpoint in Langchain Chatchat 0.3.1 is vulnerable to pa… |
| 2026-10-01 22:17:03 | [CVE-2026-51886](https://nvd.nist.gov/vuln/detail/CVE-2026-51886) |  |  | langflow-ai langflow v1.9.3 is affected by: Code Injection. The impact is: execute arbitrary code (remote). The compone… |
| 2026-10-01 22:17:03 | [CVE-2026-51888](https://nvd.nist.gov/vuln/detail/CVE-2026-51888) |  |  | langflow-ai langflow v1.8.4 is affected by: Directory Traversal. The impact is: Arbitrary file write outside the intend… |
| 2026-10-01 22:17:03 | [CVE-2026-51892](https://nvd.nist.gov/vuln/detail/CVE-2026-51892) |  |  | infiniflow ragflow 0.24.0 is vulnerable to Incorrect Access Control via /v1/document/get/<doc_id>. |
| 2026-10-01 22:17:03 | [CVE-2026-51893](https://nvd.nist.gov/vuln/detail/CVE-2026-51893) |  |  | infiniflow ragflow 0.24.0 is vulnerable to Incorrect Access Control via trace_mindmap. An externally reachable path acc… |
| 2026-10-01 22:17:03 | [CVE-2026-51894](https://nvd.nist.gov/vuln/detail/CVE-2026-51894) |  |  | infiniflow ragflow 0.24.0 is vulnerable to Incorrect Access Control via run_mindmap. A reachable path accepts a caller-… |
| 2026-10-01 22:17:04 | [CVE-2026-51895](https://nvd.nist.gov/vuln/detail/CVE-2026-51895) |  |  | Ragflow 0.24.0 and prior contains improper access control in update_metadata_setting (api/apps/kb_app.py). Depending on… |
| 2026-10-01 22:17:04 | [CVE-2026-51896](https://nvd.nist.gov/vuln/detail/CVE-2026-51896) |  |  | infiniflow ragflow 0.25.3 contains improper access control in resume (api/apps/connector_app.py). Depending on the expo… |
| 2026-10-01 22:17:04 | [CVE-2026-51897](https://nvd.nist.gov/vuln/detail/CVE-2026-51897) |  |  | RAGFlow 0.24.0 contains improper access control in get_dataset (api/apps/evaluation_app). Depending on the exposed entr… |
| 2026-10-01 22:17:04 | [CVE-2026-64892](https://nvd.nist.gov/vuln/detail/CVE-2026-64892) | Medium | 6.3 | - Exposure of Sensitive Information vulnerability in Johnson Controls Easy IO Neo allows Collect Data from Common Resou… |
| 2026-10-01 22:17:04 | [CVE-2026-64893](https://nvd.nist.gov/vuln/detail/CVE-2026-64893) | High | 7.3 | - Cleartext Transmission of Sensitive Information vulnerability in Johnson Controls EasyIO NEO allows - Man In the Midd… |
| 2026-10-01 22:17:04 | [CVE-2026-71448](https://nvd.nist.gov/vuln/detail/CVE-2026-71448) | Medium | 5.6 | : Insecure Default Initialization of Resource vulnerability in Johnson Controls EasyIO FS32 allows : Authentication Abu… |
| 2026-10-01 22:17:04 | [CVE-2026-71449](https://nvd.nist.gov/vuln/detail/CVE-2026-71449) | Critical | 9.3 | : Use of Hard-coded Cryptographic Key vulnerability in Johnson Controls EasyIO FS32 allows : Retrieve Embedded Sensitiv… |
| 2026-10-01 22:17:05 | [CVE-2026-71452](https://nvd.nist.gov/vuln/detail/CVE-2026-71452) | High | 7.2 | - OS Command Injection vulnerability in Johnson Controls EasyIO FS32 allows OS Command Injection. This issue affects Ea… |
| 2026-10-01 22:17:05 | [CVE-2026-71453](https://nvd.nist.gov/vuln/detail/CVE-2026-71453) | Medium | 5.6 | - External Control of File Name or Path vulnerability in Johnson Controls EasyIO FS32 allows - traversal attack. This i… |
| 2026-10-01 22:17:05 | [CVE-2026-71454](https://nvd.nist.gov/vuln/detail/CVE-2026-71454) | Medium | 5.8 | Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in CWE-79 - Cross-si… |
| 2026-10-01 22:17:05 | [CVE-2026-86344](https://nvd.nist.gov/vuln/detail/CVE-2026-86344) | High | 7.5 | A flaw was found in 389-ds-base. An unauthenticated remote attacker can send a complete LDAP operation followed by the… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
