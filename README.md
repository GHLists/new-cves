# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-05 22:21 UTC

New CVEs published between 2026-11-05 21:19 UTC and 2026-11-05 22:21 UTC.

[Full CSV](data/new-cves-2026-11-05T22-21-19-183276Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-05 22:17:41 | [CVE-2026-100395](https://nvd.nist.gov/vuln/detail/CVE-2026-100395) | Medium | 6.8 | LXC is a userspace interface for the Linux kernel containment features used to create and manage system containers. In… |
| 2026-11-05 22:17:43 | [CVE-2026-111489](https://nvd.nist.gov/vuln/detail/CVE-2026-111489) | Critical | 9.9 | A static credential embedded in the mobile app has been reported to return the 'autorizado' token on the MatchPoint pla… |
| 2026-11-05 22:17:43 | [CVE-2026-111490](https://nvd.nist.gov/vuln/detail/CVE-2026-111490) | Critical | 9.9 | Insecure direct object reference (IDOR) vulnerability in the MatchPoint API, which relies on the `actingasuser` HTTP he… |
| 2026-11-05 22:17:43 | [CVE-2026-111491](https://nvd.nist.gov/vuln/detail/CVE-2026-111491) | Medium | 6.9 | Credentials are stored in plain text in an SQLite database and in the MatchPoint Android app's SharedPreferences. An at… |
| 2026-11-05 22:17:43 | [CVE-2026-111492](https://nvd.nist.gov/vuln/detail/CVE-2026-111492) | High | 8.6 | SQL injection in the push notification handler of the MatchPoint Android app, which processes messages from Firebase Cl… |
| 2026-11-05 22:17:44 | [CVE-2026-111493](https://nvd.nist.gov/vuln/detail/CVE-2026-111493) | High | 8.7 | Lack of authentication and authorization in the Images.ashx endpoint in MatchPoint, which allows profile photos to be d… |
| 2026-11-05 22:17:44 | [CVE-2026-111494](https://nvd.nist.gov/vuln/detail/CVE-2026-111494) | Critical | 9.1 | Incorrect validation of TLS certificates in the MatchPoint Android app due to a TrustManager that accepts any certifica… |
| 2026-11-05 22:17:44 | [CVE-2026-111495](https://nvd.nist.gov/vuln/detail/CVE-2026-111495) | Medium | 5.1 | API keys, credentials, and configuration parameters embedded in the MatchPoint APK, which can be extracted through reve… |
| 2026-11-05 22:17:45 | [CVE-2026-111768](https://nvd.nist.gov/vuln/detail/CVE-2026-111768) | High | 7.5 | The Model Context Protocol TypeScript SDK provides TypeScript client and server implementations of the Model Context Pr… |
| 2026-11-05 22:17:45 | [CVE-2026-111769](https://nvd.nist.gov/vuln/detail/CVE-2026-111769) | Medium | 6.5 | The Model Context Protocol TypeScript SDK provides TypeScript client and server implementations of the Model Context Pr… |
| 2026-11-05 22:17:45 | [CVE-2026-111770](https://nvd.nist.gov/vuln/detail/CVE-2026-111770) | High | 7.7 | The Model Context Protocol TypeScript SDK provides TypeScript client and server implementations of the Model Context Pr… |
| 2026-11-05 22:17:46 | [CVE-2026-112907](https://nvd.nist.gov/vuln/detail/CVE-2026-112907) | Low | 2.5 | filelock is a platform-independent file lock for Python. From 3.22.0 until 4.2.1, soft lock classes on Windows read an… |
| 2026-11-05 22:17:46 | [CVE-2026-112908](https://nvd.nist.gov/vuln/detail/CVE-2026-112908) | Medium | 5.3 | filelock is a platform-independent file lock for Python. From version 3.30.0 until version 4.2.1, StrictSoftFileLock an… |
| 2026-11-05 22:17:46 | [CVE-2026-112910](https://nvd.nist.gov/vuln/detail/CVE-2026-112910) | Medium | 5.3 | filelock is a platform-independent file lock for Python. From 3.10.0 until 4.2.1, filelock on Windows ignores the mode… |
| 2026-11-05 22:17:47 | [CVE-2026-112913](https://nvd.nist.gov/vuln/detail/CVE-2026-112913) | Low | 3.3 | filelock is a platform-independent file lock for Python. From 3.20.4 until 4.2.1, ReadWriteLock and AsyncReadWriteLock… |
| 2026-11-05 22:17:47 | [CVE-2026-112938](https://nvd.nist.gov/vuln/detail/CVE-2026-112938) | Medium | 5.8 | filelock is a platform-independent file lock for Python. From 3.30.0 until 4.2.1, On POSIX platforms, StrictSoftFileLoc… |
| 2026-11-05 22:17:53 | [CVE-2026-119757](https://nvd.nist.gov/vuln/detail/CVE-2026-119757) | Critical | 9.3 | BTCPay Server before 2.4.2, including 2.4.2 release candidates, contains an information disclosure vulnerability that a… |
| 2026-11-05 22:17:55 | [CVE-2026-122267](https://nvd.nist.gov/vuln/detail/CVE-2026-122267) | High | 8.8 | MinIO Signature V4 verification before RELEASE.2026-09-22T19-25-18Z accepts unsigned x-amz-* headers, letting a presign… |
| 2026-11-05 22:18:41 | [CVE-2026-33944](https://nvd.nist.gov/vuln/detail/CVE-2026-33944) | High | 8.8 | Dolibarr is an open-source enterprise resource planning and customer relationship management application. Prior to 22.0… |
| 2026-11-05 22:18:49 | [CVE-2026-58273](https://nvd.nist.gov/vuln/detail/CVE-2026-58273) | High | 8.1 | Rucio is a scientific data management framework. From 1.16.1 until 35.9.0, 38.6.0, and 41.0.0rc1, the /credentials/sign… |
| 2026-11-05 22:18:54 | [CVE-2026-88983](https://nvd.nist.gov/vuln/detail/CVE-2026-88983) | Medium | 5.0 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.17.0, th… |
| 2026-11-05 22:18:54 | [CVE-2026-88985](https://nvd.nist.gov/vuln/detail/CVE-2026-88985) | Medium | 6.5 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.17.0, th… |
| 2026-11-05 22:18:54 | [CVE-2026-88986](https://nvd.nist.gov/vuln/detail/CVE-2026-88986) | Medium | 6.1 | Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows. Prior to 2.15.0, th… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
