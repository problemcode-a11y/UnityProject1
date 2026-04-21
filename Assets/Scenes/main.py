 
Repository navigation
Code
Issues
Pull requests
Agents
Actions
Projects
Security and quality
Insights
Commit 9e57263
OtspIII
OtspIII
committed
on Feb 1
Input updates
main
1 parent 
fbd44b1
 commit 
9e57263
File tree
Filter files…
Packages
manifest.json
packages-lock.json
ProjectSettings
5 files changed
+169
-65
lines changed
Search within code
 
‎Packages/manifest.json‎
+9
-6
Lines changed: 9 additions & 6 deletions
Original file line number	Diff line number	Diff line change
@@ -1,15 +1,17 @@
{
  "dependencies": {
    "com.unity.collab-proxy": "2.9.3",
    "com.unity.feature.2d": "2.0.1",
    "com.unity.collab-proxy": "2.11.2",
    "com.unity.feature.2d": "2.0.2",
    "com.unity.ide.rider": "3.0.38",
    "com.unity.ide.visualstudio": "2.0.23",
    "com.unity.multiplayer.center": "1.0.0",
    "com.unity.ide.visualstudio": "2.0.26",
    "com.unity.inputsystem": "1.17.0",
    "com.unity.multiplayer.center": "1.0.1",
    "com.unity.test-framework": "1.6.0",
    "com.unity.timeline": "1.8.9",
    "com.unity.timeline": "1.8.10",
    "com.unity.ugui": "2.0.0",
    "com.unity.visualscripting": "1.9.7",
    "com.unity.visualscripting": "1.9.9",
    "com.unity.modules.accessibility": "1.0.0",
    "com.unity.modules.adaptiveperformance": "1.0.0",
    "com.unity.modules.ai": "1.0.0",
    "com.unity.modules.androidjni": "1.0.0",
    "com.unity.modules.animation": "1.0.0",
@@ -36,6 +38,7 @@
    "com.unity.modules.unitywebrequestaudio": "1.0.0",
    "com.unity.modules.unitywebrequesttexture": "1.0.0",
    "com.unity.modules.unitywebrequestwww": "1.0.0",
    "com.unity.modules.vectorgraphics": "1.0.0",
    "com.unity.modules.vehicles": "1.0.0",
    "com.unity.modules.video": "1.0.0",
    "com.unity.modules.vr": "1.0.0",
‎Packages/packages-lock.json‎
+82
-36
Lines changed: 82 additions & 36 deletions
Original file line number	Diff line number	Diff line change
@@ -1,57 +1,63 @@
{
  "dependencies": {
    "com.unity.2d.animation": {
      "version": "10.2.1",
      "version": "13.0.2",
      "depth": 1,
      "source": "registry",
      "dependencies": {
        "com.unity.2d.common": "9.1.1",
        "com.unity.2d.common": "12.0.1",
        "com.unity.2d.sprite": "1.0.0",
        "com.unity.collections": "1.2.4",
        "com.unity.collections": "2.4.3",
        "com.unity.modules.animation": "1.0.0",
        "com.unity.modules.uielements": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.2d.aseprite": {
      "version": "1.1.10",
      "version": "3.0.1",
      "depth": 1,
      "source": "registry",
      "dependencies": {
        "com.unity.2d.common": "6.0.6",
        "com.unity.2d.common": "12.0.1",
        "com.unity.2d.sprite": "1.0.0",
        "com.unity.2d.tilemap": "1.0.0",
        "com.unity.mathematics": "1.2.6",
        "com.unity.modules.animation": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.2d.common": {
      "version": "9.1.1",
      "version": "12.0.2",
      "depth": 2,
      "source": "registry",
      "dependencies": {
        "com.unity.burst": "1.8.4",
        "com.unity.2d.sprite": "1.0.0",
        "com.unity.collections": "2.4.3",
        "com.unity.mathematics": "1.1.0",
        "com.unity.modules.animation": "1.0.0",
        "com.unity.modules.uielements": "1.0.0"
        "com.unity.modules.uielements": "1.0.0",
        "com.unity.modules.imageconversion": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.2d.pixel-perfect": {
      "version": "5.0.3",
      "version": "5.1.1",
      "depth": 1,
      "source": "registry",
      "dependencies": {},
      "dependencies": {
        "com.unity.modules.imgui": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.2d.psdimporter": {
      "version": "9.1.0",
      "version": "12.0.1",
      "depth": 1,
      "source": "registry",
      "dependencies": {
        "com.unity.2d.common": "9.1.1",
        "com.unity.2d.sprite": "1.0.0"
        "com.unity.2d.common": "12.0.1",
        "com.unity.2d.sprite": "1.0.0",
        "com.unity.2d.tilemap": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
@@ -62,11 +68,11 @@
      "dependencies": {}
    },
    "com.unity.2d.spriteshape": {
      "version": "10.0.7",
      "version": "13.0.0",
      "depth": 1,
      "source": "registry",
      "dependencies": {
        "com.unity.2d.common": "9.0.7",
        "com.unity.2d.common": "12.0.0",
        "com.unity.mathematics": "1.1.0",
        "com.unity.modules.physics2d": "1.0.0"
      },
@@ -82,7 +88,7 @@
      }
    },
    "com.unity.2d.tilemap.extras": {
      "version": "4.1.0",
      "version": "6.0.1",
      "depth": 1,
      "source": "registry",
      "dependencies": {
@@ -92,8 +98,18 @@
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.2d.tooling": {
      "version": "1.0.2",
      "depth": 1,
      "source": "registry",
      "dependencies": {
        "com.unity.2d.common": "12.0.2",
        "com.unity.modules.uielements": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.burst": {
      "version": "1.8.25",
      "version": "1.8.27",
      "depth": 3,
      "source": "registry",
      "dependencies": {
@@ -103,20 +119,21 @@
      "url": "https://packages.unity.com"
    },
    "com.unity.collab-proxy": {
      "version": "2.9.3",
      "version": "2.11.2",
      "depth": 0,
      "source": "registry",
      "dependencies": {},
      "url": "https://packages.unity.com"
    },
    "com.unity.collections": {
      "version": "2.5.1",
      "version": "2.6.2",
      "depth": 2,
      "source": "registry",
      "dependencies": {
        "com.unity.burst": "1.8.17",
        "com.unity.test-framework": "1.4.5",
        "com.unity.nuget.mono-cecil": "1.11.4",
        "com.unity.burst": "1.8.23",
        "com.unity.mathematics": "1.3.2",
        "com.unity.test-framework": "1.4.6",
        "com.unity.nuget.mono-cecil": "1.11.5",
        "com.unity.test-framework.performance": "3.0.3"
      },
      "url": "https://packages.unity.com"
@@ -128,18 +145,19 @@
      "dependencies": {}
    },
    "com.unity.feature.2d": {
      "version": "2.0.1",
      "version": "2.0.2",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.2d.animation": "10.2.1",
        "com.unity.2d.pixel-perfect": "5.0.3",
        "com.unity.2d.psdimporter": "9.1.0",
        "com.unity.2d.animation": "13.0.2",
        "com.unity.2d.pixel-perfect": "5.1.1",
        "com.unity.2d.psdimporter": "12.0.1",
        "com.unity.2d.sprite": "1.0.0",
        "com.unity.2d.spriteshape": "10.0.7",
        "com.unity.2d.spriteshape": "13.0.0",
        "com.unity.2d.tilemap": "1.0.0",
        "com.unity.2d.tilemap.extras": "4.1.0",
        "com.unity.2d.aseprite": "1.1.10"
        "com.unity.2d.tilemap.extras": "6.0.1",
        "com.unity.2d.aseprite": "3.0.1",
        "com.unity.2d.tooling": "1.0.2"
      }
    },
    "com.unity.ide.rider": {
@@ -152,31 +170,40 @@
      "url": "https://packages.unity.com"
    },
    "com.unity.ide.visualstudio": {
      "version": "2.0.23",
      "version": "2.0.26",
      "depth": 0,
      "source": "registry",
      "dependencies": {
        "com.unity.test-framework": "1.1.33"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.inputsystem": {
      "version": "1.17.0",
      "depth": 0,
      "source": "registry",
      "dependencies": {
        "com.unity.test-framework": "1.1.9"
        "com.unity.modules.uielements": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.mathematics": {
      "version": "1.3.2",
      "version": "1.3.3",
      "depth": 2,
      "source": "registry",
      "dependencies": {},
      "url": "https://packages.unity.com"
    },
    "com.unity.multiplayer.center": {
      "version": "1.0.0",
      "version": "1.0.1",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.uielements": "1.0.0"
      }
    },
    "com.unity.nuget.mono-cecil": {
      "version": "1.11.4",
      "version": "1.11.6",
      "depth": 3,
      "source": "registry",
      "dependencies": {},
@@ -203,7 +230,7 @@
      "url": "https://packages.unity.com"
    },
    "com.unity.timeline": {
      "version": "1.8.9",
      "version": "1.8.10",
      "depth": 0,
      "source": "registry",
      "dependencies": {
@@ -224,7 +251,7 @@
      }
    },
    "com.unity.visualscripting": {
      "version": "1.9.7",
      "version": "1.9.9",
      "depth": 0,
      "source": "registry",
      "dependencies": {
@@ -239,6 +266,14 @@
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.adaptiveperformance": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.subsystems": "1.0.0"
      }
    },
    "com.unity.modules.ai": {
      "version": "1.0.0",
      "depth": 0,
@@ -381,7 +416,8 @@
        "com.unity.modules.ui": "1.0.0",
        "com.unity.modules.imgui": "1.0.0",
        "com.unity.modules.jsonserialize": "1.0.0",
        "com.unity.modules.hierarchycore": "1.0.0"
        "com.unity.modules.hierarchycore": "1.0.0",
        "com.unity.modules.physics": "1.0.0"
      }
    },
    "com.unity.modules.umbra": {
@@ -445,6 +481,16 @@
        "com.unity.modules.imageconversion": "1.0.0"
      }
    },
    "com.unity.modules.vectorgraphics": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.uielements": "1.0.0",
        "com.unity.modules.imageconversion": "1.0.0",
        "com.unity.modules.imgui": "1.0.0"
      }
    },
    "com.unity.modules.vehicles": {
      "version": "1.0.0",
      "depth": 0,
‎ProjectSettings/Packages/com.unity.dedicated-server/MultiplayerRolesSettings.asset‎
+17
Lines changed: 17 additions & 0 deletions
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,17 @@
%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!114 &1
MonoBehaviour:
  m_ObjectHideFlags: 53
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: 0}
  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {fileID: 15023, guid: 0000000000000000e000000000000000, type: 0}
  m_Name: 
  m_EditorClassIdentifier: UnityEditor.MultiplayerModule.dll::UnityEditor.Multiplayer.Internal.MultiplayerRolesSettings
  m_MultiplayerRoleForClassicProfile:
    m_Keys: []
    m_Values: 
‎ProjectSettings/ProjectSettings.asset‎
+59
-21
Lines changed: 59 additions & 21 deletions
Original file line number	Diff line number	Diff line change
@@ -3,7 +3,7 @@
--- !u!129 &1
PlayerSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 26
  serializedVersion: 28
  productGUID: 1b92c460b58cd1f4dba804b233db4062
  AndroidProfiler: 0
  AndroidFilterTouchesWhenObscured: 0
@@ -48,6 +48,8 @@ PlayerSettings:
  defaultScreenHeightWeb: 600
  m_StereoRenderingPath: 0
  m_ActiveColorSpace: 1
  unsupportedMSAAFallback: 0
  m_SpriteBatchMaxVertexCount: 65535
  m_SpriteBatchVertexThreshold: 300
  m_MTRendering: 1
  mipStripping: 0
@@ -68,20 +70,24 @@ PlayerSettings:
  androidStartInFullscreen: 1
  androidRenderOutsideSafeArea: 1
  androidUseSwappy: 1
  androidDisplayOptions: 1
  androidBlitType: 0
  androidResizableWindow: 0
  androidResizeableActivity: 0
  androidDefaultWindowWidth: 1920
  androidDefaultWindowHeight: 1080
  androidMinimumWindowWidth: 400
  androidMinimumWindowHeight: 300
  androidFullscreenMode: 1
  androidAutoRotationBehavior: 1
  androidPredictiveBackSupport: 1
  androidApplicationEntry: 1
  defaultIsNativeResolution: 1
  macRetinaSupport: 1
  runInBackground: 0
  captureSingleScreen: 0
  muteOtherAudioSources: 0
  Prepare IOS For Recording: 0
  Force IOS Speakers When Recording: 0
  audioSpatialExperience: 0
  deferSystemGesturesMode: 0
  hideHomeButton: 0
  submitAnalytics: 1
@@ -94,6 +100,7 @@ PlayerSettings:
  useMacAppStoreValidation: 0
  macAppStoreCategory: public.app-category.games
  gpuSkinning: 0
  meshDeformation: 0
  xboxPIXTextureCapture: 0
  xboxEnableAvatar: 0
  xboxEnableKinect: 0
@@ -125,16 +132,17 @@ PlayerSettings:
  switchAllowGpuScratchShrinking: 0
  switchNVNMaxPublicTextureIDCount: 0
  switchNVNMaxPublicSamplerIDCount: 0
  switchNVNGraphicsFirmwareMemory: 32
  switchMaxWorkerMultiple: 8
  stadiaPresentMode: 0
  stadiaTargetFramerate: 0
  switchNVNGraphicsFirmwareMemory: 32
  switchGraphicsJobsSyncAfterKick: 1
  vulkanNumSwapchainBuffers: 3
  vulkanEnableSetSRGBWrite: 0
  vulkanEnablePreTransform: 0
  vulkanEnableLateAcquireNextImage: 0
  vulkanEnableCommandBufferRecycling: 1
  loadStoreDebugModeEnabled: 0
  visionOSBundleVersion: 1.0
  tvOSBundleVersion: 1.0
  bundleVersion: 1.0
  preloadedAssets: []
  metroInputSource: 0
@@ -147,6 +155,7 @@ PlayerSettings:
  isWsaHolographicRemotingEnabled: 0
  enableFrameTimingStats: 0
  enableOpenGLProfilerGPURecorders: 1
  allowHDRDisplaySupport: 0
  useHDRDisplay: 0
  hdrBitDepth: 0
  m_ColorGamuts: 00000000
@@ -155,6 +164,7 @@ PlayerSettings:
  resetResolutionOnWindowResize: 0
  androidSupportedAspectRatio: 1
  androidMaxAspectRatio: 2.1
  androidMinAspectRatio: 1
  applicationIdentifier:
    Standalone: com.DefaultCompany.2DProject
  buildNumber:
@@ -164,26 +174,29 @@ PlayerSettings:
    tvOS: 0
  overrideDefaultApplicationIdentifier: 1
  AndroidBundleVersionCode: 1
  AndroidMinSdkVersion: 22
  AndroidMinSdkVersion: 25
  AndroidTargetSdkVersion: 0
  AndroidPreferredInstallLocation: 1
  AndroidPreferredDataLocation: 1
  aotOptions: 
  stripEngineCode: 1
  iPhoneStrippingLevel: 0
  iPhoneScriptCallOptimization: 0
  ForceInternetPermission: 0
  ForceSDCardPermission: 0
  CreateWallpaper: 0
  APKExpansionFiles: 0
  androidSplitApplicationBinary: 0
  keepLoadedShadersAlive: 0
  StripUnusedMeshComponents: 0
  strictShaderVariantMatching: 0
  VertexChannelCompressionMask: 4054
  iPhoneSdkVersion: 988
  iOSTargetOSVersionString: 12.0
  iOSSimulatorArchitecture: 0
  iOSTargetOSVersionString: 15.0
  tvOSSdkVersion: 0
  tvOSSimulatorArchitecture: 0
  tvOSRequireExtendedGameController: 0
  tvOSTargetOSVersionString: 12.0
  tvOSTargetOSVersionString: 15.0
  VisionOSSdkVersion: 0
  VisionOSTargetOSVersionString: 1.0
  uIPrerenderedIcon: 0
@@ -210,15 +223,13 @@ PlayerSettings:
    rgba: 0
  iOSLaunchScreenFillPct: 100
  iOSLaunchScreenSize: 100
  iOSLaunchScreenCustomXibPath: 
  iOSLaunchScreeniPadType: 0
  iOSLaunchScreeniPadImage: {fileID: 0}
  iOSLaunchScreeniPadBackgroundColor:
    serializedVersion: 2
    rgba: 0
  iOSLaunchScreeniPadFillPct: 100
  iOSLaunchScreeniPadSize: 100
  iOSLaunchScreeniPadCustomXibPath: 
  iOSLaunchScreenCustomStoryboardPath: 
  iOSLaunchScreeniPadCustomStoryboardPath: 
  iOSDeviceRequirements: []
@@ -228,6 +239,7 @@ PlayerSettings:
  iOSMetalForceHardShadows: 0
  metalEditorSupport: 1
  metalAPIValidation: 1
  metalCompileShaderBinary: 0
  iOSRenderExtraFrameOnPause: 0
  iosCopyPluginsCodeInsteadOfSymlink: 0
  appleDeveloperTeamID: 
@@ -254,15 +266,19 @@ PlayerSettings:
  useCustomGradleSettingsTemplate: 0
  useCustomProguardFile: 0
  AndroidTargetArchitectures: 1
  AndroidTargetDevices: 0
  AndroidAllowedArchitectures: -1
  AndroidSplashScreenScale: 0
  androidSplashScreen: {fileID: 0}
  AndroidKeystoreName: 
  AndroidKeyaliasName: 
  AndroidEnableArmv9SecurityFeatures: 0
  AndroidEnableArm64MTE: 0
  AndroidBuildApkPerCpuArchitecture: 0
  AndroidTVCompatibility: 0
  AndroidIsGame: 1
  androidAppCategory: 3
  useAndroidAppCategory: 1
  androidAppCategoryOther: 
  AndroidEnableTango: 0
  androidEnableBanner: 1
  androidUseLowAccuracyLocation: 0
@@ -272,11 +288,12 @@ PlayerSettings:
    height: 180
    banner: {fileID: 0}
  androidGamepadSupportLevel: 0
  chromeosInputEmulation: 1
  AndroidMinifyRelease: 0
  AndroidMinifyDebug: 0
  AndroidValidateAppBundleSize: 1
  AndroidAppBundleSizeToValidate: 150
  AndroidReportGooglePlayAppDependencies: 1
  androidSymbolsSizeThreshold: 800
  m_BuildTargetIcons: []
  m_BuildTargetPlatformIcons: []
  m_BuildTargetBatching: []
@@ -316,6 +333,9 @@ PlayerSettings:
  - m_BuildTarget: iOSSupport
    m_APIs: 10000000
    m_Automatic: 1
  - m_BuildTarget: WindowsStandaloneSupport
    m_APIs: 0200000012000000
    m_Automatic: 0
  m_BuildTargetVRSettings: []
  m_DefaultShaderChunkSizeInMB: 16
  m_DefaultShaderChunkCount: 0
@@ -333,27 +353,29 @@ PlayerSettings:
  m_BuildTargetGroupLoadStoreDebugModeSettings: []
  m_BuildTargetNormalMapEncoding: []
  m_BuildTargetDefaultTextureCompressionFormat:
  - m_BuildTarget: Android
    m_Format: 3
  - serializedVersion: 3
    m_BuildTarget: Android
    m_Formats: 03000000
  playModeTestRunnerEnabled: 0
  runPlayModeTestAsEditModeTest: 0
  actionOnDotNetUnhandledException: 1
  editorGfxJobOverride: 1
  enableInternalProfiler: 0
  logObjCUncaughtExceptions: 1
  enableCrashReportAPI: 0
  cameraUsageDescription: 
  locationUsageDescription: 
  microphoneUsageDescription: 
  bluetoothUsageDescription: 
  macOSTargetOSVersion: 10.13.0
  macOSTargetOSVersion: 12.0
  switchNMETAOverride: 
  switchNetLibKey: 
  switchSocketMemoryPoolSize: 6144
  switchSocketAllocatorPoolSize: 128
  switchSocketConcurrencyLimit: 14
  switchScreenResolutionBehavior: 2
  switchUseCPUProfiler: 0
  switchUseGOLDLinker: 0
  switchEnableFileSystemTrace: 0
  switchLTOSetting: 0
  switchApplicationID: 0x01004b9000490000
  switchNSODependencies: 
@@ -483,13 +505,14 @@ PlayerSettings:
  switchSocketBufferEfficiency: 4
  switchSocketInitializeEnabled: 1
  switchNetworkInterfaceManagerInitializeEnabled: 1
  switchPlayerConnectionEnabled: 1
  switchDisableHTCSPlayerConnection: 0
  switchUseNewStyleFilepaths: 0
  switchUseLegacyFmodPriorities: 0
  switchUseMicroSleepForYield: 1
  switchEnableRamDiskSupport: 0
  switchMicroSleepForYieldTime: 25
  switchRamDiskSpaceSize: 12
  switchUpgradedPlayerSettingsToNMETA: 0
  ps4NPAgeRating: 12
  ps4NPTitleSecret: 
  ps4NPTrophyPackPath: 
@@ -593,12 +616,18 @@ PlayerSettings:
  webGLMemoryGeometricGrowthStep: 0.2
  webGLMemoryGeometricGrowthCap: 96
  webGLPowerPreference: 2
  webGLWebAssemblyTable: 0
  webGLWebAssemblyBigInt: 0
  webGLCloseOnQuit: 0
  webWasm2023: 0
  webEnableSubmoduleStrippingCompatibility: 0
  scriptingDefineSymbols: {}
  additionalCompilerArguments: {}
  platformArchitecture: {}
  scriptingBackend: {}
  il2cppCompilerConfiguration: {}
  il2cppCodeGeneration: {}
  il2cppStacktraceInformation: {}
  managedStrippingLevel:
    EmbeddedLinux: 1
    GameCoreScarlett: 1
@@ -623,6 +652,7 @@ PlayerSettings:
  gcIncremental: 1
  gcWBarrierValidation: 0
  apiCompatibilityLevelPerPlatform: {}
  editorAssembliesCompatibilityLevel: 1
  m_RenderingPath: 1
  m_MobileRenderingPath: 1
  metroPackageName: DGD4 Part 2
@@ -646,6 +676,7 @@ PlayerSettings:
  metroTileBackgroundColor: {r: 0.13333334, g: 0.17254902, b: 0.21568628, a: 0}
  metroSplashScreenBackgroundColor: {r: 0.12941177, g: 0.17254902, b: 0.21568628, a: 1}
  metroSplashScreenUseBackgroundColor: 0
  syncCapabilities: 0
  platformCapabilities: {}
  metroTargetDeviceFamilies: {}
  metroFTAName: 
@@ -695,10 +726,12 @@ PlayerSettings:
  hmiPlayerDataPath: 
  hmiForceSRGBBlit: 1
  embeddedLinuxEnableGamepadInput: 1
  hmiLogStartupTiming: 0
  hmiCpuConfiguration: 
  hmiLogStartupTiming: 0
  qnxGraphicConfPath: 
  apiCompatibilityLevel: 6
  activeInputHandler: 0
  captureStartupLogs: {}
  activeInputHandler: 2
  windowsGamepadBackendHint: 0
  cloudProjectId: 
  framebufferDepthMemorylessMode: 0
@@ -711,3 +744,8 @@ PlayerSettings:
  platformRequiresReadableAssets: 0
  virtualTexturingSupportEnabled: 0
  insecureHttpOption: 0
  androidVulkanDenyFilterList: []
  androidVulkanAllowFilterList: []
  androidVulkanDeviceFilterListAsset: {fileID: 0}
  d3d12DeviceFilterListAsset: {fileID: 0}
  allowedHttpConnections: 3
‎ProjectSettings/ProjectVersion.txt‎
+2
-2
Lines changed: 2 additions & 2 deletions
Original file line number	Diff line number	Diff line change
@@ -1,2 +1,2 @@
m_EditorVersion: 6000.0.59f2
m_EditorVersionWithRevision: 6000.0.59f2 (ef281c76c3c1)
m_EditorVersion: 6000.3.5f1
m_EditorVersionWithRevision: 6000.3.5f1 (a1ec4b2f2d19)
0 commit comments
Comments
0
 (0)
Comment