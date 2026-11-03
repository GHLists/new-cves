# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-03 14:18 UTC

New CVEs published between 2026-11-03 13:19 UTC and 2026-11-03 14:18 UTC.

[Full CSV](data/new-cves-2026-11-03T14-18-55-177323Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-03 14:17:33 | [CVE-2026-119179](https://nvd.nist.gov/vuln/detail/CVE-2026-119179) | High | 8.3 | A flaw in the connection management layer of the MongoDB Node.js driver can leave a pooled network connection in the po… |
| 2026-11-03 14:17:34 | [CVE-2026-119742](https://nvd.nist.gov/vuln/detail/CVE-2026-119742) | High | 8.6 | Nagios XI before 2026R2 contains an OS command injection vulnerability in the MIB upload feature where the install_mib(… |
| 2026-11-03 14:17:35 | [CVE-2026-120572](https://nvd.nist.gov/vuln/detail/CVE-2026-120572) |  |  | Incorrect boundary conditions in the Layout: Block and Inline component. This vulnerability was fixed in Firefox 159.0.… |
| 2026-11-03 14:17:38 | [CVE-2026-85032](https://nvd.nist.gov/vuln/detail/CVE-2026-85032) | Medium | 4.8 | The MCTP over USB device class in subsys/pmci/mctp/mctp_usb.c splits RX handling across two threads: the system workque… |
| 2026-11-03 14:17:38 | [CVE-2026-85033](https://nvd.nist.gov/vuln/detail/CVE-2026-85033) | Medium | 4.6 | The AVRCP Target role in subsys/bluetooth/host/classic/avrcp.c keeps its vendor-dependent response transmit state in a… |
| 2026-11-03 14:17:39 | [CVE-2026-85034](https://nvd.nist.gov/vuln/detail/CVE-2026-85034) | Medium | 6.7 | The Bluetooth host's GATT client passed the value of a received Handle Value Notification, Handle Value Indication or M… |
| 2026-11-03 14:17:39 | [CVE-2026-85035](https://nvd.nist.gov/vuln/detail/CVE-2026-85035) | High | 8.8 | The can_add_rx_filter_msgq() system call installs a CAN RX filter whose callback (can_msgq_put() in drivers/can/can_com… |
| 2026-11-03 14:17:39 | [CVE-2026-89295](https://nvd.nist.gov/vuln/detail/CVE-2026-89295) |  |  | In Eclipse Mnestix AAS Generator versions 0.1.0 up until but excluding 1.5.0, a practical upper bound on the client-sup… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
