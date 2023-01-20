class ScrollLogicalPosition:
    start = "start"
    center = "center"
    end = "end"
    nearest = "nearest"


class RequestDestination:
    empty_ = ""
    audio = "audio"
    audioworklet = "audioworklet"
    document = "document"
    embed = "embed"
    font = "font"
    image = "image"
    manifest = "manifest"
    object = "object"
    paintworklet = "paintworklet"
    report = "report"
    script = "script"
    sharedworker = "sharedworker"
    style = "style"
    track = "track"
    video = "video"
    worker = "worker"
    xslt = "xslt"


class RequestMode:
    same_origin = "same-origin"
    no_cors = "no-cors"
    cors = "cors"
    navigate = "navigate"


class RequestCredentials:
    omit = "omit"
    same_origin = "same-origin"
    include = "include"


class RequestCache:
    default = "default"
    no_store = "no-store"
    reload = "reload"
    no_cache = "no-cache"
    force_cache = "force-cache"
    only_if_cached = "only-if-cached"


class RequestRedirect:
    follow = "follow"
    error = "error"
    manual = "manual"


class ReferrerPolicy:
    empty_ = ""
    no_referrer = "no-referrer"
    no_referrer_when_downgrade = "no-referrer-when-downgrade"
    origin = "origin"
    origin_when_cross_origin = "origin-when-cross-origin"
    unsafe_url = "unsafe-url"
    same_origin = "same-origin"
    strict_origin = "strict-origin"
    strict_origin_when_cross_origin = "strict-origin-when-cross-origin"


class AudioContextState:
    suspended = "suspended"
    running = "running"
    closed = "closed"


class SourceBufferAppendMode:
    segments = "segments"
    sequence = "sequence"


class MediaKeysRequirement:
    required = "required"
    optional = "optional"
    not_allowed = "not-allowed"


class AuthenticatorAttachment:
    platform = "platform"
    cross_platform = "cross-platform"


class AttestationConveyancePreference:
    none = "none"
    indirect = "indirect"
    direct = "direct"


class UserVerificationRequirement:
    required = "required"
    preferred = "preferred"
    discouraged = "discouraged"


class PublicKeyCredentialType:
    public_key = "public-key"


class AuthenticatorTransport:
    usb = "usb"
    nfc = "nfc"
    ble = "ble"


class VideoFacingModeEnum:
    user = "user"
    environment = "environment"
    left = "left"
    right = "right"


class MediaSourceEnum:
    camera = "camera"
    screen = "screen"
    application = "application"
    window = "window"
    browser = "browser"
    microphone = "microphone"
    audioCapture = "audioCapture"
    other = "other"


class MediaStreamTrackState:
    live = "live"
    ended = "ended"


class NavigationType:
    navigate = "navigate"
    reload = "reload"
    back_forward = "back_forward"
    prerender = "prerender"


class GridDeclaration:
    explicit = "explicit"
    implicit = "implicit"


class GridTrackState:
    static = "static"
    repeat = "repeat"
    removed = "removed"


class RTCLifecycleEvent:
    initialized = "initialized"
    icegatheringstatechange = "icegatheringstatechange"
    iceconnectionstatechange = "iceconnectionstatechange"


class MediaKeySystemStatus:
    available = "available"
    api_disabled = "api-disabled"
    cdm_disabled = "cdm-disabled"
    cdm_not_supported = "cdm-not-supported"
    cdm_not_installed = "cdm-not-installed"
    cdm_created = "cdm-created"


class FrameType:
    auxiliary = "auxiliary"
    top_level = "top-level"
    nested = "nested"
    none = "none"


class BiquadFilterType:
    lowpass = "lowpass"
    highpass = "highpass"
    bandpass = "bandpass"
    lowshelf = "lowshelf"
    highshelf = "highshelf"
    peaking = "peaking"
    notch = "notch"
    allpass = "allpass"


class FetchState:
    requesting = "requesting"
    responding = "responding"
    aborted = "aborted"
    errored = "errored"
    complete = "complete"


class PCObserverStateType:
    None_ = "None"
    IceConnectionState = "IceConnectionState"
    IceGatheringState = "IceGatheringState"
    SignalingState = "SignalingState"


class OscillatorType:
    sine = "sine"
    square = "square"
    sawtooth = "sawtooth"
    triangle = "triangle"
    custom = "custom"


class PermissionState:
    granted = "granted"
    denied = "denied"
    prompt = "prompt"


class VREye:
    left = "left"
    right = "right"


class IDBRequestReadyState:
    pending = "pending"
    done = "done"


class MediaDeviceKind:
    audioinput = "audioinput"
    audiooutput = "audiooutput"
    videoinput = "videoinput"


class SpeechRecognitionErrorCode:
    no_speech = "no-speech"
    aborted = "aborted"
    audio_capture = "audio-capture"
    network = "network"
    not_allowed = "not-allowed"
    service_not_allowed = "service-not-allowed"
    bad_grammar = "bad-grammar"
    language_not_supported = "language-not-supported"


class BrowserFindCaseSensitivity:
    case_sensitive = "case-sensitive"
    case_insensitive = "case-insensitive"


class BrowserFindDirection:
    forward = "forward"
    backward = "backward"


class EndingTypes:
    transparent = "transparent"
    native = "native"


class PaymentComplete:
    success = "success"
    fail = "fail"
    unknown = "unknown"


class CaretChangedReason:
    visibilitychange = "visibilitychange"
    updateposition = "updateposition"
    longpressonemptycontent = "longpressonemptycontent"
    taponcaret = "taponcaret"
    presscaret = "presscaret"
    releasecaret = "releasecaret"
    scroll = "scroll"


class ScrollRestoration:
    auto = "auto"
    manual = "manual"


class MIDIPortType:
    input = "input"
    output = "output"


class MIDIPortDeviceState:
    disconnected = "disconnected"
    connected = "connected"


class MIDIPortConnectionState:
    open = "open"
    closed = "closed"
    pending = "pending"


class PresentationConnectionClosedReason:
    error = "error"
    closed = "closed"
    wentaway = "wentaway"


class MediaSourceReadyState:
    closed = "closed"
    open = "open"
    ended = "ended"


class MediaSourceEndOfStreamError:
    network = "network"
    decode = "decode"


class NotificationPermission:
    default = "default"
    denied = "denied"
    granted = "granted"


class NotificationDirection:
    auto = "auto"
    ltr = "ltr"
    rtl = "rtl"


class ScrollBehavior:
    auto = "auto"
    instant = "instant"
    smooth = "smooth"


class StorageType:
    persistent = "persistent"
    temporary = "temporary"
    default = "default"


class FlexLineGrowthState:
    unchanged = "unchanged"
    shrinking = "shrinking"
    growing = "growing"


class CSSBoxType:
    margin = "margin"
    border = "border"
    padding = "padding"
    content = "content"


class DOMRequestReadyState:
    pending = "pending"
    done = "done"


class ResponseType:
    basic = "basic"
    cors = "cors"
    default = "default"
    error = "error"
    opaque = "opaque"
    opaqueredirect = "opaqueredirect"


class TextTrackKind:
    subtitles = "subtitles"
    captions = "captions"
    descriptions = "descriptions"
    chapters = "chapters"
    metadata = "metadata"


class TextTrackMode:
    disabled = "disabled"
    hidden = "hidden"
    showing = "showing"


class RTCSignalingState:
    stable = "stable"
    have_local_offer = "have-local-offer"
    have_remote_offer = "have-remote-offer"
    have_local_pranswer = "have-local-pranswer"
    have_remote_pranswer = "have-remote-pranswer"
    closed = "closed"


class RTCIceGatheringState:
    new = "new"
    gathering = "gathering"
    complete = "complete"


class RTCIceConnectionState:
    new = "new"
    checking = "checking"
    connected = "connected"
    completed = "completed"
    failed = "failed"
    disconnected = "disconnected"
    closed = "closed"


class ServiceWorkerState:
    parsed = "parsed"
    installing = "installing"
    installed = "installed"
    activating = "activating"
    activated = "activated"
    redundant = "redundant"


class RTCSdpType:
    offer = "offer"
    pranswer = "pranswer"
    answer = "answer"
    rollback = "rollback"


class RTCRtpSourceEntryType:
    contributing = "contributing"
    synchronization = "synchronization"


class ScreenColorGamut:
    srgb = "srgb"
    p3 = "p3"
    rec2020 = "rec2020"


class ClientType:
    window = "window"
    worker = "worker"
    sharedworker = "sharedworker"
    serviceworker = "serviceworker"
    all = "all"


class RTCDataChannelState:
    connecting = "connecting"
    open = "open"
    closing = "closing"
    closed = "closed"


class RTCDataChannelType:
    arraybuffer = "arraybuffer"
    blob = "blob"


class HeadersGuardEnum:
    none = "none"
    request = "request"
    request_no_cors = "request-no-cors"
    response = "response"
    immutable = "immutable"


class ScrollSetting:
    empty_ = ""
    up = "up"


class XMLHttpRequestResponseType:
    empty_ = ""
    arraybuffer = "arraybuffer"
    blob = "blob"
    document = "document"
    json = "json"
    text = "text"


class GamepadHapticActuatorType:
    vibration = "vibration"


class SpeechSynthesisErrorCode:
    canceled = "canceled"
    interrupted = "interrupted"
    audio_busy = "audio-busy"
    audio_hardware = "audio-hardware"
    network = "network"
    synthesis_unavailable = "synthesis-unavailable"
    synthesis_failed = "synthesis-failed"
    language_unavailable = "language-unavailable"
    voice_unavailable = "voice-unavailable"
    text_too_long = "text-too-long"
    invalid_argument = "invalid-argument"


class SecurityPolicyViolationEventDisposition:
    enforce = "enforce"
    report = "report"


class CSSStyleSheetParsingMode:
    author = "author"
    user = "user"
    agent = "agent"


class OrientationType:
    portrait_primary = "portrait-primary"
    portrait_secondary = "portrait-secondary"
    landscape_primary = "landscape-primary"
    landscape_secondary = "landscape-secondary"


class OrientationLockType:
    any = "any"
    natural = "natural"
    landscape = "landscape"
    portrait = "portrait"
    portrait_primary = "portrait-primary"
    portrait_secondary = "portrait-secondary"
    landscape_primary = "landscape-primary"
    landscape_secondary = "landscape-secondary"


class MediaKeyStatus:
    usable = "usable"
    expired = "expired"
    released = "released"
    output_restricted = "output-restricted"
    output_downscaled = "output-downscaled"
    status_pending = "status-pending"
    internal_error = "internal-error"


class CheckerboardReason:
    severe = "severe"
    recent = "recent"


class SupportedType:
    text_html = "text/html"
    text_xml = "text/xml"
    application_xml = "application/xml"
    application_xhtml_xml = "application/xhtml+xml"
    image_svg_xml = "image/svg+xml"


class CompositeOperation:
    replace = "replace"
    add = "add"
    accumulate = "accumulate"


class RTCPriorityType:
    very_low = "very-low"
    low = "low"
    medium = "medium"
    high = "high"


class RTCDegradationPreference:
    maintain_framerate = "maintain-framerate"
    maintain_resolution = "maintain-resolution"
    balanced = "balanced"


class WebGLPowerPreference:
    default = "default"
    low_power = "low-power"
    high_performance = "high-performance"


class OverSampleType:
    none = "none"
    X_2x = "2x"
    X_4x = "4x"


class BinaryType:
    blob = "blob"
    arraybuffer = "arraybuffer"


class ScrollState:
    started = "started"
    stopped = "stopped"


class ConnectionType:
    cellular = "cellular"
    bluetooth = "bluetooth"
    ethernet = "ethernet"
    wifi = "wifi"
    other = "other"
    none = "none"
    unknown = "unknown"


class ShadowRootMode:
    open = "open"
    closed = "closed"


class DecoderDoctorNotificationType:
    cannot_play = "cannot-play"
    platform_decoder_not_found = "platform-decoder-not-found"
    can_play_but_some_missing_decoders = "can-play-but-some-missing-decoders"
    cannot_initialize_pulseaudio = "cannot-initialize-pulseaudio"
    unsupported_libavcodec = "unsupported-libavcodec"
    decode_error = "decode-error"
    decode_warning = "decode-warning"


class BasicCardType:
    credit = "credit"
    debit = "debit"
    prepaid = "prepaid"


class PanningModelType:
    equalpower = "equalpower"
    HRTF = "HRTF"


class DistanceModelType:
    linear = "linear"
    inverse = "inverse"
    exponential = "exponential"


class IterationCompositeOperation:
    replace = "replace"
    accumulate = "accumulate"


class CanvasWindingRule:
    nonzero = "nonzero"
    evenodd = "evenodd"


class PCImplSignalingState:
    SignalingInvalid = "SignalingInvalid"
    SignalingStable = "SignalingStable"
    SignalingHaveLocalOffer = "SignalingHaveLocalOffer"
    SignalingHaveRemoteOffer = "SignalingHaveRemoteOffer"
    SignalingHaveLocalPranswer = "SignalingHaveLocalPranswer"
    SignalingHaveRemotePranswer = "SignalingHaveRemotePranswer"
    SignalingClosed = "SignalingClosed"


class PCImplIceConnectionState:
    new = "new"
    checking = "checking"
    connected = "connected"
    completed = "completed"
    failed = "failed"
    disconnected = "disconnected"
    closed = "closed"


class PCImplIceGatheringState:
    new = "new"
    gathering = "gathering"
    complete = "complete"


class VisibilityState:
    hidden = "hidden"
    visible = "visible"


class FlashClassification:
    unclassified = "unclassified"
    unknown = "unknown"
    allowed = "allowed"
    denied = "denied"


class ProfileTimelineMessagePortOperationType:
    serializeData = "serializeData"
    deserializeData = "deserializeData"


class ProfileTimelineWorkerOperationType:
    serializeDataOffMainThread = "serializeDataOffMainThread"
    serializeDataOnMainThread = "serializeDataOnMainThread"
    deserializeDataOffMainThread = "deserializeDataOffMainThread"
    deserializeDataOnMainThread = "deserializeDataOnMainThread"


class AnimationPlayState:
    idle = "idle"
    running = "running"
    paused = "paused"
    finished = "finished"


class PushPermissionState:
    granted = "granted"
    denied = "denied"
    prompt = "prompt"


class MediaDecodingType:
    file = "file"
    media_source = "media-source"


class MediaEncodingType:
    record = "record"
    transmission = "transmission"


class PushEncryptionKeyName:
    p256dh = "p256dh"
    auth = "auth"


class ReadableStreamReaderMode:
    byob = "byob"


class ReadableStreamType:
    bytes = "bytes"


class RTCStatsType:
    inbound_rtp = "inbound-rtp"
    outbound_rtp = "outbound-rtp"
    csrc = "csrc"
    session = "session"
    track = "track"
    transport = "transport"
    candidate_pair = "candidate-pair"
    local_candidate = "local-candidate"
    remote_candidate = "remote-candidate"


class RTCStatsIceCandidatePairState:
    frozen = "frozen"
    waiting = "waiting"
    inprogress = "inprogress"
    failed = "failed"
    succeeded = "succeeded"
    cancelled = "cancelled"


class RTCStatsIceCandidateType:
    host = "host"
    serverreflexive = "serverreflexive"
    peerreflexive = "peerreflexive"
    relayed = "relayed"


class GamepadHand:
    empty_ = ""
    left = "left"
    right = "right"


class GamepadMappingType:
    empty_ = ""
    standard = "standard"


class ConsoleLogLevel:
    All = "All"
    Debug = "Debug"
    Log = "Log"
    Info = "Info"
    Clear = "Clear"
    Trace = "Trace"
    TimeLog = "TimeLog"
    TimeEnd = "TimeEnd"
    Time = "Time"
    Group = "Group"
    GroupEnd = "GroupEnd"
    Profile = "Profile"
    ProfileEnd = "ProfileEnd"
    Dir = "Dir"
    Dirxml = "Dirxml"
    Warn = "Warn"
    Error = "Error"
    Off = "Off"


class ConsoleLevel:
    log = "log"
    warning = "warning"
    error = "error"


class FontFaceSetLoadStatus:
    loading = "loading"
    loaded = "loaded"


class PresentationConnectionState:
    connecting = "connecting"
    connected = "connected"
    closed = "closed"
    terminated = "terminated"


class PresentationConnectionBinaryType:
    blob = "blob"
    arraybuffer = "arraybuffer"


class CacheStorageNamespace:
    content = "content"
    chrome = "chrome"


class FontFaceLoadStatus:
    unloaded = "unloaded"
    loading = "loading"
    loaded = "loaded"
    error = "error"


class MediaKeySessionType:
    temporary = "temporary"
    persistent_license = "persistent-license"


class MediaKeyMessageType:
    license_request = "license-request"
    license_renewal = "license-renewal"
    license_release = "license-release"
    individualization_request = "individualization-request"


class RecordingState:
    inactive = "inactive"
    recording = "recording"
    paused = "paused"


class RTCIceCredentialType:
    password = "password"
    token = "token"


class RTCIceTransportPolicy:
    relay = "relay"
    all = "all"


class RTCBundlePolicy:
    balanced = "balanced"
    max_compat = "max-compat"
    max_bundle = "max-bundle"


class IDBTransactionMode:
    readonly = "readonly"
    readwrite = "readwrite"
    readwriteflush = "readwriteflush"
    cleanup = "cleanup"
    versionchange = "versionchange"


class IDBCursorDirection:
    next = "next"
    nextunique = "nextunique"
    prev = "prev"
    prevunique = "prevunique"


class FillMode:
    none = "none"
    forwards = "forwards"
    backwards = "backwards"
    both = "both"
    auto = "auto"


class PlaybackDirection:
    normal = "normal"
    reverse = "reverse"
    alternate = "alternate"
    alternate_reverse = "alternate-reverse"


class ChannelCountMode:
    max = "max"
    clamped_max = "clamped-max"
    explicit = "explicit"


class ChannelInterpretation:
    speakers = "speakers"
    discrete = "discrete"


class Transport:
    bt = "bt"
    ble = "ble"
    nfc = "nfc"
    usb = "usb"


class RTCRtpTransceiverDirection:
    sendrecv = "sendrecv"
    sendonly = "sendonly"
    recvonly = "recvonly"
    inactive = "inactive"


class WorkerType:
    classic = "classic"
    module = "module"


class ServiceWorkerUpdateViaCache:
    imports = "imports"
    all = "all"
    none = "none"


class TCPSocketBinaryType:
    arraybuffer = "arraybuffer"
    string = "string"


class TCPReadyState:
    connecting = "connecting"
    open = "open"
    closing = "closing"
    closed = "closed"


class AutoKeyword:
    auto = "auto"


class LineAlignSetting:
    start = "start"
    center = "center"
    end = "end"


class PositionAlignSetting:
    line_left = "line-left"
    center = "center"
    line_right = "line-right"
    auto = "auto"


class AlignSetting:
    start = "start"
    center = "center"
    end = "end"
    left = "left"
    right = "right"


class DirectionSetting:
    empty_ = ""
    rl = "rl"
    lr = "lr"


class SocketReadyState:
    opening = "opening"
    open = "open"
    closing = "closing"
    closed = "closed"
    halfclosed = "halfclosed"


class PermissionName:
    geolocation = "geolocation"
    notifications = "notifications"
    push = "push"
    persistent_storage = "persistent-storage"


class WakeLockType:
    screen = "screen"


class XRSessionMode:
    inline = "inline"
    immersive_vr = "immersive-vr"
    immersive_ar = "immersive-ar"


class XRVisibilityState:
    visible = "visible"
    visible_blurred = "visible-blurred"
    hidden = "hidden"


class XRReferenceSpaceType:
    viewer = "viewer"
    local = "local"
    local_floor = "local-floor"
    bounded_floor = "bounded-floor"
    unbounded = "unbounded"


class XREye:
    none = "none"
    left = "left"
    right = "right"


class XRHandedness:
    none = "none"
    left = "left"
    right = "right"


class XRTargetRayMode:
    gaze = "gaze"
    tracked_pointer = "tracked-pointer"
    screen = "screen"


class MediaSessionPlaybackState:
    none = "none"
    paused = "paused"
    playing = "playing"


