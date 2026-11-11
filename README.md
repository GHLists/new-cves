# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-11 06:21 UTC

New CVEs published between 2026-11-11 05:18 UTC and 2026-11-11 06:21 UTC.

[Full CSV](data/new-cves-2026-11-11T06-21-03-08789Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-11 05:19:27 | [CVE-2026-118368](https://nvd.nist.gov/vuln/detail/CVE-2026-118368) | High | 7.0 | Akaunting 3.3.0 contains a stored cross-site scripting vulnerability in the XLSX item-import workflow. An authenticated… |
| 2026-11-11 05:19:49 | [CVE-2026-59191](https://nvd.nist.gov/vuln/detail/CVE-2026-59191) | Medium | 6.9 | TwigView plugin for CakePHP provides wrappers for common View operations and extensions that expose CakePHP functions a… |
| 2026-11-11 05:19:49 | [CVE-2026-59192](https://nvd.nist.gov/vuln/detail/CVE-2026-59192) | Medium | 6.9 | TwigView plugin for CakePHP provides wrappers for common View operations and extensions that expose CakePHP functions a… |
| 2026-11-11 05:19:49 | [CVE-2026-61810](https://nvd.nist.gov/vuln/detail/CVE-2026-61810) | Medium | 6.0 | libspdm is a sample implementation that follows the DMTF SPDM specifications. In version 1.4.0, both the FINISH request… |
| 2026-11-11 05:19:50 | [CVE-2026-64666](https://nvd.nist.gov/vuln/detail/CVE-2026-64666) | High | 7.1 | pam_usb provides hardware authentication for Linux using removable media. Prior to version 0.9.3, src/local.c reads XRD… |
| 2026-11-11 05:19:50 | [CVE-2026-64667](https://nvd.nist.gov/vuln/detail/CVE-2026-64667) | Medium | 4.4 | pam_usb provides hardware authentication for Linux using removable media. Prior to version 0.9.3, src/local.c (pusb_get… |
| 2026-11-11 05:19:51 | [CVE-2026-64668](https://nvd.nist.gov/vuln/detail/CVE-2026-64668) | High | 7.4 | pam_usb provides hardware authentication for Linux using removable media. From version 0.8.0 to before version 0.9.3, t… |
| 2026-11-11 05:19:51 | [CVE-2026-64669](https://nvd.nist.gov/vuln/detail/CVE-2026-64669) | High | 7.4 | pam_usb provides hardware authentication for Linux using removable media. From version 0.8.0 to before version 0.9.3, t… |
| 2026-11-11 05:19:51 | [CVE-2026-64670](https://nvd.nist.gov/vuln/detail/CVE-2026-64670) | Critical | 9.3 | Waline is a comment system with backend support. In versions 3.15.2 and prior, @waline/client renders the comment edito… |
| 2026-11-11 05:19:51 | [CVE-2026-64671](https://nvd.nist.gov/vuln/detail/CVE-2026-64671) | High | 7.2 | Waline is a comment system with backend support. In versions 3.15.2 and prior, the @waline/client UserList widget build… |
| 2026-11-11 05:19:51 | [CVE-2026-64678](https://nvd.nist.gov/vuln/detail/CVE-2026-64678) | Critical | 9.8 | NOsql Object (NO2 a.k.a Nitrite) database is an open source nosql embedded document store. Prior to version 4.4.1, when… |
| 2026-11-11 05:19:52 | [CVE-2026-64682](https://nvd.nist.gov/vuln/detail/CVE-2026-64682) | Critical | 9.8 | AstroBlocks is a block-first CMS for Astro projects. Prior to version 3.4.0, admin session tokens can be forged due to… |
| 2026-11-11 05:19:52 | [CVE-2026-64686](https://nvd.nist.gov/vuln/detail/CVE-2026-64686) | Medium | 5.0 | OpenSearch Dashboards is an open-source data visualization tool designed to work with OpenSearch. From versions 2.14.0… |
| 2026-11-11 05:19:57 | [CVE-2026-97033](https://nvd.nist.gov/vuln/detail/CVE-2026-97033) |  |  | Building a malicious package that uses cgo could cause arbitrary code execution at build time through several compiler… |
| 2026-11-11 05:19:57 | [CVE-2026-97034](https://nvd.nist.gov/vuln/detail/CVE-2026-97034) |  |  | When using GCC, building a malicious package that uses cgo could cause arbitrary command execution at link time via unt… |
| 2026-11-11 05:19:57 | [CVE-2026-97035](https://nvd.nist.gov/vuln/detail/CVE-2026-97035) |  |  | When using Clang or GCC, building a malicious package that uses cgo could cause unexpected code execution at build time… |
| 2026-11-11 05:19:57 | [CVE-2026-97036](https://nvd.nist.gov/vuln/detail/CVE-2026-97036) |  |  | On Darwin, building a malicious package that uses cgo could cause arbitrary code execution when using the Apple linker… |
| 2026-11-11 05:19:57 | [CVE-2026-97037](https://nvd.nist.gov/vuln/detail/CVE-2026-97037) |  |  | Building a malicious package that uses cgo could cause arbitrary code execution at link time by passing linker script f… |
| 2026-11-11 05:19:58 | [CVE-2026-97039](https://nvd.nist.gov/vuln/detail/CVE-2026-97039) |  |  | Building a malicious package that uses "#cgo pkg-config:" directives could load untrusted pkg-config ".pc" files or inj… |
| 2026-11-11 05:19:58 | [CVE-2026-97040](https://nvd.nist.gov/vuln/detail/CVE-2026-97040) |  |  | Building a package containing a crafted ".syso" file could bypass cgo flag validation and inject arbitrary linker flags… |
| 2026-11-11 05:19:58 | [CVE-2026-97041](https://nvd.nist.gov/vuln/detail/CVE-2026-97041) |  |  | Building a malicious package containing "//go:cgo_*" compiler directives could inject arbitrary flags into the external… |
| 2026-11-11 05:19:58 | [CVE-2026-97042](https://nvd.nist.gov/vuln/detail/CVE-2026-97042) |  |  | Building a malicious package that uses "//go:cgo_import_dynamic" or links against a crafted PE object on Windows could… |
| 2026-11-11 05:19:58 | [CVE-2026-97043](https://nvd.nist.gov/vuln/detail/CVE-2026-97043) |  |  | Building a malicious package that uses cgo could bypass "#cgo LDFLAGS" validation and cause unexpected code execution a… |
| 2026-11-11 05:19:58 | [CVE-2026-97054](https://nvd.nist.gov/vuln/detail/CVE-2026-97054) |  |  | For HTTP/1 servers, when MaxBytesReader's limit is exceeded, "Connection: close" header is automatically set without sy… |
| 2026-11-11 05:19:58 | [CVE-2026-97038](https://nvd.nist.gov/vuln/detail/CVE-2026-97038) |  |  | Building a malicious package containing ".syso" files or cgo linker inputs could inject arbitrary linker flags or execu… |
| 2026-11-11 06:17:08 | [CVE-2025-15711](https://nvd.nist.gov/vuln/detail/CVE-2025-15711) |  |  | The Live Composer WordPress plugin before 2.1.24 does not sanitise and escape some of its module settings before output… |
| 2026-11-11 06:17:10 | [CVE-2025-15712](https://nvd.nist.gov/vuln/detail/CVE-2025-15712) |  |  | The Live Composer WordPress plugin before 2.1.24 does not sanitise and escape some of its staff member settings before… |
| 2026-11-11 06:17:10 | [CVE-2025-15713](https://nvd.nist.gov/vuln/detail/CVE-2025-15713) |  |  | The Live Composer WordPress plugin before 2.1.24 does not sanitise and escape some of its page-builder module settings… |
| 2026-11-11 06:17:10 | [CVE-2025-15714](https://nvd.nist.gov/vuln/detail/CVE-2025-15714) |  |  | The Live Composer WordPress plugin before 2.1.24 does not sanitise and escape some of its Button module settings before… |
| 2026-11-11 06:17:10 | [CVE-2026-104718](https://nvd.nist.gov/vuln/detail/CVE-2026-104718) |  |  | The Elementor Website Builder WordPress plugin before 4.3.6 does not validate or escape an element identifier before re… |
| 2026-11-11 06:17:10 | [CVE-2026-106468](https://nvd.nist.gov/vuln/detail/CVE-2026-106468) |  |  | The Code Snippets WordPress plugin before 4.1.0 does not verify network-level capabilities before honouring a network-s… |
| 2026-11-11 06:17:10 | [CVE-2026-109870](https://nvd.nist.gov/vuln/detail/CVE-2026-109870) |  |  | The User Registration & Membership WordPress plugin before 5.3.2 does not verify that a discount coupon applied to a pa… |
| 2026-11-11 06:17:10 | [CVE-2026-109871](https://nvd.nist.gov/vuln/detail/CVE-2026-109871) |  |  | The User Registration & Membership WordPress plugin before 5.3.2 does not verify that a payment has actually been compl… |
| 2026-11-11 06:17:11 | [CVE-2026-109873](https://nvd.nist.gov/vuln/detail/CVE-2026-109873) |  |  | The User Registration & Membership WordPress plugin before 5.3.2 does not enforce its payment-before-login restriction… |
| 2026-11-11 06:17:11 | [CVE-2026-110016](https://nvd.nist.gov/vuln/detail/CVE-2026-110016) |  |  | The Data Tables Generator by Supsystic WordPress plugin before 1.15.8 does not perform any authorization or ownership c… |
| 2026-11-11 06:17:11 | [CVE-2026-110948](https://nvd.nist.gov/vuln/detail/CVE-2026-110948) |  |  | The Download Manager WordPress plugin before 3.3.73, Download Manager WordPress plugin before 7.6.2 does not verify tha… |
| 2026-11-11 06:17:11 | [CVE-2026-110949](https://nvd.nist.gov/vuln/detail/CVE-2026-110949) |  |  | The Download Manager WordPress plugin before 3.3.73, Download Manager WordPress plugin before 7.6.2 does not verify a p… |
| 2026-11-11 06:17:11 | [CVE-2026-111579](https://nvd.nist.gov/vuln/detail/CVE-2026-111579) |  |  | The Forminator Forms WordPress plugin before 1.58.4 does not enforce payment on the server side when a form's configure… |
| 2026-11-11 06:17:11 | [CVE-2026-111597](https://nvd.nist.gov/vuln/detail/CVE-2026-111597) |  |  | The Forminator Forms WordPress plugin before 1.58.4 does not verify that a Stripe Checkout payment has completed before… |
| 2026-11-11 06:17:13 | [CVE-2026-115733](https://nvd.nist.gov/vuln/detail/CVE-2026-115733) |  |  | The Printaura-Woocommerce WordPress plugin through 4.0.2 does not properly restrict access to the WooCommerce REST API,… |
| 2026-11-11 06:17:13 | [CVE-2026-115734](https://nvd.nist.gov/vuln/detail/CVE-2026-115734) |  |  | The Pay with a tweet WordPress plugin through 1.0.5 does not validate a file path before deleting it, nor does it restr… |
| 2026-11-11 06:17:13 | [CVE-2026-115735](https://nvd.nist.gov/vuln/detail/CVE-2026-115735) |  |  | The Somatic Framework WordPress plugin through 1.8.14 does not perform an authorization check or validate a user-suppli… |
| 2026-11-11 06:17:14 | [CVE-2026-116081](https://nvd.nist.gov/vuln/detail/CVE-2026-116081) | Low | 2.3 | Sleipnir Mobile for iPhone / iPad and Sleipnir Mobile for iPhone / iPad Black Edition provided by Fenrir Inc. are vulne… |
| 2026-11-11 06:17:14 | [CVE-2026-117521](https://nvd.nist.gov/vuln/detail/CVE-2026-117521) |  |  | The Dynific Addons for Elementor (formerly Anywhere Elementor) WordPress plugin before 1.3.1 does not escape a user-con… |
| 2026-11-11 06:17:14 | [CVE-2026-117522](https://nvd.nist.gov/vuln/detail/CVE-2026-117522) |  |  | The Dynific Addons for Elementor (formerly Anywhere Elementor) WordPress plugin before 1.3.1 does not escape the post t… |
| 2026-11-11 06:17:14 | [CVE-2026-117523](https://nvd.nist.gov/vuln/detail/CVE-2026-117523) |  |  | The Dynific Addons for Elementor (formerly Anywhere Elementor) WordPress plugin before 1.3.1 does not perform a capabil… |
| 2026-11-11 06:17:14 | [CVE-2026-117524](https://nvd.nist.gov/vuln/detail/CVE-2026-117524) |  |  | The Dynific Addons for Elementor (formerly Anywhere Elementor) WordPress plugin before 1.3.1 does not perform a status… |
| 2026-11-11 06:17:14 | [CVE-2026-118041](https://nvd.nist.gov/vuln/detail/CVE-2026-118041) |  |  | The Contest Gallery WordPress plugin before 34.0.3 does not sanitise the name of files uploaded through its e-commerce… |
| 2026-11-11 06:17:14 | [CVE-2026-118241](https://nvd.nist.gov/vuln/detail/CVE-2026-118241) |  |  | The Smush WordPress plugin before 4.3.6 does not verify that a user is authorised to act on the targeted media attachme… |
| 2026-11-11 06:17:15 | [CVE-2026-118418](https://nvd.nist.gov/vuln/detail/CVE-2026-118418) |  |  | The WP Directory Kit WordPress plugin before 1.6.3 does not restrict which database models and columns its public direc… |
| 2026-11-11 06:17:15 | [CVE-2026-118420](https://nvd.nist.gov/vuln/detail/CVE-2026-118420) |  |  | The WP Directory Kit WordPress plugin before 1.6.3 does not sanitise and escape a parameter before using it in a SQL st… |
| 2026-11-11 06:17:15 | [CVE-2026-118439](https://nvd.nist.gov/vuln/detail/CVE-2026-118439) |  |  | The Limit Login Attempts Security WordPress plugin before 3.4.2 does not validate the destination of a server-side requ… |
| 2026-11-11 06:17:15 | [CVE-2026-119032](https://nvd.nist.gov/vuln/detail/CVE-2026-119032) |  |  | The Schema & Structured Data for WP & AMP WordPress plugin before 1.70 does not check that the importing user may edit… |
| 2026-11-11 06:17:15 | [CVE-2026-119033](https://nvd.nist.gov/vuln/detail/CVE-2026-119033) |  |  | The Schema & Structured Data for WP & AMP WordPress plugin before 1.70 does not verify that a user may edit a post befo… |
| 2026-11-11 06:17:15 | [CVE-2026-119034](https://nvd.nist.gov/vuln/detail/CVE-2026-119034) |  |  | The Schema & Structured Data for WP & AMP WordPress plugin before 1.70 does not verify that a post is publicly viewable… |
| 2026-11-11 06:17:15 | [CVE-2026-119035](https://nvd.nist.gov/vuln/detail/CVE-2026-119035) |  |  | The Schema & Structured Data for WP & AMP WordPress plugin before 1.70 does not safely encode its structured data outpu… |
| 2026-11-11 06:17:16 | [CVE-2026-119303](https://nvd.nist.gov/vuln/detail/CVE-2026-119303) |  |  | The NotificationX WordPress plugin before 3.3.7 does not perform any capability or nonce check on one of its REST route… |
| 2026-11-11 06:17:16 | [CVE-2026-119529](https://nvd.nist.gov/vuln/detail/CVE-2026-119529) |  |  | The Gravity Forms WordPress plugin before 3.2.2 does not properly restrict the file types that unauthenticated users ca… |
| 2026-11-11 06:17:16 | [CVE-2026-119531](https://nvd.nist.gov/vuln/detail/CVE-2026-119531) |  |  | The Live Composer WordPress plugin before 2.1.24 does not escape several attributes of one of its page-builder shortcod… |
| 2026-11-11 06:17:16 | [CVE-2026-121472](https://nvd.nist.gov/vuln/detail/CVE-2026-121472) |  |  | The AutomatorWP WordPress plugin before 6.0.8 does not bind the requests that complete its Zoom and AWeber integration… |
| 2026-11-11 06:17:16 | [CVE-2026-121497](https://nvd.nist.gov/vuln/detail/CVE-2026-121497) |  |  | The AskAny WordPress plugin before 2.2.0 does not validate the extension or content of files attached to chat messages,… |
| 2026-11-11 06:17:16 | [CVE-2026-121862](https://nvd.nist.gov/vuln/detail/CVE-2026-121862) |  |  | The Knowledge Building WordPress plugin before 0.7.3 does not sanitise and escape comments submitted through its reply… |
| 2026-11-11 06:17:16 | [CVE-2026-121863](https://nvd.nist.gov/vuln/detail/CVE-2026-121863) |  |  | The Knowledge Building WordPress plugin before 0.7.3 does not escape several user-supplied values before echoing them b… |
| 2026-11-11 06:17:17 | [CVE-2026-121870](https://nvd.nist.gov/vuln/detail/CVE-2026-121870) |  |  | The Simpler Checkout WordPress plugin before 1.5.4 does not properly restrict who can create orders and checks its auto… |
| 2026-11-11 06:17:17 | [CVE-2026-121873](https://nvd.nist.gov/vuln/detail/CVE-2026-121873) |  |  | The Redirection for Contact Form 7 WordPress plugin before 3.2.16 does not verify ownership of the email address suppli… |
| 2026-11-11 06:17:17 | [CVE-2026-121998](https://nvd.nist.gov/vuln/detail/CVE-2026-121998) |  |  | The iChart WordPress plugin before 2.2.4 does not perform capability or ownership checks in several of its AJAX actions… |
| 2026-11-11 06:17:17 | [CVE-2026-122061](https://nvd.nist.gov/vuln/detail/CVE-2026-122061) |  |  | The Event Tickets and Registration WordPress plugin before 5.30.3.1 does not correctly check whether an event displays… |
| 2026-11-11 06:17:17 | [CVE-2026-122087](https://nvd.nist.gov/vuln/detail/CVE-2026-122087) |  |  | The Event Tickets and Registration WordPress plugin before 5.30.3.1 does not restrict attendee data to events the reque… |
| 2026-11-11 06:17:17 | [CVE-2026-123134](https://nvd.nist.gov/vuln/detail/CVE-2026-123134) |  |  | The Smoove abandoned cart trigger for WooCommerce WordPress plugin before 4.3.6 does not sanitise and escape abandoned-… |
| 2026-11-11 06:17:17 | [CVE-2026-123656](https://nvd.nist.gov/vuln/detail/CVE-2026-123656) |  |  | The ProfilePress WordPress plugin before 4.17.6 does not correctly evaluate some of its content protection rule conditi… |
| 2026-11-11 06:17:17 | [CVE-2026-123657](https://nvd.nist.gov/vuln/detail/CVE-2026-123657) |  |  | The ProfilePress WordPress plugin before 4.17.6 does not reject negative membership plan identifiers before checking wh… |
| 2026-11-11 06:17:18 | [CVE-2026-123661](https://nvd.nist.gov/vuln/detail/CVE-2026-123661) |  |  | The ProfilePress WordPress plugin before 4.17.4 does not check that a membership plan is still active when checkout is… |
| 2026-11-11 06:17:18 | [CVE-2026-123666](https://nvd.nist.gov/vuln/detail/CVE-2026-123666) |  |  | The Photo Engine (Media Organizer & Lightroom) WordPress plugin before 6.6.2 does not check that a user may delete the… |
| 2026-11-11 06:17:18 | [CVE-2026-123667](https://nvd.nist.gov/vuln/detail/CVE-2026-123667) |  |  | The Photo Engine (Media Organizer & Lightroom) WordPress plugin before 6.6.2 does not sanitise and escape keyword names… |
| 2026-11-11 06:17:18 | [CVE-2026-123695](https://nvd.nist.gov/vuln/detail/CVE-2026-123695) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not restrict access to several of its REST API routes… |
| 2026-11-11 06:17:18 | [CVE-2026-123696](https://nvd.nist.gov/vuln/detail/CVE-2026-123696) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not check that the requester is authorised before res… |
| 2026-11-11 06:17:18 | [CVE-2026-123697](https://nvd.nist.gov/vuln/detail/CVE-2026-123697) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not restrict who can request a user's current two-fac… |
| 2026-11-11 06:17:18 | [CVE-2026-123698](https://nvd.nist.gov/vuln/detail/CVE-2026-123698) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not restrict access to one of its REST API routes, al… |
| 2026-11-11 06:17:19 | [CVE-2026-123699](https://nvd.nist.gov/vuln/detail/CVE-2026-123699) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not check that the requester is authorised before run… |
| 2026-11-11 06:17:19 | [CVE-2026-123700](https://nvd.nist.gov/vuln/detail/CVE-2026-123700) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not check that the requester is authorised before run… |
| 2026-11-11 06:17:19 | [CVE-2026-123701](https://nvd.nist.gov/vuln/detail/CVE-2026-123701) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not have proper authorization checks when resetting i… |
| 2026-11-11 06:17:19 | [CVE-2026-123702](https://nvd.nist.gov/vuln/detail/CVE-2026-123702) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not check that the requester is authorised before reg… |
| 2026-11-11 06:17:19 | [CVE-2026-123703](https://nvd.nist.gov/vuln/detail/CVE-2026-123703) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not check that the requester is authorised before end… |
| 2026-11-11 06:17:19 | [CVE-2026-123704](https://nvd.nist.gov/vuln/detail/CVE-2026-123704) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not restrict access to one of its REST API routes, al… |
| 2026-11-11 06:17:19 | [CVE-2026-123705](https://nvd.nist.gov/vuln/detail/CVE-2026-123705) |  |  | The Security For WooCommerce WordPress plugin through 1.0.16 does not restrict access to one of its REST API routes, al… |
| 2026-11-11 06:17:21 | [CVE-2026-88813](https://nvd.nist.gov/vuln/detail/CVE-2026-88813) |  |  | The YITH WooCommerce Gift Cards WordPress plugin through 4.39.0 does not reconcile the value of a gift card it issues a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
