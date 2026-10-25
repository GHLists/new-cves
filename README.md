# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-25 06:18 UTC

New CVEs published between 2026-10-25 05:20 UTC and 2026-10-25 06:18 UTC.

[Full CSV](data/new-cves-2026-10-25T06-18-41-603442Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-25 06:16:29 | [CVE-2025-15705](https://nvd.nist.gov/vuln/detail/CVE-2025-15705) |  |  | The Contact Form by Supsystic WordPress plugin before 1.8.0 does not sanitise and escape a form name, allowing users wi… |
| 2026-10-25 06:16:31 | [CVE-2026-110285](https://nvd.nist.gov/vuln/detail/CVE-2026-110285) |  |  | The WP Stripe Checkout WordPress plugin before 1.2.2.62 does not verify the Stripe webhook signature when no signing se… |
| 2026-10-25 06:16:31 | [CVE-2026-111976](https://nvd.nist.gov/vuln/detail/CVE-2026-111976) |  |  | The GiveWP WordPress plugin before 4.19.0.1 does not perform any status or capability check when rendering a donation f… |
| 2026-10-25 06:16:31 | [CVE-2026-111978](https://nvd.nist.gov/vuln/detail/CVE-2026-111978) |  |  | The GiveWP WordPress plugin before 4.19.0.1 does not properly validate a user-supplied filename before reading it from… |
| 2026-10-25 06:16:31 | [CVE-2026-111979](https://nvd.nist.gov/vuln/detail/CVE-2026-111979) |  |  | The GiveWP WordPress plugin before 4.19.0.1 does not properly sanitise and escape one of its donation form template set… |
| 2026-10-25 06:16:31 | [CVE-2026-111980](https://nvd.nist.gov/vuln/detail/CVE-2026-111980) |  |  | The GiveWP WordPress plugin before 4.19.0.1 does not correctly determine which page a page-capability request applies t… |
| 2026-10-25 06:16:31 | [CVE-2026-111981](https://nvd.nist.gov/vuln/detail/CVE-2026-111981) |  |  | The GiveWP WordPress plugin before 4.19.0.1 does not perform a capability check when handling donor address changes, al… |
| 2026-10-25 06:16:31 | [CVE-2026-114740](https://nvd.nist.gov/vuln/detail/CVE-2026-114740) |  |  | The WPVR WordPress plugin before 9.1.3 does not correctly check user capabilities when creating a tour through its setu… |
| 2026-10-25 06:16:31 | [CVE-2026-114741](https://nvd.nist.gov/vuln/detail/CVE-2026-114741) |  |  | The WPVR WordPress plugin before 9.0.3 does not perform object-level authorization checks when reading and updating vir… |
| 2026-10-25 06:16:31 | [CVE-2026-114742](https://nvd.nist.gov/vuln/detail/CVE-2026-114742) |  |  | The WPVR WordPress plugin before 9.0.3 does not perform object-level ownership checks when updating virtual tours, allo… |
| 2026-10-25 06:16:32 | [CVE-2026-114743](https://nvd.nist.gov/vuln/detail/CVE-2026-114743) |  |  | The InstaWP Connect WordPress plugin before 0.1.4.2 does not perform a capability check on its InstaWP Connect WordPres… |
| 2026-10-25 06:16:32 | [CVE-2026-115183](https://nvd.nist.gov/vuln/detail/CVE-2026-115183) |  |  | The Qi Addons For Elementor WordPress plugin before 1.11.2 does not properly sanitise a widget's heading text after dec… |
| 2026-10-25 06:16:32 | [CVE-2026-115214](https://nvd.nist.gov/vuln/detail/CVE-2026-115214) |  |  | The Datawiza Proxy Auth Plugin WordPress plugin before 1.1.1 does not verify that the user-identity and role HTTP reque… |
| 2026-10-25 06:16:32 | [CVE-2026-115251](https://nvd.nist.gov/vuln/detail/CVE-2026-115251) |  |  | The Duplicator WordPress plugin before 5.0.0 does not restrict its one-click upgrade routine to users allowed to instal… |
| 2026-10-25 06:16:32 | [CVE-2026-116044](https://nvd.nist.gov/vuln/detail/CVE-2026-116044) | Low | 2.1 | A security vulnerability has been detected in prasathmani TinyFileManager up to 2.6. Affected by this issue is some unk… |
| 2026-10-25 06:16:33 | [CVE-2026-94295](https://nvd.nist.gov/vuln/detail/CVE-2026-94295) |  |  | The Chikkili- Google Pay India for Woocommerce WordPress plugin through 1.0.6 does not verify that a payment notificati… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
