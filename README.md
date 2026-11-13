# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-13 01:19 UTC

New CVEs published between 2026-11-13 00:18 UTC and 2026-11-13 01:19 UTC.

[Full CSV](data/new-cves-2026-11-13T01-19-56-987068Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-13 00:20:09 | [CVE-2026-120868](https://nvd.nist.gov/vuln/detail/CVE-2026-120868) | Critical | 9.3 | Memory overflow in Packet Processing can lead to unpredictable or erroneous behavior or Denial of Service in NetScaler… |
| 2026-11-13 00:20:10 | [CVE-2026-126355](https://nvd.nist.gov/vuln/detail/CVE-2026-126355) | Medium | 5.3 | Hono is a Web application framework that provides support for any JavaScript runtime. Prior to 4.13.16, csrf() limits o… |
| 2026-11-13 00:20:10 | [CVE-2026-126356](https://nvd.nist.gov/vuln/detail/CVE-2026-126356) | Medium | 5.3 | Hono is a Web application framework that provides support for any JavaScript runtime. From 4.5.1 until 4.13.16, validat… |
| 2026-11-13 00:20:10 | [CVE-2026-126357](https://nvd.nist.gov/vuln/detail/CVE-2026-126357) | Medium | 5.3 | Hono is a Web application framework that provides support for any JavaScript runtime. Prior to 4.13.16, mount() and app… |
| 2026-11-13 00:20:11 | [CVE-2026-126358](https://nvd.nist.gov/vuln/detail/CVE-2026-126358) | Medium | 5.3 | Hono is a Web application framework that provides support for any JavaScript runtime. From 4.1.4 until 4.13.16, RegExpR… |
| 2026-11-13 00:20:11 | [CVE-2026-126359](https://nvd.nist.gov/vuln/detail/CVE-2026-126359) | Low | 3.4 | Hono is a Web application framework that provides support for any JavaScript runtime. From 3.12.0 until 4.13.16, the cs… |
| 2026-11-13 00:20:11 | [CVE-2026-126360](https://nvd.nist.gov/vuln/detail/CVE-2026-126360) | Medium | 5.3 | OpenTelemetry Python provides the Python API and SDK for OpenTelemetry. Prior to 1.45.2, TraceContextTextMapPropagator.… |
| 2026-11-13 00:20:11 | [CVE-2026-126361](https://nvd.nist.gov/vuln/detail/CVE-2026-126361) | Low | 2.3 | Astro is a web framework for content-driven websites. Prior to 7.4.5, Astro rendered a string used as a dynamic element… |
| 2026-11-13 00:20:11 | [CVE-2026-126362](https://nvd.nist.gov/vuln/detail/CVE-2026-126362) | Low | 2.3 | Astro is a web framework for content-driven websites. From 5.7.3 until 9.1.2, the @astrojs/svelte renderer inserted a n… |
| 2026-11-13 00:20:11 | [CVE-2026-126363](https://nvd.nist.gov/vuln/detail/CVE-2026-126363) | Low | 2.3 | Astro is a web framework for content-driven websites. From 0.2.0 until 7.1.2, the @astrojs/solid-js renderer inserted a… |
| 2026-11-13 00:20:12 | [CVE-2026-126364](https://nvd.nist.gov/vuln/detail/CVE-2026-126364) | Medium | 6.3 | Astro is a web framework for content-driven websites. From 5.14.3 until 7.4.7, Astro's /_image endpoint compared the re… |
| 2026-11-13 00:20:12 | [CVE-2026-126365](https://nvd.nist.gov/vuln/detail/CVE-2026-126365) | Medium | 5.4 | Astro is a web framework for content-driven websites. Prior to @astrojs/prism 4.1.2, and from @astrojs/markdoc 0.3.0 un… |
| 2026-11-13 00:20:12 | [CVE-2026-126366](https://nvd.nist.gov/vuln/detail/CVE-2026-126366) | High | 7.5 | MessagePack for Ruby is an implementation of the MessagePack binary serialization format. Prior to 1.8.7, the Java-plat… |
| 2026-11-13 00:20:12 | [CVE-2026-126367](https://nvd.nist.gov/vuln/detail/CVE-2026-126367) | Medium | 4.8 | @grpc/grpc-js implements the core functionality of gRPC purely in JavaScript, without a C++ addon. Before 1.13.2, and f… |
| 2026-11-13 00:20:12 | [CVE-2026-126792](https://nvd.nist.gov/vuln/detail/CVE-2026-126792) | Medium | 5.7 | A memory-safety flaw in the key-management request-building component of the library can lead to an out-of-bounds write… |
| 2026-11-13 00:20:13 | [CVE-2026-126839](https://nvd.nist.gov/vuln/detail/CVE-2026-126839) | Low | 2.3 | A deserialization type-restriction control in the BSON serialization component can be bypassed because the check used t… |
| 2026-11-13 00:20:13 | [CVE-2026-126982](https://nvd.nist.gov/vuln/detail/CVE-2026-126982) | High | 7.7 | A type allow-list bypass in the BSON serialization library of the MongoDB C# Driver allows a type-restriction check to… |
| 2026-11-13 00:20:13 | [CVE-2026-127212](https://nvd.nist.gov/vuln/detail/CVE-2026-127212) | Medium | 5.3 | Dokploy before 0.31.1 contains a missing ownership check vulnerability in the readAppMonitoring tRPC procedure that all… |
| 2026-11-13 00:20:13 | [CVE-2026-127273](https://nvd.nist.gov/vuln/detail/CVE-2026-127273) | Low | 2.1 | A vulnerability has been found in Linksys EA8100 1.0.3.216940. This affects the function GetWANStatus/GetWANStatus3/IsA… |
| 2026-11-13 00:20:13 | [CVE-2026-127274](https://nvd.nist.gov/vuln/detail/CVE-2026-127274) | Low | 2.9 | A vulnerability was found in Linksys EA8100 1.0.3.216940. This vulnerability affects unknown code of the file /jnap/cor… |
| 2026-11-13 00:20:14 | [CVE-2026-127275](https://nvd.nist.gov/vuln/detail/CVE-2026-127275) | Critical | 9.3 | A vulnerability was determined in Linksys EA8100 1.0.3.216940. This issue affects the function SetRemoteSetting/SetUnse… |
| 2026-11-13 00:20:14 | [CVE-2026-128065](https://nvd.nist.gov/vuln/detail/CVE-2026-128065) | Medium | 6.9 | @grpc/grpc-js implements the core functionality of gRPC purely in JavaScript, without a C++ addon. From 1.14.0 through… |
| 2026-11-13 00:20:14 | [CVE-2026-128066](https://nvd.nist.gov/vuln/detail/CVE-2026-128066) | High | 8.7 | Pillow is a Python imaging library. From 1.0 through 12.3.0, ImageFileDirectory_v2.load() in src/PIL/TiffImagePlugin.py… |
| 2026-11-13 00:20:14 | [CVE-2026-128067](https://nvd.nist.gov/vuln/detail/CVE-2026-128067) | High | 8.4 | Pillow is a Python imaging library. From 2.3.0 through 12.3.0, Pillow applications that save compressed TIFF images thr… |
| 2026-11-13 00:20:18 | [CVE-2026-92735](https://nvd.nist.gov/vuln/detail/CVE-2026-92735) | Medium | 5.9 | HashiCorp Vault and Vault Enterprise are vulnerable to an issue in the integrated storage join process that may allow a… |
| 2026-11-13 00:20:18 | [CVE-2026-93333](https://nvd.nist.gov/vuln/detail/CVE-2026-93333) | Low | 2.7 | Vault's audit devices did not validate the contents of a configured audit log prefix and did not consistently enforce t… |
| 2026-11-13 00:20:19 | [CVE-2026-93335](https://nvd.nist.gov/vuln/detail/CVE-2026-93335) | Medium | 6.5 | Vault Community Edition and Vault Enterprise did not consistently apply explicit ACL policy deny rules to request paths… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
