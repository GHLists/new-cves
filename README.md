# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-21 13:18 UTC

New CVEs published between 2026-11-21 12:20 UTC and 2026-11-21 13:18 UTC.

[Full CSV](data/new-cves-2026-11-21T13-18-46-116695Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-21 13:16:38 | [CVE-2026-129794](https://nvd.nist.gov/vuln/detail/CVE-2026-129794) | High | 8.8 | The EoE fragment reassembly code uses a frame size from the wire as the bound for memcpy into the application receive b… |
| 2026-11-21 13:16:38 | [CVE-2026-129795](https://nvd.nist.gov/vuln/detail/CVE-2026-129795) | Medium | 6.5 | When the last EoE fragment has the TIME_APPEND flag set, the handler subtracts 4 from rxframeoffset to strip the timest… |
| 2026-11-21 13:16:38 | [CVE-2026-129796](https://nvd.nist.gov/vuln/detail/CVE-2026-129796) | High | 8.8 | The CoE SDO download handler for flexible-length objects (VISIBLE_STRING, OCTET_STRING, and similar) does not check tha… |
| 2026-11-21 13:16:39 | [CVE-2026-129797](https://nvd.nist.gov/vuln/detail/CVE-2026-129797) | High | 8.8 | SDO_downloadsegment is called whenever a mailbox frame carries the DOWNLOADSEGREQ command byte, regardless of whether a… |
| 2026-11-21 13:16:39 | [CVE-2026-129798](https://nvd.nist.gov/vuln/detail/CVE-2026-129798) | High | 8.8 | The CoE SDO segmented download handler advances a write pointer by each incoming segment's size but does not track how… |
| 2026-11-21 13:16:39 | [CVE-2026-129799](https://nvd.nist.gov/vuln/detail/CVE-2026-129799) | Medium | 6.5 | A CoE SDO request for index 0xFFFF matches the object list terminator entry instead of returning not-found. The termina… |
| 2026-11-21 13:16:39 | [CVE-2026-129800](https://nvd.nist.gov/vuln/detail/CVE-2026-129800) | Medium | 6.5 | sizeOfPDO, called during state transitions, uses the subindex-0 count of the SM-assign and PDO-mapping objects as loop… |
| 2026-11-21 13:16:39 | [CVE-2026-129801](https://nvd.nist.gov/vuln/detail/CVE-2026-129801) | High | 7.1 | The FoE DATA frame handler computes the payload length from the master-supplied mailbox length field and passes it dire… |
| 2026-11-21 13:16:39 | [CVE-2026-129802](https://nvd.nist.gov/vuln/detail/CVE-2026-129802) | Medium | 4.3 | EOE_set_ip reads each network parameter field (MAC, IP, subnet, gateway, DNS IP, DNS name) from the mailbox payload bef… |
| 2026-11-21 13:16:39 | [CVE-2026-129803](https://nvd.nist.gov/vuln/detail/CVE-2026-129803) | Medium | 4.3 | The CoE entry gate accepts frames with mbxheader.length as low as COE_MINIMUM_LENGTH (8), but a normal SDO Download req… |
| 2026-11-21 13:16:40 | [CVE-2026-129804](https://nvd.nist.gov/vuln/detail/CVE-2026-129804) | Medium | 4.2 | FOE_read and FOE_write store the filename length as uint8_t, truncating it modulo 256. When (mbxheader.length - ESC_FOE… |
| 2026-11-21 13:16:40 | [CVE-2026-129805](https://nvd.nist.gov/vuln/detail/CVE-2026-129805) | Medium | 5.3 | An object dictionary entry can carry write-access flags and still have a NULL data pointer, for example when a constant… |
| 2026-11-21 13:16:40 | [CVE-2026-129806](https://nvd.nist.gov/vuln/detail/CVE-2026-129806) | Medium | 5.3 | The CoE SDO upload handler enters its normal-response path (used for objects longer than 4 bytes) and passes (objd + ns… |
| 2026-11-21 13:16:40 | [CVE-2026-129807](https://nvd.nist.gov/vuln/detail/CVE-2026-129807) | Medium | 6.5 | The FoE file table allows entries to omit a write handler by setting write_function to NULL, making the file read-only.… |
| 2026-11-21 13:16:40 | [CVE-2026-129808](https://nvd.nist.gov/vuln/detail/CVE-2026-129808) | Medium | 6.5 | The EoE receive and transmit paths call the handle_recv_buffer and fetch_send_buffer callbacks without first checking w… |
| 2026-11-21 13:16:40 | [CVE-2026-129809](https://nvd.nist.gov/vuln/detail/CVE-2026-129809) | Medium | 5.3 | ESC_foeprocess can be reached by an incoming mailbox frame before the application calls FOE_config to supply the file t… |
| 2026-11-21 13:16:40 | [CVE-2026-129810](https://nvd.nist.gov/vuln/detail/CVE-2026-129810) | Medium | 5.3 | ESC_eoeprocess and ESC_eoeprocess_tx can be reached before the application calls EOE_config to supply the callback tabl… |
| 2026-11-21 13:16:40 | [CVE-2026-129811](https://nvd.nist.gov/vuln/detail/CVE-2026-129811) | High | 8.8 | The PDO mapping bit lengths stored in the mapping objects are writable by the master via SDO. sizeOfPDO summed them wit… |
| 2026-11-21 13:16:41 | [CVE-2026-129812](https://nvd.nist.gov/vuln/detail/CVE-2026-129812) | Medium | 5.3 | An object dictionary entry that holds a constant has no process data storage and carries a NULL data pointer. sizeOfPDO… |
| 2026-11-21 13:16:41 | [CVE-2026-129813](https://nvd.nist.gov/vuln/detail/CVE-2026-129813) | Medium | 5.3 | The CoE complete-access download handler iterated over all subindices of an object and wrote the master-supplied payloa… |
| 2026-11-21 13:16:41 | [CVE-2026-129814](https://nvd.nist.gov/vuln/detail/CVE-2026-129814) | Low | 3.1 | The SDO Information Get Object Description and Get Entry Description responses copy the object or entry name into the m… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
