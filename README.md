# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-09 10:18 UTC

New CVEs published between 2026-11-09 09:18 UTC and 2026-11-09 10:18 UTC.

[Full CSV](data/new-cves-2026-11-09T10-18-56-188786Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-09 10:17:02 | [CVE-2026-101031](https://nvd.nist.gov/vuln/detail/CVE-2026-101031) |  |  | The `example_dag_decorator` example Dag shipped with Apache Airflow validated an IP address fetched over HTTP with Pyth… |
| 2026-11-09 10:17:02 | [CVE-2026-107474](https://nvd.nist.gov/vuln/detail/CVE-2026-107474) |  |  | The Apache Airflow connections API did not mask the apprise provider's `config` connection extra, which can embed notif… |
| 2026-11-09 10:17:02 | [CVE-2026-111395](https://nvd.nist.gov/vuln/detail/CVE-2026-111395) |  |  | Apache Airflow did not reject reserved serialization keys inside a Dag run's `conf`. A user allowed to trigger a Dag th… |
| 2026-11-09 10:17:03 | [CVE-2026-111403](https://nvd.nist.gov/vuln/detail/CVE-2026-111403) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Inventory WP I… |
| 2026-11-09 10:17:03 | [CVE-2026-111421](https://nvd.nist.gov/vuln/detail/CVE-2026-111421) |  |  | Apache Airflow's Task Execution API stored XCom values written by a task without the reserved-key check applied elsewhe… |
| 2026-11-09 10:17:03 | [CVE-2026-111452](https://nvd.nist.gov/vuln/detail/CVE-2026-111452) |  |  | Apache Airflow's secrets masker matched sensitive key names only in their snake_case form, so values stored under camel… |
| 2026-11-09 10:17:04 | [CVE-2026-111453](https://nvd.nist.gov/vuln/detail/CVE-2026-111453) |  |  | Apache Airflow's API endpoint for deleting an asset's queued events checked Dag edit permission against the `dag_id` qu… |
| 2026-11-09 10:17:04 | [CVE-2026-111454](https://nvd.nist.gov/vuln/detail/CVE-2026-111454) |  |  | Apache Airflow's asset API endpoints returned the IDs of Dags that are scheduled on, produce, or consume an asset witho… |
| 2026-11-09 10:17:05 | [CVE-2026-111455](https://nvd.nist.gov/vuln/detail/CVE-2026-111455) |  |  | Apache Airflow's asynchronous connection test checked permissions when the test was queued — only create permission whe… |
| 2026-11-09 10:17:05 | [CVE-2026-113504](https://nvd.nist.gov/vuln/detail/CVE-2026-113504) |  |  | Apache Airflow's secrets masker stopped descending into nested structures after five levels, so a secret registered wit… |
| 2026-11-09 10:17:05 | [CVE-2026-113508](https://nvd.nist.gov/vuln/detail/CVE-2026-113508) |  |  | Apache Airflow's logout endpoint attempted to revoke the presented token on the server, but any failure during revocati… |
| 2026-11-09 10:17:05 | [CVE-2026-119483](https://nvd.nist.gov/vuln/detail/CVE-2026-119483) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in 10Web Form Maker… |
| 2026-11-09 10:17:05 | [CVE-2026-119497](https://nvd.nist.gov/vuln/detail/CVE-2026-119497) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in wpWax Directorist… |
| 2026-11-09 10:17:06 | [CVE-2026-119503](https://nvd.nist.gov/vuln/detail/CVE-2026-119503) | Medium | 6.5 | Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in Welcart Welcart e-Commer… |
| 2026-11-09 10:17:06 | [CVE-2026-119504](https://nvd.nist.gov/vuln/detail/CVE-2026-119504) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in DynamiApps Fronte… |
| 2026-11-09 10:17:06 | [CVE-2026-119505](https://nvd.nist.gov/vuln/detail/CVE-2026-119505) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Welcart Welcart e… |
| 2026-11-09 10:17:06 | [CVE-2026-119514](https://nvd.nist.gov/vuln/detail/CVE-2026-119514) | Medium | 6.3 | Incorrect Privilege Assignment vulnerability in Webful Creations RepairBuddy computer-repair-shop allows Privilege Esca… |
| 2026-11-09 10:17:07 | [CVE-2026-121760](https://nvd.nist.gov/vuln/detail/CVE-2026-121760) | High | 7.5 | Missing Authorization vulnerability in weDevs weDocs wedocs allows Exploiting Incorrectly Configured Access Control Sec… |
| 2026-11-09 10:17:07 | [CVE-2026-121763](https://nvd.nist.gov/vuln/detail/CVE-2026-121763) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WPMU DEV Hummingb… |
| 2026-11-09 10:17:07 | [CVE-2026-121764](https://nvd.nist.gov/vuln/detail/CVE-2026-121764) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in FolioVision FV Fl… |
| 2026-11-09 10:17:07 | [CVE-2026-121780](https://nvd.nist.gov/vuln/detail/CVE-2026-121780) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Gijo Varghese Fly… |
| 2026-11-09 10:17:07 | [CVE-2026-123463](https://nvd.nist.gov/vuln/detail/CVE-2026-123463) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Wham Checkout… |
| 2026-11-09 10:17:08 | [CVE-2026-123465](https://nvd.nist.gov/vuln/detail/CVE-2026-123465) | High | 7.5 | Exposure of Sensitive System Information to an Unauthorized Control Sphere vulnerability in myCred myCred mycred allows… |
| 2026-11-09 10:17:08 | [CVE-2026-123484](https://nvd.nist.gov/vuln/detail/CVE-2026-123484) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Crocoblock JetFor… |
| 2026-11-09 10:17:08 | [CVE-2026-124586](https://nvd.nist.gov/vuln/detail/CVE-2026-124586) | Medium | 5.5 | A vulnerability was determined in Tencent RapidJSON 1.1.0. Impacted is the function GetCachedPowerByIndex in the librar… |
| 2026-11-09 10:17:08 | [CVE-2026-124587](https://nvd.nist.gov/vuln/detail/CVE-2026-124587) | Low | 2.1 | A vulnerability was identified in elizaOS eliza 2.0.3-beta.7. The affected element is an unknown function of the file p… |
| 2026-11-09 10:17:09 | [CVE-2026-124588](https://nvd.nist.gov/vuln/detail/CVE-2026-124588) | Low | 2.1 | A security flaw has been discovered in huggingface finetrainers 0.1.0/0.2.0. The impacted element is the function resol… |
| 2026-11-09 10:17:09 | [CVE-2026-124589](https://nvd.nist.gov/vuln/detail/CVE-2026-124589) | Low | 2.1 | A weakness has been identified in lxtGH OMG-Seg up to f3b26b609bae919760cd3ccf09c36179bb8624a0. This affects the functi… |
| 2026-11-09 10:17:09 | [CVE-2026-124637](https://nvd.nist.gov/vuln/detail/CVE-2026-124637) | Medium | 5.3 | A stored Cross-Site Scripting (XSS) vulnerability was identified in the profile editing form, in the parameters: cliNom… |
| 2026-11-09 10:17:10 | [CVE-2026-40913](https://nvd.nist.gov/vuln/detail/CVE-2026-40913) |  |  | Apache Airflow's public Import Errors API returns the raw parse-failure stack trace to any user with the `ImportError.c… |
| 2026-11-09 10:17:10 | [CVE-2026-50204](https://nvd.nist.gov/vuln/detail/CVE-2026-50204) |  |  | Apache Airflow's audit log stored Connection and Variable secret values in cleartext in the `Log.extra` column because… |
| 2026-11-09 10:17:10 | [CVE-2026-54863](https://nvd.nist.gov/vuln/detail/CVE-2026-54863) | High | 7.1 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Mamunur Rashid Re… |
| 2026-11-09 10:17:10 | [CVE-2026-66675](https://nvd.nist.gov/vuln/detail/CVE-2026-66675) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in StylemixThemes Mo… |
| 2026-11-09 10:17:11 | [CVE-2026-68982](https://nvd.nist.gov/vuln/detail/CVE-2026-68982) |  |  | Apache Airflow's CeleryExecutor ran callback workloads (`ExecuteCallback`, used for deadline-alert callbacks) without v… |
| 2026-11-09 10:17:11 | [CVE-2026-76185](https://nvd.nist.gov/vuln/detail/CVE-2026-76185) |  |  | Apache Airflow's Task SDK secret cache built its keys from the team name and secret id with unescaped `_` delimiters, s… |
| 2026-11-09 10:17:11 | [CVE-2026-82337](https://nvd.nist.gov/vuln/detail/CVE-2026-82337) |  |  | Apache Airflow rebuilt deadline alert fields through generic deserialization, which imports and instantiates the class… |
| 2026-11-09 10:17:11 | [CVE-2026-82436](https://nvd.nist.gov/vuln/detail/CVE-2026-82436) |  |  | Description `DefaultStateSerializer`, used to persist and restore stateful bolt checkpoints, configured Kryo with class… |
| 2026-11-09 10:17:11 | [CVE-2026-82440](https://nvd.nist.gov/vuln/detail/CVE-2026-82440) |  |  | Description Nimbus instantiates the class named by a topology's `topology.scheduler.strategy` when scheduling it. The a… |
| 2026-11-09 10:17:11 | [CVE-2026-86468](https://nvd.nist.gov/vuln/detail/CVE-2026-86468) |  |  | Apache Airflow's CLI records its arguments in the audit log but masks secrets by argument position, so some supported c… |
| 2026-11-09 10:17:13 | [CVE-2026-86829](https://nvd.nist.gov/vuln/detail/CVE-2026-86829) |  |  | Apache Airflow's scheduler fully deserializes XCom values written by task code while evaluating task dependencies. A Da… |
| 2026-11-09 10:17:15 | [CVE-2026-92683](https://nvd.nist.gov/vuln/detail/CVE-2026-92683) | High | 8.6 | Incorrect authorization in the @authentication directive JWT where filter evaluation in Neo4j @neo4j/graphql versions 7… |
| 2026-11-09 10:17:16 | [CVE-2026-96285](https://nvd.nist.gov/vuln/detail/CVE-2026-96285) |  |  | Apache Airflow 3.3.1 shipped a fix for CVE-2026-67260 that checks the scheduler's decoded `next_kwargs` value is a dict… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
