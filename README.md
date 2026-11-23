# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-23 17:22 UTC

New CVEs published between 2026-11-23 16:19 UTC and 2026-11-23 17:22 UTC.

[Full CSV](data/new-cves-2026-11-23T17-22-06-347659Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-23 17:17:27 | [CVE-2026-101218](https://nvd.nist.gov/vuln/detail/CVE-2026-101218) | High | 8.2 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains an OS Command Injection vulnerability. A high pri… |
| 2026-11-23 17:17:27 | [CVE-2026-101219](https://nvd.nist.gov/vuln/detail/CVE-2026-101219) | High | 7.5 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains a heap based buffer overflow. An unauthenticated… |
| 2026-11-23 17:17:27 | [CVE-2026-103783](https://nvd.nist.gov/vuln/detail/CVE-2026-103783) | High | 8.2 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains an OS Command Injection vulnerability. A high pri… |
| 2026-11-23 17:17:27 | [CVE-2026-103784](https://nvd.nist.gov/vuln/detail/CVE-2026-103784) | Medium | 5.9 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains a Loop with Unreachable Exit Condition ('Infinite… |
| 2026-11-23 17:17:27 | [CVE-2026-103785](https://nvd.nist.gov/vuln/detail/CVE-2026-103785) | Low | 3.7 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains a Stack-based Buffer Overflow vulnerability. An u… |
| 2026-11-23 17:17:27 | [CVE-2026-103786](https://nvd.nist.gov/vuln/detail/CVE-2026-103786) | High | 7.5 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains a null pointer dereference vulnerability. An unau… |
| 2026-11-23 17:17:27 | [CVE-2026-103787](https://nvd.nist.gov/vuln/detail/CVE-2026-103787) | Medium | 4.3 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains an out-of-bounds read vulnerability. An unauthent… |
| 2026-11-23 17:17:28 | [CVE-2026-103788](https://nvd.nist.gov/vuln/detail/CVE-2026-103788) | Critical | 9.6 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains an OS Command Injection vulnerability. An unauthe… |
| 2026-11-23 17:17:28 | [CVE-2026-103789](https://nvd.nist.gov/vuln/detail/CVE-2026-103789) | High | 7.5 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains a heap based buffer overflow. An unauthenticated… |
| 2026-11-23 17:17:28 | [CVE-2026-103790](https://nvd.nist.gov/vuln/detail/CVE-2026-103790) | Medium | 5.3 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains an out-of-bounds write vulnerability. An unauthen… |
| 2026-11-23 17:17:28 | [CVE-2026-103791](https://nvd.nist.gov/vuln/detail/CVE-2026-103791) | High | 7.6 | Dell Enterprise Sonic Distribution, versions prior to 4.6.1, contains an Improper Input Validation vulnerability. An un… |
| 2026-11-23 17:17:31 | [CVE-2026-133469](https://nvd.nist.gov/vuln/detail/CVE-2026-133469) | Critical | 9.8 | XO (Xen Orchestra) is a solution to visualize, manage, backup and delegate your XCP-ng (or XenServer) infrastructure. P… |
| 2026-11-23 17:17:49 | [CVE-2026-134841](https://nvd.nist.gov/vuln/detail/CVE-2026-134841) | High | 8.1 | pgjdbc, the PostgreSQL JDBC Driver, misreads some quoted text in its query parser. A `}` inside a literal ends a JDBC e… |
| 2026-11-23 17:17:49 | [CVE-2026-134842](https://nvd.nist.gov/vuln/detail/CVE-2026-134842) | High | 8.1 | pgjdbc, the PostgreSQL JDBC Driver, can quote a string parameter for the wrong value of standard_conforming_strings whe… |
| 2026-11-23 17:17:49 | [CVE-2026-134843](https://nvd.nist.gov/vuln/detail/CVE-2026-134843) | High | 7.5 | pgjdbc, the PostgreSQL JDBC Driver, does not close the connection when an unchecked exception interrupts a request. Par… |
| 2026-11-23 17:17:49 | [CVE-2026-134844](https://nvd.nist.gov/vuln/detail/CVE-2026-134844) | High | 7.5 | pgjdbc, the PostgreSQL JDBC Driver, uses unqualified operators and functions in the catalog queries of DatabaseMetaData… |
| 2026-11-23 17:17:49 | [CVE-2026-134845](https://nvd.nist.gov/vuln/detail/CVE-2026-134845) | High | 7.4 | pgjdbc, the PostgreSQL JDBC Driver, does not enforce TLS for some settings that ask for it. When sslmode is not set, an… |
| 2026-11-23 17:17:49 | [CVE-2026-134846](https://nvd.nist.gov/vuln/detail/CVE-2026-134846) | Medium | 6.5 | pgjdbc, the PostgreSQL JDBC Driver, does not check the token state that GSSContext.unwrap() reports on a GSS-encrypted… |
| 2026-11-23 17:17:49 | [CVE-2026-134847](https://nvd.nist.gov/vuln/detail/CVE-2026-134847) | Medium | 6.5 | pgjdbc, the PostgreSQL JDBC Driver, cuts the weight and scale of a BigDecimal to 16 bits when it sends the value in bin… |
| 2026-11-23 17:17:49 | [CVE-2026-134848](https://nvd.nist.gov/vuln/detail/CVE-2026-134848) | High | 7.4 | pgjdbc, the PostgreSQL JDBC Driver, does not refuse a NUL character in a startup parameter. The StartupMessage is a lis… |
| 2026-11-23 17:17:51 | [CVE-2026-135271](https://nvd.nist.gov/vuln/detail/CVE-2026-135271) | Low | 3.7 | In JetBrains Kotlinx.serialization before 1.12.0 a DoS attack was possible via recursive JSON decoding |
| 2026-11-23 17:17:51 | [CVE-2026-135272](https://nvd.nist.gov/vuln/detail/CVE-2026-135272) | Low | 3.3 | In JetBrains Kotlinx-io before 0.9.3 information disclosure was possible via partial file writes on Node.js |
| 2026-11-23 17:17:51 | [CVE-2026-135286](https://nvd.nist.gov/vuln/detail/CVE-2026-135286) | Medium | 5.3 | phpwcms before 1.9.53, 1.12.7 and 2.0.0-beta.4 contains a host header poisoning vulnerability that allows unauthenticat… |
| 2026-11-23 17:17:52 | [CVE-2026-135287](https://nvd.nist.gov/vuln/detail/CVE-2026-135287) | Medium | 5.3 | LiteLLM Proxy 1.62.4 before 1.84.0 contains a callback injection vulnerability that allows authenticated API key holder… |
| 2026-11-23 17:17:52 | [CVE-2026-135288](https://nvd.nist.gov/vuln/detail/CVE-2026-135288) | Medium | 6.3 | AIOStreams 2.9.0 through 2.38.1 contains an information disclosure vulnerability in makeRequest() that leaks the intern… |
| 2026-11-23 17:17:52 | [CVE-2026-135289](https://nvd.nist.gov/vuln/detail/CVE-2026-135289) | Medium | 5.1 | ERPSaaS 3.7.9 through 3.47.0 contains a stored cross-site scripting vulnerability that allows authenticated company use… |
| 2026-11-23 17:17:52 | [CVE-2026-135290](https://nvd.nist.gov/vuln/detail/CVE-2026-135290) | Medium | 6.8 | OpenCV through 4.14.0 and 5.0.0 through 5.1.0 contains an infinite loop vulnerability in YAMLParser::parse that allows… |
| 2026-11-23 17:17:52 | [CVE-2026-135291](https://nvd.nist.gov/vuln/detail/CVE-2026-135291) | Medium | 6.0 | Contiki-NG through 5.2 contains a NULL pointer dereference vulnerability in rpl_remove_routes_by_nexthop() in the RPL-C… |
| 2026-11-23 17:17:52 | [CVE-2026-135292](https://nvd.nist.gov/vuln/detail/CVE-2026-135292) | High | 8.3 | Contiki-NG through 5.2 contains an out-of-bounds write vulnerability in the MPL multicast engine that allows remote una… |
| 2026-11-23 17:17:53 | [CVE-2026-135293](https://nvd.nist.gov/vuln/detail/CVE-2026-135293) | High | 7.1 | Contiki-NG through 5.2 contains an infinite loop vulnerability in icmp_in() in os/net/ipv6/multicast/mpl.c that allows… |
| 2026-11-23 17:17:53 | [CVE-2026-135294](https://nvd.nist.gov/vuln/detail/CVE-2026-135294) | Medium | 5.8 | LibreCAD through 2.2.1.6 contains a heap-based out-of-bounds write vulnerability in RS_FilterDXF1::readFileInBuffer() c… |
| 2026-11-23 17:17:53 | [CVE-2026-135295](https://nvd.nist.gov/vuln/detail/CVE-2026-135295) | High | 8.5 | FontForge through 20251009 contains a heap out-of-bounds write vulnerability in PcfReadEncodingsNames() that allows att… |
| 2026-11-23 17:17:53 | [CVE-2026-135296](https://nvd.nist.gov/vuln/detail/CVE-2026-135296) | Medium | 6.9 | LibreCAD through 2.2.1.6 contains an out-of-bounds access vulnerability in picPunto::processFilePic() of the PIC import… |
| 2026-11-23 17:17:53 | [CVE-2026-135297](https://nvd.nist.gov/vuln/detail/CVE-2026-135297) | Medium | 5.3 | Convoy before 26.6.0 contains an information disclosure vulnerability that allows authenticated dashboard users to read… |
| 2026-11-23 17:17:53 | [CVE-2026-135298](https://nvd.nist.gov/vuln/detail/CVE-2026-135298) | High | 7.6 | Convoy before 26.6.0 contains an insecure direct object reference vulnerability in /portal-api single-resource handlers… |
| 2026-11-23 17:17:54 | [CVE-2026-135299](https://nvd.nist.gov/vuln/detail/CVE-2026-135299) | High | 7.1 | Convoy before 26.3.7 contains an arbitrary file read vulnerability that allows any project API key holder, including vi… |
| 2026-11-23 17:17:54 | [CVE-2026-135300](https://nvd.nist.gov/vuln/detail/CVE-2026-135300) | Critical | 9.1 | Pomerium from 0.30.0 before 0.34.0 contains an authentication bypass vulnerability in the MCP token endpoint that skips… |
| 2026-11-23 17:17:54 | [CVE-2026-135301](https://nvd.nist.gov/vuln/detail/CVE-2026-135301) | Medium | 5.1 | The AIL Framework web application contains a stored cross-site scripting (XSS) vulnerability in its dashboard templates… |
| 2026-11-23 17:17:55 | [CVE-2026-95410](https://nvd.nist.gov/vuln/detail/CVE-2026-95410) |  |  | In PeriodicAdvertisingSynchronizer::OnPeriodicAdvertisingReport of periodic_advertising_synchronizer.cc, there is a pos… |
| 2026-11-23 17:17:55 | [CVE-2026-95411](https://nvd.nist.gov/vuln/detail/CVE-2026-95411) |  |  | In BrEdrDynamicChannel of bredr_dynamic_channel.cc, there is a possible resource leak due to a logic error in the code.… |
| 2026-11-23 17:17:55 | [CVE-2026-95412](https://nvd.nist.gov/vuln/detail/CVE-2026-95412) |  |  | In OpalCommunicationManagerService of opal_communication_manager_service.cc, there is a possible use after free due to… |
| 2026-11-23 17:17:55 | [CVE-2026-95413](https://nvd.nist.gov/vuln/detail/CVE-2026-95413) |  |  | In CameraManagerBroker::~CameraManagerBroker of camera_manager_broker.cc, there is a possible use after free due to a r… |
| 2026-11-23 17:17:56 | [CVE-2026-95414](https://nvd.nist.gov/vuln/detail/CVE-2026-95414) |  |  | In HttpFileRequestHandler::GetFilePath of http_file_request_handler.cc, there is a possible path traversal due to impro… |
| 2026-11-23 17:17:56 | [CVE-2026-95415](https://nvd.nist.gov/vuln/detail/CVE-2026-95415) |  |  | In RemoteCharacteristic of remote_characteristic.cc, there is a possible process abort due to a missing check that the… |
| 2026-11-23 17:17:56 | [CVE-2026-95416](https://nvd.nist.gov/vuln/detail/CVE-2026-95416) |  |  | In OnPairingFailed of security_manager.cc, there is a possible crash due to a logic error in clearing the link encrypti… |
| 2026-11-23 17:17:56 | [CVE-2026-95417](https://nvd.nist.gov/vuln/detail/CVE-2026-95417) |  |  | In ResolvePendingNotifyRequests of remote_characteristic.cc, there is a possible use after free due to a status callbac… |
| 2026-11-23 17:17:56 | [CVE-2026-95418](https://nvd.nist.gov/vuln/detail/CVE-2026-95418) |  |  | In LogicalLink::SignalError of logical_link.cc, there is a possible use after free due to the object being destroyed by… |
| 2026-11-23 17:17:56 | [CVE-2026-95419](https://nvd.nist.gov/vuln/detail/CVE-2026-95419) |  |  | In OnPairingRequest of security_manager.cc, there is a possible process abort due to a missing check of the local IO ca… |
| 2026-11-23 17:17:56 | [CVE-2026-95420](https://nvd.nist.gov/vuln/detail/CVE-2026-95420) |  |  | In OnEncryptionChange of security_manager.cc, there is a possible way to establish a bond marked as authenticated witho… |
| 2026-11-23 17:17:56 | [CVE-2026-95421](https://nvd.nist.gov/vuln/detail/CVE-2026-95421) |  |  | In BrEdrSignalingChannel::DecodeRxUnit of bredr_signaling_channel.cc, there is a possible use after free due to a missi… |
| 2026-11-23 17:17:57 | [CVE-2026-95422](https://nvd.nist.gov/vuln/detail/CVE-2026-95422) |  |  | In OnSyncEstablished of periodic_advertising_synchronizer.cc, there is a possible crash due to a reachable assertion. T… |
| 2026-11-23 17:17:57 | [CVE-2026-95423](https://nvd.nist.gov/vuln/detail/CVE-2026-95423) |  |  | In OnWriteCCC of local_service_manager.cc, there is a possible crash due to a missing null check. This could lead to re… |
| 2026-11-23 17:17:57 | [CVE-2026-95424](https://nvd.nist.gov/vuln/detail/CVE-2026-95424) |  |  | In IsoDataChannelImpl::TrySendPackets of iso_data_channel.cc, there is a possible assertion failure due to improper inp… |
| 2026-11-23 17:17:57 | [CVE-2026-95425](https://nvd.nist.gov/vuln/detail/CVE-2026-95425) |  |  | In StartDescriptorDiscovery of remote_service.cc, there is a possible use after free due to the service object being de… |
| 2026-11-23 17:17:57 | [CVE-2026-95426](https://nvd.nist.gov/vuln/detail/CVE-2026-95426) |  |  | In ParseAdvertisingReports of extended_low_energy_scanner.cc, there is a possible out of bounds read due to a missing b… |
| 2026-11-23 17:17:57 | [CVE-2026-95427](https://nvd.nist.gov/vuln/detail/CVE-2026-95427) |  |  | In IsBrEdrCrossTransportKeyDerivationAllowed of security_manager.cc, there is a possible way to replace an authenticate… |
| 2026-11-23 17:17:57 | [CVE-2026-95429](https://nvd.nist.gov/vuln/detail/CVE-2026-95429) |  |  | In BrEdrDynamicChannel of bredr_dynamic_channel.cc, there is a possible resource exhaustion due to a missing timeout du… |
| 2026-11-23 17:17:57 | [CVE-2026-95430](https://nvd.nist.gov/vuln/detail/CVE-2026-95430) |  |  | In DuoVideoBuffer of duo_video_buffer.cc, there is a possible out of bounds write due to an integer overflow. This coul… |
| 2026-11-23 17:17:58 | [CVE-2026-95431](https://nvd.nist.gov/vuln/detail/CVE-2026-95431) |  |  | In HDSBrokerFidlImpl::RegisterMessageHandler of hds_broker_fidl_impl.cc, there is a possible way to replace internal me… |
| 2026-11-23 17:17:58 | [CVE-2026-95432](https://nvd.nist.gov/vuln/detail/CVE-2026-95432) |  |  | In InteropPolicy::OnStateChange of interop_policy.cc, there is a possible way to turn off the camera streaming indicato… |
| 2026-11-23 17:17:58 | [CVE-2026-95433](https://nvd.nist.gov/vuln/detail/CVE-2026-95433) |  |  | In FuchsiaVideoOutputProvider of fuchsia_video_output_provider.cc, there is a possible use after free due to a race con… |
| 2026-11-23 17:17:58 | [CVE-2026-95434](https://nvd.nist.gov/vuln/detail/CVE-2026-95434) |  |  | In LowEnergyScanner::NotifyPeerFound of low_energy_scanner.cc, there is a possible resource exhaustion due to a missing… |
| 2026-11-23 17:17:58 | [CVE-2026-95435](https://nvd.nist.gov/vuln/detail/CVE-2026-95435) |  |  | In AdvertisingData::FromBytes of advertising_data.cc, there is a possible crash due to an unaligned memory access. This… |
| 2026-11-23 17:17:58 | [CVE-2026-95436](https://nvd.nist.gov/vuln/detail/CVE-2026-95436) |  |  | In StatusCodeFromView of control_packets.h, there is a possible crash due to an incomplete length check. This could lea… |
| 2026-11-23 17:17:58 | [CVE-2026-95438](https://nvd.nist.gov/vuln/detail/CVE-2026-95438) |  |  | In LeAddrToDeviceAddr of device_address.cc, there is a possible crash due to improper input validation. This could lead… |
| 2026-11-23 17:17:58 | [CVE-2026-95439](https://nvd.nist.gov/vuln/detail/CVE-2026-95439) |  |  | In EnhancedRetransmissionModeRxEngine::ProcessPdu of enhanced_retransmission_mode_rx_engine.cc, there is a possible use… |
| 2026-11-23 17:17:58 | [CVE-2026-95440](https://nvd.nist.gov/vuln/detail/CVE-2026-95440) |  |  | In OnModeChange of autosniff.cc, there is a possible crash due to a missing length check. This could lead to local deni… |
| 2026-11-23 17:17:59 | [CVE-2026-95441](https://nvd.nist.gov/vuln/detail/CVE-2026-95441) |  |  | In Connection::OnDisconnectionComplete of connection.cc, there is a possible way to stall outgoing Bluetooth data due t… |
| 2026-11-23 17:17:59 | [CVE-2026-95442](https://nvd.nist.gov/vuln/detail/CVE-2026-95442) |  |  | In NotifyCachedPeers of low_energy_scanner.cc, there is a possible use after free due to a scan result cache being clea… |
| 2026-11-23 17:17:59 | [CVE-2026-95443](https://nvd.nist.gov/vuln/detail/CVE-2026-95443) |  |  | In ZxFdServer of zx_fd_grpc_ipc_builder.cc, there is a possible use after free due to a raw pointer to a server object… |
| 2026-11-23 17:17:59 | [CVE-2026-95444](https://nvd.nist.gov/vuln/detail/CVE-2026-95444) |  |  | In HandleEndTransaction of bearer.cc, there is a possible use after free due to a missing check that the object still e… |
| 2026-11-23 17:17:59 | [CVE-2026-95445](https://nvd.nist.gov/vuln/detail/CVE-2026-95445) |  |  | In ProcessWriteQueue of client.cc, there is a possible use after free due to a callback that continues to use its objec… |
| 2026-11-23 17:17:59 | [CVE-2026-95446](https://nvd.nist.gov/vuln/detail/CVE-2026-95446) |  |  | In ProcessPdu of credit_based_flow_control_rx_engine.cc, there is a possible resource exhaustion due to improper input… |
| 2026-11-23 17:17:59 | [CVE-2026-95447](https://nvd.nist.gov/vuln/detail/CVE-2026-95447) |  |  | In sdp::Client::Impl::OnRxFrame of client.cc, there is a possible assertion failure due to a missing bounds check. This… |
| 2026-11-23 17:17:59 | [CVE-2026-95448](https://nvd.nist.gov/vuln/detail/CVE-2026-95448) |  |  | In MediaFocusFidlImpl of media_focus_fidl_impl.cc, there is a possible use after free due to a race condition. This cou… |
| 2026-11-23 17:18:00 | [CVE-2026-95449](https://nvd.nist.gov/vuln/detail/CVE-2026-95449) |  |  | In NexustalkStream::PullFrameTask of nexustalk_stream.cc, there is a possible use after free due to a race condition. T… |
| 2026-11-23 17:18:00 | [CVE-2026-95450](https://nvd.nist.gov/vuln/detail/CVE-2026-95450) |  |  | In HandleRxPdu of channel.cc, there is a possible use after free due to the channel being destroyed while it is still p… |
| 2026-11-23 17:18:00 | [CVE-2026-95451](https://nvd.nist.gov/vuln/detail/CVE-2026-95451) |  |  | In LogicalLink::SignalError of logical_link.cc, there is a possible use after free due to an error callback that can sy… |
| 2026-11-23 17:18:00 | [CVE-2026-95452](https://nvd.nist.gov/vuln/detail/CVE-2026-95452) |  |  | In LeAddrToDeviceAddr of device_address.cc, there is a possible crash due to improper input validation. This could lead… |
| 2026-11-23 17:18:00 | [CVE-2026-95453](https://nvd.nist.gov/vuln/detail/CVE-2026-95453) |  |  | In LogExportControllerImpl of log_export_fidl.cc, there is a possible use after free due to a service handler that is n… |
| 2026-11-23 17:18:00 | [CVE-2026-95454](https://nvd.nist.gov/vuln/detail/CVE-2026-95454) |  |  | In IsoDataChannelImpl::OnRxPacket of iso_data_channel.cc, there is a possible out of bounds read due to a missing bound… |
| 2026-11-23 17:18:00 | [CVE-2026-95455](https://nvd.nist.gov/vuln/detail/CVE-2026-95455) |  |  | In ServerSessionBroker of server_session_broker.cc, there is a possible use after free due to a race condition. This co… |
| 2026-11-23 17:18:00 | [CVE-2026-95456](https://nvd.nist.gov/vuln/detail/CVE-2026-95456) |  |  | In StartA2dpOffload of a2dp_offload_manager.cc, there is a possible use after free due to a stored callback that is not… |
| 2026-11-23 17:18:01 | [CVE-2026-95457](https://nvd.nist.gov/vuln/detail/CVE-2026-95457) |  |  | In reconnect.shard.cml, there is a possible way to turn off the camera streaming and microphone mute indicator LEDs due… |
| 2026-11-23 17:18:01 | [CVE-2026-95458](https://nvd.nist.gov/vuln/detail/CVE-2026-95458) |  |  | In BluetoothSetupImpl::OnAudioSourceConnectChanged of bluetooth_setup_impl.cc, there is a possible way for an unauthent… |
| 2026-11-23 17:18:01 | [CVE-2026-95459](https://nvd.nist.gov/vuln/detail/CVE-2026-95459) |  |  | In OnRxLeCreditBasedConnectionRequest of le_dynamic_channel.cc, there is a possible assertion failure due to improper i… |
| 2026-11-23 17:18:01 | [CVE-2026-95460](https://nvd.nist.gov/vuln/detail/CVE-2026-95460) |  |  | In Phase2SecureConnections::OnPeerPublicKey of phase_2_secure_connections.cc, there is a possible way to learn the pass… |
| 2026-11-23 17:18:01 | [CVE-2026-95461](https://nvd.nist.gov/vuln/detail/CVE-2026-95461) |  |  | In HandleRxPacket of logical_link.cc, there is a possible resource exhaustion due to a missing limit on packets buffere… |
| 2026-11-23 17:18:01 | [CVE-2026-95462](https://nvd.nist.gov/vuln/detail/CVE-2026-95462) |  |  | In ServiceSearchResponse::GetPDU of pdu.cc, there is a possible crash due to an incorrect size calculation. This could… |
| 2026-11-23 17:18:01 | [CVE-2026-95463](https://nvd.nist.gov/vuln/detail/CVE-2026-95463) |  |  | In DataElement::Read of data_element.cc, there is a possible stack exhaustion due to unbounded recursion. This could le… |
| 2026-11-23 17:18:01 | [CVE-2026-95464](https://nvd.nist.gov/vuln/detail/CVE-2026-95464) |  |  | In SignalError of logical_link.cc, there is a possible use after free due to an error callback that can destroy the obj… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
