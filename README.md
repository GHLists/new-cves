# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-29 16:20 UTC

New CVEs published between 2026-10-29 15:19 UTC and 2026-10-29 16:20 UTC.

[Full CSV](data/new-cves-2026-10-29T16-20-23-804706Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-10-29 16:17:32 | [CVE-2025-13050](https://nvd.nist.gov/vuln/detail/CVE-2025-13050) | Medium | 5.4 | Broken Function Level Authorization allows execution of poller post-restart commands by authenticated user |
| 2026-10-29 16:17:35 | [CVE-2026-101288](https://nvd.nist.gov/vuln/detail/CVE-2026-101288) | High | 8.8 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to execute arbitrary code due to impr… |
| 2026-10-29 16:17:39 | [CVE-2026-102590](https://nvd.nist.gov/vuln/detail/CVE-2026-102590) | Medium | 5.0 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to obtain sensitive information due t… |
| 2026-10-29 16:17:41 | [CVE-2026-103092](https://nvd.nist.gov/vuln/detail/CVE-2026-103092) | High | 8.5 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to execute arbitrary SQL commands due… |
| 2026-10-29 16:17:43 | [CVE-2026-104308](https://nvd.nist.gov/vuln/detail/CVE-2026-104308) | Medium | 4.3 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to cause a denial of service due to i… |
| 2026-10-29 16:17:43 | [CVE-2026-104309](https://nvd.nist.gov/vuln/detail/CVE-2026-104309) | Medium | 6.5 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to obtain sensitive information due t… |
| 2026-10-29 16:17:43 | [CVE-2026-104310](https://nvd.nist.gov/vuln/detail/CVE-2026-104310) | Medium | 4.3 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to obtain sensitive information due t… |
| 2026-10-29 16:17:43 | [CVE-2026-104312](https://nvd.nist.gov/vuln/detail/CVE-2026-104312) | Low | 3.5 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow an authenticated attacker to produce a server-generated ZIP archive c… |
| 2026-10-29 16:17:43 | [CVE-2026-104314](https://nvd.nist.gov/vuln/detail/CVE-2026-104314) | Medium | 6.5 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow an authenticated attacker with a read or share grant on a target flow… |
| 2026-10-29 16:17:43 | [CVE-2026-104315](https://nvd.nist.gov/vuln/detail/CVE-2026-104315) | Medium | 4.3 | IBM Langflow OSS 1.0.0 through 1.12.3 is vulnerable to server-side request forgery (SSRF). This may allow an authentica… |
| 2026-10-29 16:17:43 | [CVE-2026-104316](https://nvd.nist.gov/vuln/detail/CVE-2026-104316) | Medium | 6.5 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow an authenticated attacker to cancel any victim's running background w… |
| 2026-10-29 16:17:43 | [CVE-2026-104317](https://nvd.nist.gov/vuln/detail/CVE-2026-104317) | High | 8.1 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote attacker who could reach the message broker to execute arbit… |
| 2026-10-29 16:17:44 | [CVE-2026-104324](https://nvd.nist.gov/vuln/detail/CVE-2026-104324) | High | 8.8 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to execute arbitrary code due to dese… |
| 2026-10-29 16:17:44 | [CVE-2026-104328](https://nvd.nist.gov/vuln/detail/CVE-2026-104328) | High | 8.8 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to execute arbitrary code due to impr… |
| 2026-10-29 16:17:44 | [CVE-2026-104331](https://nvd.nist.gov/vuln/detail/CVE-2026-104331) | Medium | 5.4 | IBM Langflow OSS 1.0.0 through 1.12.3 is vulnerable to server-side request forgery (SSRF). This may allow an authentica… |
| 2026-10-29 16:17:44 | [CVE-2026-104339](https://nvd.nist.gov/vuln/detail/CVE-2026-104339) | Critical | 9.8 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote attacker to execute arbitrary code due to improper neutraliz… |
| 2026-10-29 16:17:47 | [CVE-2026-106036](https://nvd.nist.gov/vuln/detail/CVE-2026-106036) | Medium | 6.9 | Szafir accepts any client or server certificate without performing certificate and hostname validation, allowing HTTPS… |
| 2026-10-29 16:17:48 | [CVE-2026-107025](https://nvd.nist.gov/vuln/detail/CVE-2026-107025) |  |  | Insecure permissions in WikiAndPad alpha/beta v0.2alpha03 (versionCode 200300) allows unauthorized attackers to export… |
| 2026-10-29 16:17:48 | [CVE-2026-107026](https://nvd.nist.gov/vuln/detail/CVE-2026-107026) |  |  | Insecure permissions in Share to Clipboard v1.14.1 (versionCode 32) allows unauthorized attackers to arbitrarily overwr… |
| 2026-10-29 16:17:48 | [CVE-2026-107027](https://nvd.nist.gov/vuln/detail/CVE-2026-107027) |  |  | Insecure permissions in lz233 Tarnhelm v1.8.2 (versionCode 20250630) allows unauthorized attackers to invoke an exporte… |
| 2026-10-29 16:17:48 | [CVE-2026-107028](https://nvd.nist.gov/vuln/detail/CVE-2026-107028) |  |  | Insecure permissions in wbpxre150 Shopping List v11.0 (versionCode 11) allows unauthorized attackers to invoke an expor… |
| 2026-10-29 16:17:48 | [CVE-2026-107029](https://nvd.nist.gov/vuln/detail/CVE-2026-107029) |  |  | Insecure permissions in rubenalfon Pile v1.1.3 allows unauthorized attackers to invoke an exported component, leading t… |
| 2026-10-29 16:17:48 | [CVE-2026-107030](https://nvd.nist.gov/vuln/detail/CVE-2026-107030) |  |  | Insecure permissions in craftxbox YubiClip XOR fork v1.0.1 (versionCode 10003) allows unauthorized attackers to trigger… |
| 2026-10-29 16:17:48 | [CVE-2026-107032](https://nvd.nist.gov/vuln/detail/CVE-2026-107032) |  |  | Insecure permissions in Bulk Share : Location Sender v2.1.0 (versionCode 5) allows unauthorized attackers to invoke an… |
| 2026-10-29 16:17:49 | [CVE-2026-107033](https://nvd.nist.gov/vuln/detail/CVE-2026-107033) |  |  | Insecure permissions in the MirakelInternalContentProvider component of Mirakel v3.0 (versionCode 60) allows unauthoriz… |
| 2026-10-29 16:17:49 | [CVE-2026-107034](https://nvd.nist.gov/vuln/detail/CVE-2026-107034) |  |  | Insecure permissions in LeafPad / Leaf Note v1.21 (versionCode 21) allows unauthorized attackers to arbitrarily read an… |
| 2026-10-29 16:17:49 | [CVE-2026-107035](https://nvd.nist.gov/vuln/detail/CVE-2026-107035) |  |  | Insecure permissions in the object/Page.java component of MBasov OMN Outline notes Markdown versionCode 3400 allows una… |
| 2026-10-29 16:17:49 | [CVE-2026-107036](https://nvd.nist.gov/vuln/detail/CVE-2026-107036) |  |  | Insecure permissions in Mission Control / AIMSICD versionCode 2026080501 allows unauthorized attackers to invoke an exp… |
| 2026-10-29 16:17:49 | [CVE-2026-107037](https://nvd.nist.gov/vuln/detail/CVE-2026-107037) |  |  | Insecure permissions in the NotificationHelper component of NoNonsense Notes versionCode 72600 allows unauthorized atta… |
| 2026-10-29 16:17:49 | [CVE-2026-107038](https://nvd.nist.gov/vuln/detail/CVE-2026-107038) |  |  | Insecure permissions in Yet Another UPnP Controller versionCode 50200 allows unauthorized attackers to invoke an export… |
| 2026-10-29 16:17:49 | [CVE-2026-107039](https://nvd.nist.gov/vuln/detail/CVE-2026-107039) |  |  | Insecure permissions in the ActivityMain component of M66B/Marcel Bokhorst NetGuard no-root firewall versionCode 202608… |
| 2026-10-29 16:17:49 | [CVE-2026-107040](https://nvd.nist.gov/vuln/detail/CVE-2026-107040) |  |  | Insecure permissions in MBasov OMN-Go versionCode 26080824 allows unauthorized attackers to invoke an exported componen… |
| 2026-10-29 16:17:49 | [CVE-2026-107041](https://nvd.nist.gov/vuln/detail/CVE-2026-107041) |  |  | Insecure permissions in the FeatureActionActivity component of Oasis Feng Island versionCode 51801 allows unauthorized… |
| 2026-10-29 16:17:50 | [CVE-2026-107042](https://nvd.nist.gov/vuln/detail/CVE-2026-107042) |  |  | Insecure permissions in USP Ultimate Screenshot Painter versionCode 240213.009 allows unauthorized attackers to move or… |
| 2026-10-29 16:17:50 | [CVE-2026-107326](https://nvd.nist.gov/vuln/detail/CVE-2026-107326) | High | 8.8 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to impr… |
| 2026-10-29 16:17:50 | [CVE-2026-107327](https://nvd.nist.gov/vuln/detail/CVE-2026-107327) | Critical | 9.9 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to miss… |
| 2026-10-29 16:17:50 | [CVE-2026-107328](https://nvd.nist.gov/vuln/detail/CVE-2026-107328) | Critical | 9.9 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to impr… |
| 2026-10-29 16:17:50 | [CVE-2026-107329](https://nvd.nist.gov/vuln/detail/CVE-2026-107329) | Critical | 9.9 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary code due to impr… |
| 2026-10-29 16:17:55 | [CVE-2026-108494](https://nvd.nist.gov/vuln/detail/CVE-2026-108494) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in Chained Quiz <= 1.4.1 versions. |
| 2026-10-29 16:17:55 | [CVE-2026-109891](https://nvd.nist.gov/vuln/detail/CVE-2026-109891) | Medium | 6.4 | Missing Authorization vulnerability in weDevs Happy Addons for Elementor happy-elementor-addons allows Exploiting Incor… |
| 2026-10-29 16:17:55 | [CVE-2026-110186](https://nvd.nist.gov/vuln/detail/CVE-2026-110186) | Critical | 9.8 | IBM Langflow OSS 1.0.0 through 1.12.8 could allow a remote attacker to execute arbitrary code due to improper control o… |
| 2026-10-29 16:17:55 | [CVE-2026-110190](https://nvd.nist.gov/vuln/detail/CVE-2026-110190) | Medium | 6.5 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow an authenticated user to traverse directories on the system. An attac… |
| 2026-10-29 16:17:56 | [CVE-2026-110192](https://nvd.nist.gov/vuln/detail/CVE-2026-110192) | Medium | 6.5 | IBM Langflow OSS 1.0.0 through 1.12.8 could allow a remote authenticated attacker to obtain sensitive information due t… |
| 2026-10-29 16:17:56 | [CVE-2026-110193](https://nvd.nist.gov/vuln/detail/CVE-2026-110193) | High | 8.8 | IBM Langflow OSS 1.0.0 through 1.12.8 could allow a remote attacker with a low-privileged authenticated account to caus… |
| 2026-10-29 16:17:56 | [CVE-2026-110196](https://nvd.nist.gov/vuln/detail/CVE-2026-110196) | High | 8.8 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote attacker with a low-privileged authenticated account to bypa… |
| 2026-10-29 16:17:56 | [CVE-2026-110200](https://nvd.nist.gov/vuln/detail/CVE-2026-110200) | Medium | 6.5 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to obtain sensitive information due t… |
| 2026-10-29 16:17:56 | [CVE-2026-110244](https://nvd.nist.gov/vuln/detail/CVE-2026-110244) | High | 8.8 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to obtain sensitive information due t… |
| 2026-10-29 16:17:56 | [CVE-2026-110245](https://nvd.nist.gov/vuln/detail/CVE-2026-110245) | High | 7.5 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote attacker to obtain sensitive information due to improper aut… |
| 2026-10-29 16:17:57 | [CVE-2026-110309](https://nvd.nist.gov/vuln/detail/CVE-2026-110309) | High | 8.8 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to execute arbitrary commands due to… |
| 2026-10-29 16:17:57 | [CVE-2026-111730](https://nvd.nist.gov/vuln/detail/CVE-2026-111730) | High | 7.2 | P-Net before 1.0.3 does not validate the LengthPeerStationName field of a CheckPeers block in get_check_peer(). The rec… |
| 2026-10-29 16:17:57 | [CVE-2026-111731](https://nvd.nist.gov/vuln/detail/CVE-2026-111731) | High | 8.7 | P-Net before 1.0.3 enters an infinite loop when handling a read request for the PDPortDataCheck record with subslot 0 (… |
| 2026-10-29 16:17:57 | [CVE-2026-111732](https://nvd.nist.gov/vuln/detail/CVE-2026-111732) | Critical | 9.3 | P-Net before 1.0.3, when built with PNET_OPTION_AR_VENDOR_BLOCKS enabled, parses a data length from a field of the ARVe… |
| 2026-10-29 16:17:57 | [CVE-2026-111733](https://nvd.nist.gov/vuln/detail/CVE-2026-111733) | High | 8.7 | P-Net before 1.0.3 dereferences a NULL AR pointer when handling an implicit read request without a valid target AR UUID… |
| 2026-10-29 16:17:57 | [CVE-2026-111734](https://nvd.nist.gov/vuln/detail/CVE-2026-111734) | High | 7.1 | P-Net before 1.0.3 does not validate the length of a received Ethernet frame in pf_eth_recv() before reading the EtherT… |
| 2026-10-29 16:17:57 | [CVE-2026-111735](https://nvd.nist.gov/vuln/detail/CVE-2026-111735) | High | 7.1 | P-Net before 1.0.3 contains an integer underflow in pf_cpm_c_data_ind(). When handling a received cyclic data frame whi… |
| 2026-10-29 16:17:57 | [CVE-2026-111736](https://nvd.nist.gov/vuln/detail/CVE-2026-111736) | High | 8.7 | P-Net before 1.0.3 dereferences a NULL AR pointer in pf_fspm_cm_read_ind() when handling an implicit read request witho… |
| 2026-10-29 16:17:58 | [CVE-2026-112200](https://nvd.nist.gov/vuln/detail/CVE-2026-112200) | High | 8.7 | P-Net before 1.0.3 does not release the Application Relationship (AR) and the RPC session when an RPC request is reject… |
| 2026-10-29 16:17:58 | [CVE-2026-112255](https://nvd.nist.gov/vuln/detail/CVE-2026-112255) | Low | 2.9 | Initialization of a resource with an insecure default vulnerability in OpenText Advanced Authentication Server allows E… |
| 2026-10-29 16:17:58 | [CVE-2026-112256](https://nvd.nist.gov/vuln/detail/CVE-2026-112256) | Critical | 9.2 | Acceptance of extraneous untrusted data with trusted data vulnerability in OpenText Advanced Authentication Server allo… |
| 2026-10-29 16:17:58 | [CVE-2026-113576](https://nvd.nist.gov/vuln/detail/CVE-2026-113576) | Medium | 6.3 | Adobe Digital Editions is affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')… |
| 2026-10-29 16:17:58 | [CVE-2026-114148](https://nvd.nist.gov/vuln/detail/CVE-2026-114148) | High | 7.8 | Incorrect default permissions in ASP.NET Core allows an authorized attacker to elevate privileges locally. |
| 2026-10-29 16:17:58 | [CVE-2026-115793](https://nvd.nist.gov/vuln/detail/CVE-2026-115793) | High | 8.7 | P-Net before 1.0.3 does not release the RPC session allocated for an RPC request that names an unknown interface or obj… |
| 2026-10-29 16:17:58 | [CVE-2026-115794](https://nvd.nist.gov/vuln/detail/CVE-2026-115794) | Low | 2.3 | P-Net before 1.0.3 passes the application alarm callback a data length derived from the variable part length field of a… |
| 2026-10-29 16:17:59 | [CVE-2026-115795](https://nvd.nist.gov/vuln/detail/CVE-2026-115795) | Medium | 5.3 | P-Net before 1.0.3 does not check that a complete block header is present in the received data before reading the next… |
| 2026-10-29 16:18:00 | [CVE-2026-116848](https://nvd.nist.gov/vuln/detail/CVE-2026-116848) | Medium | 6.5 | Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting') vulnerability in POSIMYTH Innovati… |
| 2026-10-29 16:18:01 | [CVE-2026-116864](https://nvd.nist.gov/vuln/detail/CVE-2026-116864) | High | 7.2 | Author PHP Object Injection in WPCargo Track & Trace <= 8.0.5 versions. |
| 2026-10-29 16:18:01 | [CVE-2026-116865](https://nvd.nist.gov/vuln/detail/CVE-2026-116865) | High | 7.2 | Editor PHP Object Injection in Zippy <= 1.7.0 versions. |
| 2026-10-29 16:18:01 | [CVE-2026-116866](https://nvd.nist.gov/vuln/detail/CVE-2026-116866) | High | 8.8 | Contributor PHP Object Injection in Extra Fees Plugin for WooCommerce <= 4.4.0 versions. |
| 2026-10-29 16:18:01 | [CVE-2026-116867](https://nvd.nist.gov/vuln/detail/CVE-2026-116867) | High | 8.8 | Contributor PHP Object Injection in Dynamic QR Code &#8211; generator <= 1.0.1 versions. |
| 2026-10-29 16:18:01 | [CVE-2026-116868](https://nvd.nist.gov/vuln/detail/CVE-2026-116868) | High | 8.8 | Subscriber PHP Object Injection in BuddyPress Xprofile Custom Field Types <= 1.3.1 versions. |
| 2026-10-29 16:18:01 | [CVE-2026-116869](https://nvd.nist.gov/vuln/detail/CVE-2026-116869) | High | 7.2 | Shop manager PHP Object Injection in myPOS Checkout <= 1.4.5 versions. |
| 2026-10-29 16:18:01 | [CVE-2026-118073](https://nvd.nist.gov/vuln/detail/CVE-2026-118073) | High | 8.8 | Subscriber PHP Object Injection in News Kit Elementor Addons <= 1.5.0 versions. |
| 2026-10-29 16:18:02 | [CVE-2026-118074](https://nvd.nist.gov/vuln/detail/CVE-2026-118074) | High | 7.2 | Shop manager PHP Object Injection in Finale Lite <= 2.21.0 versions. |
| 2026-10-29 16:18:02 | [CVE-2026-118075](https://nvd.nist.gov/vuln/detail/CVE-2026-118075) | High | 8.8 | Contributor PHP Object Injection in WP Media folders <= 1.1.10 versions. |
| 2026-10-29 16:18:02 | [CVE-2026-118076](https://nvd.nist.gov/vuln/detail/CVE-2026-118076) | High | 8.8 | Contributor PHP Object Injection in Frisbii Pay <= 1.8.19 versions. |
| 2026-10-29 16:18:02 | [CVE-2026-118077](https://nvd.nist.gov/vuln/detail/CVE-2026-118077) | High | 7.2 | Author PHP Object Injection in Sastra Essential Addons for Elementor <= 1.2.3 versions. |
| 2026-10-29 16:18:02 | [CVE-2026-118078](https://nvd.nist.gov/vuln/detail/CVE-2026-118078) | High | 7.2 | Shop manager PHP Object Injection in Product Catalog Feed by PixelYourSite <= 3.1.4 versions. |
| 2026-10-29 16:18:02 | [CVE-2026-118079](https://nvd.nist.gov/vuln/detail/CVE-2026-118079) | High | 7.2 | Shop manager PHP Object Injection in FV Flowplayer Video Player <= 8.3.4 versions. |
| 2026-10-29 16:18:02 | [CVE-2026-118080](https://nvd.nist.gov/vuln/detail/CVE-2026-118080) | High | 8.8 | Contributor PHP Object Injection in Social Snap <= 1.5.4 versions. |
| 2026-10-29 16:18:02 | [CVE-2026-118081](https://nvd.nist.gov/vuln/detail/CVE-2026-118081) | High | 8.8 | Contributor PHP Object Injection in 10Web Social Photo Feed <= 1.5.6 versions. |
| 2026-10-29 16:18:03 | [CVE-2026-118082](https://nvd.nist.gov/vuln/detail/CVE-2026-118082) | High | 8.8 | Subscriber Privilege Escalation in Buddyboss Platform <= 3.5.0 versions. |
| 2026-10-29 16:18:03 | [CVE-2026-118083](https://nvd.nist.gov/vuln/detail/CVE-2026-118083) | High | 7.5 | Unauthenticated Sensitive Data Exposure in WP Crowdfunding <= 2.2.2 versions. |
| 2026-10-29 16:18:03 | [CVE-2026-118084](https://nvd.nist.gov/vuln/detail/CVE-2026-118084) | Medium | 6.5 | Subscriber Insecure Direct Object References (IDOR) in Hotel Booking <= 3.8 versions. |
| 2026-10-29 16:18:03 | [CVE-2026-118085](https://nvd.nist.gov/vuln/detail/CVE-2026-118085) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in GlobalPayments WooCommerce <= 1.23.3 versions. |
| 2026-10-29 16:18:03 | [CVE-2026-118673](https://nvd.nist.gov/vuln/detail/CVE-2026-118673) | Medium | 4.1 | KeePassXC is a cross-platform community-driven port of the Windows application KeePass Password Safe. From 2.3.0 until… |
| 2026-10-29 16:18:04 | [CVE-2026-119118](https://nvd.nist.gov/vuln/detail/CVE-2026-119118) | High | 8.3 | Crawl4AI before 0.9.5 contains an improper certificate validation vulnerability that allows network attackers to interc… |
| 2026-10-29 16:18:04 | [CVE-2026-119119](https://nvd.nist.gov/vuln/detail/CVE-2026-119119) | High | 8.7 | Crawl4AI before 0.9.5 contains a denial of service vulnerability in the Docker API server where _clamp_untrusted() fail… |
| 2026-10-29 16:18:04 | [CVE-2026-119120](https://nvd.nist.gov/vuln/detail/CVE-2026-119120) | High | 7.7 | Crawl4AI from 0.9.0 before 0.9.5 fails to filter the CosineStrategy model_name field in untrusted Docker API request bo… |
| 2026-10-29 16:18:04 | [CVE-2026-119121](https://nvd.nist.gov/vuln/detail/CVE-2026-119121) | Medium | 5.3 | Crawl4AI from 0.9.0 before 0.9.5 contains a JavaScript injection vulnerability in the Docker API server that allows aut… |
| 2026-10-29 16:18:04 | [CVE-2026-119122](https://nvd.nist.gov/vuln/detail/CVE-2026-119122) | Medium | 6.9 | Crawl4AI before 0.9.5 contains a blind server-side request forgery vulnerability in the Docker server that allows API c… |
| 2026-10-29 16:18:04 | [CVE-2026-119123](https://nvd.nist.gov/vuln/detail/CVE-2026-119123) | Medium | 6.3 | ImageMagick before 7.1.2-34 contains a stack overflow vulnerability in the TIFF decoder that occurs when the DNG decode… |
| 2026-10-29 16:18:05 | [CVE-2026-119124](https://nvd.nist.gov/vuln/detail/CVE-2026-119124) | Medium | 4.8 | ImageMagick before 7.1.2-34 contains a heap-based buffer overflow in its -morph processing, where crafted images cause… |
| 2026-10-29 16:18:05 | [CVE-2026-119125](https://nvd.nist.gov/vuln/detail/CVE-2026-119125) | Low | 2.3 | Parse Server before 8.6.107 and 9.0.0 before 9.10.5-alpha.8 returns the stored value of a field reverted by a beforeSav… |
| 2026-10-29 16:18:05 | [CVE-2026-119126](https://nvd.nist.gov/vuln/detail/CVE-2026-119126) | Low | 2.3 | Parse Server before 8.6.106 and 9.0.0 before 9.10.5-alpha.7 mishandles dot notation keys with null or undefined values… |
| 2026-10-29 16:18:05 | [CVE-2026-119127](https://nvd.nist.gov/vuln/detail/CVE-2026-119127) | High | 8.6 | ZITADEL 4.0.0 before 4.19.5 contains a host header injection vulnerability in the Login V2 UI that allows unauthenticat… |
| 2026-10-29 16:18:05 | [CVE-2026-119128](https://nvd.nist.gov/vuln/detail/CVE-2026-119128) | Critical | 9.1 | ZITADEL 4.0.0 before 4.19.5 contains an authentication bypass vulnerability in the Login V2 UI that allows unauthentica… |
| 2026-10-29 16:18:05 | [CVE-2026-119129](https://nvd.nist.gov/vuln/detail/CVE-2026-119129) | High | 8.6 | ZITADEL 3.0.0 through 3.4.15 and 4.0.0 before 4.19.5 contains a missing authorization vulnerability in Login V2 that al… |
| 2026-10-29 16:18:05 | [CVE-2026-119130](https://nvd.nist.gov/vuln/detail/CVE-2026-119130) | Low | 2.1 | Wasmtime before 36.0.18, 37.0.0 before 48.0.6, and 49.0.0 before 49.0.3 does not verify that set-path-with-query values… |
| 2026-10-29 16:18:06 | [CVE-2026-119131](https://nvd.nist.gov/vuln/detail/CVE-2026-119131) | Medium | 6.9 | Wasmtime 46.0.0 before 48.0.6 and 49.0.0 before 49.0.3 contains a denial of service vulnerability in wasmtime-wasi-http… |
| 2026-10-29 16:18:06 | [CVE-2026-119132](https://nvd.nist.gov/vuln/detail/CVE-2026-119132) | Medium | 5.9 | Wasmtime from 49.0.0 before 49.0.3 contains a denial-of-service vulnerability that allows a WebAssembly guest to trigge… |
| 2026-10-29 16:18:06 | [CVE-2026-119133](https://nvd.nist.gov/vuln/detail/CVE-2026-119133) | Low | 2.1 | Wasmtime 47.0.0 before 48.0.6 and 49.0.0 before 49.0.3 contains a memory misalignment flaw in VMContext layout that cau… |
| 2026-10-29 16:18:06 | [CVE-2026-119134](https://nvd.nist.gov/vuln/detail/CVE-2026-119134) | Medium | 6.9 | Wasmtime before 36.0.18, 37.0.0 before 48.0.6, and 49.0.0 before 49.0.3 caps component-model resource handle tables onl… |
| 2026-10-29 16:18:06 | [CVE-2026-119135](https://nvd.nist.gov/vuln/detail/CVE-2026-119135) | Medium | 5.9 | Wasmtime 46.0.0 before 48.0.6 and 49.0.0 before 49.0.3 panics when the host reads a component model stream as a differe… |
| 2026-10-29 16:18:06 | [CVE-2026-119136](https://nvd.nist.gov/vuln/detail/CVE-2026-119136) | Medium | 5.9 | Wasmtime 42.0.0 before 48.0.6 and 49.0.0 before 49.0.3 contains insufficient checks in Store when mixing async-style an… |
| 2026-10-29 16:18:07 | [CVE-2026-119137](https://nvd.nist.gov/vuln/detail/CVE-2026-119137) | Medium | 6.9 | Wasmtime 42.0.0 before 48.0.6 and 49.0.0 before 49.0.3 contains a stack overflow vulnerability that allows guests to cr… |
| 2026-10-29 16:18:07 | [CVE-2026-119138](https://nvd.nist.gov/vuln/detail/CVE-2026-119138) | Medium | 5.9 | Wasmtime 46.0.0 before 48.0.6 and 49.0.0 before 49.0.3 contains a denial of service vulnerability that allows pending c… |
| 2026-10-29 16:18:07 | [CVE-2026-119139](https://nvd.nist.gov/vuln/detail/CVE-2026-119139) | Medium | 5.9 | Wasmtime 46.0.0 before 48.0.6 and 49.0.0 before 49.0.3 contains a leftover assertion in component::Func::call that reje… |
| 2026-10-29 16:18:07 | [CVE-2026-119140](https://nvd.nist.gov/vuln/detail/CVE-2026-119140) | Medium | 5.9 | Wasmtime 46.0.0 before 48.0.6 and 49.0.0 before 49.0.3 contains a denial of service vulnerability that allows malicious… |
| 2026-10-29 16:18:07 | [CVE-2026-119141](https://nvd.nist.gov/vuln/detail/CVE-2026-119141) | Medium | 6.9 | Wasmtime 46.0.0 before 48.0.6 and 49.0.0 before 49.0.3 contains a denial of service vulnerability that allows malicious… |
| 2026-10-29 16:18:07 | [CVE-2026-119142](https://nvd.nist.gov/vuln/detail/CVE-2026-119142) | Medium | 5.9 | Wasmtime 46.0.0 before 48.0.6 and 49.0.0 before 49.0.3 contains a denial of service vulnerability where dropping the Fu… |
| 2026-10-29 16:18:07 | [CVE-2026-119143](https://nvd.nist.gov/vuln/detail/CVE-2026-119143) | Medium | 5.9 | Wasmtime 46.0.0 before 48.0.6 and 49.0.0 before 49.0.3 contains a denial of service vulnerability that allows guest cod… |
| 2026-10-29 16:18:08 | [CVE-2026-119144](https://nvd.nist.gov/vuln/detail/CVE-2026-119144) | High | 8.7 | Frappe Framework before 15.111.0 and 16.x before 16.21.0 contains a server-side template injection vulnerability becaus… |
| 2026-10-29 16:18:08 | [CVE-2026-119145](https://nvd.nist.gov/vuln/detail/CVE-2026-119145) | Critical | 9.4 | Frappe before 15.121.0 and 16.x before 16.34.0 contains a path traversal vulnerability because certain file-upload hand… |
| 2026-10-29 16:18:08 | [CVE-2026-18894](https://nvd.nist.gov/vuln/detail/CVE-2026-18894) | Medium | 6.5 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote attacker to trigger pre-existing stored Python component cod… |
| 2026-10-29 16:18:08 | [CVE-2026-20942](https://nvd.nist.gov/vuln/detail/CVE-2026-20942) | Medium | 4.3 | Improper restriction of rendered ui layers or frames in Microsoft Edge (Chromium-based) allows an unauthorized attacker… |
| 2026-10-29 16:18:08 | [CVE-2026-27394](https://nvd.nist.gov/vuln/detail/CVE-2026-27394) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in Eventer <= 0.1.1 versions. |
| 2026-10-29 16:18:09 | [CVE-2026-42690](https://nvd.nist.gov/vuln/detail/CVE-2026-42690) | Medium | 5.4 | Subscriber Broken Access Control in LearnPress <= 4.4.10 versions. |
| 2026-10-29 16:18:09 | [CVE-2026-42692](https://nvd.nist.gov/vuln/detail/CVE-2026-42692) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in WP Crowdfunding <= 2.2.2 versions. |
| 2026-10-29 16:18:09 | [CVE-2026-42694](https://nvd.nist.gov/vuln/detail/CVE-2026-42694) | Medium | 4.3 | Improper Neutralization of Script-Related HTML Tags in a Web Page (Basic XSS) vulnerability in Themeum Kirki kirki allo… |
| 2026-10-29 16:18:09 | [CVE-2026-42701](https://nvd.nist.gov/vuln/detail/CVE-2026-42701) | High | 7.2 | Shop manager PHP Object Injection in YayMail <= 4.4.6 versions. |
| 2026-10-29 16:18:09 | [CVE-2026-48200](https://nvd.nist.gov/vuln/detail/CVE-2026-48200) | Medium | 5.3 | Insertion of Sensitive Information Into Sent Data vulnerability in Barn2 Plugins Document Library Lite document-library… |
| 2026-10-29 16:18:09 | [CVE-2026-54856](https://nvd.nist.gov/vuln/detail/CVE-2026-54856) | Critical | 9.8 | Unauthenticated PHP Object Injection in RexCoin <= 1.2.6 versions. |
| 2026-10-29 16:18:09 | [CVE-2026-54857](https://nvd.nist.gov/vuln/detail/CVE-2026-54857) | Critical | 9.8 | Unauthenticated PHP Object Injection in Quirky <= 1.23 versions. |
| 2026-10-29 16:18:09 | [CVE-2026-54858](https://nvd.nist.gov/vuln/detail/CVE-2026-54858) | Critical | 9.8 | Unauthenticated PHP Object Injection in Printy <= 1.13.0 versions. |
| 2026-10-29 16:18:10 | [CVE-2026-54859](https://nvd.nist.gov/vuln/detail/CVE-2026-54859) | Critical | 9.8 | Unauthenticated PHP Object Injection in Preservation <= 1.15 versions. |
| 2026-10-29 16:18:10 | [CVE-2026-54860](https://nvd.nist.gov/vuln/detail/CVE-2026-54860) | Critical | 9.8 | Unauthenticated PHP Object Injection in Ozisti <= 1.1.10 versions. |
| 2026-10-29 16:18:10 | [CVE-2026-54864](https://nvd.nist.gov/vuln/detail/CVE-2026-54864) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in Post Video Players <= 1.165 versions. |
| 2026-10-29 16:18:10 | [CVE-2026-54865](https://nvd.nist.gov/vuln/detail/CVE-2026-54865) | Medium | 6.5 | Subscriber Cross Site Scripting (XSS) in Podamibe Custom User Gravatar <= 1.0.8 versions. |
| 2026-10-29 16:18:10 | [CVE-2026-54866](https://nvd.nist.gov/vuln/detail/CVE-2026-54866) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in Razorpay Payment Button Elementor Plugin <= 1.2.8 versions. |
| 2026-10-29 16:18:11 | [CVE-2026-61988](https://nvd.nist.gov/vuln/detail/CVE-2026-61988) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in Auction Nudge – Your eBay on Your Site <= 8.4.0 versions. |
| 2026-10-29 16:18:11 | [CVE-2026-61989](https://nvd.nist.gov/vuln/detail/CVE-2026-61989) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in Easy Property Listings <= 3.5.25 versions. |
| 2026-10-29 16:18:11 | [CVE-2026-61991](https://nvd.nist.gov/vuln/detail/CVE-2026-61991) | Critical | 10.0 | Unauthenticated Remote Code Execution (RCE) in AjaxLoadMore Cache <= 3.1.1 versions. |
| 2026-10-29 16:18:11 | [CVE-2026-61992](https://nvd.nist.gov/vuln/detail/CVE-2026-61992) | Critical | 9.8 | Unauthenticated PHP Object Injection in GEO my WordPress <= 4.5.5.3 versions. |
| 2026-10-29 16:18:12 | [CVE-2026-61993](https://nvd.nist.gov/vuln/detail/CVE-2026-61993) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in Blockonomics 3.11.0 versions. |
| 2026-10-29 16:18:12 | [CVE-2026-61995](https://nvd.nist.gov/vuln/detail/CVE-2026-61995) | High | 7.1 | Unauthenticated Cross Site Scripting (XSS) in YouTube Showcase <= 4.1.0 versions. |
| 2026-10-29 16:18:12 | [CVE-2026-61996](https://nvd.nist.gov/vuln/detail/CVE-2026-61996) | High | 8.5 | Subscriber SQL Injection in MLS On The Fly <= 1.8.1.5 versions. |
| 2026-10-29 16:18:12 | [CVE-2026-61997](https://nvd.nist.gov/vuln/detail/CVE-2026-61997) | Critical | 9.8 | Unauthenticated PHP Object Injection in Legal Stone <= 1.2.11 versions. |
| 2026-10-29 16:18:12 | [CVE-2026-61998](https://nvd.nist.gov/vuln/detail/CVE-2026-61998) | Critical | 9.8 | Unauthenticated PHP Object Injection in Le Truffe <= 1.1.7 versions. |
| 2026-10-29 16:18:12 | [CVE-2026-62001](https://nvd.nist.gov/vuln/detail/CVE-2026-62001) | Critical | 9.8 | Unauthenticated PHP Object Injection in Marcell <= 1.2.14 versions. |
| 2026-10-29 16:18:12 | [CVE-2026-62002](https://nvd.nist.gov/vuln/detail/CVE-2026-62002) | Critical | 9.8 | Unauthenticated PHP Object Injection in Meals & Wheels <= 1.1.13 versions. |
| 2026-10-29 16:18:12 | [CVE-2026-62003](https://nvd.nist.gov/vuln/detail/CVE-2026-62003) | Critical | 9.8 | Unauthenticated PHP Object Injection in Mission <= 1.22 versions. |
| 2026-10-29 16:18:13 | [CVE-2026-62004](https://nvd.nist.gov/vuln/detail/CVE-2026-62004) | Critical | 9.8 | Unauthenticated PHP Object Injection in Motorix <= 1.11 versions. |
| 2026-10-29 16:18:13 | [CVE-2026-62005](https://nvd.nist.gov/vuln/detail/CVE-2026-62005) | Critical | 9.8 | Unauthenticated PHP Object Injection in Muzicon <= 1.15 versions. |
| 2026-10-29 16:18:13 | [CVE-2026-62006](https://nvd.nist.gov/vuln/detail/CVE-2026-62006) | Critical | 9.8 | Unauthenticated PHP Object Injection in Nuts <= 1.12 versions. |
| 2026-10-29 16:18:13 | [CVE-2026-62008](https://nvd.nist.gov/vuln/detail/CVE-2026-62008) | Critical | 9.8 | Unauthenticated PHP Object Injection in Orpheus <= 1.8 versions. |
| 2026-10-29 16:18:13 | [CVE-2026-62009](https://nvd.nist.gov/vuln/detail/CVE-2026-62009) | Critical | 9.8 | Unauthenticated PHP Object Injection in Filmax <= 1.1.11 versions. |
| 2026-10-29 16:18:13 | [CVE-2026-62010](https://nvd.nist.gov/vuln/detail/CVE-2026-62010) | Critical | 9.8 | Unauthenticated PHP Object Injection in Avventure <= 1.1.12 versions. |
| 2026-10-29 16:18:13 | [CVE-2026-62011](https://nvd.nist.gov/vuln/detail/CVE-2026-62011) | Critical | 9.8 | Unauthenticated PHP Object Injection in Bonbon <= 1.11 versions. |
| 2026-10-29 16:18:13 | [CVE-2026-62012](https://nvd.nist.gov/vuln/detail/CVE-2026-62012) | Critical | 9.8 | Unauthenticated PHP Object Injection in Coinpress <= 1.0.15 versions. |
| 2026-10-29 16:18:14 | [CVE-2026-62013](https://nvd.nist.gov/vuln/detail/CVE-2026-62013) | Critical | 9.8 | Unauthenticated PHP Object Injection in Edge Decor <= 2.9 versions. |
| 2026-10-29 16:18:14 | [CVE-2026-62014](https://nvd.nist.gov/vuln/detail/CVE-2026-62014) | Critical | 9.8 | Unauthenticated PHP Object Injection in EmojiNation <= 1.0.12 versions. |
| 2026-10-29 16:18:14 | [CVE-2026-62015](https://nvd.nist.gov/vuln/detail/CVE-2026-62015) | Critical | 9.8 | Unauthenticated PHP Object Injection in Gamezone <= 1.1.11 versions. |
| 2026-10-29 16:18:14 | [CVE-2026-62016](https://nvd.nist.gov/vuln/detail/CVE-2026-62016) | Critical | 9.8 | Unauthenticated PHP Object Injection in Gamic <= 1.19 versions. |
| 2026-10-29 16:18:14 | [CVE-2026-62017](https://nvd.nist.gov/vuln/detail/CVE-2026-62017) | Critical | 9.8 | Unauthenticated PHP Object Injection in Good Homes <= 1.3.13 versions. |
| 2026-10-29 16:18:14 | [CVE-2026-62018](https://nvd.nist.gov/vuln/detail/CVE-2026-62018) | Critical | 9.8 | Unauthenticated PHP Object Injection in Gunslinger <= 1.11 versions. |
| 2026-10-29 16:18:14 | [CVE-2026-62131](https://nvd.nist.gov/vuln/detail/CVE-2026-62131) | Critical | 9.8 | Unauthenticated PHP Object Injection in Zoho Flow <= 2.14.5 versions. |
| 2026-10-29 16:18:15 | [CVE-2026-66911](https://nvd.nist.gov/vuln/detail/CVE-2026-66911) | Medium | 5.3 | Zimbra is vulnerable to stored cross-site scripting (XSS) via the Content-Location MIME header in email attachments. Du… |
| 2026-10-29 16:18:15 | [CVE-2026-66912](https://nvd.nist.gov/vuln/detail/CVE-2026-66912) | Medium | 5.3 | Zimbra is vulnerable to Stored Cross-Site Scripting (XSS) via the From email header during HTML reply composition in Cl… |
| 2026-10-29 16:18:52 | [CVE-2026-77817](https://nvd.nist.gov/vuln/detail/CVE-2026-77817) | Medium | 6.5 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to obtain sensitive information due t… |
| 2026-10-29 16:18:52 | [CVE-2026-77819](https://nvd.nist.gov/vuln/detail/CVE-2026-77819) | Medium | 6.5 | IBM Langflow OSS 1.0.0 through 1.12.3 could allow a remote authenticated attacker to overwrite arbitrary files due to i… |
| 2026-10-29 16:19:29 | [CVE-2026-84294](https://nvd.nist.gov/vuln/detail/CVE-2026-84294) | High | 7.7 | Improper limitation of pathname in the Ad Hoc Transfer component of Progress Software WS_FTP Server versions prior to 2… |
| 2026-10-29 16:19:29 | [CVE-2026-84295](https://nvd.nist.gov/vuln/detail/CVE-2026-84295) | Critical | 10.0 | Improper authentication in Progress Software WS_FTP Server versions prior to 2024.0.6 and 2025.0.3 on Windows could all… |
| 2026-10-29 16:19:29 | [CVE-2026-84296](https://nvd.nist.gov/vuln/detail/CVE-2026-84296) | Medium | 6.8 | Multi-Factor Authentication Bypass vulnerability in SSH component in Progress Software WS_FTP Server versions prior to… |
| 2026-10-29 16:19:31 | [CVE-2026-85330](https://nvd.nist.gov/vuln/detail/CVE-2026-85330) | Medium | 4.3 | Incorrect authorization in Microsoft Edge for Android allows an unauthorized attacker to bypass a security feature over… |
| 2026-10-29 16:19:45 | [CVE-2026-85890](https://nvd.nist.gov/vuln/detail/CVE-2026-85890) | High | 8.8 | Double free in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a network. |
| 2026-10-29 16:19:45 | [CVE-2026-85897](https://nvd.nist.gov/vuln/detail/CVE-2026-85897) | High | 8.8 | Heap-based buffer overflow in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a ne… |
| 2026-10-29 16:19:45 | [CVE-2026-85899](https://nvd.nist.gov/vuln/detail/CVE-2026-85899) | High | 8.1 | Use after free in Microsoft Edge (Chromium-based) allows an authorized attacker to elevate privileges over a network. |
| 2026-10-29 16:19:52 | [CVE-2026-88077](https://nvd.nist.gov/vuln/detail/CVE-2026-88077) | High | 8.8 | Integer overflow or wraparound in Microsoft Edge (Chromium-based) allows an unauthorized attacker to elevate privileges… |
| 2026-10-29 16:19:53 | [CVE-2026-88078](https://nvd.nist.gov/vuln/detail/CVE-2026-88078) | Medium | 4.3 | Improper verification of cryptographic signature in Microsoft Edge (Chromium-based) allows an unauthorized attacker to… |
| 2026-10-29 16:19:54 | [CVE-2026-88090](https://nvd.nist.gov/vuln/detail/CVE-2026-88090) | Medium | 5.4 | Access of resource using incompatible type ('type confusion') in Microsoft Edge (Chromium-based) allows an unauthorized… |
| 2026-10-29 16:20:04 | [CVE-2026-90861](https://nvd.nist.gov/vuln/detail/CVE-2026-90861) | Medium | 6.6 | Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Windows may expose a user's password in clea… |
| 2026-10-29 16:20:04 | [CVE-2026-90862](https://nvd.nist.gov/vuln/detail/CVE-2026-90862) | Medium | 4.3 | Improper authentication in the Web Transfer Module of Progress Software WS_FTP Server versions prior to 2024.0.7 and 20… |
| 2026-10-29 16:20:04 | [CVE-2026-90863](https://nvd.nist.gov/vuln/detail/CVE-2026-90863) | Critical | 9.1 | Missing authorization in the administrative interface of Progress Software WS_FTP Server versions prior to 2024.0.7 and… |
| 2026-10-29 16:20:04 | [CVE-2026-90864](https://nvd.nist.gov/vuln/detail/CVE-2026-90864) | Critical | 9.1 | A path traversal vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Windows co… |
| 2026-10-29 16:20:04 | [CVE-2026-90865](https://nvd.nist.gov/vuln/detail/CVE-2026-90865) | Critical | 9.0 | An OS command injection vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Win… |
| 2026-10-29 16:20:04 | [CVE-2026-90866](https://nvd.nist.gov/vuln/detail/CVE-2026-90866) | Critical | 9.1 | A path traversal vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Windows co… |
| 2026-10-29 16:20:04 | [CVE-2026-90867](https://nvd.nist.gov/vuln/detail/CVE-2026-90867) | High | 8.1 | Improper access control in the Web Admin console of Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025… |
| 2026-10-29 16:20:04 | [CVE-2026-90868](https://nvd.nist.gov/vuln/detail/CVE-2026-90868) | Critical | 9.9 | An OS command injection vulnerability in Progress Software WS_FTP Server versions prior to 2024.0.7 and 2025.0.4 on Win… |
| 2026-10-29 16:20:05 | [CVE-2026-90869](https://nvd.nist.gov/vuln/detail/CVE-2026-90869) | High | 7.5 | A remote attacker who knows a valid account's enrolled SSH public key can terminate the shared SSH service in Progress… |
| 2026-10-29 16:20:05 | [CVE-2026-90870](https://nvd.nist.gov/vuln/detail/CVE-2026-90870) | Medium | 5.3 | A missing release of backend receiver sessions in the Ad Hoc Transfer component of Progress Software WS_FTP Server vers… |
| 2026-10-29 16:20:05 | [CVE-2026-90871](https://nvd.nist.gov/vuln/detail/CVE-2026-90871) | Medium | 5.3 | Improper limitation of a pathname to a restricted directory in Progress Software WS_FTP Server versions prior to 2024.0… |
| 2026-10-29 16:20:05 | [CVE-2026-90872](https://nvd.nist.gov/vuln/detail/CVE-2026-90872) | Medium | 6.6 | Improper neutralization of directives in dynamically evaluated code in the Manager web console of Progress Software WS_… |
| 2026-10-29 16:20:05 | [CVE-2026-90991](https://nvd.nist.gov/vuln/detail/CVE-2026-90991) | Medium | 6.5 | IBM Langflow OSS 1.0.0 through 1.12.4 could allow a remote authenticated attacker to cause a denial of service due to a… |
| 2026-10-29 16:20:05 | [CVE-2026-93570](https://nvd.nist.gov/vuln/detail/CVE-2026-93570) | High | 8.2 | Szafir and Szafir Weryfikująca are vulnerable to XML External Entity (XXE) injection. When a user signs or verify a cra… |
| 2026-10-29 16:20:05 | [CVE-2026-93571](https://nvd.nist.gov/vuln/detail/CVE-2026-93571) | Low | 2.3 | Szafir is vulnerable to Path Traversal in the uploaded filename. A man-in-the-middle attacker who can reroute update re… |
| 2026-10-29 16:20:06 | [CVE-2026-93680](https://nvd.nist.gov/vuln/detail/CVE-2026-93680) | Critical | 9.8 | IBM Langflow OSS 1.0.0 through 1.12.8 could allow a remote attacker to bypass security restrictions due to improper aut… |
| 2026-10-29 16:20:08 | [CVE-2026-96187](https://nvd.nist.gov/vuln/detail/CVE-2026-96187) | High | 7.4 | Access of resource using incompatible type ('type confusion') in Microsoft Edge (Chromium-based) allows an unauthorized… |
| 2026-10-29 16:20:08 | [CVE-2026-96192](https://nvd.nist.gov/vuln/detail/CVE-2026-96192) | High | 8.8 | Use after free in Microsoft Edge for iOS allows an unauthorized attacker to execute code over a network. |
| 2026-10-29 16:20:08 | [CVE-2026-96196](https://nvd.nist.gov/vuln/detail/CVE-2026-96196) | High | 8.8 | Incomplete list of disallowed inputs in Microsoft Edge (Chromium-based) allows an unauthorized attacker to bypass a sec… |
| 2026-10-29 16:20:08 | [CVE-2026-96198](https://nvd.nist.gov/vuln/detail/CVE-2026-96198) | High | 8.8 | Heap-based buffer overflow in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a ne… |
| 2026-10-29 16:20:08 | [CVE-2026-96199](https://nvd.nist.gov/vuln/detail/CVE-2026-96199) | High | 8.8 | Heap-based buffer overflow in Microsoft Edge (Chromium-based) allows an unauthorized attacker to execute code over a ne… |
| 2026-10-29 16:20:09 | [CVE-2026-96203](https://nvd.nist.gov/vuln/detail/CVE-2026-96203) | High | 8.8 | Use after free in Microsoft Edge (Chromium-based) allows an unauthorized attacker to elevate privileges over a network. |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
