# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-16 12:18 UTC

New CVEs published between 2026-11-16 11:18 UTC and 2026-11-16 12:18 UTC.

[Full CSV](data/new-cves-2026-11-16T12-18-43-493077Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-16 12:17:41 | [CVE-2026-110941](https://nvd.nist.gov/vuln/detail/CVE-2026-110941) | Medium | 6.8 | Mattermost Desktop App versions <=6.3 6.0.3 6.3.2.0 fail to monitor secondary browser windows in the local network acce… |
| 2026-11-16 12:17:43 | [CVE-2026-116288](https://nvd.nist.gov/vuln/detail/CVE-2026-116288) | High | 8.6 | In affected versions of Octopus Server, a user with permission to edit team scoped roles could escalate their privilege… |
| 2026-11-16 12:17:46 | [CVE-2026-123745](https://nvd.nist.gov/vuln/detail/CVE-2026-123745) | Medium | 6.1 | In affected versions of Octopus Server, improper path validation allowed a user with scoped runbook permissions to exec… |
| 2026-11-16 12:17:46 | [CVE-2026-124629](https://nvd.nist.gov/vuln/detail/CVE-2026-124629) | Medium | 5.3 | In affected versions of Octopus Server, insufficient authorization checks on scheduled project triggers allowed users w… |
| 2026-11-16 12:17:46 | [CVE-2026-124631](https://nvd.nist.gov/vuln/detail/CVE-2026-124631) | Medium | 5.3 | In affected versions of Octopus Server, insufficient authorization checks allowed a low-privileged authenticated user t… |
| 2026-11-16 12:17:52 | [CVE-2026-129545](https://nvd.nist.gov/vuln/detail/CVE-2026-129545) | High | 8.7 | Kalmia through 0.2.0 contains a privilege escalation vulnerability that allows low-privileged authenticated users to mo… |
| 2026-11-16 12:17:52 | [CVE-2026-129546](https://nvd.nist.gov/vuln/detail/CVE-2026-129546) | High | 7.1 | Kalmia through 0.2.0 contains an information disclosure vulnerability that allows authenticated read-only users to retr… |
| 2026-11-16 12:17:52 | [CVE-2026-129547](https://nvd.nist.gov/vuln/detail/CVE-2026-129547) | High | 8.7 | Kalmia through 0.2.0 contains an authentication bypass vulnerability in RsPressMiddleware that allows unauthenticated a… |
| 2026-11-16 12:17:52 | [CVE-2026-129548](https://nvd.nist.gov/vuln/detail/CVE-2026-129548) | Medium | 5.1 | Kalmia through 0.2.0 contains a stored cross-site scripting vulnerability that allows read-only authenticated users to… |
| 2026-11-16 12:17:52 | [CVE-2026-129549](https://nvd.nist.gov/vuln/detail/CVE-2026-129549) | Medium | 5.3 | Tensei through 0.11.5 contains an unrestricted file upload vulnerability in the @tensei/media plugin that allows unauth… |
| 2026-11-16 12:17:53 | [CVE-2026-129550](https://nvd.nist.gov/vuln/detail/CVE-2026-129550) | Critical | 9.3 | Tensei through 0.11.5 contains a privilege escalation vulnerability in @tensei/auth that allows unauthenticated or auth… |
| 2026-11-16 12:17:53 | [CVE-2026-129551](https://nvd.nist.gov/vuln/detail/CVE-2026-129551) | Medium | 6.9 | Tensei through 0.11.5 contains a prototype pollution vulnerability in parseSortFromStringToObject of @tensei/rest that… |
| 2026-11-16 12:17:53 | [CVE-2026-129552](https://nvd.nist.gov/vuln/detail/CVE-2026-129552) | Critical | 9.3 | Tensei through 0.11.5 contains an authentication bypass vulnerability in @tensei/auth that falls back to the hard-coded… |
| 2026-11-16 12:17:53 | [CVE-2026-129553](https://nvd.nist.gov/vuln/detail/CVE-2026-129553) | Medium | 5.3 | Tensei through 0.11.5 contains an open redirect vulnerability in the @tensei/social-auth SocialAuthCallbackController t… |
| 2026-11-16 12:17:53 | [CVE-2026-15707](https://nvd.nist.gov/vuln/detail/CVE-2026-15707) | High | 8.5 | An uncontrolled search path vulnerability (CWE-427) in statically linked OpenSSL libraries within Netskope Client (stAg… |
| 2026-11-16 12:17:53 | [CVE-2026-21141](https://nvd.nist.gov/vuln/detail/CVE-2026-21141) | Medium | 6.9 | Improper access control in Samsung Dialer prior to SMR Nov-2026 Release 1 allows local attackers to access sensitive in… |
| 2026-11-16 12:17:53 | [CVE-2026-21142](https://nvd.nist.gov/vuln/detail/CVE-2026-21142) | Low | 2.1 | Incorrect default permissions in Samsung Contacts prior to SMR Nov-2026 Release 1 allows local attackers to access prof… |
| 2026-11-16 12:17:54 | [CVE-2026-21143](https://nvd.nist.gov/vuln/detail/CVE-2026-21143) | Medium | 5.1 | Improper authorization in CoverScreenRecentsWidgetProvider in Samsung Contacts prior to SMR Nov-2026 Release 1 allows l… |
| 2026-11-16 12:17:54 | [CVE-2026-21144](https://nvd.nist.gov/vuln/detail/CVE-2026-21144) | Medium | 5.1 | Improper authorization in RecentsCallLogLargeWidgetProvider in Samsung Contacts prior to SMR Nov-2026 Release 1 allows… |
| 2026-11-16 12:17:54 | [CVE-2026-21145](https://nvd.nist.gov/vuln/detail/CVE-2026-21145) | Medium | 4.8 | Improper export of android application components in CoverScreenWidgetActionActivityLarge in Samsung Contacts prior to… |
| 2026-11-16 12:17:55 | [CVE-2026-21146](https://nvd.nist.gov/vuln/detail/CVE-2026-21146) | Medium | 4.8 | Improper export of android application components in CoverScreenWidgetActionActivitySmall in Samsung Contacts prior to… |
| 2026-11-16 12:17:55 | [CVE-2026-21147](https://nvd.nist.gov/vuln/detail/CVE-2026-21147) | Medium | 4.8 | Improper export of android application components in CoverScreenWidgetActionActivity in Samsung Contacts prior to SMR N… |
| 2026-11-16 12:17:55 | [CVE-2026-21148](https://nvd.nist.gov/vuln/detail/CVE-2026-21148) | Medium | 5.1 | Incorrect authorization in Samsung Messages prior to SMR Nov-2026 Release 1 allows local attackers to access sensitive… |
| 2026-11-16 12:17:55 | [CVE-2026-21149](https://nvd.nist.gov/vuln/detail/CVE-2026-21149) | Medium | 6.9 | Improper access control in StatusBarManagerService prior to SMR Nov-2026 Release 1 allows local attackers to use the pr… |
| 2026-11-16 12:17:55 | [CVE-2026-21150](https://nvd.nist.gov/vuln/detail/CVE-2026-21150) | Medium | 5.1 | Improper access control in edmnativehelper prior to SMR Nov-2026 Release 1 allows local attackers to access sensitive i… |
| 2026-11-16 12:17:55 | [CVE-2026-21151](https://nvd.nist.gov/vuln/detail/CVE-2026-21151) | High | 8.3 | Improper privilege management in TransitionPlayer prior to SMR Nov-2026 Release 1 allows local privileged attackers to… |
| 2026-11-16 12:17:55 | [CVE-2026-21152](https://nvd.nist.gov/vuln/detail/CVE-2026-21152) | High | 7.0 | Improper input validation in libMyFilterPlugin.camera.samsung.so prior to SMR Nov-2026 Release 1 allows local attackers… |
| 2026-11-16 12:17:55 | [CVE-2026-21153](https://nvd.nist.gov/vuln/detail/CVE-2026-21153) | High | 7.4 | Stack-based buffer overflow in libsecuibc.so prior to SMR Nov-2026 Release 1 allows local attackers to execute arbitrar… |
| 2026-11-16 12:17:56 | [CVE-2026-21154](https://nvd.nist.gov/vuln/detail/CVE-2026-21154) | Medium | 6.9 | Improper authorization in libsecuibc.so prior to SMR Nov-2026 Release 1 allows local attackers to access dump data. |
| 2026-11-16 12:17:56 | [CVE-2026-21155](https://nvd.nist.gov/vuln/detail/CVE-2026-21155) | Medium | 4.7 | Out-of-bounds write in bootloader prior to SMR Nov-2026 Release 1 allows physical attackers to write out-of-bounds memo… |
| 2026-11-16 12:17:56 | [CVE-2026-21156](https://nvd.nist.gov/vuln/detail/CVE-2026-21156) | Medium | 6.9 | Out-of-bounds write in libsmkvextractor.so prior to SMR Nov-2026 Release 1 allows local attackers to write out-of-bound… |
| 2026-11-16 12:17:56 | [CVE-2026-21158](https://nvd.nist.gov/vuln/detail/CVE-2026-21158) | Medium | 4.3 | Improper certificate validation in CP prior to SMR Nov-2026 Release 1 allows local privileged attackers to bypass SIM l… |
| 2026-11-16 12:17:56 | [CVE-2026-21159](https://nvd.nist.gov/vuln/detail/CVE-2026-21159) | Medium | 6.8 | Improper authorization in Samsung Pass prior to version 5.2.12.7 allows physical attackers to access sensitive informat… |
| 2026-11-16 12:17:56 | [CVE-2026-21160](https://nvd.nist.gov/vuln/detail/CVE-2026-21160) | Medium | 5.3 | Cross-site request forgery in Samsung Health prior to version 7.1.0.053 allows remote attackers to access sensitive inf… |
| 2026-11-16 12:17:56 | [CVE-2026-21161](https://nvd.nist.gov/vuln/detail/CVE-2026-21161) | Medium | 5.1 | Improper input validation in Samsung Members prior to version 5.8.20.31 allows local attackers to launch arbitrary acti… |
| 2026-11-16 12:17:56 | [CVE-2026-21162](https://nvd.nist.gov/vuln/detail/CVE-2026-21162) | Medium | 5.2 | Out-of-bounds write in libiosotglib.so prior to version 3.7.73.4 allows physical attackers to execute arbitrary code. U… |
| 2026-11-16 12:17:57 | [CVE-2026-21163](https://nvd.nist.gov/vuln/detail/CVE-2026-21163) | Medium | 5.3 | Improper input validation in Bixby prior to version 4.1.20 allows remote attackers to launch arbitrary activity with Bi… |
| 2026-11-16 12:17:57 | [CVE-2026-21164](https://nvd.nist.gov/vuln/detail/CVE-2026-21164) | Medium | 5.1 | Improper handling of insufficient permission in Samsung Pay for Galaxy Watch prior to version 8.0.53 allows local attac… |
| 2026-11-16 12:17:57 | [CVE-2026-21165](https://nvd.nist.gov/vuln/detail/CVE-2026-21165) | Medium | 6.0 | Insufficient session expiration in Smart Switch prior to version 3.7.74.7 allows adjacent attackers to bypass device au… |
| 2026-11-16 12:17:57 | [CVE-2026-21166](https://nvd.nist.gov/vuln/detail/CVE-2026-21166) | Medium | 6.9 | Improper authentication in Smart Switch prior to version 3.7.74.7 allows adjacent attackers to install arbitrary applic… |
| 2026-11-16 12:17:57 | [CVE-2026-21167](https://nvd.nist.gov/vuln/detail/CVE-2026-21167) | High | 8.6 | Binding to an unrestricted IP address in Smart Switch prior to version 3.7.74.7 allows adjacent attackers to bypass aut… |
| 2026-11-16 12:17:57 | [CVE-2026-21168](https://nvd.nist.gov/vuln/detail/CVE-2026-21168) | Medium | 5.1 | External control of system or configuration setting in Smart Switch prior to version 3.7.74.7 allows local attackers to… |
| 2026-11-16 12:17:57 | [CVE-2026-21169](https://nvd.nist.gov/vuln/detail/CVE-2026-21169) | Medium | 5.3 | Improper input validation in Smart Switch prior to version 3.7.74.1 allows adjacent attackers to install arbitrary appl… |
| 2026-11-16 12:17:57 | [CVE-2026-21170](https://nvd.nist.gov/vuln/detail/CVE-2026-21170) | Medium | 6.1 | Improper enforcement of behavioral workflow in Smart Switch prior to version 3.7.74.7 allows adjacent attackers to writ… |
| 2026-11-16 12:17:58 | [CVE-2026-21171](https://nvd.nist.gov/vuln/detail/CVE-2026-21171) | Medium | 5.8 | Improper initialization in Smart Switch prior to version 3.7.74.7 allows adjacent attackers to bypass user authorizatio… |
| 2026-11-16 12:17:58 | [CVE-2026-21172](https://nvd.nist.gov/vuln/detail/CVE-2026-21172) | Medium | 6.0 | Incomplete cleanup in Smart Switch prior to version 3.7.74.7 allows adjacent attackers to establish an unauthorized con… |
| 2026-11-16 12:17:58 | [CVE-2026-21173](https://nvd.nist.gov/vuln/detail/CVE-2026-21173) | Medium | 6.0 | Improper authorization in Smart Switch prior to version 3.7.74.7 allows adjacent attackers to initiate an unauthorized… |
| 2026-11-16 12:17:58 | [CVE-2026-21174](https://nvd.nist.gov/vuln/detail/CVE-2026-21174) | Medium | 6.0 | Improper access control in Smart Switch prior to version 3.7.74.7 allows adjacent attackers to bypass APK verification. |
| 2026-11-16 12:17:58 | [CVE-2026-21175](https://nvd.nist.gov/vuln/detail/CVE-2026-21175) | High | 8.6 | Incorrect permission assignment for critical resource in Samsung Update prior to version 3.0.111.0 allows local attacke… |
| 2026-11-16 12:17:58 | [CVE-2026-21176](https://nvd.nist.gov/vuln/detail/CVE-2026-21176) | High | 8.6 | Unquoted search path or element in Samsung Device Care prior to version 4.0.80 allows local attackers to execute arbitr… |
| 2026-11-16 12:17:58 | [CVE-2026-21177](https://nvd.nist.gov/vuln/detail/CVE-2026-21177) | Medium | 5.2 | Improper input validation in Settings Suggestions prior to One UI 8.5 allows local attackers to automatically launch an… |
| 2026-11-16 12:17:59 | [CVE-2026-63246](https://nvd.nist.gov/vuln/detail/CVE-2026-63246) | Medium | 5.0 | A kernel pool buffer overflow vulnerability in the ct0531fl.sys file of the Creative WDM Audio Driver (64-bit), Sound B… |
| 2026-11-16 12:17:59 | [CVE-2026-67250](https://nvd.nist.gov/vuln/detail/CVE-2026-67250) | High | 7.3 | A local privilege escalation (LPE) vulnerability in Pebble’s installers could allow a local attacker with low privilege… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
