# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-21 22:19 UTC

New CVEs published between 2026-10-21 21:20 UTC and 2026-10-21 22:19 UTC.

[Full CSV](data/new-cves-2026-10-21T22-19-14-217268Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-21 21:20:31 | [CVE-2026-96636](https://nvd.nist.gov/vuln/detail/CVE-2026-96636) | Medium | 6.5 | Pillow is a Python imaging library. Prior to 13.0.0, MpoImageFile.seek() and DcxImageFile.seek() reparse later MPO or D… |
| 2026-10-21 21:20:31 | [CVE-2026-96637](https://nvd.nist.gov/vuln/detail/CVE-2026-96637) | High | 7.1 | Pillow is a Python imaging library. Prior to 13.0.0, SpiderImageFile.seek() in src/PIL/SpiderImagePlugin.py reparses a… |
| 2026-10-21 21:20:32 | [CVE-2026-96638](https://nvd.nist.gov/vuln/detail/CVE-2026-96638) | Medium | 6.5 | Pillow is a Python imaging library. From 9.1.0 until 13.0.0, BmpRleDecoder.decode() in src/PIL/BmpImagePlugin.py permit… |
| 2026-10-21 21:20:32 | [CVE-2026-96639](https://nvd.nist.gov/vuln/detail/CVE-2026-96639) | Critical | 9.8 | Pillow is a Python imaging library. From 11.0.0 until 13.0.0, multi-frame loaders can retain an ImagingCore allocation… |
| 2026-10-21 21:20:32 | [CVE-2026-96640](https://nvd.nist.gov/vuln/detail/CVE-2026-96640) | High | 8.2 | Pillow is a Python imaging library. From 5.1.0 until 13.0.0, PdfParser.linearize_page_tree() in src/PIL/PdfParser.py tr… |
| 2026-10-21 21:20:32 | [CVE-2026-96641](https://nvd.nist.gov/vuln/detail/CVE-2026-96641) | Medium | 6.5 | Pillow is a Python imaging library. Prior to 13.0.0, PILfont text-width accumulation in src/_imaging.c checks positive… |
| 2026-10-21 21:20:32 | [CVE-2026-96642](https://nvd.nist.gov/vuln/detail/CVE-2026-96642) | High | 7.1 | Pillow is a Python imaging library. Prior to 13.0.0, the TarIO initializer in src/PIL/TarIO.py accepts a negative octal… |
| 2026-10-21 21:20:32 | [CVE-2026-96643](https://nvd.nist.gov/vuln/detail/CVE-2026-96643) | High | 7.1 | Pillow is a Python imaging library. From 11.0.0 until 13.0.0, Exif.load() in src/PIL/Image.py repeatedly slices the rem… |
| 2026-10-21 21:20:32 | [CVE-2026-96644](https://nvd.nist.gov/vuln/detail/CVE-2026-96644) | High | 7.1 | Pillow is a Python imaging library. Prior to 13.0.0 on Windows, src/PIL/WmfImagePlugin.py passes unchecked 32-bit WMF o… |
| 2026-10-21 21:20:33 | [CVE-2026-96778](https://nvd.nist.gov/vuln/detail/CVE-2026-96778) | High | 7.7 | Pillow is a Python imaging library. From 9.4.0 until 13.0.0, ImagingJpegEncode() in src/libImaging/JpegEncode.c can cal… |
| 2026-10-21 22:16:48 | [CVE-2026-112921](https://nvd.nist.gov/vuln/detail/CVE-2026-112921) |  |  | Robots::Validate versions from 0.4.3 before 0.4.10 for Perl report clients as imposter robots when User-Agent matcher s… |
| 2026-10-21 22:16:48 | [CVE-2026-114381](https://nvd.nist.gov/vuln/detail/CVE-2026-114381) | Low | 2.1 | A vulnerability was determined in itsourcecode Online Cake Ordering System 1.0. The affected element is an unknown func… |
| 2026-10-21 22:16:48 | [CVE-2026-114382](https://nvd.nist.gov/vuln/detail/CVE-2026-114382) | Critical | 9.3 | A security flaw has been discovered in TOTOLINK EX200 5.2.3c.7200. This affects the function setStaticDhcpConfig of the… |
| 2026-10-21 22:16:49 | [CVE-2026-114383](https://nvd.nist.gov/vuln/detail/CVE-2026-114383) | Critical | 9.3 | A weakness has been identified in TOTOLINK EX200 5.2.3c.7200. This impacts the function setWiFiAclAddConfig of the file… |
| 2026-10-21 22:16:49 | [CVE-2026-114384](https://nvd.nist.gov/vuln/detail/CVE-2026-114384) | Low | 2.1 | A security vulnerability has been detected in itsourcecode Online Cake Ordering System 1.0. Affected is an unknown func… |
| 2026-10-21 22:16:49 | [CVE-2026-114501](https://nvd.nist.gov/vuln/detail/CVE-2026-114501) | Medium | 6.3 | Pillow is a Python imaging library. From 11.2.1 until 13.0.0, Arrow export assumes that an image's rows are tightly con… |
| 2026-10-21 22:16:49 | [CVE-2026-114508](https://nvd.nist.gov/vuln/detail/CVE-2026-114508) | Medium | 6.5 | Laravel is a web application framework. From 12.45.0 until 12.68.0 and 13.27.0, crafted relationship inclusion on a rea… |
| 2026-10-21 22:16:49 | [CVE-2026-114509](https://nvd.nist.gov/vuln/detail/CVE-2026-114509) | Critical | 9.2 | Laravel is a web application framework. Prior to 12.68.0 and 13.29.0, TokenGuard configured as a standard token-based A… |
| 2026-10-21 22:16:50 | [CVE-2026-91403](https://nvd.nist.gov/vuln/detail/CVE-2026-91403) | Critical | 9.1 | Vulnerability in the Oracle Java SE, Oracle GraalVM for JDK, Oracle GraalVM Enterprise Edition product of Oracle Java S… |
| 2026-10-21 22:16:50 | [CVE-2026-94140](https://nvd.nist.gov/vuln/detail/CVE-2026-94140) |  |  | Rex versions through 1.16.1 for Perl accept an unknown SSH host key for remote rsync transfers because sync hardcodes S… |
| 2026-10-21 22:16:50 | [CVE-2026-94423](https://nvd.nist.gov/vuln/detail/CVE-2026-94423) |  |  | Net::LibSSH versions before 0.004 for Perl authenticate to an unverified server because connect never checks the host k… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
