# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 19:20 UTC

New CVEs published between 2026-11-02 18:18 UTC and 2026-11-02 19:20 UTC.

[Full CSV](data/new-cves-2026-11-02T19-20-06-837769Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 19:17:49 | [CVE-2026-105603](https://nvd.nist.gov/vuln/detail/CVE-2026-105603) | Critical | 9.4 | Joomla Extension - dj-extensions.com - Authenticated arbitrary file upload in DJ-Classifieds < 3.11.3 - The Joomla exte… |
| 2026-11-02 19:17:49 | [CVE-2026-105604](https://nvd.nist.gov/vuln/detail/CVE-2026-105604) | Critical | 9.3 | Joomla Extension - dj-extensions.com - Unauthenticated SQL injection in DJ-Classifieds < 3.11.3 - The Joomla extension… |
| 2026-11-02 19:17:50 | [CVE-2026-105605](https://nvd.nist.gov/vuln/detail/CVE-2026-105605) | Medium | 5.3 | Joomla Extension - dj-extensions.com - IDOR vulnerability allowing cross-account ad access in DJ-Classifieds < 3.11.3 -… |
| 2026-11-02 19:17:50 | [CVE-2026-105606](https://nvd.nist.gov/vuln/detail/CVE-2026-105606) | Critical | 9.5 | Joomla Extension - joomlaboat.com - Unauthenticated arbitrary file upload in Custom Tables < 3.7.8 - An unauthenticated… |
| 2026-11-02 19:18:00 | [CVE-2026-117069](https://nvd.nist.gov/vuln/detail/CVE-2026-117069) |  |  | An integer truncation vulnerability in the NAS decoder of OpenAirInterface (OAI) CN5G AMF v2.2.1 allows an unauthentica… |
| 2026-11-02 19:18:00 | [CVE-2026-117127](https://nvd.nist.gov/vuln/detail/CVE-2026-117127) |  |  | Directory Traversal vulnerability in Gleez GleezCMS v.1.2.0 allows a remote attacker to obtain sensitive information vi… |
| 2026-11-02 19:18:01 | [CVE-2026-119731](https://nvd.nist.gov/vuln/detail/CVE-2026-119731) | High | 8.7 | Munshi (by Petpooja) before 2026-06-30 contained a payment bypass vulnerability in its subscription payment webhook at… |
| 2026-11-02 19:18:01 | [CVE-2026-119732](https://nvd.nist.gov/vuln/detail/CVE-2026-119732) | High | 7.1 | Munshi (by Petpooja) before 2026-07-28 contained a broken object level authorization vulnerability that allows authenti… |
| 2026-11-02 19:18:02 | [CVE-2026-119733](https://nvd.nist.gov/vuln/detail/CVE-2026-119733) | High | 7.2 | Munshi (by Petpooja) before 2026-07-07 contained a missing authorization vulnerability in its company deletion workflow… |
| 2026-11-02 19:18:02 | [CVE-2026-119734](https://nvd.nist.gov/vuln/detail/CVE-2026-119734) | High | 7.1 | Munshi (by Petpooja) before 2026-06-17 contained a broken object level authorization vulnerability that allows authenti… |
| 2026-11-02 19:18:02 | [CVE-2026-119735](https://nvd.nist.gov/vuln/detail/CVE-2026-119735) | Medium | 5.1 | Munshi (by Petpooja) before 2026-07-13 contained a stored cross-site scripting vulnerability that allows authenticated… |
| 2026-11-02 19:18:02 | [CVE-2026-119736](https://nvd.nist.gov/vuln/detail/CVE-2026-119736) | High | 8.8 | Attendo (formerly Petpooja Payroll) Admin Android application version 3.0.13 and earlier contains a hard-coded credenti… |
| 2026-11-02 19:18:02 | [CVE-2026-120057](https://nvd.nist.gov/vuln/detail/CVE-2026-120057) | High | 7.5 | psqlODBC copies the reply to a large-object read (loread) into the application's buffer using the length sent by the se… |
| 2026-11-02 19:18:02 | [CVE-2026-120058](https://nvd.nist.gov/vuln/detail/CVE-2026-120058) | High | 7.5 | psqlODBC sizes its row cache from the column count of a cursor's first result, but recomputes the column count from eac… |
| 2026-11-02 19:18:02 | [CVE-2026-120059](https://nvd.nist.gov/vuln/detail/CVE-2026-120059) | Medium | 6.8 | For an updatable cursor over a table without OIDs that has an auto-increment int4 column, psqlODBC places that column's… |
| 2026-11-02 19:18:03 | [CVE-2026-120060](https://nvd.nist.gov/vuln/detail/CVE-2026-120060) | Medium | 5.9 | psqlODBC trusts counts and lengths in server data in three places. SQLBulkOperations uses a server-supplied row count i… |
| 2026-11-02 19:18:03 | [CVE-2026-120061](https://nvd.nist.gov/vuln/detail/CVE-2026-120061) | High | 7.5 | The psqlODBC parser for ODBC escape sequences in application SQL text writes the argument offsets of a {fn} escape into… |
| 2026-11-02 19:18:03 | [CVE-2026-120062](https://nvd.nist.gov/vuln/detail/CVE-2026-120062) | High | 7.5 | SQLSpecialColumns in psqlODBC splices the table and schema names it receives into its catalog query without escaping th… |
| 2026-11-02 19:18:03 | [CVE-2026-120063](https://nvd.nist.gov/vuln/detail/CVE-2026-120063) | Medium | 5.9 | When psqlODBC quotes a schema or table name into a 128-byte stack buffer, its length check lets it write up to two byte… |
| 2026-11-02 19:18:03 | [CVE-2026-120064](https://nvd.nist.gov/vuln/detail/CVE-2026-120064) | High | 7.5 | Several psqlODBC entry points use an application-supplied column number or row index as an array index without validati… |
| 2026-11-02 19:18:03 | [CVE-2026-120065](https://nvd.nist.gov/vuln/detail/CVE-2026-120065) | High | 7.1 | For an updatable cursor over a table without OIDs that has an auto-increment int4 column, psqlODBC uses that column to… |
| 2026-11-02 19:18:03 | [CVE-2026-120066](https://nvd.nist.gov/vuln/detail/CVE-2026-120066) | Medium | 5.3 | On Unix-like systems, when logging is enabled, psqlODBC creates its log files in /tmp by default, named from the progra… |
| 2026-11-02 19:18:04 | [CVE-2026-120067](https://nvd.nist.gov/vuln/detail/CVE-2026-120067) | Medium | 5.9 | For updatable cursors, which are enabled by default, psqlODBC adds hidden ctid and, for tables with OIDs, oid columns t… |
| 2026-11-02 19:18:04 | [CVE-2026-120497](https://nvd.nist.gov/vuln/detail/CVE-2026-120497) | Medium | 4.6 | Stored cross-site scripting (XSS) in the HTML report generator in the aidlc-traceability CLI in AWS AI-DLC Workflows be… |
| 2026-11-02 19:18:04 | [CVE-2026-120656](https://nvd.nist.gov/vuln/detail/CVE-2026-120656) |  |  | OpenKruise kruise-manager exposes an unauthenticated ppof endpoint when enabled, opening it on 0.0.0.0:8090, which can… |
| 2026-11-02 19:18:10 | [CVE-2026-67186](https://nvd.nist.gov/vuln/detail/CVE-2026-67186) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-02 19:18:11 | [CVE-2026-81938](https://nvd.nist.gov/vuln/detail/CVE-2026-81938) | High | 7.7 | Grafana Mimir's Alertmanager rejects tenant-supplied receiver configurations that reference local files, but the check… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
