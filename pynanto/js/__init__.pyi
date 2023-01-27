# @formatter:off

from typing import Awaitable, Sequence, Literal, overload
USVString = str


LandmarkType = Literal["mouth", "eye", "nose"]

BarcodeFormat = Literal["aztec", "code_128", "code_39", "code_93", "codabar", "data_matrix", "ean_13", "ean_8", "itf", "pdf417", "qr_code", "unknown", "upc_a", "upc_e"]

MockCapturePromptResult = Literal["granted", "denied"]

NavigationTimingType = Literal["navigate", "reload", "back_forward", "prerender"]

DevicePostureType = Literal["continuous", "folded", "folded-over"]

PermissionState = Literal["granted", "denied", "prompt"]

PaymentDelegation = Literal["shippingAddress", "payerName", "payerPhone", "payerEmail"]

PaymentShippingType = Literal["shipping", "delivery", "pickup"]

AnimationPlayState = Literal["idle", "running", "paused", "finished"]

AnimationReplaceState = Literal["active", "removed", "persisted"]

FillMode = Literal["none", "forwards", "backwards", "both", "auto"]

PlaybackDirection = Literal["normal", "reverse", "alternate", "alternate-reverse"]

CompositeOperation = Literal["replace", "add", "accumulate"]

CompositeOperationOrAuto = Literal["replace", "add", "accumulate", "auto"]

CredentialMediationRequirement = Literal["silent", "optional", "conditional", "required"]

MIDIPortType = Literal["input", "output"]

MIDIPortDeviceState = Literal["disconnected", "connected"]

MIDIPortConnectionState = Literal["open", "closed", "pending"]

ChildDisplayType = Literal["block", "normal"]

LayoutSizingMode = Literal["block-like", "manual"]

BlockFragmentationType = Literal["none", "page", "column", "region"]

BreakType = Literal["none", "line", "column", "page", "region"]

ParityType = Literal["none", "even", "odd"]

FlowControlType = Literal["none", "hardware"]

WebTransportReliabilityMode = Literal["pending", "reliable-only", "supports-unreliable"]

WebTransportCongestionControl = Literal["default", "throughput", "low-latency"]

WebTransportErrorSource = Literal["stream", "session"]

CookieSameSite = Literal["strict", "lax", "none"]

GamepadMappingType = Literal["", "standard", "xr-standard"]

MLDeviceType = Literal["cpu", "gpu"]

MLPowerPreference = Literal["default", "high-performance", "low-power"]

MLInputOperandLayout = Literal["nchw", "nhwc"]

MLOperandType = Literal["float32", "float16", "int32", "uint32", "int8", "uint8"]

MLConv2dFilterOperandLayout = Literal["oihw", "hwio", "ohwi", "ihwo"]

MLAutoPad = Literal["explicit", "same-upper", "same-lower"]

MLConvTranspose2dFilterOperandLayout = Literal["iohw", "hwoi", "ohwi"]

MLGruWeightLayout = Literal["zrn", "rzn"]

MLRecurrentNetworkDirection = Literal["forward", "backward", "both"]

MLLstmWeightLayout = Literal["iofg", "ifgo"]

MLPaddingMode = Literal["constant", "edge", "reflection", "symmetric"]

MLRoundingType = Literal["floor", "ceil"]

MLInterpolationMode = Literal["nearest-neighbor", "linear"]

MediaKeysRequirement = Literal["required", "optional", "not-allowed"]

MediaKeySessionType = Literal["temporary", "persistent-license"]

MediaKeySessionClosedReason = Literal["internal-error", "closed-by-application", "release-acknowledged", "hardware-context-reset", "resource-evicted"]

MediaKeyStatus = Literal["usable", "expired", "released", "output-restricted", "output-downscaled", "usable-in-future", "status-pending", "internal-error"]

MediaKeyMessageType = Literal["license-request", "license-renewal", "license-release", "individualization-request"]

MediaStreamTrackState = Literal["live", "ended"]

VideoFacingModeEnum = Literal["user", "environment", "left", "right"]

VideoResizeModeEnum = Literal["none", "crop-and-scale"]

MediaDeviceKind = Literal["audioinput", "audiooutput", "videoinput"]

NotificationPermission = Literal["default", "denied", "granted"]

NotificationDirection = Literal["auto", "ltr", "rtl"]

TaskPriority = Literal["user-blocking", "user-visible", "background"]

OrientationLockType = Literal["any", "natural", "landscape", "portrait", "portrait-primary", "portrait-secondary", "landscape-primary", "landscape-secondary"]

OrientationType = Literal["portrait-primary", "portrait-secondary", "landscape-primary", "landscape-secondary"]

ScrollBehavior = Literal["auto", "smooth"]

ScrollLogicalPosition = Literal["start", "center", "end", "nearest"]

CSSBoxType = Literal["margin", "border", "padding", "content"]

GPUPowerPreference = Literal["low-power", "high-performance"]

GPUFeatureName = Literal["depth-clip-control", "depth32float-stencil8", "texture-compression-bc", "texture-compression-etc2", "texture-compression-astc", "timestamp-query", "indirect-first-instance", "shader-f16", "rg11b10ufloat-renderable"]

GPUBufferMapState = Literal["unmapped", "pending", "mapped"]

GPUTextureDimension = Literal["1d", "2d", "3d"]

GPUTextureViewDimension = Literal["1d", "2d", "2d-array", "cube", "cube-array", "3d"]

GPUTextureAspect = Literal["all", "stencil-only", "depth-only"]

GPUTextureFormat = Literal["r8unorm", "r8snorm", "r8uint", "r8sint", "r16uint", "r16sint", "r16float", "rg8unorm", "rg8snorm", "rg8uint", "rg8sint", "r32uint", "r32sint", "r32float", "rg16uint", "rg16sint", "rg16float", "rgba8unorm", "rgba8unorm-srgb", "rgba8snorm", "rgba8uint", "rgba8sint", "bgra8unorm", "bgra8unorm-srgb", "rgb9e5ufloat", "rgb10a2unorm", "rg11b10ufloat", "rg32uint", "rg32sint", "rg32float", "rgba16uint", "rgba16sint", "rgba16float", "rgba32uint", "rgba32sint", "rgba32float", "stencil8", "depth16unorm", "depth24plus", "depth24plus-stencil8", "depth32float", "depth32float-stencil8", "bc1-rgba-unorm", "bc1-rgba-unorm-srgb", "bc2-rgba-unorm", "bc2-rgba-unorm-srgb", "bc3-rgba-unorm", "bc3-rgba-unorm-srgb", "bc4-r-unorm", "bc4-r-snorm", "bc5-rg-unorm", "bc5-rg-snorm", "bc6h-rgb-ufloat", "bc6h-rgb-float", "bc7-rgba-unorm", "bc7-rgba-unorm-srgb", "etc2-rgb8unorm", "etc2-rgb8unorm-srgb", "etc2-rgb8a1unorm", "etc2-rgb8a1unorm-srgb", "etc2-rgba8unorm", "etc2-rgba8unorm-srgb", "eac-r11unorm", "eac-r11snorm", "eac-rg11unorm", "eac-rg11snorm", "astc-4x4-unorm", "astc-4x4-unorm-srgb", "astc-5x4-unorm", "astc-5x4-unorm-srgb", "astc-5x5-unorm", "astc-5x5-unorm-srgb", "astc-6x5-unorm", "astc-6x5-unorm-srgb", "astc-6x6-unorm", "astc-6x6-unorm-srgb", "astc-8x5-unorm", "astc-8x5-unorm-srgb", "astc-8x6-unorm", "astc-8x6-unorm-srgb", "astc-8x8-unorm", "astc-8x8-unorm-srgb", "astc-10x5-unorm", "astc-10x5-unorm-srgb", "astc-10x6-unorm", "astc-10x6-unorm-srgb", "astc-10x8-unorm", "astc-10x8-unorm-srgb", "astc-10x10-unorm", "astc-10x10-unorm-srgb", "astc-12x10-unorm", "astc-12x10-unorm-srgb", "astc-12x12-unorm", "astc-12x12-unorm-srgb"]

GPUAddressMode = Literal["clamp-to-edge", "repeat", "mirror-repeat"]

GPUFilterMode = Literal["nearest", "linear"]

GPUMipmapFilterMode = Literal["nearest", "linear"]

GPUCompareFunction = Literal["never", "less", "equal", "less-equal", "greater", "not-equal", "greater-equal", "always"]

GPUBufferBindingType = Literal["uniform", "storage", "read-only-storage"]

GPUSamplerBindingType = Literal["filtering", "non-filtering", "comparison"]

GPUTextureSampleType = Literal["float", "unfilterable-float", "depth", "sint", "uint"]

GPUStorageTextureAccess = Literal["write-only"]

GPUCompilationMessageType = Literal["error", "warning", "info"]

GPUPipelineErrorReason = Literal["validation", "internal"]

GPUAutoLayoutMode = Literal["auto"]

GPUPrimitiveTopology = Literal["point-list", "line-list", "line-strip", "triangle-list", "triangle-strip"]

GPUFrontFace = Literal["ccw", "cw"]

GPUCullMode = Literal["none", "front", "back"]

GPUBlendFactor = Literal["zero", "one", "src", "one-minus-src", "src-alpha", "one-minus-src-alpha", "dst", "one-minus-dst", "dst-alpha", "one-minus-dst-alpha", "src-alpha-saturated", "constant", "one-minus-constant"]

GPUBlendOperation = Literal["add", "subtract", "reverse-subtract", "min", "max"]

GPUStencilOperation = Literal["keep", "zero", "replace", "invert", "increment-clamp", "decrement-clamp", "increment-wrap", "decrement-wrap"]

GPUIndexFormat = Literal["uint16", "uint32"]

GPUVertexFormat = Literal["uint8x2", "uint8x4", "sint8x2", "sint8x4", "unorm8x2", "unorm8x4", "snorm8x2", "snorm8x4", "uint16x2", "uint16x4", "sint16x2", "sint16x4", "unorm16x2", "unorm16x4", "snorm16x2", "snorm16x4", "float16x2", "float16x4", "float32", "float32x2", "float32x3", "float32x4", "uint32", "uint32x2", "uint32x3", "uint32x4", "sint32", "sint32x2", "sint32x3", "sint32x4"]

GPUVertexStepMode = Literal["vertex", "instance"]

GPUComputePassTimestampLocation = Literal["beginning", "end"]

GPURenderPassTimestampLocation = Literal["beginning", "end"]

GPULoadOp = Literal["load", "clear"]

GPUStoreOp = Literal["store", "discard"]

GPUQueryType = Literal["occlusion", "timestamp"]

GPUCanvasAlphaMode = Literal["opaque", "premultiplied"]

GPUDeviceLostReason = Literal["destroyed"]

GPUErrorFilter = Literal["validation", "out-of-memory", "internal"]

HighlightType = Literal["highlight", "spelling-error", "grammar-error"]

UserIdleState = Literal["active", "idle"]

ScreenIdleState = Literal["locked", "unlocked"]

PressureState = Literal["nominal", "fair", "serious", "critical"]

PressureFactor = Literal["thermal", "power-supply"]

PressureSource = Literal["cpu"]

ClientLifecycleState = Literal["active", "frozen"]

RTCStatsType = Literal["codec", "inbound-rtp", "outbound-rtp", "remote-inbound-rtp", "remote-outbound-rtp", "media-source", "media-playout", "peer-connection", "data-channel", "stream", "track", "transport", "candidate-pair", "local-candidate", "remote-candidate", "certificate"]

RTCQualityLimitationReason = Literal["none", "cpu", "bandwidth", "other"]

RTCDtlsRole = Literal["client", "server", "unknown"]

RTCStatsIceCandidatePairState = Literal["frozen", "waiting", "in-progress", "failed", "succeeded"]

CSSNumericBaseType = Literal["length", "angle", "time", "frequency", "resolution", "flex", "percent"]

CSSMathOperator = Literal["sum", "product", "negate", "invert", "min", "max", "clamp"]

AudioContextState = Literal["suspended", "running", "closed"]

AudioContextLatencyCategory = Literal["balanced", "interactive", "playback"]

AudioSinkType = Literal["none"]

ChannelCountMode = Literal["max", "clamped-max", "explicit"]

ChannelInterpretation = Literal["speakers", "discrete"]

AutomationRate = Literal["a-rate", "k-rate"]

BiquadFilterType = Literal["lowpass", "highpass", "bandpass", "lowshelf", "highshelf", "peaking", "notch", "allpass"]

OscillatorType = Literal["sine", "square", "sawtooth", "triangle", "custom"]

PanningModelType = Literal["equalpower", "HRTF"]

DistanceModelType = Literal["linear", "inverse", "exponential"]

OverSampleType = Literal["none", "2x", "4x"]

AutoKeyword = Literal["auto"]

DirectionSetting = Literal["", "rl", "lr"]

LineAlignSetting = Literal["start", "center", "end"]

PositionAlignSetting = Literal["line-left", "center", "line-right", "auto"]

AlignSetting = Literal["start", "center", "end", "left", "right"]

ScrollSetting = Literal["", "up"]

RTCIceTransportPolicy = Literal["relay", "all"]

RTCBundlePolicy = Literal["balanced", "max-compat", "max-bundle"]

RTCRtcpMuxPolicy = Literal["require"]

RTCSignalingState = Literal["stable", "have-local-offer", "have-remote-offer", "have-local-pranswer", "have-remote-pranswer", "closed"]

RTCIceGatheringState = Literal["new", "gathering", "complete"]

RTCPeerConnectionState = Literal["closed", "failed", "disconnected", "new", "connecting", "connected"]

RTCIceConnectionState = Literal["closed", "failed", "disconnected", "new", "checking", "completed", "connected"]

RTCSdpType = Literal["offer", "pranswer", "answer", "rollback"]

RTCIceProtocol = Literal["udp", "tcp"]

RTCIceTcpCandidateType = Literal["active", "passive", "so"]

RTCIceCandidateType = Literal["host", "srflx", "prflx", "relay"]

RTCIceServerTransportProtocol = Literal["udp", "tcp", "tls"]

RTCRtpTransceiverDirection = Literal["sendrecv", "sendonly", "recvonly", "inactive", "stopped"]

RTCDtlsTransportState = Literal["new", "connecting", "connected", "closed", "failed"]

RTCIceGathererState = Literal["new", "gathering", "complete"]

RTCIceTransportState = Literal["new", "checking", "connected", "completed", "disconnected", "failed", "closed"]

RTCIceRole = Literal["unknown", "controlling", "controlled"]

RTCIceComponent = Literal["rtp", "rtcp"]

RTCSctpTransportState = Literal["connecting", "connected", "closed"]

RTCDataChannelState = Literal["connecting", "open", "closing", "closed"]

RTCErrorDetailType = Literal["data-channel-failure", "dtls-failure", "fingerprint-failure", "sctp-failure", "sdp-syntax-error", "hardware-encoder-not-available", "hardware-encoder-error"]

ItemType = Literal["product", "subscription"]

RTCErrorDetailTypeIdp = Literal["idp-bad-script-failure", "idp-execution-failure", "idp-load-failure", "idp-need-login", "idp-timeout", "idp-tls-failure", "idp-token-expired", "idp-token-invalid"]

ConnectionType = Literal["bluetooth", "cellular", "ethernet", "mixed", "none", "other", "unknown", "wifi", "wimax"]

EffectiveConnectionType = Literal["2g", "3g", "4g", "slow-2g"]

TransactionAutomationMode = Literal["none", "autoAccept", "autoReject", "autoOptOut"]

LockMode = Literal["shared", "exclusive"]

CaptureStartFocusBehavior = Literal["focus-captured-surface", "no-focus-change"]

SelfCapturePreferenceEnum = Literal["include", "exclude"]

SystemAudioPreferenceEnum = Literal["include", "exclude"]

SurfaceSwitchingPreferenceEnum = Literal["include", "exclude"]

DisplayCaptureSurfaceType = Literal["monitor", "window", "browser"]

CursorCaptureConstraint = Literal["never", "always", "motion"]

MediaDecodingType = Literal["file", "media-source", "webrtc"]

MediaEncodingType = Literal["record", "webrtc"]

HdrMetadataType = Literal["smpteSt2086", "smpteSt2094-10", "smpteSt2094-40"]

ColorGamut = Literal["srgb", "p3", "rec2020"]

TransferFunction = Literal["srgb", "pq", "hlg"]

AppBannerPromptOutcome = Literal["accepted", "dismissed"]

JsonLdFramingErrorCode = Literal["invalid frame", "invalid @embed value"]

JsonLdEmbed = Literal["@always", "@once", "@never"]

XRDepthUsage = Literal["cpu-optimized", "gpu-optimized"]

XRDepthDataFormat = Literal["luminance-alpha", "float32"]

AccelerometerLocalCoordinateSystem = Literal["device", "screen"]

ScriptingPolicyViolationType = Literal["externalScript", "inlineScript", "inlineEventHandler", "eval"]

ResizeObserverBoxOptions = Literal["border-box", "content-box", "device-pixel-content-box"]

USBTransferStatus = Literal["ok", "stall", "babble"]

USBRequestType = Literal["standard", "class", "vendor"]

USBRecipient = Literal["device", "interface", "endpoint", "other"]

USBDirection = Literal["in", "out"]

USBEndpointType = Literal["bulk", "interrupt", "isochronous"]

XMLHttpRequestResponseType = Literal["", "arraybuffer", "blob", "document", "json", "text"]

XREnvironmentBlendMode = Literal["opaque", "alpha-blend", "additive"]

XRInteractionMode = Literal["screen-space", "world-space"]

ReferrerPolicy = Literal["", "no-referrer", "no-referrer-when-downgrade", "same-origin", "origin", "strict-origin", "origin-when-cross-origin", "strict-origin-when-cross-origin", "unsafe-url"]

HardwareAcceleration = Literal["no-preference", "prefer-hardware", "prefer-software"]

AlphaOption = Literal["keep", "discard"]

LatencyMode = Literal["quality", "realtime"]

CodecState = Literal["unconfigured", "configured", "closed"]

EncodedAudioChunkType = Literal["key", "delta"]

EncodedVideoChunkType = Literal["key", "delta"]

AudioSampleFormat = Literal["u8", "s16", "s32", "f32", "u8-planar", "s16-planar", "s32-planar", "f32-planar"]

VideoPixelFormat = Literal["I420", "I420A", "I422", "I444", "NV12", "RGBA", "RGBX", "BGRA", "BGRX"]

VideoColorPrimaries = Literal["bt709", "bt470bg", "smpte170m", "bt2020", "smpte432"]

VideoTransferCharacteristics = Literal["bt709", "smpte170m", "iec61966-2-1", "linear", "pq", "hlg"]

VideoMatrixCoefficients = Literal["rgb", "bt709", "bt470bg", "smpte170m", "bt2020-ncl"]

BackgroundFetchResult = Literal["", "success", "failure"]

BackgroundFetchFailureReason = Literal["", "aborted", "bad-status", "fetch-error", "quota-exceeded", "download-total-exceeded"]

FullscreenNavigationUI = Literal["auto", "show", "hide"]

HIDUnitSystem = Literal["none", "si-linear", "si-rotation", "english-linear", "english-rotation", "vendor-defined", "reserved"]

SecurityPolicyViolationEventDisposition = Literal["enforce", "report"]

RequestDestination = Literal["", "audio", "audioworklet", "document", "embed", "font", "frame", "iframe", "image", "manifest", "object", "paintworklet", "report", "script", "sharedworker", "style", "track", "video", "worker", "xslt"]

RequestMode = Literal["navigate", "same-origin", "no-cors", "cors"]

RequestCredentials = Literal["omit", "same-origin", "include"]

RequestCache = Literal["default", "no-store", "reload", "no-cache", "force-cache", "only-if-cached"]

RequestRedirect = Literal["follow", "error", "manual"]

RequestDuplex = Literal["half"]

RequestPriority = Literal["high", "low", "auto"]

ResponseType = Literal["basic", "cors", "default", "error", "opaque", "opaqueredirect"]

OTPCredentialTransportType = Literal["sms"]

MockSensorType = Literal["ambient-light", "accelerometer", "linear-acceleration", "gravity", "gyroscope", "magnetometer", "uncalibrated-magnetometer", "absolute-orientation", "relative-orientation", "geolocation", "proximity"]

AutoplayPolicy = Literal["allowed", "allowed-muted", "disallowed"]

AutoplayPolicyMediaType = Literal["mediaelement", "audiocontext"]

RedEyeReduction = Literal["never", "always", "controllable"]

FillLightMode = Literal["auto", "off", "flash"]

MeteringMode = Literal["none", "manual", "single-shot", "continuous"]

XRHandJoint = Literal["wrist", "thumb-metacarpal", "thumb-phalanx-proximal", "thumb-phalanx-distal", "thumb-tip", "index-finger-metacarpal", "index-finger-phalanx-proximal", "index-finger-phalanx-intermediate", "index-finger-phalanx-distal", "index-finger-tip", "middle-finger-metacarpal", "middle-finger-phalanx-proximal", "middle-finger-phalanx-intermediate", "middle-finger-phalanx-distal", "middle-finger-tip", "ring-finger-metacarpal", "ring-finger-phalanx-proximal", "ring-finger-phalanx-intermediate", "ring-finger-phalanx-distal", "ring-finger-tip", "pinky-finger-metacarpal", "pinky-finger-phalanx-proximal", "pinky-finger-phalanx-intermediate", "pinky-finger-phalanx-distal", "pinky-finger-tip"]

ReadableStreamReaderMode = Literal["byob"]

ReadableStreamType = Literal["bytes"]

ShadowRootMode = Literal["open", "closed"]

SlotAssignmentMode = Literal["manual", "named"]

IDBRequestReadyState = Literal["pending", "done"]

IDBTransactionDurability = Literal["default", "strict", "relaxed"]

IDBCursorDirection = Literal["next", "nextunique", "prev", "prevunique"]

IDBTransactionMode = Literal["readonly", "readwrite", "versionchange"]

BinaryType = Literal["blob", "arraybuffer"]

WebGLPowerPreference = Literal["default", "low-power", "high-performance"]

DocumentReadyState = Literal["loading", "interactive", "complete"]

DocumentVisibilityState = Literal["visible", "hidden"]

CanPlayTypeResult = Literal["", "maybe", "probably"]

TextTrackMode = Literal["disabled", "hidden", "showing"]

TextTrackKind = Literal["subtitles", "captions", "descriptions", "chapters", "metadata"]

SelectionMode = Literal["select", "start", "end", "preserve"]

PredefinedColorSpace = Literal["srgb", "display-p3"]

CanvasFillRule = Literal["nonzero", "evenodd"]

ImageSmoothingQuality = Literal["low", "medium", "high"]

CanvasLineCap = Literal["butt", "round", "square"]

CanvasLineJoin = Literal["round", "bevel", "miter"]

CanvasTextAlign = Literal["start", "end", "left", "right", "center"]

CanvasTextBaseline = Literal["top", "hanging", "middle", "alphabetic", "ideographic", "bottom"]

CanvasDirection = Literal["ltr", "rtl", "inherit"]

CanvasFontKerning = Literal["auto", "normal", "none"]

CanvasFontStretch = Literal["ultra-condensed", "extra-condensed", "condensed", "semi-condensed", "normal", "semi-expanded", "expanded", "extra-expanded", "ultra-expanded"]

CanvasFontVariantCaps = Literal["normal", "small-caps", "all-small-caps", "petite-caps", "all-petite-caps", "unicase", "titling-caps"]

CanvasTextRendering = Literal["auto", "optimizeSpeed", "optimizeLegibility", "geometricPrecision"]

OffscreenRenderingContextId = Literal["2d", "bitmaprenderer", "webgl", "webgl2", "webgpu"]

ScrollRestoration = Literal["auto", "manual"]

DOMParserSupportedType = Literal["text/html", "text/xml", "application/xml", "application/xhtml+xml", "image/svg+xml"]

ImageOrientation = Literal["from-image", "flipY"]

PremultiplyAlpha = Literal["none", "premultiply", "default"]

ColorSpaceConversion = Literal["none", "default"]

ResizeQuality = Literal["pixelated", "low", "medium", "high"]

WorkerType = Literal["classic", "module"]

PresentationConnectionState = Literal["connecting", "connected", "closed", "terminated"]

PresentationConnectionCloseReason = Literal["error", "closed", "wentaway"]

XRDOMOverlayType = Literal["screen", "floating", "head-locked"]

FileSystemPermissionMode = Literal["read", "readwrite"]

WellKnownDirectory = Literal["desktop", "documents", "downloads", "music", "pictures", "videos"]

XRReflectionFormat = Literal["srgba8", "rgba16f"]

RemotePlaybackState = Literal["connecting", "connected", "disconnected"]

AuthenticatorAttachment = Literal["platform", "cross-platform"]

ResidentKeyRequirement = Literal["discouraged", "preferred", "required"]

AttestationConveyancePreference = Literal["none", "indirect", "direct", "enterprise"]

TokenBindingStatus = Literal["present", "supported"]

PublicKeyCredentialType = Literal["public-key"]

AuthenticatorTransport = Literal["usb", "nfc", "ble", "hybrid", "internal"]

UserVerificationRequirement = Literal["required", "preferred", "discouraged"]

LargeBlobSupport = Literal["required", "preferred"]

XRHitTestTrackableType = Literal["point", "plane", "mesh"]

SpeechRecognitionErrorCode = Literal["no-speech", "aborted", "audio-capture", "network", "not-allowed", "service-not-allowed", "bad-grammar", "language-not-supported"]

SpeechSynthesisErrorCode = Literal["canceled", "interrupted", "audio-busy", "audio-hardware", "network", "synthesis-unavailable", "synthesis-failed", "language-unavailable", "voice-unavailable", "text-too-long", "invalid-argument", "not-allowed"]

SFrameTransformRole = Literal["encrypt", "decrypt"]

SFrameTransformErrorEventType = Literal["authentication", "keyID", "syntax"]

RTCEncodedVideoFrameType = Literal["empty", "key", "delta"]

SpatialNavigationDirection = Literal["up", "down", "left", "right"]

FocusableAreaSearchMode = Literal["visible", "all"]

FileSystemHandleKind = Literal["file", "directory"]

WriteCommandType = Literal["write", "seek", "truncate"]

ContentCategory = Literal["", "homepage", "article", "video", "audio"]

PushEncryptionKeyName = Literal["p256dh", "auth"]

JsonLdErrorCode = Literal["colliding keywords", "conflicting indexes", "context overflow", "cyclic IRI mapping", "invalid @id value", "invalid @import value", "invalid @included value", "invalid @index value", "invalid @nest value", "invalid @prefix value", "invalid @propagate value", "invalid @protected value", "invalid @reverse value", "invalid @version value", "invalid base direction", "invalid base IRI", "invalid container mapping", "invalid context entry", "invalid context nullification", "invalid default language", "invalid IRI mapping", "invalid JSON literal", "invalid keyword alias", "invalid language map value", "invalid language mapping", "invalid language-tagged string", "invalid language-tagged value", "invalid local context", "invalid remote context", "invalid reverse property map", "invalid reverse property value", "invalid reverse property", "invalid scoped context", "invalid script element", "invalid set or list object", "invalid term definition", "invalid type mapping", "invalid type value", "invalid typed value", "invalid value object value", "invalid value object", "invalid vocab mapping", "IRI confused with prefix", "keyword redefinition", "loading document failed", "loading remote context failed", "multiple context link headers", "processing mode conflict", "protected term redefinition"]

OrientationSensorLocalCoordinateSystem = Literal["device", "screen"]

BitrateMode = Literal["constant", "variable"]

RecordingState = Literal["inactive", "recording", "paused"]

CaptureAction = Literal["next", "previous", "first", "last"]

MediaSessionPlaybackState = Literal["none", "paused", "playing"]

MediaSessionAction = Literal["play", "pause", "seekbackward", "seekforward", "previoustrack", "nexttrack", "skipad", "stop", "seekto", "togglemicrophone", "togglecamera", "hangup", "previousslide", "nextslide"]

XRLayerLayout = Literal["default", "mono", "stereo", "stereo-left-right", "stereo-top-bottom"]

XRTextureType = Literal["texture", "texture-array"]

MagnetometerLocalCoordinateSystem = Literal["device", "screen"]

PresentationStyle = Literal["unspecified", "inline", "attachment"]

HevcBitstreamFormat = Literal["annexb", "hevc"]

ScrollAxis = Literal["block", "inline", "horizontal", "vertical"]

XRSessionMode = Literal["inline", "immersive-vr", "immersive-ar"]

XRVisibilityState = Literal["visible", "visible-blurred", "hidden"]

XRReferenceSpaceType = Literal["viewer", "local", "local-floor", "bounded-floor", "unbounded"]

XREye = Literal["none", "left", "right"]

XRHandedness = Literal["none", "left", "right"]

XRTargetRayMode = Literal["gaze", "tracked-pointer", "screen"]

GamepadHand = Literal["", "left", "right"]

GamepadHapticsResult = Literal["complete", "preempted"]

GamepadHapticActuatorType = Literal["vibration", "dual-rumble"]

GamepadHapticEffectType = Literal["dual-rumble"]

FontFaceLoadStatus = Literal["unloaded", "loading", "loaded", "error"]

FontFaceSetLoadStatus = Literal["loading", "loaded"]

ReadyState = Literal["closed", "open", "ended"]

EndOfStreamError = Literal["network", "decode"]

AppendMode = Literal["segments", "sequence"]

TouchType = Literal["direct", "stylus"]

ServiceWorkerState = Literal["parsed", "installing", "installed", "activating", "activated", "redundant"]

ServiceWorkerUpdateViaCache = Literal["imports", "all", "none"]

FrameType = Literal["auxiliary", "top-level", "nested", "none"]

ClientType = Literal["window", "worker", "sharedworker", "all"]

ContactProperty = Literal["address", "email", "icon", "name", "tel"]

WakeLockType = Literal["screen"]

OpusBitstreamFormat = Literal["opus", "ogg"]

AvcBitstreamFormat = Literal["annexb", "avc"]

ImportExportKind = Literal["function", "table", "memory", "global"]

TableKind = Literal["externref", "anyfunc"]

ValueType = Literal["i32", "i64", "f32", "f64", "v128", "externref", "anyfunc"]

GyroscopeLocalCoordinateSystem = Literal["device", "screen"]

AacBitstreamFormat = Literal["aac", "adts"]

IterationCompositeOperation = Literal["replace", "accumulate"]

EndingType = Literal["transparent", "native"]

PaymentComplete = Literal["fail", "success", "unknown"]

KeyType = Literal["public", "private", "secret"]

KeyUsage = Literal["encrypt", "decrypt", "sign", "verify", "deriveKey", "deriveBits", "wrapKey", "unwrapKey"]

KeyFormat = Literal["raw", "spki", "pkcs8", "jwk"]

RTCPriorityType = Literal["very-low", "low", "medium", "high"]

RTCDegradationPreference = Literal["maintain-framerate", "maintain-resolution", "balanced"]

NavigationHistoryBehavior = Literal["auto", "push", "replace"]

NavigationFocusReset = Literal["after-transition", "manual"]

NavigationScrollBehavior = Literal["after-transition", "manual"]

NavigationType = Literal["reload", "push", "replace", "traverse"]

RenderBlockingStatusType = Literal["blocking", "non-blocking"]

FileMode = Literal["readonly", "readwrite"]

PasswordCredentialInit = PasswordCredentialData | HTMLFormElement

CookieList = Sequence[CookieListItem]

MLNamedArrayBufferViews = ArrayBufferView

MLGPUResource = GPUBuffer | GPUTexture

MLNamedGPUResources = MLGPUResource

MLNamedOperands = MLOperand

MLBufferView = ArrayBufferView | MLBufferResourceView

ArrayBufferView = Int8Array | Int16Array | Int32Array | Uint8Array | Uint16Array | Uint32Array | Uint8ClampedArray | BigInt64Array | BigUint64Array | Float32Array | Float64Array | DataView

BufferSource = ArrayBufferView | ArrayBuffer

DOMTimeStamp = int

ConstrainULong = int | ConstrainULongRange

ConstrainDouble = float | ConstrainDoubleRange

ConstrainBoolean = bool | ConstrainBooleanParameters

ConstrainDOMString = str | Sequence[str] | ConstrainDOMStringParameters

DOMHighResTimeStamp = float

EpochTimeStamp = int

GeometryNode = Text | Element | CSSPseudoElement | Document

GPUBufferUsageFlags = int

GPUMapModeFlags = int

GPUTextureUsageFlags = int

GPUShaderStageFlags = int

GPUBindingResource = GPUSampler | GPUTextureView | GPUBufferBinding | GPUExternalTexture

GPUPipelineConstantValue = float

GPUColorWriteFlags = int

GPUComputePassTimestampWrites = Sequence[GPUComputePassTimestampWrite]

GPURenderPassTimestampWrites = Sequence[GPURenderPassTimestampWrite]

GPUBufferDynamicOffset = int

GPUStencilValue = int

GPUSampleMask = int

GPUDepthBias = int

GPUSize64 = int

GPUIntegerCoordinate = int

GPUIndex32 = int

GPUSize32 = int

GPUSignedOffset32 = int

GPUFlagsConstant = int

GPUColor = Sequence[float] | GPUColorDict

GPUOrigin2D = Sequence[GPUIntegerCoordinate] | GPUOrigin2DDict

GPUOrigin3D = Sequence[GPUIntegerCoordinate] | GPUOrigin3DDict

GPUExtent3D = Sequence[GPUIntegerCoordinate] | GPUExtent3DDict

CSSUnparsedSegment = USVString | CSSVariableReferenceValue

CSSKeywordish = str | CSSKeywordValue

CSSNumberish = float | CSSNumericValue

CSSPerspectiveValue = CSSNumericValue | CSSKeywordish

CSSColorRGBComp = CSSNumberish | CSSKeywordish

CSSColorPercent = CSSNumberish | CSSKeywordish

CSSColorNumber = CSSNumberish | CSSKeywordish

CSSColorAngle = CSSNumberish | CSSKeywordish

LineAndPositionSetting = float | AutoKeyword

Megabit = float

Millisecond = int

PerformanceEntryList = Sequence[PerformanceEntry]

FormDataEntryValue = File | USVString

HTMLString = str

ScriptString = str

ScriptURLString = USVString

TrustedType = TrustedHTML | TrustedScript | TrustedScriptURL

ImageBufferSource = BufferSource | ReadableStream

HeadersInit = Sequence[Sequence[ByteString]] | ByteString

XMLHttpRequestBodyInit = Blob | BufferSource | FormData | URLSearchParams | USVString

BodyInit = ReadableStream | XMLHttpRequestBodyInit

RequestInfo = Request | USVString

ConstrainPoint2D = Sequence[Point2D] | ConstrainPoint2DParameters

ReadableStreamReader = ReadableStreamDefaultReader | ReadableStreamBYOBReader

ReadableStreamController = ReadableStreamDefaultController | ReadableByteStreamController

GLuint64EXT = int

GLenum = int

GLboolean = bool

GLbitfield = int

GLbyte = byte

GLshort = short

GLint = int

GLsizei = int

GLintptr = int

GLsizeiptr = int

GLubyte = octet

GLushort = int

GLuint = int

GLfloat = float

GLclampf = float

TexImageSource = ImageBitmap | ImageData | HTMLImageElement | HTMLCanvasElement | HTMLVideoElement | OffscreenCanvas | VideoFrame

Float32List = Float32Array | Sequence[GLfloat]

Int32List = Int32Array | Sequence[GLint]

HTMLOrSVGScriptElement = HTMLScriptElement | SVGScriptElement

MediaProvider = MediaStream | MediaSource | Blob

RenderingContext = CanvasRenderingContext2D | ImageBitmapRenderingContext | WebGLRenderingContext | WebGL2RenderingContext | GPUCanvasContext

HTMLOrSVGImageElement = HTMLImageElement | SVGImageElement

CanvasImageSource = HTMLOrSVGImageElement | HTMLVideoElement | HTMLCanvasElement | ImageBitmap | OffscreenCanvas | VideoFrame

OffscreenRenderingContext = OffscreenCanvasRenderingContext2D | ImageBitmapRenderingContext | WebGLRenderingContext | WebGL2RenderingContext | GPUCanvasContext

EventHandler = EventHandlerNonNull | None

OnErrorEventHandler = OnErrorEventHandlerNonNull | None

OnBeforeUnloadEventHandler = OnBeforeUnloadEventHandlerNonNull | None

TimerHandler = str | Function

ImageBitmapSource = CanvasImageSource | Blob | ImageData

MessageEventSource = WindowProxy | MessagePort | ServiceWorker

StartInDirectory = WellKnownDirectory | FileSystemHandle

Base64URLString = str

PublicKeyCredentialJSON = RegistrationResponseJSON | AuthenticationResponseJSON

COSEAlgorithmIdentifier = int

UvmEntry = Sequence[int]

UvmEntries = Sequence[UvmEntry]

RTCRtpTransform = SFrameTransform | RTCRtpScriptTransform

SmallCryptoKeyID = int

CryptoKeyID = SmallCryptoKeyID | bigint

FileSystemWriteChunkType = BufferSource | Blob | USVString | WriteParams

GLint64 = int

GLuint64 = int

Uint32List = Uint32Array | Sequence[GLuint]

PushMessageDataInit = BufferSource | USVString

ProfilerResource = str

JsonLdInput = JsonLdRecord | Sequence[JsonLdRecord] | USVString | RemoteDocument

JsonLdContext = JsonLdRecord | Sequence[JsonLdRecord | USVString] | USVString

ReportList = Sequence[Report]

RotationMatrixType = Float32Array | Float64Array | DOMMatrix

AttributeMatchList = Sequence[str]

CSSStringSource = str | ReadableStream

CSSToken = str | CSSStyleValue | CSSParserValue

ClipboardItemData = Awaitable[str | Blob]

ClipboardItems = Sequence[ClipboardItem]

UUID = str

BluetoothServiceUUID = str | int

BluetoothCharacteristicUUID = str | int

BluetoothDescriptorUUID = str | int

URLPatternInput = USVString | URLPatternInit

XRWebGLRenderingContext = WebGLRenderingContext | WebGL2RenderingContext

BinaryData = ArrayBuffer | ArrayBufferView

VibratePattern = int | Sequence[int]

BlobPart = BufferSource | Blob | USVString

AlgorithmIdentifier = object | str

HashAlgorithmIdentifier = AlgorithmIdentifier

BigInteger = Uint8Array

NamedCurve = str

NDEFMessageSource = str | BufferSource | NDEFMessageInit

class EXT_blend_minmax: ...

class FaceDetector:
    def New(self, faceDetectorOptions: FaceDetectorOptions | None = {}) -> FaceDetector: ...
    def detect(self, image: ImageBitmapSource) -> Awaitable[Sequence[DetectedFace]]: ...

class BarcodeDetector:
    def New(self, barcodeDetectorOptions: BarcodeDetectorOptions | None = {}) -> BarcodeDetector: ...
    def detect(self, image: ImageBitmapSource) -> Awaitable[Sequence[DetectedBarcode]]: ...

class Navigator(NavigatorBadge, NavigatorML, NavigatorGPU, NavigatorDeviceMemory, NavigatorNetworkInformation, NavigatorAutomationInformation, NavigatorLocks, NavigatorStorage, NavigatorID, NavigatorLanguage, NavigatorOnLine, NavigatorContentUtils, NavigatorCookies, NavigatorPlugins, NavigatorConcurrentHardware, NavigatorUA):
    def sendBeacon(self, url: USVString, data: BodyInit | None = None) -> bool: ...
    def setClientBadge(self, contents: int | None = None) -> Awaitable[None]: ...
    def clearClientBadge(self) -> Awaitable[None]: ...
    geolocation: Geolocation
    devicePosture: DevicePosture
    permissions: Permissions
    credentials: CredentialsContainer
    def requestMIDIAccess(self, options: MIDIOptions | None = {}) -> Awaitable[MIDIAccess]: ...
    serial: Serial
    def getGamepads(self) -> Sequence[Gamepad | None]: ...
    def requestMediaKeySystemAccess(self, keySystem: str, supportedConfigurations: Sequence[MediaKeySystemConfiguration]) -> Awaitable[MediaKeySystemAccess]: ...
    mediaDevices: MediaDevices
    def getUserMedia(self, constraints: MediaStreamConstraints, successCallback: NavigatorUserMediaSuccessCallback, errorCallback: NavigatorUserMediaErrorCallback): ...
    def getBattery(self) -> Awaitable[BatteryManager]: ...
    mediaCapabilities: MediaCapabilities
    def getInstalledRelatedApps(self) -> Awaitable[Sequence[RelatedApplication]]: ...
    scheduling: Scheduling
    usb: USB
    windowControlsOverlay: WindowControlsOverlay
    ink: Ink
    hid: HID
    @overload
    def getAutoplayPolicy(self, type: AutoplayPolicyMediaType) -> AutoplayPolicy: ...
    @overload
    def getAutoplayPolicy(self, element: HTMLMediaElement) -> AutoplayPolicy: ...
    @overload
    def getAutoplayPolicy(self, context: AudioContext) -> AutoplayPolicy: ...
    epubReadingSystem: EpubReadingSystem
    userActivation: UserActivation
    def share(self, data: ShareData | None = {}) -> Awaitable[None]: ...
    def canShare(self, data: ShareData | None = {}) -> bool: ...
    presentation: Presentation
    mediaSession: MediaSession
    clipboard: Clipboard
    bluetooth: Bluetooth
    xr: XRSystem
    keyboard: Keyboard
    serviceWorker: ServiceWorkerContainer
    contacts: ContactsManager
    wakeLock: WakeLock
    virtualKeyboard: VirtualKeyboard
    maxTouchPoints: int
    def vibrate(self, pattern: VibratePattern) -> bool: ...

class PerformanceLongTaskTiming(PerformanceEntry):
    attribution: Sequence[TaskAttributionTiming]
    def toJSON(self) -> object: ...

class TaskAttributionTiming(PerformanceEntry):
    containerType: str
    containerSrc: str
    containerId: str
    containerName: str
    def toJSON(self) -> object: ...

class NavigatorBadge:
    def setAppBadge(self, contents: int | None = None) -> Awaitable[None]: ...
    def clearAppBadge(self) -> Awaitable[None]: ...

class WorkerNavigator(NavigatorBadge, NavigatorML, NavigatorGPU, NavigatorDeviceMemory, NavigatorNetworkInformation, NavigatorLocks, NavigatorStorage, NavigatorID, NavigatorLanguage, NavigatorOnLine, NavigatorConcurrentHardware, NavigatorUA):
    permissions: Permissions
    serial: Serial
    mediaCapabilities: MediaCapabilities
    usb: USB
    hid: HID
    serviceWorker: ServiceWorkerContainer

class Element(Node, Animatable, GeometryUtils, ParentNode, NonDocumentTypeChildNode, ChildNode, Slottable, InnerHTML, Region, ARIAMixin):
    editContext: EditContext | None
    part: DOMTokenList
    def getClientRects(self) -> DOMRectList: ...
    def getBoundingClientRect(self) -> DOMRect: ...
    def checkVisibility(self, options: CheckVisibilityOptions | None = {}) -> bool: ...
    def scrollIntoView(self, arg: bool | ScrollIntoViewOptions | None = {}): ...
    @overload
    def scroll(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scroll(self, x: float, y: float): ...
    @overload
    def scrollTo(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scrollTo(self, x: float, y: float): ...
    @overload
    def scrollBy(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scrollBy(self, x: float, y: float): ...
    scrollTop: float
    scrollLeft: float
    scrollWidth: int
    scrollHeight: int
    clientTop: int
    clientLeft: int
    clientWidth: int
    clientHeight: int
    def computedStyleMap(self) -> StylePropertyMapReadOnly: ...
    def requestPointerLock(self): ...
    elementTiming: str
    def requestFullscreen(self, options: FullscreenOptions | None = {}) -> Awaitable[None]: ...
    onfullscreenchange: EventHandler
    onfullscreenerror: EventHandler
    def pseudo(self, type: CSSOMString) -> CSSPseudoElement | None: ...
    namespaceURI: str | None
    prefix: str | None
    localName: str
    tagName: str
    id: str
    className: str
    classList: DOMTokenList
    slot: str
    def hasAttributes(self) -> bool: ...
    attributes: NamedNodeMap
    def getAttributeNames(self) -> Sequence[str]: ...
    def getAttribute(self, qualifiedName: str) -> str | None: ...
    def getAttributeNS(self, namespace: str | None, localName: str) -> str | None: ...
    def setAttribute(self, qualifiedName: str, value: str): ...
    def setAttributeNS(self, namespace: str | None, qualifiedName: str, value: str): ...
    def removeAttribute(self, qualifiedName: str): ...
    def removeAttributeNS(self, namespace: str | None, localName: str): ...
    def toggleAttribute(self, qualifiedName: str, force: bool | None = None) -> bool: ...
    def hasAttribute(self, qualifiedName: str) -> bool: ...
    def hasAttributeNS(self, namespace: str | None, localName: str) -> bool: ...
    def getAttributeNode(self, qualifiedName: str) -> Attr | None: ...
    def getAttributeNodeNS(self, namespace: str | None, localName: str) -> Attr | None: ...
    def setAttributeNode(self, attr: Attr) -> Attr | None: ...
    def setAttributeNodeNS(self, attr: Attr) -> Attr | None: ...
    def removeAttributeNode(self, attr: Attr) -> Attr: ...
    def attachShadow(self, init: ShadowRootInit) -> ShadowRoot: ...
    shadowRoot: ShadowRoot | None
    def closest(self, selectors: str) -> Element | None: ...
    def matches(self, selectors: str) -> bool: ...
    def webkitMatchesSelector(self, selectors: str) -> bool: ...
    def getElementsByTagName(self, qualifiedName: str) -> HTMLCollection: ...
    def getElementsByTagNameNS(self, namespace: str | None, localName: str) -> HTMLCollection: ...
    def getElementsByClassName(self, classNames: str) -> HTMLCollection: ...
    def insertAdjacentElement(self, where: str, element: Element) -> Element | None: ...
    def insertAdjacentText(self, where: str, data: str): ...
    outerHTML: str
    def insertAdjacentHTML(self, position: str, text: str): ...
    def getSpatialNavigationContainer(self) -> Node: ...
    def focusableAreas(self, option: FocusableAreasOption | None = {}) -> Sequence[Node]: ...
    def spatialNavigationSearch(self, dir: SpatialNavigationDirection, options: SpatialNavigationSearchOptions | None = {}) -> Node | None: ...
    def setHTML(self, input: str, options: SetHTMLOptions | None = {}): ...
    def setPointerCapture(self, pointerId: int): ...
    def releasePointerCapture(self, pointerId: int): ...
    def hasPointerCapture(self, pointerId: int) -> bool: ...

class EditContext(EventTarget):
    def New(self, options: EditContextInit | None = {}) -> EditContext: ...
    def updateText(self, rangeStart: int, rangeEnd: int, text: str): ...
    def updateSelection(self, start: int, end: int): ...
    def updateControlBound(self, controlBound: DOMRect): ...
    def updateSelectionBound(self, selectionBound: DOMRect): ...
    def updateCharacterBounds(self, rangeStart: int, characterBounds: Sequence[DOMRect]): ...
    def attachedElements(self) -> Sequence[Element]: ...
    text: str
    selectionStart: int
    selectionEnd: int
    compositionRangeStart: int
    compositionRangeEnd: int
    isInComposition: bool
    controlBound: DOMRect
    selectionBound: DOMRect
    characterBoundsRangeStart: int
    def characterBounds(self) -> Sequence[DOMRect]: ...
    ontextupdate: EventHandler
    ontextformatupdate: EventHandler
    oncharacterboundsupdate: EventHandler
    oncompositionstart: EventHandler
    oncompositionend: EventHandler

class TextUpdateEvent(Event):
    def New(self, options: TextUpdateEventInit | None = {}) -> TextUpdateEvent: ...
    updateRangeStart: int
    updateRangeEnd: int
    text: str
    selectionStart: int
    selectionEnd: int
    compositionStart: int
    compositionEnd: int

class TextFormat:
    def New(self, options: TextFormatInit | None = {}) -> TextFormat: ...
    rangeStart: int
    rangeEnd: int
    textColor: str
    backgroundColor: str
    underlineStyle: str
    underlineThickness: str
    underlineColor: str

class TextFormatUpdateEvent(Event):
    def New(self, options: TextFormatUpdateEventInit | None = {}) -> TextFormatUpdateEvent: ...
    def getTextFormats(self) -> Sequence[TextFormat]: ...

class CharacterBoundsUpdateEvent(Event):
    def New(self, options: CharacterBoundsUpdateEventInit | None = {}) -> CharacterBoundsUpdateEvent: ...
    rangeStart: int
    rangeEnd: int

class Screen:
    isExtended: bool
    onchange: EventHandler
    orientation: ScreenOrientation
    availWidth: int
    availHeight: int
    width: int
    height: int
    colorDepth: int
    pixelDepth: int

class Window(EventTarget, GlobalEventHandlers, WindowEventHandlers, WindowOrWorkerGlobalScope, AnimationFrameProvider, WindowSessionStorage, WindowLocalStorage):
    def getScreenDetails(self) -> Awaitable[ScreenDetails]: ...
    cookieStore: CookieStore
    launchQueue: LaunchQueue
    def matchMedia(self, query: CSSOMString) -> MediaQueryList: ...
    screen: Screen
    visualViewport: VisualViewport | None
    def moveTo(self, x: int, y: int): ...
    def moveBy(self, x: int, y: int): ...
    def resizeTo(self, width: int, height: int): ...
    def resizeBy(self, x: int, y: int): ...
    innerWidth: int
    innerHeight: int
    scrollX: float
    pageXOffset: float
    scrollY: float
    pageYOffset: float
    @overload
    def scroll(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scroll(self, x: float, y: float): ...
    @overload
    def scrollTo(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scrollTo(self, x: float, y: float): ...
    @overload
    def scrollBy(self, options: ScrollToOptions | None = {}): ...
    @overload
    def scrollBy(self, x: float, y: float): ...
    screenX: int
    screenLeft: int
    screenY: int
    screenTop: int
    outerWidth: int
    outerHeight: int
    devicePixelRatio: float
    def getDigitalGoodsService(self, serviceProvider: str) -> Awaitable[DigitalGoodsService]: ...
    onappinstalled: EventHandler
    onbeforeinstallprompt: EventHandler
    def queryLocalFonts(self, options: QueryOptions | None = {}) -> Awaitable[Sequence[FontData]]: ...
    def requestIdleCallback(self, callback: IdleRequestCallback, options: IdleRequestOptions | None = {}) -> int: ...
    def cancelIdleCallback(self, handle: int): ...
    def getSelection(self) -> Selection | None: ...
    event: Event | None
    window: WindowProxy
    self: WindowProxy
    document: Document
    name: str
    location: Location
    history: History
    customElements: CustomElementRegistry
    locationbar: BarProp
    menubar: BarProp
    personalbar: BarProp
    scrollbars: BarProp
    statusbar: BarProp
    toolbar: BarProp
    status: str
    def close(self): ...
    closed: bool
    def stop(self): ...
    def focus(self): ...
    def blur(self): ...
    frames: WindowProxy
    length: int
    top: WindowProxy | None
    parent: WindowProxy | None
    frameElement: Element | None
    def open(self, url: USVString | None = "", target: str | None = "_blank", features: str | None = "") -> WindowProxy | None: ...
    navigator: Navigator
    clientInformation: Navigator
    originAgentCluster: bool
    @overload
    def alert(self): ...
    @overload
    def alert(self, message: str): ...
    def confirm(self, message: str | None = "") -> bool: ...
    def prompt(self, message: str | None = "", default: str | None = "") -> str | None: ...
    def print(self): ...
    def captureEvents(self): ...
    def releaseEvents(self): ...
    external: External
    def showOpenFilePicker(self, options: OpenFilePickerOptions | None = {}) -> Awaitable[Sequence[FileSystemFileHandle]]: ...
    def showSaveFilePicker(self, options: SaveFilePickerOptions | None = {}) -> Awaitable[FileSystemFileHandle]: ...
    def showDirectoryPicker(self, options: DirectoryPickerOptions | None = {}) -> Awaitable[FileSystemDirectoryHandle]: ...
    orientation: short
    onorientationchange: EventHandler
    speechSynthesis: SpeechSynthesis
    def navigate(self, dir: SpatialNavigationDirection): ...
    portalHost: PortalHost | None
    def getComputedStyle(self, elt: Element, pseudoElt: CSSOMString | None = None) -> CSSStyleDeclaration: ...
    ondeviceorientation: EventHandler
    ondeviceorientationabsolute: EventHandler
    oncompassneedscalibration: EventHandler
    ondevicemotion: EventHandler
    navigation: Navigation

class ScreenDetails(EventTarget):
    screens: Sequence[ScreenDetailed]
    currentScreen: ScreenDetailed
    onscreenschange: EventHandler
    oncurrentscreenchange: EventHandler

class ScreenDetailed(Screen):
    availLeft: int
    availTop: int
    left: int
    top: int
    isPrimary: bool
    isInternal: bool
    devicePixelRatio: float
    label: str

class PerformanceNavigationTiming(PerformanceResourceTiming):
    unloadEventStart: DOMHighResTimeStamp
    unloadEventEnd: DOMHighResTimeStamp
    domInteractive: DOMHighResTimeStamp
    domContentLoadedEventStart: DOMHighResTimeStamp
    domContentLoadedEventEnd: DOMHighResTimeStamp
    domComplete: DOMHighResTimeStamp
    loadEventStart: DOMHighResTimeStamp
    loadEventEnd: DOMHighResTimeStamp
    type: NavigationTimingType
    redirectCount: int
    def toJSON(self) -> object: ...
    activationStart: DOMHighResTimeStamp

class PerformanceTiming:
    navigationStart: int
    unloadEventStart: int
    unloadEventEnd: int
    redirectStart: int
    redirectEnd: int
    fetchStart: int
    domainLookupStart: int
    domainLookupEnd: int
    connectStart: int
    connectEnd: int
    secureConnectionStart: int
    requestStart: int
    responseStart: int
    responseEnd: int
    domLoading: int
    domInteractive: int
    domContentLoadedEventStart: int
    domContentLoadedEventEnd: int
    domComplete: int
    loadEventStart: int
    loadEventEnd: int
    def toJSON(self) -> object: ...

class PerformanceNavigation:
    type: int
    redirectCount: int
    def toJSON(self) -> object: ...

class Performance(EventTarget):
    timing: PerformanceTiming
    navigation: PerformanceNavigation
    def now(self) -> DOMHighResTimeStamp: ...
    timeOrigin: DOMHighResTimeStamp
    def toJSON(self) -> object: ...
    def getEntries(self) -> PerformanceEntryList: ...
    def getEntriesByType(self, type: str) -> PerformanceEntryList: ...
    def getEntriesByName(self, name: str, type: str | None = None) -> PerformanceEntryList: ...
    def measureUserAgentSpecificMemory(self) -> Awaitable[MemoryMeasurement]: ...
    eventCounts: EventCounts
    interactionCount: int
    def mark(self, markName: str, markOptions: PerformanceMarkOptions | None = {}) -> PerformanceMark: ...
    def clearMarks(self, markName: str | None = None): ...
    def measure(self, measureName: str, startOrMeasureOptions: str | PerformanceMeasureOptions | None = {}, endMark: str | None = None) -> PerformanceMeasure: ...
    def clearMeasures(self, measureName: str | None = None): ...
    def clearResourceTimings(self): ...
    def setResourceTimingBufferSize(self, maxSize: int): ...
    onresourcetimingbufferfull: EventHandler

class Geolocation:
    def getCurrentPosition(self, successCallback: PositionCallback, errorCallback: PositionErrorCallback | None = None, options: PositionOptions | None = {}): ...
    def watchPosition(self, successCallback: PositionCallback, errorCallback: PositionErrorCallback | None = None, options: PositionOptions | None = {}) -> int: ...
    def clearWatch(self, watchId: int): ...

class GeolocationPosition:
    coords: GeolocationCoordinates
    timestamp: EpochTimeStamp

class GeolocationCoordinates:
    accuracy: float
    latitude: float
    longitude: float
    altitude: float | None
    altitudeAccuracy: float | None
    heading: float | None
    speed: float | None

class GeolocationPositionError:
    code: int
    message: str

class Permissions:
    def request(self, permissionDesc: object) -> Awaitable[PermissionStatus]: ...
    def query(self, permissionDesc: object) -> Awaitable[PermissionStatus]: ...
    def revoke(self, permissionDesc: object) -> Awaitable[PermissionStatus]: ...

class DevicePosture(EventTarget):
    type: DevicePostureType
    onchange: EventHandler

class PermissionStatus(EventTarget):
    state: PermissionState
    name: str
    onchange: EventHandler

class ServiceWorkerRegistration(EventTarget):
    paymentManager: PaymentManager
    cookies: CookieStoreManager
    def showNotification(self, title: str, options: NotificationOptions | None = {}) -> Awaitable[None]: ...
    def getNotifications(self, filter: GetNotificationOptions | None = {}) -> Awaitable[Sequence[Notification]]: ...
    backgroundFetch: BackgroundFetchManager
    index: ContentIndex
    pushManager: PushManager
    sync: SyncManager
    installing: ServiceWorker | None
    waiting: ServiceWorker | None
    active: ServiceWorker | None
    navigationPreload: NavigationPreloadManager
    scope: USVString
    updateViaCache: ServiceWorkerUpdateViaCache
    def update(self) -> Awaitable[None]: ...
    def unregister(self) -> Awaitable[bool]: ...
    onupdatefound: EventHandler
    periodicSync: PeriodicSyncManager

class PaymentManager:
    instruments: PaymentInstruments
    userHint: str
    def enableDelegations(self, delegations: Sequence[PaymentDelegation]) -> Awaitable[None]: ...

class PaymentInstruments:
    def delete(self, instrumentKey: str) -> Awaitable[bool]: ...
    def keys(self) -> Awaitable[Sequence[str]]: ...
    def has(self, instrumentKey: str) -> Awaitable[bool]: ...
    def set(self, instrumentKey: str, details: PaymentInstrument) -> Awaitable[None]: ...
    def clear(self) -> Awaitable[None]: ...

class ServiceWorkerGlobalScope(WorkerGlobalScope):
    oncanmakepayment: EventHandler
    onpaymentrequest: EventHandler
    cookieStore: CookieStore
    oncookiechange: EventHandler
    onnotificationclick: EventHandler
    onnotificationclose: EventHandler
    onbackgroundfetchsuccess: EventHandler
    onbackgroundfetchfail: EventHandler
    onbackgroundfetchabort: EventHandler
    onbackgroundfetchclick: EventHandler
    oncontentdelete: EventHandler
    onpush: EventHandler
    onpushsubscriptionchange: EventHandler
    onsync: EventHandler
    clients: Clients
    registration: ServiceWorkerRegistration
    serviceWorker: ServiceWorker
    def skipWaiting(self) -> Awaitable[None]: ...
    oninstall: EventHandler
    onactivate: EventHandler
    onfetch: EventHandler
    onmessage: EventHandler
    onmessageerror: EventHandler
    onperiodicsync: EventHandler

class CanMakePaymentEvent(ExtendableEvent):
    def New(self, type: str) -> CanMakePaymentEvent: ...
    def respondWith(self, canMakePaymentResponse: Awaitable[bool]): ...

class PaymentRequestEvent(ExtendableEvent):
    def New(self, type: str, eventInitDict: PaymentRequestEventInit | None = {}) -> PaymentRequestEvent: ...
    topOrigin: USVString
    paymentRequestOrigin: USVString
    paymentRequestId: str
    methodData: Sequence[PaymentMethodData]
    total: object
    modifiers: Sequence[PaymentDetailsModifier]
    paymentOptions: object | None
    shippingOptions: Sequence[PaymentShippingOption]
    def openWindow(self, url: USVString) -> Awaitable[WindowClient | None]: ...
    def changePaymentMethod(self, methodName: str, methodDetails: object | None = None) -> Awaitable[PaymentRequestDetailsUpdate | None]: ...
    def changeShippingAddress(self, shippingAddress: AddressInit | None = {}) -> Awaitable[PaymentRequestDetailsUpdate | None]: ...
    def changeShippingOption(self, shippingOption: str) -> Awaitable[PaymentRequestDetailsUpdate | None]: ...
    def respondWith(self, handlerResponsePromise: Awaitable[PaymentHandlerResponse]): ...

class AnimationTimeline:
    currentTime: float | None
    def getCurrentTime(self, rangeName: CSSOMString | None = None) -> CSSNumericValue | None: ...
    duration: CSSNumberish | None
    def play(self, effect: AnimationEffect | None = None) -> Animation: ...

class DocumentTimeline(AnimationTimeline):
    def New(self, options: DocumentTimelineOptions | None = {}) -> DocumentTimeline: ...

class Animation(EventTarget):
    def New(self, effect: AnimationEffect | None = None, timeline: AnimationTimeline | None = None) -> Animation: ...
    id: str
    effect: AnimationEffect | None
    timeline: AnimationTimeline | None
    playbackRate: float
    playState: AnimationPlayState
    replaceState: AnimationReplaceState
    pending: bool
    ready: Awaitable[Animation]
    finished: Awaitable[Animation]
    onfinish: EventHandler
    oncancel: EventHandler
    onremove: EventHandler
    def cancel(self): ...
    def finish(self): ...
    def play(self): ...
    def pause(self): ...
    def updatePlaybackRate(self, playbackRate: float): ...
    def reverse(self): ...
    def persist(self): ...
    def commitStyles(self): ...
    startTime: CSSNumberish | None
    currentTime: CSSNumberish | None

class AnimationEffect:
    def getTiming(self) -> EffectTiming: ...
    def getComputedTiming(self) -> ComputedEffectTiming: ...
    def updateTiming(self, timing: OptionalEffectTiming | None = {}): ...
    parent: GroupEffect | None
    previousSibling: AnimationEffect | None
    nextSibling: AnimationEffect | None
    def before(self, effects: AnimationEffect | None = None): ...
    def after(self, effects: AnimationEffect | None = None): ...
    def replace(self, effects: AnimationEffect | None = None): ...
    def remove(self): ...

class KeyframeEffect(AnimationEffect):
    @overload
    def New(self, target: Element | None, keyframes: object | None, options: float | KeyframeEffectOptions | None = {}) -> KeyframeEffect: ...
    @overload
    def New(self, source: KeyframeEffect) -> KeyframeEffect: ...
    target: Element | None
    pseudoElement: CSSOMString | None
    composite: CompositeOperation
    def getKeyframes(self) -> Sequence[object]: ...
    def setKeyframes(self, keyframes: object | None): ...
    iterationComposite: IterationCompositeOperation

class Animatable:
    def animate(self, keyframes: object | None, options: float | KeyframeAnimationOptions | None = {}) -> Animation: ...
    def getAnimations(self, options: GetAnimationsOptions | None = {}) -> Sequence[Animation]: ...

class Document(Node, GeometryUtils, NonElementParentNode, DocumentOrShadowRoot, ParentNode, XPathEvaluatorBase, GlobalEventHandlers, FontFaceSource):
    def New(self) -> Document: ...
    timeline: DocumentTimeline
    def elementFromPoint(self, x: float, y: float) -> Element | None: ...
    def elementsFromPoint(self, x: float, y: float) -> Sequence[Element]: ...
    def caretPositionFromPoint(self, x: float, y: float) -> CaretPosition | None: ...
    scrollingElement: Element | None
    onfreeze: EventHandler
    onresume: EventHandler
    wasDiscarded: bool
    onpointerlockchange: EventHandler
    onpointerlockerror: EventHandler
    def exitPointerLock(self): ...
    permissionsPolicy: PermissionsPolicy
    def getSelection(self) -> Selection | None: ...
    prerendering: bool
    onprerenderingchange: EventHandler
    def hasStorageAccess(self) -> Awaitable[bool]: ...
    def requestStorageAccess(self) -> Awaitable[None]: ...
    fullscreenEnabled: bool
    fullscreen: bool
    def exitFullscreen(self) -> Awaitable[None]: ...
    onfullscreenchange: EventHandler
    onfullscreenerror: EventHandler
    implementation: DOMImplementation
    URL: USVString
    documentURI: USVString
    compatMode: str
    characterSet: str
    charset: str
    inputEncoding: str
    contentType: str
    doctype: DocumentType | None
    documentElement: Element | None
    def getElementsByTagName(self, qualifiedName: str) -> HTMLCollection: ...
    def getElementsByTagNameNS(self, namespace: str | None, localName: str) -> HTMLCollection: ...
    def getElementsByClassName(self, classNames: str) -> HTMLCollection: ...
    def createElement(self, localName: str, options: str | ElementCreationOptions | None = {}) -> Element: ...
    def createElementNS(self, namespace: str | None, qualifiedName: str, options: str | ElementCreationOptions | None = {}) -> Element: ...
    def createDocumentFragment(self) -> DocumentFragment: ...
    def createTextNode(self, data: str) -> Text: ...
    def createCDATASection(self, data: str) -> CDATASection: ...
    def createComment(self, data: str) -> Comment: ...
    def createProcessingInstruction(self, target: str, data: str) -> ProcessingInstruction: ...
    def importNode(self, node: Node, deep: bool | None = false) -> Node: ...
    def adoptNode(self, node: Node) -> Node: ...
    def createAttribute(self, localName: str) -> Attr: ...
    def createAttributeNS(self, namespace: str | None, qualifiedName: str) -> Attr: ...
    def createEvent(self, interface: str) -> Event: ...
    def createRange(self) -> Range: ...
    def createNodeIterator(self, root: Node, whatToShow: int | None = 0xFFFFFFFF, filter: NodeFilter | None = None) -> NodeIterator: ...
    def createTreeWalker(self, root: Node, whatToShow: int | None = 0xFFFFFFFF, filter: NodeFilter | None = None) -> TreeWalker: ...
    location: Location | None
    domain: USVString
    referrer: USVString
    cookie: USVString
    lastModified: str
    readyState: DocumentReadyState
    title: str
    dir: str
    body: HTMLElement | None
    head: HTMLHeadElement | None
    images: HTMLCollection
    embeds: HTMLCollection
    plugins: HTMLCollection
    links: HTMLCollection
    forms: HTMLCollection
    scripts: HTMLCollection
    def getElementsByName(self, elementName: str) -> NodeList: ...
    currentScript: HTMLOrSVGScriptElement | None
    @overload
    def open(self, unused1: str | None = None, unused2: str | None = None) -> Document: ...
    @overload
    def open(self, url: USVString, name: str, features: str) -> WindowProxy | None: ...
    def close(self): ...
    def write(self, text: str | None = None): ...
    def writeln(self, text: str | None = None): ...
    defaultView: WindowProxy | None
    def hasFocus(self) -> bool: ...
    designMode: str
    def execCommand(self, commandId: str, showUI: bool | None = false, value: str | None = "") -> bool: ...
    def queryCommandEnabled(self, commandId: str) -> bool: ...
    def queryCommandIndeterm(self, commandId: str) -> bool: ...
    def queryCommandState(self, commandId: str) -> bool: ...
    def queryCommandSupported(self, commandId: str) -> bool: ...
    def queryCommandValue(self, commandId: str) -> str: ...
    hidden: bool
    visibilityState: DocumentVisibilityState
    onreadystatechange: EventHandler
    onvisibilitychange: EventHandler
    fgColor: str
    linkColor: str
    vlinkColor: str
    alinkColor: str
    bgColor: str
    anchors: HTMLCollection
    applets: HTMLCollection
    def clear(self): ...
    def captureEvents(self): ...
    def releaseEvents(self): ...
    all: HTMLAllCollection
    def startViewTransition(self, callback: UpdateCallback | None = None) -> ViewTransition: ...
    def measureElement(self, element: Element) -> FontMetrics: ...
    def measureText(self, text: str, styleMap: StylePropertyMapReadOnly) -> FontMetrics: ...
    fragmentDirective: FragmentDirective
    pictureInPictureEnabled: bool
    def exitPictureInPicture(self) -> Awaitable[None]: ...
    namedFlows: NamedFlowMap
    rootElement: SVGSVGElement | None

class DocumentOrShadowRoot:
    def getAnimations(self) -> Sequence[Animation]: ...
    pointerLockElement: Element | None
    fullscreenElement: Element | None
    activeElement: Element | None
    styleSheets: StyleSheetList
    adoptedStyleSheets: Sequence[CSSStyleSheet]
    pictureInPictureElement: Element | None

class WEBGL_draw_instanced_base_vertex_base_instance:
    def drawArraysInstancedBaseInstanceWEBGL(self, mode: GLenum, first: GLint, count: GLsizei, instanceCount: GLsizei, baseInstance: GLuint): ...
    def drawElementsInstancedBaseVertexBaseInstanceWEBGL(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr, instanceCount: GLsizei, baseVertex: GLint, baseInstance: GLuint): ...

class Credential:
    id: USVString
    type: str

class CredentialUserData:
    name: USVString
    iconURL: USVString

class CredentialsContainer:
    def get(self, options: CredentialRequestOptions | None = {}) -> Awaitable[Credential | None]: ...
    def store(self, credential: Credential) -> Awaitable[Credential]: ...
    def create(self, options: CredentialCreationOptions | None = {}) -> Awaitable[Credential | None]: ...
    def preventSilentAccess(self) -> Awaitable[None]: ...

class PasswordCredential(Credential, CredentialUserData):
    @overload
    def New(self, form: HTMLFormElement) -> PasswordCredential: ...
    @overload
    def New(self, data: PasswordCredentialData) -> PasswordCredential: ...
    password: USVString

class FederatedCredential(Credential, CredentialUserData):
    def New(self, data: FederatedCredentialInit) -> FederatedCredential: ...
    provider: USVString
    protocol: str | None

class MediaStreamTrackProcessor:
    def New(self, init: MediaStreamTrackProcessorInit) -> MediaStreamTrackProcessor: ...
    readable: ReadableStream

class VideoTrackGenerator:
    def New(self) -> VideoTrackGenerator: ...
    writable: WritableStream
    muted: bool
    track: MediaStreamTrack

class MIDIInputMap: ...

class MIDIOutputMap: ...

class MIDIAccess(EventTarget):
    inputs: MIDIInputMap
    outputs: MIDIOutputMap
    onstatechange: EventHandler
    sysexEnabled: bool

class MIDIPort(EventTarget):
    id: str
    manufacturer: str | None
    name: str | None
    type: MIDIPortType
    version: str | None
    state: MIDIPortDeviceState
    connection: MIDIPortConnectionState
    onstatechange: EventHandler
    def open(self) -> Awaitable[MIDIPort]: ...
    def close(self) -> Awaitable[MIDIPort]: ...

class MIDIInput(MIDIPort):
    onmidimessage: EventHandler

class MIDIOutput(MIDIPort):
    def send(self, data: Sequence[octet], timestamp: DOMHighResTimeStamp | None = 0): ...
    def clear(self): ...

class MIDIMessageEvent(Event):
    def New(self, type: str, eventInitDict: MIDIMessageEventInit | None = {}) -> MIDIMessageEvent: ...
    data: Uint8Array

class MIDIConnectionEvent(Event):
    def New(self, type: str, eventInitDict: MIDIConnectionEventInit | None = {}) -> MIDIConnectionEvent: ...
    port: MIDIPort

class OES_texture_half_float_linear: ...

class MediaDevices(EventTarget):
    def setCaptureHandleConfig(self, config: CaptureHandleConfig | None = {}): ...
    ondevicechange: EventHandler
    def enumerateDevices(self) -> Awaitable[Sequence[MediaDeviceInfo]]: ...
    def getSupportedConstraints(self) -> MediaTrackSupportedConstraints: ...
    def getUserMedia(self, constraints: MediaStreamConstraints | None = {}) -> Awaitable[MediaStream]: ...
    def getViewportMedia(self, constraints: ViewportMediaStreamConstraints | None = {}) -> Awaitable[MediaStream]: ...
    def getDisplayMedia(self, options: DisplayMediaStreamOptions | None = {}) -> Awaitable[MediaStream]: ...
    def setSupportedCaptureActions(self, actions: Sequence[str]): ...
    oncaptureaction: EventHandler
    def selectAudioOutput(self, options: AudioOutputOptions | None = {}) -> Awaitable[MediaDeviceInfo]: ...

class MediaStreamTrack(EventTarget):
    def getCaptureHandle(self) -> CaptureHandle | None: ...
    oncapturehandlechange: EventHandler
    kind: str
    id: str
    label: str
    enabled: bool
    muted: bool
    onmute: EventHandler
    onunmute: EventHandler
    readyState: MediaStreamTrackState
    onended: EventHandler
    def clone(self) -> MediaStreamTrack: ...
    def stop(self): ...
    def getCapabilities(self) -> MediaTrackCapabilities: ...
    def getConstraints(self) -> MediaTrackConstraints: ...
    def getSettings(self) -> MediaTrackSettings: ...
    def applyConstraints(self, constraints: MediaTrackConstraints | None = {}) -> Awaitable[None]: ...
    isolated: bool
    onisolationchange: EventHandler
    def getSupportedCaptureActions(self) -> Sequence[str]: ...
    def sendCaptureAction(self, action: CaptureAction) -> Awaitable[None]: ...
    contentHint: str

class LayoutWorkletGlobalScope(WorkletGlobalScope):
    def registerLayout(self, name: str, layoutCtor: VoidFunction): ...

class LayoutChild:
    styleMap: StylePropertyMapReadOnly
    def intrinsicSizes(self) -> Awaitable[IntrinsicSizes]: ...
    def layoutNextFragment(self, constraints: LayoutConstraintsOptions, breakToken: ChildBreakToken) -> Awaitable[LayoutFragment]: ...

class LayoutFragment:
    inlineSize: float
    blockSize: float
    inlineOffset: float
    blockOffset: float
    breakToken: ChildBreakToken | None

class IntrinsicSizes:
    minContentSize: float
    maxContentSize: float

class LayoutConstraints:
    availableInlineSize: float
    availableBlockSize: float
    fixedInlineSize: float | None
    fixedBlockSize: float | None
    percentageInlineSize: float
    percentageBlockSize: float
    blockFragmentationOffset: float | None
    blockFragmentationType: BlockFragmentationType

class ChildBreakToken:
    breakType: BreakType
    child: LayoutChild

class BreakToken:
    childBreakTokens: Sequence[ChildBreakToken]

class LayoutEdges:
    inlineStart: float
    inlineEnd: float
    blockStart: float
    blockEnd: float
    inline: float
    block: float

class FragmentResult:
    def New(self, options: FragmentResultOptions | None = {}) -> FragmentResult: ...
    inlineSize: float
    blockSize: float

class Serial(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler
    def getPorts(self) -> Awaitable[Sequence[SerialPort]]: ...
    def requestPort(self, options: SerialPortRequestOptions | None = {}) -> Awaitable[SerialPort]: ...

class SerialPort(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler
    readable: ReadableStream
    writable: WritableStream
    def getInfo(self) -> SerialPortInfo: ...
    def open(self, options: SerialOptions) -> Awaitable[None]: ...
    def setSignals(self, signals: SerialOutputSignals | None = {}) -> Awaitable[None]: ...
    def getSignals(self) -> Awaitable[SerialInputSignals]: ...
    def close(self) -> Awaitable[None]: ...
    def forget(self) -> Awaitable[None]: ...

class WebTransportDatagramDuplexStream:
    readable: ReadableStream
    writable: WritableStream
    maxDatagramSize: int
    incomingMaxAge: float | None
    outgoingMaxAge: float | None
    incomingHighWaterMark: int
    outgoingHighWaterMark: int

class WebTransport:
    def New(self, url: USVString, options: WebTransportOptions | None = {}) -> WebTransport: ...
    def getStats(self) -> Awaitable[WebTransportStats]: ...
    ready: Awaitable[None]
    reliability: WebTransportReliabilityMode
    congestionControl: WebTransportCongestionControl
    closed: Awaitable[WebTransportCloseInfo]
    def close(self, closeInfo: WebTransportCloseInfo | None = {}): ...
    datagrams: WebTransportDatagramDuplexStream
    def createBidirectionalStream(self, options: WebTransportSendStreamOptions | None = {}) -> Awaitable[WebTransportBidirectionalStream]: ...
    incomingBidirectionalStreams: ReadableStream
    def createUnidirectionalStream(self, options: WebTransportSendStreamOptions | None = {}) -> Awaitable[WebTransportSendStream]: ...
    incomingUnidirectionalStreams: ReadableStream

class WebTransportSendStream(WritableStream):
    def getStats(self) -> Awaitable[WebTransportSendStreamStats]: ...

class WebTransportReceiveStream(ReadableStream):
    def getStats(self) -> Awaitable[WebTransportReceiveStreamStats]: ...

class WebTransportBidirectionalStream:
    readable: WebTransportReceiveStream
    writable: WebTransportSendStream

class WebTransportError(DOMException):
    def New(self, init: WebTransportErrorInit | None = {}) -> WebTransportError: ...
    source: WebTransportErrorSource
    streamErrorCode: octet | None

class HTMLAttributionSrcElementUtils:
    attributionSrc: USVString

class HTMLAnchorElement(HTMLElement, HTMLAttributionSrcElementUtils, HTMLHyperlinkElementUtils):
    def New(self) -> HTMLAnchorElement: ...
    target: str
    download: str
    ping: USVString
    rel: str
    relList: DOMTokenList
    hreflang: str
    type: str
    text: str
    referrerPolicy: str
    coords: str
    charset: str
    name: str
    rev: str
    shape: str
    attributionSourceId: int

class HTMLImageElement(HTMLElement, HTMLAttributionSrcElementUtils):
    def New(self) -> HTMLImageElement: ...
    x: int
    y: int
    fetchPriority: str
    """ # GIgnoredStmt 
    LegacyFactoryFunction=Image(optional unsigned long width, optional unsigned long height)
    """
    alt: str
    src: USVString
    srcset: USVString
    sizes: str
    crossOrigin: str | None
    useMap: str
    isMap: bool
    width: int
    height: int
    naturalWidth: int
    naturalHeight: int
    complete: bool
    currentSrc: USVString
    referrerPolicy: str
    decoding: str
    loading: str
    def decode(self) -> Awaitable[None]: ...
    name: str
    lowsrc: USVString
    align: str
    hspace: int
    vspace: int
    longDesc: USVString
    border: str

class HTMLScriptElement(HTMLElement, HTMLAttributionSrcElementUtils):
    def New(self) -> HTMLScriptElement: ...
    fetchPriority: str
    src: USVString
    type: str
    noModule: bool
    async_: bool
    defer: bool
    crossOrigin: str | None
    text: str
    integrity: str
    referrerPolicy: str
    blocking: DOMTokenList
    charset: str
    event: str
    htmlFor: str

class WEBGL_lose_context:
    def loseContext(self): ...
    def restoreContext(self): ...

class CookieStore(EventTarget):
    @overload
    def get(self, name: USVString) -> Awaitable[CookieListItem | None]: ...
    @overload
    def get(self, options: CookieStoreGetOptions | None = {}) -> Awaitable[CookieListItem | None]: ...
    @overload
    def getAll(self, name: USVString) -> Awaitable[CookieList]: ...
    @overload
    def getAll(self, options: CookieStoreGetOptions | None = {}) -> Awaitable[CookieList]: ...
    @overload
    def set(self, name: USVString, value: USVString) -> Awaitable[None]: ...
    @overload
    def set(self, options: CookieInit) -> Awaitable[None]: ...
    @overload
    def delete(self, name: USVString) -> Awaitable[None]: ...
    @overload
    def delete(self, options: CookieStoreDeleteOptions) -> Awaitable[None]: ...
    onchange: EventHandler

class CookieStoreManager:
    def subscribe(self, subscriptions: Sequence[CookieStoreGetOptions]) -> Awaitable[None]: ...
    def getSubscriptions(self) -> Awaitable[Sequence[CookieStoreGetOptions]]: ...
    def unsubscribe(self, subscriptions: Sequence[CookieStoreGetOptions]) -> Awaitable[None]: ...

class CookieChangeEvent(Event):
    def New(self, type: str, eventInitDict: CookieChangeEventInit | None = {}) -> CookieChangeEvent: ...
    changed: Sequence[CookieListItem]
    deleted: Sequence[CookieListItem]

class ExtendableCookieChangeEvent(ExtendableEvent):
    def New(self, type: str, eventInitDict: ExtendableCookieChangeEventInit | None = {}) -> ExtendableCookieChangeEvent: ...
    changed: Sequence[CookieListItem]
    deleted: Sequence[CookieListItem]

class Gamepad:
    id: str
    index: int
    connected: bool
    timestamp: DOMHighResTimeStamp
    mapping: GamepadMappingType
    axes: Sequence[float]
    buttons: Sequence[GamepadButton]
    hand: GamepadHand
    hapticActuators: Sequence[GamepadHapticActuator]
    pose: GamepadPose | None
    touchEvents: Sequence[GamepadTouch]
    vibrationActuator: GamepadHapticActuator

class GamepadButton:
    pressed: bool
    touched: bool
    value: float

class GamepadEvent(Event):
    def New(self, type: str, eventInitDict: GamepadEventInit) -> GamepadEvent: ...
    gamepad: Gamepad

class WindowEventHandlers:
    ongamepadconnected: EventHandler
    ongamepaddisconnected: EventHandler
    onafterprint: EventHandler
    onbeforeprint: EventHandler
    onbeforeunload: OnBeforeUnloadEventHandler
    onhashchange: EventHandler
    onlanguagechange: EventHandler
    onmessage: EventHandler
    onmessageerror: EventHandler
    onoffline: EventHandler
    ononline: EventHandler
    onpagehide: EventHandler
    onpageshow: EventHandler
    onpopstate: EventHandler
    onrejectionhandled: EventHandler
    onstorage: EventHandler
    onunhandledrejection: EventHandler
    onunload: EventHandler
    onportalactivate: EventHandler

class NavigatorML:
    ml: ML

class ML:
    @overload
    def createContext(self, options: MLContextOptions | None = {}) -> Awaitable[MLContext]: ...
    @overload
    def createContext(self, gpuDevice: GPUDevice) -> Awaitable[MLContext]: ...
    @overload
    def createContextSync(self, options: MLContextOptions | None = {}) -> MLContext: ...
    @overload
    def createContextSync(self, gpuDevice: GPUDevice) -> MLContext: ...

class MLGraph: ...

class MLOperand: ...

class MLActivation: ...

class MLContext:
    def computeSync(self, graph: MLGraph, inputs: MLNamedArrayBufferViews, outputs: MLNamedArrayBufferViews): ...
    def compute(self, graph: MLGraph, inputs: MLNamedArrayBufferViews, outputs: MLNamedArrayBufferViews) -> Awaitable[MLComputeResult]: ...
    def createCommandEncoder(self) -> MLCommandEncoder: ...

class MLCommandEncoder:
    def initializeGraph(self, graph: MLGraph): ...
    def dispatch(self, graph: MLGraph, inputs: MLNamedGPUResources, outputs: MLNamedGPUResources): ...
    def finish(self, descriptor: GPUCommandBufferDescriptor | None = {}) -> GPUCommandBuffer: ...

class MLGraphBuilder:
    def New(self, context: MLContext) -> MLGraphBuilder: ...
    def input(self, name: str, desc: MLOperandDescriptor) -> MLOperand: ...
    @overload
    def constant(self, desc: MLOperandDescriptor, bufferView: MLBufferView) -> MLOperand: ...
    @overload
    def constant(self, value: float, type: MLOperandType | None = "float32") -> MLOperand: ...
    def build(self, outputs: MLNamedOperands) -> Awaitable[MLGraph]: ...
    def buildSync(self, outputs: MLNamedOperands) -> MLGraph: ...
    def batchNormalization(self, input: MLOperand, mean: MLOperand, variance: MLOperand, options: MLBatchNormalizationOptions | None = {}) -> MLOperand: ...
    @overload
    def clamp(self, x: MLOperand, options: MLClampOptions | None = {}) -> MLOperand: ...
    @overload
    def clamp(self, options: MLClampOptions | None = {}) -> MLActivation: ...
    def concat(self, inputs: Sequence[MLOperand], axis: int) -> MLOperand: ...
    def conv2d(self, input: MLOperand, filter: MLOperand, options: MLConv2dOptions | None = {}) -> MLOperand: ...
    def convTranspose2d(self, input: MLOperand, filter: MLOperand, options: MLConvTranspose2dOptions | None = {}) -> MLOperand: ...
    def add(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def sub(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def mul(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def div(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def max(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def min(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def pow(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def abs(self, x: MLOperand) -> MLOperand: ...
    def ceil(self, x: MLOperand) -> MLOperand: ...
    def cos(self, x: MLOperand) -> MLOperand: ...
    def exp(self, x: MLOperand) -> MLOperand: ...
    def floor(self, x: MLOperand) -> MLOperand: ...
    def log(self, x: MLOperand) -> MLOperand: ...
    def neg(self, x: MLOperand) -> MLOperand: ...
    def sin(self, x: MLOperand) -> MLOperand: ...
    def tan(self, x: MLOperand) -> MLOperand: ...
    @overload
    def elu(self, x: MLOperand, options: MLEluOptions | None = {}) -> MLOperand: ...
    @overload
    def elu(self, options: MLEluOptions | None = {}) -> MLActivation: ...
    def gemm(self, a: MLOperand, b: MLOperand, options: MLGemmOptions | None = {}) -> MLOperand: ...
    def gru(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, steps: int, hiddenSize: int, options: MLGruOptions | None = {}) -> Sequence[MLOperand]: ...
    def gruCell(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, hiddenState: MLOperand, hiddenSize: int, options: MLGruCellOptions | None = {}) -> MLOperand: ...
    @overload
    def hardSigmoid(self, x: MLOperand, options: MLHardSigmoidOptions | None = {}) -> MLOperand: ...
    @overload
    def hardSigmoid(self, options: MLHardSigmoidOptions | None = {}) -> MLActivation: ...
    @overload
    def hardSwish(self, x: MLOperand) -> MLOperand: ...
    @overload
    def hardSwish(self) -> MLActivation: ...
    def instanceNormalization(self, input: MLOperand, options: MLInstanceNormalizationOptions | None = {}) -> MLOperand: ...
    @overload
    def leakyRelu(self, x: MLOperand, options: MLLeakyReluOptions | None = {}) -> MLOperand: ...
    @overload
    def leakyRelu(self, options: MLLeakyReluOptions | None = {}) -> MLActivation: ...
    @overload
    def linear(self, x: MLOperand, options: MLLinearOptions | None = {}) -> MLOperand: ...
    @overload
    def linear(self, options: MLLinearOptions | None = {}) -> MLActivation: ...
    def lstm(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, steps: int, hiddenSize: int, options: MLLstmOptions | None = {}) -> Sequence[MLOperand]: ...
    def lstmCell(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, hiddenState: MLOperand, cellState: MLOperand, hiddenSize: int, options: MLLstmCellOptions | None = {}) -> Sequence[MLOperand]: ...
    def matmul(self, a: MLOperand, b: MLOperand) -> MLOperand: ...
    def pad(self, input: MLOperand, padding: MLOperand, options: MLPadOptions | None = {}) -> MLOperand: ...
    def averagePool2d(self, input: MLOperand, options: MLPool2dOptions | None = {}) -> MLOperand: ...
    def l2Pool2d(self, input: MLOperand, options: MLPool2dOptions | None = {}) -> MLOperand: ...
    def maxPool2d(self, input: MLOperand, options: MLPool2dOptions | None = {}) -> MLOperand: ...
    def reduceL1(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceL2(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceLogSum(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceLogSumExp(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceMax(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceMean(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceMin(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceProduct(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceSum(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    def reduceSumSquare(self, input: MLOperand, options: MLReduceOptions | None = {}) -> MLOperand: ...
    @overload
    def relu(self, x: MLOperand) -> MLOperand: ...
    @overload
    def relu(self) -> MLActivation: ...
    def resample2d(self, input: MLOperand, options: MLResample2dOptions | None = {}) -> MLOperand: ...
    def reshape(self, input: MLOperand, newShape: Sequence[int | None]) -> MLOperand: ...
    @overload
    def sigmoid(self, x: MLOperand) -> MLOperand: ...
    @overload
    def sigmoid(self) -> MLActivation: ...
    def slice(self, input: MLOperand, starts: Sequence[int], sizes: Sequence[int], options: MLSliceOptions | None = {}) -> MLOperand: ...
    @overload
    def softmax(self, x: MLOperand) -> MLOperand: ...
    @overload
    def softmax(self) -> MLActivation: ...
    @overload
    def softplus(self, x: MLOperand, options: MLSoftplusOptions | None = {}) -> MLOperand: ...
    @overload
    def softplus(self, options: MLSoftplusOptions | None = {}) -> MLActivation: ...
    @overload
    def softsign(self, x: MLOperand) -> MLOperand: ...
    @overload
    def softsign(self) -> MLActivation: ...
    def split(self, input: MLOperand, splits: int | Sequence[int], options: MLSplitOptions | None = {}) -> Sequence[MLOperand]: ...
    def squeeze(self, input: MLOperand, options: MLSqueezeOptions | None = {}) -> MLOperand: ...
    @overload
    def tanh(self, x: MLOperand) -> MLOperand: ...
    @overload
    def tanh(self) -> MLActivation: ...
    def transpose(self, input: MLOperand, options: MLTransposeOptions | None = {}) -> MLOperand: ...

class OES_standard_derivatives: ...

class TextDetector:
    def New(self) -> TextDetector: ...
    def detect(self, image: ImageBitmapSource) -> Awaitable[Sequence[DetectedText]]: ...

class MediaKeySystemAccess:
    keySystem: str
    def getConfiguration(self) -> MediaKeySystemConfiguration: ...
    def createMediaKeys(self) -> Awaitable[MediaKeys]: ...

class MediaKeys:
    def createSession(self, sessionType: MediaKeySessionType | None = "temporary") -> MediaKeySession: ...
    def setServerCertificate(self, serverCertificate: BufferSource) -> Awaitable[bool]: ...

class MediaKeySession(EventTarget):
    sessionId: str
    expiration: float
    closed: Awaitable[MediaKeySessionClosedReason]
    keyStatuses: MediaKeyStatusMap
    onkeystatuseschange: EventHandler
    onmessage: EventHandler
    def generateRequest(self, initDataType: str, initData: BufferSource) -> Awaitable[None]: ...
    def load(self, sessionId: str) -> Awaitable[bool]: ...
    def update(self, response: BufferSource) -> Awaitable[None]: ...
    def close(self) -> Awaitable[None]: ...
    def remove(self) -> Awaitable[None]: ...

class MediaKeyStatusMap:
    size: int
    def has(self, keyId: BufferSource) -> bool: ...
    def get(self, keyId: BufferSource) -> MediaKeyStatus | None: ...

class MediaKeyMessageEvent(Event):
    def New(self, type: str, eventInitDict: MediaKeyMessageEventInit) -> MediaKeyMessageEvent: ...
    messageType: MediaKeyMessageType
    message: ArrayBuffer

class HTMLMediaElement(HTMLElement):
    mediaKeys: MediaKeys | None
    onencrypted: EventHandler
    onwaitingforkey: EventHandler
    def setMediaKeys(self, mediaKeys: MediaKeys | None) -> Awaitable[None]: ...
    def captureStream(self) -> MediaStream: ...
    error: MediaError | None
    src: USVString
    srcObject: MediaProvider | None
    currentSrc: USVString
    crossOrigin: str | None
    networkState: int
    preload: str
    buffered: TimeRanges
    def load(self): ...
    def canPlayType(self, type: str) -> CanPlayTypeResult: ...
    readyState: int
    seeking: bool
    currentTime: float
    def fastSeek(self, time: float): ...
    duration: float
    def getStartDate(self) -> object: ...
    paused: bool
    defaultPlaybackRate: float
    playbackRate: float
    preservesPitch: bool
    played: TimeRanges
    seekable: TimeRanges
    ended: bool
    autoplay: bool
    loop: bool
    def play(self) -> Awaitable[None]: ...
    def pause(self): ...
    controls: bool
    volume: float
    muted: bool
    defaultMuted: bool
    audioTracks: AudioTrackList
    videoTracks: VideoTrackList
    textTracks: TextTrackList
    def addTextTrack(self, kind: TextTrackKind, label: str | None = "", language: str | None = "") -> TextTrack: ...
    remote: RemotePlayback
    disableRemotePlayback: bool
    sinkId: str
    def setSinkId(self, sinkId: str) -> Awaitable[None]: ...

class MediaEncryptedEvent(Event):
    def New(self, type: str, eventInitDict: MediaEncryptedEventInit | None = {}) -> MediaEncryptedEvent: ...
    initDataType: str
    initData: ArrayBuffer

class LaunchParams:
    targetURL: str | None
    files: Sequence[FileSystemHandle]

class LaunchQueue:
    def setConsumer(self, consumer: LaunchConsumer): ...

class DOMException:
    def New(self, message: str | None = "", name: str | None = "Error") -> DOMException: ...
    name: str
    message: str
    code: int

class GeolocationSensor(Sensor):
    def New(self, options: GeolocationSensorOptions | None = {}) -> GeolocationSensor: ...
    latitude: float | None
    longitude: float | None
    altitude: float | None
    accuracy: float | None
    altitudeAccuracy: float | None
    heading: float | None
    speed: float | None

class EXT_shader_texture_lod: ...

class EXT_texture_filter_anisotropic: ...

class MediaStream(EventTarget):
    @overload
    def New(self) -> MediaStream: ...
    @overload
    def New(self, stream: MediaStream) -> MediaStream: ...
    @overload
    def New(self, tracks: Sequence[MediaStreamTrack]) -> MediaStream: ...
    id: str
    def getAudioTracks(self) -> Sequence[MediaStreamTrack]: ...
    def getVideoTracks(self) -> Sequence[MediaStreamTrack]: ...
    def getTracks(self) -> Sequence[MediaStreamTrack]: ...
    def getTrackById(self, trackId: str) -> MediaStreamTrack | None: ...
    def addTrack(self, track: MediaStreamTrack): ...
    def removeTrack(self, track: MediaStreamTrack): ...
    def clone(self) -> MediaStream: ...
    active: bool
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class MediaStreamTrackEvent(Event):
    def New(self, type: str, eventInitDict: MediaStreamTrackEventInit) -> MediaStreamTrackEvent: ...
    track: MediaStreamTrack

class OverconstrainedError(DOMException):
    def New(self, constraint: str, message: str | None = "") -> OverconstrainedError: ...
    constraint: str

class MediaDeviceInfo:
    deviceId: str
    kind: MediaDeviceKind
    label: str
    groupId: str
    def toJSON(self) -> object: ...

class InputDeviceInfo(MediaDeviceInfo):
    def getCapabilities(self) -> MediaTrackCapabilities: ...

class WindowOrWorkerGlobalScope:
    performance: Performance
    scheduler: Scheduler
    trustedTypes: TrustedTypePolicyFactory
    def fetch(self, input: RequestInfo, init: RequestInit | None = {}) -> Awaitable[Response]: ...
    indexedDB: IDBFactory
    origin: USVString
    isSecureContext: bool
    crossOriginIsolated: bool
    def btoa(self, data: str) -> str: ...
    def atob(self, data: str) -> ByteString: ...
    def clearTimeout(self, id: int | None = 0): ...
    def clearInterval(self, id: int | None = 0): ...
    def queueMicrotask(self, callback: VoidFunction): ...
    @overload
    def createImageBitmap(self, image: ImageBitmapSource, options: ImageBitmapOptions | None = {}) -> Awaitable[ImageBitmap]: ...
    @overload
    def createImageBitmap(self, image: ImageBitmapSource, sx: int, sy: int, sw: int, sh: int, options: ImageBitmapOptions | None = {}) -> Awaitable[ImageBitmap]: ...
    caches: CacheStorage
    crypto: Crypto

class HTMLVideoElement(HTMLMediaElement):
    def New(self) -> HTMLVideoElement: ...
    def requestVideoFrameCallback(self, callback: VideoFrameRequestCallback) -> int: ...
    def cancelVideoFrameCallback(self, handle: int): ...
    def getVideoPlaybackQuality(self) -> VideoPlaybackQuality: ...
    width: int
    height: int
    videoWidth: int
    videoHeight: int
    poster: USVString
    playsInline: bool
    def requestPictureInPicture(self) -> Awaitable[PictureInPictureWindow]: ...
    onenterpictureinpicture: EventHandler
    onleavepictureinpicture: EventHandler
    disablePictureInPicture: bool

class Notification(EventTarget):
    def New(self, title: str, options: NotificationOptions | None = {}) -> Notification: ...
    onclick: EventHandler
    onshow: EventHandler
    onerror: EventHandler
    onclose: EventHandler
    title: str
    dir: NotificationDirection
    lang: str
    body: str
    tag: str
    image: USVString
    icon: USVString
    badge: USVString
    vibrate: Sequence[int]
    timestamp: EpochTimeStamp
    renotify: bool
    silent: bool
    requireInteraction: bool
    actions: Sequence[NotificationAction]
    def close(self): ...

class NotificationEvent(ExtendableEvent):
    def New(self, type: str, eventInitDict: NotificationEventInit) -> NotificationEvent: ...
    notification: Notification
    action: str

class XRInputSource:
    gamepad: Gamepad | None
    hand: XRHand | None
    handedness: XRHandedness
    targetRayMode: XRTargetRayMode
    targetRaySpace: XRSpace
    gripSpace: XRSpace | None
    profiles: Sequence[str]

class Scheduler: ...

class TaskPriorityChangeEvent(Event):
    def New(self, type: str, priorityChangeEventInitDict: TaskPriorityChangeEventInit) -> TaskPriorityChangeEvent: ...
    previousPriority: TaskPriority

class TaskController(AbortController):
    def New(self, init: TaskControllerInit | None = {}) -> TaskController: ...
    def setPriority(self, priority: TaskPriority): ...

class TaskSignal(AbortSignal):
    priority: TaskPriority
    onprioritychange: EventHandler

class CSSColorProfileRule(CSSRule):
    name: CSSOMString
    src: CSSOMString
    renderingIntent: CSSOMString
    components: CSSOMString

class ScreenOrientation(EventTarget):
    def lock(self, orientation: OrientationLockType) -> Awaitable[None]: ...
    def unlock(self): ...
    type: OrientationType
    angle: int
    onchange: EventHandler

class WEBGL_color_buffer_float: ...

class MediaQueryList(EventTarget):
    media: CSSOMString
    matches: bool
    def addListener(self, callback: EventListener | None): ...
    def removeListener(self, callback: EventListener | None): ...
    onchange: EventHandler

class MediaQueryListEvent(Event):
    def New(self, type: CSSOMString, eventInitDict: MediaQueryListEventInit | None = {}) -> MediaQueryListEvent: ...
    media: CSSOMString
    matches: bool

class CaretPosition:
    offsetNode: Node
    offset: int
    def getClientRect(self) -> DOMRect | None: ...

class HTMLElement(Element, GlobalEventHandlers, ElementContentEditable, HTMLOrSVGElement, ElementCSSInlineStyle):
    def New(self) -> HTMLElement: ...
    offsetParent: Element | None
    offsetTop: int
    offsetLeft: int
    offsetWidth: int
    offsetHeight: int
    title: str
    lang: str
    translate: bool
    dir: str
    hidden: bool | float | str | None
    inert: bool
    def click(self): ...
    accessKey: str
    accessKeyLabel: str
    draggable: bool
    spellcheck: bool
    autocapitalize: str
    innerText: str
    outerText: str
    def attachInternals(self) -> ElementInternals: ...

class Range(AbstractRange):
    def New(self) -> Range: ...
    def getClientRects(self) -> DOMRectList: ...
    def getBoundingClientRect(self) -> DOMRect: ...
    commonAncestorContainer: Node
    def setStart(self, node: Node, offset: int): ...
    def setEnd(self, node: Node, offset: int): ...
    def setStartBefore(self, node: Node): ...
    def setStartAfter(self, node: Node): ...
    def setEndBefore(self, node: Node): ...
    def setEndAfter(self, node: Node): ...
    def collapse(self, toStart: bool | None = false): ...
    def selectNode(self, node: Node): ...
    def selectNodeContents(self, node: Node): ...
    def compareBoundaryPoints(self, how: int, sourceRange: Range) -> short: ...
    def deleteContents(self): ...
    def extractContents(self) -> DocumentFragment: ...
    def cloneContents(self) -> DocumentFragment: ...
    def insertNode(self, node: Node): ...
    def surroundContents(self, newParent: Node): ...
    def cloneRange(self) -> Range: ...
    def detach(self): ...
    def isPointInRange(self, node: Node, offset: int) -> bool: ...
    def comparePoint(self, node: Node, offset: int) -> short: ...
    def intersectsNode(self, node: Node) -> bool: ...
    def createContextualFragment(self, fragment: str) -> DocumentFragment: ...

class MouseEvent(UIEvent):
    def New(self, type: str, eventInitDict: MouseEventInit | None = {}) -> MouseEvent: ...
    pageX: float
    pageY: float
    x: float
    y: float
    offsetX: float
    offsetY: float
    movementX: float
    movementY: float
    screenX: int
    screenY: int
    clientX: int
    clientY: int
    ctrlKey: bool
    shiftKey: bool
    altKey: bool
    metaKey: bool
    button: short
    buttons: int
    relatedTarget: EventTarget | None
    def getModifierState(self, keyArg: str) -> bool: ...
    def initMouseEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false, viewArg: Window | None = None, detailArg: int | None = 0, screenXArg: int | None = 0, screenYArg: int | None = 0, clientXArg: int | None = 0, clientYArg: int | None = 0, ctrlKeyArg: bool | None = false, altKeyArg: bool | None = false, shiftKeyArg: bool | None = false, metaKeyArg: bool | None = false, buttonArg: short | None = 0, relatedTargetArg: EventTarget | None = None): ...

class GeometryUtils:
    def getBoxQuads(self, options: BoxQuadOptions | None = {}) -> Sequence[DOMQuad]: ...
    def convertQuadFromNode(self, quad: DOMQuadInit, from_: GeometryNode, options: ConvertCoordinateOptions | None = {}) -> DOMQuad: ...
    def convertRectFromNode(self, rect: DOMRectReadOnly, from_: GeometryNode, options: ConvertCoordinateOptions | None = {}) -> DOMQuad: ...
    def convertPointFromNode(self, point: DOMPointInit, from_: GeometryNode, options: ConvertCoordinateOptions | None = {}) -> DOMPoint: ...

class Text(CharacterData, GeometryUtils, Slottable):
    def New(self, data: str | None = "") -> Text: ...
    def splitText(self, offset: int) -> Text: ...
    wholeText: str

class CSSPseudoElement(EventTarget, GeometryUtils):
    type: CSSOMString
    element: Element
    parent: Element | CSSPseudoElement
    def pseudo(self, type: CSSOMString) -> CSSPseudoElement | None: ...

class VisualViewport(EventTarget):
    offsetLeft: float
    offsetTop: float
    pageLeft: float
    pageTop: float
    width: float
    height: float
    scale: float
    onresize: EventHandler
    onscroll: EventHandler
    onscrollend: EventHandler

class GPUObjectBase:
    label: USVString

class GPUSupportedLimits:
    maxTextureDimension1D: int
    maxTextureDimension2D: int
    maxTextureDimension3D: int
    maxTextureArrayLayers: int
    maxBindGroups: int
    maxBindingsPerBindGroup: int
    maxDynamicUniformBuffersPerPipelineLayout: int
    maxDynamicStorageBuffersPerPipelineLayout: int
    maxSampledTexturesPerShaderStage: int
    maxSamplersPerShaderStage: int
    maxStorageBuffersPerShaderStage: int
    maxStorageTexturesPerShaderStage: int
    maxUniformBuffersPerShaderStage: int
    maxUniformBufferBindingSize: int
    maxStorageBufferBindingSize: int
    minUniformBufferOffsetAlignment: int
    minStorageBufferOffsetAlignment: int
    maxVertexBuffers: int
    maxBufferSize: int
    maxVertexAttributes: int
    maxVertexBufferArrayStride: int
    maxInterStageShaderComponents: int
    maxInterStageShaderVariables: int
    maxColorAttachments: int
    maxColorAttachmentBytesPerSample: int
    maxComputeWorkgroupStorageSize: int
    maxComputeInvocationsPerWorkgroup: int
    maxComputeWorkgroupSizeX: int
    maxComputeWorkgroupSizeY: int
    maxComputeWorkgroupSizeZ: int
    maxComputeWorkgroupsPerDimension: int

class GPUSupportedFeatures: ...

class GPUAdapterInfo:
    vendor: str
    architecture: str
    device: str
    description: str

class NavigatorGPU:
    gpu: GPU

class GPU:
    def requestAdapter(self, options: GPURequestAdapterOptions | None = {}) -> Awaitable[GPUAdapter | None]: ...
    def getPreferredCanvasFormat(self) -> GPUTextureFormat: ...

class GPUAdapter:
    features: GPUSupportedFeatures
    limits: GPUSupportedLimits
    isFallbackAdapter: bool
    def requestDevice(self, descriptor: GPUDeviceDescriptor | None = {}) -> Awaitable[GPUDevice]: ...
    def requestAdapterInfo(self, unmaskHints: Sequence[str] | None = []) -> Awaitable[GPUAdapterInfo]: ...

class GPUDevice(EventTarget, GPUObjectBase):
    features: GPUSupportedFeatures
    limits: GPUSupportedLimits
    queue: GPUQueue
    def destroy(self): ...
    def createBuffer(self, descriptor: GPUBufferDescriptor) -> GPUBuffer: ...
    def createTexture(self, descriptor: GPUTextureDescriptor) -> GPUTexture: ...
    def createSampler(self, descriptor: GPUSamplerDescriptor | None = {}) -> GPUSampler: ...
    def importExternalTexture(self, descriptor: GPUExternalTextureDescriptor) -> GPUExternalTexture: ...
    def createBindGroupLayout(self, descriptor: GPUBindGroupLayoutDescriptor) -> GPUBindGroupLayout: ...
    def createPipelineLayout(self, descriptor: GPUPipelineLayoutDescriptor) -> GPUPipelineLayout: ...
    def createBindGroup(self, descriptor: GPUBindGroupDescriptor) -> GPUBindGroup: ...
    def createShaderModule(self, descriptor: GPUShaderModuleDescriptor) -> GPUShaderModule: ...
    def createComputePipeline(self, descriptor: GPUComputePipelineDescriptor) -> GPUComputePipeline: ...
    def createRenderPipeline(self, descriptor: GPURenderPipelineDescriptor) -> GPURenderPipeline: ...
    def createComputePipelineAsync(self, descriptor: GPUComputePipelineDescriptor) -> Awaitable[GPUComputePipeline]: ...
    def createRenderPipelineAsync(self, descriptor: GPURenderPipelineDescriptor) -> Awaitable[GPURenderPipeline]: ...
    def createCommandEncoder(self, descriptor: GPUCommandEncoderDescriptor | None = {}) -> GPUCommandEncoder: ...
    def createRenderBundleEncoder(self, descriptor: GPURenderBundleEncoderDescriptor) -> GPURenderBundleEncoder: ...
    def createQuerySet(self, descriptor: GPUQuerySetDescriptor) -> GPUQuerySet: ...
    lost: Awaitable[GPUDeviceLostInfo]
    def pushErrorScope(self, filter: GPUErrorFilter): ...
    def popErrorScope(self) -> Awaitable[GPUError | None]: ...
    onuncapturederror: EventHandler

class GPUBuffer(GPUObjectBase):
    size: GPUSize64
    usage: GPUBufferUsageFlags
    mapState: GPUBufferMapState
    def mapAsync(self, mode: GPUMapModeFlags, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None) -> Awaitable[None]: ...
    def getMappedRange(self, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None) -> ArrayBuffer: ...
    def unmap(self): ...
    def destroy(self): ...

class GPUTexture(GPUObjectBase):
    def createView(self, descriptor: GPUTextureViewDescriptor | None = {}) -> GPUTextureView: ...
    def destroy(self): ...
    width: GPUIntegerCoordinate
    height: GPUIntegerCoordinate
    depthOrArrayLayers: GPUIntegerCoordinate
    mipLevelCount: GPUIntegerCoordinate
    sampleCount: GPUSize32
    dimension: GPUTextureDimension
    format: GPUTextureFormat
    usage: GPUTextureUsageFlags

class GPUTextureView(GPUObjectBase): ...

class GPUExternalTexture(GPUObjectBase):
    expired: bool

class GPUSampler(GPUObjectBase): ...

class GPUBindGroupLayout(GPUObjectBase): ...

class GPUBindGroup(GPUObjectBase): ...

class GPUPipelineLayout(GPUObjectBase): ...

class GPUShaderModule(GPUObjectBase):
    def compilationInfo(self) -> Awaitable[GPUCompilationInfo]: ...

class GPUCompilationMessage:
    message: str
    type: GPUCompilationMessageType
    lineNum: int
    linePos: int
    offset: int
    length: int

class GPUCompilationInfo:
    messages: Sequence[GPUCompilationMessage]

class GPUPipelineError(DOMException):
    def New(self, message: str, options: GPUPipelineErrorInit) -> GPUPipelineError: ...
    reason: GPUPipelineErrorReason

class GPUPipelineBase:
    def getBindGroupLayout(self, index: int) -> GPUBindGroupLayout: ...

class GPUComputePipeline(GPUObjectBase, GPUPipelineBase): ...

class GPURenderPipeline(GPUObjectBase, GPUPipelineBase): ...

class GPUCommandBuffer(GPUObjectBase): ...

class GPUCommandsMixin: ...

class GPUCommandEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin):
    def beginRenderPass(self, descriptor: GPURenderPassDescriptor) -> GPURenderPassEncoder: ...
    def beginComputePass(self, descriptor: GPUComputePassDescriptor | None = {}) -> GPUComputePassEncoder: ...
    def copyBufferToBuffer(self, source: GPUBuffer, sourceOffset: GPUSize64, destination: GPUBuffer, destinationOffset: GPUSize64, size: GPUSize64): ...
    def copyBufferToTexture(self, source: GPUImageCopyBuffer, destination: GPUImageCopyTexture, copySize: GPUExtent3D): ...
    def copyTextureToBuffer(self, source: GPUImageCopyTexture, destination: GPUImageCopyBuffer, copySize: GPUExtent3D): ...
    def copyTextureToTexture(self, source: GPUImageCopyTexture, destination: GPUImageCopyTexture, copySize: GPUExtent3D): ...
    def clearBuffer(self, buffer: GPUBuffer, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...
    def writeTimestamp(self, querySet: GPUQuerySet, queryIndex: GPUSize32): ...
    def resolveQuerySet(self, querySet: GPUQuerySet, firstQuery: GPUSize32, queryCount: GPUSize32, destination: GPUBuffer, destinationOffset: GPUSize64): ...
    def finish(self, descriptor: GPUCommandBufferDescriptor | None = {}) -> GPUCommandBuffer: ...

class GPUBindingCommandsMixin:
    @overload
    def setBindGroup(self, index: GPUIndex32, bindGroup: GPUBindGroup, dynamicOffsets: Sequence[GPUBufferDynamicOffset] | None = []): ...
    @overload
    def setBindGroup(self, index: GPUIndex32, bindGroup: GPUBindGroup, dynamicOffsetsData: Uint32Array, dynamicOffsetsDataStart: GPUSize64, dynamicOffsetsDataLength: GPUSize32): ...

class GPUDebugCommandsMixin:
    def pushDebugGroup(self, groupLabel: USVString): ...
    def popDebugGroup(self): ...
    def insertDebugMarker(self, markerLabel: USVString): ...

class GPUComputePassEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin):
    def setPipeline(self, pipeline: GPUComputePipeline): ...
    def dispatchWorkgroups(self, workgroupCountX: GPUSize32, workgroupCountY: GPUSize32 | None = 1, workgroupCountZ: GPUSize32 | None = 1): ...
    def dispatchWorkgroupsIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64): ...
    def end(self): ...

class GPURenderPassEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin, GPURenderCommandsMixin):
    def setViewport(self, x: float, y: float, width: float, height: float, minDepth: float, maxDepth: float): ...
    def setScissorRect(self, x: GPUIntegerCoordinate, y: GPUIntegerCoordinate, width: GPUIntegerCoordinate, height: GPUIntegerCoordinate): ...
    def setBlendConstant(self, color: GPUColor): ...
    def setStencilReference(self, reference: GPUStencilValue): ...
    def beginOcclusionQuery(self, queryIndex: GPUSize32): ...
    def endOcclusionQuery(self): ...
    def executeBundles(self, bundles: Sequence[GPURenderBundle]): ...
    def end(self): ...

class GPURenderCommandsMixin:
    def setPipeline(self, pipeline: GPURenderPipeline): ...
    def setIndexBuffer(self, buffer: GPUBuffer, indexFormat: GPUIndexFormat, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...
    def setVertexBuffer(self, slot: GPUIndex32, buffer: GPUBuffer, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...
    def draw(self, vertexCount: GPUSize32, instanceCount: GPUSize32 | None = 1, firstVertex: GPUSize32 | None = 0, firstInstance: GPUSize32 | None = 0): ...
    def drawIndexed(self, indexCount: GPUSize32, instanceCount: GPUSize32 | None = 1, firstIndex: GPUSize32 | None = 0, baseVertex: GPUSignedOffset32 | None = 0, firstInstance: GPUSize32 | None = 0): ...
    def drawIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64): ...
    def drawIndexedIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64): ...

class GPURenderBundle(GPUObjectBase): ...

class GPURenderBundleEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin, GPURenderCommandsMixin):
    def finish(self, descriptor: GPURenderBundleDescriptor | None = {}) -> GPURenderBundle: ...

class GPUQueue(GPUObjectBase):
    def submit(self, commandBuffers: Sequence[GPUCommandBuffer]): ...
    def onSubmittedWorkDone(self) -> Awaitable[None]: ...
    def writeBuffer(self, buffer: GPUBuffer, bufferOffset: GPUSize64, data: BufferSource, dataOffset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...
    def writeTexture(self, destination: GPUImageCopyTexture, data: BufferSource, dataLayout: GPUImageDataLayout, size: GPUExtent3D): ...
    def copyExternalImageToTexture(self, source: GPUImageCopyExternalImage, destination: GPUImageCopyTextureTagged, copySize: GPUExtent3D): ...

class GPUQuerySet(GPUObjectBase):
    def destroy(self): ...
    type: GPUQueryType
    count: GPUSize32

class GPUCanvasContext:
    canvas: HTMLCanvasElement | OffscreenCanvas
    def configure(self, configuration: GPUCanvasConfiguration): ...
    def unconfigure(self): ...
    def getCurrentTexture(self) -> GPUTexture: ...

class GPUDeviceLostInfo:
    reason: GPUDeviceLostReason | None
    message: str

class GPUError:
    message: str

class GPUValidationError(GPUError):
    def New(self, message: str) -> GPUValidationError: ...

class GPUOutOfMemoryError(GPUError):
    def New(self, message: str) -> GPUOutOfMemoryError: ...

class GPUInternalError(GPUError):
    def New(self, message: str) -> GPUInternalError: ...

class GPUUncapturedErrorEvent(Event):
    def New(self, type: str, gpuUncapturedErrorEventInitDict: GPUUncapturedErrorEventInit) -> GPUUncapturedErrorEvent: ...
    error: GPUError

class Highlight:
    def New(self, initialRanges: AbstractRange | None = None) -> Highlight: ...
    priority: int
    type: HighlightType

class HighlightRegistry: ...

class IdleDetector(EventTarget):
    def New(self) -> IdleDetector: ...
    userState: UserIdleState | None
    screenState: ScreenIdleState | None
    onchange: EventHandler
    def start(self, options: IdleOptions | None = {}) -> Awaitable[None]: ...

class PressureObserver:
    def New(self, callback: PressureUpdateCallback, options: PressureObserverOptions | None = {}) -> PressureObserver: ...
    def observe(self, source: PressureSource) -> Awaitable[None]: ...
    def unobserve(self, source: PressureSource): ...
    def disconnect(self): ...
    def takeRecords(self) -> Sequence[PressureRecord]: ...

class PressureRecord:
    source: PressureSource
    state: PressureState
    factors: Sequence[PressureFactor]
    time: DOMHighResTimeStamp

class BatteryManager(EventTarget):
    charging: bool
    chargingTime: float
    dischargingTime: float
    level: float
    onchargingchange: EventHandler
    onchargingtimechange: EventHandler
    ondischargingtimechange: EventHandler
    onlevelchange: EventHandler

class HTMLCanvasElement(HTMLElement):
    def New(self) -> HTMLCanvasElement: ...
    def captureStream(self, frameRequestRate: float | None = None) -> MediaStream: ...
    width: int
    height: int
    def transferControlToOffscreen(self) -> OffscreenCanvas: ...

class CanvasCaptureMediaStreamTrack(MediaStreamTrack):
    canvas: HTMLCanvasElement
    def requestFrame(self): ...

class Client:
    lifecycleState: ClientLifecycleState
    url: USVString
    frameType: FrameType
    id: str
    type: ClientType

class AnimationEvent(Event):
    def New(self, type: CSSOMString, animationEventInitDict: AnimationEventInit | None = {}) -> AnimationEvent: ...
    animationName: CSSOMString
    elapsedTime: float
    pseudoElement: CSSOMString

class CSSRule:
    cssText: CSSOMString
    parentRule: CSSRule | None
    parentStyleSheet: CSSStyleSheet | None
    type: int

class CSSKeyframeRule(CSSRule):
    keyText: CSSOMString
    style: CSSStyleDeclaration

class CSSKeyframesRule(CSSRule):
    name: CSSOMString
    cssRules: CSSRuleList
    length: int
    def appendRule(self, rule: CSSOMString): ...
    def deleteRule(self, select: CSSOMString): ...
    def findRule(self, select: CSSOMString) -> CSSKeyframeRule | None: ...

class GlobalEventHandlers:
    onanimationstart: EventHandler
    onanimationiteration: EventHandler
    onanimationend: EventHandler
    onanimationcancel: EventHandler
    onselectstart: EventHandler
    onselectionchange: EventHandler
    ontransitionrun: EventHandler
    ontransitionstart: EventHandler
    ontransitionend: EventHandler
    ontransitioncancel: EventHandler
    onabort: EventHandler
    onauxclick: EventHandler
    onbeforeinput: EventHandler
    onbeforematch: EventHandler
    onblur: EventHandler
    oncancel: EventHandler
    oncanplay: EventHandler
    oncanplaythrough: EventHandler
    onchange: EventHandler
    onclick: EventHandler
    onclose: EventHandler
    oncontextlost: EventHandler
    oncontextmenu: EventHandler
    oncontextrestored: EventHandler
    oncopy: EventHandler
    oncuechange: EventHandler
    oncut: EventHandler
    ondblclick: EventHandler
    ondrag: EventHandler
    ondragend: EventHandler
    ondragenter: EventHandler
    ondragleave: EventHandler
    ondragover: EventHandler
    ondragstart: EventHandler
    ondrop: EventHandler
    ondurationchange: EventHandler
    onemptied: EventHandler
    onended: EventHandler
    onerror: OnErrorEventHandler
    onfocus: EventHandler
    onformdata: EventHandler
    oninput: EventHandler
    oninvalid: EventHandler
    onkeydown: EventHandler
    onkeypress: EventHandler
    onkeyup: EventHandler
    onload: EventHandler
    onloadeddata: EventHandler
    onloadedmetadata: EventHandler
    onloadstart: EventHandler
    onmousedown: EventHandler
    onmouseenter: EventHandler
    onmouseleave: EventHandler
    onmousemove: EventHandler
    onmouseout: EventHandler
    onmouseover: EventHandler
    onmouseup: EventHandler
    onpaste: EventHandler
    onpause: EventHandler
    onplay: EventHandler
    onplaying: EventHandler
    onprogress: EventHandler
    onratechange: EventHandler
    onreset: EventHandler
    onresize: EventHandler
    onscroll: EventHandler
    onscrollend: EventHandler
    onsecuritypolicyviolation: EventHandler
    onseeked: EventHandler
    onseeking: EventHandler
    onselect: EventHandler
    onslotchange: EventHandler
    onstalled: EventHandler
    onsubmit: EventHandler
    onsuspend: EventHandler
    ontimeupdate: EventHandler
    ontoggle: EventHandler
    onvolumechange: EventHandler
    onwaiting: EventHandler
    onwebkitanimationend: EventHandler
    onwebkitanimationiteration: EventHandler
    onwebkitanimationstart: EventHandler
    onwebkittransitionend: EventHandler
    onwheel: EventHandler
    onbeforexrselect: EventHandler
    ontouchstart: EventHandler
    ontouchend: EventHandler
    ontouchmove: EventHandler
    ontouchcancel: EventHandler
    onpointerover: EventHandler
    onpointerenter: EventHandler
    onpointerdown: EventHandler
    onpointermove: EventHandler
    onpointerrawupdate: EventHandler
    onpointerup: EventHandler
    onpointercancel: EventHandler
    onpointerout: EventHandler
    onpointerleave: EventHandler
    ongotpointercapture: EventHandler
    onlostpointercapture: EventHandler

class InputDeviceCapabilities:
    def New(self, deviceInitDict: InputDeviceCapabilitiesInit | None = {}) -> InputDeviceCapabilities: ...
    firesTouchEvents: bool
    pointerMovementScrolls: bool

class UIEvent(Event):
    def New(self, type: str, eventInitDict: UIEventInit | None = {}) -> UIEvent: ...
    sourceCapabilities: InputDeviceCapabilities | None
    view: Window | None
    detail: int
    def initUIEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false, viewArg: Window | None = None, detailArg: int | None = 0): ...
    which: int

class CSSStyleValue: ...

class StylePropertyMapReadOnly:
    def getAll(self, property: USVString) -> Sequence[CSSStyleValue]: ...
    def has(self, property: USVString) -> bool: ...
    size: int

class StylePropertyMap(StylePropertyMapReadOnly):
    def set(self, property: USVString, values: CSSStyleValue | USVString | None = None): ...
    def append(self, property: USVString, values: CSSStyleValue | USVString | None = None): ...
    def delete(self, property: USVString): ...
    def clear(self): ...

class CSSStyleRule(CSSRule):
    styleMap: StylePropertyMap
    cssRules: CSSRuleList
    def insertRule(self, rule: CSSOMString, index: int | None = 0) -> int: ...
    def deleteRule(self, index: int): ...
    selectorText: CSSOMString
    style: CSSStyleDeclaration

class ElementCSSInlineStyle:
    attributeStyleMap: StylePropertyMap
    style: CSSStyleDeclaration

class CSSUnparsedValue(CSSStyleValue):
    def New(self, members: Sequence[CSSUnparsedSegment]) -> CSSUnparsedValue: ...
    length: int

class CSSVariableReferenceValue:
    def New(self, variable: USVString, fallback: CSSUnparsedValue | None = None) -> CSSVariableReferenceValue: ...
    variable: USVString
    fallback: CSSUnparsedValue | None

class CSSKeywordValue(CSSStyleValue):
    def New(self, value: USVString) -> CSSKeywordValue: ...
    value: USVString

class CSSNumericValue(CSSStyleValue):
    def add(self, values: CSSNumberish | None = None) -> CSSNumericValue: ...
    def sub(self, values: CSSNumberish | None = None) -> CSSNumericValue: ...
    def mul(self, values: CSSNumberish | None = None) -> CSSNumericValue: ...
    def div(self, values: CSSNumberish | None = None) -> CSSNumericValue: ...
    def min(self, values: CSSNumberish | None = None) -> CSSNumericValue: ...
    def max(self, values: CSSNumberish | None = None) -> CSSNumericValue: ...
    def equals(self, value: CSSNumberish | None = None) -> bool: ...
    def to(self, unit: USVString) -> CSSUnitValue: ...
    def toSum(self, units: USVString | None = None) -> CSSMathSum: ...
    def type(self) -> CSSNumericType: ...

class CSSUnitValue(CSSNumericValue):
    def New(self, value: float, unit: USVString) -> CSSUnitValue: ...
    value: float
    unit: USVString

class CSSMathValue(CSSNumericValue):
    operator: CSSMathOperator

class CSSMathSum(CSSMathValue):
    def New(self, args: CSSNumberish | None = None) -> CSSMathSum: ...
    values: CSSNumericArray

class CSSMathProduct(CSSMathValue):
    def New(self, args: CSSNumberish | None = None) -> CSSMathProduct: ...
    values: CSSNumericArray

class CSSMathNegate(CSSMathValue):
    def New(self, arg: CSSNumberish) -> CSSMathNegate: ...
    value: CSSNumericValue

class CSSMathInvert(CSSMathValue):
    def New(self, arg: CSSNumberish) -> CSSMathInvert: ...
    value: CSSNumericValue

class CSSMathMin(CSSMathValue):
    def New(self, args: CSSNumberish | None = None) -> CSSMathMin: ...
    values: CSSNumericArray

class CSSMathMax(CSSMathValue):
    def New(self, args: CSSNumberish | None = None) -> CSSMathMax: ...
    values: CSSNumericArray

class CSSMathClamp(CSSMathValue):
    def New(self, lower: CSSNumberish, value: CSSNumberish, upper: CSSNumberish) -> CSSMathClamp: ...
    lower: CSSNumericValue
    value: CSSNumericValue
    upper: CSSNumericValue

class CSSNumericArray:
    length: int

class CSSTransformValue(CSSStyleValue):
    def New(self, transforms: Sequence[CSSTransformComponent]) -> CSSTransformValue: ...
    length: int
    is2D: bool
    def toMatrix(self) -> DOMMatrix: ...

class CSSTransformComponent:
    is2D: bool
    def toMatrix(self) -> DOMMatrix: ...

class CSSTranslate(CSSTransformComponent):
    def New(self, x: CSSNumericValue, y: CSSNumericValue, z: CSSNumericValue | None = None) -> CSSTranslate: ...
    x: CSSNumericValue
    y: CSSNumericValue
    z: CSSNumericValue

class CSSRotate(CSSTransformComponent):
    @overload
    def New(self, angle: CSSNumericValue) -> CSSRotate: ...
    @overload
    def New(self, x: CSSNumberish, y: CSSNumberish, z: CSSNumberish, angle: CSSNumericValue) -> CSSRotate: ...
    x: CSSNumberish
    y: CSSNumberish
    z: CSSNumberish
    angle: CSSNumericValue

class CSSScale(CSSTransformComponent):
    def New(self, x: CSSNumberish, y: CSSNumberish, z: CSSNumberish | None = None) -> CSSScale: ...
    x: CSSNumberish
    y: CSSNumberish
    z: CSSNumberish

class CSSSkew(CSSTransformComponent):
    def New(self, ax: CSSNumericValue, ay: CSSNumericValue) -> CSSSkew: ...
    ax: CSSNumericValue
    ay: CSSNumericValue

class CSSSkewX(CSSTransformComponent):
    def New(self, ax: CSSNumericValue) -> CSSSkewX: ...
    ax: CSSNumericValue

class CSSSkewY(CSSTransformComponent):
    def New(self, ay: CSSNumericValue) -> CSSSkewY: ...
    ay: CSSNumericValue

class CSSPerspective(CSSTransformComponent):
    def New(self, length: CSSPerspectiveValue) -> CSSPerspective: ...
    length: CSSPerspectiveValue

class CSSMatrixComponent(CSSTransformComponent):
    def New(self, matrix: DOMMatrixReadOnly, options: CSSMatrixComponentOptions | None = {}) -> CSSMatrixComponent: ...
    matrix: DOMMatrix

class CSSImageValue(CSSStyleValue): ...

class CSSColorValue(CSSStyleValue): ...

class CSSRGB(CSSColorValue):
    def New(self, r: CSSColorRGBComp, g: CSSColorRGBComp, b: CSSColorRGBComp, alpha: CSSColorPercent | None = 1) -> CSSRGB: ...
    r: CSSColorRGBComp
    g: CSSColorRGBComp
    b: CSSColorRGBComp
    alpha: CSSColorPercent

class CSSHSL(CSSColorValue):
    def New(self, h: CSSColorAngle, s: CSSColorPercent, l: CSSColorPercent, alpha: CSSColorPercent | None = 1) -> CSSHSL: ...
    h: CSSColorAngle
    s: CSSColorPercent
    l: CSSColorPercent
    alpha: CSSColorPercent

class CSSHWB(CSSColorValue):
    def New(self, h: CSSNumericValue, w: CSSNumberish, b: CSSNumberish, alpha: CSSNumberish | None = 1) -> CSSHWB: ...
    h: CSSNumericValue
    w: CSSNumberish
    b: CSSNumberish
    alpha: CSSNumberish

class CSSLab(CSSColorValue):
    def New(self, l: CSSColorPercent, a: CSSColorNumber, b: CSSColorNumber, alpha: CSSColorPercent | None = 1) -> CSSLab: ...
    l: CSSColorPercent
    a: CSSColorNumber
    b: CSSColorNumber
    alpha: CSSColorPercent

class CSSLCH(CSSColorValue):
    def New(self, l: CSSColorPercent, c: CSSColorPercent, h: CSSColorAngle, alpha: CSSColorPercent | None = 1) -> CSSLCH: ...
    l: CSSColorPercent
    c: CSSColorPercent
    h: CSSColorAngle
    alpha: CSSColorPercent

class CSSOKLab(CSSColorValue):
    def New(self, l: CSSColorPercent, a: CSSColorNumber, b: CSSColorNumber, alpha: CSSColorPercent | None = 1) -> CSSOKLab: ...
    l: CSSColorPercent
    a: CSSColorNumber
    b: CSSColorNumber
    alpha: CSSColorPercent

class CSSOKLCH(CSSColorValue):
    def New(self, l: CSSColorPercent, c: CSSColorPercent, h: CSSColorAngle, alpha: CSSColorPercent | None = 1) -> CSSOKLCH: ...
    l: CSSColorPercent
    c: CSSColorPercent
    h: CSSColorAngle
    alpha: CSSColorPercent

class CSSColor(CSSColorValue):
    def New(self, colorSpace: CSSKeywordish, channels: Sequence[CSSColorPercent], alpha: CSSNumberish | None = 1) -> CSSColor: ...
    colorSpace: CSSKeywordish
    channels: Sequence[CSSColorPercent]
    alpha: CSSNumberish

class BaseAudioContext(EventTarget):
    destination: AudioDestinationNode
    sampleRate: float
    currentTime: float
    listener: AudioListener
    state: AudioContextState
    audioWorklet: AudioWorklet
    onstatechange: EventHandler
    def createAnalyser(self) -> AnalyserNode: ...
    def createBiquadFilter(self) -> BiquadFilterNode: ...
    def createBuffer(self, numberOfChannels: int, length: int, sampleRate: float) -> AudioBuffer: ...
    def createBufferSource(self) -> AudioBufferSourceNode: ...
    def createChannelMerger(self, numberOfInputs: int | None = 6) -> ChannelMergerNode: ...
    def createChannelSplitter(self, numberOfOutputs: int | None = 6) -> ChannelSplitterNode: ...
    def createConstantSource(self) -> ConstantSourceNode: ...
    def createConvolver(self) -> ConvolverNode: ...
    def createDelay(self, maxDelayTime: float | None = 1.0) -> DelayNode: ...
    def createDynamicsCompressor(self) -> DynamicsCompressorNode: ...
    def createGain(self) -> GainNode: ...
    def createIIRFilter(self, feedforward: Sequence[float], feedback: Sequence[float]) -> IIRFilterNode: ...
    def createOscillator(self) -> OscillatorNode: ...
    def createPanner(self) -> PannerNode: ...
    def createPeriodicWave(self, real: Sequence[float], imag: Sequence[float], constraints: PeriodicWaveConstraints | None = {}) -> PeriodicWave: ...
    def createScriptProcessor(self, bufferSize: int | None = 0, numberOfInputChannels: int | None = 2, numberOfOutputChannels: int | None = 2) -> ScriptProcessorNode: ...
    def createStereoPanner(self) -> StereoPannerNode: ...
    def createWaveShaper(self) -> WaveShaperNode: ...
    def decodeAudioData(self, audioData: ArrayBuffer, successCallback: DecodeSuccessCallback | None = None, errorCallback: DecodeErrorCallback | None = None) -> Awaitable[AudioBuffer]: ...

class AudioContext(BaseAudioContext):
    def New(self, contextOptions: AudioContextOptions | None = {}) -> AudioContext: ...
    baseLatency: float
    outputLatency: float
    sinkId: str | AudioSinkInfo
    renderCapacity: AudioRenderCapacity
    onsinkchange: EventHandler
    def getOutputTimestamp(self) -> AudioTimestamp: ...
    def resume(self) -> Awaitable[None]: ...
    def suspend(self) -> Awaitable[None]: ...
    def close(self) -> Awaitable[None]: ...
    def setSinkId(self, sinkId: str | AudioSinkOptions) -> Awaitable[None]: ...
    def createMediaElementSource(self, mediaElement: HTMLMediaElement) -> MediaElementAudioSourceNode: ...
    def createMediaStreamSource(self, mediaStream: MediaStream) -> MediaStreamAudioSourceNode: ...
    def createMediaStreamTrackSource(self, mediaStreamTrack: MediaStreamTrack) -> MediaStreamTrackAudioSourceNode: ...
    def createMediaStreamDestination(self) -> MediaStreamAudioDestinationNode: ...

class AudioSinkInfo:
    type: AudioSinkType

class AudioRenderCapacity(EventTarget):
    def start(self, options: AudioRenderCapacityOptions | None = {}): ...
    def stop(self): ...
    onupdate: EventHandler

class AudioRenderCapacityEvent(Event):
    def New(self, type: str, eventInitDict: AudioRenderCapacityEventInit | None = {}) -> AudioRenderCapacityEvent: ...
    timestamp: float
    averageLoad: float
    peakLoad: float
    underrunRatio: float

class OfflineAudioContext(BaseAudioContext):
    @overload
    def New(self, contextOptions: OfflineAudioContextOptions) -> OfflineAudioContext: ...
    @overload
    def New(self, numberOfChannels: int, length: int, sampleRate: float) -> OfflineAudioContext: ...
    def startRendering(self) -> Awaitable[AudioBuffer]: ...
    def resume(self) -> Awaitable[None]: ...
    def suspend(self, suspendTime: float) -> Awaitable[None]: ...
    length: int
    oncomplete: EventHandler

class OfflineAudioCompletionEvent(Event):
    def New(self, type: str, eventInitDict: OfflineAudioCompletionEventInit) -> OfflineAudioCompletionEvent: ...
    renderedBuffer: AudioBuffer

class AudioBuffer:
    def New(self, options: AudioBufferOptions) -> AudioBuffer: ...
    sampleRate: float
    length: int
    duration: float
    numberOfChannels: int
    def getChannelData(self, channel: int) -> Float32Array: ...
    def copyFromChannel(self, destination: Float32Array, channelNumber: int, bufferOffset: int | None = 0): ...
    def copyToChannel(self, source: Float32Array, channelNumber: int, bufferOffset: int | None = 0): ...

class AudioNode(EventTarget):
    @overload
    def connect(self, destinationNode: AudioNode, output: int | None = 0, input: int | None = 0) -> AudioNode: ...
    @overload
    def connect(self, destinationParam: AudioParam, output: int | None = 0): ...
    @overload
    def disconnect(self): ...
    @overload
    def disconnect(self, output: int): ...
    @overload
    def disconnect(self, destinationNode: AudioNode): ...
    @overload
    def disconnect(self, destinationNode: AudioNode, output: int): ...
    @overload
    def disconnect(self, destinationNode: AudioNode, output: int, input: int): ...
    @overload
    def disconnect(self, destinationParam: AudioParam): ...
    @overload
    def disconnect(self, destinationParam: AudioParam, output: int): ...
    context: BaseAudioContext
    numberOfInputs: int
    numberOfOutputs: int
    channelCount: int
    channelCountMode: ChannelCountMode
    channelInterpretation: ChannelInterpretation

class AudioParam:
    value: float
    automationRate: AutomationRate
    defaultValue: float
    minValue: float
    maxValue: float
    def setValueAtTime(self, value: float, startTime: float) -> AudioParam: ...
    def linearRampToValueAtTime(self, value: float, endTime: float) -> AudioParam: ...
    def exponentialRampToValueAtTime(self, value: float, endTime: float) -> AudioParam: ...
    def setTargetAtTime(self, target: float, startTime: float, timeConstant: float) -> AudioParam: ...
    def setValueCurveAtTime(self, values: Sequence[float], startTime: float, duration: float) -> AudioParam: ...
    def cancelScheduledValues(self, cancelTime: float) -> AudioParam: ...
    def cancelAndHoldAtTime(self, cancelTime: float) -> AudioParam: ...

class AudioScheduledSourceNode(AudioNode):
    onended: EventHandler
    def start(self, when: float | None = 0): ...
    def stop(self, when: float | None = 0): ...

class AnalyserNode(AudioNode):
    def New(self, context: BaseAudioContext, options: AnalyserOptions | None = {}) -> AnalyserNode: ...
    def getFloatFrequencyData(self, array: Float32Array): ...
    def getByteFrequencyData(self, array: Uint8Array): ...
    def getFloatTimeDomainData(self, array: Float32Array): ...
    def getByteTimeDomainData(self, array: Uint8Array): ...
    fftSize: int
    frequencyBinCount: int
    minDecibels: float
    maxDecibels: float
    smoothingTimeConstant: float

class AudioBufferSourceNode(AudioScheduledSourceNode):
    def New(self, context: BaseAudioContext, options: AudioBufferSourceOptions | None = {}) -> AudioBufferSourceNode: ...
    buffer: AudioBuffer | None
    playbackRate: AudioParam
    detune: AudioParam
    loop: bool
    loopStart: float
    loopEnd: float
    def start(self, when: float | None = 0, offset: float | None = None, duration: float | None = None): ...

class AudioDestinationNode(AudioNode):
    maxChannelCount: int

class AudioListener:
    positionX: AudioParam
    positionY: AudioParam
    positionZ: AudioParam
    forwardX: AudioParam
    forwardY: AudioParam
    forwardZ: AudioParam
    upX: AudioParam
    upY: AudioParam
    upZ: AudioParam
    def setPosition(self, x: float, y: float, z: float): ...
    def setOrientation(self, x: float, y: float, z: float, xUp: float, yUp: float, zUp: float): ...

class AudioProcessingEvent(Event):
    def New(self, type: str, eventInitDict: AudioProcessingEventInit) -> AudioProcessingEvent: ...
    playbackTime: float
    inputBuffer: AudioBuffer
    outputBuffer: AudioBuffer

class BiquadFilterNode(AudioNode):
    def New(self, context: BaseAudioContext, options: BiquadFilterOptions | None = {}) -> BiquadFilterNode: ...
    type: BiquadFilterType
    frequency: AudioParam
    detune: AudioParam
    Q: AudioParam
    gain: AudioParam
    def getFrequencyResponse(self, frequencyHz: Float32Array, magResponse: Float32Array, phaseResponse: Float32Array): ...

class ChannelMergerNode(AudioNode):
    def New(self, context: BaseAudioContext, options: ChannelMergerOptions | None = {}) -> ChannelMergerNode: ...

class ChannelSplitterNode(AudioNode):
    def New(self, context: BaseAudioContext, options: ChannelSplitterOptions | None = {}) -> ChannelSplitterNode: ...

class ConstantSourceNode(AudioScheduledSourceNode):
    def New(self, context: BaseAudioContext, options: ConstantSourceOptions | None = {}) -> ConstantSourceNode: ...
    offset: AudioParam

class ConvolverNode(AudioNode):
    def New(self, context: BaseAudioContext, options: ConvolverOptions | None = {}) -> ConvolverNode: ...
    buffer: AudioBuffer | None
    normalize: bool

class DelayNode(AudioNode):
    def New(self, context: BaseAudioContext, options: DelayOptions | None = {}) -> DelayNode: ...
    delayTime: AudioParam

class DynamicsCompressorNode(AudioNode):
    def New(self, context: BaseAudioContext, options: DynamicsCompressorOptions | None = {}) -> DynamicsCompressorNode: ...
    threshold: AudioParam
    knee: AudioParam
    ratio: AudioParam
    reduction: float
    attack: AudioParam
    release: AudioParam

class GainNode(AudioNode):
    def New(self, context: BaseAudioContext, options: GainOptions | None = {}) -> GainNode: ...
    gain: AudioParam

class IIRFilterNode(AudioNode):
    def New(self, context: BaseAudioContext, options: IIRFilterOptions) -> IIRFilterNode: ...
    def getFrequencyResponse(self, frequencyHz: Float32Array, magResponse: Float32Array, phaseResponse: Float32Array): ...

class MediaElementAudioSourceNode(AudioNode):
    def New(self, context: AudioContext, options: MediaElementAudioSourceOptions) -> MediaElementAudioSourceNode: ...
    mediaElement: HTMLMediaElement

class MediaStreamAudioDestinationNode(AudioNode):
    def New(self, context: AudioContext, options: AudioNodeOptions | None = {}) -> MediaStreamAudioDestinationNode: ...
    stream: MediaStream

class MediaStreamAudioSourceNode(AudioNode):
    def New(self, context: AudioContext, options: MediaStreamAudioSourceOptions) -> MediaStreamAudioSourceNode: ...
    mediaStream: MediaStream

class MediaStreamTrackAudioSourceNode(AudioNode):
    def New(self, context: AudioContext, options: MediaStreamTrackAudioSourceOptions) -> MediaStreamTrackAudioSourceNode: ...

class OscillatorNode(AudioScheduledSourceNode):
    def New(self, context: BaseAudioContext, options: OscillatorOptions | None = {}) -> OscillatorNode: ...
    type: OscillatorType
    frequency: AudioParam
    detune: AudioParam
    def setPeriodicWave(self, periodicWave: PeriodicWave): ...

class PannerNode(AudioNode):
    def New(self, context: BaseAudioContext, options: PannerOptions | None = {}) -> PannerNode: ...
    panningModel: PanningModelType
    positionX: AudioParam
    positionY: AudioParam
    positionZ: AudioParam
    orientationX: AudioParam
    orientationY: AudioParam
    orientationZ: AudioParam
    distanceModel: DistanceModelType
    refDistance: float
    maxDistance: float
    rolloffFactor: float
    coneInnerAngle: float
    coneOuterAngle: float
    coneOuterGain: float
    def setPosition(self, x: float, y: float, z: float): ...
    def setOrientation(self, x: float, y: float, z: float): ...

class PeriodicWave:
    def New(self, context: BaseAudioContext, options: PeriodicWaveOptions | None = {}) -> PeriodicWave: ...

class ScriptProcessorNode(AudioNode):
    onaudioprocess: EventHandler
    bufferSize: int

class StereoPannerNode(AudioNode):
    def New(self, context: BaseAudioContext, options: StereoPannerOptions | None = {}) -> StereoPannerNode: ...
    pan: AudioParam

class WaveShaperNode(AudioNode):
    def New(self, context: BaseAudioContext, options: WaveShaperOptions | None = {}) -> WaveShaperNode: ...
    curve: Float32Array
    oversample: OverSampleType

class AudioWorklet(Worklet):
    port: MessagePort

class AudioWorkletGlobalScope(WorkletGlobalScope):
    def registerProcessor(self, name: str, processorCtor: AudioWorkletProcessorConstructor): ...
    currentFrame: int
    currentTime: float
    sampleRate: float
    port: MessagePort

class AudioParamMap: ...

class AudioWorkletNode(AudioNode):
    def New(self, context: BaseAudioContext, name: str, options: AudioWorkletNodeOptions | None = {}) -> AudioWorkletNode: ...
    parameters: AudioParamMap
    port: MessagePort
    onprocessorerror: EventHandler

class AudioWorkletProcessor:
    def New(self) -> AudioWorkletProcessor: ...
    port: MessagePort

class AmbientLightSensor(Sensor):
    def New(self, sensorOptions: SensorOptions | None = {}) -> AmbientLightSensor: ...
    illuminance: float | None

class NetworkInformationSaveData:
    saveData: bool

class NetworkInformation(EventTarget, NetworkInformationSaveData):
    type: ConnectionType
    effectiveType: EffectiveConnectionType
    downlinkMax: Megabit
    downlink: Megabit
    rtt: Millisecond
    onchange: EventHandler

class CSSImportRule(CSSRule):
    layerName: CSSOMString | None
    href: USVString
    media: MediaList
    styleSheet: CSSStyleSheet

class CSSLayerBlockRule(CSSGroupingRule):
    name: CSSOMString

class CSSLayerStatementRule(CSSRule):
    nameList: Sequence[CSSOMString]

class WEBGL_multi_draw:
    def multiDrawArraysWEBGL(self, mode: GLenum, firstsList: Int32Array | Sequence[GLint], firstsOffset: GLuint, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, drawcount: GLsizei): ...
    def multiDrawElementsWEBGL(self, mode: GLenum, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, type: GLenum, offsetsList: Int32Array | Sequence[GLsizei], offsetsOffset: GLuint, drawcount: GLsizei): ...
    def multiDrawArraysInstancedWEBGL(self, mode: GLenum, firstsList: Int32Array | Sequence[GLint], firstsOffset: GLuint, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, instanceCountsList: Int32Array | Sequence[GLsizei], instanceCountsOffset: GLuint, drawcount: GLsizei): ...
    def multiDrawElementsInstancedWEBGL(self, mode: GLenum, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, type: GLenum, offsetsList: Int32Array | Sequence[GLsizei], offsetsOffset: GLuint, instanceCountsList: Int32Array | Sequence[GLsizei], instanceCountsOffset: GLuint, drawcount: GLsizei): ...

class NavigatorDeviceMemory:
    deviceMemory: float

class VTTCue(TextTrackCue):
    def New(self, startTime: float, endTime: float, text: str) -> VTTCue: ...
    region: VTTRegion | None
    vertical: DirectionSetting
    snapToLines: bool
    line: LineAndPositionSetting
    lineAlign: LineAlignSetting
    position: LineAndPositionSetting
    positionAlign: PositionAlignSetting
    size: float
    align: AlignSetting
    text: str
    def getCueAsHTML(self) -> DocumentFragment: ...

class VTTRegion:
    def New(self) -> VTTRegion: ...
    id: str
    width: float
    lines: int
    regionAnchorX: float
    regionAnchorY: float
    viewportAnchorX: float
    viewportAnchorY: float
    scroll: ScrollSetting

class RTCPeerConnection(EventTarget):
    def New(self, configuration: RTCConfiguration | None = {}) -> RTCPeerConnection: ...
    @overload
    def createOffer(self, options: RTCOfferOptions | None = {}) -> Awaitable[RTCSessionDescriptionInit]: ...
    @overload
    def createAnswer(self, options: RTCAnswerOptions | None = {}) -> Awaitable[RTCSessionDescriptionInit]: ...
    @overload
    def setLocalDescription(self, description: RTCLocalSessionDescriptionInit | None = {}) -> Awaitable[None]: ...
    localDescription: RTCSessionDescription | None
    currentLocalDescription: RTCSessionDescription | None
    pendingLocalDescription: RTCSessionDescription | None
    @overload
    def setRemoteDescription(self, description: RTCSessionDescriptionInit) -> Awaitable[None]: ...
    remoteDescription: RTCSessionDescription | None
    currentRemoteDescription: RTCSessionDescription | None
    pendingRemoteDescription: RTCSessionDescription | None
    @overload
    def addIceCandidate(self, candidate: RTCIceCandidateInit | None = {}) -> Awaitable[None]: ...
    signalingState: RTCSignalingState
    iceGatheringState: RTCIceGatheringState
    iceConnectionState: RTCIceConnectionState
    connectionState: RTCPeerConnectionState
    canTrickleIceCandidates: bool | None
    def restartIce(self): ...
    def getConfiguration(self) -> RTCConfiguration: ...
    def setConfiguration(self, configuration: RTCConfiguration | None = {}): ...
    def close(self): ...
    onnegotiationneeded: EventHandler
    onicecandidate: EventHandler
    onicecandidateerror: EventHandler
    onsignalingstatechange: EventHandler
    oniceconnectionstatechange: EventHandler
    onicegatheringstatechange: EventHandler
    onconnectionstatechange: EventHandler
    @overload
    def createOffer(self, successCallback: RTCSessionDescriptionCallback, failureCallback: RTCPeerConnectionErrorCallback, options: RTCOfferOptions | None = {}) -> Awaitable[None]: ...
    @overload
    def setLocalDescription(self, description: RTCLocalSessionDescriptionInit, successCallback: VoidFunction, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    @overload
    def createAnswer(self, successCallback: RTCSessionDescriptionCallback, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    @overload
    def setRemoteDescription(self, description: RTCSessionDescriptionInit, successCallback: VoidFunction, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    @overload
    def addIceCandidate(self, candidate: RTCIceCandidateInit, successCallback: VoidFunction, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    def getSenders(self) -> Sequence[RTCRtpSender]: ...
    def getReceivers(self) -> Sequence[RTCRtpReceiver]: ...
    def getTransceivers(self) -> Sequence[RTCRtpTransceiver]: ...
    def addTrack(self, track: MediaStreamTrack, streams: MediaStream | None = None) -> RTCRtpSender: ...
    def removeTrack(self, sender: RTCRtpSender): ...
    def addTransceiver(self, trackOrKind: MediaStreamTrack | str, init: RTCRtpTransceiverInit | None = {}) -> RTCRtpTransceiver: ...
    ontrack: EventHandler
    sctp: RTCSctpTransport | None
    def createDataChannel(self, label: USVString, dataChannelDict: RTCDataChannelInit | None = {}) -> RTCDataChannel: ...
    ondatachannel: EventHandler
    def getStats(self, selector: MediaStreamTrack | None = None) -> Awaitable[RTCStatsReport]: ...
    def setIdentityProvider(self, provider: str, options: RTCIdentityProviderOptions | None = {}): ...
    def getIdentityAssertion(self) -> Awaitable[str]: ...
    peerIdentity: Awaitable[RTCIdentityAssertion]
    idpLoginUrl: str | None
    idpErrorInfo: str | None

class RTCSessionDescription:
    def New(self, descriptionInitDict: RTCSessionDescriptionInit) -> RTCSessionDescription: ...
    type: RTCSdpType
    sdp: str
    def toJSON(self) -> object: ...

class RTCIceCandidate:
    def New(self, candidateInitDict: RTCIceCandidateInit | None = {}) -> RTCIceCandidate: ...
    candidate: str
    sdpMid: str | None
    sdpMLineIndex: int | None
    foundation: str | None
    component: RTCIceComponent | None
    priority: int | None
    address: str | None
    protocol: RTCIceProtocol | None
    port: int | None
    type: RTCIceCandidateType | None
    tcpType: RTCIceTcpCandidateType | None
    relatedAddress: str | None
    relatedPort: int | None
    usernameFragment: str | None
    relayProtocol: RTCIceServerTransportProtocol | None
    url: str | None
    def toJSON(self) -> RTCIceCandidateInit: ...

class RTCPeerConnectionIceEvent(Event):
    def New(self, type: str, eventInitDict: RTCPeerConnectionIceEventInit | None = {}) -> RTCPeerConnectionIceEvent: ...
    candidate: RTCIceCandidate | None
    url: str | None

class RTCPeerConnectionIceErrorEvent(Event):
    def New(self, type: str, eventInitDict: RTCPeerConnectionIceErrorEventInit) -> RTCPeerConnectionIceErrorEvent: ...
    address: str | None
    port: int | None
    url: str
    errorCode: int
    errorText: USVString

class RTCCertificate:
    expires: EpochTimeStamp
    def getFingerprints(self) -> Sequence[RTCDtlsFingerprint]: ...

class RTCRtpSender:
    track: MediaStreamTrack | None
    transport: RTCDtlsTransport | None
    def setParameters(self, parameters: RTCRtpSendParameters) -> Awaitable[None]: ...
    def getParameters(self) -> RTCRtpSendParameters: ...
    def replaceTrack(self, withTrack: MediaStreamTrack | None) -> Awaitable[None]: ...
    def setStreams(self, streams: MediaStream | None = None): ...
    def getStats(self) -> Awaitable[RTCStatsReport]: ...
    dtmf: RTCDTMFSender | None
    transform: RTCRtpTransform | None
    def generateKeyFrame(self, rids: Sequence[str] | None = None) -> Awaitable[None]: ...

class RTCRtpReceiver:
    track: MediaStreamTrack
    transport: RTCDtlsTransport | None
    def getParameters(self) -> RTCRtpReceiveParameters: ...
    def getContributingSources(self) -> Sequence[RTCRtpContributingSource]: ...
    def getSynchronizationSources(self) -> Sequence[RTCRtpSynchronizationSource]: ...
    def getStats(self) -> Awaitable[RTCStatsReport]: ...
    transform: RTCRtpTransform | None

class RTCRtpTransceiver:
    mid: str | None
    sender: RTCRtpSender
    receiver: RTCRtpReceiver
    direction: RTCRtpTransceiverDirection
    currentDirection: RTCRtpTransceiverDirection | None
    def stop(self): ...
    def setCodecPreferences(self, codecs: Sequence[RTCRtpCodecCapability]): ...

class RTCDtlsTransport(EventTarget):
    iceTransport: RTCIceTransport
    state: RTCDtlsTransportState
    def getRemoteCertificates(self) -> Sequence[ArrayBuffer]: ...
    onstatechange: EventHandler
    onerror: EventHandler

class RTCIceTransport(EventTarget):
    def New(self) -> RTCIceTransport: ...
    role: RTCIceRole
    component: RTCIceComponent
    state: RTCIceTransportState
    gatheringState: RTCIceGathererState
    def getLocalCandidates(self) -> Sequence[RTCIceCandidate]: ...
    def getRemoteCandidates(self) -> Sequence[RTCIceCandidate]: ...
    def getSelectedCandidatePair(self) -> RTCIceCandidatePair | None: ...
    def getLocalParameters(self) -> RTCIceParameters | None: ...
    def getRemoteParameters(self) -> RTCIceParameters | None: ...
    onstatechange: EventHandler
    ongatheringstatechange: EventHandler
    onselectedcandidatepairchange: EventHandler
    def gather(self, options: RTCIceGatherOptions | None = {}): ...
    def start(self, remoteParameters: RTCIceParameters | None = {}, role: RTCIceRole | None = "controlled"): ...
    def stop(self): ...
    def addRemoteCandidate(self, remoteCandidate: RTCIceCandidateInit | None = {}): ...
    onerror: EventHandler
    onicecandidate: EventHandler

class RTCTrackEvent(Event):
    def New(self, type: str, eventInitDict: RTCTrackEventInit) -> RTCTrackEvent: ...
    receiver: RTCRtpReceiver
    track: MediaStreamTrack
    streams: Sequence[MediaStream]
    transceiver: RTCRtpTransceiver

class RTCSctpTransport(EventTarget):
    transport: RTCDtlsTransport
    state: RTCSctpTransportState
    maxMessageSize: float
    maxChannels: int | None
    onstatechange: EventHandler

class RTCDataChannel(EventTarget):
    label: USVString
    ordered: bool
    maxPacketLifeTime: int | None
    maxRetransmits: int | None
    protocol: USVString
    negotiated: bool
    id: int | None
    readyState: RTCDataChannelState
    bufferedAmount: int
    bufferedAmountLowThreshold: int
    onopen: EventHandler
    onbufferedamountlow: EventHandler
    onerror: EventHandler
    onclosing: EventHandler
    onclose: EventHandler
    def close(self): ...
    onmessage: EventHandler
    binaryType: BinaryType
    @overload
    def send(self, data: USVString): ...
    @overload
    def send(self, data: Blob): ...
    @overload
    def send(self, data: ArrayBuffer): ...
    @overload
    def send(self, data: ArrayBufferView): ...
    priority: RTCPriorityType

class RTCDataChannelEvent(Event):
    def New(self, type: str, eventInitDict: RTCDataChannelEventInit) -> RTCDataChannelEvent: ...
    channel: RTCDataChannel

class RTCDTMFSender(EventTarget):
    def insertDTMF(self, tones: str, duration: int | None = 100, interToneGap: int | None = 70): ...
    ontonechange: EventHandler
    canInsertDTMF: bool
    toneBuffer: str

class RTCDTMFToneChangeEvent(Event):
    def New(self, type: str, eventInitDict: RTCDTMFToneChangeEventInit | None = {}) -> RTCDTMFToneChangeEvent: ...
    tone: str

class RTCStatsReport: ...

class RTCError(DOMException):
    def New(self, init: RTCErrorInit, message: str | None = "") -> RTCError: ...
    errorDetail: RTCErrorDetailType
    sdpLineNumber: int | None
    sctpCauseCode: int | None
    receivedAlert: int | None
    sentAlert: int | None
    httpRequestStatusCode: int | None

class RTCErrorEvent(Event):
    def New(self, type: str, eventInitDict: RTCErrorEventInit) -> RTCErrorEvent: ...
    error: RTCError

class DigitalGoodsService:
    def getDetails(self, itemIds: Sequence[str]) -> Awaitable[Sequence[ItemDetails]]: ...
    def listPurchases(self) -> Awaitable[Sequence[PurchaseDetails]]: ...
    def listPurchaseHistory(self) -> Awaitable[Sequence[PurchaseDetails]]: ...
    def consume(self, purchaseToken: str) -> Awaitable[None]: ...

class RTCIdentityProviderGlobalScope(WorkerGlobalScope):
    rtcIdentityProvider: RTCIdentityProviderRegistrar

class RTCIdentityProviderRegistrar:
    def register(self, idp: RTCIdentityProvider): ...

class RTCIdentityAssertion:
    def New(self, idp: str, name: str) -> RTCIdentityAssertion: ...
    idp: str
    name: str

class NavigatorNetworkInformation:
    connection: NetworkInformation

class WEBGL_blend_equation_advanced_coherent: ...

class ANGLE_instanced_arrays:
    def drawArraysInstancedANGLE(self, mode: GLenum, first: GLint, count: GLsizei, primcount: GLsizei): ...
    def drawElementsInstancedANGLE(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr, primcount: GLsizei): ...
    def vertexAttribDivisorANGLE(self, index: GLuint, divisor: GLuint): ...

class EXT_texture_compression_bptc: ...

class PermissionsPolicy:
    def allowsFeature(self, feature: str, origin: str | None = None) -> bool: ...
    def features(self) -> Sequence[str]: ...
    def allowedFeatures(self) -> Sequence[str]: ...
    def getAllowlistForFeature(self, feature: str) -> Sequence[str]: ...

class HTMLIFrameElement(HTMLElement):
    def New(self) -> HTMLIFrameElement: ...
    permissionsPolicy: PermissionsPolicy
    fetchPriority: str
    src: USVString
    srcdoc: str
    name: str
    sandbox: DOMTokenList
    allow: str
    allowFullscreen: bool
    width: str
    height: str
    referrerPolicy: str
    loading: str
    contentDocument: Document | None
    contentWindow: WindowProxy | None
    def getSVGDocument(self) -> Document | None: ...
    align: str
    scrolling: str
    frameBorder: str
    longDesc: USVString
    marginHeight: str
    marginWidth: str
    csp: str

class PermissionsPolicyViolationReportBody(ReportBody):
    featureId: str
    sourceFile: str | None
    lineNumber: int | None
    columnNumber: int | None
    disposition: str

class File(Blob):
    def New(self, fileBits: Sequence[BlobPart], fileName: USVString, options: FilePropertyBag | None = {}) -> File: ...
    webkitRelativePath: USVString
    name: str
    lastModified: int

class HTMLInputElement(HTMLElement):
    def New(self) -> HTMLInputElement: ...
    webkitdirectory: bool
    webkitEntries: Sequence[FileSystemEntry]
    accept: str
    alt: str
    autocomplete: str
    defaultChecked: bool
    checked: bool
    dirName: str
    disabled: bool
    form: HTMLFormElement | None
    files: FileList | None
    formAction: USVString
    formEnctype: str
    formMethod: str
    formNoValidate: bool
    formTarget: str
    height: int
    indeterminate: bool
    list: HTMLDataListElement | None
    max: str
    maxLength: int
    min: str
    minLength: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    readOnly: bool
    required: bool
    size: int
    src: USVString
    step: str
    type: str
    defaultValue: str
    value: str
    valueAsDate: object | None
    valueAsNumber: float
    width: int
    def stepUp(self, n: int | None = 1): ...
    def stepDown(self, n: int | None = 1): ...
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    labels: NodeList | None
    def select(self): ...
    selectionStart: int | None
    selectionEnd: int | None
    selectionDirection: str | None
    @overload
    def setRangeText(self, replacement: str): ...
    @overload
    def setRangeText(self, replacement: str, start: int, end: int, selectionMode: SelectionMode | None = "preserve"): ...
    def setSelectionRange(self, start: int, end: int, direction: str | None = None): ...
    def showPicker(self): ...
    align: str
    useMap: str
    capture: str

class DataTransferItem:
    def webkitGetAsEntry(self) -> FileSystemEntry | None: ...
    kind: str
    type: str
    def getAsString(self, callback: FunctionStringCallback | None): ...
    def getAsFile(self) -> File | None: ...
    def getAsFileSystemHandle(self) -> Awaitable[FileSystemHandle | None]: ...

class FileSystemEntry:
    isFile: bool
    isDirectory: bool
    name: USVString
    fullPath: USVString
    filesystem: FileSystem
    def getParent(self, successCallback: FileSystemEntryCallback | None = None, errorCallback: ErrorCallback | None = None): ...

class FileSystemDirectoryEntry(FileSystemEntry):
    def createReader(self) -> FileSystemDirectoryReader: ...
    def getFile(self, path: USVString | None = None, options: FileSystemFlags | None = {}, successCallback: FileSystemEntryCallback | None = None, errorCallback: ErrorCallback | None = None): ...
    def getDirectory(self, path: USVString | None = None, options: FileSystemFlags | None = {}, successCallback: FileSystemEntryCallback | None = None, errorCallback: ErrorCallback | None = None): ...

class FileSystemDirectoryReader:
    def readEntries(self, successCallback: FileSystemEntriesCallback, errorCallback: ErrorCallback | None = None): ...

class FileSystemFileEntry(FileSystemEntry):
    def file(self, successCallback: FileCallback, errorCallback: ErrorCallback | None = None): ...

class FileSystem:
    name: USVString
    root: FileSystemDirectoryEntry

class NavigatorAutomationInformation:
    webdriver: bool

class NavigatorLocks:
    locks: LockManager

class LockManager:
    def query(self) -> Awaitable[LockManagerSnapshot]: ...

class Lock:
    name: str
    mode: LockMode

class CaptureController:
    def New(self) -> CaptureController: ...
    def setFocusBehavior(self, focusBehavior: CaptureStartFocusBehavior): ...

class IdentityCredential(Credential):
    token: USVString | None

class IdentityProvider: ...

class OVR_multiview2:
    def framebufferTextureMultiviewOVR(self, target: GLenum, attachment: GLenum, texture: WebGLTexture | None, level: GLint, baseViewIndex: GLint, numViews: GLsizei): ...

class EXT_frag_depth: ...

class MediaCapabilities:
    def decodingInfo(self, configuration: MediaDecodingConfiguration) -> Awaitable[MediaCapabilitiesDecodingInfo]: ...
    def encodingInfo(self, configuration: MediaEncodingConfiguration) -> Awaitable[MediaCapabilitiesEncodingInfo]: ...

class BeforeInstallPromptEvent(Event):
    def New(self, type: str, eventInitDict: EventInit | None = {}) -> BeforeInstallPromptEvent: ...
    def prompt(self) -> Awaitable[PromptResponseObject]: ...

class PerformanceEntry:
    name: str
    entryType: str
    startTime: DOMHighResTimeStamp
    duration: DOMHighResTimeStamp
    def toJSON(self) -> object: ...

class PerformanceObserver:
    def New(self, callback: PerformanceObserverCallback) -> PerformanceObserver: ...
    def observe(self, options: PerformanceObserverInit | None = {}): ...
    def disconnect(self): ...
    def takeRecords(self) -> PerformanceEntryList: ...

class PerformanceObserverEntryList:
    def getEntries(self) -> PerformanceEntryList: ...
    def getEntriesByType(self, type: str) -> PerformanceEntryList: ...
    def getEntriesByName(self, name: str, type: str | None = None) -> PerformanceEntryList: ...

class JsonLdProcessor:
    def New(self) -> JsonLdProcessor: ...

class CSSConditionRule(CSSGroupingRule):
    conditionText: CSSOMString

class CSSMediaRule(CSSConditionRule):
    media: MediaList

class CSSSupportsRule(CSSConditionRule): ...

class DOMPointReadOnly:
    def New(self, x: float | None = 0, y: float | None = 0, z: float | None = 0, w: float | None = 1) -> DOMPointReadOnly: ...
    x: float
    y: float
    z: float
    w: float
    def matrixTransform(self, matrix: DOMMatrixInit | None = {}) -> DOMPoint: ...
    def toJSON(self) -> object: ...

class DOMPoint(DOMPointReadOnly):
    def New(self, x: float | None = 0, y: float | None = 0, z: float | None = 0, w: float | None = 1) -> DOMPoint: ...
    x: float
    y: float
    z: float
    w: float

class DOMRectReadOnly:
    def New(self, x: float | None = 0, y: float | None = 0, width: float | None = 0, height: float | None = 0) -> DOMRectReadOnly: ...
    x: float
    y: float
    width: float
    height: float
    top: float
    right: float
    bottom: float
    left: float
    def toJSON(self) -> object: ...

class DOMRect(DOMRectReadOnly):
    def New(self, x: float | None = 0, y: float | None = 0, width: float | None = 0, height: float | None = 0) -> DOMRect: ...
    x: float
    y: float
    width: float
    height: float

class DOMRectList:
    length: int

class DOMQuad:
    def New(self, p1: DOMPointInit | None = {}, p2: DOMPointInit | None = {}, p3: DOMPointInit | None = {}, p4: DOMPointInit | None = {}) -> DOMQuad: ...
    p1: DOMPoint
    p2: DOMPoint
    p3: DOMPoint
    p4: DOMPoint
    def getBounds(self) -> DOMRect: ...
    def toJSON(self) -> object: ...

class DOMMatrixReadOnly:
    def New(self, init: str | Sequence[float] | None = None) -> DOMMatrixReadOnly: ...
    a: float
    b: float
    c: float
    d: float
    e: float
    f: float
    m11: float
    m12: float
    m13: float
    m14: float
    m21: float
    m22: float
    m23: float
    m24: float
    m31: float
    m32: float
    m33: float
    m34: float
    m41: float
    m42: float
    m43: float
    m44: float
    is2D: bool
    isIdentity: bool
    def translate(self, tx: float | None = 0, ty: float | None = 0, tz: float | None = 0) -> DOMMatrix: ...
    def scale(self, scaleX: float | None = 1, scaleY: float | None = None, scaleZ: float | None = 1, originX: float | None = 0, originY: float | None = 0, originZ: float | None = 0) -> DOMMatrix: ...
    def scaleNonUniform(self, scaleX: float | None = 1, scaleY: float | None = 1) -> DOMMatrix: ...
    def scale3d(self, scale: float | None = 1, originX: float | None = 0, originY: float | None = 0, originZ: float | None = 0) -> DOMMatrix: ...
    def rotate(self, rotX: float | None = 0, rotY: float | None = None, rotZ: float | None = None) -> DOMMatrix: ...
    def rotateFromVector(self, x: float | None = 0, y: float | None = 0) -> DOMMatrix: ...
    def rotateAxisAngle(self, x: float | None = 0, y: float | None = 0, z: float | None = 0, angle: float | None = 0) -> DOMMatrix: ...
    def skewX(self, sx: float | None = 0) -> DOMMatrix: ...
    def skewY(self, sy: float | None = 0) -> DOMMatrix: ...
    def multiply(self, other: DOMMatrixInit | None = {}) -> DOMMatrix: ...
    def flipX(self) -> DOMMatrix: ...
    def flipY(self) -> DOMMatrix: ...
    def inverse(self) -> DOMMatrix: ...
    def transformPoint(self, point: DOMPointInit | None = {}) -> DOMPoint: ...
    def toFloat32Array(self) -> Float32Array: ...
    def toFloat64Array(self) -> Float64Array: ...
    def toJSON(self) -> object: ...

class DOMMatrix(DOMMatrixReadOnly):
    def New(self, init: str | Sequence[float] | None = None) -> DOMMatrix: ...
    a: float
    b: float
    c: float
    d: float
    e: float
    f: float
    m11: float
    m12: float
    m13: float
    m14: float
    m21: float
    m22: float
    m23: float
    m24: float
    m31: float
    m32: float
    m33: float
    m34: float
    m41: float
    m42: float
    m43: float
    m44: float
    def multiplySelf(self, other: DOMMatrixInit | None = {}) -> DOMMatrix: ...
    def preMultiplySelf(self, other: DOMMatrixInit | None = {}) -> DOMMatrix: ...
    def translateSelf(self, tx: float | None = 0, ty: float | None = 0, tz: float | None = 0) -> DOMMatrix: ...
    def scaleSelf(self, scaleX: float | None = 1, scaleY: float | None = None, scaleZ: float | None = 1, originX: float | None = 0, originY: float | None = 0, originZ: float | None = 0) -> DOMMatrix: ...
    def scale3dSelf(self, scale: float | None = 1, originX: float | None = 0, originY: float | None = 0, originZ: float | None = 0) -> DOMMatrix: ...
    def rotateSelf(self, rotX: float | None = 0, rotY: float | None = None, rotZ: float | None = None) -> DOMMatrix: ...
    def rotateFromVectorSelf(self, x: float | None = 0, y: float | None = 0) -> DOMMatrix: ...
    def rotateAxisAngleSelf(self, x: float | None = 0, y: float | None = 0, z: float | None = 0, angle: float | None = 0) -> DOMMatrix: ...
    def skewXSelf(self, sx: float | None = 0) -> DOMMatrix: ...
    def skewYSelf(self, sy: float | None = 0) -> DOMMatrix: ...
    def invertSelf(self) -> DOMMatrix: ...
    def setMatrixValue(self, transformList: str) -> DOMMatrix: ...

class FontData:
    def blob(self) -> Awaitable[Blob]: ...
    postscriptName: USVString
    fullName: USVString
    family: USVString
    style: USVString

class XRSession(EventTarget):
    depthUsage: XRDepthUsage
    depthDataFormat: XRDepthDataFormat
    environmentBlendMode: XREnvironmentBlendMode
    interactionMode: XRInteractionMode
    domOverlayState: XRDOMOverlayState | None
    def requestLightProbe(self, options: XRLightProbeInit | None = {}) -> Awaitable[XRLightProbe]: ...
    preferredReflectionFormat: XRReflectionFormat
    def requestHitTestSource(self, options: XRHitTestOptionsInit) -> Awaitable[XRHitTestSource]: ...
    def requestHitTestSourceForTransientInput(self, options: XRTransientInputHitTestOptionsInit) -> Awaitable[XRTransientInputHitTestSource]: ...
    def restorePersistentAnchor(self, uuid: str) -> Awaitable[XRAnchor]: ...
    def deletePersistentAnchor(self, uuid: str) -> Awaitable[None]: ...
    visibilityState: XRVisibilityState
    frameRate: float | None
    supportedFrameRates: Float32Array
    renderState: XRRenderState
    inputSources: XRInputSourceArray
    enabledFeatures: Sequence[str]
    def updateRenderState(self, state: XRRenderStateInit | None = {}): ...
    def updateTargetFrameRate(self, rate: float) -> Awaitable[None]: ...
    def requestReferenceSpace(self, type: XRReferenceSpaceType) -> Awaitable[XRReferenceSpace]: ...
    def requestAnimationFrame(self, callback: XRFrameRequestCallback) -> int: ...
    def cancelAnimationFrame(self, handle: int): ...
    def end(self) -> Awaitable[None]: ...
    onend: EventHandler
    oninputsourceschange: EventHandler
    onselect: EventHandler
    onselectstart: EventHandler
    onselectend: EventHandler
    onsqueeze: EventHandler
    onsqueezestart: EventHandler
    onsqueezeend: EventHandler
    onvisibilitychange: EventHandler
    onframeratechange: EventHandler

class XRDepthInformation:
    width: int
    height: int
    normDepthBufferFromNormView: XRRigidTransform
    rawValueToMeters: float

class XRCPUDepthInformation(XRDepthInformation):
    data: ArrayBuffer
    def getDepthInMeters(self, x: float, y: float) -> float: ...

class XRFrame:
    def getDepthInformation(self, view: XRView) -> XRCPUDepthInformation | None: ...
    def getJointPose(self, joint: XRJointSpace, baseSpace: XRSpace) -> XRJointPose | None: ...
    def fillJointRadii(self, jointSpaces: Sequence[XRJointSpace], radii: Float32Array) -> bool: ...
    def fillPoses(self, spaces: Sequence[XRSpace], baseSpace: XRSpace, transforms: Float32Array) -> bool: ...
    def getLightEstimate(self, lightProbe: XRLightProbe) -> XRLightEstimate | None: ...
    def getHitTestResults(self, hitTestSource: XRHitTestSource) -> Sequence[XRHitTestResult]: ...
    def getHitTestResultsForTransientInput(self, hitTestSource: XRTransientInputHitTestSource) -> Sequence[XRTransientInputHitTestResult]: ...
    def createAnchor(self, pose: XRRigidTransform, space: XRSpace) -> Awaitable[XRAnchor]: ...
    trackedAnchors: XRAnchorSet
    session: XRSession
    predictedDisplayTime: DOMHighResTimeStamp
    def getViewerPose(self, referenceSpace: XRReferenceSpace) -> XRViewerPose | None: ...
    def getPose(self, space: XRSpace, baseSpace: XRSpace) -> XRPose | None: ...

class XRWebGLDepthInformation(XRDepthInformation):
    texture: WebGLTexture

class XRWebGLBinding:
    def New(self, session: XRSession, context: XRWebGLRenderingContext) -> XRWebGLBinding: ...
    def getDepthInformation(self, view: XRView) -> XRWebGLDepthInformation | None: ...
    def getReflectionCubeMap(self, lightProbe: XRLightProbe) -> WebGLTexture | None: ...
    nativeProjectionScaleFactor: float
    usesDepthValues: bool
    def createProjectionLayer(self, init: XRProjectionLayerInit | None = {}) -> XRProjectionLayer: ...
    def createQuadLayer(self, init: XRQuadLayerInit | None = {}) -> XRQuadLayer: ...
    def createCylinderLayer(self, init: XRCylinderLayerInit | None = {}) -> XRCylinderLayer: ...
    def createEquirectLayer(self, init: XREquirectLayerInit | None = {}) -> XREquirectLayer: ...
    def createCubeLayer(self, init: XRCubeLayerInit | None = {}) -> XRCubeLayer: ...
    def getSubImage(self, layer: XRCompositionLayer, frame: XRFrame, eye: XREye | None = "none") -> XRWebGLSubImage: ...
    def getViewSubImage(self, layer: XRProjectionLayer, view: XRView) -> XRWebGLSubImage: ...
    def getCameraImage(self, camera: XRCamera) -> WebGLTexture | None: ...

class PerformancePaintTiming(PerformanceEntry): ...

class PaintWorkletGlobalScope(WorkletGlobalScope):
    def registerPaint(self, name: str, paintCtor: VoidFunction): ...
    devicePixelRatio: float

class PaintRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing, CanvasImageSmoothing, CanvasFillStrokeStyles, CanvasShadowStyles, CanvasRect, CanvasDrawPath, CanvasDrawImage, CanvasPathDrawingStyles, CanvasPath): ...

class PaintSize:
    width: float
    height: float

class LayoutShift(PerformanceEntry):
    value: float
    hadRecentInput: bool
    lastInputTime: DOMHighResTimeStamp
    sources: Sequence[LayoutShiftAttribution]
    def toJSON(self) -> object: ...

class LayoutShiftAttribution:
    node: Node | None
    previousRect: DOMRectReadOnly
    currentRect: DOMRectReadOnly

class IdleDeadline:
    def timeRemaining(self) -> DOMHighResTimeStamp: ...
    didTimeout: bool

class CSSCounterStyleRule(CSSRule):
    name: CSSOMString
    system: CSSOMString
    symbols: CSSOMString
    additiveSymbols: CSSOMString
    negative: CSSOMString
    prefix: CSSOMString
    suffix: CSSOMString
    range: CSSOMString
    pad: CSSOMString
    speakAs: CSSOMString
    fallback: CSSOMString

class EyeDropper:
    def New(self) -> EyeDropper: ...
    def open(self, options: ColorSelectionOptions | None = {}) -> Awaitable[ColorSelectionResult]: ...

class Scheduling:
    def isInputPending(self, isInputPendingOptions: IsInputPendingOptions | None = {}) -> bool: ...

class Accelerometer(Sensor):
    def New(self, options: AccelerometerSensorOptions | None = {}) -> Accelerometer: ...
    x: float | None
    y: float | None
    z: float | None

class LinearAccelerationSensor(Accelerometer):
    def New(self, options: AccelerometerSensorOptions | None = {}) -> LinearAccelerationSensor: ...

class GravitySensor(Accelerometer):
    def New(self, options: AccelerometerSensorOptions | None = {}) -> GravitySensor: ...

class ScriptingPolicyReportBody(ReportBody):
    def toJSON(self) -> object: ...
    violationType: str
    violationURL: USVString | None
    violationSample: USVString | None
    lineno: int
    colno: int

class ResizeObserver:
    def New(self, callback: ResizeObserverCallback) -> ResizeObserver: ...
    def observe(self, target: Element, options: ResizeObserverOptions | None = {}): ...
    def unobserve(self, target: Element): ...
    def disconnect(self): ...

class ResizeObserverEntry:
    target: Element
    contentRect: DOMRectReadOnly
    borderBoxSize: Sequence[ResizeObserverSize]
    contentBoxSize: Sequence[ResizeObserverSize]
    devicePixelContentBoxSize: Sequence[ResizeObserverSize]

class ResizeObserverSize:
    inlineSize: float
    blockSize: float

class USB(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler
    def getDevices(self) -> Awaitable[Sequence[USBDevice]]: ...
    def requestDevice(self, options: USBDeviceRequestOptions) -> Awaitable[USBDevice]: ...

class USBConnectionEvent(Event):
    def New(self, type: str, eventInitDict: USBConnectionEventInit) -> USBConnectionEvent: ...
    device: USBDevice

class USBInTransferResult:
    def New(self, status: USBTransferStatus, data: DataView | None = None) -> USBInTransferResult: ...
    data: DataView
    status: USBTransferStatus

class USBOutTransferResult:
    def New(self, status: USBTransferStatus, bytesWritten: int | None = 0) -> USBOutTransferResult: ...
    bytesWritten: int
    status: USBTransferStatus

class USBIsochronousInTransferPacket:
    def New(self, status: USBTransferStatus, data: DataView | None = None) -> USBIsochronousInTransferPacket: ...
    data: DataView
    status: USBTransferStatus

class USBIsochronousInTransferResult:
    def New(self, packets: Sequence[USBIsochronousInTransferPacket], data: DataView | None = None) -> USBIsochronousInTransferResult: ...
    data: DataView
    packets: Sequence[USBIsochronousInTransferPacket]

class USBIsochronousOutTransferPacket:
    def New(self, status: USBTransferStatus, bytesWritten: int | None = 0) -> USBIsochronousOutTransferPacket: ...
    bytesWritten: int
    status: USBTransferStatus

class USBIsochronousOutTransferResult:
    def New(self, packets: Sequence[USBIsochronousOutTransferPacket]) -> USBIsochronousOutTransferResult: ...
    packets: Sequence[USBIsochronousOutTransferPacket]

class USBDevice:
    usbVersionMajor: octet
    usbVersionMinor: octet
    usbVersionSubminor: octet
    deviceClass: octet
    deviceSubclass: octet
    deviceProtocol: octet
    vendorId: int
    productId: int
    deviceVersionMajor: octet
    deviceVersionMinor: octet
    deviceVersionSubminor: octet
    manufacturerName: str | None
    productName: str | None
    serialNumber: str | None
    configuration: USBConfiguration | None
    configurations: Sequence[USBConfiguration]
    opened: bool
    def open(self) -> Awaitable[None]: ...
    def close(self) -> Awaitable[None]: ...
    def forget(self) -> Awaitable[None]: ...
    def selectConfiguration(self, configurationValue: octet) -> Awaitable[None]: ...
    def claimInterface(self, interfaceNumber: octet) -> Awaitable[None]: ...
    def releaseInterface(self, interfaceNumber: octet) -> Awaitable[None]: ...
    def selectAlternateInterface(self, interfaceNumber: octet, alternateSetting: octet) -> Awaitable[None]: ...
    def controlTransferIn(self, setup: USBControlTransferParameters, length: int) -> Awaitable[USBInTransferResult]: ...
    def controlTransferOut(self, setup: USBControlTransferParameters, data: BufferSource | None = None) -> Awaitable[USBOutTransferResult]: ...
    def clearHalt(self, direction: USBDirection, endpointNumber: octet) -> Awaitable[None]: ...
    def transferIn(self, endpointNumber: octet, length: int) -> Awaitable[USBInTransferResult]: ...
    def transferOut(self, endpointNumber: octet, data: BufferSource) -> Awaitable[USBOutTransferResult]: ...
    def isochronousTransferIn(self, endpointNumber: octet, packetLengths: Sequence[int]) -> Awaitable[USBIsochronousInTransferResult]: ...
    def isochronousTransferOut(self, endpointNumber: octet, data: BufferSource, packetLengths: Sequence[int]) -> Awaitable[USBIsochronousOutTransferResult]: ...
    def reset(self) -> Awaitable[None]: ...

class USBConfiguration:
    def New(self, device: USBDevice, configurationValue: octet) -> USBConfiguration: ...
    configurationValue: octet
    configurationName: str | None
    interfaces: Sequence[USBInterface]

class USBInterface:
    def New(self, configuration: USBConfiguration, interfaceNumber: octet) -> USBInterface: ...
    interfaceNumber: octet
    alternate: USBAlternateInterface
    alternates: Sequence[USBAlternateInterface]
    claimed: bool

class USBAlternateInterface:
    def New(self, deviceInterface: USBInterface, alternateSetting: octet) -> USBAlternateInterface: ...
    alternateSetting: octet
    interfaceClass: octet
    interfaceSubclass: octet
    interfaceProtocol: octet
    interfaceName: str | None
    endpoints: Sequence[USBEndpoint]

class USBEndpoint:
    def New(self, alternate: USBAlternateInterface, endpointNumber: octet, direction: USBDirection) -> USBEndpoint: ...
    endpointNumber: octet
    direction: USBDirection
    type: USBEndpointType
    packetSize: int

class USBPermissionResult(PermissionStatus):
    devices: Sequence[USBDevice]

class Selection:
    anchorNode: Node | None
    anchorOffset: int
    focusNode: Node | None
    focusOffset: int
    isCollapsed: bool
    rangeCount: int
    type: str
    def getRangeAt(self, index: int) -> Range: ...
    def addRange(self, range: Range): ...
    def removeRange(self, range: Range): ...
    def removeAllRanges(self): ...
    def empty(self): ...
    def getComposedRange(self, shadowRoots: ShadowRoot | None = None) -> StaticRange: ...
    def collapse(self, node: Node | None, offset: int | None = 0): ...
    def setPosition(self, node: Node | None, offset: int | None = 0): ...
    def collapseToStart(self): ...
    def collapseToEnd(self): ...
    def extend(self, node: Node, offset: int | None = 0): ...
    def setBaseAndExtent(self, anchorNode: Node, anchorOffset: int, focusNode: Node, focusOffset: int): ...
    def selectAllChildren(self, node: Node): ...
    def modify(self, alter: str | None = None, direction: str | None = None, granularity: str | None = None): ...
    def deleteFromDocument(self): ...
    def containsNode(self, node: Node, allowPartialContainment: bool | None = false) -> bool: ...

class XMLHttpRequestEventTarget(EventTarget):
    onloadstart: EventHandler
    onprogress: EventHandler
    onabort: EventHandler
    onerror: EventHandler
    onload: EventHandler
    ontimeout: EventHandler
    onloadend: EventHandler

class XMLHttpRequestUpload(XMLHttpRequestEventTarget): ...

class XMLHttpRequest(XMLHttpRequestEventTarget):
    def New(self) -> XMLHttpRequest: ...
    onreadystatechange: EventHandler
    readyState: int
    @overload
    def open(self, method: ByteString, url: USVString): ...
    @overload
    def open(self, method: ByteString, url: USVString, async_: bool, username: USVString | None = None, password: USVString | None = None): ...
    def setRequestHeader(self, name: ByteString, value: ByteString): ...
    timeout: int
    withCredentials: bool
    upload: XMLHttpRequestUpload
    def send(self, body: Document | XMLHttpRequestBodyInit | None = None): ...
    def abort(self): ...
    responseURL: USVString
    status: int
    statusText: ByteString
    def getResponseHeader(self, name: ByteString) -> ByteString | None: ...
    def getAllResponseHeaders(self) -> ByteString: ...
    def overrideMimeType(self, mime: str): ...
    responseType: XMLHttpRequestResponseType
    responseText: USVString
    responseXML: Document | None

class FormData:
    def New(self, form: HTMLFormElement | None = None) -> FormData: ...
    @overload
    def append(self, name: USVString, value: USVString): ...
    @overload
    def append(self, name: USVString, blobValue: Blob, filename: USVString | None = None): ...
    def delete(self, name: USVString): ...
    def get(self, name: USVString) -> FormDataEntryValue | None: ...
    def getAll(self, name: USVString) -> Sequence[FormDataEntryValue]: ...
    def has(self, name: USVString) -> bool: ...
    @overload
    def set(self, name: USVString, value: USVString): ...
    @overload
    def set(self, name: USVString, blobValue: Blob, filename: USVString | None = None): ...

class ProgressEvent(Event):
    def New(self, type: str, eventInitDict: ProgressEventInit | None = {}) -> ProgressEvent: ...
    lengthComputable: bool
    loaded: int
    total: int

class URL:
    def New(self, url: USVString, base: USVString | None = None) -> URL: ...
    origin: USVString
    protocol: USVString
    username: USVString
    password: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    searchParams: URLSearchParams
    hash: USVString
    def toJSON(self) -> USVString: ...

class URLSearchParams:
    def New(self, init: Sequence[Sequence[USVString]] | USVString | USVString | None = "") -> URLSearchParams: ...
    def append(self, name: USVString, value: USVString): ...
    def delete(self, name: USVString): ...
    def get(self, name: USVString) -> USVString | None: ...
    def getAll(self, name: USVString) -> Sequence[USVString]: ...
    def has(self, name: USVString) -> bool: ...
    def set(self, name: USVString, value: USVString): ...
    def sort(self): ...

class XRView:
    isFirstPersonObserver: bool
    eye: XREye
    projectionMatrix: Float32Array
    transform: XRRigidTransform
    recommendedViewportScale: float | None
    def requestViewportScale(self, scale: float | None): ...
    camera: XRCamera | None

class PerformanceElementTiming(PerformanceEntry):
    renderTime: DOMHighResTimeStamp
    loadTime: DOMHighResTimeStamp
    intersectionRect: DOMRectReadOnly
    identifier: str
    naturalWidth: int
    naturalHeight: int
    id: str
    element: Element | None
    url: str
    def toJSON(self) -> object: ...

class WindowControlsOverlay(EventTarget):
    visible: bool
    def getTitlebarAreaRect(self) -> DOMRect: ...
    ongeometrychange: EventHandler

class WindowControlsOverlayGeometryChangeEvent(Event):
    def New(self, type: str, eventInitDict: WindowControlsOverlayGeometryChangeEventInit) -> WindowControlsOverlayGeometryChangeEvent: ...
    titlebarAreaRect: DOMRect
    visible: bool

class TrustedHTML:
    def toJSON(self) -> str: ...

class TrustedScript:
    def toJSON(self) -> str: ...

class TrustedScriptURL:
    def toJSON(self) -> USVString: ...

class TrustedTypePolicyFactory:
    def createPolicy(self, policyName: str, policyOptions: TrustedTypePolicyOptions | None = {}) -> TrustedTypePolicy: ...
    emptyHTML: TrustedHTML
    emptyScript: TrustedScript
    def getAttributeType(self, tagName: str, attribute: str, elementNs: str | None = "", attrNs: str | None = "") -> str | None: ...
    def getPropertyType(self, tagName: str, property: str, elementNs: str | None = "") -> str | None: ...
    defaultPolicy: TrustedTypePolicy | None

class TrustedTypePolicy:
    name: str

class MathMLElement(Element, GlobalEventHandlers, HTMLOrSVGElement, ElementCSSInlineStyle): ...

class AudioDecoder:
    def New(self, init: AudioDecoderInit) -> AudioDecoder: ...
    state: CodecState
    decodeQueueSize: int
    ondequeue: EventHandler
    def configure(self, config: AudioDecoderConfig): ...
    def decode(self, chunk: EncodedAudioChunk): ...
    def flush(self) -> Awaitable[None]: ...
    def reset(self): ...
    def close(self): ...

class VideoDecoder:
    def New(self, init: VideoDecoderInit) -> VideoDecoder: ...
    state: CodecState
    decodeQueueSize: int
    ondequeue: EventHandler
    def configure(self, config: VideoDecoderConfig): ...
    def decode(self, chunk: EncodedVideoChunk): ...
    def flush(self) -> Awaitable[None]: ...
    def reset(self): ...
    def close(self): ...

class AudioEncoder:
    def New(self, init: AudioEncoderInit) -> AudioEncoder: ...
    state: CodecState
    encodeQueueSize: int
    ondequeue: EventHandler
    def configure(self, config: AudioEncoderConfig): ...
    def encode(self, data: AudioData): ...
    def flush(self) -> Awaitable[None]: ...
    def reset(self): ...
    def close(self): ...

class VideoEncoder:
    def New(self, init: VideoEncoderInit) -> VideoEncoder: ...
    state: CodecState
    encodeQueueSize: int
    ondequeue: EventHandler
    def configure(self, config: VideoEncoderConfig): ...
    def encode(self, frame: VideoFrame, options: VideoEncoderEncodeOptions | None = {}): ...
    def flush(self) -> Awaitable[None]: ...
    def reset(self): ...
    def close(self): ...

class EncodedAudioChunk:
    def New(self, init: EncodedAudioChunkInit) -> EncodedAudioChunk: ...
    type: EncodedAudioChunkType
    timestamp: int
    duration: int | None
    byteLength: int
    def copyTo(self, destination: BufferSource): ...

class EncodedVideoChunk:
    def New(self, init: EncodedVideoChunkInit) -> EncodedVideoChunk: ...
    type: EncodedVideoChunkType
    timestamp: int
    duration: int | None
    byteLength: int
    def copyTo(self, destination: BufferSource): ...

class AudioData:
    def New(self, init: AudioDataInit) -> AudioData: ...
    format: AudioSampleFormat | None
    sampleRate: float
    numberOfFrames: int
    numberOfChannels: int
    duration: int
    timestamp: int
    def allocationSize(self, options: AudioDataCopyToOptions) -> int: ...
    def copyTo(self, destination: BufferSource, options: AudioDataCopyToOptions): ...
    def clone(self) -> AudioData: ...
    def close(self): ...

class VideoFrame:
    @overload
    def New(self, image: CanvasImageSource, init: VideoFrameInit | None = {}) -> VideoFrame: ...
    @overload
    def New(self, data: BufferSource, init: VideoFrameBufferInit) -> VideoFrame: ...
    format: VideoPixelFormat | None
    codedWidth: int
    codedHeight: int
    codedRect: DOMRectReadOnly | None
    visibleRect: DOMRectReadOnly | None
    displayWidth: int
    displayHeight: int
    duration: int | None
    timestamp: int
    colorSpace: VideoColorSpace
    def metadata(self) -> VideoFrameMetadata: ...
    def allocationSize(self, options: VideoFrameCopyToOptions | None = {}) -> int: ...
    def copyTo(self, destination: BufferSource, options: VideoFrameCopyToOptions | None = {}) -> Awaitable[Sequence[PlaneLayout]]: ...
    def clone(self) -> VideoFrame: ...
    def close(self): ...

class VideoColorSpace:
    def New(self, init: VideoColorSpaceInit | None = {}) -> VideoColorSpace: ...
    primaries: VideoColorPrimaries | None
    transfer: VideoTransferCharacteristics | None
    matrix: VideoMatrixCoefficients | None
    fullRange: bool | None
    def toJSON(self) -> VideoColorSpaceInit: ...

class ImageDecoder:
    def New(self, init: ImageDecoderInit) -> ImageDecoder: ...
    type: str
    complete: bool
    completed: Awaitable[None]
    tracks: ImageTrackList
    def decode(self, options: ImageDecodeOptions | None = {}) -> Awaitable[ImageDecodeResult]: ...
    def reset(self): ...
    def close(self): ...

class ImageTrackList:
    ready: Awaitable[None]
    length: int
    selectedIndex: int
    selectedTrack: ImageTrack | None

class ImageTrack:
    animated: bool
    frameCount: int
    repetitionCount: float
    selected: bool

class BackgroundFetchManager:
    def fetch(self, id: str, requests: RequestInfo | Sequence[RequestInfo], options: BackgroundFetchOptions | None = {}) -> Awaitable[BackgroundFetchRegistration]: ...
    def get(self, id: str) -> Awaitable[BackgroundFetchRegistration | None]: ...
    def getIds(self) -> Awaitable[Sequence[str]]: ...

class BackgroundFetchRegistration(EventTarget):
    id: str
    uploadTotal: int
    uploaded: int
    downloadTotal: int
    downloaded: int
    result: BackgroundFetchResult
    failureReason: BackgroundFetchFailureReason
    recordsAvailable: bool
    onprogress: EventHandler
    def abort(self) -> Awaitable[bool]: ...
    def match(self, request: RequestInfo, options: CacheQueryOptions | None = {}) -> Awaitable[BackgroundFetchRecord]: ...
    def matchAll(self, request: RequestInfo | None = None, options: CacheQueryOptions | None = {}) -> Awaitable[Sequence[BackgroundFetchRecord]]: ...

class BackgroundFetchRecord:
    request: Request
    responseReady: Awaitable[Response]

class BackgroundFetchEvent(ExtendableEvent):
    def New(self, type: str, init: BackgroundFetchEventInit) -> BackgroundFetchEvent: ...
    registration: BackgroundFetchRegistration

class BackgroundFetchUpdateUIEvent(BackgroundFetchEvent):
    def New(self, type: str, init: BackgroundFetchEventInit) -> BackgroundFetchUpdateUIEvent: ...
    def updateUI(self, options: BackgroundFetchUIOptions | None = {}) -> Awaitable[None]: ...

class Ink:
    def requestPresenter(self, param: InkPresenterParam | None = {}) -> Awaitable[InkPresenter]: ...

class InkPresenter:
    presentationArea: Element | None
    expectedImprovement: int
    def updateInkTrailStartPoint(self, event: PointerEvent, style: InkTrailStyle): ...

class HID(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler
    def getDevices(self) -> Awaitable[Sequence[HIDDevice]]: ...
    def requestDevice(self, options: HIDDeviceRequestOptions) -> Awaitable[Sequence[HIDDevice]]: ...

class HIDDevice(EventTarget):
    oninputreport: EventHandler
    opened: bool
    vendorId: int
    productId: int
    productName: str
    collections: Sequence[HIDCollectionInfo]
    def open(self) -> Awaitable[None]: ...
    def close(self) -> Awaitable[None]: ...
    def forget(self) -> Awaitable[None]: ...
    def sendReport(self, reportId: octet, data: BufferSource) -> Awaitable[None]: ...
    def sendFeatureReport(self, reportId: octet, data: BufferSource) -> Awaitable[None]: ...
    def receiveFeatureReport(self, reportId: octet) -> Awaitable[DataView]: ...

class HIDConnectionEvent(Event):
    def New(self, type: str, eventInitDict: HIDConnectionEventInit) -> HIDConnectionEvent: ...
    device: HIDDevice

class HIDInputReportEvent(Event):
    def New(self, type: str, eventInitDict: HIDInputReportEventInit) -> HIDInputReportEvent: ...
    device: HIDDevice
    reportId: octet
    data: DataView

class CSPViolationReportBody(ReportBody):
    def toJSON(self) -> object: ...
    documentURL: USVString
    referrer: USVString | None
    blockedURL: USVString | None
    effectiveDirective: str
    originalPolicy: str
    sourceFile: USVString | None
    sample: str | None
    disposition: SecurityPolicyViolationEventDisposition
    statusCode: int
    lineNumber: int | None
    columnNumber: int | None

class SecurityPolicyViolationEvent(Event):
    def New(self, type: str, eventInitDict: SecurityPolicyViolationEventInit | None = {}) -> SecurityPolicyViolationEvent: ...
    documentURI: USVString
    referrer: USVString
    blockedURI: USVString
    effectiveDirective: str
    violatedDirective: str
    originalPolicy: str
    sourceFile: USVString
    sample: str
    disposition: SecurityPolicyViolationEventDisposition
    statusCode: int
    lineNumber: int
    columnNumber: int

class Headers:
    def New(self, init: HeadersInit | None = None) -> Headers: ...
    def append(self, name: ByteString, value: ByteString): ...
    def delete(self, name: ByteString): ...
    def get(self, name: ByteString) -> ByteString | None: ...
    def has(self, name: ByteString) -> bool: ...
    def set(self, name: ByteString, value: ByteString): ...

class Body:
    body: ReadableStream | None
    bodyUsed: bool
    def arrayBuffer(self) -> Awaitable[ArrayBuffer]: ...
    def blob(self) -> Awaitable[Blob]: ...
    def formData(self) -> Awaitable[FormData]: ...
    def text(self) -> Awaitable[USVString]: ...

class Request(Body):
    def New(self, input: RequestInfo, init: RequestInit | None = {}) -> Request: ...
    method: ByteString
    url: USVString
    headers: Headers
    destination: RequestDestination
    referrer: USVString
    referrerPolicy: ReferrerPolicy
    mode: RequestMode
    credentials: RequestCredentials
    cache: RequestCache
    redirect: RequestRedirect
    integrity: str
    keepalive: bool
    isReloadNavigation: bool
    isHistoryNavigation: bool
    signal: AbortSignal
    duplex: RequestDuplex
    def clone(self) -> Request: ...

class Response(Body):
    def New(self, body: BodyInit | None = None, init: ResponseInit | None = {}) -> Response: ...
    type: ResponseType
    url: USVString
    redirected: bool
    status: int
    ok: bool
    statusText: ByteString
    headers: Headers
    def clone(self) -> Response: ...

class DataCue(TextTrackCue):
    type: str

class EXT_disjoint_timer_query_webgl2:
    def queryCounterEXT(self, query: WebGLQuery, target: GLenum): ...

class OTPCredential(Credential):
    code: str

class Sensor(EventTarget):
    activated: bool
    hasReading: bool
    timestamp: DOMHighResTimeStamp | None
    def start(self): ...
    def stop(self): ...
    onreading: EventHandler
    onactivate: EventHandler
    onerror: EventHandler

class SensorErrorEvent(Event):
    def New(self, type: str, errorEventInitDict: SensorErrorEventInit) -> SensorErrorEvent: ...
    error: DOMException

class WEBGL_compressed_texture_etc: ...

class WebGLVertexArrayObjectOES(WebGLObject): ...

class OES_vertex_array_object:
    def createVertexArrayOES(self) -> WebGLVertexArrayObjectOES | None: ...
    def deleteVertexArrayOES(self, arrayObject: WebGLVertexArrayObjectOES | None): ...
    def isVertexArrayOES(self, arrayObject: WebGLVertexArrayObjectOES | None) -> GLboolean: ...
    def bindVertexArrayOES(self, arrayObject: WebGLVertexArrayObjectOES | None): ...

class ImageCapture:
    def New(self, videoTrack: MediaStreamTrack) -> ImageCapture: ...
    def takePhoto(self, photoSettings: PhotoSettings | None = {}) -> Awaitable[Blob]: ...
    def getPhotoCapabilities(self) -> Awaitable[PhotoCapabilities]: ...
    def getPhotoSettings(self) -> Awaitable[PhotoSettings]: ...
    def grabFrame(self) -> Awaitable[ImageBitmap]: ...
    track: MediaStreamTrack

class CSSContainerRule(CSSConditionRule):
    containerName: CSSOMString
    containerQuery: CSSOMString

class XRHand:
    size: int
    def get(self, key: XRHandJoint) -> XRJointSpace: ...

class XRJointSpace(XRSpace):
    jointName: XRHandJoint

class XRJointPose(XRPose):
    radius: float

class DeprecationReportBody(ReportBody):
    def toJSON(self) -> object: ...
    id: str
    anticipatedRemoval: object | None
    message: str
    sourceFile: str | None
    lineNumber: int | None
    columnNumber: int | None

class IntersectionObserver:
    def New(self, callback: IntersectionObserverCallback, options: IntersectionObserverInit | None = {}) -> IntersectionObserver: ...
    root: Element | Document | None
    rootMargin: str
    thresholds: Sequence[float]
    def observe(self, target: Element): ...
    def unobserve(self, target: Element): ...
    def disconnect(self): ...
    def takeRecords(self) -> Sequence[IntersectionObserverEntry]: ...

class IntersectionObserverEntry:
    def New(self, intersectionObserverEntryInit: IntersectionObserverEntryInit) -> IntersectionObserverEntry: ...
    time: DOMHighResTimeStamp
    rootBounds: DOMRectReadOnly | None
    boundingClientRect: DOMRectReadOnly
    intersectionRect: DOMRectReadOnly
    isIntersecting: bool
    intersectionRatio: float
    target: Element

class EpubReadingSystem:
    def hasFeature(self, feature: str, version: str | None = None) -> bool: ...

class ReadableStream:
    def New(self, underlyingSource: object | None = None, strategy: QueuingStrategy | None = {}) -> ReadableStream: ...
    locked: bool
    def getReader(self, options: ReadableStreamGetReaderOptions | None = {}) -> ReadableStreamReader: ...
    def pipeThrough(self, transform: ReadableWritablePair, options: StreamPipeOptions | None = {}) -> ReadableStream: ...
    def pipeTo(self, destination: WritableStream, options: StreamPipeOptions | None = {}) -> Awaitable[None]: ...
    def tee(self) -> Sequence[ReadableStream]: ...

class ReadableStreamGenericReader:
    closed: Awaitable[None]

class ReadableStreamDefaultReader(ReadableStreamGenericReader):
    def New(self, stream: ReadableStream) -> ReadableStreamDefaultReader: ...
    def read(self) -> Awaitable[ReadableStreamReadResult]: ...
    def releaseLock(self): ...

class ReadableStreamBYOBReader(ReadableStreamGenericReader):
    def New(self, stream: ReadableStream) -> ReadableStreamBYOBReader: ...
    def read(self, view: ArrayBufferView) -> Awaitable[ReadableStreamReadResult]: ...
    def releaseLock(self): ...

class ReadableStreamDefaultController:
    desiredSize: float | None
    def close(self): ...

class ReadableByteStreamController:
    byobRequest: ReadableStreamBYOBRequest | None
    desiredSize: float | None
    def close(self): ...
    def enqueue(self, chunk: ArrayBufferView): ...

class ReadableStreamBYOBRequest:
    view: ArrayBufferView | None
    def respond(self, bytesWritten: int): ...
    def respondWithNewView(self, view: ArrayBufferView): ...

class WritableStream:
    def New(self, underlyingSink: object | None = None, strategy: QueuingStrategy | None = {}) -> WritableStream: ...
    locked: bool
    def close(self) -> Awaitable[None]: ...
    def getWriter(self) -> WritableStreamDefaultWriter: ...

class WritableStreamDefaultWriter:
    def New(self, stream: WritableStream) -> WritableStreamDefaultWriter: ...
    closed: Awaitable[None]
    desiredSize: float | None
    ready: Awaitable[None]
    def close(self) -> Awaitable[None]: ...
    def releaseLock(self): ...

class WritableStreamDefaultController:
    signal: AbortSignal

class TransformStream:
    def New(self, transformer: object | None = None, writableStrategy: QueuingStrategy | None = {}, readableStrategy: QueuingStrategy | None = {}) -> TransformStream: ...
    readable: ReadableStream
    writable: WritableStream

class TransformStreamDefaultController:
    desiredSize: float | None
    def terminate(self): ...

class ByteLengthQueuingStrategy:
    def New(self, init: QueuingStrategyInit) -> ByteLengthQueuingStrategy: ...
    highWaterMark: float
    size: Function

class CountQueuingStrategy:
    def New(self, init: QueuingStrategyInit) -> CountQueuingStrategy: ...
    highWaterMark: float
    size: Function

class GenericTransformStream:
    readable: ReadableStream
    writable: WritableStream

class CSSFontFaceRule(CSSRule):
    style: CSSStyleDeclaration

class CSSFontFeatureValuesRule(CSSRule):
    fontFamily: CSSOMString
    annotation: CSSFontFeatureValuesMap
    ornaments: CSSFontFeatureValuesMap
    stylistic: CSSFontFeatureValuesMap
    swash: CSSFontFeatureValuesMap
    characterVariant: CSSFontFeatureValuesMap
    styleset: CSSFontFeatureValuesMap

class CSSFontFeatureValuesMap:
    def set(self, featureValueName: CSSOMString, values: int | Sequence[int]): ...

class CSSFontPaletteValuesRule(CSSRule):
    name: CSSOMString
    fontFamily: CSSOMString
    basePalette: CSSOMString
    overrideColors: CSSOMString

class Event:
    def New(self, type: str, eventInitDict: EventInit | None = {}) -> Event: ...
    type: str
    target: EventTarget | None
    srcElement: EventTarget | None
    currentTarget: EventTarget | None
    def composedPath(self) -> Sequence[EventTarget]: ...
    eventPhase: int
    def stopPropagation(self): ...
    cancelBubble: bool
    def stopImmediatePropagation(self): ...
    bubbles: bool
    cancelable: bool
    returnValue: bool
    def preventDefault(self): ...
    defaultPrevented: bool
    composed: bool
    isTrusted: bool
    timeStamp: DOMHighResTimeStamp
    def initEvent(self, type: str, bubbles: bool | None = false, cancelable: bool | None = false): ...

class CustomEvent(Event):
    def New(self, type: str, eventInitDict: CustomEventInit | None = {}) -> CustomEvent: ...

class EventTarget:
    def New(self) -> EventTarget: ...
    def addEventListener(self, type: str, callback: EventListener | None, options: AddEventListenerOptions | bool | None = {}): ...
    def removeEventListener(self, type: str, callback: EventListener | None, options: EventListenerOptions | bool | None = {}): ...
    def dispatchEvent(self, event: Event) -> bool: ...

class AbortController:
    def New(self) -> AbortController: ...
    signal: AbortSignal

class AbortSignal(EventTarget):
    aborted: bool
    def throwIfAborted(self): ...
    onabort: EventHandler

class NonElementParentNode:
    def getElementById(self, elementId: str) -> Element | None: ...

class DocumentFragment(Node, NonElementParentNode, ParentNode):
    def New(self) -> DocumentFragment: ...

class ShadowRoot(DocumentFragment, DocumentOrShadowRoot, InnerHTML):
    mode: ShadowRootMode
    delegatesFocus: bool
    slotAssignment: SlotAssignmentMode
    host: Element
    onslotchange: EventHandler

class ParentNode:
    children: HTMLCollection
    firstElementChild: Element | None
    lastElementChild: Element | None
    childElementCount: int
    def prepend(self, nodes: Node | str | None = None): ...
    def append(self, nodes: Node | str | None = None): ...
    def replaceChildren(self, nodes: Node | str | None = None): ...
    def querySelector(self, selectors: str) -> Element | None: ...
    def querySelectorAll(self, selectors: str) -> NodeList: ...

class NonDocumentTypeChildNode:
    previousElementSibling: Element | None
    nextElementSibling: Element | None

class CharacterData(Node, NonDocumentTypeChildNode, ChildNode):
    data: str
    length: int
    def substringData(self, offset: int, count: int) -> str: ...
    def appendData(self, data: str): ...
    def insertData(self, offset: int, data: str): ...
    def deleteData(self, offset: int, count: int): ...
    def replaceData(self, offset: int, count: int, data: str): ...

class ChildNode:
    def before(self, nodes: Node | str | None = None): ...
    def after(self, nodes: Node | str | None = None): ...
    def replaceWith(self, nodes: Node | str | None = None): ...
    def remove(self): ...

class DocumentType(Node, ChildNode):
    name: str
    publicId: str
    systemId: str

class Slottable:
    assignedSlot: HTMLSlotElement | None

class NodeList:
    length: int

class HTMLCollection:
    length: int

class MutationObserver:
    def New(self, callback: MutationCallback) -> MutationObserver: ...
    def observe(self, target: Node, options: MutationObserverInit | None = {}): ...
    def disconnect(self): ...
    def takeRecords(self) -> Sequence[MutationRecord]: ...

class MutationRecord:
    type: str
    target: Node
    addedNodes: NodeList
    removedNodes: NodeList
    previousSibling: Node | None
    nextSibling: Node | None
    attributeName: str | None
    attributeNamespace: str | None
    oldValue: str | None

class Node(EventTarget):
    nodeType: int
    nodeName: str
    baseURI: USVString
    isConnected: bool
    ownerDocument: Document | None
    def getRootNode(self, options: GetRootNodeOptions | None = {}) -> Node: ...
    parentNode: Node | None
    parentElement: Element | None
    def hasChildNodes(self) -> bool: ...
    childNodes: NodeList
    firstChild: Node | None
    lastChild: Node | None
    previousSibling: Node | None
    nextSibling: Node | None
    nodeValue: str | None
    textContent: str | None
    def normalize(self): ...
    def cloneNode(self, deep: bool | None = false) -> Node: ...
    def isEqualNode(self, otherNode: Node | None) -> bool: ...
    def isSameNode(self, otherNode: Node | None) -> bool: ...
    def compareDocumentPosition(self, other: Node) -> int: ...
    def contains(self, other: Node | None) -> bool: ...
    def lookupPrefix(self, namespace: str | None) -> str | None: ...
    def lookupNamespaceURI(self, prefix: str | None) -> str | None: ...
    def isDefaultNamespace(self, namespace: str | None) -> bool: ...
    def insertBefore(self, node: Node, child: Node | None) -> Node: ...
    def appendChild(self, node: Node) -> Node: ...
    def replaceChild(self, node: Node, child: Node) -> Node: ...
    def removeChild(self, child: Node) -> Node: ...

class XMLDocument(Document): ...

class DOMImplementation:
    def createDocumentType(self, qualifiedName: str, publicId: str, systemId: str) -> DocumentType: ...
    def createDocument(self, namespace: str | None, qualifiedName: str, doctype: DocumentType | None = None) -> XMLDocument: ...
    def createHTMLDocument(self, title: str | None = None) -> Document: ...
    def hasFeature(self) -> bool: ...

class NamedNodeMap:
    length: int
    def getNamedItemNS(self, namespace: str | None, localName: str) -> Attr | None: ...
    def setNamedItem(self, attr: Attr) -> Attr | None: ...
    def setNamedItemNS(self, attr: Attr) -> Attr | None: ...
    def removeNamedItem(self, qualifiedName: str) -> Attr: ...
    def removeNamedItemNS(self, namespace: str | None, localName: str) -> Attr: ...

class Attr(Node):
    namespaceURI: str | None
    prefix: str | None
    localName: str
    name: str
    value: str
    ownerElement: Element | None
    specified: bool

class CDATASection(Text): ...

class ProcessingInstruction(CharacterData, LinkStyle):
    target: str

class Comment(CharacterData):
    def New(self, data: str | None = "") -> Comment: ...

class AbstractRange:
    startContainer: Node
    startOffset: int
    endContainer: Node
    endOffset: int
    collapsed: bool

class StaticRange(AbstractRange):
    def New(self, init: StaticRangeInit) -> StaticRange: ...

class NodeIterator:
    root: Node
    referenceNode: Node
    pointerBeforeReferenceNode: bool
    whatToShow: int
    filter: NodeFilter | None
    def nextNode(self) -> Node | None: ...
    def previousNode(self) -> Node | None: ...
    def detach(self): ...

class TreeWalker:
    root: Node
    whatToShow: int
    filter: NodeFilter | None
    currentNode: Node
    def parentNode(self) -> Node | None: ...
    def firstChild(self) -> Node | None: ...
    def lastChild(self) -> Node | None: ...
    def previousSibling(self) -> Node | None: ...
    def nextSibling(self) -> Node | None: ...
    def previousNode(self) -> Node | None: ...
    def nextNode(self) -> Node | None: ...

class DOMTokenList:
    length: int
    def contains(self, token: str) -> bool: ...
    def add(self, tokens: str | None = None): ...
    def remove(self, tokens: str | None = None): ...
    def toggle(self, token: str, force: bool | None = None) -> bool: ...
    def replace(self, token: str, newToken: str) -> bool: ...
    def supports(self, token: str) -> bool: ...

class XPathResult:
    resultType: int
    numberValue: float
    stringValue: str
    booleanValue: bool
    singleNodeValue: Node | None
    invalidIteratorState: bool
    snapshotLength: int
    def iterateNext(self) -> Node | None: ...
    def snapshotItem(self, index: int) -> Node | None: ...

class XPathExpression:
    def evaluate(self, contextNode: Node, type: int | None = 0, result: XPathResult | None = None) -> XPathResult: ...

class XPathEvaluatorBase:
    def createExpression(self, expression: str, resolver: XPathNSResolver | None = None) -> XPathExpression: ...
    def createNSResolver(self, nodeResolver: Node) -> XPathNSResolver: ...
    def evaluate(self, expression: str, contextNode: Node, resolver: XPathNSResolver | None = None, type: int | None = 0, result: XPathResult | None = None) -> XPathResult: ...

class XPathEvaluator(XPathEvaluatorBase):
    def New(self) -> XPathEvaluator: ...

class XSLTProcessor:
    def New(self) -> XSLTProcessor: ...
    def importStylesheet(self, style: Node): ...
    def transformToFragment(self, source: Node, output: Document) -> DocumentFragment: ...
    def transformToDocument(self, source: Node) -> Document: ...
    def removeParameter(self, namespaceURI: str, localName: str): ...
    def clearParameters(self): ...
    def reset(self): ...

class HTMLLinkElement(HTMLElement, LinkStyle):
    def New(self) -> HTMLLinkElement: ...
    fetchPriority: str
    href: USVString
    crossOrigin: str | None
    rel: str
    relList: DOMTokenList
    media: str
    integrity: str
    hreflang: str
    type: str
    sizes: DOMTokenList
    imageSrcset: USVString
    imageSizes: str
    referrerPolicy: str
    blocking: DOMTokenList
    disabled: bool
    charset: str
    rev: str
    target: str

class IDBRequest(EventTarget):
    error: DOMException | None
    source: IDBObjectStore | IDBIndex | IDBCursor | None
    transaction: IDBTransaction | None
    readyState: IDBRequestReadyState
    onsuccess: EventHandler
    onerror: EventHandler

class IDBOpenDBRequest(IDBRequest):
    onblocked: EventHandler
    onupgradeneeded: EventHandler

class IDBVersionChangeEvent(Event):
    def New(self, type: str, eventInitDict: IDBVersionChangeEventInit | None = {}) -> IDBVersionChangeEvent: ...
    oldVersion: int
    newVersion: int | None

class IDBFactory:
    def open(self, name: str, version: int | None = None) -> IDBOpenDBRequest: ...
    def deleteDatabase(self, name: str) -> IDBOpenDBRequest: ...
    def databases(self) -> Awaitable[Sequence[IDBDatabaseInfo]]: ...

class IDBDatabase(EventTarget):
    name: str
    version: int
    objectStoreNames: DOMStringList
    def transaction(self, storeNames: str | Sequence[str], mode: IDBTransactionMode | None = "readonly", options: IDBTransactionOptions | None = {}) -> IDBTransaction: ...
    def close(self): ...
    def createObjectStore(self, name: str, options: IDBObjectStoreParameters | None = {}) -> IDBObjectStore: ...
    def deleteObjectStore(self, name: str): ...
    onabort: EventHandler
    onclose: EventHandler
    onerror: EventHandler
    onversionchange: EventHandler

class IDBObjectStore:
    name: str
    indexNames: DOMStringList
    transaction: IDBTransaction
    autoIncrement: bool
    def clear(self) -> IDBRequest: ...
    def index(self, name: str) -> IDBIndex: ...
    def createIndex(self, name: str, keyPath: str | Sequence[str], options: IDBIndexParameters | None = {}) -> IDBIndex: ...
    def deleteIndex(self, name: str): ...

class IDBIndex:
    name: str
    objectStore: IDBObjectStore
    multiEntry: bool
    unique: bool

class IDBKeyRange:
    lowerOpen: bool
    upperOpen: bool

class IDBCursor:
    source: IDBObjectStore | IDBIndex
    direction: IDBCursorDirection
    request: IDBRequest
    def advance(self, count: int): ...
    def delete(self) -> IDBRequest: ...

class IDBCursorWithValue(IDBCursor): ...

class IDBTransaction(EventTarget):
    objectStoreNames: DOMStringList
    mode: IDBTransactionMode
    durability: IDBTransactionDurability
    db: IDBDatabase
    error: DOMException | None
    def objectStore(self, name: str) -> IDBObjectStore: ...
    def commit(self): ...
    def abort(self): ...
    onabort: EventHandler
    oncomplete: EventHandler
    onerror: EventHandler

class PerformanceEventTiming(PerformanceEntry):
    processingStart: DOMHighResTimeStamp
    processingEnd: DOMHighResTimeStamp
    cancelable: bool
    target: Node | None
    interactionId: int
    def toJSON(self) -> object: ...

class EventCounts: ...

class WEBGL_debug_renderer_info: ...

class VideoPlaybackQuality:
    creationTime: DOMHighResTimeStamp
    droppedVideoFrames: int
    totalVideoFrames: int
    corruptedVideoFrames: int

class NavigatorStorage:
    storage: StorageManager

class StorageManager:
    def persisted(self) -> Awaitable[bool]: ...
    def persist(self) -> Awaitable[bool]: ...
    def estimate(self) -> Awaitable[StorageEstimate]: ...
    def getDirectory(self) -> Awaitable[FileSystemDirectoryHandle]: ...

class WebSocket(EventTarget):
    def New(self, url: USVString, protocols: str | Sequence[str] | None = []) -> WebSocket: ...
    url: USVString
    readyState: int
    bufferedAmount: int
    onopen: EventHandler
    onerror: EventHandler
    onclose: EventHandler
    extensions: str
    protocol: str
    def close(self, code: int | None = None, reason: USVString | None = None): ...
    onmessage: EventHandler
    binaryType: BinaryType
    def send(self, data: BufferSource | Blob | USVString): ...

class CloseEvent(Event):
    def New(self, type: str, eventInitDict: CloseEventInit | None = {}) -> CloseEvent: ...
    wasClean: bool
    code: int
    reason: USVString

class WebGLTimerQueryEXT(WebGLObject): ...

class EXT_disjoint_timer_query:
    def createQueryEXT(self) -> WebGLTimerQueryEXT | None: ...
    def deleteQueryEXT(self, query: WebGLTimerQueryEXT | None): ...
    def isQueryEXT(self, query: WebGLTimerQueryEXT | None) -> bool: ...
    def beginQueryEXT(self, target: GLenum, query: WebGLTimerQueryEXT): ...
    def endQueryEXT(self, target: GLenum): ...
    def queryCounterEXT(self, query: WebGLTimerQueryEXT, target: GLenum): ...

class CSSTransition(Animation):
    transitionProperty: CSSOMString

class EXT_sRGB: ...

class EXT_float_blend: ...

class ElementInternals(ARIAMixin):
    states: CustomStateSet
    shadowRoot: ShadowRoot | None
    def setFormValue(self, value: File | USVString | FormData | None, state: File | USVString | FormData | None = None): ...
    form: HTMLFormElement | None
    def setValidity(self, flags: ValidityStateFlags | None = {}, message: str | None = None, anchor: HTMLElement | None = None): ...
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    labels: NodeList

class CustomStateSet:
    def add(self, value: str): ...

class KHR_parallel_shader_compile: ...

class TransitionEvent(Event):
    def New(self, type: CSSOMString, transitionEventInitDict: TransitionEventInit | None = {}) -> TransitionEvent: ...
    propertyName: CSSOMString
    elapsedTime: float
    pseudoElement: CSSOMString

class WebGLObject: ...

class WebGLBuffer(WebGLObject): ...

class WebGLFramebuffer(WebGLObject): ...

class WebGLProgram(WebGLObject): ...

class WebGLRenderbuffer(WebGLObject): ...

class WebGLShader(WebGLObject): ...

class WebGLTexture(WebGLObject): ...

class WebGLUniformLocation: ...

class WebGLActiveInfo:
    size: GLint
    type: GLenum
    name: str

class WebGLShaderPrecisionFormat:
    rangeMin: GLint
    rangeMax: GLint
    precision: GLint

class WebGLRenderingContextBase:
    canvas: HTMLCanvasElement | OffscreenCanvas
    drawingBufferWidth: GLsizei
    drawingBufferHeight: GLsizei
    drawingBufferColorSpace: PredefinedColorSpace
    unpackColorSpace: PredefinedColorSpace
    def getContextAttributes(self) -> WebGLContextAttributes | None: ...
    def isContextLost(self) -> bool: ...
    def getSupportedExtensions(self) -> Sequence[str]: ...
    def getExtension(self, name: str) -> object | None: ...
    def activeTexture(self, texture: GLenum): ...
    def attachShader(self, program: WebGLProgram, shader: WebGLShader): ...
    def bindAttribLocation(self, program: WebGLProgram, index: GLuint, name: str): ...
    def bindBuffer(self, target: GLenum, buffer: WebGLBuffer | None): ...
    def bindFramebuffer(self, target: GLenum, framebuffer: WebGLFramebuffer | None): ...
    def bindRenderbuffer(self, target: GLenum, renderbuffer: WebGLRenderbuffer | None): ...
    def bindTexture(self, target: GLenum, texture: WebGLTexture | None): ...
    def blendColor(self, red: GLclampf, green: GLclampf, blue: GLclampf, alpha: GLclampf): ...
    def blendEquation(self, mode: GLenum): ...
    def blendEquationSeparate(self, modeRGB: GLenum, modeAlpha: GLenum): ...
    def blendFunc(self, sfactor: GLenum, dfactor: GLenum): ...
    def blendFuncSeparate(self, srcRGB: GLenum, dstRGB: GLenum, srcAlpha: GLenum, dstAlpha: GLenum): ...
    def checkFramebufferStatus(self, target: GLenum) -> GLenum: ...
    def clear(self, mask: GLbitfield): ...
    def clearColor(self, red: GLclampf, green: GLclampf, blue: GLclampf, alpha: GLclampf): ...
    def clearDepth(self, depth: GLclampf): ...
    def clearStencil(self, s: GLint): ...
    def colorMask(self, red: GLboolean, green: GLboolean, blue: GLboolean, alpha: GLboolean): ...
    def compileShader(self, shader: WebGLShader): ...
    def copyTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, x: GLint, y: GLint, width: GLsizei, height: GLsizei, border: GLint): ...
    def copyTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, x: GLint, y: GLint, width: GLsizei, height: GLsizei): ...
    def createBuffer(self) -> WebGLBuffer | None: ...
    def createFramebuffer(self) -> WebGLFramebuffer | None: ...
    def createProgram(self) -> WebGLProgram | None: ...
    def createRenderbuffer(self) -> WebGLRenderbuffer | None: ...
    def createShader(self, type: GLenum) -> WebGLShader | None: ...
    def createTexture(self) -> WebGLTexture | None: ...
    def cullFace(self, mode: GLenum): ...
    def deleteBuffer(self, buffer: WebGLBuffer | None): ...
    def deleteFramebuffer(self, framebuffer: WebGLFramebuffer | None): ...
    def deleteProgram(self, program: WebGLProgram | None): ...
    def deleteRenderbuffer(self, renderbuffer: WebGLRenderbuffer | None): ...
    def deleteShader(self, shader: WebGLShader | None): ...
    def deleteTexture(self, texture: WebGLTexture | None): ...
    def depthFunc(self, func: GLenum): ...
    def depthMask(self, flag: GLboolean): ...
    def depthRange(self, zNear: GLclampf, zFar: GLclampf): ...
    def detachShader(self, program: WebGLProgram, shader: WebGLShader): ...
    def disable(self, cap: GLenum): ...
    def disableVertexAttribArray(self, index: GLuint): ...
    def drawArrays(self, mode: GLenum, first: GLint, count: GLsizei): ...
    def drawElements(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr): ...
    def enable(self, cap: GLenum): ...
    def enableVertexAttribArray(self, index: GLuint): ...
    def finish(self): ...
    def flush(self): ...
    def framebufferRenderbuffer(self, target: GLenum, attachment: GLenum, renderbuffertarget: GLenum, renderbuffer: WebGLRenderbuffer | None): ...
    def framebufferTexture2D(self, target: GLenum, attachment: GLenum, textarget: GLenum, texture: WebGLTexture | None, level: GLint): ...
    def frontFace(self, mode: GLenum): ...
    def generateMipmap(self, target: GLenum): ...
    def getActiveAttrib(self, program: WebGLProgram, index: GLuint) -> WebGLActiveInfo | None: ...
    def getActiveUniform(self, program: WebGLProgram, index: GLuint) -> WebGLActiveInfo | None: ...
    def getAttachedShaders(self, program: WebGLProgram) -> Sequence[WebGLShader]: ...
    def getAttribLocation(self, program: WebGLProgram, name: str) -> GLint: ...
    def getError(self) -> GLenum: ...
    def getProgramInfoLog(self, program: WebGLProgram) -> str | None: ...
    def getShaderPrecisionFormat(self, shadertype: GLenum, precisiontype: GLenum) -> WebGLShaderPrecisionFormat | None: ...
    def getShaderInfoLog(self, shader: WebGLShader) -> str | None: ...
    def getShaderSource(self, shader: WebGLShader) -> str | None: ...
    def getUniformLocation(self, program: WebGLProgram, name: str) -> WebGLUniformLocation | None: ...
    def getVertexAttribOffset(self, index: GLuint, pname: GLenum) -> GLintptr: ...
    def hint(self, target: GLenum, mode: GLenum): ...
    def isBuffer(self, buffer: WebGLBuffer | None) -> GLboolean: ...
    def isEnabled(self, cap: GLenum) -> GLboolean: ...
    def isFramebuffer(self, framebuffer: WebGLFramebuffer | None) -> GLboolean: ...
    def isProgram(self, program: WebGLProgram | None) -> GLboolean: ...
    def isRenderbuffer(self, renderbuffer: WebGLRenderbuffer | None) -> GLboolean: ...
    def isShader(self, shader: WebGLShader | None) -> GLboolean: ...
    def isTexture(self, texture: WebGLTexture | None) -> GLboolean: ...
    def lineWidth(self, width: GLfloat): ...
    def linkProgram(self, program: WebGLProgram): ...
    def pixelStorei(self, pname: GLenum, param: GLint): ...
    def polygonOffset(self, factor: GLfloat, units: GLfloat): ...
    def renderbufferStorage(self, target: GLenum, internalformat: GLenum, width: GLsizei, height: GLsizei): ...
    def sampleCoverage(self, value: GLclampf, invert: GLboolean): ...
    def scissor(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei): ...
    def shaderSource(self, shader: WebGLShader, source: str): ...
    def stencilFunc(self, func: GLenum, ref: GLint, mask: GLuint): ...
    def stencilFuncSeparate(self, face: GLenum, func: GLenum, ref: GLint, mask: GLuint): ...
    def stencilMask(self, mask: GLuint): ...
    def stencilMaskSeparate(self, face: GLenum, mask: GLuint): ...
    def stencilOp(self, fail: GLenum, zfail: GLenum, zpass: GLenum): ...
    def stencilOpSeparate(self, face: GLenum, fail: GLenum, zfail: GLenum, zpass: GLenum): ...
    def texParameterf(self, target: GLenum, pname: GLenum, param: GLfloat): ...
    def texParameteri(self, target: GLenum, pname: GLenum, param: GLint): ...
    def uniform1f(self, location: WebGLUniformLocation | None, x: GLfloat): ...
    def uniform2f(self, location: WebGLUniformLocation | None, x: GLfloat, y: GLfloat): ...
    def uniform3f(self, location: WebGLUniformLocation | None, x: GLfloat, y: GLfloat, z: GLfloat): ...
    def uniform4f(self, location: WebGLUniformLocation | None, x: GLfloat, y: GLfloat, z: GLfloat, w: GLfloat): ...
    def uniform1i(self, location: WebGLUniformLocation | None, x: GLint): ...
    def uniform2i(self, location: WebGLUniformLocation | None, x: GLint, y: GLint): ...
    def uniform3i(self, location: WebGLUniformLocation | None, x: GLint, y: GLint, z: GLint): ...
    def uniform4i(self, location: WebGLUniformLocation | None, x: GLint, y: GLint, z: GLint, w: GLint): ...
    def useProgram(self, program: WebGLProgram | None): ...
    def validateProgram(self, program: WebGLProgram): ...
    def vertexAttrib1f(self, index: GLuint, x: GLfloat): ...
    def vertexAttrib2f(self, index: GLuint, x: GLfloat, y: GLfloat): ...
    def vertexAttrib3f(self, index: GLuint, x: GLfloat, y: GLfloat, z: GLfloat): ...
    def vertexAttrib4f(self, index: GLuint, x: GLfloat, y: GLfloat, z: GLfloat, w: GLfloat): ...
    def vertexAttrib1fv(self, index: GLuint, values: Float32List): ...
    def vertexAttrib2fv(self, index: GLuint, values: Float32List): ...
    def vertexAttrib3fv(self, index: GLuint, values: Float32List): ...
    def vertexAttrib4fv(self, index: GLuint, values: Float32List): ...
    def vertexAttribPointer(self, index: GLuint, size: GLint, type: GLenum, normalized: GLboolean, stride: GLsizei, offset: GLintptr): ...
    def viewport(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei): ...
    def makeXRCompatible(self) -> Awaitable[None]: ...

class WebGLRenderingContextOverloads:
    @overload
    def bufferData(self, target: GLenum, size: GLsizeiptr, usage: GLenum): ...
    @overload
    def bufferData(self, target: GLenum, data: BufferSource | None, usage: GLenum): ...
    def bufferSubData(self, target: GLenum, offset: GLintptr, data: BufferSource): ...
    def compressedTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, border: GLint, data: ArrayBufferView): ...
    def compressedTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, data: ArrayBufferView): ...
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    def uniform1fv(self, location: WebGLUniformLocation | None, v: Float32List): ...
    def uniform2fv(self, location: WebGLUniformLocation | None, v: Float32List): ...
    def uniform3fv(self, location: WebGLUniformLocation | None, v: Float32List): ...
    def uniform4fv(self, location: WebGLUniformLocation | None, v: Float32List): ...
    def uniform1iv(self, location: WebGLUniformLocation | None, v: Int32List): ...
    def uniform2iv(self, location: WebGLUniformLocation | None, v: Int32List): ...
    def uniform3iv(self, location: WebGLUniformLocation | None, v: Int32List): ...
    def uniform4iv(self, location: WebGLUniformLocation | None, v: Int32List): ...
    def uniformMatrix2fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, value: Float32List): ...
    def uniformMatrix3fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, value: Float32List): ...
    def uniformMatrix4fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, value: Float32List): ...

class WebGLRenderingContext(WebGLRenderingContextBase, WebGLRenderingContextOverloads): ...

class WebGLContextEvent(Event):
    def New(self, type: str, eventInit: WebGLContextEventInit | None = {}) -> WebGLContextEvent: ...
    statusMessage: str

class HTMLAllCollection:
    length: int
    def item(self, nameOrIndex: str | None = None) -> HTMLCollection | Element | None: ...

class HTMLFormControlsCollection(HTMLCollection): ...

class RadioNodeList(NodeList):
    value: str

class HTMLOptionsCollection(HTMLCollection):
    length: int
    def add(self, element: HTMLOptionElement | HTMLOptGroupElement, before: HTMLElement | int | None = None): ...
    def remove(self, index: int): ...
    selectedIndex: int

class DOMStringList:
    length: int
    def contains(self, string: str) -> bool: ...

class HTMLUnknownElement(HTMLElement): ...

class HTMLOrSVGElement:
    dataset: DOMStringMap
    nonce: str
    autofocus: bool
    tabIndex: int
    def focus(self, options: FocusOptions | None = {}): ...
    def blur(self): ...

class DOMStringMap: ...

class HTMLHtmlElement(HTMLElement):
    def New(self) -> HTMLHtmlElement: ...
    version: str

class HTMLHeadElement(HTMLElement):
    def New(self) -> HTMLHeadElement: ...

class HTMLTitleElement(HTMLElement):
    def New(self) -> HTMLTitleElement: ...
    text: str

class HTMLBaseElement(HTMLElement):
    def New(self) -> HTMLBaseElement: ...
    href: USVString
    target: str

class HTMLMetaElement(HTMLElement):
    def New(self) -> HTMLMetaElement: ...
    name: str
    httpEquiv: str
    content: str
    media: str
    scheme: str

class HTMLStyleElement(HTMLElement, LinkStyle):
    def New(self) -> HTMLStyleElement: ...
    disabled: bool
    media: str
    blocking: DOMTokenList
    type: str

class HTMLBodyElement(HTMLElement, WindowEventHandlers):
    def New(self) -> HTMLBodyElement: ...
    text: str
    link: str
    vLink: str
    aLink: str
    bgColor: str
    background: str
    onorientationchange: EventHandler

class HTMLHeadingElement(HTMLElement):
    def New(self) -> HTMLHeadingElement: ...
    align: str

class HTMLParagraphElement(HTMLElement):
    def New(self) -> HTMLParagraphElement: ...
    align: str

class HTMLHRElement(HTMLElement):
    def New(self) -> HTMLHRElement: ...
    align: str
    color: str
    noShade: bool
    size: str
    width: str

class HTMLPreElement(HTMLElement):
    def New(self) -> HTMLPreElement: ...
    width: int

class HTMLQuoteElement(HTMLElement):
    def New(self) -> HTMLQuoteElement: ...
    cite: USVString

class HTMLOListElement(HTMLElement):
    def New(self) -> HTMLOListElement: ...
    reversed: bool
    start: int
    type: str
    compact: bool

class HTMLUListElement(HTMLElement):
    def New(self) -> HTMLUListElement: ...
    compact: bool
    type: str

class HTMLMenuElement(HTMLElement):
    def New(self) -> HTMLMenuElement: ...
    compact: bool

class HTMLLIElement(HTMLElement):
    def New(self) -> HTMLLIElement: ...
    value: int
    type: str

class HTMLDListElement(HTMLElement):
    def New(self) -> HTMLDListElement: ...
    compact: bool

class HTMLDivElement(HTMLElement):
    def New(self) -> HTMLDivElement: ...
    align: str

class HTMLDataElement(HTMLElement):
    def New(self) -> HTMLDataElement: ...
    value: str

class HTMLTimeElement(HTMLElement):
    def New(self) -> HTMLTimeElement: ...
    dateTime: str

class HTMLSpanElement(HTMLElement):
    def New(self) -> HTMLSpanElement: ...

class HTMLBRElement(HTMLElement):
    def New(self) -> HTMLBRElement: ...
    clear: str

class HTMLHyperlinkElementUtils:
    origin: USVString
    protocol: USVString
    username: USVString
    password: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString

class HTMLModElement(HTMLElement):
    def New(self) -> HTMLModElement: ...
    cite: USVString
    dateTime: str

class HTMLPictureElement(HTMLElement):
    def New(self) -> HTMLPictureElement: ...

class HTMLSourceElement(HTMLElement):
    def New(self) -> HTMLSourceElement: ...
    src: USVString
    type: str
    srcset: USVString
    sizes: str
    media: str
    width: int
    height: int

class HTMLEmbedElement(HTMLElement):
    def New(self) -> HTMLEmbedElement: ...
    src: USVString
    type: str
    width: str
    height: str
    def getSVGDocument(self) -> Document | None: ...
    align: str
    name: str

class HTMLObjectElement(HTMLElement):
    def New(self) -> HTMLObjectElement: ...
    data: USVString
    type: str
    name: str
    form: HTMLFormElement | None
    width: str
    height: str
    contentDocument: Document | None
    contentWindow: WindowProxy | None
    def getSVGDocument(self) -> Document | None: ...
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    align: str
    archive: str
    code: str
    declare: bool
    hspace: int
    standby: str
    vspace: int
    codeBase: str
    codeType: str
    useMap: str
    border: str

class HTMLAudioElement(HTMLMediaElement):
    def New(self) -> HTMLAudioElement: ...
    """ # GIgnoredStmt 
    LegacyFactoryFunction=Audio(optional DOMString src)
    """

class HTMLTrackElement(HTMLElement):
    def New(self) -> HTMLTrackElement: ...
    kind: str
    src: USVString
    srclang: str
    label: str
    default: bool
    readyState: int
    track: TextTrack

class MediaError:
    code: int
    message: str

class AudioTrackList(EventTarget):
    length: int
    def getTrackById(self, id: str) -> AudioTrack | None: ...
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class AudioTrack:
    id: str
    kind: str
    label: str
    language: str
    enabled: bool
    sourceBuffer: SourceBuffer | None

class VideoTrackList(EventTarget):
    length: int
    def getTrackById(self, id: str) -> VideoTrack | None: ...
    selectedIndex: int
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class VideoTrack:
    id: str
    kind: str
    label: str
    language: str
    selected: bool
    sourceBuffer: SourceBuffer | None

class TextTrackList(EventTarget):
    length: int
    def getTrackById(self, id: str) -> TextTrack | None: ...
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class TextTrack(EventTarget):
    kind: TextTrackKind
    label: str
    language: str
    id: str
    inBandMetadataTrackDispatchType: str
    mode: TextTrackMode
    cues: TextTrackCueList | None
    activeCues: TextTrackCueList | None
    def addCue(self, cue: TextTrackCue): ...
    def removeCue(self, cue: TextTrackCue): ...
    oncuechange: EventHandler
    sourceBuffer: SourceBuffer | None

class TextTrackCueList:
    length: int
    def getCueById(self, id: str) -> TextTrackCue | None: ...

class TextTrackCue(EventTarget):
    track: TextTrack | None
    id: str
    startTime: float
    endTime: float
    pauseOnExit: bool
    onenter: EventHandler
    onexit: EventHandler

class TimeRanges:
    length: int
    def start(self, index: int) -> float: ...
    def end(self, index: int) -> float: ...

class TrackEvent(Event):
    def New(self, type: str, eventInitDict: TrackEventInit | None = {}) -> TrackEvent: ...
    track: VideoTrack | AudioTrack | TextTrack | None

class HTMLMapElement(HTMLElement):
    def New(self) -> HTMLMapElement: ...
    name: str
    areas: HTMLCollection

class HTMLAreaElement(HTMLElement, HTMLHyperlinkElementUtils):
    def New(self) -> HTMLAreaElement: ...
    alt: str
    coords: str
    shape: str
    target: str
    download: str
    ping: USVString
    rel: str
    relList: DOMTokenList
    referrerPolicy: str
    noHref: bool

class HTMLTableElement(HTMLElement):
    def New(self) -> HTMLTableElement: ...
    caption: HTMLTableCaptionElement | None
    def createCaption(self) -> HTMLTableCaptionElement: ...
    def deleteCaption(self): ...
    tHead: HTMLTableSectionElement | None
    def createTHead(self) -> HTMLTableSectionElement: ...
    def deleteTHead(self): ...
    tFoot: HTMLTableSectionElement | None
    def createTFoot(self) -> HTMLTableSectionElement: ...
    def deleteTFoot(self): ...
    tBodies: HTMLCollection
    def createTBody(self) -> HTMLTableSectionElement: ...
    rows: HTMLCollection
    def insertRow(self, index: int | None = -1) -> HTMLTableRowElement: ...
    def deleteRow(self, index: int): ...
    align: str
    border: str
    frame: str
    rules: str
    summary: str
    width: str
    bgColor: str
    cellPadding: str
    cellSpacing: str

class HTMLTableCaptionElement(HTMLElement):
    def New(self) -> HTMLTableCaptionElement: ...
    align: str

class HTMLTableColElement(HTMLElement):
    def New(self) -> HTMLTableColElement: ...
    span: int
    align: str
    ch: str
    chOff: str
    vAlign: str
    width: str

class HTMLTableSectionElement(HTMLElement):
    def New(self) -> HTMLTableSectionElement: ...
    rows: HTMLCollection
    def insertRow(self, index: int | None = -1) -> HTMLTableRowElement: ...
    def deleteRow(self, index: int): ...
    align: str
    ch: str
    chOff: str
    vAlign: str

class HTMLTableRowElement(HTMLElement):
    def New(self) -> HTMLTableRowElement: ...
    rowIndex: int
    sectionRowIndex: int
    cells: HTMLCollection
    def insertCell(self, index: int | None = -1) -> HTMLTableCellElement: ...
    def deleteCell(self, index: int): ...
    align: str
    ch: str
    chOff: str
    vAlign: str
    bgColor: str

class HTMLTableCellElement(HTMLElement):
    def New(self) -> HTMLTableCellElement: ...
    colSpan: int
    rowSpan: int
    headers: str
    cellIndex: int
    scope: str
    abbr: str
    align: str
    axis: str
    height: str
    width: str
    ch: str
    chOff: str
    noWrap: bool
    vAlign: str
    bgColor: str

class HTMLFormElement(HTMLElement):
    def New(self) -> HTMLFormElement: ...
    acceptCharset: str
    action: USVString
    autocomplete: str
    enctype: str
    encoding: str
    method: str
    name: str
    noValidate: bool
    target: str
    rel: str
    relList: DOMTokenList
    elements: HTMLFormControlsCollection
    length: int
    def submit(self): ...
    def requestSubmit(self, submitter: HTMLElement | None = None): ...
    def reset(self): ...
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...

class HTMLLabelElement(HTMLElement):
    def New(self) -> HTMLLabelElement: ...
    form: HTMLFormElement | None
    htmlFor: str
    control: HTMLElement | None

class HTMLButtonElement(HTMLElement):
    def New(self) -> HTMLButtonElement: ...
    disabled: bool
    form: HTMLFormElement | None
    formAction: USVString
    formEnctype: str
    formMethod: str
    formNoValidate: bool
    formTarget: str
    name: str
    type: str
    value: str
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    labels: NodeList

class HTMLSelectElement(HTMLElement):
    def New(self) -> HTMLSelectElement: ...
    autocomplete: str
    disabled: bool
    form: HTMLFormElement | None
    multiple: bool
    name: str
    required: bool
    size: int
    type: str
    options: HTMLOptionsCollection
    length: int
    def namedItem(self, name: str) -> HTMLOptionElement | None: ...
    def add(self, element: HTMLOptionElement | HTMLOptGroupElement, before: HTMLElement | int | None = None): ...
    @overload
    def remove(self): ...
    @overload
    def remove(self, index: int): ...
    selectedOptions: HTMLCollection
    selectedIndex: int
    value: str
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    labels: NodeList

class HTMLDataListElement(HTMLElement):
    def New(self) -> HTMLDataListElement: ...
    options: HTMLCollection

class HTMLOptGroupElement(HTMLElement):
    def New(self) -> HTMLOptGroupElement: ...
    disabled: bool
    label: str

class HTMLOptionElement(HTMLElement):
    def New(self) -> HTMLOptionElement: ...
    """ # GIgnoredStmt 
    LegacyFactoryFunction=Option(optional DOMString text = "", optional DOMString value, optional boolean defaultSelected = false, optional boolean selected = false)
    """
    disabled: bool
    form: HTMLFormElement | None
    label: str
    defaultSelected: bool
    selected: bool
    value: str
    text: str
    index: int

class HTMLTextAreaElement(HTMLElement):
    def New(self) -> HTMLTextAreaElement: ...
    autocomplete: str
    cols: int
    dirName: str
    disabled: bool
    form: HTMLFormElement | None
    maxLength: int
    minLength: int
    name: str
    placeholder: str
    readOnly: bool
    required: bool
    rows: int
    wrap: str
    type: str
    defaultValue: str
    value: str
    textLength: int
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    labels: NodeList
    def select(self): ...
    selectionStart: int
    selectionEnd: int
    selectionDirection: str
    @overload
    def setRangeText(self, replacement: str): ...
    @overload
    def setRangeText(self, replacement: str, start: int, end: int, selectionMode: SelectionMode | None = "preserve"): ...
    def setSelectionRange(self, start: int, end: int, direction: str | None = None): ...

class HTMLOutputElement(HTMLElement):
    def New(self) -> HTMLOutputElement: ...
    htmlFor: DOMTokenList
    form: HTMLFormElement | None
    name: str
    type: str
    defaultValue: str
    value: str
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...
    labels: NodeList

class HTMLProgressElement(HTMLElement):
    def New(self) -> HTMLProgressElement: ...
    value: float
    max: float
    position: float
    labels: NodeList

class HTMLMeterElement(HTMLElement):
    def New(self) -> HTMLMeterElement: ...
    value: float
    min: float
    max: float
    low: float
    high: float
    optimum: float
    labels: NodeList

class HTMLFieldSetElement(HTMLElement):
    def New(self) -> HTMLFieldSetElement: ...
    disabled: bool
    form: HTMLFormElement | None
    name: str
    type: str
    elements: HTMLCollection
    willValidate: bool
    validity: ValidityState
    validationMessage: str
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...
    def setCustomValidity(self, error: str): ...

class HTMLLegendElement(HTMLElement):
    def New(self) -> HTMLLegendElement: ...
    form: HTMLFormElement | None
    align: str

class ValidityState:
    valueMissing: bool
    typeMismatch: bool
    patternMismatch: bool
    tooLong: bool
    tooShort: bool
    rangeUnderflow: bool
    rangeOverflow: bool
    stepMismatch: bool
    badInput: bool
    customError: bool
    valid: bool

class SubmitEvent(Event):
    def New(self, type: str, eventInitDict: SubmitEventInit | None = {}) -> SubmitEvent: ...
    submitter: HTMLElement | None

class FormDataEvent(Event):
    def New(self, type: str, eventInitDict: FormDataEventInit) -> FormDataEvent: ...
    formData: FormData

class HTMLDetailsElement(HTMLElement):
    def New(self) -> HTMLDetailsElement: ...
    open: bool

class HTMLDialogElement(HTMLElement):
    def New(self) -> HTMLDialogElement: ...
    open: bool
    returnValue: str
    def show(self): ...
    def showModal(self): ...
    def close(self, returnValue: str | None = None): ...

class HTMLTemplateElement(HTMLElement):
    def New(self) -> HTMLTemplateElement: ...
    content: DocumentFragment

class HTMLSlotElement(HTMLElement):
    def New(self) -> HTMLSlotElement: ...
    name: str
    def assignedNodes(self, options: AssignedNodesOptions | None = {}) -> Sequence[Node]: ...
    def assignedElements(self, options: AssignedNodesOptions | None = {}) -> Sequence[Element]: ...
    def assign(self, nodes: Element | Text | None = None): ...

class CanvasRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing, CanvasImageSmoothing, CanvasFillStrokeStyles, CanvasShadowStyles, CanvasFilters, CanvasRect, CanvasDrawPath, CanvasUserInterface, CanvasText, CanvasDrawImage, CanvasImageData, CanvasPathDrawingStyles, CanvasTextDrawingStyles, CanvasPath):
    canvas: HTMLCanvasElement
    def getContextAttributes(self) -> CanvasRenderingContext2DSettings: ...

class CanvasState:
    def save(self): ...
    def restore(self): ...
    def reset(self): ...
    def isContextLost(self) -> bool: ...

class CanvasTransform:
    def scale(self, x: float, y: float): ...
    def rotate(self, angle: float): ...
    def translate(self, x: float, y: float): ...
    def transform(self, a: float, b: float, c: float, d: float, e: float, f: float): ...
    def getTransform(self) -> DOMMatrix: ...
    @overload
    def setTransform(self, a: float, b: float, c: float, d: float, e: float, f: float): ...
    @overload
    def setTransform(self, transform: DOMMatrix2DInit | None = {}): ...
    def resetTransform(self): ...

class CanvasCompositing:
    globalAlpha: float
    globalCompositeOperation: str

class CanvasImageSmoothing:
    imageSmoothingEnabled: bool
    imageSmoothingQuality: ImageSmoothingQuality

class CanvasFillStrokeStyles:
    strokeStyle: str | CanvasGradient | CanvasPattern
    fillStyle: str | CanvasGradient | CanvasPattern
    def createLinearGradient(self, x0: float, y0: float, x1: float, y1: float) -> CanvasGradient: ...
    def createRadialGradient(self, x0: float, y0: float, r0: float, x1: float, y1: float, r1: float) -> CanvasGradient: ...
    def createConicGradient(self, startAngle: float, x: float, y: float) -> CanvasGradient: ...
    def createPattern(self, image: CanvasImageSource, repetition: str) -> CanvasPattern | None: ...

class CanvasShadowStyles:
    shadowOffsetX: float
    shadowOffsetY: float
    shadowBlur: float
    shadowColor: str

class CanvasFilters:
    filter: str

class CanvasRect:
    def clearRect(self, x: float, y: float, w: float, h: float): ...
    def fillRect(self, x: float, y: float, w: float, h: float): ...
    def strokeRect(self, x: float, y: float, w: float, h: float): ...

class CanvasDrawPath:
    def beginPath(self): ...
    @overload
    def fill(self, fillRule: CanvasFillRule | None = "nonzero"): ...
    @overload
    def fill(self, path: Path2D, fillRule: CanvasFillRule | None = "nonzero"): ...
    @overload
    def stroke(self): ...
    @overload
    def stroke(self, path: Path2D): ...
    @overload
    def clip(self, fillRule: CanvasFillRule | None = "nonzero"): ...
    @overload
    def clip(self, path: Path2D, fillRule: CanvasFillRule | None = "nonzero"): ...
    @overload
    def isPointInPath(self, x: float, y: float, fillRule: CanvasFillRule | None = "nonzero") -> bool: ...
    @overload
    def isPointInPath(self, path: Path2D, x: float, y: float, fillRule: CanvasFillRule | None = "nonzero") -> bool: ...
    @overload
    def isPointInStroke(self, x: float, y: float) -> bool: ...
    @overload
    def isPointInStroke(self, path: Path2D, x: float, y: float) -> bool: ...

class CanvasUserInterface:
    @overload
    def drawFocusIfNeeded(self, element: Element): ...
    @overload
    def drawFocusIfNeeded(self, path: Path2D, element: Element): ...
    @overload
    def scrollPathIntoView(self): ...
    @overload
    def scrollPathIntoView(self, path: Path2D): ...

class CanvasText:
    def fillText(self, text: str, x: float, y: float, maxWidth: float | None = None): ...
    def strokeText(self, text: str, x: float, y: float, maxWidth: float | None = None): ...
    def measureText(self, text: str) -> TextMetrics: ...

class CanvasDrawImage:
    @overload
    def drawImage(self, image: CanvasImageSource, dx: float, dy: float): ...
    @overload
    def drawImage(self, image: CanvasImageSource, dx: float, dy: float, dw: float, dh: float): ...
    @overload
    def drawImage(self, image: CanvasImageSource, sx: float, sy: float, sw: float, sh: float, dx: float, dy: float, dw: float, dh: float): ...

class CanvasImageData:
    @overload
    def createImageData(self, sw: int, sh: int, settings: ImageDataSettings | None = {}) -> ImageData: ...
    @overload
    def createImageData(self, imagedata: ImageData) -> ImageData: ...
    def getImageData(self, sx: int, sy: int, sw: int, sh: int, settings: ImageDataSettings | None = {}) -> ImageData: ...
    @overload
    def putImageData(self, imagedata: ImageData, dx: int, dy: int): ...
    @overload
    def putImageData(self, imagedata: ImageData, dx: int, dy: int, dirtyX: int, dirtyY: int, dirtyWidth: int, dirtyHeight: int): ...

class CanvasPathDrawingStyles:
    lineWidth: float
    lineCap: CanvasLineCap
    lineJoin: CanvasLineJoin
    miterLimit: float
    def setLineDash(self, segments: Sequence[float]): ...
    def getLineDash(self) -> Sequence[float]: ...
    lineDashOffset: float

class CanvasTextDrawingStyles:
    font: str
    textAlign: CanvasTextAlign
    textBaseline: CanvasTextBaseline
    direction: CanvasDirection
    letterSpacing: str
    fontKerning: CanvasFontKerning
    fontStretch: CanvasFontStretch
    fontVariantCaps: CanvasFontVariantCaps
    textRendering: CanvasTextRendering
    wordSpacing: str

class CanvasPath:
    def closePath(self): ...
    def moveTo(self, x: float, y: float): ...
    def lineTo(self, x: float, y: float): ...
    def quadraticCurveTo(self, cpx: float, cpy: float, x: float, y: float): ...
    def bezierCurveTo(self, cp1x: float, cp1y: float, cp2x: float, cp2y: float, x: float, y: float): ...
    def arcTo(self, x1: float, y1: float, x2: float, y2: float, radius: float): ...
    def rect(self, x: float, y: float, w: float, h: float): ...
    def roundRect(self, x: float, y: float, w: float, h: float, radii: float | DOMPointInit | Sequence[float | DOMPointInit] | None = 0): ...
    def arc(self, x: float, y: float, radius: float, startAngle: float, endAngle: float, counterclockwise: bool | None = false): ...
    def ellipse(self, x: float, y: float, radiusX: float, radiusY: float, rotation: float, startAngle: float, endAngle: float, counterclockwise: bool | None = false): ...

class CanvasGradient:
    def addColorStop(self, offset: float, color: str): ...

class CanvasPattern:
    def setTransform(self, transform: DOMMatrix2DInit | None = {}): ...

class TextMetrics:
    width: float
    actualBoundingBoxLeft: float
    actualBoundingBoxRight: float
    fontBoundingBoxAscent: float
    fontBoundingBoxDescent: float
    actualBoundingBoxAscent: float
    actualBoundingBoxDescent: float
    emHeightAscent: float
    emHeightDescent: float
    hangingBaseline: float
    alphabeticBaseline: float
    ideographicBaseline: float

class ImageData:
    @overload
    def New(self, sw: int, sh: int, settings: ImageDataSettings | None = {}) -> ImageData: ...
    @overload
    def New(self, data: Uint8ClampedArray, sw: int, sh: int | None = None, settings: ImageDataSettings | None = {}) -> ImageData: ...
    width: int
    height: int
    data: Uint8ClampedArray
    colorSpace: PredefinedColorSpace

class Path2D(CanvasPath):
    def New(self, path: Path2D | str | None = None) -> Path2D: ...
    def addPath(self, path: Path2D, transform: DOMMatrix2DInit | None = {}): ...

class ImageBitmapRenderingContext:
    canvas: HTMLCanvasElement | OffscreenCanvas
    def transferFromImageBitmap(self, bitmap: ImageBitmap | None): ...

class OffscreenCanvas(EventTarget):
    def New(self, width: int, height: int) -> OffscreenCanvas: ...
    width: int
    height: int
    def transferToImageBitmap(self) -> ImageBitmap: ...
    def convertToBlob(self, options: ImageEncodeOptions | None = {}) -> Awaitable[Blob]: ...
    oncontextlost: EventHandler
    oncontextrestored: EventHandler

class OffscreenCanvasRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing, CanvasImageSmoothing, CanvasFillStrokeStyles, CanvasShadowStyles, CanvasFilters, CanvasRect, CanvasDrawPath, CanvasText, CanvasDrawImage, CanvasImageData, CanvasPathDrawingStyles, CanvasTextDrawingStyles, CanvasPath):
    def commit(self): ...
    canvas: OffscreenCanvas

class CustomElementRegistry:
    def define(self, name: str, constructor: CustomElementConstructor, options: ElementDefinitionOptions | None = {}): ...
    def get(self, name: str) -> CustomElementConstructor | None: ...
    def whenDefined(self, name: str) -> Awaitable[CustomElementConstructor]: ...
    def upgrade(self, root: Node): ...

class UserActivation:
    hasBeenActive: bool
    isActive: bool

class ElementContentEditable:
    contentEditable: str
    enterKeyHint: str
    isContentEditable: bool
    inputMode: str
    virtualKeyboardPolicy: str

class DataTransfer:
    def New(self) -> DataTransfer: ...
    dropEffect: str
    effectAllowed: str
    items: DataTransferItemList
    def setDragImage(self, image: Element, x: int, y: int): ...
    types: Sequence[str]
    def getData(self, format: str) -> str: ...
    def setData(self, format: str, data: str): ...
    def clearData(self, format: str | None = None): ...
    files: FileList

class DataTransferItemList:
    length: int
    @overload
    def add(self, data: str, type: str) -> DataTransferItem | None: ...
    @overload
    def add(self, data: File) -> DataTransferItem | None: ...
    def remove(self, index: int): ...
    def clear(self): ...

class DragEvent(MouseEvent):
    def New(self, type: str, eventInitDict: DragEventInit | None = {}) -> DragEvent: ...
    dataTransfer: DataTransfer | None

class BarProp:
    visible: bool

class Location:
    origin: USVString
    protocol: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString
    def assign(self, url: USVString): ...
    def replace(self, url: USVString): ...
    def reload(self): ...
    ancestorOrigins: DOMStringList

class History:
    length: int
    scrollRestoration: ScrollRestoration
    def go(self, delta: int | None = 0): ...
    def back(self): ...
    def forward(self): ...

class PopStateEvent(Event):
    def New(self, type: str, eventInitDict: PopStateEventInit | None = {}) -> PopStateEvent: ...

class HashChangeEvent(Event):
    def New(self, type: str, eventInitDict: HashChangeEventInit | None = {}) -> HashChangeEvent: ...
    oldURL: USVString
    newURL: USVString

class PageTransitionEvent(Event):
    def New(self, type: str, eventInitDict: PageTransitionEventInit | None = {}) -> PageTransitionEvent: ...
    persisted: bool

class BeforeUnloadEvent(Event):
    returnValue: str

class ErrorEvent(Event):
    def New(self, type: str, eventInitDict: ErrorEventInit | None = {}) -> ErrorEvent: ...
    message: str
    filename: USVString
    lineno: int
    colno: int

class PromiseRejectionEvent(Event):
    def New(self, type: str, eventInitDict: PromiseRejectionEventInit) -> PromiseRejectionEvent: ...

class WorkerGlobalScope(EventTarget, WindowOrWorkerGlobalScope, FontFaceSource):
    self: WorkerGlobalScope
    location: WorkerLocation
    navigator: WorkerNavigator
    def importScripts(self, urls: USVString | None = None): ...
    onerror: OnErrorEventHandler
    onlanguagechange: EventHandler
    onoffline: EventHandler
    ononline: EventHandler
    onrejectionhandled: EventHandler
    onunhandledrejection: EventHandler

class DOMParser:
    def New(self) -> DOMParser: ...
    def parseFromString(self, string: str, type: DOMParserSupportedType) -> Document: ...

class NavigatorID:
    appCodeName: str
    appName: str
    appVersion: str
    platform: str
    product: str
    productSub: str
    userAgent: str
    vendor: str
    vendorSub: str
    def taintEnabled(self) -> bool: ...
    oscpu: str

class NavigatorLanguage:
    language: str
    languages: Sequence[str]

class NavigatorOnLine:
    onLine: bool

class NavigatorContentUtils:
    def registerProtocolHandler(self, scheme: str, url: USVString): ...
    def unregisterProtocolHandler(self, scheme: str, url: USVString): ...

class NavigatorCookies:
    cookieEnabled: bool

class NavigatorPlugins:
    plugins: PluginArray
    mimeTypes: MimeTypeArray
    def javaEnabled(self) -> bool: ...
    pdfViewerEnabled: bool

class PluginArray:
    def refresh(self): ...
    length: int

class MimeTypeArray:
    length: int

class Plugin:
    name: str
    description: str
    filename: str
    length: int

class MimeType:
    type: str
    description: str
    suffixes: str
    enabledPlugin: Plugin

class ImageBitmap:
    width: int
    height: int
    def close(self): ...

class AnimationFrameProvider:
    def requestAnimationFrame(self, callback: FrameRequestCallback) -> int: ...
    def cancelAnimationFrame(self, handle: int): ...

class DedicatedWorkerGlobalScope(WorkerGlobalScope, AnimationFrameProvider):
    name: str
    def close(self): ...
    onmessage: EventHandler
    onmessageerror: EventHandler
    onrtctransform: EventHandler

class MessageEvent(Event):
    def New(self, type: str, eventInitDict: MessageEventInit | None = {}) -> MessageEvent: ...
    origin: USVString
    lastEventId: str
    source: MessageEventSource | None
    ports: Sequence[MessagePort]

class EventSource(EventTarget):
    def New(self, url: USVString, eventSourceInitDict: EventSourceInit | None = {}) -> EventSource: ...
    url: USVString
    withCredentials: bool
    readyState: int
    onopen: EventHandler
    onmessage: EventHandler
    onerror: EventHandler
    def close(self): ...

class MessageChannel:
    def New(self) -> MessageChannel: ...
    port1: MessagePort
    port2: MessagePort

class MessagePort(EventTarget):
    def start(self): ...
    def close(self): ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class BroadcastChannel(EventTarget):
    def New(self, name: str) -> BroadcastChannel: ...
    name: str
    def close(self): ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class SharedWorkerGlobalScope(WorkerGlobalScope):
    name: str
    def close(self): ...
    onconnect: EventHandler

class AbstractWorker:
    onerror: EventHandler

class Worker(EventTarget, AbstractWorker):
    def New(self, scriptURL: USVString, options: WorkerOptions | None = {}) -> Worker: ...
    def terminate(self): ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class SharedWorker(EventTarget, AbstractWorker):
    def New(self, scriptURL: USVString, options: str | WorkerOptions | None = {}) -> SharedWorker: ...
    port: MessagePort

class NavigatorConcurrentHardware:
    hardwareConcurrency: int

class WorkerLocation:
    origin: USVString
    protocol: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString

class WorkletGlobalScope: ...

class Worklet:
    def addModule(self, moduleURL: USVString, options: WorkletOptions | None = {}) -> Awaitable[None]: ...

class Storage:
    length: int
    def key(self, index: int) -> str | None: ...
    def clear(self): ...

class WindowSessionStorage:
    sessionStorage: Storage

class WindowLocalStorage:
    localStorage: Storage

class StorageEvent(Event):
    def New(self, type: str, eventInitDict: StorageEventInit | None = {}) -> StorageEvent: ...
    key: str | None
    oldValue: str | None
    newValue: str | None
    url: USVString
    storageArea: Storage | None
    def initStorageEvent(self, type: str, bubbles: bool | None = false, cancelable: bool | None = false, key: str | None = None, oldValue: str | None = None, newValue: str | None = None, url: USVString | None = "", storageArea: Storage | None = None): ...

class HTMLMarqueeElement(HTMLElement):
    def New(self) -> HTMLMarqueeElement: ...
    behavior: str
    bgColor: str
    direction: str
    height: str
    hspace: int
    loop: int
    scrollAmount: int
    scrollDelay: int
    trueSpeed: bool
    vspace: int
    width: str
    def start(self): ...
    def stop(self): ...

class HTMLFrameSetElement(HTMLElement, WindowEventHandlers):
    def New(self) -> HTMLFrameSetElement: ...
    cols: str
    rows: str

class HTMLFrameElement(HTMLElement):
    def New(self) -> HTMLFrameElement: ...
    name: str
    scrolling: str
    src: USVString
    frameBorder: str
    longDesc: USVString
    noResize: bool
    contentDocument: Document | None
    contentWindow: WindowProxy | None
    marginHeight: str
    marginWidth: str

class HTMLDirectoryElement(HTMLElement):
    def New(self) -> HTMLDirectoryElement: ...
    compact: bool

class HTMLFontElement(HTMLElement):
    def New(self) -> HTMLFontElement: ...
    color: str
    face: str
    size: str

class HTMLParamElement(HTMLElement):
    def New(self) -> HTMLParamElement: ...
    name: str
    value: str
    type: str
    valueType: str

class External:
    def AddSearchProvider(self): ...
    def IsSearchProviderInstalled(self): ...

class PerformanceMark(PerformanceEntry):
    def New(self, markName: str, markOptions: PerformanceMarkOptions | None = {}) -> PerformanceMark: ...

class PerformanceMeasure(PerformanceEntry): ...

class WEBGL_compressed_texture_etc1: ...

class Presentation:
    defaultRequest: PresentationRequest | None
    receiver: PresentationReceiver | None

class PresentationRequest(EventTarget):
    @overload
    def New(self, url: USVString) -> PresentationRequest: ...
    @overload
    def New(self, urls: Sequence[USVString]) -> PresentationRequest: ...
    def start(self) -> Awaitable[PresentationConnection]: ...
    def reconnect(self, presentationId: USVString) -> Awaitable[PresentationConnection]: ...
    def getAvailability(self) -> Awaitable[PresentationAvailability]: ...
    onconnectionavailable: EventHandler

class PresentationAvailability(EventTarget):
    value: bool
    onchange: EventHandler

class PresentationConnectionAvailableEvent(Event):
    def New(self, type: str, eventInitDict: PresentationConnectionAvailableEventInit) -> PresentationConnectionAvailableEvent: ...
    connection: PresentationConnection

class PresentationConnection(EventTarget):
    id: USVString
    url: USVString
    state: PresentationConnectionState
    def close(self): ...
    def terminate(self): ...
    onconnect: EventHandler
    onclose: EventHandler
    onterminate: EventHandler
    binaryType: BinaryType
    onmessage: EventHandler
    @overload
    def send(self, message: str): ...
    @overload
    def send(self, data: Blob): ...
    @overload
    def send(self, data: ArrayBuffer): ...
    @overload
    def send(self, data: ArrayBufferView): ...

class PresentationConnectionCloseEvent(Event):
    def New(self, type: str, eventInitDict: PresentationConnectionCloseEventInit) -> PresentationConnectionCloseEvent: ...
    reason: PresentationConnectionCloseReason
    message: str

class PresentationReceiver:
    connectionList: Awaitable[PresentationConnectionList]

class PresentationConnectionList(EventTarget):
    connections: Sequence[PresentationConnection]
    onconnectionavailable: EventHandler

class PerformanceServerTiming:
    name: str
    duration: DOMHighResTimeStamp
    description: str
    def toJSON(self) -> object: ...

class PerformanceResourceTiming(PerformanceEntry):
    serverTiming: Sequence[PerformanceServerTiming]
    initiatorType: str
    nextHopProtocol: ByteString
    workerStart: DOMHighResTimeStamp
    redirectStart: DOMHighResTimeStamp
    redirectEnd: DOMHighResTimeStamp
    fetchStart: DOMHighResTimeStamp
    domainLookupStart: DOMHighResTimeStamp
    domainLookupEnd: DOMHighResTimeStamp
    connectStart: DOMHighResTimeStamp
    connectEnd: DOMHighResTimeStamp
    secureConnectionStart: DOMHighResTimeStamp
    requestStart: DOMHighResTimeStamp
    responseStart: DOMHighResTimeStamp
    responseEnd: DOMHighResTimeStamp
    transferSize: int
    encodedBodySize: int
    decodedBodySize: int
    responseStatus: int
    renderBlockingStatus: RenderBlockingStatusType
    def toJSON(self) -> object: ...

class EXT_clip_cull_distance: ...

class EXT_texture_compression_rgtc: ...

class NavigatorUAData:
    brands: Sequence[NavigatorUABrandVersion]
    mobile: bool
    platform: str
    def getHighEntropyValues(self, hints: Sequence[str]) -> Awaitable[UADataValues]: ...
    def toJSON(self) -> UALowEntropyJSON: ...

class NavigatorUA:
    userAgentData: NavigatorUAData

class FileSystemHandle:
    def queryPermission(self, descriptor: FileSystemHandlePermissionDescriptor | None = {}) -> Awaitable[PermissionState]: ...
    def requestPermission(self, descriptor: FileSystemHandlePermissionDescriptor | None = {}) -> Awaitable[PermissionState]: ...
    kind: FileSystemHandleKind
    name: USVString
    def isSameEntry(self, other: FileSystemHandle) -> Awaitable[bool]: ...

class XRLightProbe(EventTarget):
    probeSpace: XRSpace
    onreflectionchange: EventHandler

class XRLightEstimate:
    sphericalHarmonicsCoefficients: Float32Array
    primaryLightDirection: DOMPointReadOnly
    primaryLightIntensity: DOMPointReadOnly

class RemotePlayback(EventTarget):
    def watchAvailability(self, callback: RemotePlaybackAvailabilityCallback) -> Awaitable[int]: ...
    def cancelWatchAvailability(self, id: int | None = None) -> Awaitable[None]: ...
    state: RemotePlaybackState
    onconnecting: EventHandler
    onconnect: EventHandler
    ondisconnect: EventHandler
    def prompt(self) -> Awaitable[None]: ...

class WEBGL_multi_draw_instanced_base_vertex_base_instance:
    def multiDrawArraysInstancedBaseInstanceWEBGL(self, mode: GLenum, firstsList: Int32Array | Sequence[GLint], firstsOffset: GLuint, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, instanceCountsList: Int32Array | Sequence[GLsizei], instanceCountsOffset: GLuint, baseInstancesList: Uint32Array | Sequence[GLuint], baseInstancesOffset: GLuint, drawcount: GLsizei): ...
    def multiDrawElementsInstancedBaseVertexBaseInstanceWEBGL(self, mode: GLenum, countsList: Int32Array | Sequence[GLsizei], countsOffset: GLuint, type: GLenum, offsetsList: Int32Array | Sequence[GLsizei], offsetsOffset: GLuint, instanceCountsList: Int32Array | Sequence[GLsizei], instanceCountsOffset: GLuint, baseVerticesList: Int32Array | Sequence[GLint], baseVerticesOffset: GLuint, baseInstancesList: Uint32Array | Sequence[GLuint], baseInstancesOffset: GLuint, drawcount: GLsizei): ...

class PublicKeyCredential(Credential):
    rawId: ArrayBuffer
    response: AuthenticatorResponse
    authenticatorAttachment: str | None
    def getClientExtensionResults(self) -> AuthenticationExtensionsClientOutputs: ...
    def toJSON(self) -> PublicKeyCredentialJSON: ...

class AuthenticatorResponse:
    clientDataJSON: ArrayBuffer

class AuthenticatorAttestationResponse(AuthenticatorResponse):
    attestationObject: ArrayBuffer
    def getTransports(self) -> Sequence[str]: ...
    def getAuthenticatorData(self) -> ArrayBuffer: ...
    def getPublicKey(self) -> ArrayBuffer: ...
    def getPublicKeyAlgorithm(self) -> COSEAlgorithmIdentifier: ...

class AuthenticatorAssertionResponse(AuthenticatorResponse):
    authenticatorData: ArrayBuffer
    signature: ArrayBuffer
    userHandle: ArrayBuffer
    attestationObject: ArrayBuffer

class XRHitTestSource:
    def cancel(self): ...

class XRTransientInputHitTestSource:
    def cancel(self): ...

class XRHitTestResult:
    def getPose(self, baseSpace: XRSpace) -> XRPose | None: ...
    def createAnchor(self) -> Awaitable[XRAnchor]: ...

class XRTransientInputHitTestResult:
    inputSource: XRInputSource
    results: Sequence[XRHitTestResult]

class XRRay:
    @overload
    def New(self, origin: DOMPointInit | None = {}, direction: XRRayDirectionInit | None = {}) -> XRRay: ...
    @overload
    def New(self, transform: XRRigidTransform) -> XRRay: ...
    origin: DOMPointReadOnly
    direction: DOMPointReadOnly
    matrix: Float32Array

class XRAnchor:
    anchorSpace: XRSpace
    def requestPersistentHandle(self) -> Awaitable[str]: ...
    def delete(self): ...

class XRAnchorSet: ...

class TextDecoderCommon:
    encoding: str
    fatal: bool
    ignoreBOM: bool

class TextDecoder(TextDecoderCommon):
    def New(self, label: str | None = "utf-8", options: TextDecoderOptions | None = {}) -> TextDecoder: ...
    def decode(self, input: BufferSource | None = None, options: TextDecodeOptions | None = {}) -> USVString: ...

class TextEncoderCommon:
    encoding: str

class TextEncoder(TextEncoderCommon):
    def New(self) -> TextEncoder: ...
    def encode(self, input: USVString | None = "") -> Uint8Array: ...
    def encodeInto(self, source: USVString, destination: Uint8Array) -> TextEncoderEncodeIntoResult: ...

class TextDecoderStream(TextDecoderCommon, GenericTransformStream):
    def New(self, label: str | None = "utf-8", options: TextDecoderOptions | None = {}) -> TextDecoderStream: ...

class TextEncoderStream(TextEncoderCommon, GenericTransformStream):
    def New(self) -> TextEncoderStream: ...

class XMLSerializer:
    def New(self) -> XMLSerializer: ...
    def serializeToString(self, root: Node) -> str: ...

class InnerHTML:
    innerHTML: str

class WEBGL_debug_shaders:
    def getTranslatedShaderSource(self, shader: WebGLShader) -> str: ...

class SpeechRecognition(EventTarget):
    def New(self) -> SpeechRecognition: ...
    grammars: SpeechGrammarList
    lang: str
    continuous: bool
    interimResults: bool
    maxAlternatives: int
    def start(self): ...
    def stop(self): ...
    def abort(self): ...
    onaudiostart: EventHandler
    onsoundstart: EventHandler
    onspeechstart: EventHandler
    onspeechend: EventHandler
    onsoundend: EventHandler
    onaudioend: EventHandler
    onresult: EventHandler
    onnomatch: EventHandler
    onerror: EventHandler
    onstart: EventHandler
    onend: EventHandler

class SpeechRecognitionErrorEvent(Event):
    def New(self, type: str, eventInitDict: SpeechRecognitionErrorEventInit) -> SpeechRecognitionErrorEvent: ...
    error: SpeechRecognitionErrorCode
    message: str

class SpeechRecognitionAlternative:
    transcript: str
    confidence: float

class SpeechRecognitionResult:
    length: int
    isFinal: bool

class SpeechRecognitionResultList:
    length: int

class SpeechRecognitionEvent(Event):
    def New(self, type: str, eventInitDict: SpeechRecognitionEventInit) -> SpeechRecognitionEvent: ...
    resultIndex: int
    results: SpeechRecognitionResultList

class SpeechGrammar:
    src: str
    weight: float

class SpeechGrammarList:
    def New(self) -> SpeechGrammarList: ...
    length: int
    def addFromURI(self, src: str, weight: float | None = 1.0): ...
    def addFromString(self, string: str, weight: float | None = 1.0): ...

class SpeechSynthesis(EventTarget):
    pending: bool
    speaking: bool
    paused: bool
    onvoiceschanged: EventHandler
    def speak(self, utterance: SpeechSynthesisUtterance): ...
    def cancel(self): ...
    def pause(self): ...
    def resume(self): ...
    def getVoices(self) -> Sequence[SpeechSynthesisVoice]: ...

class SpeechSynthesisUtterance(EventTarget):
    def New(self, text: str | None = None) -> SpeechSynthesisUtterance: ...
    text: str
    lang: str
    voice: SpeechSynthesisVoice | None
    volume: float
    rate: float
    pitch: float
    onstart: EventHandler
    onend: EventHandler
    onerror: EventHandler
    onpause: EventHandler
    onresume: EventHandler
    onmark: EventHandler
    onboundary: EventHandler

class SpeechSynthesisEvent(Event):
    def New(self, type: str, eventInitDict: SpeechSynthesisEventInit) -> SpeechSynthesisEvent: ...
    utterance: SpeechSynthesisUtterance
    charIndex: int
    charLength: int
    elapsedTime: float
    name: str

class SpeechSynthesisErrorEvent(SpeechSynthesisEvent):
    def New(self, type: str, eventInitDict: SpeechSynthesisErrorEventInit) -> SpeechSynthesisErrorEvent: ...
    error: SpeechSynthesisErrorCode

class SpeechSynthesisVoice:
    voiceURI: str
    name: str
    lang: str
    localService: bool
    default: bool

class SFrameTransform(GenericTransformStream):
    def New(self, options: SFrameTransformOptions | None = {}) -> SFrameTransform: ...
    def setEncryptionKey(self, key: CryptoKey, keyID: CryptoKeyID | None = None) -> Awaitable[None]: ...
    onerror: EventHandler

class SFrameTransformErrorEvent(Event):
    def New(self, type: str, eventInitDict: SFrameTransformErrorEventInit) -> SFrameTransformErrorEvent: ...
    errorType: SFrameTransformErrorEventType
    keyID: CryptoKeyID | None

class RTCEncodedVideoFrame:
    type: RTCEncodedVideoFrameType
    timestamp: int
    data: ArrayBuffer
    def getMetadata(self) -> RTCEncodedVideoFrameMetadata: ...

class RTCEncodedAudioFrame:
    timestamp: int
    data: ArrayBuffer
    def getMetadata(self) -> RTCEncodedAudioFrameMetadata: ...

class RTCTransformEvent(Event):
    transformer: RTCRtpScriptTransformer

class RTCRtpScriptTransformer:
    readable: ReadableStream
    writable: WritableStream
    def generateKeyFrame(self, rid: str | None = None) -> Awaitable[int]: ...
    def sendKeyFrameRequest(self) -> Awaitable[None]: ...

class RTCRtpScriptTransform: ...

class OES_texture_float: ...

class WEBGL_compressed_texture_s3tc: ...

class NavigationEvent(UIEvent):
    def New(self, type: str, eventInitDict: NavigationEventInit | None = {}) -> NavigationEvent: ...
    dir: SpatialNavigationDirection
    relatedTarget: EventTarget | None

class FileSystemFileHandle(FileSystemHandle):
    def getFile(self) -> Awaitable[File]: ...
    def createWritable(self, options: FileSystemCreateWritableOptions | None = {}) -> Awaitable[FileSystemWritableFileStream]: ...
    def createSyncAccessHandle(self) -> Awaitable[FileSystemSyncAccessHandle]: ...

class FileSystemDirectoryHandle(FileSystemHandle):
    def getFileHandle(self, name: USVString, options: FileSystemGetFileOptions | None = {}) -> Awaitable[FileSystemFileHandle]: ...
    def getDirectoryHandle(self, name: USVString, options: FileSystemGetDirectoryOptions | None = {}) -> Awaitable[FileSystemDirectoryHandle]: ...
    def removeEntry(self, name: USVString, options: FileSystemRemoveOptions | None = {}) -> Awaitable[None]: ...
    def resolve(self, possibleDescendant: FileSystemHandle) -> Awaitable[Sequence[USVString]]: ...

class FileSystemWritableFileStream(WritableStream):
    def write(self, data: FileSystemWriteChunkType) -> Awaitable[None]: ...
    def seek(self, position: int) -> Awaitable[None]: ...
    def truncate(self, size: int) -> Awaitable[None]: ...

class FileSystemSyncAccessHandle:
    def read(self, buffer: BufferSource, options: FileSystemReadWriteOptions | None = {}) -> int: ...
    def write(self, buffer: BufferSource, options: FileSystemReadWriteOptions | None = {}) -> int: ...
    def truncate(self, newSize: int): ...
    def getSize(self) -> int: ...
    def flush(self): ...
    def close(self): ...

class WebGLQuery(WebGLObject): ...

class WebGLSampler(WebGLObject): ...

class WebGLSync(WebGLObject): ...

class WebGLTransformFeedback(WebGLObject): ...

class WebGLVertexArrayObject(WebGLObject): ...

class WebGL2RenderingContextBase:
    def copyBufferSubData(self, readTarget: GLenum, writeTarget: GLenum, readOffset: GLintptr, writeOffset: GLintptr, size: GLsizeiptr): ...
    def getBufferSubData(self, target: GLenum, srcByteOffset: GLintptr, dstBuffer: ArrayBufferView, dstOffset: GLuint | None = 0, length: GLuint | None = 0): ...
    def blitFramebuffer(self, srcX0: GLint, srcY0: GLint, srcX1: GLint, srcY1: GLint, dstX0: GLint, dstY0: GLint, dstX1: GLint, dstY1: GLint, mask: GLbitfield, filter: GLenum): ...
    def framebufferTextureLayer(self, target: GLenum, attachment: GLenum, texture: WebGLTexture | None, level: GLint, layer: GLint): ...
    def invalidateFramebuffer(self, target: GLenum, attachments: Sequence[GLenum]): ...
    def invalidateSubFramebuffer(self, target: GLenum, attachments: Sequence[GLenum], x: GLint, y: GLint, width: GLsizei, height: GLsizei): ...
    def readBuffer(self, src: GLenum): ...
    def renderbufferStorageMultisample(self, target: GLenum, samples: GLsizei, internalformat: GLenum, width: GLsizei, height: GLsizei): ...
    def texStorage2D(self, target: GLenum, levels: GLsizei, internalformat: GLenum, width: GLsizei, height: GLsizei): ...
    def texStorage3D(self, target: GLenum, levels: GLsizei, internalformat: GLenum, width: GLsizei, height: GLsizei, depth: GLsizei): ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, pboOffset: GLintptr): ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, srcData: ArrayBufferView | None): ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, srcData: ArrayBufferView, srcOffset: GLuint): ...
    @overload
    def texSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, type: GLenum, pboOffset: GLintptr): ...
    @overload
    def texSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, type: GLenum, srcData: ArrayBufferView | None, srcOffset: GLuint | None = 0): ...
    def copyTexSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, x: GLint, y: GLint, width: GLsizei, height: GLsizei): ...
    @overload
    def compressedTexImage3D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, imageSize: GLsizei, offset: GLintptr): ...
    @overload
    def compressedTexImage3D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, srcData: ArrayBufferView, srcOffset: GLuint | None = 0, srcLengthOverride: GLuint | None = 0): ...
    @overload
    def compressedTexSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, imageSize: GLsizei, offset: GLintptr): ...
    @overload
    def compressedTexSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, srcData: ArrayBufferView, srcOffset: GLuint | None = 0, srcLengthOverride: GLuint | None = 0): ...
    def getFragDataLocation(self, program: WebGLProgram, name: str) -> GLint: ...
    def uniform1ui(self, location: WebGLUniformLocation | None, v0: GLuint): ...
    def uniform2ui(self, location: WebGLUniformLocation | None, v0: GLuint, v1: GLuint): ...
    def uniform3ui(self, location: WebGLUniformLocation | None, v0: GLuint, v1: GLuint, v2: GLuint): ...
    def uniform4ui(self, location: WebGLUniformLocation | None, v0: GLuint, v1: GLuint, v2: GLuint, v3: GLuint): ...
    def uniform1uiv(self, location: WebGLUniformLocation | None, data: Uint32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform2uiv(self, location: WebGLUniformLocation | None, data: Uint32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform3uiv(self, location: WebGLUniformLocation | None, data: Uint32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform4uiv(self, location: WebGLUniformLocation | None, data: Uint32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix3x2fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix4x2fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix2x3fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix4x3fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix2x4fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix3x4fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def vertexAttribI4i(self, index: GLuint, x: GLint, y: GLint, z: GLint, w: GLint): ...
    def vertexAttribI4iv(self, index: GLuint, values: Int32List): ...
    def vertexAttribI4ui(self, index: GLuint, x: GLuint, y: GLuint, z: GLuint, w: GLuint): ...
    def vertexAttribI4uiv(self, index: GLuint, values: Uint32List): ...
    def vertexAttribIPointer(self, index: GLuint, size: GLint, type: GLenum, stride: GLsizei, offset: GLintptr): ...
    def vertexAttribDivisor(self, index: GLuint, divisor: GLuint): ...
    def drawArraysInstanced(self, mode: GLenum, first: GLint, count: GLsizei, instanceCount: GLsizei): ...
    def drawElementsInstanced(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr, instanceCount: GLsizei): ...
    def drawRangeElements(self, mode: GLenum, start: GLuint, end: GLuint, count: GLsizei, type: GLenum, offset: GLintptr): ...
    def drawBuffers(self, buffers: Sequence[GLenum]): ...
    def clearBufferfv(self, buffer: GLenum, drawbuffer: GLint, values: Float32List, srcOffset: GLuint | None = 0): ...
    def clearBufferiv(self, buffer: GLenum, drawbuffer: GLint, values: Int32List, srcOffset: GLuint | None = 0): ...
    def clearBufferuiv(self, buffer: GLenum, drawbuffer: GLint, values: Uint32List, srcOffset: GLuint | None = 0): ...
    def clearBufferfi(self, buffer: GLenum, drawbuffer: GLint, depth: GLfloat, stencil: GLint): ...
    def createQuery(self) -> WebGLQuery | None: ...
    def deleteQuery(self, query: WebGLQuery | None): ...
    def isQuery(self, query: WebGLQuery | None) -> GLboolean: ...
    def beginQuery(self, target: GLenum, query: WebGLQuery): ...
    def endQuery(self, target: GLenum): ...
    def getQuery(self, target: GLenum, pname: GLenum) -> WebGLQuery | None: ...
    def createSampler(self) -> WebGLSampler | None: ...
    def deleteSampler(self, sampler: WebGLSampler | None): ...
    def isSampler(self, sampler: WebGLSampler | None) -> GLboolean: ...
    def bindSampler(self, unit: GLuint, sampler: WebGLSampler | None): ...
    def samplerParameteri(self, sampler: WebGLSampler, pname: GLenum, param: GLint): ...
    def samplerParameterf(self, sampler: WebGLSampler, pname: GLenum, param: GLfloat): ...
    def fenceSync(self, condition: GLenum, flags: GLbitfield) -> WebGLSync | None: ...
    def isSync(self, sync: WebGLSync | None) -> GLboolean: ...
    def deleteSync(self, sync: WebGLSync | None): ...
    def clientWaitSync(self, sync: WebGLSync, flags: GLbitfield, timeout: GLuint64) -> GLenum: ...
    def waitSync(self, sync: WebGLSync, flags: GLbitfield, timeout: GLint64): ...
    def createTransformFeedback(self) -> WebGLTransformFeedback | None: ...
    def deleteTransformFeedback(self, tf: WebGLTransformFeedback | None): ...
    def isTransformFeedback(self, tf: WebGLTransformFeedback | None) -> GLboolean: ...
    def bindTransformFeedback(self, target: GLenum, tf: WebGLTransformFeedback | None): ...
    def beginTransformFeedback(self, primitiveMode: GLenum): ...
    def endTransformFeedback(self): ...
    def transformFeedbackVaryings(self, program: WebGLProgram, varyings: Sequence[str], bufferMode: GLenum): ...
    def getTransformFeedbackVarying(self, program: WebGLProgram, index: GLuint) -> WebGLActiveInfo | None: ...
    def pauseTransformFeedback(self): ...
    def resumeTransformFeedback(self): ...
    def bindBufferBase(self, target: GLenum, index: GLuint, buffer: WebGLBuffer | None): ...
    def bindBufferRange(self, target: GLenum, index: GLuint, buffer: WebGLBuffer | None, offset: GLintptr, size: GLsizeiptr): ...
    def getUniformIndices(self, program: WebGLProgram, uniformNames: Sequence[str]) -> Sequence[GLuint]: ...
    def getUniformBlockIndex(self, program: WebGLProgram, uniformBlockName: str) -> GLuint: ...
    def getActiveUniformBlockName(self, program: WebGLProgram, uniformBlockIndex: GLuint) -> str | None: ...
    def uniformBlockBinding(self, program: WebGLProgram, uniformBlockIndex: GLuint, uniformBlockBinding: GLuint): ...
    def createVertexArray(self) -> WebGLVertexArrayObject | None: ...
    def deleteVertexArray(self, vertexArray: WebGLVertexArrayObject | None): ...
    def isVertexArray(self, vertexArray: WebGLVertexArrayObject | None) -> GLboolean: ...
    def bindVertexArray(self, array: WebGLVertexArrayObject | None): ...

class WebGL2RenderingContextOverloads:
    @overload
    def bufferData(self, target: GLenum, size: GLsizeiptr, usage: GLenum): ...
    @overload
    def bufferData(self, target: GLenum, srcData: BufferSource | None, usage: GLenum): ...
    @overload
    def bufferSubData(self, target: GLenum, dstByteOffset: GLintptr, srcData: BufferSource): ...
    @overload
    def bufferData(self, target: GLenum, srcData: ArrayBufferView, usage: GLenum, srcOffset: GLuint, length: GLuint | None = 0): ...
    @overload
    def bufferSubData(self, target: GLenum, dstByteOffset: GLintptr, srcData: ArrayBufferView, srcOffset: GLuint, length: GLuint | None = 0): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, pboOffset: GLintptr): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, srcData: ArrayBufferView, srcOffset: GLuint): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pboOffset: GLintptr): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, source: TexImageSource): ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, srcData: ArrayBufferView, srcOffset: GLuint): ...
    @overload
    def compressedTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, border: GLint, imageSize: GLsizei, offset: GLintptr): ...
    @overload
    def compressedTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, border: GLint, srcData: ArrayBufferView, srcOffset: GLuint | None = 0, srcLengthOverride: GLuint | None = 0): ...
    @overload
    def compressedTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, imageSize: GLsizei, offset: GLintptr): ...
    @overload
    def compressedTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, srcData: ArrayBufferView, srcOffset: GLuint | None = 0, srcLengthOverride: GLuint | None = 0): ...
    def uniform1fv(self, location: WebGLUniformLocation | None, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform2fv(self, location: WebGLUniformLocation | None, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform3fv(self, location: WebGLUniformLocation | None, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform4fv(self, location: WebGLUniformLocation | None, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform1iv(self, location: WebGLUniformLocation | None, data: Int32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform2iv(self, location: WebGLUniformLocation | None, data: Int32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform3iv(self, location: WebGLUniformLocation | None, data: Int32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniform4iv(self, location: WebGLUniformLocation | None, data: Int32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix2fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix3fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    def uniformMatrix4fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List, srcOffset: GLuint | None = 0, srcLength: GLuint | None = 0): ...
    @overload
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, dstData: ArrayBufferView | None): ...
    @overload
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, offset: GLintptr): ...
    @overload
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, dstData: ArrayBufferView, dstOffset: GLuint): ...

class WebGL2RenderingContext(WebGLRenderingContextBase, WebGL2RenderingContextBase, WebGL2RenderingContextOverloads): ...

class ContentIndex:
    def add(self, description: ContentDescription) -> Awaitable[None]: ...
    def delete(self, id: str) -> Awaitable[None]: ...
    def getAll(self) -> Awaitable[Sequence[ContentDescription]]: ...

class ContentIndexEvent(ExtendableEvent):
    def New(self, type: str, init: ContentIndexEventInit) -> ContentIndexEvent: ...
    id: str

class HTMLPortalElement(HTMLElement):
    def New(self) -> HTMLPortalElement: ...
    src: USVString
    referrerPolicy: str
    def activate(self, options: PortalActivateOptions | None = {}) -> Awaitable[None]: ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class PortalHost(EventTarget):
    onmessage: EventHandler
    onmessageerror: EventHandler

class PortalActivateEvent(Event):
    def New(self, type: str, eventInitDict: PortalActivateEventInit | None = {}) -> PortalActivateEvent: ...
    def adoptPredecessor(self) -> HTMLPortalElement: ...

class PushManager:
    def subscribe(self, options: PushSubscriptionOptionsInit | None = {}) -> Awaitable[PushSubscription]: ...
    def getSubscription(self) -> Awaitable[PushSubscription | None]: ...
    def permissionState(self, options: PushSubscriptionOptionsInit | None = {}) -> Awaitable[PermissionState]: ...

class PushSubscriptionOptions:
    userVisibleOnly: bool
    applicationServerKey: ArrayBuffer

class PushSubscription:
    endpoint: USVString
    expirationTime: EpochTimeStamp | None
    options: PushSubscriptionOptions
    def getKey(self, name: PushEncryptionKeyName) -> ArrayBuffer: ...
    def unsubscribe(self) -> Awaitable[bool]: ...
    def toJSON(self) -> PushSubscriptionJSON: ...

class PushMessageData:
    def arrayBuffer(self) -> ArrayBuffer: ...
    def blob(self) -> Blob: ...
    def text(self) -> USVString: ...

class PushEvent(ExtendableEvent):
    def New(self, type: str, eventInitDict: PushEventInit | None = {}) -> PushEvent: ...
    data: PushMessageData | None

class PushSubscriptionChangeEvent(ExtendableEvent):
    def New(self, type: str, eventInitDict: PushSubscriptionChangeEventInit | None = {}) -> PushSubscriptionChangeEvent: ...
    newSubscription: PushSubscription | None
    oldSubscription: PushSubscription | None

class CloseWatcher(EventTarget):
    def New(self, options: CloseWatcherOptions | None = {}) -> CloseWatcher: ...
    def destroy(self): ...
    def close(self): ...
    oncancel: EventHandler
    onclose: EventHandler

class Profiler(EventTarget):
    def New(self, options: ProfilerInitOptions) -> Profiler: ...
    sampleInterval: DOMHighResTimeStamp
    stopped: bool
    def stop(self) -> Awaitable[ProfilerTrace]: ...

class FocusEvent(UIEvent):
    def New(self, type: str, eventInitDict: FocusEventInit | None = {}) -> FocusEvent: ...
    relatedTarget: EventTarget | None

class WheelEvent(MouseEvent):
    def New(self, type: str, eventInitDict: WheelEventInit | None = {}) -> WheelEvent: ...
    deltaX: float
    deltaY: float
    deltaZ: float
    deltaMode: int

class InputEvent(UIEvent):
    def New(self, type: str, eventInitDict: InputEventInit | None = {}) -> InputEvent: ...
    data: str | None
    isComposing: bool
    inputType: str
    dataTransfer: DataTransfer | None
    def getTargetRanges(self) -> Sequence[StaticRange]: ...

class KeyboardEvent(UIEvent):
    def New(self, type: str, eventInitDict: KeyboardEventInit | None = {}) -> KeyboardEvent: ...
    key: str
    code: str
    location: int
    ctrlKey: bool
    shiftKey: bool
    altKey: bool
    metaKey: bool
    repeat: bool
    isComposing: bool
    def getModifierState(self, keyArg: str) -> bool: ...
    def initKeyboardEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false, viewArg: Window | None = None, keyArg: str | None = "", locationArg: int | None = 0, ctrlKey: bool | None = false, altKey: bool | None = false, shiftKey: bool | None = false, metaKey: bool | None = false): ...
    charCode: int
    keyCode: int

class CompositionEvent(UIEvent):
    def New(self, type: str, eventInitDict: CompositionEventInit | None = {}) -> CompositionEvent: ...
    data: str
    def initCompositionEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false, viewArg: WindowProxy | None = None, dataArg: str | None = ""): ...

class MutationEvent(Event):
    relatedNode: Node | None
    prevValue: str
    newValue: str
    attrName: str
    attrChange: int
    def initMutationEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false, relatedNodeArg: Node | None = None, prevValueArg: str | None = "", newValueArg: str | None = "", attrNameArg: str | None = "", attrChangeArg: int | None = 0): ...

class OES_element_index_uint: ...

class JsonLd: ...

class RdfDataset:
    def New(self) -> RdfDataset: ...
    defaultGraph: RdfGraph
    def add(self, graphName: USVString, graph: RdfGraph): ...

class RdfGraph:
    def New(self) -> RdfGraph: ...
    def add(self, triple: RdfTriple): ...

class RdfTriple:
    def New(self) -> RdfTriple: ...
    subject: USVString
    predicate: USVString
    object: USVString | RdfLiteral

class RdfLiteral:
    def New(self) -> RdfLiteral: ...
    value: USVString
    datatype: USVString
    language: USVString | None

class RemoteDocument:
    def New(self) -> RemoteDocument: ...
    contentType: USVString
    contextUrl: USVString
    documentUrl: USVString
    profile: USVString

class CSSAnimation(Animation):
    animationName: CSSOMString

class ReportBody:
    def toJSON(self) -> object: ...

class Report:
    def toJSON(self) -> object: ...
    type: str
    url: str
    body: ReportBody | None

class ReportingObserver:
    def New(self, callback: ReportingObserverCallback, options: ReportingObserverOptions | None = {}) -> ReportingObserver: ...
    def observe(self): ...
    def disconnect(self): ...
    def takeRecords(self) -> ReportList: ...

class OrientationSensor(Sensor):
    quaternion: Sequence[float]
    def populateMatrix(self, targetMatrix: RotationMatrixType): ...

class AbsoluteOrientationSensor(OrientationSensor):
    def New(self, sensorOptions: OrientationSensorOptions | None = {}) -> AbsoluteOrientationSensor: ...

class RelativeOrientationSensor(OrientationSensor):
    def New(self, sensorOptions: OrientationSensorOptions | None = {}) -> RelativeOrientationSensor: ...

class MediaRecorder(EventTarget):
    def New(self, stream: MediaStream, options: MediaRecorderOptions | None = {}) -> MediaRecorder: ...
    stream: MediaStream
    mimeType: str
    state: RecordingState
    onstart: EventHandler
    onstop: EventHandler
    ondataavailable: EventHandler
    onpause: EventHandler
    onresume: EventHandler
    onerror: EventHandler
    videoBitsPerSecond: int
    audioBitsPerSecond: int
    audioBitrateMode: BitrateMode
    def start(self, timeslice: int | None = None): ...
    def stop(self): ...
    def pause(self): ...
    def resume(self): ...
    def requestData(self): ...

class BlobEvent(Event):
    def New(self, type: str, eventInitDict: BlobEventInit) -> BlobEvent: ...
    data: Blob
    timecode: DOMHighResTimeStamp

class CaptureActionEvent(Event):
    def New(self, init: CaptureActionEventInit | None = {}) -> CaptureActionEvent: ...
    action: CaptureAction

class MediaSession:
    metadata: MediaMetadata | None
    playbackState: MediaSessionPlaybackState
    def setActionHandler(self, action: MediaSessionAction, handler: MediaSessionActionHandler | None): ...
    def setPositionState(self, state: MediaPositionState | None = {}): ...
    def setMicrophoneActive(self, active: bool): ...
    def setCameraActive(self, active: bool): ...

class MediaMetadata:
    def New(self, init: MediaMetadataInit | None = {}) -> MediaMetadata: ...
    title: str
    artist: str
    album: str
    artwork: Sequence[MediaImage]

class Sanitizer:
    def New(self, config: SanitizerConfig | None = {}) -> Sanitizer: ...
    def sanitize(self, input: Document | DocumentFragment) -> DocumentFragment: ...
    def sanitizeFor(self, element: str, input: str) -> Element | None: ...
    def getConfiguration(self) -> SanitizerConfig: ...

class XRCompositionLayer(XRLayer):
    layout: XRLayerLayout
    blendTextureSourceAlpha: bool
    chromaticAberrationCorrection: bool | None
    forceMonoPresentation: bool
    opacity: float
    mipLevels: int
    needsRedraw: bool
    def destroy(self): ...

class XRProjectionLayer(XRCompositionLayer):
    textureWidth: int
    textureHeight: int
    textureArrayLength: int
    ignoreDepthValues: bool
    fixedFoveation: float | None
    deltaPose: XRRigidTransform | None

class XRQuadLayer(XRCompositionLayer):
    space: XRSpace
    transform: XRRigidTransform
    width: float
    height: float
    onredraw: EventHandler

class XRCylinderLayer(XRCompositionLayer):
    space: XRSpace
    transform: XRRigidTransform
    radius: float
    centralAngle: float
    aspectRatio: float
    onredraw: EventHandler

class XREquirectLayer(XRCompositionLayer):
    space: XRSpace
    transform: XRRigidTransform
    radius: float
    centralHorizontalAngle: float
    upperVerticalAngle: float
    lowerVerticalAngle: float
    onredraw: EventHandler

class XRCubeLayer(XRCompositionLayer):
    space: XRSpace
    orientation: DOMPointReadOnly
    onredraw: EventHandler

class XRSubImage:
    viewport: XRViewport

class XRWebGLSubImage(XRSubImage):
    colorTexture: WebGLTexture
    depthStencilTexture: WebGLTexture | None
    motionVectorTexture: WebGLTexture | None
    imageIndex: int | None
    colorTextureWidth: int
    colorTextureHeight: int
    depthStencilTextureWidth: int | None
    depthStencilTextureHeight: int | None
    motionVectorTextureWidth: int | None
    motionVectorTextureHeight: int | None

class XRMediaBinding:
    def New(self, session: XRSession) -> XRMediaBinding: ...
    def createQuadLayer(self, video: HTMLVideoElement, init: XRMediaQuadLayerInit | None = {}) -> XRQuadLayer: ...
    def createCylinderLayer(self, video: HTMLVideoElement, init: XRMediaCylinderLayerInit | None = {}) -> XRCylinderLayer: ...
    def createEquirectLayer(self, video: HTMLVideoElement, init: XRMediaEquirectLayerInit | None = {}) -> XREquirectLayer: ...

class XRLayerEvent(Event):
    def New(self, type: str, eventInitDict: XRLayerEventInit) -> XRLayerEvent: ...
    layer: XRLayer

class XRRenderState:
    layers: Sequence[XRLayer]
    depthNear: float
    depthFar: float
    inlineVerticalFieldOfView: float | None
    baseLayer: XRWebGLLayer | None

class Magnetometer(Sensor):
    def New(self, sensorOptions: MagnetometerSensorOptions | None = {}) -> Magnetometer: ...
    x: float | None
    y: float | None
    z: float | None

class UncalibratedMagnetometer(Sensor):
    def New(self, sensorOptions: MagnetometerSensorOptions | None = {}) -> UncalibratedMagnetometer: ...
    x: float | None
    y: float | None
    z: float | None
    xBias: float | None
    yBias: float | None
    zBias: float | None

class CSSParserRule: ...

class CSSParserAtRule(CSSParserRule):
    def New(self, name: str, prelude: Sequence[CSSToken], body: Sequence[CSSParserRule] | None = None) -> CSSParserAtRule: ...
    name: str
    prelude: Sequence[CSSParserValue]
    body: Sequence[CSSParserRule]

class CSSParserQualifiedRule(CSSParserRule):
    def New(self, prelude: Sequence[CSSToken], body: Sequence[CSSParserRule] | None = None) -> CSSParserQualifiedRule: ...
    prelude: Sequence[CSSParserValue]
    body: Sequence[CSSParserRule]

class CSSParserDeclaration(CSSParserRule):
    def New(self, name: str, body: Sequence[CSSParserRule] | None = None) -> CSSParserDeclaration: ...
    name: str
    body: Sequence[CSSParserValue]

class CSSParserValue: ...

class CSSParserBlock(CSSParserValue):
    def New(self, name: str, body: Sequence[CSSParserValue]) -> CSSParserBlock: ...
    name: str
    body: Sequence[CSSParserValue]

class CSSParserFunction(CSSParserValue):
    def New(self, name: str, args: Sequence[Sequence[CSSParserValue]]) -> CSSParserFunction: ...
    name: str
    args: Sequence[Sequence[CSSParserValue]]

class WEBGL_compressed_texture_pvrtc: ...

class ClipboardEvent(Event):
    def New(self, type: str, eventInitDict: ClipboardEventInit | None = {}) -> ClipboardEvent: ...
    clipboardData: DataTransfer | None

class ClipboardItem:
    def New(self, items: ClipboardItemData, options: ClipboardItemOptions | None = {}) -> ClipboardItem: ...
    presentationStyle: PresentationStyle
    types: Sequence[str]
    def getType(self, type: str) -> Awaitable[Blob]: ...

class Clipboard(EventTarget):
    def read(self) -> Awaitable[ClipboardItems]: ...
    def readText(self) -> Awaitable[str]: ...
    def write(self, data: ClipboardItems) -> Awaitable[None]: ...
    def writeText(self, data: str) -> Awaitable[None]: ...

class EXT_color_buffer_half_float: ...

class OES_texture_half_float: ...

class WEBGL_compressed_texture_astc:
    def getSupportedProfiles(self) -> Sequence[str]: ...

class OES_fbo_render_mipmap: ...

class SyncManager:
    def register(self, tag: str) -> Awaitable[None]: ...
    def getTags(self) -> Awaitable[Sequence[str]]: ...

class SyncEvent(ExtendableEvent):
    def New(self, type: str, init: SyncEventInit) -> SyncEvent: ...
    tag: str
    lastChance: bool

class EXT_color_buffer_float: ...

class Bluetooth(EventTarget, BluetoothDeviceEventHandlers, CharacteristicEventHandlers, ServiceEventHandlers):
    def getAvailability(self) -> Awaitable[bool]: ...
    onavailabilitychanged: EventHandler
    referringDevice: BluetoothDevice | None
    def getDevices(self) -> Awaitable[Sequence[BluetoothDevice]]: ...
    def requestDevice(self, options: RequestDeviceOptions | None = {}) -> Awaitable[BluetoothDevice]: ...

class BluetoothPermissionResult(PermissionStatus):
    devices: Sequence[BluetoothDevice]

class ValueEvent(Event):
    def New(self, type: str, initDict: ValueEventInit | None = {}) -> ValueEvent: ...

class BluetoothDevice(EventTarget, BluetoothDeviceEventHandlers, CharacteristicEventHandlers, ServiceEventHandlers):
    id: str
    name: str | None
    gatt: BluetoothRemoteGATTServer | None
    def forget(self) -> Awaitable[None]: ...
    def watchAdvertisements(self, options: WatchAdvertisementsOptions | None = {}) -> Awaitable[None]: ...
    watchingAdvertisements: bool

class BluetoothManufacturerDataMap: ...

class BluetoothServiceDataMap: ...

class BluetoothAdvertisingEvent(Event):
    def New(self, type: str, init: BluetoothAdvertisingEventInit) -> BluetoothAdvertisingEvent: ...
    device: BluetoothDevice
    uuids: Sequence[UUID]
    name: str | None
    appearance: int | None
    txPower: byte | None
    rssi: byte | None
    manufacturerData: BluetoothManufacturerDataMap
    serviceData: BluetoothServiceDataMap

class BluetoothRemoteGATTServer:
    device: BluetoothDevice
    connected: bool
    def connect(self) -> Awaitable[BluetoothRemoteGATTServer]: ...
    def disconnect(self): ...
    def getPrimaryService(self, service: BluetoothServiceUUID) -> Awaitable[BluetoothRemoteGATTService]: ...
    def getPrimaryServices(self, service: BluetoothServiceUUID | None = None) -> Awaitable[Sequence[BluetoothRemoteGATTService]]: ...

class BluetoothRemoteGATTService(EventTarget, CharacteristicEventHandlers, ServiceEventHandlers):
    device: BluetoothDevice
    uuid: UUID
    isPrimary: bool
    def getCharacteristic(self, characteristic: BluetoothCharacteristicUUID) -> Awaitable[BluetoothRemoteGATTCharacteristic]: ...
    def getCharacteristics(self, characteristic: BluetoothCharacteristicUUID | None = None) -> Awaitable[Sequence[BluetoothRemoteGATTCharacteristic]]: ...
    def getIncludedService(self, service: BluetoothServiceUUID) -> Awaitable[BluetoothRemoteGATTService]: ...
    def getIncludedServices(self, service: BluetoothServiceUUID | None = None) -> Awaitable[Sequence[BluetoothRemoteGATTService]]: ...

class BluetoothRemoteGATTCharacteristic(EventTarget, CharacteristicEventHandlers):
    service: BluetoothRemoteGATTService
    uuid: UUID
    properties: BluetoothCharacteristicProperties
    value: DataView
    def getDescriptor(self, descriptor: BluetoothDescriptorUUID) -> Awaitable[BluetoothRemoteGATTDescriptor]: ...
    def getDescriptors(self, descriptor: BluetoothDescriptorUUID | None = None) -> Awaitable[Sequence[BluetoothRemoteGATTDescriptor]]: ...
    def readValue(self) -> Awaitable[DataView]: ...
    def writeValue(self, value: BufferSource) -> Awaitable[None]: ...
    def writeValueWithResponse(self, value: BufferSource) -> Awaitable[None]: ...
    def writeValueWithoutResponse(self, value: BufferSource) -> Awaitable[None]: ...
    def startNotifications(self) -> Awaitable[BluetoothRemoteGATTCharacteristic]: ...
    def stopNotifications(self) -> Awaitable[BluetoothRemoteGATTCharacteristic]: ...

class BluetoothCharacteristicProperties:
    broadcast: bool
    read: bool
    writeWithoutResponse: bool
    write: bool
    notify: bool
    indicate: bool
    authenticatedSignedWrites: bool
    reliableWrite: bool
    writableAuxiliaries: bool

class BluetoothRemoteGATTDescriptor:
    characteristic: BluetoothRemoteGATTCharacteristic
    uuid: UUID
    value: DataView
    def readValue(self) -> Awaitable[DataView]: ...
    def writeValue(self, value: BufferSource) -> Awaitable[None]: ...

class CharacteristicEventHandlers:
    oncharacteristicvaluechanged: EventHandler

class BluetoothDeviceEventHandlers:
    onadvertisementreceived: EventHandler
    ongattserverdisconnected: EventHandler

class ServiceEventHandlers:
    onserviceadded: EventHandler
    onservicechanged: EventHandler
    onserviceremoved: EventHandler

class BluetoothUUID: ...

class OES_draw_buffers_indexed:
    def enableiOES(self, target: GLenum, index: GLuint): ...
    def disableiOES(self, target: GLenum, index: GLuint): ...
    def blendEquationiOES(self, buf: GLuint, mode: GLenum): ...
    def blendEquationSeparateiOES(self, buf: GLuint, modeRGB: GLenum, modeAlpha: GLenum): ...
    def blendFunciOES(self, buf: GLuint, src: GLenum, dst: GLenum): ...
    def blendFuncSeparateiOES(self, buf: GLuint, srcRGB: GLenum, dstRGB: GLenum, srcAlpha: GLenum, dstAlpha: GLenum): ...
    def colorMaskiOES(self, buf: GLuint, r: GLboolean, g: GLboolean, b: GLboolean, a: GLboolean): ...

class ScrollTimeline(AnimationTimeline):
    def New(self, options: ScrollTimelineOptions | None = {}) -> ScrollTimeline: ...
    source: Element | None
    axis: ScrollAxis

class ViewTimeline(ScrollTimeline):
    def New(self, options: ViewTimelineOptions | None = {}) -> ViewTimeline: ...
    subject: Element
    startOffset: CSSNumericValue
    endOffset: CSSNumericValue

class EXT_texture_norm16: ...

class CompressionStream(GenericTransformStream):
    def New(self, format: str) -> CompressionStream: ...

class DecompressionStream(GenericTransformStream):
    def New(self, format: str) -> DecompressionStream: ...

class SVGFilterElement(SVGElement, SVGURIReference):
    filterUnits: SVGAnimatedEnumeration
    primitiveUnits: SVGAnimatedEnumeration
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class SVGFilterPrimitiveStandardAttributes:
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    result: SVGAnimatedString

class SVGFEBlendElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    mode: SVGAnimatedEnumeration

class SVGFEColorMatrixElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    type: SVGAnimatedEnumeration
    values: SVGAnimatedNumberList

class SVGFEComponentTransferElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString

class SVGComponentTransferFunctionElement(SVGElement):
    type: SVGAnimatedEnumeration
    tableValues: SVGAnimatedNumberList
    slope: SVGAnimatedNumber
    intercept: SVGAnimatedNumber
    amplitude: SVGAnimatedNumber
    exponent: SVGAnimatedNumber
    offset: SVGAnimatedNumber

class SVGFEFuncRElement(SVGComponentTransferFunctionElement): ...

class SVGFEFuncGElement(SVGComponentTransferFunctionElement): ...

class SVGFEFuncBElement(SVGComponentTransferFunctionElement): ...

class SVGFEFuncAElement(SVGComponentTransferFunctionElement): ...

class SVGFECompositeElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    operator: SVGAnimatedEnumeration
    k1: SVGAnimatedNumber
    k2: SVGAnimatedNumber
    k3: SVGAnimatedNumber
    k4: SVGAnimatedNumber

class SVGFEConvolveMatrixElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    orderX: SVGAnimatedInteger
    orderY: SVGAnimatedInteger
    kernelMatrix: SVGAnimatedNumberList
    divisor: SVGAnimatedNumber
    bias: SVGAnimatedNumber
    targetX: SVGAnimatedInteger
    targetY: SVGAnimatedInteger
    edgeMode: SVGAnimatedEnumeration
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber
    preserveAlpha: SVGAnimatedBoolean

class SVGFEDiffuseLightingElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    surfaceScale: SVGAnimatedNumber
    diffuseConstant: SVGAnimatedNumber
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber

class SVGFEDistantLightElement(SVGElement):
    azimuth: SVGAnimatedNumber
    elevation: SVGAnimatedNumber

class SVGFEPointLightElement(SVGElement):
    x: SVGAnimatedNumber
    y: SVGAnimatedNumber
    z: SVGAnimatedNumber

class SVGFESpotLightElement(SVGElement):
    x: SVGAnimatedNumber
    y: SVGAnimatedNumber
    z: SVGAnimatedNumber
    pointsAtX: SVGAnimatedNumber
    pointsAtY: SVGAnimatedNumber
    pointsAtZ: SVGAnimatedNumber
    specularExponent: SVGAnimatedNumber
    limitingConeAngle: SVGAnimatedNumber

class SVGFEDisplacementMapElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    scale: SVGAnimatedNumber
    xChannelSelector: SVGAnimatedEnumeration
    yChannelSelector: SVGAnimatedEnumeration

class SVGFEDropShadowElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    dx: SVGAnimatedNumber
    dy: SVGAnimatedNumber
    stdDeviationX: SVGAnimatedNumber
    stdDeviationY: SVGAnimatedNumber
    def setStdDeviation(self, stdDeviationX: float, stdDeviationY: float): ...

class SVGFEFloodElement(SVGElement, SVGFilterPrimitiveStandardAttributes): ...

class SVGFEGaussianBlurElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    stdDeviationX: SVGAnimatedNumber
    stdDeviationY: SVGAnimatedNumber
    edgeMode: SVGAnimatedEnumeration
    def setStdDeviation(self, stdDeviationX: float, stdDeviationY: float): ...

class SVGFEImageElement(SVGElement, SVGFilterPrimitiveStandardAttributes, SVGURIReference):
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio
    crossOrigin: SVGAnimatedString

class SVGFEMergeElement(SVGElement, SVGFilterPrimitiveStandardAttributes): ...

class SVGFEMergeNodeElement(SVGElement):
    in1: SVGAnimatedString

class SVGFEMorphologyElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    operator: SVGAnimatedEnumeration
    radiusX: SVGAnimatedNumber
    radiusY: SVGAnimatedNumber

class SVGFEOffsetElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    dx: SVGAnimatedNumber
    dy: SVGAnimatedNumber

class SVGFESpecularLightingElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    surfaceScale: SVGAnimatedNumber
    specularConstant: SVGAnimatedNumber
    specularExponent: SVGAnimatedNumber
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber

class SVGFETileElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString

class SVGFETurbulenceElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    baseFrequencyX: SVGAnimatedNumber
    baseFrequencyY: SVGAnimatedNumber
    numOctaves: SVGAnimatedInteger
    seed: SVGAnimatedNumber
    stitchTiles: SVGAnimatedEnumeration
    type: SVGAnimatedEnumeration

class ProximitySensor(Sensor):
    def New(self, sensorOptions: SensorOptions | None = {}) -> ProximitySensor: ...
    distance: float | None
    max: float | None
    near: bool | None

class URLPattern:
    @overload
    def New(self, input: URLPatternInput, baseURL: USVString, options: URLPatternOptions | None = {}) -> URLPattern: ...
    @overload
    def New(self, input: URLPatternInput | None = {}, options: URLPatternOptions | None = {}) -> URLPattern: ...
    def test(self, input: URLPatternInput | None = {}, baseURL: USVString | None = None) -> bool: ...
    def exec(self, input: URLPatternInput | None = {}, baseURL: USVString | None = None) -> URLPatternResult | None: ...
    protocol: USVString
    username: USVString
    password: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString

class ViewTransition:
    def skipTransition(self): ...
    finished: Awaitable[None]
    ready: Awaitable[None]
    updateCallbackDone: Awaitable[None]

class WEBGL_draw_buffers:
    def drawBuffersWEBGL(self, buffers: Sequence[GLenum]): ...

class XRSystem(EventTarget):
    def isSessionSupported(self, mode: XRSessionMode) -> Awaitable[bool]: ...
    def requestSession(self, mode: XRSessionMode, options: XRSessionInit | None = {}) -> Awaitable[XRSession]: ...
    ondevicechange: EventHandler

class XRSpace(EventTarget): ...

class XRReferenceSpace(XRSpace):
    def getOffsetReferenceSpace(self, originOffset: XRRigidTransform) -> XRReferenceSpace: ...
    onreset: EventHandler

class XRBoundedReferenceSpace(XRReferenceSpace):
    boundsGeometry: Sequence[DOMPointReadOnly]

class XRViewport:
    x: int
    y: int
    width: int
    height: int

class XRRigidTransform:
    def New(self, position: DOMPointInit | None = {}, orientation: DOMPointInit | None = {}) -> XRRigidTransform: ...
    position: DOMPointReadOnly
    orientation: DOMPointReadOnly
    matrix: Float32Array
    inverse: XRRigidTransform

class XRPose:
    transform: XRRigidTransform
    linearVelocity: DOMPointReadOnly | None
    angularVelocity: DOMPointReadOnly | None
    emulatedPosition: bool

class XRViewerPose(XRPose):
    views: Sequence[XRView]

class XRInputSourceArray:
    length: int

class XRLayer(EventTarget): ...

class XRWebGLLayer(XRLayer):
    def New(self, session: XRSession, context: XRWebGLRenderingContext, layerInit: XRWebGLLayerInit | None = {}) -> XRWebGLLayer: ...
    antialias: bool
    ignoreDepthValues: bool
    fixedFoveation: float | None
    framebuffer: WebGLFramebuffer | None
    framebufferWidth: int
    framebufferHeight: int
    def getViewport(self, view: XRView) -> XRViewport | None: ...

class XRSessionEvent(Event):
    def New(self, type: str, eventInitDict: XRSessionEventInit) -> XRSessionEvent: ...
    session: XRSession

class XRInputSourceEvent(Event):
    def New(self, type: str, eventInitDict: XRInputSourceEventInit) -> XRInputSourceEvent: ...
    frame: XRFrame
    inputSource: XRInputSource

class XRInputSourcesChangeEvent(Event):
    def New(self, type: str, eventInitDict: XRInputSourcesChangeEventInit) -> XRInputSourcesChangeEvent: ...
    session: XRSession
    added: Sequence[XRInputSource]
    removed: Sequence[XRInputSource]

class XRReferenceSpaceEvent(Event):
    def New(self, type: str, eventInitDict: XRReferenceSpaceEventInit) -> XRReferenceSpaceEvent: ...
    referenceSpace: XRReferenceSpace
    transform: XRRigidTransform | None

class XRPermissionStatus(PermissionStatus):
    granted: Sequence[str]

class GamepadHapticActuator:
    type: GamepadHapticActuatorType
    def canPlayEffectType(self, type: GamepadHapticEffectType) -> bool: ...
    def playEffect(self, type: GamepadHapticEffectType, params: GamepadEffectParameters | None = {}) -> Awaitable[GamepadHapticsResult]: ...
    def pulse(self, value: float, duration: float) -> Awaitable[bool]: ...
    def reset(self) -> Awaitable[GamepadHapticsResult]: ...

class GamepadPose:
    hasOrientation: bool
    hasPosition: bool
    position: Float32Array
    linearVelocity: Float32Array
    linearAcceleration: Float32Array
    orientation: Float32Array
    angularVelocity: Float32Array
    angularAcceleration: Float32Array

class GamepadTouch:
    touchId: int
    surfaceId: octet
    position: Float32Array
    surfaceDimensions: Uint32Array

class LargestContentfulPaint(PerformanceEntry):
    renderTime: DOMHighResTimeStamp
    loadTime: DOMHighResTimeStamp
    size: int
    id: str
    url: str
    element: Element | None
    def toJSON(self) -> object: ...

class AnimationWorkletGlobalScope(WorkletGlobalScope):
    def registerAnimator(self, name: str, animatorCtor: AnimatorInstanceConstructor): ...

class WorkletAnimationEffect:
    def getTiming(self) -> EffectTiming: ...
    def getComputedTiming(self) -> ComputedEffectTiming: ...
    localTime: float | None

class WorkletAnimation(Animation):
    animatorName: str

class WorkletGroupEffect:
    def getChildren(self) -> Sequence[WorkletAnimationEffect]: ...

class FontFace:
    def New(self, family: CSSOMString, source: CSSOMString | BinaryData, descriptors: FontFaceDescriptors | None = {}) -> FontFace: ...
    family: CSSOMString
    style: CSSOMString
    weight: CSSOMString
    stretch: CSSOMString
    unicodeRange: CSSOMString
    variant: CSSOMString
    featureSettings: CSSOMString
    variationSettings: CSSOMString
    display: CSSOMString
    ascentOverride: CSSOMString
    descentOverride: CSSOMString
    lineGapOverride: CSSOMString
    status: FontFaceLoadStatus
    def load(self) -> Awaitable[FontFace]: ...
    loaded: Awaitable[FontFace]
    features: FontFaceFeatures
    variations: FontFaceVariations
    palettes: FontFacePalettes

class FontFaceFeatures: ...

class FontFaceVariationAxis:
    name: str
    axisTag: str
    minimumValue: float
    maximumValue: float
    defaultValue: float

class FontFaceVariations: ...

class FontFacePalette:
    length: int
    usableWithLightBackground: bool
    usableWithDarkBackground: bool

class FontFacePalettes:
    length: int

class FontFaceSetLoadEvent(Event):
    def New(self, type: CSSOMString, eventInitDict: FontFaceSetLoadEventInit | None = {}) -> FontFaceSetLoadEvent: ...
    fontfaces: Sequence[FontFace]

class FontFaceSet(EventTarget):
    def New(self, initialFaces: Sequence[FontFace]) -> FontFaceSet: ...
    def add(self, font: FontFace) -> FontFaceSet: ...
    def delete(self, font: FontFace) -> bool: ...
    def clear(self): ...
    onloading: EventHandler
    onloadingdone: EventHandler
    onloadingerror: EventHandler
    def load(self, font: CSSOMString, text: CSSOMString | None = " ") -> Awaitable[Sequence[FontFace]]: ...
    def check(self, font: CSSOMString, text: CSSOMString | None = " ") -> bool: ...
    ready: Awaitable[FontFaceSet]
    status: FontFaceSetLoadStatus

class FontFaceSource:
    fonts: FontFaceSet

class Keyboard(EventTarget):
    def lock(self, keyCodes: Sequence[str] | None = []) -> Awaitable[None]: ...
    def unlock(self): ...
    def getLayoutMap(self) -> Awaitable[KeyboardLayoutMap]: ...
    onlayoutchange: EventHandler

class MediaSource(EventTarget):
    def New(self) -> MediaSource: ...
    handle: MediaSourceHandle
    sourceBuffers: SourceBufferList
    activeSourceBuffers: SourceBufferList
    readyState: ReadyState
    duration: float
    onsourceopen: EventHandler
    onsourceended: EventHandler
    onsourceclose: EventHandler
    def addSourceBuffer(self, type: str) -> SourceBuffer: ...
    def removeSourceBuffer(self, sourceBuffer: SourceBuffer): ...
    def endOfStream(self, error: EndOfStreamError | None = None): ...
    def setLiveSeekableRange(self, start: float, end: float): ...
    def clearLiveSeekableRange(self): ...

class MediaSourceHandle: ...

class SourceBuffer(EventTarget):
    mode: AppendMode
    updating: bool
    buffered: TimeRanges
    timestampOffset: float
    audioTracks: AudioTrackList
    videoTracks: VideoTrackList
    textTracks: TextTrackList
    appendWindowStart: float
    appendWindowEnd: float
    onupdatestart: EventHandler
    onupdate: EventHandler
    onupdateend: EventHandler
    onerror: EventHandler
    onabort: EventHandler
    def appendBuffer(self, data: BufferSource): ...
    def abort(self): ...
    def changeType(self, type: str): ...
    def remove(self, start: float, end: float): ...

class SourceBufferList(EventTarget):
    length: int
    onaddsourcebuffer: EventHandler
    onremovesourcebuffer: EventHandler

class Touch:
    def New(self, touchInitDict: TouchInit) -> Touch: ...
    identifier: int
    target: EventTarget
    screenX: float
    screenY: float
    clientX: float
    clientY: float
    pageX: float
    pageY: float
    radiusX: float
    radiusY: float
    rotationAngle: float
    force: float
    altitudeAngle: float
    azimuthAngle: float
    touchType: TouchType

class TouchList:
    length: int

class TouchEvent(UIEvent):
    def New(self, type: str, eventInitDict: TouchEventInit | None = {}) -> TouchEvent: ...
    touches: TouchList
    targetTouches: TouchList
    changedTouches: TouchList
    altKey: bool
    metaKey: bool
    ctrlKey: bool
    shiftKey: bool

class ServiceWorker(EventTarget, AbstractWorker):
    scriptURL: USVString
    state: ServiceWorkerState
    onstatechange: EventHandler

class ServiceWorkerContainer(EventTarget):
    controller: ServiceWorker | None
    ready: Awaitable[ServiceWorkerRegistration]
    def register(self, scriptURL: USVString, options: RegistrationOptions | None = {}) -> Awaitable[ServiceWorkerRegistration]: ...
    def getRegistration(self, clientURL: USVString | None = "") -> Awaitable[ServiceWorkerRegistration | None]: ...
    def getRegistrations(self) -> Awaitable[Sequence[ServiceWorkerRegistration]]: ...
    def startMessages(self): ...
    oncontrollerchange: EventHandler
    onmessage: EventHandler
    onmessageerror: EventHandler

class NavigationPreloadManager:
    def enable(self) -> Awaitable[None]: ...
    def disable(self) -> Awaitable[None]: ...
    def setHeaderValue(self, value: ByteString) -> Awaitable[None]: ...
    def getState(self) -> Awaitable[NavigationPreloadState]: ...

class WindowClient(Client):
    visibilityState: DocumentVisibilityState
    focused: bool
    ancestorOrigins: Sequence[USVString]
    def focus(self) -> Awaitable[WindowClient]: ...
    def navigate(self, url: USVString) -> Awaitable[WindowClient | None]: ...

class Clients:
    def get(self, id: str) -> Awaitable[Client | None]: ...
    def matchAll(self, options: ClientQueryOptions | None = {}) -> Awaitable[Sequence[Client]]: ...
    def openWindow(self, url: USVString) -> Awaitable[WindowClient | None]: ...
    def claim(self) -> Awaitable[None]: ...

class ExtendableEvent(Event):
    def New(self, type: str, eventInitDict: ExtendableEventInit | None = {}) -> ExtendableEvent: ...

class FetchEvent(ExtendableEvent):
    def New(self, type: str, eventInitDict: FetchEventInit) -> FetchEvent: ...
    request: Request
    clientId: str
    resultingClientId: str
    replacesClientId: str
    handled: Awaitable[None]
    def respondWith(self, r: Awaitable[Response]): ...

class ExtendableMessageEvent(ExtendableEvent):
    def New(self, type: str, eventInitDict: ExtendableMessageEventInit | None = {}) -> ExtendableMessageEvent: ...
    origin: USVString
    lastEventId: str
    source: Client | ServiceWorker | MessagePort | None
    ports: Sequence[MessagePort]

class Cache:
    def match(self, request: RequestInfo, options: CacheQueryOptions | None = {}) -> Awaitable[Response | None]: ...
    def matchAll(self, request: RequestInfo | None = None, options: CacheQueryOptions | None = {}) -> Awaitable[Sequence[Response]]: ...
    def add(self, request: RequestInfo) -> Awaitable[None]: ...
    def addAll(self, requests: Sequence[RequestInfo]) -> Awaitable[None]: ...
    def put(self, request: RequestInfo, response: Response) -> Awaitable[None]: ...
    def delete(self, request: RequestInfo, options: CacheQueryOptions | None = {}) -> Awaitable[bool]: ...
    def keys(self, request: RequestInfo | None = None, options: CacheQueryOptions | None = {}) -> Awaitable[Sequence[Request]]: ...

class CacheStorage:
    def match(self, request: RequestInfo, options: MultiCacheQueryOptions | None = {}) -> Awaitable[Response | None]: ...
    def has(self, cacheName: str) -> Awaitable[bool]: ...
    def open(self, cacheName: str) -> Awaitable[Cache]: ...
    def delete(self, cacheName: str) -> Awaitable[bool]: ...
    def keys(self) -> Awaitable[Sequence[str]]: ...

class WEBGL_depth_texture: ...

class XRCamera:
    width: int
    height: int

class InterventionReportBody(ReportBody):
    def toJSON(self) -> object: ...
    id: str
    message: str
    sourceFile: str | None
    lineNumber: int | None
    columnNumber: int | None

class ContactAddress:
    def toJSON(self) -> object: ...
    city: str
    country: str
    dependentLocality: str
    organization: str
    phone: str
    postalCode: str
    recipient: str
    region: str
    sortingCode: str
    addressLine: Sequence[str]

class ContactsManager:
    def getProperties(self) -> Awaitable[Sequence[ContactProperty]]: ...
    def select(self, properties: Sequence[ContactProperty], options: ContactsSelectOptions | None = {}) -> Awaitable[Sequence[ContactInfo]]: ...

class WakeLock:
    def request(self, type: WakeLockType | None = "screen") -> Awaitable[WakeLockSentinel]: ...

class WakeLockSentinel(EventTarget):
    released: bool
    type: WakeLockType
    def release(self) -> Awaitable[None]: ...
    onrelease: EventHandler

class TimeEvent(Event):
    view: WindowProxy | None
    detail: int
    def initTimeEvent(self, typeArg: str, viewArg: Window | None, detailArg: int): ...

class SVGAnimationElement(SVGElement, SVGTests):
    targetElement: SVGElement | None
    onbegin: EventHandler
    onend: EventHandler
    onrepeat: EventHandler
    def getStartTime(self) -> float: ...
    def getCurrentTime(self) -> float: ...
    def getSimpleDuration(self) -> float: ...
    def beginElement(self): ...
    def beginElementAt(self, offset: float): ...
    def endElement(self): ...
    def endElementAt(self, offset: float): ...

class SVGAnimateElement(SVGAnimationElement): ...

class SVGSetElement(SVGAnimationElement): ...

class SVGAnimateMotionElement(SVGAnimationElement): ...

class SVGMPathElement(SVGElement, SVGURIReference): ...

class SVGAnimateTransformElement(SVGAnimationElement): ...

class SVGDiscardElement(SVGAnimationElement): ...

class SVGSVGElement(SVGGraphicsElement, SVGFitToViewBox, WindowEventHandlers):
    def pauseAnimations(self): ...
    def unpauseAnimations(self): ...
    def animationsPaused(self) -> bool: ...
    def getCurrentTime(self) -> float: ...
    def setCurrentTime(self, seconds: float): ...
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    currentScale: float
    currentTranslate: DOMPointReadOnly
    def getIntersectionList(self, rect: DOMRectReadOnly, referenceElement: SVGElement | None) -> NodeList: ...
    def getEnclosureList(self, rect: DOMRectReadOnly, referenceElement: SVGElement | None) -> NodeList: ...
    def checkIntersection(self, element: SVGElement, rect: DOMRectReadOnly) -> bool: ...
    def checkEnclosure(self, element: SVGElement, rect: DOMRectReadOnly) -> bool: ...
    def deselectAll(self): ...
    def createSVGNumber(self) -> SVGNumber: ...
    def createSVGLength(self) -> SVGLength: ...
    def createSVGAngle(self) -> SVGAngle: ...
    def createSVGPoint(self) -> DOMPoint: ...
    def createSVGMatrix(self) -> DOMMatrix: ...
    def createSVGRect(self) -> DOMRect: ...
    def createSVGTransform(self) -> SVGTransform: ...
    def createSVGTransformFromMatrix(self, matrix: DOMMatrix2DInit | None = {}) -> SVGTransform: ...
    def getElementById(self, elementId: str) -> Element: ...
    def suspendRedraw(self, maxWaitMilliseconds: int) -> int: ...
    def unsuspendRedraw(self, suspendHandleID: int): ...
    def unsuspendRedrawAll(self): ...
    def forceRedraw(self): ...

class FontMetrics:
    width: float
    advances: Sequence[float]
    boundingBoxLeft: float
    boundingBoxRight: float
    height: float
    emHeightAscent: float
    emHeightDescent: float
    boundingBoxAscent: float
    boundingBoxDescent: float
    fontBoundingBoxAscent: float
    fontBoundingBoxDescent: float
    dominantBaseline: Baseline
    baselines: Sequence[Baseline]
    fonts: Sequence[Font]

class Baseline:
    name: str
    value: float

class Font:
    name: str
    glyphsRendered: int

class PeriodicSyncManager:
    def register(self, tag: str, options: BackgroundSyncOptions | None = {}) -> Awaitable[None]: ...
    def getTags(self) -> Awaitable[Sequence[str]]: ...
    def unregister(self, tag: str) -> Awaitable[None]: ...

class PeriodicSyncEvent(ExtendableEvent):
    def New(self, type: str, init: PeriodicSyncEventInit) -> PeriodicSyncEvent: ...
    tag: str

class MediaList:
    length: int
    def appendMedium(self, medium: CSSOMString): ...
    def deleteMedium(self, medium: CSSOMString): ...

class StyleSheet:
    type: CSSOMString
    href: USVString | None
    ownerNode: Element | ProcessingInstruction | None
    parentStyleSheet: CSSStyleSheet | None
    title: str | None
    media: MediaList
    disabled: bool

class CSSStyleSheet(StyleSheet):
    def New(self, options: CSSStyleSheetInit | None = {}) -> CSSStyleSheet: ...
    ownerRule: CSSRule | None
    cssRules: CSSRuleList
    def insertRule(self, rule: CSSOMString, index: int | None = 0) -> int: ...
    def deleteRule(self, index: int): ...
    def replace(self, text: USVString) -> Awaitable[CSSStyleSheet]: ...
    def replaceSync(self, text: USVString): ...
    rules: CSSRuleList
    def addRule(self, selector: str | None = "undefined", style: str | None = "undefined", index: int | None = None) -> int: ...
    def removeRule(self, index: int | None = 0): ...

class StyleSheetList:
    length: int

class LinkStyle:
    sheet: CSSStyleSheet | None

class CSSRuleList:
    length: int

class CSSGroupingRule(CSSRule):
    cssRules: CSSRuleList
    def insertRule(self, rule: CSSOMString, index: int | None = 0) -> int: ...
    def deleteRule(self, index: int): ...

class CSSPageRule(CSSGroupingRule):
    selectorText: CSSOMString
    style: CSSStyleDeclaration

class CSSMarginRule(CSSRule):
    name: CSSOMString
    style: CSSStyleDeclaration

class CSSNamespaceRule(CSSRule):
    namespaceURI: CSSOMString
    prefix: CSSOMString

class CSSStyleDeclaration:
    cssText: CSSOMString
    length: int
    def getPropertyValue(self, property: CSSOMString) -> CSSOMString: ...
    def getPropertyPriority(self, property: CSSOMString) -> CSSOMString: ...
    def setProperty(self, property: CSSOMString, value: CSSOMString, priority: CSSOMString | None = ""): ...
    def removeProperty(self, property: CSSOMString) -> CSSOMString: ...
    parentRule: CSSRule | None
    cssFloat: CSSOMString

class SVGElement(Element, ElementCSSInlineStyle, GlobalEventHandlers, SVGElementInstance, HTMLOrSVGElement):
    className: SVGAnimatedString
    ownerSVGElement: SVGSVGElement | None
    viewportElement: SVGElement | None

class CrashReportBody(ReportBody):
    def toJSON(self) -> object: ...
    reason: str | None

class DeviceOrientationEvent(Event):
    def New(self, type: str, eventInitDict: DeviceOrientationEventInit | None = {}) -> DeviceOrientationEvent: ...
    alpha: float | None
    beta: float | None
    gamma: float | None
    absolute: bool

class DeviceMotionEventAcceleration:
    x: float | None
    y: float | None
    z: float | None

class DeviceMotionEventRotationRate:
    alpha: float | None
    beta: float | None
    gamma: float | None

class DeviceMotionEvent(Event):
    def New(self, type: str, eventInitDict: DeviceMotionEventInit | None = {}) -> DeviceMotionEvent: ...
    acceleration: DeviceMotionEventAcceleration | None
    accelerationIncludingGravity: DeviceMotionEventAcceleration | None
    rotationRate: DeviceMotionEventRotationRate | None
    interval: float

class CropTarget: ...

class BrowserCaptureMediaStreamTrack(MediaStreamTrack):
    def cropTo(self, cropTarget: CropTarget | None) -> Awaitable[None]: ...
    def clone(self) -> BrowserCaptureMediaStreamTrack: ...

class SVGClipPathElement(SVGElement):
    clipPathUnits: SVGAnimatedEnumeration
    transform: SVGAnimatedTransformList

class SVGMaskElement(SVGElement):
    maskUnits: SVGAnimatedEnumeration
    maskContentUnits: SVGAnimatedEnumeration
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class VirtualKeyboard(EventTarget):
    def show(self): ...
    def hide(self): ...
    boundingRect: DOMRect
    overlaysContent: bool
    ongeometrychange: EventHandler

class FragmentDirective: ...

class Module:
    def New(self, bytes: BufferSource) -> Module: ...

class Instance:
    def New(self, module: Module, importObject: object | None = None) -> Instance: ...
    exports: object

class Memory:
    def New(self, descriptor: MemoryDescriptor) -> Memory: ...
    def grow(self, delta: int) -> int: ...
    buffer: ArrayBuffer

class Table:
    length: int

class Global: ...

class PictureInPictureWindow(EventTarget):
    width: int
    height: int
    onresize: EventHandler

class PictureInPictureEvent(Event):
    def New(self, type: str, eventInitDict: PictureInPictureEventInit) -> PictureInPictureEvent: ...
    pictureInPictureWindow: PictureInPictureWindow

class PointerEvent(MouseEvent):
    def New(self, type: str, eventInitDict: PointerEventInit | None = {}) -> PointerEvent: ...
    pointerId: int
    width: float
    height: float
    pressure: float
    tangentialPressure: float
    tiltX: int
    tiltY: int
    twist: int
    altitudeAngle: float
    azimuthAngle: float
    pointerType: str
    isPrimary: bool
    def getCoalescedEvents(self) -> Sequence[PointerEvent]: ...
    def getPredictedEvents(self) -> Sequence[PointerEvent]: ...

class ContentVisibilityAutoStateChangedEvent(Event):
    def New(self, type: str, eventInitDict: ContentVisibilityAutoStateChangedEventInit | None = {}) -> ContentVisibilityAutoStateChangedEvent: ...
    skipped: bool

class KeyboardLayoutMap: ...

class Gyroscope(Sensor):
    def New(self, sensorOptions: GyroscopeSensorOptions | None = {}) -> Gyroscope: ...
    x: float | None
    y: float | None
    z: float | None

class WEBGL_compressed_texture_s3tc_srgb: ...

class HTMLModelElement(HTMLElement): ...

class GroupEffect:
    def New(self, children: Sequence[AnimationEffect], timing: float | EffectTiming | None = {}) -> GroupEffect: ...
    children: AnimationNodeList
    firstChild: AnimationEffect | None
    lastChild: AnimationEffect | None
    def clone(self) -> GroupEffect: ...
    def prepend(self, effects: AnimationEffect | None = None): ...
    def append(self, effects: AnimationEffect | None = None): ...

class AnimationNodeList:
    length: int

class SequenceEffect(GroupEffect):
    def New(self, children: Sequence[AnimationEffect], timing: float | EffectTiming | None = {}) -> SequenceEffect: ...
    def clone(self) -> SequenceEffect: ...

class AnimationPlaybackEvent(Event):
    def New(self, type: str, eventInitDict: AnimationPlaybackEventInit | None = {}) -> AnimationPlaybackEvent: ...
    currentTime: CSSNumberish | None
    timelineTime: CSSNumberish | None

class Blob:
    def New(self, blobParts: Sequence[BlobPart] | None = None, options: BlobPropertyBag | None = {}) -> Blob: ...
    size: int
    type: str
    def slice(self, start: int | None = None, end: int | None = None, contentType: str | None = None) -> Blob: ...
    def stream(self) -> ReadableStream: ...
    def text(self) -> Awaitable[USVString]: ...
    def arrayBuffer(self) -> Awaitable[ArrayBuffer]: ...

class FileList:
    length: int

class FileReader(EventTarget):
    def New(self) -> FileReader: ...
    def readAsArrayBuffer(self, blob: Blob): ...
    def readAsBinaryString(self, blob: Blob): ...
    def readAsText(self, blob: Blob, encoding: str | None = None): ...
    def readAsDataURL(self, blob: Blob): ...
    def abort(self): ...
    readyState: int
    result: str | ArrayBuffer | None
    error: DOMException | None
    onloadstart: EventHandler
    onprogress: EventHandler
    onload: EventHandler
    onabort: EventHandler
    onerror: EventHandler
    onloadend: EventHandler

class FileReaderSync:
    def New(self) -> FileReaderSync: ...
    def readAsArrayBuffer(self, blob: Blob) -> ArrayBuffer: ...
    def readAsBinaryString(self, blob: Blob) -> str: ...
    def readAsText(self, blob: Blob, encoding: str | None = None) -> str: ...
    def readAsDataURL(self, blob: Blob) -> str: ...

class NamedFlowMap: ...

class NamedFlow(EventTarget):
    name: CSSOMString
    overset: bool
    def getRegions(self) -> Sequence[Element]: ...
    firstEmptyRegionIndex: short
    def getContent(self) -> Sequence[Node]: ...
    def getRegionsByContent(self, node: Node) -> Sequence[Element]: ...

class Region:
    regionOverset: CSSOMString
    def getRegionFlowRanges(self) -> Sequence[Range]: ...

class PaymentRequest(EventTarget):
    def New(self, methodData: Sequence[PaymentMethodData], details: PaymentDetailsInit) -> PaymentRequest: ...
    def show(self, detailsPromise: Awaitable[PaymentDetailsUpdate] | None = None) -> Awaitable[PaymentResponse]: ...
    def abort(self) -> Awaitable[None]: ...
    def canMakePayment(self) -> Awaitable[bool]: ...
    id: str
    onpaymentmethodchange: EventHandler

class PaymentResponse(EventTarget):
    def toJSON(self) -> object: ...
    requestId: str
    methodName: str
    details: object
    def complete(self, result: PaymentComplete | None = "unknown", details: PaymentCompleteDetails | None = {}) -> Awaitable[None]: ...
    def retry(self, errorFields: PaymentValidationErrors | None = {}) -> Awaitable[None]: ...

class PaymentMethodChangeEvent(PaymentRequestUpdateEvent):
    def New(self, type: str, eventInitDict: PaymentMethodChangeEventInit | None = {}) -> PaymentMethodChangeEvent: ...
    methodName: str
    methodDetails: object | None

class PaymentRequestUpdateEvent(Event):
    def New(self, type: str, eventInitDict: PaymentRequestUpdateEventInit | None = {}) -> PaymentRequestUpdateEvent: ...
    def updateWith(self, detailsPromise: Awaitable[PaymentDetailsUpdate]): ...

class OES_texture_float_linear: ...

class Crypto:
    subtle: SubtleCrypto
    def getRandomValues(self, array: ArrayBufferView) -> ArrayBufferView: ...
    def randomUUID(self) -> str: ...

class CryptoKey:
    type: KeyType
    extractable: bool
    algorithm: object
    usages: object

class SubtleCrypto:
    def deriveBits(self, algorithm: AlgorithmIdentifier, baseKey: CryptoKey, length: int) -> Awaitable[ArrayBuffer]: ...
    def importKey(self, format: KeyFormat, keyData: BufferSource | JsonWebKey, algorithm: AlgorithmIdentifier, extractable: bool, keyUsages: Sequence[KeyUsage]) -> Awaitable[CryptoKey]: ...
    def unwrapKey(self, format: KeyFormat, wrappedKey: BufferSource, unwrappingKey: CryptoKey, unwrapAlgorithm: AlgorithmIdentifier, unwrappedKeyAlgorithm: AlgorithmIdentifier, extractable: bool, keyUsages: Sequence[KeyUsage]) -> Awaitable[CryptoKey]: ...

class NDEFMessage:
    def New(self, messageInit: NDEFMessageInit) -> NDEFMessage: ...
    records: Sequence[NDEFRecord]

class NDEFRecord:
    def New(self, recordInit: NDEFRecordInit) -> NDEFRecord: ...
    recordType: USVString
    mediaType: USVString | None
    id: USVString | None
    data: DataView
    encoding: USVString | None
    lang: USVString | None
    def toRecords(self) -> Sequence[NDEFRecord]: ...

class NDEFReader(EventTarget):
    def New(self) -> NDEFReader: ...
    onreading: EventHandler
    onreadingerror: EventHandler
    def scan(self, options: NDEFScanOptions | None = {}) -> Awaitable[None]: ...
    def write(self, message: NDEFMessageSource, options: NDEFWriteOptions | None = {}) -> Awaitable[None]: ...
    def makeReadOnly(self, options: NDEFMakeReadOnlyOptions | None = {}) -> Awaitable[None]: ...

class NDEFReadingEvent(Event):
    def New(self, type: str, readingEventInitDict: NDEFReadingEventInit) -> NDEFReadingEvent: ...
    serialNumber: str
    message: NDEFMessage

class CSSPropertyRule(CSSRule):
    name: CSSOMString
    syntax: CSSOMString
    inherits: bool
    initialValue: CSSOMString | None

class ARIAMixin:
    role: str | None
    ariaActiveDescendantElement: Element | None
    ariaAtomic: str | None
    ariaAutoComplete: str | None
    ariaBusy: str | None
    ariaChecked: str | None
    ariaColCount: str | None
    ariaColIndex: str | None
    ariaColIndexText: str | None
    ariaColSpan: str | None
    ariaControlsElements: Sequence[Element]
    ariaCurrent: str | None
    ariaDescribedByElements: Sequence[Element]
    ariaDescription: str | None
    ariaDetailsElements: Sequence[Element]
    ariaDisabled: str | None
    ariaErrorMessageElements: Sequence[Element]
    ariaExpanded: str | None
    ariaFlowToElements: Sequence[Element]
    ariaHasPopup: str | None
    ariaHidden: str | None
    ariaInvalid: str | None
    ariaKeyShortcuts: str | None
    ariaLabel: str | None
    ariaLabelledByElements: Sequence[Element]
    ariaLevel: str | None
    ariaLive: str | None
    ariaModal: str | None
    ariaMultiLine: str | None
    ariaMultiSelectable: str | None
    ariaOrientation: str | None
    ariaOwnsElements: Sequence[Element]
    ariaPlaceholder: str | None
    ariaPosInSet: str | None
    ariaPressed: str | None
    ariaReadOnly: str | None
    ariaRequired: str | None
    ariaRoleDescription: str | None
    ariaRowCount: str | None
    ariaRowIndex: str | None
    ariaRowIndexText: str | None
    ariaRowSpan: str | None
    ariaSelected: str | None
    ariaSetSize: str | None
    ariaSort: str | None
    ariaValueMax: str | None
    ariaValueMin: str | None
    ariaValueNow: str | None
    ariaValueText: str | None

class SVGGraphicsElement(SVGElement, SVGTests):
    transform: SVGAnimatedTransformList
    def getBBox(self, options: SVGBoundingBoxOptions | None = {}) -> DOMRect: ...
    def getCTM(self) -> DOMMatrix | None: ...
    def getScreenCTM(self) -> DOMMatrix | None: ...

class SVGGeometryElement(SVGGraphicsElement):
    pathLength: SVGAnimatedNumber
    def isPointInFill(self, point: DOMPointInit | None = {}) -> bool: ...
    def isPointInStroke(self, point: DOMPointInit | None = {}) -> bool: ...
    def getTotalLength(self) -> float: ...
    def getPointAtLength(self, distance: float) -> DOMPoint: ...

class SVGNumber:
    value: float

class SVGLength:
    unitType: int
    value: float
    valueInSpecifiedUnits: float
    valueAsString: str
    def newValueSpecifiedUnits(self, unitType: int, valueInSpecifiedUnits: float): ...
    def convertToSpecifiedUnits(self, unitType: int): ...

class SVGAngle:
    unitType: int
    value: float
    valueInSpecifiedUnits: float
    valueAsString: str
    def newValueSpecifiedUnits(self, unitType: int, valueInSpecifiedUnits: float): ...
    def convertToSpecifiedUnits(self, unitType: int): ...

class SVGNumberList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: SVGNumber) -> SVGNumber: ...
    def insertItemBefore(self, newItem: SVGNumber, index: int) -> SVGNumber: ...
    def replaceItem(self, newItem: SVGNumber, index: int) -> SVGNumber: ...
    def removeItem(self, index: int) -> SVGNumber: ...
    def appendItem(self, newItem: SVGNumber) -> SVGNumber: ...

class SVGLengthList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: SVGLength) -> SVGLength: ...
    def insertItemBefore(self, newItem: SVGLength, index: int) -> SVGLength: ...
    def replaceItem(self, newItem: SVGLength, index: int) -> SVGLength: ...
    def removeItem(self, index: int) -> SVGLength: ...
    def appendItem(self, newItem: SVGLength) -> SVGLength: ...

class SVGStringList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: str) -> str: ...
    def insertItemBefore(self, newItem: str, index: int) -> str: ...
    def replaceItem(self, newItem: str, index: int) -> str: ...
    def removeItem(self, index: int) -> str: ...
    def appendItem(self, newItem: str) -> str: ...

class SVGAnimatedBoolean:
    baseVal: bool
    animVal: bool

class SVGAnimatedEnumeration:
    baseVal: int
    animVal: int

class SVGAnimatedInteger:
    baseVal: int
    animVal: int

class SVGAnimatedNumber:
    baseVal: float
    animVal: float

class SVGAnimatedLength:
    baseVal: SVGLength
    animVal: SVGLength

class SVGAnimatedAngle:
    baseVal: SVGAngle
    animVal: SVGAngle

class SVGAnimatedString:
    baseVal: str
    animVal: str

class SVGAnimatedRect:
    baseVal: DOMRect
    animVal: DOMRectReadOnly

class SVGAnimatedNumberList:
    baseVal: SVGNumberList
    animVal: SVGNumberList

class SVGAnimatedLengthList:
    baseVal: SVGLengthList
    animVal: SVGLengthList

class SVGUnitTypes: ...

class SVGTests:
    requiredExtensions: SVGStringList
    systemLanguage: SVGStringList

class SVGFitToViewBox:
    viewBox: SVGAnimatedRect
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio

class SVGURIReference:
    href: SVGAnimatedString

class SVGGElement(SVGGraphicsElement): ...

class SVGDefsElement(SVGGraphicsElement): ...

class SVGDescElement(SVGElement): ...

class SVGMetadataElement(SVGElement): ...

class SVGTitleElement(SVGElement): ...

class SVGSymbolElement(SVGGraphicsElement, SVGFitToViewBox): ...

class SVGUseElement(SVGGraphicsElement, SVGURIReference):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    instanceRoot: SVGElement | None
    animatedInstanceRoot: SVGElement | None

class SVGUseElementShadowRoot(ShadowRoot): ...

class SVGElementInstance:
    correspondingElement: SVGElement | None
    correspondingUseElement: SVGUseElement | None

class ShadowAnimation(Animation):
    def New(self, source: Animation, newTarget: Element | CSSPseudoElement) -> ShadowAnimation: ...
    sourceAnimation: Animation

class SVGSwitchElement(SVGGraphicsElement): ...

class GetSVGDocument:
    def getSVGDocument(self) -> Document: ...

class SVGStyleElement(SVGElement, LinkStyle):
    type: str
    media: str
    title: str

class SVGTransform:
    type: int
    matrix: DOMMatrix
    angle: float
    def setMatrix(self, matrix: DOMMatrix2DInit | None = {}): ...
    def setTranslate(self, tx: float, ty: float): ...
    def setScale(self, sx: float, sy: float): ...
    def setRotate(self, angle: float, cx: float, cy: float): ...
    def setSkewX(self, angle: float): ...
    def setSkewY(self, angle: float): ...

class SVGTransformList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: SVGTransform) -> SVGTransform: ...
    def insertItemBefore(self, newItem: SVGTransform, index: int) -> SVGTransform: ...
    def replaceItem(self, newItem: SVGTransform, index: int) -> SVGTransform: ...
    def removeItem(self, index: int) -> SVGTransform: ...
    def appendItem(self, newItem: SVGTransform) -> SVGTransform: ...
    def createSVGTransformFromMatrix(self, matrix: DOMMatrix2DInit | None = {}) -> SVGTransform: ...
    def consolidate(self) -> SVGTransform | None: ...

class SVGAnimatedTransformList:
    baseVal: SVGTransformList
    animVal: SVGTransformList

class SVGPreserveAspectRatio:
    align: int
    meetOrSlice: int

class SVGAnimatedPreserveAspectRatio:
    baseVal: SVGPreserveAspectRatio
    animVal: SVGPreserveAspectRatio

class SVGPathElement(SVGGeometryElement): ...

class SVGRectElement(SVGGeometryElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    rx: SVGAnimatedLength
    ry: SVGAnimatedLength

class SVGCircleElement(SVGGeometryElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    r: SVGAnimatedLength

class SVGEllipseElement(SVGGeometryElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    rx: SVGAnimatedLength
    ry: SVGAnimatedLength

class SVGLineElement(SVGGeometryElement):
    x1: SVGAnimatedLength
    y1: SVGAnimatedLength
    x2: SVGAnimatedLength
    y2: SVGAnimatedLength

class SVGAnimatedPoints:
    points: SVGPointList
    animatedPoints: SVGPointList

class SVGPointList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: DOMPoint) -> DOMPoint: ...
    def insertItemBefore(self, newItem: DOMPoint, index: int) -> DOMPoint: ...
    def replaceItem(self, newItem: DOMPoint, index: int) -> DOMPoint: ...
    def removeItem(self, index: int) -> DOMPoint: ...
    def appendItem(self, newItem: DOMPoint) -> DOMPoint: ...

class SVGPolylineElement(SVGGeometryElement, SVGAnimatedPoints): ...

class SVGPolygonElement(SVGGeometryElement, SVGAnimatedPoints): ...

class SVGTextContentElement(SVGGraphicsElement):
    textLength: SVGAnimatedLength
    lengthAdjust: SVGAnimatedEnumeration
    def getNumberOfChars(self) -> int: ...
    def getComputedTextLength(self) -> float: ...
    def getSubStringLength(self, charnum: int, nchars: int) -> float: ...
    def getStartPositionOfChar(self, charnum: int) -> DOMPoint: ...
    def getEndPositionOfChar(self, charnum: int) -> DOMPoint: ...
    def getExtentOfChar(self, charnum: int) -> DOMRect: ...
    def getRotationOfChar(self, charnum: int) -> float: ...
    def getCharNumAtPosition(self, point: DOMPointInit | None = {}) -> int: ...
    def selectSubString(self, charnum: int, nchars: int): ...

class SVGTextPositioningElement(SVGTextContentElement):
    x: SVGAnimatedLengthList
    y: SVGAnimatedLengthList
    dx: SVGAnimatedLengthList
    dy: SVGAnimatedLengthList
    rotate: SVGAnimatedNumberList

class SVGTextElement(SVGTextPositioningElement): ...

class SVGTSpanElement(SVGTextPositioningElement): ...

class SVGTextPathElement(SVGTextContentElement, SVGURIReference):
    startOffset: SVGAnimatedLength
    method: SVGAnimatedEnumeration
    spacing: SVGAnimatedEnumeration

class SVGImageElement(SVGGraphicsElement, SVGURIReference):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio
    crossOrigin: str | None

class SVGForeignObjectElement(SVGGraphicsElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class SVGMarkerElement(SVGElement, SVGFitToViewBox):
    refX: SVGAnimatedLength
    refY: SVGAnimatedLength
    markerUnits: SVGAnimatedEnumeration
    markerWidth: SVGAnimatedLength
    markerHeight: SVGAnimatedLength
    orientType: SVGAnimatedEnumeration
    orientAngle: SVGAnimatedAngle
    orient: str
    def setOrientToAuto(self): ...
    def setOrientToAngle(self, angle: SVGAngle): ...

class SVGGradientElement(SVGElement, SVGURIReference):
    gradientUnits: SVGAnimatedEnumeration
    gradientTransform: SVGAnimatedTransformList
    spreadMethod: SVGAnimatedEnumeration

class SVGLinearGradientElement(SVGGradientElement):
    x1: SVGAnimatedLength
    y1: SVGAnimatedLength
    x2: SVGAnimatedLength
    y2: SVGAnimatedLength

class SVGRadialGradientElement(SVGGradientElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    r: SVGAnimatedLength
    fx: SVGAnimatedLength
    fy: SVGAnimatedLength
    fr: SVGAnimatedLength

class SVGStopElement(SVGElement):
    offset: SVGAnimatedNumber

class SVGPatternElement(SVGElement, SVGFitToViewBox, SVGURIReference):
    patternUnits: SVGAnimatedEnumeration
    patternContentUnits: SVGAnimatedEnumeration
    patternTransform: SVGAnimatedTransformList
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class SVGScriptElement(SVGElement, SVGURIReference):
    type: str
    crossOrigin: str | None

class SVGAElement(SVGGraphicsElement, SVGURIReference):
    target: SVGAnimatedString
    download: str
    ping: USVString
    rel: str
    relList: DOMTokenList
    hreflang: str
    type: str
    text: str
    referrerPolicy: str
    origin: USVString
    protocol: USVString
    username: USVString
    password: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString

class SVGViewElement(SVGElement, SVGFitToViewBox): ...

class Navigation(EventTarget):
    def entries(self) -> Sequence[NavigationHistoryEntry]: ...
    currentEntry: NavigationHistoryEntry | None
    def updateCurrentEntry(self, options: NavigationUpdateCurrentEntryOptions): ...
    transition: NavigationTransition | None
    canGoBack: bool
    canGoForward: bool
    def navigate(self, url: USVString, options: NavigationNavigateOptions | None = {}) -> NavigationResult: ...
    def reload(self, options: NavigationReloadOptions | None = {}) -> NavigationResult: ...
    def traverseTo(self, key: str, options: NavigationOptions | None = {}) -> NavigationResult: ...
    def back(self, options: NavigationOptions | None = {}) -> NavigationResult: ...
    def forward(self, options: NavigationOptions | None = {}) -> NavigationResult: ...
    onnavigate: EventHandler
    onnavigatesuccess: EventHandler
    onnavigateerror: EventHandler
    oncurrententrychange: EventHandler

class NavigationCurrentEntryChangeEvent(Event):
    def New(self, type: str, eventInit: NavigationCurrentEntryChangeEventInit) -> NavigationCurrentEntryChangeEvent: ...
    navigationType: NavigationType | None
    from_: NavigationHistoryEntry

class NavigationTransition:
    navigationType: NavigationType
    from_: NavigationHistoryEntry
    finished: Awaitable[None]

class NavigateEvent(Event):
    def New(self, type: str, eventInit: NavigateEventInit) -> NavigateEvent: ...
    navigationType: NavigationType
    destination: NavigationDestination
    canIntercept: bool
    userInitiated: bool
    hashChange: bool
    signal: AbortSignal
    formData: FormData | None
    downloadRequest: str | None
    def intercept(self, options: NavigationInterceptOptions | None = {}): ...
    def scroll(self): ...

class NavigationDestination:
    url: USVString
    key: str | None
    id: str | None
    index: int
    sameDocument: bool

class NavigationHistoryEntry(EventTarget):
    url: USVString | None
    key: str
    id: str
    index: int
    sameDocument: bool
    ondispose: EventHandler



document: Document
window: Window
navigator: Navigator

