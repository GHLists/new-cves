# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-25 23:19 UTC

New CVEs published between 2026-11-25 22:20 UTC and 2026-11-25 23:19 UTC.

[Full CSV](data/new-cves-2026-11-25T23-19-42-839614Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-25 23:17:19 | [CVE-2018-25445](https://nvd.nist.gov/vuln/detail/CVE-2018-25445) |  |  | Crypt::JWT versions before 0.024 for Perl skip issuer, subject, audience and JWT ID checks when the claim is absent or… |
| 2026-11-25 23:17:20 | [CVE-2022-50995](https://nvd.nist.gov/vuln/detail/CVE-2022-50995) |  |  | WWW::Form::UrlEncoded::XS versions before 0.27 for Perl read one byte before the input buffer when parsing an empty str… |
| 2026-11-25 23:17:21 | [CVE-2022-50996](https://nvd.nist.gov/vuln/detail/CVE-2022-50996) |  |  | WWW::Form::UrlEncoded::XS versions before 0.28 for Perl write past the end of the Perl argument stack when parse_urlenc… |
| 2026-11-25 23:17:21 | [CVE-2026-102987](https://nvd.nist.gov/vuln/detail/CVE-2026-102987) | Medium | 6.3 | Plane is an open-source project management tool. In versions prior to 1.4.0, the v2 asset static endpoint allows unauth… |
| 2026-11-25 23:17:21 | [CVE-2026-104943](https://nvd.nist.gov/vuln/detail/CVE-2026-104943) |  |  | Rejected reason: This CVE ID has been rejected or withdrawn by its CVE Numbering Authority. |
| 2026-11-25 23:17:21 | [CVE-2026-133971](https://nvd.nist.gov/vuln/detail/CVE-2026-133971) | Critical | 9.8 | An authentication bypass vulnerability exists in the web management interface of HPE Networking Management Software (Ai… |
| 2026-11-25 23:17:21 | [CVE-2026-133972](https://nvd.nist.gov/vuln/detail/CVE-2026-133972) | Critical | 9.8 | A vulnerability in system functionality could allow an attacker with network access to bypass authentication. Successfu… |
| 2026-11-25 23:17:21 | [CVE-2026-133973](https://nvd.nist.gov/vuln/detail/CVE-2026-133973) | Critical | 9.8 | A command injection vulnerability exists in the web-based management interface of HPE Networking Management Software (A… |
| 2026-11-25 23:17:21 | [CVE-2026-133974](https://nvd.nist.gov/vuln/detail/CVE-2026-133974) | High | 8.8 | A vulnerability in a system functionality could allow a low-privilege authenticated attacker with network access to pot… |
| 2026-11-25 23:17:22 | [CVE-2026-133975](https://nvd.nist.gov/vuln/detail/CVE-2026-133975) | High | 8.8 | Authenticated SQL injection vulnerabilities in the web-based management interface and API of HPE Networking Management… |
| 2026-11-25 23:17:22 | [CVE-2026-133976](https://nvd.nist.gov/vuln/detail/CVE-2026-133976) | High | 8.8 | A missing integrity verification vulnerability exists in HPE Networking Management Software (Airwave). Successful explo… |
| 2026-11-25 23:17:22 | [CVE-2026-133977](https://nvd.nist.gov/vuln/detail/CVE-2026-133977) | High | 7.5 | A sensitive information disclosure vulnerability exists in the affected interface of HPE Networking Management Software… |
| 2026-11-25 23:17:22 | [CVE-2026-133978](https://nvd.nist.gov/vuln/detail/CVE-2026-133978) | High | 7.5 | A command injection vulnerability exists in the web-based management interface of HPE Networking Management Software (A… |
| 2026-11-25 23:17:22 | [CVE-2026-133979](https://nvd.nist.gov/vuln/detail/CVE-2026-133979) | High | 7.4 | Improper certificate validation vulnerabilities in the web-based management interface of HPE Networking Management Soft… |
| 2026-11-25 23:17:22 | [CVE-2026-133980](https://nvd.nist.gov/vuln/detail/CVE-2026-133980) | Medium | 6.5 | Path traversal vulnerabilities exist in the web-based management interface and API of HPE Networking Management Softwar… |
| 2026-11-25 23:17:22 | [CVE-2026-135092](https://nvd.nist.gov/vuln/detail/CVE-2026-135092) |  |  | PDF::API2 versions before 2.049 for Perl allow unbounded recursion via circular cross-reference chains in readxrtr. Whe… |
| 2026-11-25 23:17:22 | [CVE-2026-136499](https://nvd.nist.gov/vuln/detail/CVE-2026-136499) | Medium | 5.9 | psqlODBC read memory it had not written, or memory past the end of an application buffer, and sent it to the server or… |
| 2026-11-25 23:17:22 | [CVE-2026-136500](https://nvd.nist.gov/vuln/detail/CVE-2026-136500) | High | 8.1 | To escape a bound parameter, or a name passed to a catalog function, psqlODBC has to know where each multibyte characte… |
| 2026-11-25 23:17:23 | [CVE-2026-136501](https://nvd.nist.gov/vuln/detail/CVE-2026-136501) | High | 7.1 | To build positioned updates and to describe columns, psqlODBC matches the names in a statement against the catalog. Whe… |
| 2026-11-25 23:17:23 | [CVE-2026-136502](https://nvd.nist.gov/vuln/detail/CVE-2026-136502) | High | 8.1 | psqlODBC scans statement text itself to substitute parameters, translate ODBC escapes, join batched statements and rewr… |
| 2026-11-25 23:17:23 | [CVE-2026-136503](https://nvd.nist.gov/vuln/detail/CVE-2026-136503) | High | 7.5 | psqlODBC frees memory that is still in use, frees it twice, or writes outside an application buffer in these cases: - T… |
| 2026-11-25 23:17:23 | [CVE-2026-136504](https://nvd.nist.gov/vuln/detail/CVE-2026-136504) | Medium | 5.0 | With the driver's debug log (MyLog) turned on, two paths write the database password to the log in clear text, both bes… |
| 2026-11-25 23:17:23 | [CVE-2026-136505](https://nvd.nist.gov/vuln/detail/CVE-2026-136505) | High | 7.5 | psqlODBC uses sizes and counts without checking their range, or keeps them in types too small for them: - A row array s… |
| 2026-11-25 23:17:23 | [CVE-2026-136506](https://nvd.nist.gov/vuln/detail/CVE-2026-136506) | High | 7.5 | psqlODBC builds queries of its own from names, and put these names into them without escaping or qualification: - the d… |
| 2026-11-25 23:17:23 | [CVE-2026-136507](https://nvd.nist.gov/vuln/detail/CVE-2026-136507) | High | 8.1 | psqlODBC parsed and built connection strings in ways that let a value end early: - In a braced value, such as PWD={…},… |
| 2026-11-25 23:17:23 | [CVE-2026-136508](https://nvd.nist.gov/vuln/detail/CVE-2026-136508) | Medium | 6.8 | On Windows, when a connection takes part in a distributed transaction, psqlODBC and its XA library open further connect… |
| 2026-11-25 23:17:24 | [CVE-2026-136509](https://nvd.nist.gov/vuln/detail/CVE-2026-136509) | High | 7.5 | psqlODBC did not check that a server reply matches the query it sent: that a FETCH returns no more rows than it asked f… |
| 2026-11-25 23:17:24 | [CVE-2026-136510](https://nvd.nist.gov/vuln/detail/CVE-2026-136510) | Medium | 4.8 | A parameter-array execution that fails part-way leaves the rows it has already queued on the statement handle, and the… |
| 2026-11-25 23:17:24 | [CVE-2026-136511](https://nvd.nist.gov/vuln/detail/CVE-2026-136511) | Medium | 6.8 | psqlODBC mapped an SSLmode value in a connection string that it did not recognise, such as SSLmode=Require, SSLmode=Ver… |
| 2026-11-25 23:17:24 | [CVE-2026-136512](https://nvd.nist.gov/vuln/detail/CVE-2026-136512) | High | 7.5 | With SQL_C_DEFAULT, the C type of a bound column or parameter follows its SQL type. An application sizes its buffer fro… |
| 2026-11-25 23:17:24 | [CVE-2026-136513](https://nvd.nist.gov/vuln/detail/CVE-2026-136513) | Low | 3.6 | When Debug or CommLog is enabled and the log directory cannot be used, psqlODBC falls back to a directory under the use… |
| 2026-11-25 23:17:24 | [CVE-2026-136514](https://nvd.nist.gov/vuln/detail/CVE-2026-136514) | Medium | 6.5 | psqlODBC assumed that a table it reads keeps the definition it had when the statement was described or parsed. A databa… |
| 2026-11-25 23:17:24 | [CVE-2026-136515](https://nvd.nist.gov/vuln/detail/CVE-2026-136515) | High | 7.5 | psqlODBC rewrites statement text for keyset-driven cursors and ODBC escapes using positions it found in the text. These… |
| 2026-11-25 23:17:25 | [CVE-2026-136795](https://nvd.nist.gov/vuln/detail/CVE-2026-136795) |  |  | Crypt::JWT versions before 0.037_1 for Perl allow memory exhaustion via unbounded inflation of zip DEF payloads. When a… |
| 2026-11-25 23:17:25 | [CVE-2026-136796](https://nvd.nist.gov/vuln/detail/CVE-2026-136796) |  |  | Crypt::JWT versions before 0.037_1 for Perl allow CPU exhaustion via an unbounded PBES2 iteration count. For a token us… |
| 2026-11-25 23:17:25 | [CVE-2026-136869](https://nvd.nist.gov/vuln/detail/CVE-2026-136869) | Medium | 6.9 | A vulnerability was detected in GL.iNet GL-A1300, GL-AR300M, GL-AR300M16, GL-AX1800, GL-AXT1800, GL-B3000, GL-BE3600, G… |
| 2026-11-25 23:17:25 | [CVE-2026-136870](https://nvd.nist.gov/vuln/detail/CVE-2026-136870) | Medium | 6.9 | A flaw has been found in GL.iNet GL-A1300, GL-AR300M, GL-AR300M16, GL-AX1800, GL-AXT1800, GL-B3000, GL-BE3600, GL-BE650… |
| 2026-11-25 23:17:25 | [CVE-2026-136871](https://nvd.nist.gov/vuln/detail/CVE-2026-136871) | Medium | 6.9 | A vulnerability has been found in GL.iNet GL-A1300, GL-AR300M, GL-AR300M16, GL-AX1800, GL-AXT1800, GL-B3000, GL-BE3600,… |
| 2026-11-25 23:17:26 | [CVE-2026-8748](https://nvd.nist.gov/vuln/detail/CVE-2026-8748) |  |  | Crypt::JWT versions before 0.037_1 for Perl compare HMAC signatures and JWE authentication tags in non-constant time. d… |
| 2026-11-25 23:17:26 | [CVE-2026-95794](https://nvd.nist.gov/vuln/detail/CVE-2026-95794) | Medium | 6.5 | An XML external entity (XXE) vulnerability exists in the web-based management interface of HPE Networking Management So… |
| 2026-11-25 23:17:26 | [CVE-2026-95795](https://nvd.nist.gov/vuln/detail/CVE-2026-95795) | Medium | 6.5 | Missing authorization vulnerabilities exist in the API of HPE Networking Management Software (Airwave). Successful expl… |
| 2026-11-25 23:17:26 | [CVE-2026-95796](https://nvd.nist.gov/vuln/detail/CVE-2026-95796) | Medium | 6.1 | A vulnerability in the web-based management interface of HPE Networking Management Software (Airwave) could allow an un… |
| 2026-11-25 23:17:26 | [CVE-2026-95797](https://nvd.nist.gov/vuln/detail/CVE-2026-95797) | Medium | 4.4 | A weak cryptography vulnerability exists in HPE Networking Management Software (Airwave). Successful exploitation could… |
| 2026-11-25 23:17:27 | [CVE-2026-95798](https://nvd.nist.gov/vuln/detail/CVE-2026-95798) | Low | 3.6 | Missing integrity verification vulnerabilities exist in the command line interface of HPE Networking Management Softwar… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