class MediaSessionAction:
    play = "play"
    pause = "pause"
    seekbackward = "seekbackward"
    seekforward = "seekforward"
    previoustrack = "previoustrack"
    nexttrack = "nexttrack"
    skipad = "skipad"
    stop = "stop"
    seekto = "seekto"
    togglemicrophone = "togglemicrophone"
    togglecamera = "togglecamera"
    hangup = "hangup"


class XRHandJoint:
    wrist = "wrist"
    thumb_metacarpal = "thumb-metacarpal"
    thumb_phalanx_proximal = "thumb-phalanx-proximal"
    thumb_phalanx_distal = "thumb-phalanx-distal"
    thumb_tip = "thumb-tip"
    index_finger_metacarpal = "index-finger-metacarpal"
    index_finger_phalanx_proximal = "index-finger-phalanx-proximal"
    index_finger_phalanx_intermediate = "index-finger-phalanx-intermediate"
    index_finger_phalanx_distal = "index-finger-phalanx-distal"
    index_finger_tip = "index-finger-tip"
    middle_finger_metacarpal = "middle-finger-metacarpal"
    middle_finger_phalanx_proximal = "middle-finger-phalanx-proximal"
    middle_finger_phalanx_intermediate = "middle-finger-phalanx-intermediate"
    middle_finger_phalanx_distal = "middle-finger-phalanx-distal"
    middle_finger_tip = "middle-finger-tip"
    ring_finger_metacarpal = "ring-finger-metacarpal"
    ring_finger_phalanx_proximal = "ring-finger-phalanx-proximal"
    ring_finger_phalanx_intermediate = "ring-finger-phalanx-intermediate"
    ring_finger_phalanx_distal = "ring-finger-phalanx-distal"
    ring_finger_tip = "ring-finger-tip"
    pinky_finger_metacarpal = "pinky-finger-metacarpal"
    pinky_finger_phalanx_proximal = "pinky-finger-phalanx-proximal"
    pinky_finger_phalanx_intermediate = "pinky-finger-phalanx-intermediate"
    pinky_finger_phalanx_distal = "pinky-finger-phalanx-distal"
    pinky_finger_tip = "pinky-finger-tip"


class HIDUnitSystem:
    none = "none"
    si_linear = "si-linear"
    si_rotation = "si-rotation"
    english_linear = "english-linear"
    english_rotation = "english-rotation"
    vendor_defined = "vendor-defined"
    reserved = "reserved"


class USBRequestType:
    standard = "standard"
    class_ = "class"
    vendor = "vendor"


class USBRecipient:
    device = "device"
    interface = "interface"
    endpoint = "endpoint"
    other = "other"


class USBTransferStatus:
    ok = "ok"
    stall = "stall"
    babble = "babble"


class USBDirection:
    in_ = "in"
    out = "out"


class USBEndpointType:
    bulk = "bulk"
    interrupt = "interrupt"
    isochronous = "isochronous"


class PresentationStyle:
    unspecified = "unspecified"
    inline = "inline"
    attachment = "attachment"


class ResizeObserverBoxOptions:
    border_box = "border-box"
    content_box = "content-box"
    device_pixel_content_box = "device-pixel-content-box"


class GPUPowerPreference:
    low_power = "low-power"
    high_performance = "high-performance"


class GPUFeatureName:
    depth_clip_control = "depth-clip-control"
    depth32float_stencil8 = "depth32float-stencil8"
    texture_compression_bc = "texture-compression-bc"
    texture_compression_etc2 = "texture-compression-etc2"
    texture_compression_astc = "texture-compression-astc"
    timestamp_query = "timestamp-query"
    indirect_first_instance = "indirect-first-instance"
    shader_f16 = "shader-f16"
    bgra8unorm_storage = "bgra8unorm-storage"
    rg11b10ufloat_renderable = "rg11b10ufloat-renderable"


class GPUBufferMapState:
    unmapped = "unmapped"
    pending = "pending"
    mapped = "mapped"


class GPUTextureDimension:
    X_1d = "1d"
    X_2d = "2d"
    X_3d = "3d"


class GPUTextureViewDimension:
    X_1d = "1d"
    X_2d = "2d"
    X_2d_array = "2d-array"
    cube = "cube"
    cube_array = "cube-array"
    X_3d = "3d"


class GPUTextureAspect:
    all = "all"
    stencil_only = "stencil-only"
    depth_only = "depth-only"


class GPUTextureFormat:
    r8unorm = "r8unorm"
    r8snorm = "r8snorm"
    r8uint = "r8uint"
    r8sint = "r8sint"
    r16uint = "r16uint"
    r16sint = "r16sint"
    r16float = "r16float"
    rg8unorm = "rg8unorm"
    rg8snorm = "rg8snorm"
    rg8uint = "rg8uint"
    rg8sint = "rg8sint"
    r32uint = "r32uint"
    r32sint = "r32sint"
    r32float = "r32float"
    rg16uint = "rg16uint"
    rg16sint = "rg16sint"
    rg16float = "rg16float"
    rgba8unorm = "rgba8unorm"
    rgba8unorm_srgb = "rgba8unorm-srgb"
    rgba8snorm = "rgba8snorm"
    rgba8uint = "rgba8uint"
    rgba8sint = "rgba8sint"
    bgra8unorm = "bgra8unorm"
    bgra8unorm_srgb = "bgra8unorm-srgb"
    rgb9e5ufloat = "rgb9e5ufloat"
    rgb10a2unorm = "rgb10a2unorm"
    rg11b10ufloat = "rg11b10ufloat"
    rg32uint = "rg32uint"
    rg32sint = "rg32sint"
    rg32float = "rg32float"
    rgba16uint = "rgba16uint"
    rgba16sint = "rgba16sint"
    rgba16float = "rgba16float"
    rgba32uint = "rgba32uint"
    rgba32sint = "rgba32sint"
    rgba32float = "rgba32float"
    stencil8 = "stencil8"
    depth16unorm = "depth16unorm"
    depth24plus = "depth24plus"
    depth24plus_stencil8 = "depth24plus-stencil8"
    depth32float = "depth32float"
    depth32float_stencil8 = "depth32float-stencil8"
    bc1_rgba_unorm = "bc1-rgba-unorm"
    bc1_rgba_unorm_srgb = "bc1-rgba-unorm-srgb"
    bc2_rgba_unorm = "bc2-rgba-unorm"
    bc2_rgba_unorm_srgb = "bc2-rgba-unorm-srgb"
    bc3_rgba_unorm = "bc3-rgba-unorm"
    bc3_rgba_unorm_srgb = "bc3-rgba-unorm-srgb"
    bc4_r_unorm = "bc4-r-unorm"
    bc4_r_snorm = "bc4-r-snorm"
    bc5_rg_unorm = "bc5-rg-unorm"
    bc5_rg_snorm = "bc5-rg-snorm"
    bc6h_rgb_ufloat = "bc6h-rgb-ufloat"
    bc6h_rgb_float = "bc6h-rgb-float"
    bc7_rgba_unorm = "bc7-rgba-unorm"
    bc7_rgba_unorm_srgb = "bc7-rgba-unorm-srgb"
    etc2_rgb8unorm = "etc2-rgb8unorm"
    etc2_rgb8unorm_srgb = "etc2-rgb8unorm-srgb"
    etc2_rgb8a1unorm = "etc2-rgb8a1unorm"
    etc2_rgb8a1unorm_srgb = "etc2-rgb8a1unorm-srgb"
    etc2_rgba8unorm = "etc2-rgba8unorm"
    etc2_rgba8unorm_srgb = "etc2-rgba8unorm-srgb"
    eac_r11unorm = "eac-r11unorm"
    eac_r11snorm = "eac-r11snorm"
    eac_rg11unorm = "eac-rg11unorm"
    eac_rg11snorm = "eac-rg11snorm"
    astc_4x4_unorm = "astc-4x4-unorm"
    astc_4x4_unorm_srgb = "astc-4x4-unorm-srgb"
    astc_5x4_unorm = "astc-5x4-unorm"
    astc_5x4_unorm_srgb = "astc-5x4-unorm-srgb"
    astc_5x5_unorm = "astc-5x5-unorm"
    astc_5x5_unorm_srgb = "astc-5x5-unorm-srgb"
    astc_6x5_unorm = "astc-6x5-unorm"
    astc_6x5_unorm_srgb = "astc-6x5-unorm-srgb"
    astc_6x6_unorm = "astc-6x6-unorm"
    astc_6x6_unorm_srgb = "astc-6x6-unorm-srgb"
    astc_8x5_unorm = "astc-8x5-unorm"
    astc_8x5_unorm_srgb = "astc-8x5-unorm-srgb"
    astc_8x6_unorm = "astc-8x6-unorm"
    astc_8x6_unorm_srgb = "astc-8x6-unorm-srgb"
    astc_8x8_unorm = "astc-8x8-unorm"
    astc_8x8_unorm_srgb = "astc-8x8-unorm-srgb"
    astc_10x5_unorm = "astc-10x5-unorm"
    astc_10x5_unorm_srgb = "astc-10x5-unorm-srgb"
    astc_10x6_unorm = "astc-10x6-unorm"
    astc_10x6_unorm_srgb = "astc-10x6-unorm-srgb"
    astc_10x8_unorm = "astc-10x8-unorm"
    astc_10x8_unorm_srgb = "astc-10x8-unorm-srgb"
    astc_10x10_unorm = "astc-10x10-unorm"
    astc_10x10_unorm_srgb = "astc-10x10-unorm-srgb"
    astc_12x10_unorm = "astc-12x10-unorm"
    astc_12x10_unorm_srgb = "astc-12x10-unorm-srgb"
    astc_12x12_unorm = "astc-12x12-unorm"
    astc_12x12_unorm_srgb = "astc-12x12-unorm-srgb"


class GPUAddressMode:
    clamp_to_edge = "clamp-to-edge"
    repeat = "repeat"
    mirror_repeat = "mirror-repeat"


class GPUFilterMode:
    nearest = "nearest"
    linear = "linear"


class GPUMipmapFilterMode:
    nearest = "nearest"
    linear = "linear"


class GPUCompareFunction:
    never = "never"
    less = "less"
    equal = "equal"
    less_equal = "less-equal"
    greater = "greater"
    not_equal = "not-equal"
    greater_equal = "greater-equal"
    always = "always"


class GPUBufferBindingType:
    uniform = "uniform"
    storage = "storage"
    read_only_storage = "read-only-storage"


class GPUSamplerBindingType:
    filtering = "filtering"
    non_filtering = "non-filtering"
    comparison = "comparison"


class GPUTextureSampleType:
    float_ = "float"
    unfilterable_float = "unfilterable-float"
    depth = "depth"
    sint = "sint"
    uint = "uint"


class GPUStorageTextureAccess:
    write_only = "write-only"


class GPUCompilationMessageType:
    error = "error"
    warning = "warning"
    info = "info"


class GPUAutoLayoutMode:
    auto = "auto"


class GPUPrimitiveTopology:
    point_list = "point-list"
    line_list = "line-list"
    line_strip = "line-strip"
    triangle_list = "triangle-list"
    triangle_strip = "triangle-strip"


class GPUFrontFace:
    ccw = "ccw"
    cw = "cw"


class GPUCullMode:
    none = "none"
    front = "front"
    back = "back"


class GPUBlendFactor:
    zero = "zero"
    one = "one"
    src = "src"
    one_minus_src = "one-minus-src"
    src_alpha = "src-alpha"
    one_minus_src_alpha = "one-minus-src-alpha"
    dst = "dst"
    one_minus_dst = "one-minus-dst"
    dst_alpha = "dst-alpha"
    one_minus_dst_alpha = "one-minus-dst-alpha"
    src_alpha_saturated = "src-alpha-saturated"
    constant = "constant"
    one_minus_constant = "one-minus-constant"


class GPUBlendOperation:
    add = "add"
    subtract = "subtract"
    reverse_subtract = "reverse-subtract"
    min = "min"
    max = "max"


class GPUStencilOperation:
    keep = "keep"
    zero = "zero"
    replace = "replace"
    invert = "invert"
    increment_clamp = "increment-clamp"
    decrement_clamp = "decrement-clamp"
    increment_wrap = "increment-wrap"
    decrement_wrap = "decrement-wrap"


class GPUIndexFormat:
    uint16 = "uint16"
    uint32 = "uint32"


class GPUVertexFormat:
    uint8x2 = "uint8x2"
    uint8x4 = "uint8x4"
    sint8x2 = "sint8x2"
    sint8x4 = "sint8x4"
    unorm8x2 = "unorm8x2"
    unorm8x4 = "unorm8x4"
    snorm8x2 = "snorm8x2"
    snorm8x4 = "snorm8x4"
    uint16x2 = "uint16x2"
    uint16x4 = "uint16x4"
    sint16x2 = "sint16x2"
    sint16x4 = "sint16x4"
    unorm16x2 = "unorm16x2"
    unorm16x4 = "unorm16x4"
    snorm16x2 = "snorm16x2"
    snorm16x4 = "snorm16x4"
    float16x2 = "float16x2"
    float16x4 = "float16x4"
    float32 = "float32"
    float32x2 = "float32x2"
    float32x3 = "float32x3"
    float32x4 = "float32x4"
    uint32 = "uint32"
    uint32x2 = "uint32x2"
    uint32x3 = "uint32x3"
    uint32x4 = "uint32x4"
    sint32 = "sint32"
    sint32x2 = "sint32x2"
    sint32x3 = "sint32x3"
    sint32x4 = "sint32x4"


class GPUVertexStepMode:
    vertex = "vertex"
    instance = "instance"


class GPUComputePassTimestampLocation:
    beginning = "beginning"
    end = "end"


class GPURenderPassTimestampLocation:
    beginning = "beginning"
    end = "end"


class GPULoadOp:
    load = "load"
    clear = "clear"


class GPUStoreOp:
    store = "store"
    discard = "discard"


class GPUQueryType:
    occlusion = "occlusion"
    timestamp = "timestamp"


class GPUCanvasAlphaMode:
    opaque = "opaque"
    premultiplied = "premultiplied"


class GPUDeviceLostReason:
    destroyed = "destroyed"


class GPUErrorFilter:
    validation = "validation"
    out_of_memory = "out-of-memory"
    internal = "internal"


class ParityType:
    none = "none"
    even = "even"
    odd = "odd"


class FlowControlType:
    none = "none"
    hardware = "hardware"


class HardwareAcceleration:
    no_preference = "no-preference"
    prefer_hardware = "prefer-hardware"
    prefer_software = "prefer-software"


class AlphaOption:
    keep = "keep"
    discard = "discard"


class LatencyMode:
    quality = "quality"
    realtime = "realtime"


class CodecState:
    unconfigured = "unconfigured"
    configured = "configured"
    closed = "closed"


class EncodedAudioChunkType:
    key = "key"
    delta = "delta"


class EncodedVideoChunkType:
    key = "key"
    delta = "delta"


class AudioSampleFormat:
    u8 = "u8"
    s16 = "s16"
    s32 = "s32"
    f32 = "f32"
    u8_planar = "u8-planar"
    s16_planar = "s16-planar"
    s32_planar = "s32-planar"
    f32_planar = "f32-planar"


class VideoPixelFormat:
    I420 = "I420"
    I420A = "I420A"
    I422 = "I422"
    I444 = "I444"
    NV12 = "NV12"
    RGBA = "RGBA"
    RGBX = "RGBX"
    BGRA = "BGRA"
    BGRX = "BGRX"


class VideoColorPrimaries:
    bt709 = "bt709"
    bt470bg = "bt470bg"
    smpte170m = "smpte170m"


class VideoTransferCharacteristics:
    bt709 = "bt709"
    smpte170m = "smpte170m"
    iec61966_2_1 = "iec61966-2-1"


class VideoMatrixCoefficients:
    rgb = "rgb"
    bt709 = "bt709"
    bt470bg = "bt470bg"
    smpte170m = "smpte170m"


class PaymentItemType:
    tax = "tax"


class PaymentShippingType:
    shipping = "shipping"
    delivery = "delivery"
    pickup = "pickup"


class VRDisplayEventReason:
    mounted = "mounted"
    navigation = "navigation"
    requested = "requested"
    unmounted = "unmounted"


RequestInfo = Request | USVString

nsContentPolicyType = int

DOMHighResTimeStamp = float

COSEAlgorithmIdentifier = int

AAGUID = BufferSource

ConstrainLong = int | ConstrainLongRange

ConstrainDouble = float | ConstrainDoubleRange

ConstrainBoolean = bool | ConstrainBooleanParameters

GLint64 = int

GLuint64 = int

VRSource = HTMLCanvasElement | OffscreenCanvas

EventHandler = EventHandlerNonNull | None

OnBeforeUnloadEventHandler = OnBeforeUnloadEventHandlerNonNull | None

OnErrorEventHandler = OnErrorEventHandlerNonNull | None

BlobPart = BufferSource | Blob | USVString

nsISupports = object

GeometryNode = Text | Element | Document

UnrestrictedDoubleOrKeyframeAnimationOptions = float | KeyframeAnimationOptions

KeyType = str

KeyUsage = str

NamedCurve = str

BigInteger = Uint8Array

KeyFormat = str

AlgorithmIdentifier = object | str

JSON = object

BodyInit = Blob | BufferSource | FormData | URLSearchParams | USVString | ReadableStream

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

GLuint64EXT = int

HTMLOrSVGImageElement = HTMLImageElement | SVGImageElement

CanvasImageSource = HTMLOrSVGImageElement | HTMLCanvasElement | HTMLVideoElement | ImageBitmap | OffscreenCanvas | VideoFrame

PushMessageDataInit = BufferSource | USVString

ReadableStreamReader = ReadableStreamDefaultReader | ReadableStreamBYOBReader

ReadableStreamController = ReadableStreamDefaultController | ReadableByteStreamController

BinaryData = ArrayBuffer | ArrayBufferView

FormDataEntryValue = Blob | Directory | USVString

ErrorCode = int

MessageEventSource = WindowProxy | MessagePort | ServiceWorker

ImageBitmapSource = CanvasImageSource | Blob | ImageData

XRWebGLRenderingContext = WebGLRenderingContext | WebGL2RenderingContext

ClipboardItemDataType = str | Blob

GPUBufferUsageFlags = int

GPUMapModeFlags = int

GPUTextureUsageFlags = int

GPUShaderStageFlags = int

GPUBindingResource = GPUSampler | GPUTextureView | GPUBufferBinding | GPUExternalTexture

GPUPipelineConstantValue = float

GPUColorWriteFlags = int

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

ImageBufferSource = BufferSource | ReadableStream

UUID = str

BluetoothServiceUUID = str | int

BluetoothCharacteristicUUID = str | int

BluetoothDescriptorUUID = str | int


class FrameLoader(WebBrowserPersistable):
    docShell: nsIDocShell | None
    tabParent: TabParent | None
    loadContext: LoadContext
    parentSHistory: ParentSHistory | None
    depthTooGreat: bool

    def activateRemoteFrame(self): ...

    def deactivateRemoteFrame(self): ...

    def sendCrossProcessMouseEvent(self, aType: str, aX: float, aY: float, aButton: int, aClickCount: int,
                                   aModifiers: int, aIgnoreRootScrollFrame: bool | None = false): ...

    def activateFrameEvent(self, aType: str, capture: bool): ...

    messageManager: MessageSender | None
    def requestNotifyAfterRemotePaint(self): ...
    def requestFrameLoaderClose(self): ...

    def requestUpdatePosition(self): ...

    def print(self, aOuterWindowID: int, aPrintSettings: nsIPrintSettings,
              aProgressListener: nsIWebProgressListener | None = None): ...
    clipSubdocument: bool
    clampScrollPosition: bool
    ownerElement: Element | None
    childID: int
    ownerIsMozBrowserFrame: bool
    lazyWidth: int
    lazyHeight: int
    isDead: bool

class HTMLOutputElement(HTMLElement):
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

class PerformanceEntry:
    name: str
    entryType: str
    startTime: DOMHighResTimeStamp
    duration: DOMHighResTimeStamp
    def toJSON(self) -> object: ...

