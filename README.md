# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-20 15:20 UTC

New CVEs published between 2026-11-20 14:21 UTC and 2026-11-20 15:20 UTC.

[Full CSV](data/new-cves-2026-11-20T15-20-36-656373Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-20 15:17:39 | [CVE-2026-126054](https://nvd.nist.gov/vuln/detail/CVE-2026-126054) | Critical | 9.3 | A Path Traversal vulnerability in workspace directory handling and Git integration in Google Cloud Dataform, BigQuery S… |
| 2026-11-20 15:17:40 | [CVE-2026-126334](https://nvd.nist.gov/vuln/detail/CVE-2026-126334) | Medium | 6.0 | Incorrect Authorization vulnerability in phoenixframework phoenix_live_view allows an authenticated user to mount a rou… |
| 2026-11-20 15:17:40 | [CVE-2026-127027](https://nvd.nist.gov/vuln/detail/CVE-2026-127027) | Critical | 9.2 | Poste.io is vulnerable to remote code execution in DMARC report processing. Email sent to dmarc-reports@<domain> is sav… |
| 2026-11-20 15:17:47 | [CVE-2026-132658](https://nvd.nist.gov/vuln/detail/CVE-2026-132658) | Critical | 9.4 | In Postgres Enterprise Manager (PEM), the pem_agent role, which every PEM agent login inherits, is a member of the Post… |
| 2026-11-20 15:17:47 | [CVE-2026-132659](https://nvd.nist.gov/vuln/detail/CVE-2026-132659) | Critical | 9.4 | In Postgres Enterprise Manager (PEM), the row-level security policies on pem.job and pem.jobstep that apply to PEM agen… |
| 2026-11-20 15:17:47 | [CVE-2026-132660](https://nvd.nist.gov/vuln/detail/CVE-2026-132660) | Critical | 9.4 | In Postgres Enterprise Manager (PEM), several SECURITY DEFINER functions in the pem schema of the PEM backend database… |
| 2026-11-20 15:17:47 | [CVE-2026-132661](https://nvd.nist.gov/vuln/detail/CVE-2026-132661) | High | 7.6 | In Postgres Enterprise Manager (PEM), multi-factor authentication (MFA) is not enforced on the PEM web application's ow… |
| 2026-11-20 15:17:48 | [CVE-2026-132662](https://nvd.nist.gov/vuln/detail/CVE-2026-132662) | High | 7.2 | In Postgres Enterprise Manager (PEM), the SQL Profiler save and load functions in the PEM web application do not keep t… |
| 2026-11-20 15:17:48 | [CVE-2026-132663](https://nvd.nist.gov/vuln/detail/CVE-2026-132663) | High | 7.1 | In Postgres Enterprise Manager (PEM), webhook URLs are not validated, and the PEM agent does not restrict the URL schem… |
| 2026-11-20 15:17:48 | [CVE-2026-132664](https://nvd.nist.gov/vuln/detail/CVE-2026-132664) | High | 7.0 | In Postgres Enterprise Manager (PEM), any PEM user can read the encrypted passwords that PEM agents use to connect to m… |
| 2026-11-20 15:17:48 | [CVE-2026-132665](https://nvd.nist.gov/vuln/detail/CVE-2026-132665) | Medium | 5.8 | In Postgres Enterprise Manager (PEM), the pem.deploy_job_template() function does not check that the caller can access… |
| 2026-11-20 15:17:48 | [CVE-2026-132668](https://nvd.nist.gov/vuln/detail/CVE-2026-132668) | Low | 2.3 | In Postgres Enterprise Manager (PEM), any PEM user can run the pem.send_webhook() function, which runs with elevated pr… |
| 2026-11-20 15:17:49 | [CVE-2026-133612](https://nvd.nist.gov/vuln/detail/CVE-2026-133612) | Low | 2.0 | A weakness has been identified in SqueezeAILab SqueezeLLM up to a5fd71f353bf569feb7b55737c1c1493e78e8f31. This vulnerab… |
| 2026-11-20 15:17:49 | [CVE-2026-133616](https://nvd.nist.gov/vuln/detail/CVE-2026-133616) | Low | 2.0 | A vulnerability was found in sonos tract up to 0.23.4. The affected element is the function InferenceRulesOp::rules of… |
| 2026-11-20 15:17:50 | [CVE-2026-133621](https://nvd.nist.gov/vuln/detail/CVE-2026-133621) | Medium | 5.3 | A flaw has been found in shader-slang slangpy up to 0.43.1. This vulnerability affects the function tinyexr::DecodePixe… |
| 2026-11-20 15:17:50 | [CVE-2026-133629](https://nvd.nist.gov/vuln/detail/CVE-2026-133629) | Low | 2.1 | A vulnerability was determined in Sunnet CTMS up to 10.11. Impacted is an unknown function of the file /cltcms/api/exte… |
| 2026-11-20 15:17:51 | [CVE-2026-133837](https://nvd.nist.gov/vuln/detail/CVE-2026-133837) | High | 7.1 | flowintel contains an authorization bypass in its task completion workflow for privileged cases. Users with lower-privi… |
| 2026-11-20 15:17:51 | [CVE-2026-133838](https://nvd.nist.gov/vuln/detail/CVE-2026-133838) | Medium | 5.3 | FlowIntel contains an authorization bypass that allows non-approver case members to modify restricted tasks (those in R… |
| 2026-11-20 15:17:51 | [CVE-2026-133839](https://nvd.nist.gov/vuln/detail/CVE-2026-133839) | High | 7.1 | FlowIntel contains a missing authorization vulnerability in its task file deletion functionality. When a privileged tas… |
| 2026-11-20 15:17:51 | [CVE-2026-133840](https://nvd.nist.gov/vuln/detail/CVE-2026-133840) | Medium | 5.3 | flowintel contains an authorization bypass in the file-to-note conversion feature for case tasks. When a task is in a r… |
| 2026-11-20 15:17:51 | [CVE-2026-133841](https://nvd.nist.gov/vuln/detail/CVE-2026-133841) | Medium | 5.3 | FlowIntel contains an authorization bypass in its case serialization logic that allows an authenticated user to view me… |
| 2026-11-20 15:17:52 | [CVE-2026-133843](https://nvd.nist.gov/vuln/detail/CVE-2026-133843) | Medium | 5.3 | flowintel contains a vulnerability in the MISP correlation feature that allows unauthorized disclosure of case identifi… |
| 2026-11-20 15:17:52 | [CVE-2026-133844](https://nvd.nist.gov/vuln/detail/CVE-2026-133844) | Medium | 5.3 | FlowIntel, a threat intelligence case management platform, contains an information disclosure vulnerability in its case… |
| 2026-11-20 15:17:52 | [CVE-2026-133846](https://nvd.nist.gov/vuln/detail/CVE-2026-133846) | Medium | 5.3 | FlowIntel contains an authorization bypass in its task management workflow. When a user reopens a completed task (by to… |
| 2026-11-20 15:17:52 | [CVE-2026-133847](https://nvd.nist.gov/vuln/detail/CVE-2026-133847) | High | 8.4 | flowintel contains an authorization bypass in the browser-based admin user editing interface. The edit_user view in the… |
| 2026-11-20 15:17:52 | [CVE-2026-133848](https://nvd.nist.gov/vuln/detail/CVE-2026-133848) | High | 8.3 | flowintel contains an authorization flaw in its user deletion functionality. Organization-scoped administrators (org ad… |
| 2026-11-20 15:17:53 | [CVE-2026-133849](https://nvd.nist.gov/vuln/detail/CVE-2026-133849) | High | 7.1 | A vulnerability exists in the flowintel application's calendar functionality that allows unauthorized access to private… |
| 2026-11-20 15:17:53 | [CVE-2026-133850](https://nvd.nist.gov/vuln/detail/CVE-2026-133850) | Medium | 5.3 | flowintel contains an authorization flaw in its recurring reminder notification subsystem. When a user is subscribed to… |
| 2026-11-20 15:17:53 | [CVE-2026-133851](https://nvd.nist.gov/vuln/detail/CVE-2026-133851) | Medium | 5.3 | FlowIntel's alerting module contained an authorization bypass in the alert access control logic. When an alert was link… |
| 2026-11-20 15:17:53 | [CVE-2026-133852](https://nvd.nist.gov/vuln/detail/CVE-2026-133852) | Medium | 5.3 | flowintel is a case management application that enforces an approval workflow for tasks in privileged cases. Tasks in s… |
| 2026-11-20 15:17:53 | [CVE-2026-133853](https://nvd.nist.gov/vuln/detail/CVE-2026-133853) | Medium | 6.0 | FlowIntel's chatbot component used a single shared MCP (Model Context Protocol) session and process-wide environment va… |
| 2026-11-20 15:17:54 | [CVE-2026-133854](https://nvd.nist.gov/vuln/detail/CVE-2026-133854) | High | 7.1 | flowintel contains a vulnerability in the case and task classification usage endpoints that allows authenticated users… |
| 2026-11-20 15:17:54 | [CVE-2026-133855](https://nvd.nist.gov/vuln/detail/CVE-2026-133855) | Medium | 5.3 | flowintel contains an information disclosure vulnerability in its case history feature. When a user views the history o… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
