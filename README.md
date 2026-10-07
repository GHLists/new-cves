# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-07 03:18 UTC

New CVEs published between 2026-10-07 02:18 UTC and 2026-10-07 03:18 UTC.

[Full CSV](data/new-cves-2026-10-07T03-18-40-286059Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-07 03:16:57 | [CVE-2026-106061](https://nvd.nist.gov/vuln/detail/CVE-2026-106061) | Medium | 5.5 | A flaw was found in GIMP’s X cursor (XMC) thumbnail loader. When GIMP generates a thumbnail for a crafted XMC file, it… |
| 2026-10-07 03:16:58 | [CVE-2026-14911](https://nvd.nist.gov/vuln/detail/CVE-2026-14911) | Critical | 9.3 | Improper Neutralization of Input During Web Page Generation (“Cross-site Scripting”) in ASUS router modules allows a re… |
| 2026-10-07 03:16:58 | [CVE-2026-16516](https://nvd.nist.gov/vuln/detail/CVE-2026-16516) | Critical | 9.0 | wolfSSH does not validate that the ECDSA curve identifier in a KEXDH_REPLY host key blob matches the algorithm negotiat… |
| 2026-10-07 03:16:59 | [CVE-2026-81535](https://nvd.nist.gov/vuln/detail/CVE-2026-81535) | Medium | 6.3 | In wolfSSH through 1.5.0 built with --enable-fwd, DoChannelOpen() in src/internal.c gates only direct-tcpip channel ope… |
| 2026-10-07 03:16:59 | [CVE-2026-83540](https://nvd.nist.gov/vuln/detail/CVE-2026-83540) | High | 7.7 | When password or public key authentication is used with the Windows port of wolfSSHd, the Windows logon token acquired… |
| 2026-10-07 03:16:59 | [CVE-2026-83742](https://nvd.nist.gov/vuln/detail/CVE-2026-83742) | Medium | 5.3 | Unsigned integer underflow in wstrncat() in src/port.c in wolfSSL wolfSSH from v1.4.11 through v1.5.0 on non-Windows pl… |
| 2026-10-07 03:17:00 | [CVE-2026-84897](https://nvd.nist.gov/vuln/detail/CVE-2026-84897) | Medium | 6.9 | src/internal.c in wolfSSL wolfSSH through 1.5.0 admits the server-to-client Diffie-Hellman group exchange messages SSH_… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