class IDBMutableFile(EventTarget):
    name: str
    type: str
    database: IDBDatabase
    def open(self, mode: FileMode | None = "readonly") -> IDBFileHandle: ...
    def getFile(self) -> DOMRequest: ...
    onabort: EventHandler
    onerror: EventHandler

class TimeRanges:
    length: int

    def start(self, index: int) -> float: ...

    def end(self, index: int) -> float: ...


class Element(Node, ChildNode, NonDocumentTypeChildNode, ParentNode, Animatable, GeometryUtils):
    namespaceURI: str | None
    prefix: str | None
    localName: str
    tagName: str
    id: str
    className: str
    classList: DOMTokenList
    attributes: NamedNodeMap

    def getAttribute(self, name: str) -> str | None: ...

    def getAttributeNS(self, namespace: str | None, localName: str) -> str | None: ...
    def toggleAttribute(self, name: str, force: bool | None = None) -> bool: ...
    def setAttribute(self, name: str, value: str): ...
    def setAttributeNS(self, namespace: str | None, name: str, value: str): ...
    def removeAttribute(self, name: str): ...
    def removeAttributeNS(self, namespace: str | None, localName: str): ...
    def hasAttribute(self, name: str) -> bool: ...
    def hasAttributeNS(self, namespace: str | None, localName: str) -> bool: ...
    def hasAttributes(self) -> bool: ...
    def closest(self, selector: str) -> Element | None: ...
    def matches(self, selector: str) -> bool: ...
    def webkitMatchesSelector(self, selector: str) -> bool: ...
    def getElementsByTagName(self, localName: str) -> HTMLCollection: ...
    def getElementsByTagNameNS(self, namespace: str | None, localName: str) -> HTMLCollection: ...
    def getElementsByClassName(self, classNames: str) -> HTMLCollection: ...
    def insertAdjacentElement(self, where: str, element: Element) -> Element | None: ...
    def insertAdjacentText(self, where: str, data: str): ...

    fontSizeInflation: float
    def setPointerCapture(self, pointerId: int): ...
    def releasePointerCapture(self, pointerId: int): ...
    def hasPointerCapture(self, pointerId: int) -> bool: ...
    def setCapture(self, retargetToElement: bool | None = false): ...
    def releaseCapture(self): ...
    def setCaptureAlways(self, retargetToElement: bool | None = false): ...
    def getAttributeNode(self, name: str) -> Attr | None: ...
    def setAttributeNode(self, newAttr: Attr) -> Attr | None: ...
    def removeAttributeNode(self, oldAttr: Attr) -> Attr | None: ...
    def getAttributeNodeNS(self, namespaceURI: str | None, localName: str) -> Attr | None: ...
    def setAttributeNodeNS(self, newAttr: Attr) -> Attr | None: ...
    def scrollByNoFlush(self, dx: int, dy: int) -> bool: ...
    def getAsFlexContainer(self) -> Flex | None: ...
    def getTransformToAncestor(self, ancestor: Element) -> DOMMatrixReadOnly: ...
    def getTransformToParent(self) -> DOMMatrixReadOnly: ...
    def getTransformToViewport(self) -> DOMMatrixReadOnly: ...
    def getClientRects(self) -> DOMRectList: ...
    def getBoundingClientRect(self) -> DOMRect: ...
    def scrollIntoView(self, arg: bool | ScrollIntoViewOptions | None = None): ...
    scrollTop: int
    scrollLeft: int
    scrollWidth: int
    scrollHeight: int

    def scroll(self, x: float, y: float): ...

    def scroll(self, options: ScrollToOptions | None = None): ...

    def scrollTo(self, x: float, y: float): ...

    def scrollTo(self, options: ScrollToOptions | None = None): ...

    def scrollBy(self, x: float, y: float): ...

    def scrollBy(self, options: ScrollToOptions | None = None): ...
    clientTop: int
    clientLeft: int
    clientWidth: int
    clientHeight: int
    innerHTML: str
    outerHTML: str
    def insertAdjacentHTML(self, position: str, text: str): ...
    def querySelector(self, selectors: str) -> Element | None: ...
    def querySelectorAll(self, selectors: str) -> NodeList: ...
    def attachShadow(self, shadowRootInitDict: ShadowRootInit) -> ShadowRoot: ...
    shadowRoot: ShadowRoot | None
    openOrClosedShadowRoot: ShadowRoot | None
    assignedSlot: HTMLSlotElement | None
    slot: str
    def requestFullscreen(self): ...
    def requestPointerLock(self): ...

class CSSNamespaceRule(CSSRule):
    namespaceURI: str
    prefix: str

class Directory:
    name: str
    path: str

class ListBoxObject(BoxObject):
    def getRowCount(self) -> int: ...
    def getRowHeight(self) -> int: ...
    def getNumberOfVisibleRows(self) -> int: ...
    def getIndexOfFirstVisibleRow(self) -> int: ...
    def ensureIndexIsVisible(self, rowIndex: int): ...
    def scrollToIndex(self, rowIndex: int): ...
    def scrollByLines(self, numLines: int): ...
    def getItemAtIndex(self, index: int) -> Element | None: ...
    def getIndexOfItem(self, item: Element) -> int: ...


class BaseAudioContext(EventTarget, rustBaseAudioContext): ...

class Range:
    def createContextualFragment(self, fragment: str) -> DocumentFragment: ...
    def getClientRects(self) -> DOMRectList | None: ...
    def getBoundingClientRect(self) -> DOMRect: ...
    def getClientRectsAndTexts(self) -> ClientRectsAndTexts: ...


class SVGFEBlendElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    mode: SVGAnimatedEnumeration

class HTMLHRElement(HTMLElement):
    align: str
    color: str
    noShade: bool
    size: str
    width: str

class SourceBuffer(EventTarget):
    mode: SourceBufferAppendMode
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

    def appendBuffer(self, data: ArrayBuffer): ...

    def appendBuffer(self, data: ArrayBufferView): ...

    def abort(self): ...

    def remove(self, start: float, end: float): ...

    def changeType(self, type: str): ...

class MediaKeyError(Event):
    systemCode: int

class TimeEvent(Event):
    detail: int
    view: WindowProxy | None
    def initTimeEvent(self, aType: str, aView: Window | None = None, aDetail: int | None = 0): ...

class CSSMediaRule(CSSConditionRule):
    media: MediaList

class HTMLQuoteElement(HTMLElement):
    cite: str

class MediaKeySystemAccess:
    keySystem: str
    def getConfiguration(self) -> MediaKeySystemConfiguration: ...

class HTMLFormElement(HTMLElement):
    acceptCharset: str
    action: str
    autocomplete: str
    enctype: str
    encoding: str
    method: str
    name: str
    noValidate: bool
    target: str
    elements: HTMLCollection
    length: int
    def submit(self): ...
    def reset(self): ...
    def checkValidity(self) -> bool: ...
    def reportValidity(self) -> bool: ...

class IntersectionObserverEntry:
    time: DOMHighResTimeStamp
    rootBounds: DOMRectReadOnly | None
    boundingClientRect: DOMRectReadOnly
    intersectionRect: DOMRectReadOnly
    isIntersecting: bool
    intersectionRatio: float
    target: Element

class PublicKeyCredential(Credential):
    rawId: ArrayBuffer
    response: AuthenticatorResponse
    def getClientExtensionResults(self) -> AuthenticationExtensionsClientOutputs: ...

class AuthenticatorResponse:
    clientDataJSON: ArrayBuffer

class AuthenticatorAttestationResponse(AuthenticatorResponse):
    attestationObject: ArrayBuffer

class AuthenticatorAssertionResponse(AuthenticatorResponse):
    authenticatorData: ArrayBuffer
    signature: ArrayBuffer
    userHandle: ArrayBuffer

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


class SVGImageElement(SVGGraphicsElement, SVGURIReference):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio

class HTMLTableCaptionElement(HTMLElement):
    align: str

class TreeBoxObject(BoxObject):
    columns: TreeColumns | None
    focused: bool
    treeBody: Element | None
    rowHeight: int
    rowWidth: int
    horizontalPosition: int
    selectionRegion: nsIScriptableRegion
    def getFirstVisibleRow(self) -> int: ...
    def getLastVisibleRow(self) -> int: ...
    def getPageLength(self) -> int: ...
    def ensureRowIsVisible(self, index: int): ...
    def ensureCellIsVisible(self, row: int, col: TreeColumn | None): ...
    def scrollToRow(self, index: int): ...
    def scrollByLines(self, numLines: int): ...
    def scrollByPages(self, numPages: int): ...
    def invalidate(self): ...
    def invalidateColumn(self, col: TreeColumn | None): ...
    def invalidateRow(self, index: int): ...
    def invalidateCell(self, row: int, col: TreeColumn | None): ...
    def invalidateRange(self, startIndex: int, endIndex: int): ...
    def getRowAt(self, x: int, y: int) -> int: ...
    def getCellAt(self, x: int, y: int) -> TreeCellInfo: ...
    def getCellAt(self, x: int, y: int, row: object, column: object, childElt: object): ...

    def getCoordsForCellItem(self, row: int, col: TreeColumn, element: str) -> DOMRect | None: ...

    def getCoordsForCellItem(self, row: int, col: TreeColumn, element: str, x: object, y: object, width: object,
                             height: object): ...

    def isCellCropped(self, row: int, col: TreeColumn | None) -> bool: ...
    def rowCountChanged(self, index: int, count: int): ...
    def beginUpdateBatch(self): ...
    def endUpdateBatch(self): ...
    def clearStyleAndImageCaches(self): ...
    def removeImageCacheEntry(self, row: int, col: TreeColumn): ...

class MediaStreamTrack(EventTarget):
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
    def getConstraints(self) -> MediaTrackConstraints: ...
    def getSettings(self) -> MediaTrackSettings: ...
    def mutedChanged(self, muted: bool): ...

class CSSRuleList:
    length: int

class PerformanceNavigationTiming(PerformanceResourceTiming):
    unloadEventStart: DOMHighResTimeStamp
    unloadEventEnd: DOMHighResTimeStamp
    domInteractive: DOMHighResTimeStamp
    domContentLoadedEventStart: DOMHighResTimeStamp
    domContentLoadedEventEnd: DOMHighResTimeStamp
    domComplete: DOMHighResTimeStamp
    loadEventStart: DOMHighResTimeStamp
    loadEventEnd: DOMHighResTimeStamp
    type: NavigationType
    redirectCount: int
    def toJSON(self) -> object: ...


class ProcessingInstruction(CharacterData, LinkStyle):
    target: str

class PushMessageData:
    def arrayBuffer(self) -> ArrayBuffer: ...
    def blob(self) -> Blob: ...
    def text(self) -> USVString: ...

class XMLHttpRequestEventTarget(EventTarget):
    onloadstart: EventHandler
    onprogress: EventHandler
    onabort: EventHandler
    onerror: EventHandler
    onload: EventHandler
    ontimeout: EventHandler
    onloadend: EventHandler

class IdleDeadline:
    def timeRemaining(self) -> DOMHighResTimeStamp: ...
    didTimeout: bool

class ChildSHistory:
    count: int
    index: int
    def canGo(self, aOffset: int) -> bool: ...
    def go(self, aOffset: int): ...
    def reload(self, aReloadFlags: int): ...
    legacySHistory: nsISHistory

class SVGAnimatedLength:
    baseVal: SVGLength
    animVal: SVGLength

class PaintRequestList:
    length: int


class SVGPolylineElement(SVGGeometryElement, SVGAnimatedPoints): ...


class SVGFEImageElement(SVGElement, SVGFilterPrimitiveStandardAttributes, SVGURIReference):
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio

class Grid:
    rows: GridDimension
    cols: GridDimension

class GridDimension:
    lines: GridLines
    tracks: GridTracks

class GridLines:
    length: int


class GridLine:
    start: float
    breadth: float
    type: GridDeclaration
    number: int
    negativeNumber: int

class GridTracks:
    length: int


class GridTrack:
    start: float
    breadth: float
    type: GridDeclaration
    state: GridTrackState

class GridArea:
    name: str
    type: GridDeclaration
    rowStart: int
    rowEnd: int
    columnStart: int
    columnEnd: int

class SVGAnimatedRect:
    baseVal: SVGRect | None
    animVal: SVGRect | None

class SharedWorkerGlobalScope(WorkerGlobalScope):
    name: str
    def close(self): ...
    onconnect: EventHandler

class HTMLMenuItemElement(HTMLElement):
    type: str
    label: str
    icon: str
    disabled: bool
    checked: bool
    radiogroup: str
    defaultChecked: bool

class SVGPathSeg:
    pathSegType: int
    pathSegTypeAsLetter: str

class SVGPathSegClosePath(SVGPathSeg): ...


class SVGPathSegMovetoAbs(SVGPathSeg):
    x: float
    y: float


class SVGPathSegMovetoRel(SVGPathSeg):
    x: float
    y: float


class SVGPathSegLinetoAbs(SVGPathSeg):
    x: float
    y: float


class SVGPathSegLinetoRel(SVGPathSeg):
    x: float
    y: float


class SVGPathSegCurvetoCubicAbs(SVGPathSeg):
    x: float
    y: float
    x1: float
    y1: float
    x2: float
    y2: float


class SVGPathSegCurvetoCubicRel(SVGPathSeg):
    x: float
    y: float
    x1: float
    y1: float
    x2: float
    y2: float


class SVGPathSegCurvetoQuadraticAbs(SVGPathSeg):
    x: float
    y: float
    x1: float
    y1: float


class SVGPathSegCurvetoQuadraticRel(SVGPathSeg):
    x: float
    y: float
    x1: float
    y1: float


class SVGPathSegArcAbs(SVGPathSeg):
    x: float
    y: float
    r1: float
    r2: float
    angle: float
    largeArcFlag: bool
    sweepFlag: bool


class SVGPathSegArcRel(SVGPathSeg):
    x: float
    y: float
    r1: float
    r2: float
    angle: float
    largeArcFlag: bool
    sweepFlag: bool


class SVGPathSegLinetoHorizontalAbs(SVGPathSeg):
    x: float


class SVGPathSegLinetoHorizontalRel(SVGPathSeg):
    x: float


class SVGPathSegLinetoVerticalAbs(SVGPathSeg):
    y: float


class SVGPathSegLinetoVerticalRel(SVGPathSeg):
    y: float


class SVGPathSegCurvetoCubicSmoothAbs(SVGPathSeg):
    x: float
    y: float
    x2: float
    y2: float


class SVGPathSegCurvetoCubicSmoothRel(SVGPathSeg):
    x: float
    y: float
    x2: float
    y2: float


class SVGPathSegCurvetoQuadraticSmoothAbs(SVGPathSeg):
    x: float
    y: float


class SVGPathSegCurvetoQuadraticSmoothRel(SVGPathSeg):
    x: float
    y: float

class HTMLMenuElement(HTMLElement):
    type: str
    label: str
    compact: bool

class Client:
    url: USVString
    frameType: FrameType
    type: ClientType
    id: str

class WindowClient(Client):
    visibilityState: VisibilityState
    focused: bool

class PerformanceMeasure(PerformanceEntry): ...

class PushSubscriptionOptions:
    applicationServerKey: ArrayBuffer

class OVR_multiview2:
    def framebufferTextureMultiviewOVR(self, target: GLenum, attachment: GLenum, texture: WebGLTexture | None,
                                       level: GLint, baseViewIndex: GLint, numViews: GLsizei): ...

class MouseScrollEvent(MouseEvent):
    axis: int

    def initMouseScrollEvent(self, type: str, canBubble: bool | None = false, cancelable: bool | None = false,
                             view: Window | None = None, detail: int | None = 0, screenX: int | None = 0,
                             screenY: int | None = 0, clientX: int | None = 0, clientY: int | None = 0,
                             ctrlKey: bool | None = false, altKey: bool | None = false, shiftKey: bool | None = false,
                             metaKey: bool | None = false, button: short | None = 0,
                             relatedTarget: EventTarget | None = None, axis: int | None = 0): ...


class SVGFETurbulenceElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    baseFrequencyX: SVGAnimatedNumber
    baseFrequencyY: SVGAnimatedNumber
    numOctaves: SVGAnimatedInteger
    seed: SVGAnimatedNumber
    stitchTiles: SVGAnimatedEnumeration
    type: SVGAnimatedEnumeration

class FetchObserver(EventTarget):
    state: FetchState
    onstatechange: EventHandler
    onrequestprogress: EventHandler
    onresponseprogress: EventHandler

class SVGLinearGradientElement(SVGGradientElement):
    x1: SVGAnimatedLength
    y1: SVGAnimatedLength
    x2: SVGAnimatedLength
    y2: SVGAnimatedLength


class SVGFESpecularLightingElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    surfaceScale: SVGAnimatedNumber
    specularConstant: SVGAnimatedNumber
    specularExponent: SVGAnimatedNumber
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber

class TextClause:
    startOffset: int
    endOffset: int
    isCaret: bool
    isTargetClause: bool

class FileList:
    length: int

class MediaList:
    mediaText: str
    length: int
    def deleteMedium(self, oldMedium: str): ...
    def appendMedium(self, newMedium: str): ...


class HTMLIFrameElement(HTMLElement, BrowserElement):
    src: str
    srcdoc: str
    name: str
    sandbox: DOMTokenList
    allowFullscreen: bool
    allowPaymentRequest: bool
    width: str
    height: str
    referrerPolicy: str
    contentDocument: Document | None
    contentWindow: WindowProxy | None
    align: str
    scrolling: str
    frameBorder: str
    longDesc: str
    marginHeight: str
    marginWidth: str
    def getSVGDocument(self) -> Document | None: ...

class LocalMediaStream(MediaStream):
    def stop(self): ...

class WebGLSampler: ...

class WebGLSync: ...

class WebGLTransformFeedback: ...


class WebGL2RenderingContext(WebGL2RenderingContextBase): ...

class EXT_color_buffer_float: ...


class URL: ...

class CSSImportRule(CSSRule):
    href: str
    media: MediaList | None
    styleSheet: CSSStyleSheet | None


class HTMLMeterElement(HTMLElement):
    value: float
    min: float
    max: float
    low: float
    high: float
    optimum: float
    labels: NodeList

class FileSystem:
    name: USVString
    root: FileSystemDirectoryEntry

class BatteryManager(EventTarget):
    charging: bool
    chargingTime: float
    dischargingTime: float
    level: float
    onchargingchange: EventHandler
    onchargingtimechange: EventHandler
    ondischargingtimechange: EventHandler
    onlevelchange: EventHandler

class SVGPathSegList:
    numberOfItems: int


class SVGFEFloodElement(SVGElement, SVGFilterPrimitiveStandardAttributes): ...

