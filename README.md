# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 03:18 UTC

New CVEs published between 2026-11-02 02:19 UTC and 2026-11-02 03:18 UTC.

[Full CSV](data/new-cves-2026-11-02T03-18-31-140674Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 03:17:28 | [CVE-2026-120309](https://nvd.nist.gov/vuln/detail/CVE-2026-120309) | Medium | 6.3 | Nuxt from 4.6.0 before 4.6.2 contains a route parameter confusion vulnerability in getRouterParam and getRouterParams t… |
| 2026-11-02 03:17:28 | [CVE-2026-120310](https://nvd.nist.gov/vuln/detail/CVE-2026-120310) | Low | 2.3 | Parse Server before 8.6.109 and 9.0.0 before 9.10.6-alpha.1 returns stored field values in object update responses with… |
| 2026-11-02 03:17:28 | [CVE-2026-120311](https://nvd.nist.gov/vuln/detail/CVE-2026-120311) | High | 8.7 | Network-AI from 5.13.4 before 5.15.5 contains a path traversal vulnerability in FileJobStore that allows attackers to r… |
| 2026-11-02 03:17:28 | [CVE-2026-120312](https://nvd.nist.gov/vuln/detail/CVE-2026-120312) | High | 8.7 | Network-AI from 5.13.4 before 5.15.5 contains a path traversal vulnerability in AgentVCR that allows attackers controll… |
| 2026-11-02 03:17:29 | [CVE-2026-120313](https://nvd.nist.gov/vuln/detail/CVE-2026-120313) | High | 8.7 | Network-AI before 5.15.5 contains a path traversal vulnerability in InputSanitizer.sanitizePath() that allows attackers… |
| 2026-11-02 03:17:29 | [CVE-2026-120314](https://nvd.nist.gov/vuln/detail/CVE-2026-120314) | Medium | 6.9 | Network-AI from 5.14.0 before 5.15.5 contains a missing authentication vulnerability in the A2AServer class that allows… |
| 2026-11-02 03:17:29 | [CVE-2026-120315](https://nvd.nist.gov/vuln/detail/CVE-2026-120315) | High | 8.7 | LobeHub Chat from 1.84.26 before 2.1.49 contains a path traversal vulnerability that allows authenticated users to writ… |
| 2026-11-02 03:17:29 | [CVE-2026-120316](https://nvd.nist.gov/vuln/detail/CVE-2026-120316) | High | 8.2 | http4k before 6.62.0.0-ee contains a path traversal vulnerability in ThymeleafTemplates Caching and HotReload that allo… |
| 2026-11-02 03:17:29 | [CVE-2026-120317](https://nvd.nist.gov/vuln/detail/CVE-2026-120317) | High | 8.2 | http4k from 4.9.10.0 before 6.60.0.0 contains a missing integrity check vulnerability because DigestEncoder computes th… |
| 2026-11-02 03:17:30 | [CVE-2026-120324](https://nvd.nist.gov/vuln/detail/CVE-2026-120324) | Medium | 5.5 | A weakness has been identified in Aklivity Zilla up to 1.3.4/2.4.7/2.5.0-rc2. The affected element is the function Path… |
| 2026-11-02 03:17:30 | [CVE-2026-120325](https://nvd.nist.gov/vuln/detail/CVE-2026-120325) | Low | 2.1 | A security vulnerability has been detected in Webpro-nl Knip up to 6.44.0. The impacted element is the function writeFi… |
| 2026-11-02 03:17:30 | [CVE-2026-120334](https://nvd.nist.gov/vuln/detail/CVE-2026-120334) | Low | 2.1 | A flaw has been found in deepset-ai farm up to 0.8.0. This impacts the function EmbeddingTokenizer.from_pretrained of t… |
| 2026-11-02 03:17:30 | [CVE-2026-120335](https://nvd.nist.gov/vuln/detail/CVE-2026-120335) | Low | 0.9 | A vulnerability has been found in deepset-ai farm up to 0.8.0. Affected is the function WordEmbedding_LM.load of the fi… |
| 2026-11-02 03:17:31 | [CVE-2026-20499](https://nvd.nist.gov/vuln/detail/CVE-2026-20499) |  |  | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation o… |
| 2026-11-02 03:17:31 | [CVE-2026-20545](https://nvd.nist.gov/vuln/detail/CVE-2026-20545) |  |  | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation o… |
| 2026-11-02 03:17:31 | [CVE-2026-20546](https://nvd.nist.gov/vuln/detail/CVE-2026-20546) |  |  | In Modem, there is a possible out of bounds write due to an incorrect bounds check. This could lead to remote escalatio… |
| 2026-11-02 03:17:31 | [CVE-2026-20547](https://nvd.nist.gov/vuln/detail/CVE-2026-20547) |  |  | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation o… |
| 2026-11-02 03:17:31 | [CVE-2026-20548](https://nvd.nist.gov/vuln/detail/CVE-2026-20548) |  |  | In Modem, there is a possible out of bounds write due to an integer overflow. This could lead to remote escalation of p… |
| 2026-11-02 03:17:31 | [CVE-2026-20549](https://nvd.nist.gov/vuln/detail/CVE-2026-20549) |  |  | In Modem, there is a possible out of bounds write due to improper input validation. This could lead to remote escalatio… |
| 2026-11-02 03:17:31 | [CVE-2026-20550](https://nvd.nist.gov/vuln/detail/CVE-2026-20550) |  |  | In gnss, there is a possible out of bounds write due to a missing bounds check. This could lead to local denial of serv… |
| 2026-11-02 03:17:32 | [CVE-2026-20551](https://nvd.nist.gov/vuln/detail/CVE-2026-20551) |  |  | In gnss, there is a possible out of bounds write due to a missing bounds check. This could lead to local denial of serv… |
| 2026-11-02 03:17:32 | [CVE-2026-20552](https://nvd.nist.gov/vuln/detail/CVE-2026-20552) |  |  | In ccci, there is a possible out of bounds write due to a missing bounds check. This could lead to remote denial of ser… |
| 2026-11-02 03:17:32 | [CVE-2026-20553](https://nvd.nist.gov/vuln/detail/CVE-2026-20553) |  |  | In DA, there is a possible out of bounds write due to a missing bounds check. This could lead to local escalation of pr… |
| 2026-11-02 03:17:32 | [CVE-2026-20554](https://nvd.nist.gov/vuln/detail/CVE-2026-20554) |  |  | In Modem, there is a possible system crash due to a missing bounds check. This could lead to remote escalation of privi… |
| 2026-11-02 03:17:32 | [CVE-2026-20555](https://nvd.nist.gov/vuln/detail/CVE-2026-20555) |  |  | In Modem, there is a possible out of bounds read due to a missing bounds check. This could lead to remote denial of ser… |
| 2026-11-02 03:17:32 | [CVE-2026-20556](https://nvd.nist.gov/vuln/detail/CVE-2026-20556) |  |  | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation o… |
| 2026-11-02 03:17:32 | [CVE-2026-20557](https://nvd.nist.gov/vuln/detail/CVE-2026-20557) |  |  | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation o… |
| 2026-11-02 03:17:32 | [CVE-2026-20558](https://nvd.nist.gov/vuln/detail/CVE-2026-20558) |  |  | In GPU pdma, there is a possible escalation of privilege due to use after free. This could lead to local escalation of… |
| 2026-11-02 03:17:33 | [CVE-2026-20559](https://nvd.nist.gov/vuln/detail/CVE-2026-20559) |  |  | In GPU pdma, there is a possible memory corruption due to use after free. This could lead to local escalation of privil… |
| 2026-11-02 03:17:33 | [CVE-2026-20560](https://nvd.nist.gov/vuln/detail/CVE-2026-20560) |  |  | In Modem, there is a possible system crash due to improper input validation. This could lead to remote denial of servic… |
| 2026-11-02 03:17:33 | [CVE-2026-20561](https://nvd.nist.gov/vuln/detail/CVE-2026-20561) |  |  | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote denial of se… |
| 2026-11-02 03:17:33 | [CVE-2026-20562](https://nvd.nist.gov/vuln/detail/CVE-2026-20562) |  |  | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote denial of se… |
| 2026-11-02 03:17:33 | [CVE-2026-20563](https://nvd.nist.gov/vuln/detail/CVE-2026-20563) |  |  | In Modem, there is a possible out of bounds write due to an incorrect bounds check. This could lead to remote denial of… |
| 2026-11-02 03:17:33 | [CVE-2026-20564](https://nvd.nist.gov/vuln/detail/CVE-2026-20564) |  |  | In Modem, there is a possible out of bounds write due to an incorrect bounds check. This could lead to local denial of… |
| 2026-11-02 03:17:33 | [CVE-2026-20565](https://nvd.nist.gov/vuln/detail/CVE-2026-20565) |  |  | In Modem, there is a possible out of bounds write due to an incorrect bounds check. This could lead to local escalation… |
| 2026-11-02 03:17:33 | [CVE-2026-20566](https://nvd.nist.gov/vuln/detail/CVE-2026-20566) |  |  | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote denial of se… |
| 2026-11-02 03:17:34 | [CVE-2026-20567](https://nvd.nist.gov/vuln/detail/CVE-2026-20567) |  |  | In afe, there is a possible out of bounds write due to a missing bounds check. This could lead to local escalation of p… |
| 2026-11-02 03:17:34 | [CVE-2026-20568](https://nvd.nist.gov/vuln/detail/CVE-2026-20568) |  |  | In afe, there is a possible system crash due to use after free. This could lead to local escalation of privilege if a m… |
| 2026-11-02 03:17:34 | [CVE-2026-20569](https://nvd.nist.gov/vuln/detail/CVE-2026-20569) |  |  | In adsp, there is a possible memory corruption due to use after free. This could lead to local escalation of privilege… |
| 2026-11-02 03:17:34 | [CVE-2026-20570](https://nvd.nist.gov/vuln/detail/CVE-2026-20570) |  |  | In adsp, there is a possible escalation of privilege due to use after free. This could lead to local escalation of priv… |
| 2026-11-02 03:17:34 | [CVE-2026-20571](https://nvd.nist.gov/vuln/detail/CVE-2026-20571) |  |  | In afe, there is a possible memory corruption due to use after free. This could lead to local escalation of privilege i… |
| 2026-11-02 03:17:34 | [CVE-2026-20572](https://nvd.nist.gov/vuln/detail/CVE-2026-20572) |  |  | In adsp, there is a possible out of bounds write due to an integer overflow. This could lead to local escalation of pri… |
| 2026-11-02 03:17:34 | [CVE-2026-20573](https://nvd.nist.gov/vuln/detail/CVE-2026-20573) |  |  | In afe, there is a possible memory corruption due to double free. This could lead to local escalation of privilege if a… |
| 2026-11-02 03:17:35 | [CVE-2026-20574](https://nvd.nist.gov/vuln/detail/CVE-2026-20574) |  |  | In afe, there is a possible memory corruption due to use after free. This could lead to local escalation of privilege i… |
| 2026-11-02 03:17:35 | [CVE-2026-20575](https://nvd.nist.gov/vuln/detail/CVE-2026-20575) |  |  | In afe, there is a possible memory corruption due to use after free. This could lead to local escalation of privilege i… |
| 2026-11-02 03:17:35 | [CVE-2026-20576](https://nvd.nist.gov/vuln/detail/CVE-2026-20576) |  |  | In afe, there is a possible out of bounds write due to a missing bounds check. This could lead to local escalation of p… |
| 2026-11-02 03:17:35 | [CVE-2026-20577](https://nvd.nist.gov/vuln/detail/CVE-2026-20577) |  |  | In Modem, there is a possible permission bypass due to a permissions bypass. This could lead to local denial of service… |
| 2026-11-02 03:17:35 | [CVE-2026-20578](https://nvd.nist.gov/vuln/detail/CVE-2026-20578) |  |  | In Modem, there is a possible information disclosure due to side channel information disclosure. This could lead to rem… |
| 2026-11-02 03:17:35 | [CVE-2026-20580](https://nvd.nist.gov/vuln/detail/CVE-2026-20580) |  |  | In usb, there is a possible system crash due to use after free. This could lead to local denial of service if a malicio… |
| 2026-11-02 03:17:35 | [CVE-2026-20581](https://nvd.nist.gov/vuln/detail/CVE-2026-20581) |  |  | In usb, there is a possible memory corruption due to use after free. This could lead to local escalation of privilege i… |
| 2026-11-02 03:17:35 | [CVE-2026-20582](https://nvd.nist.gov/vuln/detail/CVE-2026-20582) |  |  | In usb, there is a possible memory corruption due to double free. This could lead to local escalation of privilege if a… |
| 2026-11-02 03:17:36 | [CVE-2026-20583](https://nvd.nist.gov/vuln/detail/CVE-2026-20583) |  |  | In usb, there is a possible system crash due to use after free. This could lead to local denial of service if a malicio… |
| 2026-11-02 03:17:36 | [CVE-2026-20584](https://nvd.nist.gov/vuln/detail/CVE-2026-20584) |  |  | In usb, there is a possible memory corruption due to a missing bounds check. This could lead to local escalation of pri… |
| 2026-11-02 03:17:36 | [CVE-2026-20585](https://nvd.nist.gov/vuln/detail/CVE-2026-20585) |  |  | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to remote escalation o… |
| 2026-11-02 03:17:36 | [CVE-2026-20590](https://nvd.nist.gov/vuln/detail/CVE-2026-20590) |  |  | In display, there is a possible system crash due to a logic error. This could lead to local denial of service if a mali… |
| 2026-11-02 03:17:36 | [CVE-2026-20591](https://nvd.nist.gov/vuln/detail/CVE-2026-20591) |  |  | In GPU pdma, there is a possible escalation of privilege due to a missing permission check. This could lead to local es… |
| 2026-11-02 03:17:36 | [CVE-2026-20592](https://nvd.nist.gov/vuln/detail/CVE-2026-20592) |  |  | In Modem, there is a possible information disclosure due to side channel information disclosure. This could lead to loc… |
| 2026-11-02 03:17:36 | [CVE-2026-20593](https://nvd.nist.gov/vuln/detail/CVE-2026-20593) |  |  | In Modem, there is a possible application crash due to improper input validation. This could lead to remote denial of s… |
| 2026-11-02 03:17:36 | [CVE-2026-20594](https://nvd.nist.gov/vuln/detail/CVE-2026-20594) |  |  | In Modem, there is a possible out of bounds read due to a missing bounds check. This could lead to remote denial of ser… |
| 2026-11-02 03:17:37 | [CVE-2026-20595](https://nvd.nist.gov/vuln/detail/CVE-2026-20595) |  |  | In neuropilot, there is a possible out of bounds write due to a missing bounds check. This could lead to local escalati… |
| 2026-11-02 03:17:37 | [CVE-2026-20596](https://nvd.nist.gov/vuln/detail/CVE-2026-20596) |  |  | In Modem, there is a possible out of bounds read due to improper input validation. This could lead to remote denial of… |
| 2026-11-02 03:17:37 | [CVE-2026-20597](https://nvd.nist.gov/vuln/detail/CVE-2026-20597) |  |  | In Modem, there is a possible out of bounds read due to a missing bounds check. This could lead to remote denial of ser… |
| 2026-11-02 03:17:37 | [CVE-2026-20598](https://nvd.nist.gov/vuln/detail/CVE-2026-20598) |  |  | In Modem, there is a possible out of bounds read due to an integer overflow. This could lead to remote denial of servic… |
| 2026-11-02 03:17:37 | [CVE-2026-20599](https://nvd.nist.gov/vuln/detail/CVE-2026-20599) |  |  | In Modem, there is a possible escalation of privilege due to a missing permission check. This could lead to local escal… |
| 2026-11-02 03:17:37 | [CVE-2026-20600](https://nvd.nist.gov/vuln/detail/CVE-2026-20600) |  |  | In Modem, there is a possible application crash due to a logic error. This could lead to remote denial of service, if a… |
| 2026-11-02 03:17:37 | [CVE-2026-68588](https://nvd.nist.gov/vuln/detail/CVE-2026-68588) |  |  | In Modem, there is a possible way (for XXX) to XXXXX due to an integer overflow. This could lead to remote denial of se… |
| 2026-11-02 03:17:38 | [CVE-2026-68589](https://nvd.nist.gov/vuln/detail/CVE-2026-68589) |  |  | In Modem, there is a possible out of bounds write due to a missing bounds check. This could lead to local escalation of… |
| 2026-11-02 03:17:38 | [CVE-2026-68590](https://nvd.nist.gov/vuln/detail/CVE-2026-68590) |  |  | In ip_stack, there is a possible out of bounds read due to improper input validation. This could lead to remote denial… |
| 2026-11-02 03:17:38 | [CVE-2026-68591](https://nvd.nist.gov/vuln/detail/CVE-2026-68591) |  |  | In Modem, there is a possible escalation of privilege due to a permissions bypass. This could lead to local escalation… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
