# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-01 22:18 UTC

New CVEs published between 2026-11-01 21:18 UTC and 2026-11-01 22:18 UTC.

[Full CSV](data/new-cves-2026-11-01T22-18-28-733238Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-01 22:17:46 | [CVE-2026-82115](https://nvd.nist.gov/vuln/detail/CVE-2026-82115) | Medium | 6.3 | Missing authorization in Apache Wicket. org.apache.wicket.protocol.ws.api.WebSocketMessageBroadcastHandler, the request… |
| 2026-11-01 22:17:46 | [CVE-2026-82557](https://nvd.nist.gov/vuln/detail/CVE-2026-82557) | Medium | 6.9 | Missing authorization in Apache Wicket. org.apache.wicket.markup.html.form.Form resolves the component that submitted a… |
| 2026-11-01 22:17:47 | [CVE-2026-82558](https://nvd.nist.gov/vuln/detail/CVE-2026-82558) | Low | 2.3 | Missing authorization in Apache Wicket. org.apache.wicket.protocol.ws.api.WebSocketBehavior, through which Wicket's nat… |
| 2026-11-01 22:17:47 | [CVE-2026-82559](https://nvd.nist.gov/vuln/detail/CVE-2026-82559) | Low | 2.3 | Insufficient session expiration in Apache Wicket. org.apache.wicket.protocol.ws.WebSocketSettings#newWebSocketRequest()… |
| 2026-11-01 22:17:47 | [CVE-2026-82704](https://nvd.nist.gov/vuln/detail/CVE-2026-82704) | Medium | 6.9 | Missing authorization in Apache Wicket. org.apache.wicket.core.request.handler.ListenerRequestHandler invokes an IReque… |
| 2026-11-01 22:17:47 | [CVE-2026-82705](https://nvd.nist.gov/vuln/detail/CVE-2026-82705) | Medium | 6.3 | Missing authorization in Apache Wicket. org.apache.wicket.authorization.IAuthorizationStrategy declares isResourceAutho… |
| 2026-11-01 22:17:48 | [CVE-2026-82840](https://nvd.nist.gov/vuln/detail/CVE-2026-82840) | High | 7.2 | Session fixation in Apache Wicket. org.apache.wicket.authroles.authentication.AuthenticatedWebSession is the authentica… |
| 2026-11-01 22:17:48 | [CVE-2026-82898](https://nvd.nist.gov/vuln/detail/CVE-2026-82898) | Low | 2.1 | Incorrect order of security checks in Apache Wicket. org.apache.wicket.protocol.http.ResourceIsolationRequestCycleListe… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