class SVGEllipseElement(SVGGeometryElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    rx: SVGAnimatedLength
    ry: SVGAnimatedLength

class HTMLTemplateElement(HTMLElement):
    content: DocumentFragment

class TransceiverImpl:
    def getReceiveTrack(self) -> MediaStreamTrack: ...
    def syncWithJS(self, transceiver: RTCRtpTransceiver): ...

class PermissionStatus(EventTarget):
    state: PermissionState
    onchange: EventHandler

class HTMLEmbedElement(HTMLElement):
    src: str
    type: str
    width: str
    height: str
    align: str
    name: str
    def getSVGDocument(self) -> Document | None: ...

class HTMLDataElement(HTMLElement):
    value: str

class SVGAnimatedEnumeration:
    baseVal: int
    animVal: int


class VRFieldOfView:
    upDegrees: float
    rightDegrees: float
    downDegrees: float
    leftDegrees: float

class VRDisplayCapabilities:
    hasPosition: bool
    hasOrientation: bool
    hasExternalDisplay: bool
    canPresent: bool
    maxLayers: int

class VRStageParameters:
    sittingToStandingTransform: Float32Array
    sizeX: float
    sizeZ: float

class VRPose:
    position: Float32Array
    linearVelocity: Float32Array
    linearAcceleration: Float32Array
    orientation: Float32Array
    angularVelocity: Float32Array
    angularAcceleration: Float32Array

class VREyeParameters:
    offset: Float32Array
    fieldOfView: VRFieldOfView
    renderWidth: int
    renderHeight: int

class VRDisplay(EventTarget):
    presentingGroups: int
    groupMask: int
    isConnected: bool
    isPresenting: bool
    capabilities: VRDisplayCapabilities
    stageParameters: VRStageParameters | None

    def getEyeParameters(self, whichEye: VREye) -> VREyeParameters: ...

    displayId: int
    displayName: str

    def getFrameData(self, frameData: VRFrameData) -> bool: ...

    def getPose(self) -> VRPose: ...

    def getSubmitFrameResult(self, result: VRSubmitFrameResult) -> bool: ...

    def resetPose(self): ...

    depthNear: float
    depthFar: float

    def requestAnimationFrame(self, callback: FrameRequestCallback) -> int: ...

    def cancelAnimationFrame(self, handle: int): ...

    def submitFrame(self): ...


class HTMLFrameSetElement(HTMLElement, WindowEventHandlers):
    cols: str
    rows: str

class SVGGElement(SVGGraphicsElement): ...


class SVGFilterElement(SVGElement, SVGURIReference):
    filterUnits: SVGAnimatedEnumeration
    primitiveUnits: SVGAnimatedEnumeration
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength


class SVGScriptElement(SVGElement, SVGURIReference):
    type: str
    crossOrigin: str | None

class IDBRequest(EventTarget):
    error: DOMException | None
    source: IDBObjectStore | IDBIndex | IDBCursor | None
    transaction: IDBTransaction | None
    readyState: IDBRequestReadyState
    onsuccess: EventHandler
    onerror: EventHandler


class WorkerNavigator(NavigatorID, NavigatorLanguage, NavigatorOnLine, NavigatorConcurrentHardware, NavigatorStorage,
                      NavigatorGPU):
    connection: NetworkInformation
    mediaCapabilities: MediaCapabilities
    usb: USB
    serial: Serial

class SVGFEFuncAElement(SVGComponentTransferFunctionElement): ...


class SVGFEComponentTransferElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString

class MediaDeviceInfo:
    deviceId: str
    kind: MediaDeviceKind
    label: str
    groupId: str
    def toJSON(self) -> object: ...

class HTMLLegendElement(HTMLElement):
    form: HTMLFormElement | None
    align: str

class RTCRtpReceiver:
    track: MediaStreamTrack
    def setRemoteSendBit(self, sendBit: bool): ...
    def processTrackAdditionsAndRemovals(self, transceiver: RTCRtpTransceiver, postProcessing: object): ...

class Attr(Node):
    localName: str
    value: str
    name: str
    namespaceURI: str | None
    prefix: str | None
    specified: bool

class ParentSHistory:
    count: int
    index: int

class StorageManager: ...

class PerformanceNavigation:
    type: int
    redirectCount: int
    def toJSON(self) -> object: ...

class DOMStringMap: ...

class PerformanceResourceTiming(PerformanceEntry):
    initiatorType: str
    nextHopProtocol: str
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
    def toJSON(self) -> object: ...


class AnimationTimeline:
    currentTime: float | None


class CSSPseudoElement(Animatable):
    type: str
    parentElement: Element

class Crypto:
    subtle: SubtleCrypto
    def getRandomValues(self, array: ArrayBufferView) -> ArrayBufferView: ...
    def randomUUID(self) -> str: ...

class AudioTrack:
    id: str
    kind: str
    label: str
    language: str
    enabled: bool
    sourceBuffer: SourceBuffer | None


class SVGFEGaussianBlurElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    stdDeviationX: SVGAnimatedNumber
    stdDeviationY: SVGAnimatedNumber

    def setStdDeviation(self, stdDeviationX: float, stdDeviationY: float): ...

class Position:
    coords: Coordinates
    timestamp: DOMTimeStamp


class SVGFEColorMatrixElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    type: SVGAnimatedEnumeration
    values: SVGAnimatedNumberList

class PaymentResponse:
    def toJSON(self) -> object: ...
    requestId: str
    methodName: str
    details: object
    shippingAddress: PaymentAddress | None
    shippingOption: str | None
    payerName: str | None
    payerEmail: str | None
    payerPhone: str | None

class IDBOpenDBRequest(IDBRequest):
    onblocked: EventHandler
    onupgradeneeded: EventHandler


class SVGFEOffsetElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    dx: SVGAnimatedNumber
    dy: SVGAnimatedNumber

class AudioParamMap: ...

class NamedNodeMap:
    def setNamedItem(self, arg: Attr) -> Attr | None: ...
    def removeNamedItem(self, name: str) -> Attr: ...
    length: int
    def getNamedItemNS(self, namespaceURI: str | None, localName: str) -> Attr | None: ...
    def setNamedItemNS(self, arg: Attr) -> Attr | None: ...
    def removeNamedItemNS(self, namespaceURI: str | None, localName: str) -> Attr: ...

class SpeechRecognitionResult:
    length: int
    isFinal: bool

class HTMLVideoElement(HTMLMediaElement):
    width: int
    height: int
    videoWidth: int
    videoHeight: int
    poster: str
    def getVideoPlaybackQuality(self) -> VideoPlaybackQuality: ...


class SVGAnimationElement(SVGElement, SVGTests):
    targetElement: SVGElement | None

    def getStartTime(self) -> float: ...

    def getCurrentTime(self) -> float: ...

    def getSimpleDuration(self) -> float: ...

    def beginElement(self): ...

    def beginElementAt(self, offset: float): ...

    def endElement(self): ...

    def endElementAt(self, offset: float): ...

class SVGSetElement(SVGAnimationElement): ...

class SVGClipPathElement(SVGElement):
    clipPathUnits: SVGAnimatedEnumeration
    transform: SVGAnimatedTransformList

class History:
    length: int
    scrollRestoration: ScrollRestoration
    def go(self, delta: int | None = 0): ...
    def back(self): ...
    def forward(self): ...

class FileSystemEntry:
    isFile: bool
    isDirectory: bool
    name: USVString
    fullPath: USVString
    filesystem: FileSystem

    def getParent(self, successCallback: FileSystemEntryCallback | None = None,
                  errorCallback: ErrorCallback | None = None): ...


class SVGAElement(SVGGraphicsElement, SVGURIReference):
    target: SVGAnimatedString
    download: str
    ping: str
    rel: str
    referrerPolicy: str
    relList: DOMTokenList
    hreflang: str
    type: str
    text: str

class SVGRadialGradientElement(SVGGradientElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    r: SVGAnimatedLength
    fx: SVGAnimatedLength
    fy: SVGAnimatedLength
    fr: SVGAnimatedLength

class MIDIPort(EventTarget):
    id: str
    manufacturer: str | None
    name: str | None
    version: str | None
    type: MIDIPortType
    state: MIDIPortDeviceState
    connection: MIDIPortConnectionState
    onstatechange: EventHandler

class SpeechSynthesisVoice:
    voiceURI: str
    name: str
    lang: str
    localService: bool
    default: bool

class HTMLTextAreaElement(HTMLElement):
    autocomplete: str
    autofocus: bool
    cols: int
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
    selectionStart: int | None
    selectionEnd: int | None
    selectionDirection: str | None

    def setRangeText(self, replacement: str): ...

    def setRangeText(self, replacement: str, start: int, end: int,
                     selectionMode: SelectionMode | None = "preserve"): ...

    def setSelectionRange(self, start: int, end: int, direction: str | None = None): ...

class SVGTSpanElement(SVGTextPositioningElement): ...

class DataTransferItemList:
    length: int
    def add(self, data: str, type: str) -> DataTransferItem | None: ...
    def add(self, data: File) -> DataTransferItem | None: ...
    def remove(self, index: int): ...
    def clear(self): ...


class SVGZoomAndPan(SVGZoomAndPanValues): ...

class VideoPlaybackQuality:
    creationTime: DOMHighResTimeStamp
    totalVideoFrames: int
    droppedVideoFrames: int
    corruptedVideoFrames: int

class SVGPreserveAspectRatio:
    align: int
    meetOrSlice: int

class SVGTransformList:
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: SVGTransform) -> SVGTransform: ...
    def insertItemBefore(self, newItem: SVGTransform, index: int) -> SVGTransform: ...
    def replaceItem(self, newItem: SVGTransform, index: int) -> SVGTransform: ...
    def removeItem(self, index: int) -> SVGTransform: ...
    def appendItem(self, newItem: SVGTransform) -> SVGTransform: ...
    def createSVGTransformFromMatrix(self, matrix: SVGMatrix) -> SVGTransform: ...
    def consolidate(self) -> SVGTransform | None: ...

class CDATASection(Text): ...

class PluginArray:
    length: int
    def refresh(self, reloadDocuments: bool | None = false): ...


class Exception(ExceptionMembers):
    name: str
    message: str

class HTMLInputElement(HTMLElement):
    accept: str
    alt: str
    autocomplete: str
    autofocus: bool
    defaultChecked: bool
    checked: bool
    disabled: bool
    form: HTMLFormElement | None
    files: FileList | None
    formAction: str
    formEnctype: str
    formMethod: str
    formNoValidate: bool
    formTarget: str
    height: int
    indeterminate: bool
    inputMode: str
    list: HTMLElement | None
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
    src: str
    step: str
    type: str
    defaultValue: str
    value: str
    valueAsDate: Date | None
    valueAsNumber: float
    width: int
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

    def setRangeText(self, replacement: str): ...

    def setRangeText(self, replacement: str, start: int, end: int,
                     selectionMode: SelectionMode | None = "preserve"): ...

    def setSelectionRange(self, start: int, end: int, direction: str | None = None): ...

    def showPicker(self): ...

    align: str
    useMap: str
    webkitdirectory: bool

    def getDateTimeInputBoxValue(self) -> DateTimeValue: ...

    def updateDateTimeInputBox(self, value: DateTimeValue | None = None): ...

    def setDateTimePickerState(self, open: bool): ...

    def getMinimum(self) -> float: ...

    def getMaximum(self) -> float: ...

    previewValue: str


class Window(EventTarget, GlobalEventHandlers, WindowEventHandlers, WindowSessionStorage, WindowLocalStorage,
             GlobalCrypto, GlobalU2F, SpeechSynthesisGetter, TouchEventHandlers, OnErrorEventHandlerForWindow,
             WindowOrWorkerGlobalScope):
    window: Window
    self: Window
    document: Document | None
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
    def open(self, url: str | None = "", target: str | None = "", features: str | None = "") -> WindowProxy | None: ...
    navigator: Navigator
    external: External
    applicationCache: ApplicationCache
    def alert(self): ...
    def alert(self, message: str): ...
    def confirm(self, message: str | None = "") -> bool: ...
    def prompt(self, message: str | None = "", default: str | None = "") -> str | None: ...
    def print(self): ...
    onappinstalled: EventHandler
    def captureEvents(self): ...
    def releaseEvents(self): ...
    def getSelection(self) -> Selection | None: ...
    def getComputedStyle(self, elt: Element, pseudoElt: str | None = "") -> CSSStyleDeclaration | None: ...
    def matchMedia(self, query: str) -> MediaQueryList | None: ...
    screen: Screen

    def moveTo(self, x: int, y: int): ...

    def moveBy(self, x: int, y: int): ...

    def resizeTo(self, x: int, y: int): ...

    def resizeBy(self, x: int, y: int): ...

    def scroll(self, x: float, y: float): ...

    def scroll(self, options: ScrollToOptions | None = None): ...

    def scrollTo(self, x: float, y: float): ...

    def scrollTo(self, options: ScrollToOptions | None = None): ...

    def scrollBy(self, x: float, y: float): ...

    def scrollBy(self, options: ScrollToOptions | None = None): ...

    scrollX: float
    pageXOffset: float
    scrollY: float
    pageYOffset: float
    devicePixelRatio: float

    def requestAnimationFrame(self, callback: FrameRequestCallback) -> int: ...

    def cancelAnimationFrame(self, handle: int): ...

    performance: Performance | None
    orientation: short
    onorientationchange: EventHandler
    onvrdisplayconnect: EventHandler
    onvrdisplaydisconnect: EventHandler
    onvrdisplayactivate: EventHandler
    onvrdisplaydeactivate: EventHandler
    onvrdisplaypresentchange: EventHandler
    paintWorklet: Worklet
    def requestIdleCallback(self, callback: IdleRequestCallback, options: IdleRequestOptions | None = None) -> int: ...
    def cancelIdleCallback(self, handle: int): ...


class HTMLImageElement:
    name: str
    align: str
    hspace: int
    vspace: int
    longDesc: str
    border: str
    sizes: str
    currentSrc: str

class Plugin:
    description: str
    filename: str
    version: str
    name: str
    length: int

class ScrollBoxObject(BoxObject):
    def scrollTo(self, x: int, y: int): ...
    def scrollBy(self, dx: int, dy: int): ...
    def scrollByIndex(self, dindexes: int): ...
    def scrollToElement(self, child: Element): ...
    positionX: int
    positionY: int
    scrolledWidth: int
    scrolledHeight: int
    def ensureElementIsVisible(self, child: Element): ...

class Flex: ...

class FlexLine:
    growthState: FlexLineGrowthState
    crossStart: float
    crossSize: float
    firstBaselineOffset: float
    lastBaselineOffset: float

class FlexItem:
    node: Node | None
    mainBaseSize: float
    mainDeltaSize: float
    mainMinSize: float
    mainMaxSize: float
    crossMinSize: float
    crossMaxSize: float

class PaintWorkletGlobalScope(WorkletGlobalScope):
    def registerPaint(self, name: str, paintCtor: VoidFunction): ...

class AudioDestinationNode(AudioNode):
    maxChannelCount: int

class ScriptProcessorNode(AudioNode):
    onaudioprocess: EventHandler
    bufferSize: int


class DOMRequest(EventTarget, DOMRequestShared):
    def fireDetailedError(self, aError: DOMException): ...

class IDBDatabase(EventTarget):
    name: str
    version: int
    objectStoreNames: DOMStringList

    def createObjectStore(self, name: str,
                          optionalParameters: IDBObjectStoreParameters | None = {}) -> IDBObjectStore: ...

    def deleteObjectStore(self, name: str): ...
    def close(self): ...
    onabort: EventHandler
    onclose: EventHandler
    onerror: EventHandler
    onversionchange: EventHandler
    storage: StorageType
    def createMutableFile(self, name: str, type: str | None = None) -> IDBRequest: ...

class SVGFESpotLightElement(SVGElement):
    x: SVGAnimatedNumber
    y: SVGAnimatedNumber
    z: SVGAnimatedNumber
    pointsAtX: SVGAnimatedNumber
    pointsAtY: SVGAnimatedNumber
    pointsAtZ: SVGAnimatedNumber
    specularExponent: SVGAnimatedNumber
    limitingConeAngle: SVGAnimatedNumber

class HTMLBaseElement(HTMLElement):
    href: str
    target: str

class HTMLButtonElement(HTMLElement):
    autofocus: bool
    disabled: bool
    form: HTMLFormElement | None
    formAction: str
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

class CSSKeyframesRule(CSSRule):
    name: str
    cssRules: CSSRuleList
    def appendRule(self, rule: str): ...
    def deleteRule(self, select: str): ...
    def findRule(self, select: str) -> CSSKeyframeRule | None: ...

class CSSCounterStyleRule(CSSRule):
    name: str
    system: str
    symbols: str
    additiveSymbols: str
    negative: str
    prefix: str
    suffix: str
    range: str
    pad: str
    speakAs: str
    fallback: str

class CSSAnimation(Animation):
    animationName: str


class DocumentFragment(ParentNode):
    def querySelector(self, selectors: str) -> Element | None: ...

    def querySelectorAll(self, selectors: str) -> NodeList: ...

class HTMLTimeElement(HTMLElement):
    dateTime: str

class MimeTypeArray:
    length: int

class FileSystemDirectoryEntry(FileSystemEntry):
    def createReader(self) -> FileSystemDirectoryReader: ...

    def getFile(self, path: USVString | None = None, options: FileSystemFlags | None = None,
                successCallback: FileSystemEntryCallback | None = None, errorCallback: ErrorCallback | None = None): ...

    def getDirectory(self, path: USVString | None = None, options: FileSystemFlags | None = None,
                     successCallback: FileSystemEntryCallback | None = None,
                     errorCallback: ErrorCallback | None = None): ...

class TextTrack(EventTarget):
    kind: TextTrackKind
    label: str
    language: str
    id: str
    inBandMetadataTrackDispatchType: str
    mode: TextTrackMode
    cues: TextTrackCueList | None
    activeCues: TextTrackCueList | None
    def addCue(self, cue: VTTCue): ...
    def removeCue(self, cue: VTTCue): ...
    oncuechange: EventHandler
    sourceBuffer: SourceBuffer | None

class SVGMetadataElement(SVGElement): ...

class TextTrackCue(EventTarget):
    track: TextTrack | None
    id: str
    startTime: float
    endTime: float
    pauseOnExit: bool
    onenter: EventHandler
    onexit: EventHandler


class Geolocation:
    def getCurrentPosition(self, successCallback: PositionCallback, errorCallback: PositionErrorCallback | None = None,
                           options: PositionOptions | None = None): ...

    def watchPosition(self, successCallback: PositionCallback, errorCallback: PositionErrorCallback | None = None,
                      options: PositionOptions | None = None) -> int: ...

    def clearWatch(self, watchId: int): ...

class SVGAnimatedTransformList:
    baseVal: SVGTransformList
    animVal: SVGTransformList

class BeforeUnloadEvent(Event):
    returnValue: str


class RTCPeerConnection: ...


class ServiceWorker(EventTarget, AbstractWorker):
    scriptURL: USVString
    state: ServiceWorkerState
    onstatechange: EventHandler


class ScrollAreaEvent(UIEvent):
    x: float
    y: float
    width: float
    height: float

    def initScrollAreaEvent(self, type: str, canBubble: bool | None = false, cancelable: bool | None = false,
                            view: Window | None = None, detail: int | None = 0, x: float | None = 0,
                            y: float | None = 0, width: float | None = 0, height: float | None = 0): ...

class HTMLOListElement(HTMLElement):
    reversed: bool
    start: int
    type: str
    compact: bool


class Text(GeometryUtils):
    assignedSlot: HTMLSlotElement | None

class IDBObjectStore:
    name: str
    indexNames: DOMStringList
    transaction: IDBTransaction
    autoIncrement: bool
    def clear(self) -> IDBRequest: ...
    def index(self, name: str) -> IDBIndex: ...
    def deleteIndex(self, indexName: str): ...

class HTMLHtmlElement(HTMLElement):
    version: str

class GetUserMediaRequest:
    windowID: int
    innerWindowID: int
    callID: str
    rawID: str
    mediaSource: str
    def getConstraints(self) -> MediaStreamConstraints: ...
    isSecure: bool
    isHandlingUserInput: bool

class MimeType:
    description: str
    enabledPlugin: Plugin | None
    suffixes: str
    type: str

class CSSFontFeatureValuesRule(CSSRule):
    fontFamily: str
    valueText: str

class SVGAnimatedBoolean:
    baseVal: bool
    animVal: bool


class AudioListener:
    dopplerFactor: float
    speedOfSound: float

    def setPosition(self, x: float, y: float, z: float): ...

    def setOrientation(self, x: float, y: float, z: float, xUp: float, yUp: float, zUp: float): ...

    def setVelocity(self, x: float, y: float, z: float): ...


class UIEvent:
    layerX: int
    layerY: int
    pageX: int
    pageY: int
    which: int
    rangeParent: Node | None
    rangeOffset: int

class HTMLHeadingElement(HTMLElement):
    align: str

class HTMLMapElement(HTMLElement):
    name: str
    areas: HTMLCollection

class MIDIInput(MIDIPort):
    onmidimessage: EventHandler

class HTMLScriptElement(HTMLElement):
    src: str
    type: str
    noModule: bool
    charset: str
    async_: bool
    defer: bool
    crossOrigin: str | None
    text: str
    event: str
    htmlFor: str
    integrity: str


class SVGUseElement(SVGGraphicsElement, SVGURIReference):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class SVGFEMergeNodeElement(SVGElement):
    in1: SVGAnimatedString

class AudioWorklet(Worklet): ...

class ImageCaptureError:
    code: int
    message: str

class HTMLCollection:
    length: int

class HTMLTableCellElement(HTMLElement):
    colSpan: int
    rowSpan: int
    headers: str
    cellIndex: int
    align: str
    axis: str
    height: str
    width: str
    ch: str
    chOff: str
    noWrap: bool
    vAlign: str
    bgColor: str


class HTMLElement(Element, GlobalEventHandlers, DocumentAndElementEventHandlers, TouchEventHandlers,
                  OnErrorEventHandlerForNodes):
    title: str
    scrollHeight: int
    scrollTop: int
    lang: str
    dir: str
    dataset: DOMStringMap
    innerText: str
    hidden: bool

    def click(self): ...

    tabIndex: int
    def focus(self): ...
    def blur(self): ...
    accessKey: str
    accessKeyLabel: str
    draggable: bool
    contentEditable: str
    isContentEditable: bool
    spellcheck: bool
    style: CSSStyleDeclaration
    offsetParent: Element | None
    offsetTop: int
    offsetLeft: int
    offsetWidth: int
    offsetHeight: int

class HTMLUnknownElement(HTMLElement): ...

class CryptoKey:
    type: KeyType
    extractable: bool
    algorithm: object

class SubtleCrypto: ...


class SVGFEMergeElement(SVGElement, SVGFilterPrimitiveStandardAttributes): ...

class CustomElementRegistry:
    def define(self, name: str, functionConstructor: Function, options: ElementDefinitionOptions | None = None): ...
    def setElementCreationCallback(self, name: str, callback: CustomElementCreationCallback): ...
    def upgrade(self, root: Node): ...


class SVGFEMorphologyElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    operator: SVGAnimatedEnumeration
    radiusX: SVGAnimatedNumber
    radiusY: SVGAnimatedNumber

class ImageDocument(HTMLDocument):
    imageIsOverflowing: bool
    imageIsResized: bool
    imageRequest: imgIRequest | None
    def shrinkToFit(self): ...
    def restoreImage(self): ...
    def restoreImageTo(self, x: int, y: int): ...
    def toggleImageSize(self): ...

class HTMLPictureElement(HTMLElement): ...


class SVGMatrix:
    a: float
    b: float
    c: float
    d: float
    e: float
    f: float

    def multiply(self, secondMatrix: SVGMatrix) -> SVGMatrix: ...

    def inverse(self) -> SVGMatrix: ...

    def translate(self, x: float, y: float) -> SVGMatrix: ...

    def scale(self, scaleFactor: float) -> SVGMatrix: ...

    def scaleNonUniform(self, scaleFactorX: float, scaleFactorY: float) -> SVGMatrix: ...

    def rotate(self, angle: float) -> SVGMatrix: ...

    def rotateFromVector(self, x: float, y: float) -> SVGMatrix: ...

    def flipX(self) -> SVGMatrix: ...

    def flipY(self) -> SVGMatrix: ...

    def skewX(self, angle: float) -> SVGMatrix: ...

    def skewY(self, angle: float) -> SVGMatrix: ...

class MutationRecord:
    type: str
    target: Node | None
    addedNodes: NodeList
    removedNodes: NodeList
    previousSibling: Node | None
    nextSibling: Node | None
    attributeName: str | None
    attributeNamespace: str | None
    oldValue: str | None


class Screen(EventTarget):
    availWidth: int
    availHeight: int
    width: int
    height: int
    colorDepth: int
    pixelDepth: int
    top: int
    left: int
    availTop: int
    availLeft: int
    orientation: ScreenOrientation
    colorGamut: ScreenColorGamut
    luminance: ScreenLuminance | None
    onchange: EventHandler


class ScreenLuminance:
    min: float
    max: float
    maxAverage: float

class CSSRule:
    type: int
    cssText: str
    parentRule: CSSRule | None
    parentStyleSheet: CSSStyleSheet | None

class Clients: ...

class TextTrackCueList:
    length: int
    def getCueById(self, id: str) -> VTTCue | None: ...

class PresentationAvailability(EventTarget):
    value: bool
    onchange: EventHandler

class WindowRoot(EventTarget): ...

class HTMLDirectoryElement(HTMLElement):
    compact: bool

class SVGAngle:
    unitType: int
    value: float
    valueInSpecifiedUnits: float
    valueAsString: str

    def newValueSpecifiedUnits(self, unitType: int, valueInSpecifiedUnits: float): ...

    def convertToSpecifiedUnits(self, unitType: int): ...

class StyleSheet:
    type: str
    href: str | None
    ownerNode: Node | None
    parentStyleSheet: StyleSheet | None
    title: str | None
    media: MediaList
    disabled: bool
    sourceMapURL: str
    sourceURL: str

class RTCDataChannel(EventTarget):
    label: str
    reliable: bool
    maxPacketLifeTime: int | None
    maxRetransmits: int | None
    readyState: RTCDataChannelState
    bufferedAmount: int
    bufferedAmountLowThreshold: int
    onopen: EventHandler
    onerror: EventHandler
    onclose: EventHandler
    def close(self): ...
    onmessage: EventHandler
    onbufferedamountlow: EventHandler
    binaryType: RTCDataChannelType
    def send(self, data: str): ...
    def send(self, data: Blob): ...
    def send(self, data: ArrayBuffer): ...
    def send(self, data: ArrayBufferView): ...


class SVGStyleElement(SVGElement, LinkStyle):
    xmlspace: str
    type: str
    media: str
    title: str

class GamepadHapticActuator:
    type: GamepadHapticActuatorType


class CompositionEvent:
    def initCompositionEvent(self, typeArg: str, canBubbleArg: bool | None = false, cancelableArg: bool | None = false,
                             viewArg: Window | None = None, dataArg: str | None = None, localeArg: str | None = ""): ...

class Cache: ...

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
    def collapse(self, node: Node | None, offset: int | None = 0): ...
    def setPosition(self, node: Node | None, offset: int | None = 0): ...
    def collapseToStart(self): ...
    def collapseToEnd(self): ...
    def extend(self, node: Node, offset: int | None = 0): ...
    def setBaseAndExtent(self, anchorNode: Node, anchorOffset: int, focusNode: Node, focusOffset: int): ...
    def selectAllChildren(self, node: Node): ...
    def deleteFromDocument(self): ...
    def containsNode(self, node: Node, allowPartialContainment: bool | None = false) -> bool: ...
    def modify(self, alter: str, direction: str, granularity: str): ...
    interlinePosition: bool
    caretBidiLevel: short | None
    def toStringWithFormat(self, formatType: str, flags: int, wrapColumn: int) -> str: ...
    def addSelectionListener(self, newListener: nsISelectionListener): ...
    def removeSelectionListener(self, listenerToRemove: nsISelectionListener): ...
    selectionType: short

    def scrollIntoView(self, aRegion: short, aIsSynchronous: bool, aVPercent: short, aHPercent: short): ...

    def setColors(self, aForegroundColor: str, aBackgroundColor: str, aAltForegroundColor: str,
                  aAltBackgroundColor: str): ...

    def resetColors(self): ...

class HTMLDocument(Document):
    domain: str
    cookie: str
    def open(self, type: str | None = None, replace: str | None = "") -> Document: ...
    def open(self, url: str, name: str, features: str, replace: bool | None = false) -> WindowProxy | None: ...
    def close(self): ...
    def write(self, text: str | None = None): ...
    def writeln(self, text: str | None = None): ...
    designMode: str
    def execCommand(self, commandId: str, showUI: bool | None = false, value: str | None = "") -> bool: ...
    def queryCommandEnabled(self, commandId: str) -> bool: ...
    def queryCommandIndeterm(self, commandId: str) -> bool: ...
    def queryCommandState(self, commandId: str) -> bool: ...
    def queryCommandSupported(self, commandId: str) -> bool: ...
    def queryCommandValue(self, commandId: str) -> str: ...
    fgColor: str
    linkColor: str
    vlinkColor: str
    alinkColor: str
    bgColor: str
    def clear(self): ...
    all: HTMLAllCollection
    def captureEvents(self): ...
    def releaseEvents(self): ...
    blockedTrackingNodeCount: int
    blockedTrackingNodes: NodeList

class MessagePort(EventTarget):
    def start(self): ...
    def close(self): ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class SVGUnitTypes: ...

class HTMLMetaElement(HTMLElement):
    name: str
    httpEquiv: str
    content: str
    scheme: str

class WebrtcGlobalInformation: ...

class MIDIAccess(EventTarget):
    inputs: MIDIInputMap
    outputs: MIDIOutputMap
    onstatechange: EventHandler
    sysexEnabled: bool

class MIDIOutputMap: ...

class FileSystemDirectoryReader:
    def readEntries(self, successCallback: FileSystemEntriesCallback, errorCallback: ErrorCallback | None = None): ...

class CSSStyleSheet(StyleSheet):
    ownerRule: CSSRule | None
    cssRules: CSSRuleList
    parsingMode: CSSStyleSheetParsingMode
    def insertRule(self, rule: str, index: int | None = 0) -> int: ...
    def deleteRule(self, index: int): ...

class SVGAnimatedString:
    baseVal: str
    animVal: str

class HTMLSelectElement(HTMLElement):
    autofocus: bool
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
    def remove(self): ...
    openInParentProcess: bool
    def getAutocompleteInfo(self) -> AutocompleteInfo: ...
    previewValue: str


class SVGFEDiffuseLightingElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    surfaceScale: SVGAnimatedNumber
    diffuseConstant: SVGAnimatedNumber
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber

class HTMLDataListElement(HTMLElement):
    options: HTMLCollection

class SVGLength:
    unitType: int
    value: float
    valueInSpecifiedUnits: float
    valueAsString: str

    def newValueSpecifiedUnits(self, unitType: int, valueInSpecifiedUnits: float): ...

    def convertToSpecifiedUnits(self, unitType: int): ...

class DataTransferItem:
    kind: str
    type: str
    def getAsString(self, callback: FunctionStringCallback | None): ...
    def getAsFile(self) -> File | None: ...
    def webkitGetAsEntry(self) -> FileSystemEntry | None: ...

class CSSKeyframeRule(CSSRule):
    keyText: str
    style: CSSStyleDeclaration

class XMLDocument(Document):
    def load(self, url: str) -> bool: ...
    async_: bool

class HTMLOptionsCollection(HTMLCollection):
    length: int
    def add(self, element: HTMLOptionElement | HTMLOptGroupElement, before: HTMLElement | int | None = None): ...
    def remove(self, index: int): ...
    selectedIndex: int

class SVGTitleElement(SVGElement): ...

class SourceBufferList(EventTarget):
    length: int
    onaddsourcebuffer: EventHandler
    onremovesourcebuffer: EventHandler

class MediaKeySession(EventTarget):
    error: MediaKeyError | None
    sessionId: str
    expiration: float
    keyStatuses: MediaKeyStatusMap
    onkeystatuseschange: EventHandler
    onmessage: EventHandler

class ScreenOrientation(EventTarget):
    def unlock(self): ...
    type: OrientationType
    angle: int
    onchange: EventHandler

class HTMLDetailsElement(HTMLElement):
    open: bool

class SVGTransform:
    type: int
    matrix: SVGMatrix
    angle: float

    def setMatrix(self, matrix: SVGMatrix): ...

    def setTranslate(self, tx: float, ty: float): ...

    def setScale(self, sx: float, sy: float): ...

    def setRotate(self, angle: float, cx: float, cy: float): ...

    def setSkewX(self, angle: float): ...

    def setSkewY(self, angle: float): ...


class CharacterData(Node, ChildNode, NonDocumentTypeChildNode):
    data: str
    length: int

    def substringData(self, offset: int, count: int) -> str: ...

    def appendData(self, data: str): ...

    def insertData(self, offset: int, data: str): ...

    def deleteData(self, offset: int, count: int): ...

    def replaceData(self, offset: int, count: int, data: str): ...


class InputEvent:
    dataTransfer: DataTransfer | None

class SVGCircleElement(SVGGeometryElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    r: SVGAnimatedLength

class DOMTokenList:
    length: int
    def contains(self, token: str) -> bool: ...
    def add(self, tokens: str | None = None): ...
    def remove(self, tokens: str | None = None): ...
    def replace(self, token: str, newToken: str) -> bool: ...
    def toggle(self, token: str, force: bool | None = None) -> bool: ...
    def supports(self, token: str) -> bool: ...
    value: str

class MediaKeyStatusMap:
    size: int
    def has(self, keyId: BufferSource) -> bool: ...

class HTMLDListElement(HTMLElement):
    compact: bool

class SVGRectElement(SVGGeometryElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    rx: SVGAnimatedLength
    ry: SVGAnimatedLength

class MIDIOutput(MIDIPort):
    def clear(self): ...

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
    timeToNonBlankPaint: int
    timeToDOMContentFlushed: int
    def toJSON(self) -> object: ...


class AudioScheduledSourceNode(AudioNode, rustAudioScheduledSourceNode): ...

class CSSSupportsRule(CSSConditionRule): ...


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

class Storage:
    length: int
    def key(self, index: int) -> str | None: ...
    def clear(self): ...
    isSessionOnly: bool

class SVGComponentTransferFunctionElement(SVGElement):
    type: SVGAnimatedEnumeration
    tableValues: SVGAnimatedNumberList
    slope: SVGAnimatedNumber
    intercept: SVGAnimatedNumber
    amplitude: SVGAnimatedNumber
    exponent: SVGAnimatedNumber
    offset: SVGAnimatedNumber


class SVGFECompositeElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    operator: SVGAnimatedEnumeration
    k1: SVGAnimatedNumber
    k2: SVGAnimatedNumber
    k3: SVGAnimatedNumber
    k4: SVGAnimatedNumber

class HTMLTableSectionElement(HTMLElement):
    rows: HTMLCollection
    def insertRow(self, index: int | None = -1) -> HTMLElement: ...
    def deleteRow(self, index: int): ...
    align: str
    ch: str
    chOff: str
    vAlign: str

class Node(EventTarget):
    nodeType: int
    nodeName: str
    baseURI: str | None
    isConnected: bool
    ownerDocument: Document | None
    def getRootNode(self, options: GetRootNodeOptions | None = None) -> Node: ...
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
    def insertBefore(self, node: Node, child: Node | None) -> Node: ...
    def appendChild(self, node: Node) -> Node: ...
    def replaceChild(self, node: Node, child: Node) -> Node: ...
    def removeChild(self, child: Node) -> Node: ...
    def normalize(self): ...
    def cloneNode(self, deep: bool | None = false) -> Node: ...
    def isSameNode(self, node: Node | None) -> bool: ...
    def isEqualNode(self, node: Node | None) -> bool: ...
    def compareDocumentPosition(self, other: Node) -> int: ...
    def contains(self, other: Node | None) -> bool: ...
    def lookupPrefix(self, namespace: str | None) -> str | None: ...
    def lookupNamespaceURI(self, prefix: str | None) -> str | None: ...
    def isDefaultNamespace(self, namespace: str | None) -> bool: ...

class DOMImplementation:
    def hasFeature(self) -> bool: ...

    def createDocumentType(self, qualifiedName: str, publicId: str, systemId: str) -> DocumentType: ...

    def createDocument(self, namespace: str | None, qualifiedName: str,
                       doctype: DocumentType | None = None) -> Document: ...

    def createHTMLDocument(self, title: str | None = None) -> Document: ...

class VRMockDisplay:
    def setEyeResolution(self, aRenderWidth: int, aRenderHeight: int): ...

    def setEyeParameter(self, eye: VREye, offsetX: float, offsetY: float, offsetZ: float, upDegree: float,
                        rightDegree: float, downDegree: float, leftDegree: float): ...

    def setPose(self, position: Float32Array, linearVelocity: Float32Array, linearAcceleration: Float32Array,
                orientation: Float32Array, angularVelocity: Float32Array, angularAcceleration: Float32Array): ...

    def setMountState(self, isMounted: bool): ...

    def update(self): ...

class VRMockController:
    def newButtonEvent(self, button: int, pressed: bool): ...

    def newAxisMoveEvent(self, axis: int, value: float): ...

    def newPoseMove(self, position: Float32Array, linearVelocity: Float32Array, linearAcceleration: Float32Array,
                    orientation: Float32Array, angularVelocity: Float32Array, angularAcceleration: Float32Array): ...

class VRServiceTest: ...

class HTMLSourceElement(HTMLElement):
    src: str
    type: str
    srcset: str
    sizes: str
    media: str

class SVGPointList:
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: SVGPoint) -> SVGPoint: ...
    def insertItemBefore(self, newItem: SVGPoint, index: int) -> SVGPoint: ...
    def replaceItem(self, newItem: SVGPoint, index: int) -> SVGPoint: ...
    def removeItem(self, index: int) -> SVGPoint: ...
    def appendItem(self, newItem: SVGPoint) -> SVGPoint: ...

class SVGStopElement(SVGElement):
    offset: SVGAnimatedNumber

class SVGAnimateTransformElement(SVGAnimationElement): ...

class CSSStyleRule(CSSRule):
    selectorText: str
    style: CSSStyleDeclaration

class CSSGroupingRule(CSSRule):
    cssRules: CSSRuleList
    def insertRule(self, rule: str, index: int | None = 0) -> int: ...
    def deleteRule(self, index: int): ...


class SVGPatternElement(SVGElement, SVGFitToViewBox, SVGURIReference):
    patternUnits: SVGAnimatedEnumeration
    patternContentUnits: SVGAnimatedEnumeration
    patternTransform: SVGAnimatedTransformList
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class PaintRequest:
    clientRect: DOMRect
    reason: str

class CSSStyleDeclaration:
    cssText: str
    length: int
    def getPropertyValue(self, property: str) -> str: ...
    def getPropertyPriority(self, property: str) -> str: ...
    def setProperty(self, property: str, value: str, priority: str | None = ""): ...
    def removeProperty(self, property: str) -> str: ...
    parentRule: CSSRule | None

class RTCRtpSender:
    track: MediaStreamTrack | None
    def getParameters(self) -> RTCRtpParameters: ...
    dtmf: RTCDTMFSender | None
    def setTrack(self, track: MediaStreamTrack | None): ...
    def checkWasCreatedByPc(self, pc: RTCPeerConnection): ...

class MediaDevices(EventTarget):
    ondevicechange: EventHandler
    def getSupportedConstraints(self) -> MediaTrackSupportedConstraints: ...


class SVGSVGElement(SVGGraphicsElement, SVGFitToViewBox, SVGZoomAndPanValues):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    useCurrentView: bool
    currentScale: float
    currentTranslate: SVGPoint

    def suspendRedraw(self, maxWaitMilliseconds: int) -> int: ...

    def unsuspendRedraw(self, suspendHandleID: int): ...

    def unsuspendRedrawAll(self): ...

    def forceRedraw(self): ...

    def pauseAnimations(self): ...

    def unpauseAnimations(self): ...

    def animationsPaused(self) -> bool: ...

    def getCurrentTime(self) -> float: ...

    def setCurrentTime(self, seconds: float): ...

    def deselectAll(self): ...

    def createSVGNumber(self) -> SVGNumber: ...

    def createSVGLength(self) -> SVGLength: ...

    def createSVGAngle(self) -> SVGAngle: ...

    def createSVGPoint(self) -> SVGPoint: ...

    def createSVGMatrix(self) -> SVGMatrix: ...

    def createSVGRect(self) -> SVGRect: ...

    def createSVGTransform(self) -> SVGTransform: ...

    def createSVGTransformFromMatrix(self, matrix: SVGMatrix) -> SVGTransform: ...

    def getElementById(self, elementId: str) -> Element | None: ...

class HTMLSpanElement(HTMLElement): ...

class WebGLBuffer: ...

class WebGLFramebuffer: ...

class WebGLProgram: ...

class WebGLRenderbuffer: ...

class WebGLShader: ...

class WebGLTexture: ...

class WebGLUniformLocation: ...

class WebGLVertexArrayObject: ...

class WebGLActiveInfo:
    size: GLint
    type: GLenum
    name: str

class WebGLShaderPrecisionFormat:
    rangeMin: GLint
    rangeMax: GLint
    precision: GLint


class WebGLRenderingContext(WebGLRenderingContextBase):
    def bufferData(self, target: GLenum, size: GLsizeiptr, usage: GLenum): ...

    def bufferData(self, target: GLenum, data: ArrayBuffer, usage: GLenum): ...

    def bufferData(self, target: GLenum, data: ArrayBufferView, usage: GLenum): ...

    def bufferSubData(self, target: GLenum, offset: GLintptr, data: ArrayBuffer): ...

    def bufferSubData(self, target: GLenum, offset: GLintptr, data: ArrayBufferView): ...

    def compressedTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei,
                             height: GLsizei, border: GLint, data: ArrayBufferView): ...

    def compressedTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei,
                                height: GLsizei, format: GLenum, data: ArrayBufferView): ...

    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum,
                   pixels: ArrayBufferView | None): ...

    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei,
                   border: GLint, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...

    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum,
                   pixels: ImageBitmap): ...

    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum,
                   pixels: ImageData): ...

    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum,
                   image: HTMLImageElement): ...

    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum,
                   canvas: HTMLCanvasElement): ...

    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum,
                   video: HTMLVideoElement): ...

    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum,
                   video_frame: VideoFrame): ...

    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei,
                      height: GLsizei, format: GLenum, type: GLenum, pixels: ArrayBufferView | None): ...

    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum,
                      pixels: ImageBitmap): ...

    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum,
                      pixels: ImageData): ...

    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum,
                      image: HTMLImageElement): ...

    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum,
                      canvas: HTMLCanvasElement): ...

    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum,
                      video: HTMLVideoElement): ...

    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum,
                      video_frame: VideoFrame): ...

    def uniform1fv(self, location: WebGLUniformLocation | None, data: Float32List): ...

    def uniform2fv(self, location: WebGLUniformLocation | None, data: Float32List): ...

    def uniform3fv(self, location: WebGLUniformLocation | None, data: Float32List): ...

    def uniform4fv(self, location: WebGLUniformLocation | None, data: Float32List): ...

    def uniform1iv(self, location: WebGLUniformLocation | None, data: Int32List): ...

    def uniform2iv(self, location: WebGLUniformLocation | None, data: Int32List): ...

    def uniform3iv(self, location: WebGLUniformLocation | None, data: Int32List): ...

    def uniform4iv(self, location: WebGLUniformLocation | None, data: Int32List): ...

    def uniformMatrix2fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List): ...

    def uniformMatrix3fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List): ...
    def uniformMatrix4fv(self, location: WebGLUniformLocation | None, transpose: GLboolean, data: Float32List): ...
    def commit(self): ...

