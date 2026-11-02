# New CVEs

Hourly lists of vulnerabilities newly published to the
[National Vulnerability Database](https://nvd.nist.gov/), taken from the
[NVD API](https://nvd.nist.gov/developers/vulnerabilities).
A GitHub Actions workflow runs every hour, fetches the CVEs published since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-cves-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-11-02 20:18 UTC

New CVEs published between 2026-11-02 19:20 UTC and 2026-11-02 20:18 UTC.

[Full CSV](data/new-cves-2026-11-02T20-18-13-32723Z.csv)

| Published (UTC) | CVE | Severity | Score | Description |
| :-------------- | :-- | :------- | ----: | :---------- |
| 2026-11-02 20:17:22 | [CVE-2025-22436](https://nvd.nist.gov/vuln/detail/CVE-2025-22436) |  |  | In multiple locations, there is a possible way to trick a user into disclosing Autofill contents due to a tapjacking/ov… |
| 2026-11-02 20:17:23 | [CVE-2025-26433](https://nvd.nist.gov/vuln/detail/CVE-2025-26433) |  |  | In multiple locations, there is a possible way to trick a user into accepting a permission due to a tapjacking/overlay… |
| 2026-11-02 20:17:23 | [CVE-2026-0053](https://nvd.nist.gov/vuln/detail/CVE-2026-0053) |  |  | In multiple locations, there is a possible method for a primary user to disable secure nfc on other full users due to i… |
| 2026-11-02 20:17:26 | [CVE-2026-102435](https://nvd.nist.gov/vuln/detail/CVE-2026-102435) | Critical | 9.8 | The Ultra Addons for Contact Form 7 plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient f… |
| 2026-11-02 20:17:33 | [CVE-2026-116769](https://nvd.nist.gov/vuln/detail/CVE-2026-116769) | Critical | 9.3 | CVE-2026-116769 is an authentication bypass vulnerability in Secure Access servers starting with version 13.0 and prior… |
| 2026-11-02 20:17:33 | [CVE-2026-117082](https://nvd.nist.gov/vuln/detail/CVE-2026-117082) |  |  | An authentication bypass vulnerability in the Universal Plug and Play (UPnP) framework of the Sercomm AOT-4221SR 4.6 Du… |
| 2026-11-02 20:17:38 | [CVE-2026-119737](https://nvd.nist.gov/vuln/detail/CVE-2026-119737) | High | 8.5 | The pppoe_wrapper vendor daemon from the Amlogic Android SDK, as shipped on Nexbox A95X (Amlogic S905/S905X) TV boxes,… |
| 2026-11-02 20:17:38 | [CVE-2026-119738](https://nvd.nist.gov/vuln/detail/CVE-2026-119738) | Medium | 6.9 | The VobSub subtitle decoder libsub_vob (part of the Amlogic DroidLogic SubTitleService), as shipped on Nexbox A95X (Aml… |
| 2026-11-02 20:17:38 | [CVE-2026-119739](https://nvd.nist.gov/vuln/detail/CVE-2026-119739) | Medium | 6.9 | The VobSub subtitle decoder libsub_vob (part of the Amlogic DroidLogic SubTitleService), as shipped on Nexbox A95X (Aml… |
| 2026-11-02 20:17:38 | [CVE-2026-119740](https://nvd.nist.gov/vuln/detail/CVE-2026-119740) | High | 7.0 | Nexbox A95X TV boxes built on the Amlogic S905X platform contain an unauthenticated console exposed via an internal UAR… |
| 2026-11-02 20:17:41 | [CVE-2026-120689](https://nvd.nist.gov/vuln/detail/CVE-2026-120689) | Medium | 4.3 | HDF5 through 2.2.0 contains an uncontrolled recursion vulnerability in H5B__iterate_helper() in src/H5B.c. When iterati… |
| 2026-11-02 20:17:41 | [CVE-2026-28588](https://nvd.nist.gov/vuln/detail/CVE-2026-28588) | High | 8.4 | In shouldBlockDirectoryFromTree of ExternalStorageProvider.java, there is a possible way to access protected data due t… |
| 2026-11-02 20:17:41 | [CVE-2026-28597](https://nvd.nist.gov/vuln/detail/CVE-2026-28597) |  |  | In writeGrantedUriPermissions of UriGrantsManagerService.java, there is a possible permission bypass due to improper in… |
| 2026-11-02 20:17:42 | [CVE-2026-28621](https://nvd.nist.gov/vuln/detail/CVE-2026-28621) |  |  | In getRingtone of RingtoneFactory.java, there is a possible unprivileged access risk due to a missing permission check.… |
| 2026-11-02 20:17:42 | [CVE-2026-28632](https://nvd.nist.gov/vuln/detail/CVE-2026-28632) |  |  | In multiple locations, there is a possible way to share files across profiles due to a logic error in the code. This co… |
| 2026-11-02 20:17:42 | [CVE-2026-28643](https://nvd.nist.gov/vuln/detail/CVE-2026-28643) |  |  | In multiple locations, there is a possible denial of service due to a missing permission check. This could lead to loca… |
| 2026-11-02 20:17:42 | [CVE-2026-28645](https://nvd.nist.gov/vuln/detail/CVE-2026-28645) |  |  | In onStrongAuthRequiredChanged of UsbService.java, there is a possible unauthenticated enabling of USB data due to a lo… |
| 2026-11-02 20:17:42 | [CVE-2026-28665](https://nvd.nist.gov/vuln/detail/CVE-2026-28665) |  |  | In onCreate of SettingsApplication.java, there is a possible cross-profile consent dialog label injection due to improp… |
| 2026-11-02 20:17:42 | [CVE-2026-45514](https://nvd.nist.gov/vuln/detail/CVE-2026-45514) |  |  | In multiple functions of SaveUi.java, there is a possible bypass of package installation requirements due to a logic er… |
| 2026-11-02 20:17:42 | [CVE-2026-49912](https://nvd.nist.gov/vuln/detail/CVE-2026-49912) |  |  | In multiple functions of MediaCarouselController.kt, there is a possible way for media to show up after disablement due… |
| 2026-11-02 20:17:42 | [CVE-2026-49922](https://nvd.nist.gov/vuln/detail/CVE-2026-49922) |  |  | In queryRemoteConnectionServices of ConnectionServiceWrapper.java, there is a possible permission bypass due to a confu… |
| 2026-11-02 20:17:42 | [CVE-2026-49923](https://nvd.nist.gov/vuln/detail/CVE-2026-49923) |  |  | In onResult of AccountManagerService.java, there is a possible untrusted/misleading UI issue due to a logic error in th… |
| 2026-11-02 20:17:43 | [CVE-2026-49924](https://nvd.nist.gov/vuln/detail/CVE-2026-49924) |  |  | In ShortcutInfo of ShortcutInfo.java, there is a possible way to crash the launcher via unauthorized shortcuts due to r… |
| 2026-11-02 20:17:43 | [CVE-2026-49931](https://nvd.nist.gov/vuln/detail/CVE-2026-49931) |  |  | In onActivityResult in multiple locations, there is a possible contact leak from protected profile due to a confused de… |
| 2026-11-02 20:17:43 | [CVE-2026-49934](https://nvd.nist.gov/vuln/detail/CVE-2026-49934) |  |  | In multiple functions of MmiUtils.java, there is a possible risk of USSD/MMI code execution due to improper input valid… |
| 2026-11-02 20:17:43 | [CVE-2026-49935](https://nvd.nist.gov/vuln/detail/CVE-2026-49935) |  |  | In getXmlFileNameForUser of LocaleManagerService.java, there is a possible permission bypass due to a confusable path t… |
| 2026-11-02 20:17:43 | [CVE-2026-55257](https://nvd.nist.gov/vuln/detail/CVE-2026-55257) |  |  | In UsbDialogHelper of UsbDialogHelper.java, there is a possible UI confusion due to misleading or insufficient UI. This… |
| 2026-11-02 20:17:44 | [CVE-2026-55261](https://nvd.nist.gov/vuln/detail/CVE-2026-55261) |  |  | In nfa_t4tnfcee_store_rx_buf of nfa_nfcee_act.cc, there is a possible way to achieve code execution due to a missing pe… |
| 2026-11-02 20:17:44 | [CVE-2026-55262](https://nvd.nist.gov/vuln/detail/CVE-2026-55262) |  |  | In setNotificationListenerAccessGrantedForUserInternal of NotificationManagerService.java, there is a possible policy d… |
| 2026-11-02 20:17:44 | [CVE-2026-55263](https://nvd.nist.gov/vuln/detail/CVE-2026-55263) |  |  | In multiple functions of AllowBindAppWidgetActivity.java, there is a possible misunderstanding of reject/consent action… |
| 2026-11-02 20:17:44 | [CVE-2026-55264](https://nvd.nist.gov/vuln/detail/CVE-2026-55264) |  |  | In checkWhetherCallingAppHasAccess of DownloadProvider.java, there is a possible information leak due to a confused dep… |
| 2026-11-02 20:17:44 | [CVE-2026-55271](https://nvd.nist.gov/vuln/detail/CVE-2026-55271) |  |  | In forwardToPreferredActionPickHandler of ContactsPickerActivity.kt, there is a possible intent redirection due to a co… |
| 2026-11-02 20:17:44 | [CVE-2026-55272](https://nvd.nist.gov/vuln/detail/CVE-2026-55272) |  |  | In multiple places, there is a possible permission bypass due to resource exhaustion. This could lead to local denial o… |
| 2026-11-02 20:17:44 | [CVE-2026-55275](https://nvd.nist.gov/vuln/detail/CVE-2026-55275) |  |  | In multiple locations, there is a possible use-after-free due to a race condition. This could lead to remote escalation… |
| 2026-11-02 20:17:44 | [CVE-2026-55283](https://nvd.nist.gov/vuln/detail/CVE-2026-55283) |  |  | In multiple locations, there is a possible memory safety issue due to a use-after-free. This could lead to remote escal… |
| 2026-11-02 20:17:45 | [CVE-2026-55287](https://nvd.nist.gov/vuln/detail/CVE-2026-55287) |  |  | In onCreate of GrantCredentialsPermissionActivity.java, there is a possible way to trick the user into granting account… |
| 2026-11-02 20:17:45 | [CVE-2026-55288](https://nvd.nist.gov/vuln/detail/CVE-2026-55288) |  |  | In validEfCfis of SIMRecords.java, there is a possible way to cause a denial of service due to an uncaught exception. T… |
| 2026-11-02 20:17:45 | [CVE-2026-55289](https://nvd.nist.gov/vuln/detail/CVE-2026-55289) |  |  | In multiple functions in multiple locations, there is a possible execution of sensitive USSD codes due to a confused de… |
| 2026-11-02 20:17:45 | [CVE-2026-55292](https://nvd.nist.gov/vuln/detail/CVE-2026-55292) |  |  | In rw_ci_data_cback of rw_ci.cc, there is a possible memory safety issue due to integer underflow. This could lead to r… |
| 2026-11-02 20:17:46 | [CVE-2026-58814](https://nvd.nist.gov/vuln/detail/CVE-2026-58814) |  |  | In parseContentType of PduParser.java, there is a possible denial of service due to an integer overflow. This could lea… |
| 2026-11-02 20:17:47 | [CVE-2026-58817](https://nvd.nist.gov/vuln/detail/CVE-2026-58817) |  |  | In parseKnownActivityEmbeddingCerts of ParsingUtils.java, there is a possible permanent denial of service due to improp… |
| 2026-11-02 20:17:47 | [CVE-2026-58821](https://nvd.nist.gov/vuln/detail/CVE-2026-58821) |  |  | In multiple functions of SearchRequestDatabaseUtil.java, there is a possible way to access protected data due to SQL in… |
| 2026-11-02 20:17:47 | [CVE-2026-58824](https://nvd.nist.gov/vuln/detail/CVE-2026-58824) |  |  | In __pkvm_load_tracing of trace.c, there is a possible out-of-bounds write due to an incorrect bounds check. This could… |
| 2026-11-02 20:17:47 | [CVE-2026-58825](https://nvd.nist.gov/vuln/detail/CVE-2026-58825) |  |  | In multiple functions of fork.c, there is a possible use after free due to a logic error in the code. This could lead t… |
| 2026-11-02 20:17:47 | [CVE-2026-58826](https://nvd.nist.gov/vuln/detail/CVE-2026-58826) |  |  | In ksys_unshare of fork.c, there is a possible memory corruption due to a use after free. This could lead to local esca… |
| 2026-11-02 20:17:47 | [CVE-2026-58827](https://nvd.nist.gov/vuln/detail/CVE-2026-58827) |  |  | In multiple functions of dma-buf.c, there is a possible use after free due to a race condition. This could lead to loca… |
| 2026-11-02 20:17:47 | [CVE-2026-58828](https://nvd.nist.gov/vuln/detail/CVE-2026-58828) |  |  | In multiple functions of base.c, there is a possible use-after-free due to a race condition. This could lead to local e… |
| 2026-11-02 20:17:47 | [CVE-2026-58829](https://nvd.nist.gov/vuln/detail/CVE-2026-58829) |  |  | In fuse_backing_mmap of backing.c, there is a possible memory corruption due to a use after free. This could lead to lo… |
| 2026-11-02 20:17:48 | [CVE-2026-58836](https://nvd.nist.gov/vuln/detail/CVE-2026-58836) |  |  | In handlePackagePostInstall of InstallPackageHelper.java, there is a possible Enhanced Confirmation Mode (ECM) bypass v… |
| 2026-11-02 20:17:48 | [CVE-2026-58837](https://nvd.nist.gov/vuln/detail/CVE-2026-58837) |  |  | In multiple locations, there is a possible background activity launch due to a logic error in the code. This could lead… |
| 2026-11-02 20:17:48 | [CVE-2026-58838](https://nvd.nist.gov/vuln/detail/CVE-2026-58838) |  |  | In multiple functions of Helpers.java, there is a possible information disclosure due to improper input validation. Thi… |
| 2026-11-02 20:17:48 | [CVE-2026-58844](https://nvd.nist.gov/vuln/detail/CVE-2026-58844) |  |  | In multiple locations, there is a possible out of bounds read/write due to an incorrect bounds check. This could lead t… |
| 2026-11-02 20:17:48 | [CVE-2026-58845](https://nvd.nist.gov/vuln/detail/CVE-2026-58845) |  |  | In multiple locations, there is a possible out of bounds write due to an integer overflow. This could lead to local esc… |
| 2026-11-02 20:17:48 | [CVE-2026-58847](https://nvd.nist.gov/vuln/detail/CVE-2026-58847) |  |  | In kvm_vfio_pviommu_attach of vfio.c, there is a possible double free due to a logic error in the code. This could lead… |
| 2026-11-02 20:17:48 | [CVE-2026-58853](https://nvd.nist.gov/vuln/detail/CVE-2026-58853) |  |  | In multiple functions of ipphelper.c, there is a possible stack bugger overflow due to a missing bounds check. This cou… |
| 2026-11-02 20:17:48 | [CVE-2026-58857](https://nvd.nist.gov/vuln/detail/CVE-2026-58857) |  |  | In decrypt of CryptoHalHidl.cpp, there is a possible use-after-free due to a race condition. This could lead to remote… |
| 2026-11-02 20:17:49 | [CVE-2026-58866](https://nvd.nist.gov/vuln/detail/CVE-2026-58866) |  |  | In setAccessibilityWindowAttributes of AccessibilityWindowManager.java, there is a possible untrusted/misleading UI iss… |
| 2026-11-02 20:17:49 | [CVE-2026-58867](https://nvd.nist.gov/vuln/detail/CVE-2026-58867) |  |  | In getMessenger of WifiP2pServiceImpl.java, there is a possible permission bypass due to a missing permission check. Th… |
| 2026-11-02 20:17:49 | [CVE-2026-58868](https://nvd.nist.gov/vuln/detail/CVE-2026-58868) |  |  | In onOutputReceived of FrameDecoder.cpp, there is a possible out-of-bounds write due to a heap buffer overflow. This co… |
| 2026-11-02 20:17:49 | [CVE-2026-58870](https://nvd.nist.gov/vuln/detail/CVE-2026-58870) |  |  | In onPersistentGroupsChanged of WifiP2pServiceImpl.java, there is a possible permission bypass due to a missing permiss… |
| 2026-11-02 20:17:49 | [CVE-2026-58871](https://nvd.nist.gov/vuln/detail/CVE-2026-58871) |  |  | In set_type4_frame_classifier of sta_iface.cpp, there is a possible memory safety issue due to a heap buffer overflow.… |
| 2026-11-02 20:17:49 | [CVE-2026-58875](https://nvd.nist.gov/vuln/detail/CVE-2026-58875) |  |  | In multiple locations, there is a possible denial of service due to improper input validation. This could lead to local… |
| 2026-11-02 20:17:49 | [CVE-2026-58876](https://nvd.nist.gov/vuln/detail/CVE-2026-58876) |  |  | In multiple locations, there is a possible memory safety issue due to a use-after-free. This could lead to remote code… |
| 2026-11-02 20:17:49 | [CVE-2026-58877](https://nvd.nist.gov/vuln/detail/CVE-2026-58877) |  |  | In checkNearbyDevicesPermission of WifiP2pServiceImpl.java, there is a possible permission bypass due to a confused dep… |
| 2026-11-02 20:17:49 | [CVE-2026-58879](https://nvd.nist.gov/vuln/detail/CVE-2026-58879) |  |  | In descramble of multiple files, there is a possible out-of-bounds write due to improper casting. This could lead to lo… |
| 2026-11-02 20:17:50 | [CVE-2026-58882](https://nvd.nist.gov/vuln/detail/CVE-2026-58882) |  |  | In decodeWapPdu of WapPushOverSms.java, there is a possible out of bounds read due to an integer overflow. This could l… |
| 2026-11-02 20:17:50 | [CVE-2026-58883](https://nvd.nist.gov/vuln/detail/CVE-2026-58883) |  |  | In multiple locations, there is a possible denial of service due to a logic error in the code. This could lead to remot… |
| 2026-11-02 20:17:50 | [CVE-2026-58884](https://nvd.nist.gov/vuln/detail/CVE-2026-58884) |  |  | In startTetheredHotspotRequest of WifiServiceImpl.java, there is a possible permission bypass due to a confused deputy.… |
| 2026-11-02 20:17:50 | [CVE-2026-58885](https://nvd.nist.gov/vuln/detail/CVE-2026-58885) |  |  | In multiple locations, there is a possible permission bypass due to a confused deputy. This could lead to local escalat… |
| 2026-11-02 20:17:50 | [CVE-2026-58886](https://nvd.nist.gov/vuln/detail/CVE-2026-58886) |  |  | In updateInputWindows of InputMonitor.java, there is a possible tapjacking issue due to a logic error in the code. This… |
| 2026-11-02 20:17:50 | [CVE-2026-58933](https://nvd.nist.gov/vuln/detail/CVE-2026-58933) |  |  | In process of C2SoftApvDec.cpp, there is a possible out-of-bounds read due to a logic error in the code. This could lea… |
| 2026-11-02 20:17:50 | [CVE-2026-58934](https://nvd.nist.gov/vuln/detail/CVE-2026-58934) |  |  | In prepareWindowToDisplayDuringRelayout of WindowState.java, there is a possible permission bypass due to a logic error… |
| 2026-11-02 20:17:50 | [CVE-2026-58936](https://nvd.nist.gov/vuln/detail/CVE-2026-58936) |  |  | In png_set_tRNS of pngset.c, there is a possible memory corruption due to a use-after-free. This could lead to remote c… |
| 2026-11-02 20:17:50 | [CVE-2026-58937](https://nvd.nist.gov/vuln/detail/CVE-2026-58937) |  |  | In multiple locations, there is a possible persistent denial of service due to improper input validation. This could le… |
| 2026-11-02 20:17:51 | [CVE-2026-58938](https://nvd.nist.gov/vuln/detail/CVE-2026-58938) |  |  | In parseChunk of MPEG4Extractor.cpp, there is a possible denial of service due to improper input validation. This could… |
| 2026-11-02 20:17:51 | [CVE-2026-58942](https://nvd.nist.gov/vuln/detail/CVE-2026-58942) |  |  | In do_fault_around of memory.c, there is a possible use after free due to a logic error in the code. This could lead to… |
| 2026-11-02 20:17:51 | [CVE-2026-58943](https://nvd.nist.gov/vuln/detail/CVE-2026-58943) |  |  | In run of AddAccountSettings.java, there is a possible background activity launch due to a confused deputy. This could… |
| 2026-11-02 20:17:51 | [CVE-2026-58944](https://nvd.nist.gov/vuln/detail/CVE-2026-58944) |  |  | In moveTaskToFrontLocked of ActivityTaskManagerService.java, there is a possible background application launch (bal) is… |
| 2026-11-02 20:17:51 | [CVE-2026-58945](https://nvd.nist.gov/vuln/detail/CVE-2026-58945) |  |  | In multiple locations, there is a possible side channel information leak due to improperly used crypto. This could lead… |
| 2026-11-02 20:17:51 | [CVE-2026-58946](https://nvd.nist.gov/vuln/detail/CVE-2026-58946) |  |  | In navigateUpTo of ActivityClientController.java, there is a possible permission bypass due to a logic error in the cod… |
| 2026-11-02 20:17:51 | [CVE-2026-58949](https://nvd.nist.gov/vuln/detail/CVE-2026-58949) |  |  | In parseMetaData of StagefrightMetadataRetriever.cpp, there is a possible denial of service due to a stack buffer overf… |
| 2026-11-02 20:17:51 | [CVE-2026-58951](https://nvd.nist.gov/vuln/detail/CVE-2026-58951) |  |  | In multiple locations, there is a possible permission bypass due to a missing permission check. This could lead to loca… |
| 2026-11-02 20:17:51 | [CVE-2026-58953](https://nvd.nist.gov/vuln/detail/CVE-2026-58953) |  |  | In dec_vlc_read of oapv_vlc.c, there is a possible out-of-bounds read due to a heap buffer overflow. This could lead to… |
| 2026-11-02 20:17:52 | [CVE-2026-58955](https://nvd.nist.gov/vuln/detail/CVE-2026-58955) |  |  | In updateNotificationChannel of PreferencesHelper.java, there is a possible ui obfuscation issue due to a logic error i… |
| 2026-11-02 20:17:52 | [CVE-2026-58956](https://nvd.nist.gov/vuln/detail/CVE-2026-58956) |  |  | In modpowF4 of avb_rsa.c, there is a possible signature verification bypass due to a logic error in the code. This coul… |
| 2026-11-02 20:17:52 | [CVE-2026-58957](https://nvd.nist.gov/vuln/detail/CVE-2026-58957) |  |  | In resolveToHeavyWeightSwitcherIfNeeded of ActivityStarter.java, there is a possible background activity launch due to… |
| 2026-11-02 20:17:52 | [CVE-2026-58961](https://nvd.nist.gov/vuln/detail/CVE-2026-58961) |  |  | In moveTaskToFrontLocked of ActivityTaskManagerService.java, there is a possible background activity launch due to a lo… |
| 2026-11-02 20:17:52 | [CVE-2026-58962](https://nvd.nist.gov/vuln/detail/CVE-2026-58962) |  |  | In moveTaskToFrontLocked of ActivityTaskManagerService.java, there is a possible permission bypass due to a missing per… |
| 2026-11-02 20:17:52 | [CVE-2026-58963](https://nvd.nist.gov/vuln/detail/CVE-2026-58963) |  |  | In multiple locations, there is a possible denial of service due to improper input validation. This could lead to remot… |
| 2026-11-02 20:17:52 | [CVE-2026-58964](https://nvd.nist.gov/vuln/detail/CVE-2026-58964) |  |  | In checkDestination of SmsUsageMonitor.java, there is a possible permission bypass due to improper input validation. Th… |
| 2026-11-02 20:17:52 | [CVE-2026-58965](https://nvd.nist.gov/vuln/detail/CVE-2026-58965) |  |  | In handleAudioEffectBroadcast of MusicFxHelper.java, there is a possible permission bypass due to a confused deputy. Th… |
| 2026-11-02 20:17:52 | [CVE-2026-58966](https://nvd.nist.gov/vuln/detail/CVE-2026-58966) |  |  | In multiple functions of hppsfilter.c, there is a possible out-of-bounds write due to a stack buffer overflow. This cou… |
| 2026-11-02 20:17:53 | [CVE-2026-58968](https://nvd.nist.gov/vuln/detail/CVE-2026-58968) |  |  | In oapvd_vlc_metadata of oapv_vlc.c, there is a possible memory corruption due to a double free. This could lead to rem… |
| 2026-11-02 20:17:53 | [CVE-2026-58969](https://nvd.nist.gov/vuln/detail/CVE-2026-58969) |  |  | In multiple functions of MediaQualityService.java, there is a possible permission bypass due to a missing permission ch… |
| 2026-11-02 20:17:53 | [CVE-2026-58970](https://nvd.nist.gov/vuln/detail/CVE-2026-58970) |  |  | In deliverResult of AppTimeTracker.java, there is a possible background activity launch due to a confused deputy. This… |
| 2026-11-02 20:17:53 | [CVE-2026-58971](https://nvd.nist.gov/vuln/detail/CVE-2026-58971) |  |  | In _mupdf_get_hdr of wprint_mupdf.c, there is a possible out-of-bounds read due to an integer overflow. This could lead… |
| 2026-11-02 20:17:53 | [CVE-2026-58974](https://nvd.nist.gov/vuln/detail/CVE-2026-58974) |  |  | In multiple locations, there is a possible permission bypass due to a missing permission check. This could lead to loca… |
| 2026-11-02 20:17:53 | [CVE-2026-58975](https://nvd.nist.gov/vuln/detail/CVE-2026-58975) |  |  | In multiple locations, there is a possible out-of-bounds write due to a missing bounds check. This could lead to local… |
| 2026-11-02 20:17:53 | [CVE-2026-58976](https://nvd.nist.gov/vuln/detail/CVE-2026-58976) |  |  | In getSelectionBySubIds of ProviderUtil.java, there is a possible cross-user data leak due to a logic error in the code… |
| 2026-11-02 20:17:53 | [CVE-2026-58978](https://nvd.nist.gov/vuln/detail/CVE-2026-58978) |  |  | In multiple locations, there is a possible permission bypass due to a logic error in the code. This could lead to physi… |
| 2026-11-02 20:17:53 | [CVE-2026-58979](https://nvd.nist.gov/vuln/detail/CVE-2026-58979) |  |  | In canPresent of PresentationController.java, there is a possible permission bypass due to a logic error in the code. T… |
| 2026-11-02 20:17:54 | [CVE-2026-58984](https://nvd.nist.gov/vuln/detail/CVE-2026-58984) |  |  | In multiple locations, there is a possible memory corruption due to a use-after-free. This could lead to local escalati… |
| 2026-11-02 20:17:54 | [CVE-2026-58985](https://nvd.nist.gov/vuln/detail/CVE-2026-58985) |  |  | In handleConnectInternal of RpcServerTrusty.cpp, there is a possible denial of service due to a logic error in the code… |
| 2026-11-02 20:17:54 | [CVE-2026-58986](https://nvd.nist.gov/vuln/detail/CVE-2026-58986) |  |  | In notifyPictureProfileHandleSelection of MediaQualityService.java, there is a possible permission bypass due to a miss… |
| 2026-11-02 20:17:54 | [CVE-2026-58988](https://nvd.nist.gov/vuln/detail/CVE-2026-58988) |  |  | In isValid of ShimConverter.cpp, there is a possible out of bounds read due to a missing bounds check. This could lead… |
| 2026-11-02 20:17:54 | [CVE-2026-58989](https://nvd.nist.gov/vuln/detail/CVE-2026-58989) |  |  | In setOemUnlockAllowedByUser of OemLockService.java, there is a possible way to bypass FRP due to a missing permission… |
| 2026-11-02 20:17:54 | [CVE-2026-58990](https://nvd.nist.gov/vuln/detail/CVE-2026-58990) |  |  | In l2c_fcr_process_peer_cfg_req of l2c_fcr.cc, there is a possible memory safety issue due to an integer overflow. This… |
| 2026-11-02 20:17:54 | [CVE-2026-58994](https://nvd.nist.gov/vuln/detail/CVE-2026-58994) |  |  | In multiple functions of NfcService.java, there is a possible permission bypass due to a missing permission check. This… |
| 2026-11-02 20:17:54 | [CVE-2026-58995](https://nvd.nist.gov/vuln/detail/CVE-2026-58995) |  |  | In getEntryFileName of ZipFileRO.cpp, there is a possible memory safety issue due to a heap buffer overflow. This could… |
| 2026-11-02 20:17:54 | [CVE-2026-58997](https://nvd.nist.gov/vuln/detail/CVE-2026-58997) |  |  | In validateImageInfo of Bitmap.cpp, there is a possible out-of-bounds read due to a precondition check failure. This co… |
| 2026-11-02 20:17:55 | [CVE-2026-59000](https://nvd.nist.gov/vuln/detail/CVE-2026-59000) |  |  | In multiple locations, there is a possible permission bypass due to a confused deputy. This could lead to local escalat… |
| 2026-11-02 20:17:55 | [CVE-2026-59001](https://nvd.nist.gov/vuln/detail/CVE-2026-59001) |  |  | In checkQueryPermission of TelephonyProvider.java, there is a possible permission bypass due to a logic error in the co… |
| 2026-11-02 20:17:55 | [CVE-2026-59002](https://nvd.nist.gov/vuln/detail/CVE-2026-59002) |  |  | In handleMessage of UsbDeviceManager.java, there is a possible lock-screen bypass due to a logic error in the code. Thi… |
| 2026-11-02 20:17:55 | [CVE-2026-59003](https://nvd.nist.gov/vuln/detail/CVE-2026-59003) |  |  | In getSubscriptionProperty of SubscriptionManagerService.java, there is a possible information disclosure due to a miss… |
| 2026-11-02 20:17:55 | [CVE-2026-59004](https://nvd.nist.gov/vuln/detail/CVE-2026-59004) |  |  | In multiple locations, there is a possible permission bypass due to an uncaught exception. This could lead to local esc… |
| 2026-11-02 20:17:55 | [CVE-2026-59005](https://nvd.nist.gov/vuln/detail/CVE-2026-59005) |  |  | In insertInternal of MmsProvider.java, there is a possible multiuser isolation issue due to a missing permission check.… |
| 2026-11-02 20:17:55 | [CVE-2026-59006](https://nvd.nist.gov/vuln/detail/CVE-2026-59006) |  |  | In getTouchOcclusionMode of WindowState.java, there is a possible tapjacking issue due to a tapjacking/overlay attack.… |
| 2026-11-02 20:17:55 | [CVE-2026-59007](https://nvd.nist.gov/vuln/detail/CVE-2026-59007) |  |  | In decode_packed_entry_number of codebook.c, there is a possible out-of-bounds read due to a logic error in the code. T… |
| 2026-11-02 20:17:56 | [CVE-2026-59008](https://nvd.nist.gov/vuln/detail/CVE-2026-59008) |  |  | In setApplicationRestrictions of DevicePolicyManagerService.java, there is a possible denial of service due to resource… |
| 2026-11-02 20:17:56 | [CVE-2026-59010](https://nvd.nist.gov/vuln/detail/CVE-2026-59010) |  |  | In deserialize of legacy.rs, there is a possible denial of service due to a missing bounds check. This could lead to lo… |
| 2026-11-02 20:17:56 | [CVE-2026-59011](https://nvd.nist.gov/vuln/detail/CVE-2026-59011) |  |  | In multiple locations, there is a possible permission bypass due to a logic error in the code. This could lead to local… |
| 2026-11-02 20:17:56 | [CVE-2026-59012](https://nvd.nist.gov/vuln/detail/CVE-2026-59012) |  |  | In checkLastKnownCellIdAccessPermission of TelephonyPermissions.java, there is a possible permission bypass due to a mi… |
| 2026-11-02 20:17:56 | [CVE-2026-59014](https://nvd.nist.gov/vuln/detail/CVE-2026-59014) |  |  | In multiple locations, there is a possible out-of-bounds write due to an integer overflow. This could lead to local esc… |
| 2026-11-02 20:17:56 | [CVE-2026-59015](https://nvd.nist.gov/vuln/detail/CVE-2026-59015) |  |  | In multiple locations, there is a possible permission bypass due to a confused deputy. This could lead to local informa… |
| 2026-11-02 20:17:56 | [CVE-2026-59016](https://nvd.nist.gov/vuln/detail/CVE-2026-59016) |  |  | In sendAnomalyProfile of ProfilingService.java, there is a possible path traversal issue due to path traversal. This co… |
| 2026-11-02 20:17:56 | [CVE-2026-59020](https://nvd.nist.gov/vuln/detail/CVE-2026-59020) |  |  | In removeUserData of DevicePolicyManagerService.java, there is a possible denial of service due to a race condition. Th… |
| 2026-11-02 20:17:57 | [CVE-2026-59021](https://nvd.nist.gov/vuln/detail/CVE-2026-59021) |  |  | In multiple locations, there is a possible denial of service due to improper input validation. This could lead to local… |
| 2026-11-02 20:17:57 | [CVE-2026-59022](https://nvd.nist.gov/vuln/detail/CVE-2026-59022) |  |  | In multiple functions of MediaProvider.java, there is a possible permission bypass due to a logic error in the code. Th… |
| 2026-11-02 20:17:57 | [CVE-2026-59028](https://nvd.nist.gov/vuln/detail/CVE-2026-59028) |  |  | In resolveAidConflictLocked of RegisteredAidCache.java, there is a possible permission bypass due to a confused deputy.… |
| 2026-11-02 20:17:57 | [CVE-2026-59031](https://nvd.nist.gov/vuln/detail/CVE-2026-59031) |  |  | In InputDispatcher::flushSensor of InputDispatcher.cpp, there is a possible denial of service due to a logic error in t… |
| 2026-11-02 20:17:57 | [CVE-2026-59042](https://nvd.nist.gov/vuln/detail/CVE-2026-59042) |  |  | In __pkvm_pages_to_ppages of mmu.c, there is a possible out-of-bounds write due to a race condition. This could lead to… |
| 2026-11-02 20:17:57 | [CVE-2026-59043](https://nvd.nist.gov/vuln/detail/CVE-2026-59043) |  |  | In arm_lpae_split_blk_unmap of io-pgtable-arm-common.c, there is a possible memory corruption due to a race condition.… |
| 2026-11-02 20:17:57 | [CVE-2026-59044](https://nvd.nist.gov/vuln/detail/CVE-2026-59044) |  |  | In multiple locations, there is a possible use-after-free due to a logic error in the code. This could lead to local es… |
| 2026-11-02 20:17:57 | [CVE-2026-59045](https://nvd.nist.gov/vuln/detail/CVE-2026-59045) |  |  | In multiple locations, there is a possible memory corruption due to a race condition. This could lead to local escalati… |
| 2026-11-02 20:17:57 | [CVE-2026-59046](https://nvd.nist.gov/vuln/detail/CVE-2026-59046) |  |  | In __pkvm_guest_relinquish_to_host of mem_protect.c, there is a possible out-of-bounds write due to improper input vali… |
| 2026-11-02 20:17:58 | [CVE-2026-59047](https://nvd.nist.gov/vuln/detail/CVE-2026-59047) |  |  | In multiple locations, there is a possible denial of service due to a logic error in the code. This could lead to local… |
| 2026-11-02 20:17:58 | [CVE-2026-59048](https://nvd.nist.gov/vuln/detail/CVE-2026-59048) |  |  | In rb_cpu_init of trace.c, there is a possible out-of-bounds read due to an incorrect bounds check. This could lead to… |
| 2026-11-02 20:18:02 | [CVE-2026-86365](https://nvd.nist.gov/vuln/detail/CVE-2026-86365) | Medium | 4.2 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Improper Input Validation vulnerability.… |
| 2026-11-02 20:18:03 | [CVE-2026-91893](https://nvd.nist.gov/vuln/detail/CVE-2026-91893) | High | 7.8 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Improper Privilege Management vulnerabili… |
| 2026-11-02 20:18:03 | [CVE-2026-91894](https://nvd.nist.gov/vuln/detail/CVE-2026-91894) | Medium | 6.7 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain a Least Privilege Violation vulnerability. A… |
| 2026-11-02 20:18:03 | [CVE-2026-91895](https://nvd.nist.gov/vuln/detail/CVE-2026-91895) | High | 7.1 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Incorrect Default Permissions vulnerabili… |
| 2026-11-02 20:18:04 | [CVE-2026-91896](https://nvd.nist.gov/vuln/detail/CVE-2026-91896) | Low | 3.9 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Authentication Bypass by Spoofing vulnera… |
| 2026-11-02 20:18:04 | [CVE-2026-91897](https://nvd.nist.gov/vuln/detail/CVE-2026-91897) | Medium | 6.4 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Improper Certificate Validation vulnerabi… |
| 2026-11-02 20:18:04 | [CVE-2026-91898](https://nvd.nist.gov/vuln/detail/CVE-2026-91898) | High | 8.1 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Improper Verification of Cryptographic Si… |
| 2026-11-02 20:18:04 | [CVE-2026-91899](https://nvd.nist.gov/vuln/detail/CVE-2026-91899) | Medium | 6.4 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Improper Verification of Cryptographic Si… |
| 2026-11-02 20:18:04 | [CVE-2026-91900](https://nvd.nist.gov/vuln/detail/CVE-2026-91900) | Medium | 5.8 | Dell Alienware Command Center (AWCC), version(s) Versions up to and including 6.14.20.0, contain(s) an Improper Authori… |
| 2026-11-02 20:18:04 | [CVE-2026-91901](https://nvd.nist.gov/vuln/detail/CVE-2026-91901) | Low | 3.5 | Dell Alienware Command Center (AWCC), versions prior to 6.14.54.0, contain an Improper Authorization in Handler for Cus… |
| 2026-11-02 20:18:05 | [CVE-2026-97718](https://nvd.nist.gov/vuln/detail/CVE-2026-97718) | Critical | 9.4 | CVE-2026-97718 Is a cross-site request forgery vulnerability in version 14.60 of the Secure Access server. Because of a… |

## Data source

Data comes from the [NVD API](https://nvd.nist.gov/developers/vulnerabilities),
provided by the National Institute of Standards and Technology (NIST). NVD data
is in the public domain. CVE identifiers are assigned by the
[CVE Program](https://www.cve.org/), operated by MITRE.

This product uses data from the NVD API but is not endorsed or certified by the NVD.
