# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-17 16:21 UTC

New CVEs published between 2026-11-17 15:18 UTC and 2026-11-17 16:21 UTC.

[Full CSV](data/new-cves-2026-11-17T16-21-20-433234Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-17 16:17:33 | [CVE-2026-100963](https://nvd.nist.gov/vuln/detail/CVE-2026-100963) | High | 8.1 | NVIDIA TensorRT for Linux contains a vulnerability where a user could cause an integer overflow issue. A successful exp… |
| 2026-11-17 16:17:33 | [CVE-2026-100970](https://nvd.nist.gov/vuln/detail/CVE-2026-100970) | Medium | 6.4 | NVIDIA OpenShell for Linux contains a vulnerability in the network policy hot-reload component where a local attacker w… |
| 2026-11-17 16:17:34 | [CVE-2026-100971](https://nvd.nist.gov/vuln/detail/CVE-2026-100971) | High | 8.4 | NVIDIA OpenShell for Linux contains a vulnerability in the L7 path allowlist enforcement component where a local attack… |
| 2026-11-17 16:17:34 | [CVE-2026-100972](https://nvd.nist.gov/vuln/detail/CVE-2026-100972) | High | 8.1 | NVIDIA OpenShell for Linux contains a vulnerability in resource-level authorization for create, read, update, and delet… |
| 2026-11-17 16:17:34 | [CVE-2026-100973](https://nvd.nist.gov/vuln/detail/CVE-2026-100973) | Medium | 6.4 | NVIDIA OpenShell for Linux contains a vulnerability in L7 policy enforcement for HTTP CONNECT tunnels where a local att… |
| 2026-11-17 16:17:34 | [CVE-2026-100974](https://nvd.nist.gov/vuln/detail/CVE-2026-100974) | Medium | 6.7 | NVIDIA OpenShell for Linux contains a vulnerability in the sandbox SSH authentication component where a remote attacker… |
| 2026-11-17 16:17:34 | [CVE-2026-100975](https://nvd.nist.gov/vuln/detail/CVE-2026-100975) | High | 7.6 | NVIDIA OpenShell for Linux contains a vulnerability in the Kubernetes sandbox SSH authentication configuration where a… |
| 2026-11-17 16:17:34 | [CVE-2026-100976](https://nvd.nist.gov/vuln/detail/CVE-2026-100976) | Medium | 5.2 | NVIDIA OpenShell for Linux contains a vulnerability in Kubernetes network policy enforcement where a local attacker wit… |
| 2026-11-17 16:17:34 | [CVE-2026-100977](https://nvd.nist.gov/vuln/detail/CVE-2026-100977) | High | 7.5 | NVIDIA OpenShell for Linux contains a vulnerability in L7 REST policy enforcement where a local attacker with low privi… |
| 2026-11-17 16:17:34 | [CVE-2026-100978](https://nvd.nist.gov/vuln/detail/CVE-2026-100978) | Medium | 6.4 | NVIDIA OpenShell for Linux contains a vulnerability in its gateway-to-sandbox transport where a network attacker positi… |
| 2026-11-17 16:17:35 | [CVE-2026-100979](https://nvd.nist.gov/vuln/detail/CVE-2026-100979) | Medium | 6.6 | NVIDIA OpenShell for Linux contains a vulnerability in its gateway connection-proxy component where an attacker who can… |
| 2026-11-17 16:17:35 | [CVE-2026-100980](https://nvd.nist.gov/vuln/detail/CVE-2026-100980) | High | 7.5 | NVIDIA OpenShell for Linux contains a vulnerability in its command-line diagnostic interface where an attacker could ca… |
| 2026-11-17 16:17:35 | [CVE-2026-100981](https://nvd.nist.gov/vuln/detail/CVE-2026-100981) | Medium | 6.4 | NVIDIA OpenShell for Linux contains a vulnerability in its layer-7 REST proxy where a sandboxed actor could bypass the… |
| 2026-11-17 16:17:35 | [CVE-2026-100982](https://nvd.nist.gov/vuln/detail/CVE-2026-100982) | Medium | 6.5 | NVIDIA OpenShell for Linux contains a vulnerability in its inference-interception request parser where a sandboxed acto… |
| 2026-11-17 16:17:39 | [CVE-2026-121590](https://nvd.nist.gov/vuln/detail/CVE-2026-121590) | Medium | 6.5 | Mattermost Desktop App versions <=6.3 6.0.3 6.3.2.0 fail to validate the SiteURL value returned in a server's client co… |
| 2026-11-17 16:17:39 | [CVE-2026-122055](https://nvd.nist.gov/vuln/detail/CVE-2026-122055) |  |  | ICRTouch PocketTouch version 1.700 build 2025.3726 contains a default socket password set to the literal value password… |
| 2026-11-17 16:17:39 | [CVE-2026-122122](https://nvd.nist.gov/vuln/detail/CVE-2026-122122) |  |  | The order-tracking functionality in ICRTouch ByTable and TouchTakeaway does not adequately verify that a requester is a… |
| 2026-11-17 16:17:40 | [CVE-2026-122125](https://nvd.nist.gov/vuln/detail/CVE-2026-122125) |  |  | ICRTouch ByTable and TouchTakeaway do not consistently implement anti-CSRF protections for state-changing web requests.… |
| 2026-11-17 16:17:40 | [CVE-2026-122141](https://nvd.nist.gov/vuln/detail/CVE-2026-122141) |  |  | The wallet top-up functionality in ICRTouch ByTable and TouchTakeaway does not adequately protect state-changing reques… |
| 2026-11-17 16:17:40 | [CVE-2026-122142](https://nvd.nist.gov/vuln/detail/CVE-2026-122142) |  |  | ICRTouch Commander administrative login interface does not adequately restrict repeated authentication attempts. The in… |
| 2026-11-17 16:17:40 | [CVE-2026-122143](https://nvd.nist.gov/vuln/detail/CVE-2026-122143) |  |  | ICRTouch Commander administrative interface performs security-sensitive operations through HTTP GET requests and includ… |
| 2026-11-17 16:17:40 | [CVE-2026-122145](https://nvd.nist.gov/vuln/detail/CVE-2026-122145) |  |  | ICRTouch PocketTouch version 1.700 build 2025.3726 transmits the POS socket password in plaintext XML over an unencrypt… |
| 2026-11-17 16:17:40 | [CVE-2026-122147](https://nvd.nist.gov/vuln/detail/CVE-2026-122147) |  |  | ICRTouch PocketTouch version 1.700 build 2025.3726 defines hard-coded default values for multiple credential fields, in… |
| 2026-11-17 16:17:40 | [CVE-2026-122149](https://nvd.nist.gov/vuln/detail/CVE-2026-122149) |  |  | The PocketTouch and TouchPoint POS protocol includes a `SAVECONFIG` command that appears capable of overwriting till co… |
| 2026-11-17 16:17:40 | [CVE-2026-122150](https://nvd.nist.gov/vuln/detail/CVE-2026-122150) |  |  | The PocketTouch and TouchPoint POS `CHECKPAYMENT` workflow accepts a caller-supplied clerk number without adequately ve… |
| 2026-11-17 16:17:40 | [CVE-2026-122152](https://nvd.nist.gov/vuln/detail/CVE-2026-122152) |  |  | The ICRTouch white-label TouchTakeaway Cordova applications do not implement certificate or public-key pinning for back… |
| 2026-11-17 16:17:41 | [CVE-2026-122153](https://nvd.nist.gov/vuln/detail/CVE-2026-122153) |  |  | The TouchOffice API `clerkList` endpoint appears to return sensitive clerk authentication data, including clerk PINs an… |
| 2026-11-17 16:17:52 | [CVE-2026-65106](https://nvd.nist.gov/vuln/detail/CVE-2026-65106) | High | 7.8 | NVIDIA Transformer Engine for Linux contains a vulnerability where a user could cause deserialization by loading untrus… |
| 2026-11-17 16:17:52 | [CVE-2026-65167](https://nvd.nist.gov/vuln/detail/CVE-2026-65167) | Medium | 5.5 | NVIDIA TensorRT contains a vulnerability where a user could cause memory allocation with excessive size value by crafti… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