class WEBGL_compressed_texture_s3tc: ...

class WEBGL_compressed_texture_s3tc_srgb: ...

class WEBGL_compressed_texture_astc: ...

class WEBGL_compressed_texture_atc: ...

class WEBGL_compressed_texture_etc: ...

class WEBGL_compressed_texture_etc1: ...

class WEBGL_compressed_texture_pvrtc: ...

class WEBGL_debug_renderer_info: ...

class WEBGL_debug_shaders:
    def getTranslatedShaderSource(self, shader: WebGLShader) -> str: ...

class WEBGL_depth_texture: ...

class OES_element_index_uint: ...

class EXT_frag_depth: ...

class WEBGL_lose_context:
    def loseContext(self): ...
    def restoreContext(self): ...

class EXT_texture_filter_anisotropic: ...

class EXT_sRGB: ...

class OES_standard_derivatives: ...

class OES_texture_float: ...

class WEBGL_draw_buffers: ...

class OES_texture_float_linear: ...

class EXT_shader_texture_lod: ...

class OES_texture_half_float: ...

class OES_texture_half_float_linear: ...

class WEBGL_color_buffer_float: ...

class EXT_color_buffer_half_float: ...

class OES_vertex_array_object:
    def createVertexArrayOES(self) -> WebGLVertexArrayObject | None: ...
    def deleteVertexArrayOES(self, arrayObject: WebGLVertexArrayObject | None): ...
    def isVertexArrayOES(self, arrayObject: WebGLVertexArrayObject | None) -> GLboolean: ...
    def bindVertexArrayOES(self, arrayObject: WebGLVertexArrayObject | None): ...

