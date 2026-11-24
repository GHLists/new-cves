# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-24 13:18 UTC

New CVEs published between 2026-11-24 12:21 UTC and 2026-11-24 13:18 UTC.

[Full CSV](data/new-cves-2026-11-24T13-18-38-746055Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-24 13:17:21 | [CVE-2026-120720](https://nvd.nist.gov/vuln/detail/CVE-2026-120720) | Medium | 5.9 | Server-Side Request Forgery (SSRF) vulnerability in ex-aws ex_aws allows an attacker who controls an S3 bucket name to… |
| 2026-11-24 13:17:22 | [CVE-2026-124268](https://nvd.nist.gov/vuln/detail/CVE-2026-124268) | Medium | 4.3 | Missing Authorization vulnerability in Arraytics WP Event Solution wp-event-solution allows Exploiting Incorrectly Conf… |
| 2026-11-24 13:17:22 | [CVE-2026-124273](https://nvd.nist.gov/vuln/detail/CVE-2026-124273) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Arraytics WP Even… |
| 2026-11-24 13:17:22 | [CVE-2026-124754](https://nvd.nist.gov/vuln/detail/CVE-2026-124754) | Medium | 6.9 | RTU500 has a NULL pointer dereference vulnerability through the NCMD metric name present in the Sparkplug payload of th… |
| 2026-11-24 13:17:22 | [CVE-2026-125441](https://nvd.nist.gov/vuln/detail/CVE-2026-125441) | Medium | 5.3 | Missing Authorization vulnerability in Arraytics WP Event Solution wp-event-solution allows Exploiting Incorrectly Conf… |
| 2026-11-24 13:17:23 | [CVE-2026-127181](https://nvd.nist.gov/vuln/detail/CVE-2026-127181) | High | 7.6 | SUSE Neuvector before 5.5, 5.5.0 before 5.5.6 and 5.6.0 before 5.6.5 handling of ephemeral containers was not setting s… |
| 2026-11-24 13:17:23 | [CVE-2026-129058](https://nvd.nist.gov/vuln/detail/CVE-2026-129058) | Medium | 5.3 | Missing Authorization vulnerability in VillaTheme CURCY woo-multi-currency allows Exploiting Incorrectly Configured Acc… |
| 2026-11-24 13:17:23 | [CVE-2026-131746](https://nvd.nist.gov/vuln/detail/CVE-2026-131746) | Medium | 5.3 | Missing Authorization vulnerability in VillaTheme Coupzy woo-coupon-box allows Exploiting Incorrectly Configured Access… |
| 2026-11-24 13:17:23 | [CVE-2026-131747](https://nvd.nist.gov/vuln/detail/CVE-2026-131747) | Medium | 5.4 | Cross-Site Request Forgery (CSRF) vulnerability in Themeisle WP Full Stripe Free wp-full-stripe-free allows Cross Site… |
| 2026-11-24 13:17:23 | [CVE-2026-131762](https://nvd.nist.gov/vuln/detail/CVE-2026-131762) | Medium | 4.3 | Cross-Site Request Forgery (CSRF) vulnerability in VeronaLabs WP Statistics wp-statistics allows Cross Site Request For… |
| 2026-11-24 13:17:23 | [CVE-2026-131779](https://nvd.nist.gov/vuln/detail/CVE-2026-131779) | Medium | 5.3 | Missing Authorization vulnerability in WP Desk Flexible Quantity – Measurement Price Calculator for WooCommerce flexibl… |
| 2026-11-24 13:17:24 | [CVE-2026-133763](https://nvd.nist.gov/vuln/detail/CVE-2026-133763) | Medium | 5.3 | The sandbox checks that a template may call toString() on an object before converting it to a string. For an object, th… |
| 2026-11-24 13:17:24 | [CVE-2026-133764](https://nvd.nist.gov/vuln/detail/CVE-2026-133764) | Low | 2.3 | The sandbox checks that a template may call toString() on an object before converting it to a string. It didn't check t… |
| 2026-11-24 13:17:24 | [CVE-2026-133765](https://nvd.nist.gov/vuln/detail/CVE-2026-133765) | Medium | 5.3 | The sandbox checks that a template may call toString() on an object before converting it to a string. Since Twig 3.23.0… |
| 2026-11-24 13:17:24 | [CVE-2026-133766](https://nvd.nist.gov/vuln/detail/CVE-2026-133766) | Low | 2.3 | Since Twig 3.28.0, the sandbox skips the toString() check of an argument whose PHP parameter can't hold a string, like… |
| 2026-11-24 13:17:24 | [CVE-2026-133767](https://nvd.nist.gov/vuln/detail/CVE-2026-133767) | Medium | 5.3 | When the parent of an embed tag was an expression other than a string or a variable, the sandbox didn't see that expres… |
| 2026-11-24 13:17:24 | [CVE-2026-133768](https://nvd.nist.gov/vuln/detail/CVE-2026-133768) | Medium | 5.3 | The join filter converted a value that isn't iterable with (array) $value. For an object, that gives every property, in… |
| 2026-11-24 13:17:25 | [CVE-2026-133769](https://nvd.nist.gov/vuln/detail/CVE-2026-133769) | Low | 2.3 | Cva::apply() converted the values of variants, default variants and compound variants with (array). These values come f… |
| 2026-11-24 13:17:25 | [CVE-2026-133770](https://nvd.nist.gov/vuln/detail/CVE-2026-133770) | Low | 2.1 | The sandbox allows every method of Twig\Markup objects, including their public constructor. A sandboxed template can th… |
| 2026-11-24 13:17:25 | [CVE-2026-133771](https://nvd.nist.gov/vuln/detail/CVE-2026-133771) | Low | 2.3 | The escaper considered x.attr, x['key'] and x.method() safe whenever {% import ... as x %} appeared anywhere in the tem… |
| 2026-11-24 13:17:25 | [CVE-2026-133772](https://nvd.nist.gov/vuln/detail/CVE-2026-133772) | Low | 2.3 | The guard tag compiles only one of its branches, depending on whether a callable exists. The other branch was still par… |
| 2026-11-24 13:17:25 | [CVE-2026-133773](https://nvd.nist.gov/vuln/detail/CVE-2026-133773) | Low | 2.3 | The html_to_markdown filter of twig/markdown-extra keeps an HtmlConverter for each distinct mapping of options it recei… |
| 2026-11-24 13:17:25 | [CVE-2026-134125](https://nvd.nist.gov/vuln/detail/CVE-2026-134125) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in hupe13 Extension… |
| 2026-11-24 13:17:25 | [CVE-2026-134467](https://nvd.nist.gov/vuln/detail/CVE-2026-134467) | Medium | 4.3 | Missing Authorization vulnerability in HivePress HivePress hivepress allows Exploiting Incorrectly Configured Access Co… |
| 2026-11-24 13:17:26 | [CVE-2026-134468](https://nvd.nist.gov/vuln/detail/CVE-2026-134468) | Medium | 4.3 | Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in HivePress HivePress hive… |
| 2026-11-24 13:17:26 | [CVE-2026-134482](https://nvd.nist.gov/vuln/detail/CVE-2026-134482) | Medium | 5.3 | Missing Authorization vulnerability in VillaTheme Thank You Page Customizer for WooCommerce woo-thank-you-page-customiz… |
| 2026-11-24 13:17:26 | [CVE-2026-134485](https://nvd.nist.gov/vuln/detail/CVE-2026-134485) | Medium | 5.3 | Missing Authorization vulnerability in Mamunur Rashid Radius Booking — Booking Calendar for Appointments &amp; Services… |
| 2026-11-24 13:17:26 | [CVE-2026-134707](https://nvd.nist.gov/vuln/detail/CVE-2026-134707) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in WP Speedo Team Me… |
| 2026-11-24 13:17:26 | [CVE-2026-134709](https://nvd.nist.gov/vuln/detail/CVE-2026-134709) | Medium | 5.3 | Missing Authorization vulnerability in Mamunur Rashid Radius Booking — Booking Calendar for Appointments &amp; Services… |
| 2026-11-24 13:17:27 | [CVE-2026-134954](https://nvd.nist.gov/vuln/detail/CVE-2026-134954) | Medium | 5.3 | Missing Authorization vulnerability in StaxWP Visibility Logic for Elementor visibility-logic-elementor allows Exploiti… |
| 2026-11-24 13:17:27 | [CVE-2026-134962](https://nvd.nist.gov/vuln/detail/CVE-2026-134962) | High | 7.1 | Missing Authorization vulnerability in Slim & Dapper Theater for WordPress theatre allows Exploiting Incorrectly Config… |
| 2026-11-24 13:17:27 | [CVE-2026-134996](https://nvd.nist.gov/vuln/detail/CVE-2026-134996) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in YITH YITH WooComm… |
| 2026-11-24 13:17:27 | [CVE-2026-134998](https://nvd.nist.gov/vuln/detail/CVE-2026-134998) | Medium | 4.3 | Missing Authorization vulnerability in Themefic Ultimate Addons for Contact Form 7 ultimate-addons-for-contact-form-7 a… |
| 2026-11-24 13:17:27 | [CVE-2026-135015](https://nvd.nist.gov/vuln/detail/CVE-2026-135015) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Themefic BEAF bea… |
| 2026-11-24 13:17:27 | [CVE-2026-135020](https://nvd.nist.gov/vuln/detail/CVE-2026-135020) | Medium | 5.3 | Missing Authorization vulnerability in Themefic Tourfic tourfic allows Exploiting Incorrectly Configured Access Control… |
| 2026-11-24 13:17:27 | [CVE-2026-135021](https://nvd.nist.gov/vuln/detail/CVE-2026-135021) | Medium | 5.3 | Missing Authorization vulnerability in Themefic Tourfic tourfic allows Exploiting Incorrectly Configured Access Control… |
| 2026-11-24 13:17:28 | [CVE-2026-135023](https://nvd.nist.gov/vuln/detail/CVE-2026-135023) | Medium | 4.3 | Missing Authorization vulnerability in Themefic Tourfic tourfic allows Exploiting Incorrectly Configured Access Control… |
| 2026-11-24 13:17:28 | [CVE-2026-135026](https://nvd.nist.gov/vuln/detail/CVE-2026-135026) | Medium | 5.3 | Missing Authorization vulnerability in Themefic Tourfic tourfic allows Exploiting Incorrectly Configured Access Control… |
| 2026-11-24 13:17:28 | [CVE-2026-135041](https://nvd.nist.gov/vuln/detail/CVE-2026-135041) | Medium | 5.3 | Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in Themefic Hydra Booking h… |
| 2026-11-24 13:17:28 | [CVE-2026-135043](https://nvd.nist.gov/vuln/detail/CVE-2026-135043) | Medium | 5.3 | Insertion of Sensitive Information Into Sent Data vulnerability in Themefic Hydra Booking hydra-booking allows Retrieve… |
| 2026-11-24 13:17:28 | [CVE-2026-135044](https://nvd.nist.gov/vuln/detail/CVE-2026-135044) | Medium | 5.3 | Missing Authorization vulnerability in Themefic Hydra Booking hydra-booking allows Exploiting Incorrectly Configured Ac… |
| 2026-11-24 13:17:30 | [CVE-2026-135842](https://nvd.nist.gov/vuln/detail/CVE-2026-135842) | Medium | 5.3 | Missing Authorization vulnerability in Themefic Ultra Addons for WPForms ultra-addons-for-wpforms allows Exploiting Inc… |
| 2026-11-24 13:17:30 | [CVE-2026-135891](https://nvd.nist.gov/vuln/detail/CVE-2026-135891) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in Qode Interactive… |
| 2026-11-24 13:17:30 | [CVE-2026-136120](https://nvd.nist.gov/vuln/detail/CVE-2026-136120) | High | 8.6 | Ziit 1.3.2 contains a cross-site request forgery vulnerability in the /api/auth/epilogue/callback handler that accepts… |
| 2026-11-24 13:17:31 | [CVE-2026-136123](https://nvd.nist.gov/vuln/detail/CVE-2026-136123) | High | 8.7 | Friendica through 2026.05-1 contains an improper validation vulnerability in APContact::compactProfile() that allows re… |
| 2026-11-24 13:17:31 | [CVE-2026-136124](https://nvd.nist.gov/vuln/detail/CVE-2026-136124) | Medium | 6.0 | ffmate before 2.1.0 contains an argument injection vulnerability in wildcardReplacer that allows attackers to inject ff… |
| 2026-11-24 13:17:31 | [CVE-2026-136126](https://nvd.nist.gov/vuln/detail/CVE-2026-136126) | Critical | 9.2 | c-icap-server through 0.5.15 and 0.6.5 contains an out-of-bounds write in process_encapsulated() that allows unauthenti… |
| 2026-11-24 13:17:31 | [CVE-2026-136128](https://nvd.nist.gov/vuln/detail/CVE-2026-136128) | High | 8.5 | WPC Linked Variation plugin for WordPress, all versions before 4.6.1, contain a stored cross-site scripting vulnerabili… |
| 2026-11-24 13:17:31 | [CVE-2026-14569](https://nvd.nist.gov/vuln/detail/CVE-2026-14569) | High | 8.7 | Use of externally-controlled format string vulnerability exists in RTU500 component of the logging function for TLS, PP… |
| 2026-11-24 13:17:33 | [CVE-2026-62270](https://nvd.nist.gov/vuln/detail/CVE-2026-62270) | Medium | 5.9 | Improper Validation of Specified Type of Input in ExAws.Dynamo.Encoder.encode/2 in ex_aws_dynamo allows an attacker who… |
| 2026-11-24 13:17:34 | [CVE-2026-62271](https://nvd.nist.gov/vuln/detail/CVE-2026-62271) | Low | 2.1 | Use of RSA Algorithm without OAEP vulnerability in ex-aws ex_aws_kms (ExAws.KMS module) causes callers who import exter… |
| 2026-11-24 13:17:35 | [CVE-2026-81577](https://nvd.nist.gov/vuln/detail/CVE-2026-81577) | Medium | 6.5 | Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability in ITG Bilgisayar Teknoloj… |
| 2026-11-24 13:17:35 | [CVE-2026-82216](https://nvd.nist.gov/vuln/detail/CVE-2026-82216) | High | 7.5 | Server-Side request forgery (SSRF) vulnerability in ITG Bilgisayar Teknolojileri Grubu Ltd. Şti. VSRM allows Server Sid… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
