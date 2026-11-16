# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 17:18 UTC

New CVEs published between 2026-11-16 16:18 UTC and 2026-11-16 17:18 UTC.

[Full CSV](data/new-cves-2026-11-16T17-18-31-934538Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 17:17:26 | [CVE-2026-100101](https://nvd.nist.gov/vuln/detail/CVE-2026-100101) | High | 8.4 | On Linux and other Unix-like systems, LibreOffice can send the current document as an email attachment with File > Send… |
| 2026-11-16 17:17:26 | [CVE-2026-101351](https://nvd.nist.gov/vuln/detail/CVE-2026-101351) | Low | 1.9 | LibreOffice can import PICT images, which may be embedded in documents. Parts of a crafted image could be left unwritte… |
| 2026-11-16 17:17:26 | [CVE-2026-101352](https://nvd.nist.gov/vuln/detail/CVE-2026-101352) | High | 8.5 | A document can carry its own user interface customizations, such as keyboard shortcuts, menus and toolbars, which take… |
| 2026-11-16 17:17:26 | [CVE-2026-101353](https://nvd.nist.gov/vuln/detail/CVE-2026-101353) | Medium | 6.8 | LibreOffice Base documents can contain an embedded HSQLDB database, and other documents can use such a database as a da… |
| 2026-11-16 17:17:26 | [CVE-2026-101892](https://nvd.nist.gov/vuln/detail/CVE-2026-101892) | High | 8.5 | LibreOffice documents in ODF format can contain form controls, such as buttons and text fields, and each control names… |
| 2026-11-16 17:17:27 | [CVE-2026-101929](https://nvd.nist.gov/vuln/detail/CVE-2026-101929) | Medium | 5.4 | LibreOffice documents can contain Basic macro libraries. A library protected by a password is stored in the document in… |
| 2026-11-16 17:17:27 | [CVE-2026-101930](https://nvd.nist.gov/vuln/detail/CVE-2026-101930) | High | 8.5 | LibreOffice Writer can open HTML documents, and an HTML document can bind macros to events of the document as a whole,… |
| 2026-11-16 17:17:27 | [CVE-2026-101933](https://nvd.nist.gov/vuln/detail/CVE-2026-101933) | Medium | 5.4 | LibreOffice documents can contain Basic macro libraries. A library protected by a password is stored in the document in… |
| 2026-11-16 17:17:27 | [CVE-2026-104007](https://nvd.nist.gov/vuln/detail/CVE-2026-104007) | High | 8.5 | LibreOffice can connect to databases through JDBC drivers written in Java. A spreadsheet can use a database as the sour… |
| 2026-11-16 17:17:27 | [CVE-2026-104692](https://nvd.nist.gov/vuln/detail/CVE-2026-104692) | High | 8.5 | LibreOffice bundles the HSQLDB database engine, which can be used through the generic JDBC database driver as well as t… |
| 2026-11-16 17:17:27 | [CVE-2026-104920](https://nvd.nist.gov/vuln/detail/CVE-2026-104920) | High | 8.5 | LibreOffice Calc can link a cell range to an external data source, and the link is saved in the document. A Java databa… |
| 2026-11-16 17:17:27 | [CVE-2026-104933](https://nvd.nist.gov/vuln/detail/CVE-2026-104933) | Medium | 6.7 | LibreOffice can embed audio and video in documents. Where it plays media with GStreamer, as on Linux, the media is open… |
| 2026-11-16 17:17:27 | [CVE-2026-106535](https://nvd.nist.gov/vuln/detail/CVE-2026-106535) | Medium | 5.4 | libvisio is a library that reads drawings in the VSD and VSDX formats. LibreOffice and other applications use it to imp… |
| 2026-11-16 17:17:28 | [CVE-2026-108169](https://nvd.nist.gov/vuln/detail/CVE-2026-108169) | High | 7.3 | LibreOffice can open a web query file (.iqy), which names a web page to import into a spreadsheet, when the file is giv… |
| 2026-11-16 17:17:29 | [CVE-2026-113630](https://nvd.nist.gov/vuln/detail/CVE-2026-113630) | High | 7.8 | Command injection in the documentserver-flush-cache.sh maintenance helper in ONLYOFFICE Docs (Document Server) 9.4.0-12… |
| 2026-11-16 17:17:29 | [CVE-2026-113631](https://nvd.nist.gov/vuln/detail/CVE-2026-113631) | Medium | 6.5 | Incorrect authorization in the sendForm RPC handler and Session JWT reconnect handling in ONLYOFFICE Docs (Document Ser… |
| 2026-11-16 17:17:31 | [CVE-2026-129235](https://nvd.nist.gov/vuln/detail/CVE-2026-129235) | Medium | 5.3 | Kubeshark is an eBPF-powered network observability tool for Kubernetes. From 53.1.0 until 53.4.0, the download_file too… |
| 2026-11-16 17:17:31 | [CVE-2026-129236](https://nvd.nist.gov/vuln/detail/CVE-2026-129236) | High | 7.2 | Kubeshark is an eBPF-powered network observability tool for Kubernetes. From 53.1.0 until 53.4.0, the start_kubeshark M… |
| 2026-11-16 17:17:31 | [CVE-2026-129237](https://nvd.nist.gov/vuln/detail/CVE-2026-129237) | Medium | 5.4 | qbee-agent is the device agent component of the qbee.io IoT device management platform. Prior to 2026.41, the unpackTar… |
| 2026-11-16 17:17:31 | [CVE-2026-129239](https://nvd.nist.gov/vuln/detail/CVE-2026-129239) | Medium | 6.5 | Directus is a real-time API and App dashboard for managing SQL database content. Prior to 12.3.1, Directus allows an au… |
| 2026-11-16 17:17:33 | [CVE-2026-18563](https://nvd.nist.gov/vuln/detail/CVE-2026-18563) | Medium | 5.4 | LibreOffice supports fonts embedded in documents. When a document is exported to PDF, the fonts it uses are embedded in… |
| 2026-11-16 17:17:33 | [CVE-2026-18564](https://nvd.nist.gov/vuln/detail/CVE-2026-18564) | Medium | 6.9 | LibreOffice can export documents to PDF protected by a password. With the PDF 2.0 option the file is encrypted with 256… |
| 2026-11-16 17:17:33 | [CVE-2026-18565](https://nvd.nist.gov/vuln/detail/CVE-2026-18565) | Low | 1.1 | LibreOffice has an option, called stealth mode in earlier advisories, that stops documents from outside the trusted fil… |
| 2026-11-16 17:17:33 | [CVE-2026-18566](https://nvd.nist.gov/vuln/detail/CVE-2026-18566) | Medium | 5.4 | LibreOffice can import EMF, EMF+ and WMF images, which may be embedded in documents. Several out-of-bounds reads existe… |
| 2026-11-16 17:17:34 | [CVE-2026-64890](https://nvd.nist.gov/vuln/detail/CVE-2026-64890) | Medium | 5.5 | : Cleartext Storage of Sensitive Information vulnerability in Johnson Controls Open Blue Companion Android App on Andro… |
| 2026-11-16 17:17:35 | [CVE-2026-84234](https://nvd.nist.gov/vuln/detail/CVE-2026-84234) | Medium | 5.4 | LibreOffice can open PDF files in Draw, where the PDF import converts each page into drawing objects that can be edited… |
| 2026-11-16 17:17:35 | [CVE-2026-84443](https://nvd.nist.gov/vuln/detail/CVE-2026-84443) | High | 8.5 | LibreOffice Base documents can bind macros to document events, such as opening or closing the document. The macro secur… |
| 2026-11-16 17:17:35 | [CVE-2026-86046](https://nvd.nist.gov/vuln/detail/CVE-2026-86046) | High | 7.1 | termux-sync is an open source tool for backing up and restoring a Termux environment across devices. Prior to 1.2.4, te… |
| 2026-11-16 17:17:36 | [CVE-2026-87932](https://nvd.nist.gov/vuln/detail/CVE-2026-87932) | Medium | 6.8 | LibreOffice Writer can save documents in DOCX format. A document can contain content controls whose values are bound to… |
| 2026-11-16 17:17:36 | [CVE-2026-88987](https://nvd.nist.gov/vuln/detail/CVE-2026-88987) | Medium | 5.4 | Silverstripe Framework is a PHP framework which powers the Silverstripe CMS. Prior to 6.2.13, the HTML sanitiser does n… |
| 2026-11-16 17:17:36 | [CVE-2026-88988](https://nvd.nist.gov/vuln/detail/CVE-2026-88988) | Medium | 5.4 | Silverstripe Framework is a PHP framework which powers the Silverstripe CMS. Prior to 6.2.13, the HTML sanitiser does n… |
| 2026-11-16 17:17:36 | [CVE-2026-88989](https://nvd.nist.gov/vuln/detail/CVE-2026-88989) | Medium | 4.3 | Silverstripe Framework is a PHP framework which powers the Silverstripe CMS. Prior to 6.2.13, a CMS user who can edit r… |
| 2026-11-16 17:17:36 | [CVE-2026-91110](https://nvd.nist.gov/vuln/detail/CVE-2026-91110) | Medium | 6.4 | Silverstripe Framework is a PHP framework which powers the Silverstripe CMS. Prior to 6.2.13, the HTML sanitiser does n… |
| 2026-11-16 17:17:36 | [CVE-2026-91112](https://nvd.nist.gov/vuln/detail/CVE-2026-91112) | Medium | 6.8 | Silverstripe Framework is a PHP framework which powers the Silverstripe CMS. Prior to 6.2.13, a user with CMS_ACCESS_Se… |
| 2026-11-16 17:17:36 | [CVE-2026-91113](https://nvd.nist.gov/vuln/detail/CVE-2026-91113) | Medium | 4.3 | Silverstripe Framework is a PHP framework which powers the Silverstripe CMS. Prior to 6.2.13, a CMS user who can edit a… |
| 2026-11-16 17:17:37 | [CVE-2026-91114](https://nvd.nist.gov/vuln/detail/CVE-2026-91114) | Medium | 4.4 | Silverstripe Framework is a PHP framework which powers the Silverstripe CMS. Prior to 6.2.13, PermissionCheckboxSetFiel… |
| 2026-11-16 17:17:37 | [CVE-2026-91115](https://nvd.nist.gov/vuln/detail/CVE-2026-91115) | High | 8.8 | Silverstripe Framework is a PHP framework which powers the Silverstripe CMS. From 6.0.0 until 6.2.13, the writer option… |
| 2026-11-16 17:17:54 | [CVE-2026-97892](https://nvd.nist.gov/vuln/detail/CVE-2026-97892) | Medium | 5.4 | LibreOffice checks the digital signatures of a PDF document when the document is opened, and shows whether each signatu… |
| 2026-11-16 17:17:55 | [CVE-2026-97894](https://nvd.nist.gov/vuln/detail/CVE-2026-97894) | Medium | 5.4 | LibreOffice Calc can open spreadsheets in the DIF format, and text files such as CSV in the UTF-16 encoding. Both are r… |
| 2026-11-16 17:17:55 | [CVE-2026-97999](https://nvd.nist.gov/vuln/detail/CVE-2026-97999) | Medium | 5.4 | LibreOffice Base documents can hold an embedded HSQLDB database. When the experimental features option is enabled, Libr… |
| 2026-11-16 17:17:55 | [CVE-2026-98100](https://nvd.nist.gov/vuln/detail/CVE-2026-98100) | Medium | 5.4 | LibreOffice can import documents in the HWP format, including pictures that link to an external file. An out-of-bounds… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