class ANGLE_instanced_arrays:
    def drawArraysInstancedANGLE(self, mode: GLenum, first: GLint, count: GLsizei, primcount: GLsizei): ...

    def drawElementsInstancedANGLE(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr,
                                   primcount: GLsizei): ...

    def vertexAttribDivisorANGLE(self, index: GLuint, divisor: GLuint): ...

class EXT_blend_minmax: ...

class WebGLQuery: ...

class EXT_disjoint_timer_query:
    def createQueryEXT(self) -> WebGLQuery | None: ...
    def deleteQueryEXT(self, query: WebGLQuery | None): ...
    def isQueryEXT(self, query: WebGLQuery | None) -> bool: ...
    def beginQueryEXT(self, target: GLenum, query: WebGLQuery): ...
    def endQueryEXT(self, target: GLenum): ...
    def queryCounterEXT(self, query: WebGLQuery, target: GLenum): ...

class MOZ_debug: ...

class ImageBitmapRenderingContext:
    def transferFromImageBitmap(self, bitmap: ImageBitmap): ...
    def transferImageBitmap(self, bitmap: ImageBitmap): ...

class RTCCertificate:
    expires: DOMTimeStamp


class SVGPathElement(SVGGeometryElement, SVGAnimatedPathData):
    def getPathSegAtLength(self, distance: float) -> int: ...

class AudioStreamTrack(MediaStreamTrack): ...


class WebSocket: ...

class InstallTriggerImpl:
    def enabled(self) -> bool: ...
    def updateEnabled(self) -> bool: ...
    def installChrome(self, type: int, url: str, skin: str) -> bool: ...
    def startSoftwareUpdate(self, url: str, flags: int | None = None) -> bool: ...


class HTMLLinkElement(HTMLElement, LinkStyle):
    disabled: bool
    href: str
    crossOrigin: str | None
    rel: str
    relList: DOMTokenList
    media: str
    hreflang: str
    type: str
    referrerPolicy: str
    sizes: DOMTokenList
    charset: str
    rev: str
    target: str
    integrity: str

class Credential:
    id: USVString
    type: str

class CredentialsContainer: ...

class NetworkInformation(EventTarget):
    type: ConnectionType
    ontypechange: EventHandler

class StyleSheetList:
    length: int


class ShadowRoot(DocumentFragment, DocumentOrShadowRoot):
    mode: ShadowRootMode
    host: Element

    def getElementById(self, elementId: str) -> Element | None: ...

    def getElementsByTagName(self, localName: str) -> HTMLCollection: ...

    def getElementsByTagNameNS(self, namespace: str | None, localName: str) -> HTMLCollection: ...

    def getElementsByClassName(self, classNames: str) -> HTMLCollection: ...

    innerHTML: str

class HTMLTableRowElement(HTMLElement):
    rowIndex: int
    sectionRowIndex: int
    cells: HTMLCollection
    def insertCell(self, index: int | None = -1) -> HTMLElement: ...
    def deleteCell(self, index: int): ...
    align: str
    ch: str
    chOff: str
    vAlign: str
    bgColor: str

class SVGFEPointLightElement(SVGElement):
    x: SVGAnimatedNumber
    y: SVGAnimatedNumber
    z: SVGAnimatedNumber

class WorkerDebuggerGlobalScope(EventTarget):
    def createSandbox(self, name: str, prototype: object) -> object: ...
    def loadSubScript(self, url: str, sandbox: object | None = None): ...
    def enterEventLoop(self): ...
    def leaveEventLoop(self): ...
    def postMessage(self, message: str): ...
    onmessage: EventHandler
    def setImmediate(self, handler: Function): ...
    def reportError(self, message: str): ...
    def setConsoleEventHandler(self, handler: AnyCallback | None): ...
    def dump(self, string: str | None = None): ...

class SVGForeignObjectElement(SVGGraphicsElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class HTMLPreElement(HTMLElement):
    width: int

class HTMLFieldSetElement(HTMLElement):
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

class MutationEvent(Event):
    relatedNode: Node | None
    prevValue: str
    newValue: str
    attrName: str
    attrChange: int

    def initMutationEvent(self, type: str, canBubble: bool | None = false, cancelable: bool | None = false,
                          relatedNode: Node | None = None, prevValue: str | None = "", newValue: str | None = "",
                          attrName: str | None = "", attrChange: int | None = 0): ...

class RTCDTMFSender(EventTarget):
    def insertDTMF(self, tones: str, duration: int | None = 100, interToneGap: int | None = 70): ...
    ontonechange: EventHandler
    toneBuffer: str


class SVGFETileElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString

class OfflineResourceList(EventTarget):
    status: int
    def update(self): ...
    def swapCache(self): ...
    onchecking: EventHandler
    onerror: EventHandler
    onnoupdate: EventHandler
    ondownloading: EventHandler
    onprogress: EventHandler
    onupdateready: EventHandler
    oncached: EventHandler
    onobsolete: EventHandler


class Navigator(NavigatorID, NavigatorLanguage, NavigatorOnLine, NavigatorContentUtils, NavigatorStorageUtils,
                NavigatorConcurrentHardware, NavigatorStorage, NavigatorAutomationInformation, NavigatorGeolocation,
                NavigatorGPU):
    permissions: Permissions
    mimeTypes: MimeTypeArray
    plugins: PluginArray
    doNotTrack: str

    def vibrate(self, duration: int) -> bool: ...

    maxTouchPoints: int
    mediaCapabilities: MediaCapabilities
    connection: NetworkInformation

    def requestGamepadServiceTest(self) -> GamepadServiceTest: ...

    isWebVRContentDetected: bool
    isWebVRContentPresenting: bool

    def requestVRPresentation(self, display: VRDisplay): ...

    def requestVRServiceTest(self) -> VRServiceTest: ...

    mediaDevices: MediaDevices
    serviceWorker: ServiceWorkerContainer

    def sendBeacon(self, url: str, data: BodyInit | None = None) -> bool: ...

    presentation: Presentation | None
    credentials: CredentialsContainer
    wakeLock: WakeLock
    xr: XRSystem
    mediaSession: MediaSession

    def canShare(self, data: ShareData | None = {}) -> bool: ...

    hid: HID
    usb: USB
    clipboard: Clipboard | None
    serial: Serial
    bluetooth: Bluetooth | None

class NavigatorAutomationInformation:
    webdriver: bool

class DOMRectList:
    length: int

class HTMLLabelElement(HTMLElement):
    form: HTMLFormElement | None
    htmlFor: str
    control: HTMLElement | None

class WEBGL_multi_draw: ...

class SVGSwitchElement(SVGGraphicsElement): ...

class AudioTrackList(EventTarget):
    length: int
    def getTrackById(self, id: str) -> AudioTrack | None: ...
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class AudioWorkletGlobalScope(WorkletGlobalScope):
    def registerProcessor(self, name: str, processorCtor: VoidFunction): ...

    currentFrame: int
    currentTime: float
    sampleRate: float


class HTMLAnchorElement(HTMLElement, HTMLHyperlinkElementUtils):
    target: str
    download: str
    ping: str
    rel: str
    referrerPolicy: str
    relList: DOMTokenList
    hreflang: str
    type: str
    text: str
    coords: str
    charset: str
    name: str
    rev: str
    shape: str

class HTMLOptGroupElement(HTMLElement):
    disabled: bool
    label: str


class Coordinates:
    latitude: float
    longitude: float
    altitude: float | None
    accuracy: float
    altitudeAccuracy: float | None
    heading: float | None
    speed: float | None


class KeyframeEffect: ...


class SVGFEDropShadowElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    dx: SVGAnimatedNumber
    dy: SVGAnimatedNumber
    stdDeviationX: SVGAnimatedNumber
    stdDeviationY: SVGAnimatedNumber

    def setStdDeviation(self, stdDeviationX: float, stdDeviationY: float): ...

class MediaQueryList(EventTarget):
    media: str
    matches: bool
    def addListener(self, listener: EventListener | None): ...
    def removeListener(self, listener: EventListener | None): ...
    onchange: EventHandler


class CanvasRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing, CanvasImageSmoothing,
                               CanvasFillStrokeStyles, CanvasShadowStyles, CanvasFilters, CanvasRect, CanvasDrawPath,
                               CanvasUserInterface, CanvasText, CanvasDrawImage, CanvasImageData,
                               CanvasPathDrawingStyles, CanvasTextDrawingStyles, CanvasPathMethods, CanvasHitRegions):
    canvas: HTMLCanvasElement | None

    def drawWindow(self, window: Window, x: float, y: float, w: float, h: float, bgColor: str,
                   flags: int | None = 0): ...

    def demote(self): ...


class CanvasGradient:
    def addColorStop(self, offset: float, color: str): ...

class CanvasPattern:
    def setTransform(self, matrix: SVGMatrix): ...


class TextMetrics:
    width: float
    actualBoundingBoxLeft: float
    actualBoundingBoxRight: float
    fontBoundingBoxAscent: float
    fontBoundingBoxDescent: float
    actualBoundingBoxAscent: float
    actualBoundingBoxDescent: float

class SVGDescElement(SVGElement): ...

class PerformanceServerTiming:
    name: str
    duration: DOMHighResTimeStamp
    description: str
    def toJSON(self) -> object: ...


class HTMLProgressElement(HTMLElement):
    value: float
    max: float
    position: float
    labels: NodeList

class ServiceWorkerGlobalScope(WorkerGlobalScope):
    clients: Clients
    registration: ServiceWorkerRegistration
    oninstall: EventHandler
    onactivate: EventHandler
    onfetch: EventHandler
    onmessage: EventHandler
    onpush: EventHandler
    onpushsubscriptionchange: EventHandler
    onnotificationclick: EventHandler
    onnotificationclose: EventHandler

class SVGTextPositioningElement(SVGTextContentElement):
    x: SVGAnimatedLengthList
    y: SVGAnimatedLengthList
    dx: SVGAnimatedLengthList
    dy: SVGAnimatedLengthList
    rotate: SVGAnimatedNumberList

class HTMLFrameElement(HTMLElement):
    name: str
    scrolling: str
    src: str
    frameBorder: str
    longDesc: str
    noResize: bool
    contentDocument: Document | None
    contentWindow: WindowProxy | None
    marginHeight: str
    marginWidth: str

class SVGAnimateElement(SVGAnimationElement): ...

class CSSFontFaceRule(CSSRule):
    style: CSSStyleDeclaration


class SVGFEDisplacementMapElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    scale: SVGAnimatedNumber
    xChannelSelector: SVGAnimatedEnumeration
    yChannelSelector: SVGAnimatedEnumeration

class HTMLTableElement(HTMLElement):
    caption: HTMLTableCaptionElement | None
    def createCaption(self) -> HTMLElement: ...
    def deleteCaption(self): ...
    tHead: HTMLTableSectionElement | None
    def createTHead(self) -> HTMLElement: ...
    def deleteTHead(self): ...
    tFoot: HTMLTableSectionElement | None
    def createTFoot(self) -> HTMLElement: ...
    def deleteTFoot(self): ...
    tBodies: HTMLCollection
    def createTBody(self) -> HTMLElement: ...
    rows: HTMLCollection
    def insertRow(self, index: int | None = -1) -> HTMLElement: ...
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

class External:
    def AddSearchProvider(self, aDescriptionURL: str): ...
    def IsSearchProviderInstalled(self, aSearchURL: str) -> int: ...


class HTMLStyleElement(HTMLElement, LinkStyle):
    disabled: bool
    media: str
    type: str

class HTMLObjectElement(HTMLElement):
    data: str
    type: str
    typeMustMatch: bool
    name: str
    useMap: str
    form: HTMLFormElement | None
    width: str
    height: str
    contentDocument: Document | None
    contentWindow: WindowProxy | None
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
    border: str
    def getSVGDocument(self) -> Document | None: ...


class Document(XPathEvaluator, GlobalEventHandlers, DocumentAndElementEventHandlers, TouchEventHandlers, ParentNode,
               OnErrorEventHandlerForNodes, GeometryUtils, FontFaceSource, DocumentOrShadowRoot):
    location: Location | None
    referrer: str
    lastModified: str
    readyState: str
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
    defaultView: WindowProxy | None
    def hasFocus(self) -> bool: ...
    onreadystatechange: EventHandler
    onbeforescriptexecute: EventHandler
    onafterscriptexecute: EventHandler
    onselectionchange: EventHandler
    currentScript: Element | None
    def releaseCapture(self): ...
    documentURIObject: URI | None
    referrerPolicy: int
    anchors: HTMLCollection
    applets: HTMLCollection
    fullscreen: bool
    fullscreenEnabled: bool
    def exitFullscreen(self): ...
    onfullscreenchange: EventHandler
    onfullscreenerror: EventHandler
    def exitPointerLock(self): ...
    onpointerlockchange: EventHandler
    onpointerlockerror: EventHandler
    hidden: bool
    visibilityState: VisibilityState
    onvisibilitychange: EventHandler
    selectedStyleSheetSet: str | None
    lastStyleSheetSet: str | None
    preferredStyleSheetSet: str | None
    styleSheetSets: DOMStringList

    def enableStyleSheetsForSet(self, name: str | None): ...

    def caretPositionFromPoint(self, x: float, y: float) -> CaretPosition | None: ...
    scrollingElement: Element | None
    def querySelector(self, selectors: str) -> Element | None: ...
    def querySelectorAll(self, selectors: str) -> NodeList: ...
    timeline: DocumentTimeline
    rootElement: SVGSVGElement | None
    isSrcdocDocument: bool
    sandboxFlagsAsString: str | None
    def insertAnonymousContent(self, aElement: Element) -> AnonymousContent: ...
    def removeAnonymousContent(self, aContent: AnonymousContent): ...
    def getSelection(self) -> Selection | None: ...
    userHasInteracted: bool
    def notifyUserGestureActivation(self): ...
    documentFlashClassification: FlashClassification


class SVGPolygonElement(SVGGeometryElement, SVGAnimatedPoints): ...

class PromiseNativeHandler: ...

class SVGLengthList:
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: SVGLength) -> SVGLength: ...
    def insertItemBefore(self, newItem: SVGLength, index: int) -> SVGLength: ...
    def replaceItem(self, newItem: SVGLength, index: int) -> SVGLength: ...
    def removeItem(self, index: int) -> SVGLength: ...
    def appendItem(self, newItem: SVGLength) -> SVGLength: ...

class AudioProcessingEvent(Event):
    playbackTime: float
    inputBuffer: AudioBuffer
    outputBuffer: AudioBuffer


class SVGGradientElement(SVGElement, SVGURIReference):
    gradientUnits: SVGAnimatedEnumeration
    gradientTransform: SVGAnimatedTransformList
    spreadMethod: SVGAnimatedEnumeration

class HTMLHeadElement(HTMLElement): ...

class SVGFEFuncBElement(SVGComponentTransferFunctionElement): ...

class XMLHttpRequestUpload(XMLHttpRequestEventTarget): ...

class HTMLDialogElement(HTMLElement):
    open: bool
    returnValue: str
    def show(self): ...
    def showModal(self): ...
    def close(self, returnValue: str | None = None): ...


class Animation:
    isRunningOnCompositor: bool

class TouchList:
    length: int

class IDBIndex:
    name: str
    objectStore: IDBObjectStore
    multiEntry: bool
    unique: bool
    locale: str | None
    isAutoLocale: bool

class SVGTextElement(SVGTextPositioningElement): ...

class SVGAnimatedInteger:
    baseVal: int
    animVal: int

class IDBKeyRange:
    lowerOpen: bool
    upperOpen: bool

class IDBLocaleAwareKeyRange(IDBKeyRange): ...

class SVGGeometryElement(SVGGraphicsElement):
    pathLength: SVGAnimatedNumber

    def getTotalLength(self) -> float: ...

    def getPointAtLength(self, distance: float) -> SVGPoint: ...

class SVGStringList:
    length: int
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: str) -> str: ...
    def getItem(self, index: int) -> str: ...
    def insertItemBefore(self, newItem: str, index: int) -> str: ...
    def replaceItem(self, newItem: str, index: int) -> str: ...
    def removeItem(self, index: int) -> str: ...
    def appendItem(self, newItem: str) -> str: ...

