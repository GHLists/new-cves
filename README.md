# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-12 15:20 UTC

New CVEs published between 2026-11-12 14:18 UTC and 2026-11-12 15:20 UTC.

[Full CSV](data/new-cves-2026-11-12T15-20-18-348103Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-12 15:17:37 | [CVE-2026-116303](https://nvd.nist.gov/vuln/detail/CVE-2026-116303) | Low | 3.1 | Missing authorization in PostgreSQL type conversion allows a database user to invoke a cast function despite lacking EX… |
| 2026-11-12 15:17:38 | [CVE-2026-116304](https://nvd.nist.gov/vuln/detail/CVE-2026-116304) | High | 8.8 | Use after free in PostgreSQL coordination of anonymous RECORD type identifiers among parallel workers allows a database… |
| 2026-11-12 15:17:38 | [CVE-2026-116306](https://nvd.nist.gov/vuln/detail/CVE-2026-116306) | High | 8.8 | Type confusion in PostgreSQL composite-value field assignment allows an object creator to execute arbitrary code as the… |
| 2026-11-12 15:17:38 | [CVE-2026-116307](https://nvd.nist.gov/vuln/detail/CVE-2026-116307) | High | 8.8 | Use after free in PostgreSQL plperl allows an object creator to execute arbitrary code as the operating system user run… |
| 2026-11-12 15:17:38 | [CVE-2026-116308](https://nvd.nist.gov/vuln/detail/CVE-2026-116308) | Medium | 4.3 | Buffer over-read in PostgreSQL dict_int allows a database user to disclose portions of server memory, via a zero-length… |
| 2026-11-12 15:17:38 | [CVE-2026-116309](https://nvd.nist.gov/vuln/detail/CVE-2026-116309) | High | 8.8 | Type confusion in PostgreSQL plperl may allow an object creator to execute arbitrary code, via blessing a non-hash refe… |
| 2026-11-12 15:17:38 | [CVE-2026-116310](https://nvd.nist.gov/vuln/detail/CVE-2026-116310) | Medium | 4.3 | Use after free in PostgreSQL COPY FROM error reporting allows a database user to disclose portions of server memory, vi… |
| 2026-11-12 15:17:39 | [CVE-2026-116311](https://nvd.nist.gov/vuln/detail/CVE-2026-116311) | Medium | 5.4 | Missing authorization in PostgreSQL DROP OWNED allows a role to remove itself from restrictive row level security polic… |
| 2026-11-12 15:17:39 | [CVE-2026-116312](https://nvd.nist.gov/vuln/detail/CVE-2026-116312) | Medium | 5.4 | Inconsistent transition-capture state in PostgreSQL MERGE allows a table data modifier to make an AFTER trigger process… |
| 2026-11-12 15:17:39 | [CVE-2026-116313](https://nvd.nist.gov/vuln/detail/CVE-2026-116313) | High | 7.2 | Untrusted search path in PostgreSQL vacuumdb allows a database owner to execute arbitrary SQL as the database user runn… |
| 2026-11-12 15:17:39 | [CVE-2026-116314](https://nvd.nist.gov/vuln/detail/CVE-2026-116314) | High | 8.8 | Improper input validation in PostgreSQL pg_restore allows a non-plain archive provider to execute arbitrary code as the… |
| 2026-11-12 15:17:39 | [CVE-2026-116315](https://nvd.nist.gov/vuln/detail/CVE-2026-116315) | High | 8.8 | Heap-based buffer overflow in PostgreSQL tsvector_delete() allows a database user to execute arbitrary code as the oper… |
| 2026-11-12 15:17:39 | [CVE-2026-116316](https://nvd.nist.gov/vuln/detail/CVE-2026-116316) | High | 8.8 | Improper protection of alternate path in PostgreSQL security-restricted operations allows an object creator to execute… |
| 2026-11-12 15:17:39 | [CVE-2026-116317](https://nvd.nist.gov/vuln/detail/CVE-2026-116317) | High | 8.8 | Heap-based buffer overflow in PostgreSQL ts_rank_cd() may allow a database user to execute arbitrary code as the operat… |
| 2026-11-12 15:17:40 | [CVE-2026-116318](https://nvd.nist.gov/vuln/detail/CVE-2026-116318) | High | 8.8 | SQL injection in PostgreSQL pg_dump allows an object creator to execute arbitrary SQL as the user restoring the dump, v… |
| 2026-11-12 15:17:40 | [CVE-2026-116319](https://nvd.nist.gov/vuln/detail/CVE-2026-116319) | High | 8.8 | Use after free in PostgreSQL plperl allows an object creator to execute arbitrary code as the operating system user run… |
| 2026-11-12 15:17:40 | [CVE-2026-116320](https://nvd.nist.gov/vuln/detail/CVE-2026-116320) | High | 8.8 | Use after free in PostgreSQL plperl allows an object creator to execute arbitrary code as the operating system user run… |
| 2026-11-12 15:17:40 | [CVE-2026-116321](https://nvd.nist.gov/vuln/detail/CVE-2026-116321) | Medium | 4.3 | Improper null termination in PostgreSQL array element assignment allows a database user to disclose server memory, via… |
| 2026-11-12 15:17:40 | [CVE-2026-116322](https://nvd.nist.gov/vuln/detail/CVE-2026-116322) | Medium | 5.3 | Improper locking in PostgreSQL startup processing allows an unauthenticated network client to trigger a server restart,… |
| 2026-11-12 15:17:40 | [CVE-2026-116323](https://nvd.nist.gov/vuln/detail/CVE-2026-116323) | High | 8.8 | Use after free in PostgreSQL pltcl allows an object creator to execute arbitrary code as the operating system user runn… |
| 2026-11-12 15:17:40 | [CVE-2026-116325](https://nvd.nist.gov/vuln/detail/CVE-2026-116325) | High | 8.0 | SQL injection in PostgreSQL reindexdb allows an object creator to execute arbitrary SQL as the database user running re… |
| 2026-11-12 15:17:41 | [CVE-2026-116326](https://nvd.nist.gov/vuln/detail/CVE-2026-116326) | High | 8.8 | Uncaught exceptions in PostgreSQL plperl allow an object creator to cause use of a stale sigjmp_buf, via a tied Perl ob… |
| 2026-11-12 15:17:41 | [CVE-2026-116327](https://nvd.nist.gov/vuln/detail/CVE-2026-116327) | Medium | 4.3 | Exposure of sensitive information in PostgreSQL security_barrier processing allows a database user to infer values hidd… |
| 2026-11-12 15:17:41 | [CVE-2026-116328](https://nvd.nist.gov/vuln/detail/CVE-2026-116328) | High | 8.8 | Integer wraparound in PostgreSQL generation memory contexts allows a database user to execute arbitrary code as the ope… |
| 2026-11-12 15:17:41 | [CVE-2026-116329](https://nvd.nist.gov/vuln/detail/CVE-2026-116329) | High | 8.8 | Type confusion in PostgreSQL statistics import allows a table maintainer to execute arbitrary code as the operating sys… |
| 2026-11-12 15:17:41 | [CVE-2026-116330](https://nvd.nist.gov/vuln/detail/CVE-2026-116330) | High | 8.8 | Untrusted data inclusion in PostgreSQL pg_dump tar-format restore.sql allows a compromised origin server to execute arb… |
| 2026-11-12 15:17:41 | [CVE-2026-116331](https://nvd.nist.gov/vuln/detail/CVE-2026-116331) | High | 8.8 | Type confusion in PostgreSQL min/max aggregate optimization allows an object creator to execute arbitrary code as the o… |
| 2026-11-12 15:17:41 | [CVE-2026-116332](https://nvd.nist.gov/vuln/detail/CVE-2026-116332) | High | 8.8 | Use after free in PostgreSQL portal setup allows an object creator to execute arbitrary code as the operating system us… |
| 2026-11-12 15:17:41 | [CVE-2026-116333](https://nvd.nist.gov/vuln/detail/CVE-2026-116333) | Medium | 6.5 | Buffer over-read in PostgreSQL parallel B-tree scans allows an object creator to read attacker-chosen server-memory add… |
| 2026-11-12 15:17:42 | [CVE-2026-116335](https://nvd.nist.gov/vuln/detail/CVE-2026-116335) | High | 8.8 | Type confusion in PostgreSQL operator commutator and negator links allows an object creator to execute arbitrary code a… |
| 2026-11-12 15:17:42 | [CVE-2026-116336](https://nvd.nist.gov/vuln/detail/CVE-2026-116336) | High | 8.8 | Operation on a dropped index in PostgreSQL REINDEX CONCURRENTLY allows an object creator to execute arbitrary code as t… |
| 2026-11-12 15:17:42 | [CVE-2026-120139](https://nvd.nist.gov/vuln/detail/CVE-2026-120139) | High | 8.8 | Integer wraparound in PostgreSQL in-memory tuple-size calculations allows a database user to execute arbitrary code as… |
| 2026-11-12 15:17:42 | [CVE-2026-120141](https://nvd.nist.gov/vuln/detail/CVE-2026-120141) | High | 8.8 | Type confusion in PostgreSQL materialized set-returning functions allows a database user to execute arbitrary code as t… |
| 2026-11-12 15:17:42 | [CVE-2026-120142](https://nvd.nist.gov/vuln/detail/CVE-2026-120142) | High | 8.8 | Type confusion in PostgreSQL anonymous RECORD types allows an object creator to execute arbitrary code as the operating… |
| 2026-11-12 15:17:42 | [CVE-2026-120143](https://nvd.nist.gov/vuln/detail/CVE-2026-120143) | High | 8.8 | Use after free in PostgreSQL trigger functions allows an object creator to execute arbitrary code as the operating syst… |
| 2026-11-12 15:17:42 | [CVE-2026-120144](https://nvd.nist.gov/vuln/detail/CVE-2026-120144) | High | 8.8 | Type confusion from incomplete PostgreSQL type-cache invalidation allows an object creator to execute arbitrary code as… |
| 2026-11-12 15:17:43 | [CVE-2026-120145](https://nvd.nist.gov/vuln/detail/CVE-2026-120145) | High | 8.8 | Missing authorization in PostgreSQL logical replication allows a compromised publisher to execute arbitrary code as the… |
| 2026-11-12 15:17:43 | [CVE-2026-120146](https://nvd.nist.gov/vuln/detail/CVE-2026-120146) | Medium | 4.3 | Missing authorization in PostgreSQL REASSIGN OWNED allows a role granted INHERIT but not SET to transfer objects to the… |
| 2026-11-12 15:17:43 | [CVE-2026-120147](https://nvd.nist.gov/vuln/detail/CVE-2026-120147) | High | 8.8 | Use after free in the PostgreSQL dblink extension allows an object creator to execute arbitrary code as the operating s… |
| 2026-11-12 15:17:43 | [CVE-2026-120148](https://nvd.nist.gov/vuln/detail/CVE-2026-120148) | High | 8.1 | Type confusion in PostgreSQL extended statistics allows an object creator to execute arbitrary code as the operating sy… |
| 2026-11-12 15:17:43 | [CVE-2026-120149](https://nvd.nist.gov/vuln/detail/CVE-2026-120149) | High | 8.8 | Heap-based buffer overflow in PostgreSQL foreign batch inserts allows a foreign server to execute arbitrary code, via r… |
| 2026-11-12 15:17:43 | [CVE-2026-120150](https://nvd.nist.gov/vuln/detail/CVE-2026-120150) | High | 8.8 | Use after free in PostgreSQL expanded-record domain checks allows an object creator to execute arbitrary code as the op… |
| 2026-11-12 15:17:43 | [CVE-2026-120151](https://nvd.nist.gov/vuln/detail/CVE-2026-120151) | High | 8.8 | Type confusion in PostgreSQL plpgsql record-field assignment allows an object creator to execute arbitrary code as the… |
| 2026-11-12 15:17:43 | [CVE-2026-120152](https://nvd.nist.gov/vuln/detail/CVE-2026-120152) | Medium | 4.3 | Use after free in PostgreSQL pg_show_all_settings() allows a database user to retrieve memory contents, via loading a m… |
| 2026-11-12 15:17:44 | [CVE-2026-120153](https://nvd.nist.gov/vuln/detail/CVE-2026-120153) | High | 7.2 | SQL injection in PostgreSQL extension-script substitutions allows an attacker with database-level CREATE privilege to e… |
| 2026-11-12 15:17:44 | [CVE-2026-120154](https://nvd.nist.gov/vuln/detail/CVE-2026-120154) | Medium | 4.3 | Improper protection in PostgreSQL INSERT ... ON CONFLICT allows an attacker having INSERT, UPDATE, and applicable SELEC… |
| 2026-11-12 15:17:46 | [CVE-2026-123790](https://nvd.nist.gov/vuln/detail/CVE-2026-123790) |  |  | ComfyUI-Easy-Use version 1.3.6 contains a path traversal vulnerability in the `save_preview()` handler for POST `/easyu… |
| 2026-11-12 15:17:48 | [CVE-2026-126996](https://nvd.nist.gov/vuln/detail/CVE-2026-126996) | Low | 2.1 | A vulnerability was determined in SakanaAI text-to-LoRA 0.0.1. Affected by this issue is the function get_tokenizer of… |
| 2026-11-12 15:17:49 | [CVE-2026-126997](https://nvd.nist.gov/vuln/detail/CVE-2026-126997) | Medium | 5.5 | A vulnerability was identified in JeecgBoot up to 3.9.6. This affects the function RestTemplate.exchange of the file or… |
| 2026-11-12 15:17:49 | [CVE-2026-126998](https://nvd.nist.gov/vuln/detail/CVE-2026-126998) | Medium | 5.5 | A security flaw has been discovered in JeecgBoot up to 3.9.5. This vulnerability affects the function OpenApiController… |
| 2026-11-12 15:17:49 | [CVE-2026-14661](https://nvd.nist.gov/vuln/detail/CVE-2026-14661) | High | 8.1 | External control of file name in PostgreSQL dblink and CREATE/ALTER SUBSCRIPTION allows a user to achieve persistent de… |
| 2026-11-12 15:17:50 | [CVE-2026-16237](https://nvd.nist.gov/vuln/detail/CVE-2026-16237) | Medium | 5.4 | Improper protection in PostgreSQL INSERT ... ON CONFLICT on auto-updatable views allows an attacker having INSERT and U… |
| 2026-11-12 15:17:50 | [CVE-2026-16240](https://nvd.nist.gov/vuln/detail/CVE-2026-16240) | Low | 3.7 | Use of externally-controlled format string in PostgreSQL pg_basebackup allows an attacker having already compromised a… |
| 2026-11-12 15:17:51 | [CVE-2026-18447](https://nvd.nist.gov/vuln/detail/CVE-2026-18447) | High | 8.8 | Type confusion in PostgreSQL SQL-language functions allows an object creator to execute arbitrary code as the operating… |
| 2026-11-12 15:17:51 | [CVE-2026-6460](https://nvd.nist.gov/vuln/detail/CVE-2026-6460) | High | 8.8 | Type confusion in PostgreSQL allows an object creator to execute arbitrary code as the operating system user running th… |
| 2026-11-12 15:17:51 | [CVE-2026-6467](https://nvd.nist.gov/vuln/detail/CVE-2026-6467) | High | 7.2 | Uncontrolled search path element in PostgreSQL CREATE EXTENSION allows an attacker with database-level CREATE privilege… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
