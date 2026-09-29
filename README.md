# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-29 09:20 UTC

New CVEs published between 2026-09-29 08:24 UTC and 2026-09-29 09:20 UTC.

[Full CSV](data/new-cves-2026-09-29T09-20-19-227958Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-09-29 09:17:09 | [CVE-2026-91012](https://nvd.nist.gov/vuln/detail/CVE-2026-91012) |  |  | org.apache.karaf.config.core.impl.ConfigRepositoryImpl#update(pid, properties), which backs the "config" MBean and the… |
| 2026-09-29 09:17:10 | [CVE-2026-91048](https://nvd.nist.gov/vuln/detail/CVE-2026-91048) |  |  | The jdbc shell command scope shipped no org.apache.karaf.command.acl.jdbc.cfg. Karaf's command guard (SecuredSessionFac… |
| 2026-09-29 09:17:10 | [CVE-2026-91085](https://nvd.nist.gov/vuln/detail/CVE-2026-91085) |  |  | Apache Karaf's shell/SSH command security is enforced by per-scope ACL configuration files (etc/org.apache.karaf.comman… |
| 2026-09-29 09:17:10 | [CVE-2026-92142](https://nvd.nist.gov/vuln/detail/CVE-2026-92142) |  |  | Apache Karaf exposes a JMX MBeanServer guarded by KarafMBeanServerGuard, which enforces role-based access control (RBAC… |
| 2026-09-29 09:17:10 | [CVE-2026-96428](https://nvd.nist.gov/vuln/detail/CVE-2026-96428) | Critical | 9.3 | SQL Injection in the /WebAgenda/SMBAjaxAutoComplete.do API endpoint of Flowring Agentflow 4.0 version before 2025/08/08… |
| 2026-09-29 09:17:10 | [CVE-2026-96429](https://nvd.nist.gov/vuln/detail/CVE-2026-96429) | Critical | 9.3 | SQL Injection in the /WebAgenda/SMBAjaxConfigProcess.do API endpoint of Flowring Agentflow 4.0 version before 2025/08/0… |
| 2026-09-29 09:17:11 | [CVE-2026-96430](https://nvd.nist.gov/vuln/detail/CVE-2026-96430) | High | 8.7 | Exposed Dangerous Method or Function in the /WebAgenda/SQLWin.do API endpoint of Flowring Agentflow 4.0 version Before… |
| 2026-09-29 09:17:11 | [CVE-2026-96431](https://nvd.nist.gov/vuln/detail/CVE-2026-96431) | Critical | 9.3 | Unrestricted Upload of File with Dangerous Type in the /WebAgenda/download/uploadFile.jsp API endpoint of Flowring Agen… |
| 2026-09-29 09:17:11 | [CVE-2026-96440](https://nvd.nist.gov/vuln/detail/CVE-2026-96440) | High | 7.1 | Improper Limitation of a Pathname to a Restricted Directory（Path Traversal） in the /WebAgenda/download/uploadFile.jsp A… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