class Performance(EventTarget):
    def now(self) -> DOMHighResTimeStamp: ...
    timeOrigin: DOMHighResTimeStamp
    timing: PerformanceTiming
    navigation: PerformanceNavigation
    def toJSON(self) -> object: ...
    def getEntries(self) -> PerformanceEntryList: ...
    def getEntriesByType(self, entryType: str) -> PerformanceEntryList: ...
    def getEntriesByName(self, name: str, entryType: str | None = None) -> PerformanceEntryList: ...
    def clearResourceTimings(self): ...
    def setResourceTimingBufferSize(self, maxSize: int): ...
    onresourcetimingbufferfull: EventHandler
    def mark(self, markName: str): ...
    def clearMarks(self, markName: str | None = None): ...
    def measure(self, measureName: str, startMark: str | None = None, endMark: str | None = None): ...
    def clearMeasures(self, measureName: str | None = None): ...


class SVGTextPathElement(SVGTextContentElement, SVGURIReference):
    startOffset: SVGAnimatedLength
    method: SVGAnimatedEnumeration
    spacing: SVGAnimatedEnumeration

class SpeechSynthesis(EventTarget):
    pending: bool
    speaking: bool
    paused: bool
    def speak(self, utterance: SpeechSynthesisUtterance): ...
    def cancel(self): ...
    def pause(self): ...
    def resume(self): ...
    onvoiceschanged: EventHandler
    def forceEnd(self): ...

class PushManager: ...

class MediaCapabilitiesInfo:
    supported: bool
    smooth: bool
    powerEfficient: bool

class MediaCapabilities: ...

class HTMLDivElement(HTMLElement):
    align: str

class TreeView:
    rowCount: int
    selection: nsITreeSelection | None
    def getRowProperties(self, row: int) -> str: ...
    def getCellProperties(self, row: int, column: TreeColumn) -> str: ...
    def getColumnProperties(self, column: TreeColumn) -> str: ...
    def isContainer(self, row: int) -> bool: ...
    def isContainerOpen(self, row: int) -> bool: ...
    def isContainerEmpty(self, row: int) -> bool: ...
    def isSeparator(self, row: int) -> bool: ...
    def isSorted(self) -> bool: ...
    def canDrop(self, row: int, orientation: int, dataTransfer: DataTransfer | None) -> bool: ...
    def drop(self, row: int, orientation: int, dataTransfer: DataTransfer | None): ...
    def getParentIndex(self, row: int) -> int: ...
    def hasNextSibling(self, row: int, afterIndex: int) -> bool: ...
    def getLevel(self, row: int) -> int: ...
    def getImageSrc(self, row: int, column: TreeColumn) -> str: ...
    def getCellValue(self, row: int, column: TreeColumn) -> str: ...
    def getCellText(self, row: int, column: TreeColumn) -> str: ...
    def setTree(self, tree: TreeBoxObject | None): ...
    def toggleOpenState(self, row: int): ...
    def cycleHeader(self, column: TreeColumn): ...
    def selectionChanged(self): ...
    def cycleCell(self, row: int, column: TreeColumn): ...
    def isEditable(self, row: int, column: TreeColumn) -> bool: ...
    def isSelectable(self, row: int, column: TreeColumn) -> bool: ...
    def setCellValue(self, row: int, column: TreeColumn, value: str): ...
    def setCellText(self, row: int, column: TreeColumn, value: str): ...
    def performAction(self, action: str): ...
    def performActionOnRow(self, action: str, row: int): ...
    def performActionOnCell(self, action: str, row: int, column: TreeColumn): ...

class HTMLLIElement(HTMLElement):
    value: int
    type: str

class MediaStreamError:
    name: str
    message: str | None
    constraint: str | None


class SVGAnimatedNumber:
    baseVal: float
    animVal: float

class PushSubscription:
    endpoint: USVString
    options: PushSubscriptionOptions
    def getKey(self, name: PushEncryptionKeyName) -> ArrayBuffer: ...
    def toJSON(self) -> PushSubscriptionJSON: ...

class HTMLSlotElement(HTMLElement):
    name: str

class SVGMaskElement(SVGElement):
    maskUnits: SVGAnimatedEnumeration
    maskContentUnits: SVGAnimatedEnumeration
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength


class SVGSymbolElement(SVGElement, SVGFitToViewBox, SVGTests): ...


class SVGViewElement(SVGElement, SVGFitToViewBox, SVGZoomAndPanValues): ...

class IDBFileHandle(EventTarget):
    mutableFile: IDBMutableFile | None
    fileHandle: IDBMutableFile | None
    mode: FileMode
    active: bool
    location: int | None
    def getMetadata(self, parameters: IDBFileMetadataParameters | None = {}) -> IDBFileRequest | None: ...
    def readAsArrayBuffer(self, size: int) -> IDBFileRequest | None: ...
    def readAsText(self, size: int, encoding: str | None = None) -> IDBFileRequest | None: ...
    def write(self, value: str | ArrayBuffer | ArrayBufferView | Blob) -> IDBFileRequest | None: ...
    def append(self, value: str | ArrayBuffer | ArrayBufferView | Blob) -> IDBFileRequest | None: ...
    def truncate(self, size: int | None = None) -> IDBFileRequest | None: ...
    def flush(self) -> IDBFileRequest | None: ...
    def abort(self): ...
    oncomplete: EventHandler
    onabort: EventHandler
    onerror: EventHandler

class NodeIterator:
    root: Node
    referenceNode: Node | None
    pointerBeforeReferenceNode: bool
    whatToShow: int
    filter: NodeFilter | None
    def nextNode(self) -> Node | None: ...
    def previousNode(self) -> Node | None: ...
    def detach(self): ...

class ReadableStream:
    locked: bool

    def getReader(self, options: ReadableStreamGetReaderOptions | None = {}) -> ReadableStreamReader: ...

    def pipeThrough(self, transform: ReadableWritablePair,
                    options: StreamPipeOptions | None = {}) -> ReadableStream: ...


class ReadableStreamDefaultReader(ReadableStreamGenericReader):
    def releaseLock(self): ...


class ReadableStreamBYOBReader(ReadableStreamGenericReader):
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
    locked: bool
    def getWriter(self) -> WritableStreamDefaultWriter: ...

class WritableStreamDefaultWriter:
    desiredSize: float | None
    def releaseLock(self): ...

class WritableStreamDefaultController:
    signal: AbortSignal

class TransformStream:
    readable: ReadableStream
    writable: WritableStream

class TransformStreamDefaultController:
    desiredSize: float | None
    def terminate(self): ...

class ByteLengthQueuingStrategy:
    highWaterMark: float
    size: Function

class CountQueuingStrategy:
    highWaterMark: float
    size: Function

class HTMLModElement(HTMLElement):
    cite: str
    dateTime: str

class SVGNumberList:
    numberOfItems: int
    def clear(self): ...
    def initialize(self, newItem: SVGNumber) -> SVGNumber: ...
    def insertItemBefore(self, newItem: SVGNumber, index: int) -> SVGNumber: ...
    def replaceItem(self, newItem: SVGNumber, index: int) -> SVGNumber: ...
    def removeItem(self, index: int) -> SVGNumber: ...
    def appendItem(self, newItem: SVGNumber) -> SVGNumber: ...

class RTCStatsReport: ...

class GamepadButton:
    pressed: bool
    touched: bool
    value: float

class Gamepad:
    id: str
    index: int
    mapping: GamepadMappingType
    hand: GamepadHand
    displayId: int
    connected: bool
    timestamp: DOMHighResTimeStamp
    pose: GamepadPose | None

class HTMLFontElement(HTMLElement):
    color: str
    face: str
    size: str


class SVGNumber:
    value: float

class CSSPageRule(CSSRule):
    style: CSSStyleDeclaration

class ConsoleInstance:
    def clear(self): ...
    def count(self, label: str | None = "default"): ...
    def countReset(self, label: str | None = "default"): ...
    def groupEnd(self): ...
    def time(self, label: str | None = "default"): ...

    def timeEnd(self, label: str | None = "default"): ...

    def reportForServiceWorkerScope(self, scope: str, message: str, filename: str, lineNumber: int, columnNumber: int,
                                    level: ConsoleLevel): ...


class SVGMarkerElement(SVGElement, SVGFitToViewBox):
    refX: SVGAnimatedLength
    refY: SVGAnimatedLength
    markerUnits: SVGAnimatedEnumeration
    markerWidth: SVGAnimatedLength
    markerHeight: SVGAnimatedLength
    orientType: SVGAnimatedEnumeration
    orientAngle: SVGAnimatedAngle

    def setOrientToAuto(self): ...

    def setOrientToAngle(self, angle: SVGAngle): ...

class BarProp:
    visible: bool


class SVGElement(Element, GlobalEventHandlers, DocumentAndElementEventHandlers, TouchEventHandlers,
                 OnErrorEventHandlerForNodes):
    id: str
    className: SVGAnimatedString
    dataset: DOMStringMap
    style: CSSStyleDeclaration
    ownerSVGElement: SVGSVGElement | None
    viewportElement: SVGElement | None
    tabIndex: int

    def focus(self): ...

    def blur(self): ...


class AudioParam:
    value: float
    defaultValue: float
    minValue: float
    maxValue: float

    def setValueAtTime(self, value: float, startTime: float) -> AudioParam: ...

    def linearRampToValueAtTime(self, value: float, endTime: float) -> AudioParam: ...

    def exponentialRampToValueAtTime(self, value: float, endTime: float) -> AudioParam: ...

    def setTargetAtTime(self, target: float, startTime: float, timeConstant: float) -> AudioParam: ...

    def setValueCurveAtTime(self, values: Float32Array, startTime: float, duration: float) -> AudioParam: ...

    def cancelScheduledValues(self, startTime: float) -> AudioParam: ...


class WorkerGlobalScope(EventTarget, GlobalCrypto, WindowOrWorkerGlobalScope):
    self: WorkerGlobalScope
    location: WorkerLocation
    navigator: WorkerNavigator

    def importScripts(self, urls: str | None = None): ...

    onerror: OnErrorEventHandler
    onoffline: EventHandler
    ononline: EventHandler

class SVGFEFuncGElement(SVGComponentTransferFunctionElement): ...

class PaymentAddress:
    def toJSON(self) -> object: ...
    country: str
    region: str
    city: str
    dependentLocality: str
    postalCode: str
    sortingCode: str
    languageCode: str
    organization: str
    recipient: str
    phone: str

class FontFaceSetIterator:
    def next(self) -> FontFaceSetIteratorResult: ...

class FontFaceSet(EventTarget):
    size: int
    def add(self, font: FontFace): ...
    def has(self, font: FontFace) -> bool: ...
    def delete(self, font: FontFace) -> bool: ...
    def clear(self): ...
    def entries(self) -> FontFaceSetIterator: ...
    def values(self) -> FontFaceSetIterator: ...
    onloading: EventHandler
    onloadingdone: EventHandler
    onloadingerror: EventHandler
    def check(self, font: str, text: str | None = " ") -> bool: ...
    status: FontFaceSetLoadStatus


class DocumentType(Node, ChildNode):
    name: str
    publicId: str
    systemId: str

class PresentationConnection(EventTarget):
    id: str
    url: str
    state: PresentationConnectionState
    onconnect: EventHandler
    onclose: EventHandler
    onterminate: EventHandler
    binaryType: PresentationConnectionBinaryType
    def send(self, data: str): ...
    def send(self, data: Blob): ...
    def send(self, data: ArrayBuffer): ...
    def send(self, data: ArrayBufferView): ...
    onmessage: EventHandler
    def close(self): ...
    def terminate(self): ...

class HTMLTableColElement(HTMLElement):
    span: int
    align: str
    ch: str
    chOff: str
    vAlign: str
    width: str

class SVGAnimatedLengthList:
    baseVal: SVGLengthList
    animVal: SVGLengthList

class PerformanceObserverEntryList:
    def getEntries(self, filter: PerformanceEntryFilterOptions | None = None) -> PerformanceEntryList: ...
    def getEntriesByType(self, entryType: str) -> PerformanceEntryList: ...
    def getEntriesByName(self, name: str, entryType: str | None = None) -> PerformanceEntryList: ...


class SVGGraphicsElement(SVGElement, SVGTests):
    transform: SVGAnimatedTransformList
    nearestViewportElement: SVGElement | None
    farthestViewportElement: SVGElement | None

    def getBBox(self, aOptions: SVGBoundingBoxOptions | None = None) -> SVGRect: ...

    def getCTM(self) -> SVGMatrix | None: ...

    def getScreenCTM(self) -> SVGMatrix | None: ...

    def getTransformToElement(self, element: SVGGraphicsElement) -> SVGMatrix: ...

class HTMLParamElement(HTMLElement):
    name: str
    value: str
    type: str
    valueType: str

class SVGFEFuncRElement(SVGComponentTransferFunctionElement): ...

class NodeList:
    length: int

class IDBFactory:
    def open(self, name: str, version: int) -> IDBOpenDBRequest: ...

    def open(self, name: str, options: IDBOpenDBOptions | None = {}) -> IDBOpenDBRequest: ...

    def deleteDatabase(self, name: str, options: IDBOpenDBOptions | None = {}) -> IDBOpenDBRequest: ...

    def openForPrincipal(self, principal: Principal, name: str, version: int) -> IDBOpenDBRequest: ...

    def openForPrincipal(self, principal: Principal, name: str,
                         options: IDBOpenDBOptions | None = {}) -> IDBOpenDBRequest: ...

    def deleteForPrincipal(self, principal: Principal, name: str,
                           options: IDBOpenDBOptions | None = {}) -> IDBOpenDBRequest: ...

class DedicatedWorkerGlobalScope(WorkerGlobalScope):
    name: str
    def close(self): ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class CacheStorage: ...

class PositionError:
    code: int
    message: str

class Presentation:
    defaultRequest: PresentationRequest | None
    receiver: PresentationReceiver | None

class VideoStreamTrack(MediaStreamTrack): ...

class MediaKeys:
    keySystem: str
    def createSession(self, sessionType: MediaKeySessionType | None = "temporary") -> MediaKeySession: ...

class SVGAnimatedAngle:
    baseVal: SVGAngle
    animVal: SVGAngle

class HTMLAllCollection:
    length: int
    def item(self, index: int) -> Node | None: ...
    def item(self, name: str) -> Node | HTMLCollection | None: ...

class HTMLCanvasElement(HTMLElement):
    width: int
    height: int
    def transferControlToOffscreen(self) -> OffscreenCanvas: ...

class GamepadServiceTest:
    noMapping: GamepadMappingType
    standardMapping: GamepadMappingType
    noHand: GamepadHand
    leftHand: GamepadHand
    rightHand: GamepadHand

    def removeGamepad(self, index: int): ...

    def newButtonEvent(self, index: int, button: int, pressed: bool, touched: bool): ...

    def newButtonValueEvent(self, index: int, button: int, pressed: bool, touched: bool, value: float): ...

    def newAxisMoveEvent(self, index: int, axis: int, value: float): ...

    def newPoseMove(self, index: int, orient: Float32Array, pos: Float32Array, angVelocity: Float32Array,
                    angAcceleration: Float32Array, linVelocity: Float32Array, linAcceleration: Float32Array): ...

class AbortSignal(EventTarget):
    aborted: bool
    onabort: EventHandler

class FileSystemFileEntry(FileSystemEntry):
    def file(self, successCallback: FileCallback, errorCallback: ErrorCallback | None = None): ...


class HTMLAreaElement(HTMLElement, HTMLHyperlinkElementUtils):
    alt: str
    coords: str
    shape: str
    target: str
    download: str
    ping: str
    rel: str
    referrerPolicy: str
    relList: DOMTokenList
    noHref: bool

class IDBTransaction(EventTarget):
    mode: IDBTransactionMode
    db: IDBDatabase
    error: DOMException | None
    def objectStore(self, name: str) -> IDBObjectStore: ...
    def commit(self): ...
    def abort(self): ...
    onabort: EventHandler
    oncomplete: EventHandler
    onerror: EventHandler
    objectStoreNames: DOMStringList

class CSSConditionRule(CSSGroupingRule):
    conditionText: str

class SVGFEDistantLightElement(SVGElement):
    azimuth: SVGAnimatedNumber
    elevation: SVGAnimatedNumber

class PresentationConnectionList(EventTarget):
    onconnectionavailable: EventHandler


class SVGMPathElement(SVGElement, SVGURIReference): ...

class HTMLParagraphElement(HTMLElement):
    align: str

class RTCIdentityProviderRegistrar:
    def register(self, idp: RTCIdentityProvider): ...
    hasIdp: bool

class IDBCursor:
    source: IDBObjectStore | IDBIndex
    direction: IDBCursorDirection
    request: IDBRequest
    def advance(self, count: int): ...
    def delete(self) -> IDBRequest: ...

class IDBCursorWithValue(IDBCursor): ...

class HTMLTitleElement(HTMLElement):
    text: str

class CSSTransition(Animation):
    transitionProperty: str

class HTMLUListElement(HTMLElement):
    compact: bool
    type: str

class DOMStringList:
    length: int
    def contains(self, string: str) -> bool: ...

class TextTrackList(EventTarget):
    length: int
    def getTrackById(self, id: str) -> TextTrack | None: ...
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class HTMLTrackElement(HTMLElement):
    kind: str
    src: str
    srclang: str
    label: str
    default: bool
    readyState: int
    track: TextTrack | None


class SVGPoint:
    x: float
    y: float

    def matrixTransform(self, matrix: SVGMatrix) -> SVGPoint: ...

class AnimationEffect:
    def getTiming(self) -> EffectTiming: ...
    def getComputedTiming(self) -> ComputedEffectTiming: ...
    def updateTiming(self, timing: OptionalEffectTiming | None = None): ...

class XPathExpression: ...

class ServiceWorkerContainer(EventTarget):
    controller: ServiceWorker | None
    oncontrollerchange: EventHandler
    onerror: EventHandler
    onmessage: EventHandler
    def getScopeForUrl(self, url: str) -> str: ...

class CanvasCaptureMediaStream(MediaStream):
    canvas: HTMLCanvasElement
    def requestFrame(self): ...

class SVGLineElement(SVGGeometryElement):
    x1: SVGAnimatedLength
    y1: SVGAnimatedLength
    x2: SVGAnimatedLength
    y2: SVGAnimatedLength

class MIDIInputMap: ...

class MediaError:
    code: int
    message: str

class SVGTextContentElement(SVGGraphicsElement):
    textLength: SVGAnimatedLength
    lengthAdjust: SVGAnimatedEnumeration

    def getNumberOfChars(self) -> int: ...

    def getComputedTextLength(self) -> float: ...

    def getSubStringLength(self, charnum: int, nchars: int) -> float: ...

    def getStartPositionOfChar(self, charnum: int) -> SVGPoint: ...

    def getEndPositionOfChar(self, charnum: int) -> SVGPoint: ...

    def getExtentOfChar(self, charnum: int) -> SVGRect: ...

    def getRotationOfChar(self, charnum: int) -> float: ...

    def getCharNumAtPosition(self, point: SVGPoint) -> int: ...

    def selectSubString(self, charnum: int, nchars: int): ...

class SpeechRecognitionAlternative:
    transcript: str
    confidence: float

class AudioNode(EventTarget):
    def connect(self, destination: AudioNode, output: int | None = 0, input: int | None = 0) -> AudioNode: ...
    def connect(self, destination: AudioParam, output: int | None = 0): ...
    def disconnect(self): ...
    def disconnect(self, output: int): ...
    def disconnect(self, destination: AudioNode): ...
    def disconnect(self, destination: AudioNode, output: int): ...
    def disconnect(self, destination: AudioNode, output: int, input: int): ...
    def disconnect(self, destination: AudioParam): ...
    def disconnect(self, destination: AudioParam, output: int): ...
    context: BaseAudioContext
    numberOfInputs: int
    numberOfOutputs: int
    channelCount: int
    channelCountMode: ChannelCountMode
    channelInterpretation: ChannelInterpretation

class GamepadPose:
    hasOrientation: bool
    hasPosition: bool
    position: Float32Array
    linearVelocity: Float32Array
    linearAcceleration: Float32Array
    orientation: Float32Array
    angularVelocity: Float32Array
    angularAcceleration: Float32Array

class HTMLBRElement(HTMLElement):
    clear: str

class U2F: ...

class IDBVersionChangeEvent(Event):
    oldVersion: int
    newVersion: int | None

class FuzzingFunctions: ...

class PresentationReceiver: ...

class RTCRtpTransceiver:
    mid: str | None
    sender: RTCRtpSender
    receiver: RTCRtpReceiver
    stopped: bool
    direction: RTCRtpTransceiverDirection
    currentDirection: RTCRtpTransceiverDirection | None
    def stop(self): ...
    def setRemoteTrackId(self, trackId: str): ...
    def remoteTrackIdIs(self, trackId: str) -> bool: ...
    def getRemoteTrackId(self) -> str: ...
    def setAddTrackMagic(self): ...
    addTrackMagic: bool
    shouldRemove: bool
    def setCurrentDirection(self, direction: RTCRtpTransceiverDirection): ...
    def setDirectionInternal(self, direction: RTCRtpTransceiverDirection): ...
    def setMid(self, mid: str): ...
    def unsetMid(self): ...
    def setStopped(self): ...
    def getKind(self) -> str: ...
    def hasBeenUsedToSend(self) -> bool: ...
    def sync(self): ...
    def insertDTMF(self, tones: str, duration: int | None = 100, interToneGap: int | None = 70): ...

class WorkerLocation:
    href: USVString
    origin: USVString
    protocol: USVString
    host: USVString
    hostname: USVString
    port: USVString
    pathname: USVString
    search: USVString
    hash: USVString

class WorkletGlobalScope: ...

class SVGAnimateMotionElement(SVGAnimationElement): ...


class DataTransfer: ...

class CaretPosition:
    offsetNode: Node | None
    offset: int
    def getClientRect(self) -> DOMRect | None: ...

class SVGAnimatedNumberList:
    baseVal: SVGNumberList
    animVal: SVGNumberList

class RadioNodeList(NodeList):
    value: str

class VideoTrackList(EventTarget):
    length: int
    def getTrackById(self, id: str) -> VideoTrack | None: ...
    selectedIndex: int
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class ServiceWorkerRegistration(EventTarget):
    installing: ServiceWorker | None
    waiting: ServiceWorker | None
    active: ServiceWorker | None
    scope: USVString
    updateViaCache: ServiceWorkerUpdateViaCache
    onupdatefound: EventHandler
    pushManager: PushManager


class HTMLBodyElement(HTMLElement, WindowEventHandlers):
    text: str
    link: str
    vLink: str
    aLink: str
    bgColor: str
    background: str

class IDBFileRequest(DOMRequest):
    fileHandle: IDBFileHandle | None
    lockedFile: IDBFileHandle | None
    onprogress: EventHandler

class NotifyPaintEvent(Event):
    clientRects: DOMRectList
    boundingClientRect: DOMRect
    paintRequests: PaintRequestList
    transactionId: int
    paintTimeStamp: DOMHighResTimeStamp

class IntlUtils: ...


class DeviceAcceleration:
    x: float | None
    y: float | None
    z: float | None


class DeviceRotationRate:
    alpha: float | None
    beta: float | None
    gamma: float | None

class SVGDefsElement(SVGGraphicsElement): ...

class Worklet: ...

class Location:
    href: USVString
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
    def reload(self, forceget: bool | None = false): ...

class SpeechRecognitionResultList:
    length: int


class SVGRect:
    x: float
    y: float
    width: float
    height: float

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

class HTMLFormControlsCollection(HTMLCollection): ...

class VideoTrack:
    id: str
    kind: str
    label: str
    language: str
    selected: bool
    sourceBuffer: SourceBuffer | None

class Permissions: ...

class HTMLMediaElement(HTMLElement):
    error: MediaError | None
    src: str
    currentSrc: str
    srcObject: MediaStream | None
    crossOrigin: str | None
    networkState: int
    preload: str
    buffered: TimeRanges

    def load(self): ...

    def canPlayType(self, type: str) -> str: ...

    readyState: int
    seeking: bool
    currentTime: float

    def fastSeek(self, time: float): ...

    duration: float
    isEncrypted: bool
    paused: bool
    defaultPlaybackRate: float
    playbackRate: float
    played: TimeRanges
    seekable: TimeRanges
    ended: bool
    autoplay: bool
    loop: bool

    def pause(self): ...

    controls: bool
    volume: float
    muted: bool
    defaultMuted: bool
    audioTracks: AudioTrackList
    videoTracks: VideoTrackList
    textTracks: TextTrackList | None
    def addTextTrack(self, kind: TextTrackKind, label: str | None = "", language: str | None = "") -> TextTrack: ...
    mediaKeys: MediaKeys | None
    onencrypted: EventHandler
    onwaitingforkey: EventHandler
    def setVisible(self, aVisible: bool): ...
    def hasSuspendTaint(self) -> bool: ...

class CreateOfferRequest:
    windowID: int
    innerWindowID: int
    callID: str
    isSecure: bool

class PerformanceMark(PerformanceEntry): ...

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

class SVGAnimatedPreserveAspectRatio:
    baseVal: SVGPreserveAspectRatio
    animVal: SVGPreserveAspectRatio

class ImageBitmap:
    width: int
    height: int
    def close(self): ...

class KeyEvent:
    def initKeyEvent(self, type: str, canBubble: bool | None = false, cancelable: bool | None = false,
                     view: Window | None = None, ctrlKey: bool | None = false, altKey: bool | None = false,
                     shiftKey: bool | None = false, metaKey: bool | None = false, keyCode: int | None = 0,
                     charCode: int | None = 0): ...

class WakeLock: ...

class WakeLockSentinel(EventTarget):
    released: bool
    type: WakeLockType
    onrelease: EventHandler

class XRSystem(EventTarget):
    ondevicechange: EventHandler

class XRSession(EventTarget):
    visibilityState: XRVisibilityState
    frameRate: float | None
    supportedFrameRates: Float32Array
    renderState: XRRenderState
    inputSources: XRInputSourceArray
    def updateRenderState(self, state: XRRenderStateInit | None = {}): ...
    def requestAnimationFrame(self, callback: XRFrameRequestCallback) -> int: ...
    def cancelAnimationFrame(self, handle: int): ...
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


class XRRenderState:
    depthNear: float
    depthFar: float
    inlineVerticalFieldOfView: float | None
    baseLayer: XRWebGLLayer | None


class XRFrame:
    session: XRSession
    predictedDisplayTime: DOMHighResTimeStamp

    def getViewerPose(self, referenceSpace: XRReferenceSpace) -> XRViewerPose | None: ...

    def getPose(self, space: XRSpace, baseSpace: XRSpace) -> XRPose | None: ...

    def getJointPose(self, joint: XRJointSpace, baseSpace: XRSpace) -> XRJointPose | None: ...

class XRSpace(EventTarget): ...

class XRReferenceSpace(XRSpace):
    def getOffsetReferenceSpace(self, originOffset: XRRigidTransform) -> XRReferenceSpace: ...
    onreset: EventHandler

class XRBoundedReferenceSpace(XRReferenceSpace): ...

class XRView:
    eye: XREye
    projectionMatrix: Float32Array
    transform: XRRigidTransform
    recommendedViewportScale: float | None

    def requestViewportScale(self, scale: float | None): ...

class XRViewport:
    x: int
    y: int
    width: int
    height: int

class XRRigidTransform:
    position: DOMPointReadOnly
    orientation: DOMPointReadOnly
    matrix: Float32Array
    inverse: XRRigidTransform

class XRPose:
    transform: XRRigidTransform
    linearVelocity: DOMPointReadOnly | None
    angularVelocity: DOMPointReadOnly | None
    emulatedPosition: bool

class XRViewerPose(XRPose): ...


class XRInputSource:
    handedness: XRHandedness
    targetRayMode: XRTargetRayMode
    targetRaySpace: XRSpace
    gripSpace: XRSpace | None
    hand: XRHand | None
    gamepad: Gamepad | None

class XRInputSourceArray:
    length: int

class XRLayer(EventTarget): ...

class XRWebGLLayer(XRLayer):
    antialias: bool
    ignoreDepthValues: bool
    fixedFoveation: float | None
    framebuffer: WebGLFramebuffer | None
    framebufferWidth: int
    framebufferHeight: int
    def getViewport(self, view: XRView) -> XRViewport | None: ...

class XRSessionEvent(Event):
    session: XRSession

class XRInputSourceEvent(Event):
    frame: XRFrame
    inputSource: XRInputSource

class XRInputSourcesChangeEvent(Event):
    session: XRSession

class XRReferenceSpaceEvent(Event):
    referenceSpace: XRReferenceSpace
    transform: XRRigidTransform | None

class XRPermissionStatus(PermissionStatus): ...

class MediaStreamTrackGenerator(MediaStreamTrack):
    writable: WritableStream

class MediaStreamTrackProcessor:
    readable: ReadableStream

class MediaSession:
    metadata: MediaMetadata | None
    playbackState: MediaSessionPlaybackState
    def setActionHandler(self, action: MediaSessionAction, handler: MediaSessionActionHandler | None): ...
    def setPositionState(self, state: MediaPositionState | None = {}): ...
    def setMicrophoneActive(self, active: bool): ...
    def setCameraActive(self, active: bool): ...

class MediaMetadata:
    title: str
    artist: str
    album: str

class XRHand:
    size: int
    def get(self, key: XRHandJoint) -> XRJointSpace: ...

class XRJointSpace(XRSpace):
    jointName: XRHandJoint


class XRJointPose(XRPose):
    radius: float

class HID(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler

class HIDConnectionEvent(Event):
    device: HIDDevice

class HIDInputReportEvent(Event):
    device: HIDDevice
    reportId: octet
    data: DataView

class HIDDevice(EventTarget):
    oninputreport: EventHandler
    opened: bool
    vendorId: int
    productId: int
    productName: str

class USB(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler

class USBConnectionEvent(Event):
    device: USBDevice

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
    opened: bool

class USBInTransferResult:
    data: DataView
    status: USBTransferStatus

class USBOutTransferResult:
    bytesWritten: int
    status: USBTransferStatus

class USBIsochronousInTransferPacket:
    data: DataView
    status: USBTransferStatus

class USBIsochronousInTransferResult:
    data: DataView

class USBIsochronousOutTransferPacket:
    bytesWritten: int
    status: USBTransferStatus

class USBIsochronousOutTransferResult: ...

class USBConfiguration:
    configurationValue: octet
    configurationName: str | None

class USBInterface:
    interfaceNumber: octet
    alternate: USBAlternateInterface
    claimed: bool

class USBAlternateInterface:
    alternateSetting: octet
    interfaceClass: octet
    interfaceSubclass: octet
    interfaceProtocol: octet
    interfaceName: str | None

class USBEndpoint:
    endpointNumber: octet
    direction: USBDirection
    type: USBEndpointType
    packetSize: int

class USBPermissionResult(PermissionStatus): ...

class ClipboardEvent(Event):
    clipboardData: DataTransfer | None

class Clipboard(EventTarget): ...

class ClipboardItem:
    presentationStyle: PresentationStyle
    lastModified: int
    delayed: bool

class ResizeObserver:
    def observe(self, target: Element, options: ResizeObserverOptions | None = {}): ...
    def unobserve(self, target: Element): ...
    def disconnect(self): ...

class ResizeObserverEntry:
    target: Element
    contentRect: DOMRectReadOnly


class ResizeObserverSize:
    inlineSize: float
    blockSize: float

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
    maxColorAttachmentBytesPerPixel: int
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

class GPU:
    def getPreferredCanvasFormat(self) -> GPUTextureFormat: ...

class GPUAdapter:
    features: GPUSupportedFeatures
    limits: GPUSupportedLimits
    isFallbackAdapter: bool


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

    def createCommandEncoder(self, descriptor: GPUCommandEncoderDescriptor | None = {}) -> GPUCommandEncoder: ...

    def createRenderBundleEncoder(self, descriptor: GPURenderBundleEncoderDescriptor) -> GPURenderBundleEncoder: ...

    def createQuerySet(self, descriptor: GPUQuerySetDescriptor) -> GPUQuerySet: ...

    def pushErrorScope(self, filter: GPUErrorFilter): ...

    onuncapturederror: EventHandler


class GPUBuffer(GPUObjectBase):
    size: GPUSize64
    usage: GPUBufferUsageFlags
    mapState: GPUBufferMapState

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


class GPUShaderModule(GPUObjectBase): ...

class GPUCompilationMessage:
    message: str
    type: GPUCompilationMessageType
    lineNum: int
    linePos: int
    offset: int
    length: int

class GPUCompilationInfo: ...


class GPUComputePipeline(GPUObjectBase, GPUPipelineBase): ...


class GPURenderPipeline(GPUObjectBase, GPUPipelineBase): ...


class GPUCommandBuffer(GPUObjectBase): ...


class GPUCommandEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin):
    def beginRenderPass(self, descriptor: GPURenderPassDescriptor) -> GPURenderPassEncoder: ...

    def beginComputePass(self, descriptor: GPUComputePassDescriptor | None = {}) -> GPUComputePassEncoder: ...

    def copyBufferToBuffer(self, source: GPUBuffer, sourceOffset: GPUSize64, destination: GPUBuffer,
                           destinationOffset: GPUSize64, size: GPUSize64): ...

    def copyBufferToTexture(self, source: GPUImageCopyBuffer, destination: GPUImageCopyTexture,
                            copySize: GPUExtent3D): ...

    def copyTextureToBuffer(self, source: GPUImageCopyTexture, destination: GPUImageCopyBuffer,
                            copySize: GPUExtent3D): ...

    def copyTextureToTexture(self, source: GPUImageCopyTexture, destination: GPUImageCopyTexture,
                             copySize: GPUExtent3D): ...

    def clearBuffer(self, buffer: GPUBuffer, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...

    def writeTimestamp(self, querySet: GPUQuerySet, queryIndex: GPUSize32): ...

    def resolveQuerySet(self, querySet: GPUQuerySet, firstQuery: GPUSize32, queryCount: GPUSize32,
                        destination: GPUBuffer, destinationOffset: GPUSize64): ...

    def finish(self, descriptor: GPUCommandBufferDescriptor | None = {}) -> GPUCommandBuffer: ...


class GPUComputePassEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin):
    def setPipeline(self, pipeline: GPUComputePipeline): ...

    def dispatchWorkgroups(self, workgroupCountX: GPUSize32, workgroupCountY: GPUSize32 | None = 1,
                           workgroupCountZ: GPUSize32 | None = 1): ...

    def dispatchWorkgroupsIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64): ...

    def end(self): ...


class GPURenderPassEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin,
                           GPURenderCommandsMixin):
    def setViewport(self, x: float, y: float, width: float, height: float, minDepth: float, maxDepth: float): ...

    def setScissorRect(self, x: GPUIntegerCoordinate, y: GPUIntegerCoordinate, width: GPUIntegerCoordinate,
                       height: GPUIntegerCoordinate): ...

    def setBlendConstant(self, color: GPUColor): ...

    def setStencilReference(self, reference: GPUStencilValue): ...

    def beginOcclusionQuery(self, queryIndex: GPUSize32): ...

    def endOcclusionQuery(self): ...

    def end(self): ...


class GPURenderBundle(GPUObjectBase): ...


class GPURenderBundleEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin,
                             GPURenderCommandsMixin):
    def finish(self, descriptor: GPURenderBundleDescriptor | None = {}) -> GPURenderBundle: ...


class GPUQueue(GPUObjectBase):
    def writeBuffer(self, buffer: GPUBuffer, bufferOffset: GPUSize64, data: BufferSource,
                    dataOffset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...

    def writeTexture(self, destination: GPUImageCopyTexture, data: BufferSource, dataLayout: GPUImageDataLayout,
                     size: GPUExtent3D): ...

    def copyExternalImageToTexture(self, source: GPUImageCopyExternalImage, destination: GPUImageCopyTextureTagged,
                                   copySize: GPUExtent3D): ...


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
    reason: GPUDeviceLostReason | undefined
    message: str

class GPUError:
    message: str

class GPUValidationError(GPUError): ...

class GPUOutOfMemoryError(GPUError): ...

class GPUInternalError(GPUError): ...

class GPUUncapturedErrorEvent(Event):
    error: GPUError

class Serial(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler

class SerialPort(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler
    readable: ReadableStream
    writable: WritableStream
    def getInfo(self) -> SerialPortInfo: ...

class AudioDecoder:
    state: CodecState
    decodeQueueSize: int
    def configure(self, config: AudioDecoderConfig): ...
    def decode(self, chunk: EncodedAudioChunk): ...
    def reset(self): ...
    def close(self): ...

class VideoDecoder:
    state: CodecState
    decodeQueueSize: int
    def configure(self, config: VideoDecoderConfig): ...
    def decode(self, chunk: EncodedVideoChunk): ...
    def reset(self): ...
    def close(self): ...

class AudioEncoder:
    state: CodecState
    encodeQueueSize: int
    def configure(self, config: AudioEncoderConfig): ...
    def encode(self, data: AudioData): ...
    def reset(self): ...
    def close(self): ...

class VideoEncoder:
    state: CodecState
    encodeQueueSize: int
    def configure(self, config: VideoEncoderConfig): ...
    def encode(self, frame: VideoFrame, options: VideoEncoderEncodeOptions | None = {}): ...
    def reset(self): ...
    def close(self): ...

class EncodedAudioChunk:
    type: EncodedAudioChunkType
    timestamp: int
    duration: int | None
    byteLength: int
    def copyTo(self, destination: BufferSource): ...

class EncodedVideoChunk:
    type: EncodedVideoChunkType
    timestamp: int
    duration: int | None
    byteLength: int
    def copyTo(self, destination: BufferSource): ...

class AudioData:
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
    format: VideoPixelFormat | None
    codedWidth: int
    codedHeight: int
    codedRect: DOMRectReadOnly | None
    visibleRect: DOMRectReadOnly | None
    displayWidth: int
    displayHeight: int
    duration: int | None
    timestamp: int | None
    colorSpace: VideoColorSpace
    def allocationSize(self, options: VideoFrameCopyToOptions | None = {}) -> int: ...
    def clone(self) -> VideoFrame: ...
    def close(self): ...

class VideoColorSpace:
    primaries: VideoColorPrimaries | None
    transfer: VideoTransferCharacteristics | None
    matrix: VideoMatrixCoefficients | None
    fullRange: bool | None
    def toJSON(self) -> VideoColorSpaceInit: ...

class ImageDecoder:
    type: str
    complete: bool
    tracks: ImageTrackList
    def reset(self): ...
    def close(self): ...

class ImageTrackList:
    length: int
    selectedIndex: int
    selectedTrack: ImageTrack | None

class ImageTrack(EventTarget):
    animated: bool
    frameCount: int
    repetitionCount: float
    onchange: EventHandler
    selected: bool


class Bluetooth(EventTarget, BluetoothDeviceEventHandlers, CharacteristicEventHandlers, ServiceEventHandlers):
    onavailabilitychanged: EventHandler
    referringDevice: BluetoothDevice | None

class BluetoothPermissionResult(PermissionStatus): ...

class ValueEvent(Event): ...


class BluetoothDevice(EventTarget, BluetoothDeviceEventHandlers, CharacteristicEventHandlers, ServiceEventHandlers):
    id: str
    name: str | None
    gatt: BluetoothRemoteGATTServer | None
    watchingAdvertisements: bool

class BluetoothManufacturerDataMap: ...

class BluetoothServiceDataMap: ...

class BluetoothAdvertisingEvent(Event):
    device: BluetoothDevice
    name: str | None
    appearance: int | None
    txPower: byte | None
    rssi: byte | None
    manufacturerData: BluetoothManufacturerDataMap
    serviceData: BluetoothServiceDataMap

class BluetoothRemoteGATTServer:
    device: BluetoothDevice
    connected: bool
    def disconnect(self): ...


class BluetoothRemoteGATTService(EventTarget, CharacteristicEventHandlers, ServiceEventHandlers):
    device: BluetoothDevice
    uuid: UUID
    isPrimary: bool


class BluetoothRemoteGATTCharacteristic(EventTarget, CharacteristicEventHandlers):
    service: BluetoothRemoteGATTService
    uuid: UUID
    properties: BluetoothCharacteristicProperties
    value: DataView

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

class BluetoothUUID: ...



document: Document
window: Window
navigator: Navigator
