class MediaQueryListEvent(Event):
    media: str
    matches: bool


class FrameLoader:
    docShell: nsIDocShell | None
    tabParent: TabParent | None
    loadContext: LoadContext
    parentSHistory: ParentSHistory | None
    depthTooGreat: bool

    def activateRemoteFrame(self): ...

    def deactivateRemoteFrame(self): ...

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


class PluginCrashedEvent(Event):
    pluginID: int
    pluginDumpID: str
    pluginName: str
    browserDumpID: str | None
    pluginFilename: str | None
    submittedCrashReport: bool
    gmpPlugin: bool


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


class Element(Node):
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

    def scroll(self, options: ScrollToOptions | None = None): ...

    def scrollTo(self, options: ScrollToOptions | None = None): ...

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


class Request:
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
    signal: AbortSignal

    def clone(self) -> Request: ...

    def overrideContentPolicyType(self, context: nsContentPolicyType): ...


class BaseAudioContext(EventTarget): ...


class MediaStreamEvent(Event):
    stream: MediaStream | None


class Range:
    startContainer: Node
    startOffset: int
    endContainer: Node
    endOffset: int
    collapsed: bool
    commonAncestorContainer: Node

    def setStart(self, refNode: Node, offset: int): ...

    def setEnd(self, refNode: Node, offset: int): ...

    def setStartBefore(self, refNode: Node): ...

    def setStartAfter(self, refNode: Node): ...

    def setEndBefore(self, refNode: Node): ...

    def setEndAfter(self, refNode: Node): ...

    def collapse(self, toStart: bool | None = false): ...

    def selectNode(self, refNode: Node): ...

    def selectNodeContents(self, refNode: Node): ...

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

    def getClientRects(self) -> DOMRectList | None: ...

    def getBoundingClientRect(self) -> DOMRect: ...

    def getClientRectsAndTexts(self) -> ClientRectsAndTexts: ...


class SVGFEBlendElement(SVGElement):
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
    audioTracks: AudioTrackList
    videoTracks: VideoTrackList
    textTracks: TextTrackList
    onupdatestart: EventHandler
    onupdate: EventHandler
    onupdateend: EventHandler
    onerror: EventHandler
    onabort: EventHandler

    def appendBuffer(self, data: ArrayBuffer): ...

    def appendBuffer(self, data: ArrayBufferView): ...

    def abort(self): ...

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


class ConstantSourceNode(AudioScheduledSourceNode):
    offset: AudioParam


class MediaKeySystemAccess:
    keySystem: str

    def getConfiguration(self) -> MediaKeySystemConfiguration: ...


class NotificationEvent(ExtendableEvent):
    notification: Notification


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
    target: Element


class IntersectionObserver:
    root: Element | None
    rootMargin: str

    def observe(self, target: Element): ...

    def unobserve(self, target: Element): ...

    def disconnect(self): ...

    intersectionCallback: IntersectionCallback


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
    stringValue: str
    booleanValue: bool
    singleNodeValue: Node | None
    invalidIteratorState: bool
    snapshotLength: int

    def iterateNext(self) -> Node | None: ...

    def snapshotItem(self, index: int) -> Node | None: ...


class GroupedHistoryEvent(Event):
    otherBrowser: Element | None


class SVGImageElement(SVGGraphicsElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio


class AnimationPlaybackEvent(Event): ...


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


class ProcessingInstruction(CharacterData):
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


class StyleRuleChangeEvent(Event):
    stylesheet: CSSStyleSheet | None
    rule: CSSRule | None


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


class SVGPolylineElement(SVGGeometryElement): ...


class SVGFEImageElement(SVGElement):
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
    type: GridDeclaration
    number: int
    negativeNumber: int


class GridTracks:
    length: int


class GridTrack:
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


class ExtendableEvent(Event): ...


class RTCPeerConnectionStatic:
    def registerPeerConnectionLifecycleCallback(self, cb: PeerConnectionLifecycleCallback): ...


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


class SVGPathSegMovetoAbs(SVGPathSeg): ...


class SVGPathSegMovetoRel(SVGPathSeg): ...


class SVGPathSegLinetoAbs(SVGPathSeg): ...


class SVGPathSegLinetoRel(SVGPathSeg): ...


class SVGPathSegCurvetoCubicAbs(SVGPathSeg): ...


class SVGPathSegCurvetoCubicRel(SVGPathSeg): ...


class SVGPathSegCurvetoQuadraticAbs(SVGPathSeg): ...


class SVGPathSegCurvetoQuadraticRel(SVGPathSeg): ...


class SVGPathSegArcAbs(SVGPathSeg):
    largeArcFlag: bool
    sweepFlag: bool


class SVGPathSegArcRel(SVGPathSeg):
    largeArcFlag: bool
    sweepFlag: bool


class SVGPathSegLinetoHorizontalAbs(SVGPathSeg): ...


class SVGPathSegLinetoHorizontalRel(SVGPathSeg): ...


class SVGPathSegLinetoVerticalAbs(SVGPathSeg): ...


class SVGPathSegLinetoVerticalRel(SVGPathSeg): ...


class SVGPathSegCurvetoCubicSmoothAbs(SVGPathSeg): ...


class SVGPathSegCurvetoCubicSmoothRel(SVGPathSeg): ...


class SVGPathSegCurvetoQuadraticSmoothAbs(SVGPathSeg): ...


class SVGPathSegCurvetoQuadraticSmoothRel(SVGPathSeg): ...


class PaymentMethodChangeEvent(PaymentRequestUpdateEvent):
    methodName: str
    methodDetails: object | None


class DOMRect(DOMRectReadOnly): ...


class DOMRectReadOnly:
    def toJSON(self) -> object: ...


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


class OffscreenCanvas(EventTarget):
    width: int
    height: int

    def transferToImageBitmap(self) -> ImageBitmap: ...


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


class WebKitCSSMatrix(DOMMatrix):
    def setMatrixValue(self, transformList: str) -> WebKitCSSMatrix: ...

    def multiply(self, other: WebKitCSSMatrix) -> WebKitCSSMatrix: ...

    def inverse(self) -> WebKitCSSMatrix: ...


class BiquadFilterNode(AudioNode):
    type: BiquadFilterType
    frequency: AudioParam
    detune: AudioParam
    Q: AudioParam
    gain: AudioParam

    def getFrequencyResponse(self, frequencyHz: Float32Array, magResponse: Float32Array,
                             phaseResponse: Float32Array): ...


class FileReader(EventTarget):
    def readAsArrayBuffer(self, blob: Blob): ...

    def readAsBinaryString(self, filedata: Blob): ...

    def readAsText(self, blob: Blob, label: str | None = None): ...

    def readAsDataURL(self, blob: Blob): ...

    def abort(self): ...

    readyState: int
    error: DOMException | None
    onloadstart: EventHandler
    onprogress: EventHandler
    onload: EventHandler
    onabort: EventHandler
    onerror: EventHandler
    onloadend: EventHandler


class IIRFilterNode(AudioNode):
    def getFrequencyResponse(self, frequencyHz: Float32Array, magResponse: Float32Array,
                             phaseResponse: Float32Array): ...


class StorageEvent(Event):
    key: str | None
    oldValue: str | None
    newValue: str | None
    url: str | None
    storageArea: Storage | None

    def initStorageEvent(self, type: str, canBubble: bool | None = false, cancelable: bool | None = false,
                         key: str | None = None, oldValue: str | None = None, newValue: str | None = None,
                         url: str | None = None, storageArea: Storage | None = None): ...


class MouseEvent(UIEvent):
    screenX: int
    screenY: int
    clientX: int
    clientY: int
    x: int
    y: int
    offsetX: int
    offsetY: int
    ctrlKey: bool
    shiftKey: bool
    altKey: bool
    metaKey: bool
    button: short
    buttons: int
    relatedTarget: EventTarget | None
    region: str | None
    movementX: int
    movementY: int

    def initMouseEvent(self, typeArg: str, canBubbleArg: bool | None = false, cancelableArg: bool | None = false,
                       viewArg: Window | None = None, detailArg: int | None = 0, screenXArg: int | None = 0,
                       screenYArg: int | None = 0, clientXArg: int | None = 0, clientYArg: int | None = 0,
                       ctrlKeyArg: bool | None = false, altKeyArg: bool | None = false,
                       shiftKeyArg: bool | None = false, metaKeyArg: bool | None = false, buttonArg: short | None = 0,
                       relatedTargetArg: EventTarget | None = None): ...

    def getModifierState(self, keyArg: str) -> bool: ...


class SVGFETurbulenceElement(SVGElement):
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


class SVGFESpecularLightingElement(SVGElement):
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


class MIDIConnectionEvent(Event):
    port: MIDIPort | None


class UDPSocket(EventTarget):
    localAddress: str | None
    localPort: int | None
    remoteAddress: str | None
    remotePort: int | None
    addressReuse: bool
    loopback: bool
    readyState: SocketReadyState
    onmessage: EventHandler

    def joinMulticastGroup(self, multicastGroupAddress: str): ...

    def leaveMulticastGroup(self, multicastGroupAddress: str): ...

    def send(self, data: str | Blob | ArrayBuffer | ArrayBufferView, remoteAddress: str | None = None,
             remotePort: int | None = None) -> bool: ...


class BlobEvent(Event):
    data: Blob | None


class MediaList:
    mediaText: str
    length: int

    def deleteMedium(self, oldMedium: str): ...

    def appendMedium(self, newMedium: str): ...


class HTMLIFrameElement(HTMLElement):
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


class WebGL2RenderingContext: ...


class EXT_color_buffer_float: ...


class URL:
    href: USVString
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


class CSSImportRule(CSSRule):
    href: str
    media: MediaList | None
    styleSheet: CSSStyleSheet | None


class HTMLMeterElement(HTMLElement):
    labels: NodeList


class FileSystem:
    name: USVString
    root: FileSystemDirectoryEntry


class BatteryManager(EventTarget):
    charging: bool
    onchargingchange: EventHandler
    onchargingtimechange: EventHandler
    ondischargingtimechange: EventHandler
    onlevelchange: EventHandler


class SVGPathSegList:
    numberOfItems: int


class HTMLAudioElement(HTMLMediaElement): ...


class SVGFEFloodElement(SVGElement): ...


class SVGEllipseElement(SVGGeometryElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    rx: SVGAnimatedLength
    ry: SVGAnimatedLength


class BrowserFeedWriter:
    def writeContent(self): ...

    def close(self): ...


class HTMLTemplateElement(HTMLElement):
    content: DocumentFragment


class OscillatorNode(AudioScheduledSourceNode):
    type: OscillatorType
    frequency: AudioParam
    detune: AudioParam

    def setPeriodicWave(self, periodicWave: PeriodicWave): ...


class TransceiverImpl:
    def getReceiveTrack(self) -> MediaStreamTrack: ...

    def syncWithJS(self, transceiver: RTCRtpTransceiver): ...


class PermissionStatus(EventTarget):
    state: PermissionState
    onchange: EventHandler


class TextEncoder:
    encoding: str

    def encode(self, input: str | None = "") -> Uint8Array: ...


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


class VRFieldOfView: ...


class VRDisplayCapabilities:
    hasPosition: bool
    hasOrientation: bool
    hasExternalDisplay: bool
    canPresent: bool
    maxLayers: int


class VRStageParameters:
    sittingToStandingTransform: Float32Array


class VRPose:
    position: Float32Array
    linearVelocity: Float32Array
    linearAcceleration: Float32Array
    orientation: Float32Array
    angularVelocity: Float32Array
    angularAcceleration: Float32Array


class VRFrameData:
    timestamp: DOMHighResTimeStamp
    leftProjectionMatrix: Float32Array
    leftViewMatrix: Float32Array
    rightProjectionMatrix: Float32Array
    rightViewMatrix: Float32Array
    pose: VRPose


class VRSubmitFrameResult:
    frameNum: int
    base64Image: str | None


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

    def requestAnimationFrame(self, callback: FrameRequestCallback) -> int: ...

    def cancelAnimationFrame(self, handle: int): ...

    def submitFrame(self): ...


class HTMLFrameSetElement(HTMLElement):
    cols: str
    rows: str


class PeriodicWave: ...


class SVGGElement(SVGGraphicsElement): ...


class SVGFilterElement(SVGElement):
    filterUnits: SVGAnimatedEnumeration
    primitiveUnits: SVGAnimatedEnumeration
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength


class DocumentTimeline(AnimationTimeline): ...


class SVGScriptElement(SVGElement):
    type: str
    crossOrigin: str | None


class IDBRequest(EventTarget):
    error: DOMException | None
    source: IDBObjectStore | IDBIndex | IDBCursor | None
    transaction: IDBTransaction | None
    readyState: IDBRequestReadyState
    onsuccess: EventHandler
    onerror: EventHandler


class WorkerNavigator:
    serial: Serial


class SVGFEFuncAElement(SVGComponentTransferFunctionElement): ...


class File(Blob):
    name: str
    lastModified: int


class SVGFEComponentTransferElement(SVGElement):
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


class SpeechRecognitionError(Event):
    error: SpeechRecognitionErrorCode
    message: str | None


class StorageManager: ...


class PerformanceNavigation:
    type: int
    redirectCount: int

    def toJSON(self) -> object: ...


class DOMStringMap: ...


class FocusEvent(UIEvent):
    relatedTarget: EventTarget | None


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


class Blob:
    size: int
    type: str

    def slice(self, start: int | None = None, end: int | None = None, contentType: str | None = None) -> Blob: ...

    def stream(self) -> ReadableStream: ...


class AnimationTimeline: ...


class CSSPseudoElement:
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


class SVGFEGaussianBlurElement(SVGElement):
    in1: SVGAnimatedString
    stdDeviationX: SVGAnimatedNumber
    stdDeviationY: SVGAnimatedNumber


class Position:
    coords: Coordinates
    timestamp: DOMTimeStamp


class SVGFEColorMatrixElement(SVGElement):
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


class SVGFEOffsetElement(SVGElement):
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


class SVGAnimationElement(SVGElement):
    targetElement: SVGElement | None

    def beginElement(self): ...

    def endElement(self): ...


class SVGSetElement(SVGAnimationElement): ...


class SVGClipPathElement(SVGElement):
    clipPathUnits: SVGAnimatedEnumeration
    transform: SVGAnimatedTransformList


class CaretStateChangedEvent(Event):
    collapsed: bool
    boundingClientRect: DOMRectReadOnly | None
    reason: CaretChangedReason
    caretVisible: bool
    caretVisuallyVisible: bool
    selectionVisible: bool
    selectionEditable: bool
    selectedTextContent: str


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


class SVGAElement(SVGGraphicsElement):
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


class SubmitEvent(Event):
    submitter: HTMLElement | None


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


class RTCDataChannelEvent(Event):
    channel: RTCDataChannel


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


class SpeechSynthesisEvent(Event):
    utterance: SpeechSynthesisUtterance
    charIndex: int
    charLength: int | None
    name: str | None


class SVGTSpanElement(SVGTextPositioningElement): ...


class PresentationConnectionCloseEvent(Event):
    reason: PresentationConnectionClosedReason
    message: str


class DataTransferItemList:
    length: int

    def add(self, data: str, type: str) -> DataTransferItem | None: ...

    def add(self, data: File) -> DataTransferItem | None: ...

    def remove(self, index: int): ...

    def clear(self): ...


class SVGZoomAndPan: ...


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


class MediaSource(EventTarget):
    sourceBuffers: SourceBufferList
    activeSourceBuffers: SourceBufferList
    readyState: MediaSourceReadyState
    onsourceopen: EventHandler
    onsourceended: EventHandler
    onsourceclose: EventHandler

    def addSourceBuffer(self, type: str) -> SourceBuffer: ...

    def removeSourceBuffer(self, sourceBuffer: SourceBuffer): ...

    def endOfStream(self, error: MediaSourceEndOfStreamError | None = None): ...

    def clearLiveSeekableRange(self): ...


class Notification(EventTarget):
    onclick: EventHandler
    onshow: EventHandler
    onerror: EventHandler
    onclose: EventHandler
    title: str
    dir: NotificationDirection
    lang: str | None
    body: str | None
    tag: str | None
    icon: str | None
    requireInteraction: bool

    def close(self): ...


class Exception:
    name: str
    message: str


class DOMException:
    name: str
    message: str
    code: int


class HashChangeEvent(Event):
    oldURL: str
    newURL: str

    def initHashChangeEvent(self, typeArg: str, canBubbleArg: bool | None = false, cancelableArg: bool | None = false,
                            oldURLArg: str | None = "", newURLArg: str | None = ""): ...


class MediaStreamAudioDestinationNode(AudioNode):
    stream: MediaStream


class PresentationRequest(EventTarget):
    onconnectionavailable: EventHandler


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

    previewValue: str


class Window(EventTarget):
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

    def scroll(self, options: ScrollToOptions | None = None): ...

    def scrollTo(self, options: ScrollToOptions | None = None): ...

    def scrollBy(self, options: ScrollToOptions | None = None): ...

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


class HTMLImageElement(HTMLElement):
    alt: str
    src: str
    srcset: str
    crossOrigin: str | None
    useMap: str
    referrerPolicy: str
    isMap: bool
    width: int
    height: int
    decoding: str
    naturalWidth: int
    naturalHeight: int
    complete: bool
    name: str
    align: str
    hspace: int
    vspace: int
    longDesc: str
    border: str
    sizes: str
    currentSrc: str


class MediaStream(EventTarget):
    id: str

    def getTrackById(self, trackId: str) -> MediaStreamTrack | None: ...

    def addTrack(self, track: MediaStreamTrack): ...

    def removeTrack(self, track: MediaStreamTrack): ...

    def clone(self) -> MediaStream: ...

    active: bool
    onaddtrack: EventHandler
    onremovetrack: EventHandler

    def assignId(self, id: str): ...


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


class FlexItem:
    node: Node | None


class PaintWorkletGlobalScope(WorkletGlobalScope):
    def registerPaint(self, name: str, paintCtor: VoidFunction): ...


class AudioDestinationNode(AudioNode):
    maxChannelCount: int


class ScriptProcessorNode(AudioNode):
    onaudioprocess: EventHandler
    bufferSize: int


class DOMRequest(EventTarget):
    def fireDetailedError(self, aError: DOMException): ...


class Response:
    type: ResponseType
    url: USVString
    redirected: bool
    status: int
    ok: bool
    statusText: ByteString
    headers: Headers

    def clone(self) -> Response: ...

    def cloneUnfiltered(self) -> Response: ...


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


class PointerEvent(MouseEvent):
    pointerId: int
    width: int
    height: int
    tiltX: int
    tiltY: int
    twist: int
    pointerType: str
    isPrimary: bool


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


class TransitionEvent(Event):
    propertyName: str
    pseudoElement: str


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


class DocumentFragment(Node):
    def getElementById(self, elementId: str) -> Element | None: ...

    def querySelector(self, selectors: str) -> Element | None: ...

    def querySelectorAll(self, selectors: str) -> NodeList: ...


class HTMLTimeElement(HTMLElement):
    dateTime: str


class MessageChannel:
    port1: MessagePort
    port2: MessagePort


class PerformanceEntryEvent(Event):
    name: str
    entryType: str
    startTime: DOMHighResTimeStamp
    duration: DOMHighResTimeStamp
    origin: str


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


class DeviceOrientationEvent(Event):
    absolute: bool


class PopupBlockedEvent(Event):
    requestingWindow: Window | None
    popupWindowURI: URI | None
    popupWindowName: str | None
    popupWindowFeatures: str | None


class TextTrackCue(EventTarget):
    track: TextTrack | None
    id: str
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


class SharedWorker(EventTarget):
    port: MessagePort


class BeforeUnloadEvent(Event):
    returnValue: str


class RTCPeerConnection(EventTarget):
    def setIdentityProvider(self, provider: str, options: RTCIdentityProviderOptions | None = None): ...

    localDescription: RTCSessionDescription | None
    currentLocalDescription: RTCSessionDescription | None
    pendingLocalDescription: RTCSessionDescription | None
    remoteDescription: RTCSessionDescription | None
    currentRemoteDescription: RTCSessionDescription | None
    pendingRemoteDescription: RTCSessionDescription | None
    signalingState: RTCSignalingState
    canTrickleIceCandidates: bool | None
    iceGatheringState: RTCIceGatheringState
    iceConnectionState: RTCIceConnectionState
    idpLoginUrl: str | None
    id: str

    def getConfiguration(self) -> RTCConfiguration: ...

    def addStream(self, stream: MediaStream): ...

    def addTrack(self, track: MediaStreamTrack, stream: MediaStream,
                 moreStreams: MediaStream | None = None) -> RTCRtpSender: ...

    def removeTrack(self, sender: RTCRtpSender): ...

    def addTransceiver(self, trackOrKind: MediaStreamTrack | str,
                       init: RTCRtpTransceiverInit | None = None) -> RTCRtpTransceiver: ...

    def close(self): ...

    onnegotiationneeded: EventHandler
    onicecandidate: EventHandler
    onsignalingstatechange: EventHandler
    onaddstream: EventHandler
    onaddtrack: EventHandler
    ontrack: EventHandler
    onremovestream: EventHandler
    oniceconnectionstatechange: EventHandler
    onicegatheringstatechange: EventHandler

    def createDataChannel(self, label: str, dataChannelDict: RTCDataChannelInit | None = None) -> RTCDataChannel: ...

    ondatachannel: EventHandler


class ServiceWorker(EventTarget):
    scriptURL: USVString
    state: ServiceWorkerState
    onstatechange: EventHandler


class ScrollAreaEvent(UIEvent): ...


class HTMLOListElement(HTMLElement):
    reversed: bool
    start: int
    type: str
    compact: bool


class Text(CharacterData):
    def splitText(self, offset: int) -> Text: ...

    wholeText: str
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


class RTCSessionDescription:
    type: RTCSdpType
    sdp: str

    def toJSON(self) -> object: ...


class AudioListener: ...


class SpeechRecognition(EventTarget):
    grammars: SpeechGrammarList
    lang: str
    continuous: bool
    interimResults: bool
    maxAlternatives: int
    serviceURI: str

    def start(self, stream: MediaStream | None = None): ...

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


class FetchEvent(ExtendableEvent):
    request: Request
    clientId: str | None
    isReload: bool


class UIEvent(Event):
    view: WindowProxy | None
    detail: int

    def initUIEvent(self, aType: str, aCanBubble: bool | None = false, aCancelable: bool | None = false,
                    aView: Window | None = None, aDetail: int | None = 0): ...

    layerX: int
    layerY: int
    pageX: int
    pageY: int
    which: int
    rangeParent: Node | None
    rangeOffset: int


class MediaElementAudioSourceNode(AudioNode): ...


class HTMLHeadingElement(HTMLElement):
    align: str


class PresentationConnectionAvailableEvent(Event):
    connection: PresentationConnection


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


class SVGUseElement(SVGGraphicsElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength


class SVGFEMergeNodeElement(SVGElement):
    in1: SVGAnimatedString


class AudioWorklet(Worklet): ...


class ImageCaptureErrorEvent(Event):
    imageCaptureError: ImageCaptureError | None


class ImageCaptureError:
    code: int
    message: str


class GamepadEvent(Event):
    gamepad: Gamepad | None


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


class HTMLElement(Element):
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


class StereoPannerNode(AudioNode):
    pan: AudioParam


class CryptoKey:
    type: KeyType
    extractable: bool
    algorithm: object


class SubtleCrypto: ...


class SVGFEMergeElement(SVGElement): ...


class CustomElementRegistry:
    def define(self, name: str, functionConstructor: Function, options: ElementDefinitionOptions | None = None): ...

    def setElementCreationCallback(self, name: str, callback: CustomElementCreationCallback): ...

    def upgrade(self, root: Node): ...


class SVGFEMorphologyElement(SVGElement):
    in1: SVGAnimatedString
    operator: SVGAnimatedEnumeration
    radiusX: SVGAnimatedNumber
    radiusY: SVGAnimatedNumber


class HTMLOptionElement(HTMLElement):
    disabled: bool
    form: HTMLFormElement | None
    label: str
    defaultSelected: bool
    selected: bool
    value: str
    text: str
    index: int


class MediaEncryptedEvent(Event):
    initDataType: str
    initData: ArrayBuffer


class ImageDocument(HTMLDocument):
    imageIsOverflowing: bool
    imageIsResized: bool
    imageRequest: imgIRequest | None

    def shrinkToFit(self): ...

    def restoreImage(self): ...

    def restoreImageTo(self, x: int, y: int): ...

    def toggleImageSize(self): ...


class StyleSheetChangeEvent(Event):
    stylesheet: CSSStyleSheet | None
    documentSheet: bool


class XMLSerializer:
    def serializeToString(self, root: Node) -> str: ...


class HTMLPictureElement(HTMLElement): ...


class SVGMatrix:
    def multiply(self, secondMatrix: SVGMatrix) -> SVGMatrix: ...

    def inverse(self) -> SVGMatrix: ...

    def flipX(self) -> SVGMatrix: ...

    def flipY(self) -> SVGMatrix: ...


class EventSource(EventTarget):
    url: str
    withCredentials: bool
    readyState: int
    onopen: EventHandler
    onmessage: EventHandler
    onerror: EventHandler

    def close(self): ...


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


class MutationObserver:
    def observe(self, target: Node, options: MutationObserverInit | None = None): ...

    def disconnect(self): ...

    mutationCallback: MutationCallback
    mergeAttributeRecords: bool


class DynamicsCompressorNode(AudioNode):
    threshold: AudioParam
    knee: AudioParam
    ratio: AudioParam
    attack: AudioParam
    release: AudioParam


class Screen:
    colorGamut: ScreenColorGamut
    luminance: ScreenLuminance | None
    onchange: EventHandler


class ScreenLuminance: ...


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


class TCPSocketEvent(Event): ...


class HTMLDirectoryElement(HTMLElement):
    compact: bool


class SVGAngle:
    unitType: int
    valueAsString: str

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


class Headers:
    def append(self, name: ByteString, value: ByteString): ...

    def delete(self, name: ByteString): ...

    def get(self, name: ByteString) -> ByteString | None: ...

    def has(self, name: ByteString) -> bool: ...

    def set(self, name: ByteString, value: ByteString): ...

    guard: HeadersGuardEnum


class VTTRegion:
    id: str
    lines: int
    scroll: ScrollSetting


class XMLHttpRequest(XMLHttpRequestEventTarget):
    onreadystatechange: EventHandler
    readyState: int

    def open(self, method: ByteString, url: USVString): ...

    def open(self, method: ByteString, url: USVString, async_: bool, user: USVString | None = None,
             password: USVString | None = None): ...

    def setRequestHeader(self, header: ByteString, value: ByteString): ...

    timeout: int
    withCredentials: bool
    upload: XMLHttpRequestUpload

    def send(self, body: Document | BodyInit | None = None): ...

    def abort(self): ...

    responseURL: USVString
    status: int
    statusText: ByteString

    def getResponseHeader(self, header: ByteString) -> ByteString | None: ...

    def getAllResponseHeaders(self) -> ByteString: ...

    def overrideMimeType(self, mime: str): ...

    responseType: XMLHttpRequestResponseType
    responseText: USVString | None
    responseXML: Document | None


class SVGStyleElement(SVGElement):
    xmlspace: str
    type: str
    media: str
    title: str


class GamepadHapticActuator:
    type: GamepadHapticActuatorType


class PerformanceObserver:
    def observe(self, options: PerformanceObserverInit): ...

    def disconnect(self): ...

    def takeRecords(self) -> PerformanceEntryList: ...


class PeerConnectionImpl:
    def initialize(self, observer: PeerConnectionObserver, window: Window, iceServers: RTCConfiguration,
                   thread: nsISupports): ...

    def createOffer(self, options: RTCOfferOptions | None = None): ...

    def createAnswer(self): ...

    def setLocalDescription(self, action: int, sdp: str): ...

    def setRemoteDescription(self, action: int, sdp: str): ...

    def getStats(self, selector: MediaStreamTrack | None): ...

    def createTransceiverImpl(self, kind: str, track: MediaStreamTrack | None) -> TransceiverImpl: ...

    def checkNegotiationNeeded(self) -> bool: ...

    def insertDTMF(self, transceiver: TransceiverImpl, tones: str, duration: int | None = 100,
                   interToneGap: int | None = 70): ...

    def getDTMFToneBuffer(self, sender: RTCRtpSender) -> str: ...

    def getNowInRtpSourceReferenceTime(self) -> DOMHighResTimeStamp: ...

    def replaceTrackNoRenegotiation(self, transceiverImpl: TransceiverImpl, withTrack: MediaStreamTrack | None): ...

    def closeStreams(self): ...

    def addRIDExtension(self, recvTrack: MediaStreamTrack, extensionId: int): ...

    def addRIDFilter(self, recvTrack: MediaStreamTrack, rid: str): ...

    def insertAudioLevelForContributingSource(self, recvTrack: MediaStreamTrack, source: int,
                                              timestamp: DOMHighResTimeStamp, hasLevel: bool, level: byte): ...

    def enablePacketDump(self, level: int, type: mozPacketDumpType, sending: bool): ...

    def disablePacketDump(self, level: int, type: mozPacketDumpType, sending: bool): ...

    def addIceCandidate(self, candidate: str, mid: str, level: int): ...

    def close(self): ...

    def pluginCrash(self, pluginId: int, name: str) -> bool: ...

    certificate: RTCCertificate
    fingerprint: str
    localDescription: str
    currentLocalDescription: str
    pendingLocalDescription: str
    remoteDescription: str
    currentRemoteDescription: str
    pendingRemoteDescription: str
    iceConnectionState: PCImplIceConnectionState
    iceGatheringState: PCImplIceGatheringState
    signalingState: PCImplSignalingState
    id: str
    peerIdentity: str
    privacyRequested: bool

    def createDataChannel(self, label: str, protocol: str, type: int, ordered: bool, maxTime: int, maxNum: int,
                          externalNegotiated: bool, stream: int) -> RTCDataChannel: ...


class GainNode(AudioNode):
    gain: AudioParam


class CompositionEvent(UIEvent):
    data: str | None
    locale: str

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


class PopStateEvent(Event): ...


class WebrtcGlobalInformation: ...


class MIDIAccess(EventTarget):
    inputs: MIDIInputMap
    outputs: MIDIOutputMap
    onstatechange: EventHandler
    sysexEnabled: bool


class SpeechSynthesisErrorEvent(SpeechSynthesisEvent):
    error: SpeechSynthesisErrorCode


class MIDIOutputMap: ...


class FileSystemDirectoryReader:
    def readEntries(self, successCallback: FileSystemEntriesCallback, errorCallback: ErrorCallback | None = None): ...


class SecurityPolicyViolationEvent(Event):
    documentURI: str
    referrer: str
    blockedURI: str
    violatedDirective: str
    effectiveDirective: str
    originalPolicy: str
    sourceFile: str
    sample: str
    disposition: SecurityPolicyViolationEventDisposition
    statusCode: int
    lineNumber: int
    columnNumber: int


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


class SVGFEDiffuseLightingElement(SVGElement):
    in1: SVGAnimatedString
    surfaceScale: SVGAnimatedNumber
    diffuseConstant: SVGAnimatedNumber
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber


class TextDecoder:
    encoding: str
    fatal: bool

    def decode(self, input: BufferSource | None = None, options: TextDecodeOptions | None = None) -> USVString: ...


class HTMLDataListElement(HTMLElement):
    options: HTMLCollection


class SVGLength:
    unitType: int
    valueAsString: str

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
    keyStatuses: MediaKeyStatusMap
    onkeystatuseschange: EventHandler
    onmessage: EventHandler


class SpeechRecognitionEvent(Event):
    resultIndex: int
    results: SpeechRecognitionResultList | None
    emma: Document | None


class ScreenOrientation(EventTarget):
    def unlock(self): ...

    type: OrientationType
    angle: int
    onchange: EventHandler


class WebGLContextEvent(Event):
    statusMessage: str


class HTMLDetailsElement(HTMLElement):
    open: bool


class SVGTransform:
    type: int
    matrix: SVGMatrix

    def setMatrix(self, matrix: SVGMatrix): ...


class CharacterData(Node):
    data: str
    length: int

    def substringData(self, offset: int, count: int) -> str: ...

    def appendData(self, data: str): ...

    def insertData(self, offset: int, data: str): ...

    def deleteData(self, offset: int, count: int): ...

    def replaceData(self, offset: int, count: int, data: str): ...


class InputEvent(UIEvent):
    isComposing: bool
    inputType: str
    data: str | None
    dataTransfer: DataTransfer | None


class SVGCircleElement(SVGGeometryElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    r: SVGAnimatedLength


class OfflineAudioCompletionEvent(Event):
    renderedBuffer: AudioBuffer


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


class AudioWorkletNode(AudioNode):
    parameters: AudioParamMap
    port: MessagePort
    onprocessorerror: EventHandler


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


class AudioScheduledSourceNode(AudioNode): ...


class CheckerboardReportService:
    def isRecordingEnabled(self) -> bool: ...

    def setRecordingEnabled(self, aEnabled: bool): ...

    def flushActiveReports(self): ...


class CSSSupportsRule(CSSConditionRule): ...


class SVGFEConvolveMatrixElement(SVGElement):
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


class CloseEvent(Event):
    wasClean: bool
    code: int
    reason: str


class SVGFECompositeElement(SVGElement):
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    operator: SVGAnimatedEnumeration
    k1: SVGAnimatedNumber
    k2: SVGAnimatedNumber
    k3: SVGAnimatedNumber
    k4: SVGAnimatedNumber


class AudioContext(BaseAudioContext):
    def createMediaElementSource(self, mediaElement: HTMLMediaElement) -> MediaElementAudioSourceNode: ...

    def createMediaStreamSource(self, mediaStream: MediaStream) -> MediaStreamAudioSourceNode: ...

    def createMediaStreamDestination(self) -> MediaStreamAudioDestinationNode: ...


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


class DOMParser:
    def parseFromString(self, str: str, type: SupportedType) -> Document: ...

    def forceEnableXULXBL(self): ...


class DOMImplementation:
    def hasFeature(self) -> bool: ...

    def createDocumentType(self, qualifiedName: str, publicId: str, systemId: str) -> DocumentType: ...

    def createDocument(self, namespace: str | None, qualifiedName: str,
                       doctype: DocumentType | None = None) -> Document: ...

    def createHTMLDocument(self, title: str | None = None) -> Document: ...


class VRMockDisplay:
    def setEyeResolution(self, aRenderWidth: int, aRenderHeight: int): ...

    def setPose(self, position: Float32Array, linearVelocity: Float32Array, linearAcceleration: Float32Array,
                orientation: Float32Array, angularVelocity: Float32Array, angularAcceleration: Float32Array): ...

    def setMountState(self, isMounted: bool): ...

    def update(self): ...


class VRMockController:
    def newButtonEvent(self, button: int, pressed: bool): ...

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


class SpeechGrammar:
    src: str


class SVGPatternElement(SVGElement):
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


class Touch:
    identifier: int
    target: EventTarget | None
    screenX: int
    screenY: int
    clientX: int
    clientY: int
    pageX: int
    pageY: int
    radiusX: int
    radiusY: int


class MediaDevices(EventTarget):
    ondevicechange: EventHandler

    def getSupportedConstraints(self) -> MediaTrackSupportedConstraints: ...


class SVGSVGElement(SVGGraphicsElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    useCurrentView: bool
    currentTranslate: SVGPoint

    def suspendRedraw(self, maxWaitMilliseconds: int) -> int: ...

    def unsuspendRedraw(self, suspendHandleID: int): ...

    def unsuspendRedrawAll(self): ...

    def forceRedraw(self): ...

    def pauseAnimations(self): ...

    def unpauseAnimations(self): ...

    def animationsPaused(self) -> bool: ...

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


class AnalyserNode(AudioNode):
    def getFloatFrequencyData(self, array: Float32Array): ...

    def getByteFrequencyData(self, array: Uint8Array): ...

    def getFloatTimeDomainData(self, array: Float32Array): ...

    def getByteTimeDomainData(self, array: Uint8Array): ...

    fftSize: int
    frequencyBinCount: int


class DOMError:
    name: str
    message: str


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


class WebGLRenderingContext:
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


class WaveShaperNode(AudioNode):
    curve: Float32Array
    oversample: OverSampleType


class TCPSocketErrorEvent(Event):
    name: str
    message: str


class DOMQuad:
    p1: DOMPoint
    p2: DOMPoint
    p3: DOMPoint
    p4: DOMPoint

    def getBounds(self) -> DOMRectReadOnly: ...

    bounds: DOMRectReadOnly

    def toJSON(self) -> DOMQuadJSON: ...


class SVGPathElement(SVGGeometryElement): ...


class RTCIceCandidate:
    candidate: str
    sdpMid: str | None
    sdpMLineIndex: int | None

    def toJSON(self) -> object: ...


class AudioStreamTrack(MediaStreamTrack): ...


class WebSocket(EventTarget):
    url: str
    readyState: int
    bufferedAmount: int
    onopen: EventHandler
    onerror: EventHandler
    onclose: EventHandler
    extensions: str
    protocol: str

    def close(self, code: int | None = None, reason: str | None = None): ...

    onmessage: EventHandler
    binaryType: BinaryType

    def send(self, data: str): ...

    def send(self, data: Blob): ...

    def send(self, data: ArrayBuffer): ...

    def send(self, data: ArrayBufferView): ...


class InstallTriggerImpl:
    def enabled(self) -> bool: ...

    def updateEnabled(self) -> bool: ...

    def installChrome(self, type: int, url: str, skin: str) -> bool: ...

    def startSoftwareUpdate(self, url: str, flags: int | None = None) -> bool: ...


class ScrollViewChangeEvent(Event):
    state: ScrollState


class HTMLLinkElement(HTMLElement):
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


class ShadowRoot(DocumentFragment):
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


class ConvolverNode(AudioNode):
    buffer: AudioBuffer | None
    normalize: bool


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


class MediaStreamAudioSourceNode(AudioNode): ...


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


class SVGFETileElement(SVGElement):
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


class ImageData:
    width: int
    height: int
    data: Uint8ClampedArray


class Navigator:
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


class DOMMatrixReadOnly:
    def multiply(self, other: DOMMatrix) -> DOMMatrix: ...

    def flipX(self) -> DOMMatrix: ...

    def flipY(self) -> DOMMatrix: ...

    def inverse(self) -> DOMMatrix: ...

    is2D: bool
    isIdentity: bool

    def transformPoint(self, point: DOMPointInit | None = None) -> DOMPoint: ...

    def toFloat32Array(self) -> Float32Array: ...

    def toFloat64Array(self) -> Float64Array: ...

    def toJSON(self) -> object: ...


class DOMMatrix(DOMMatrixReadOnly):
    def multiplySelf(self, other: DOMMatrix) -> DOMMatrix: ...

    def preMultiplySelf(self, other: DOMMatrix) -> DOMMatrix: ...

    def invertSelf(self) -> DOMMatrix: ...

    def setMatrixValue(self, transformList: str) -> DOMMatrix: ...


class SVGSwitchElement(SVGGraphicsElement): ...


class MIDIMessageEvent(Event):
    data: Uint8Array


class AudioTrackList(EventTarget):
    length: int

    def getTrackById(self, id: str) -> AudioTrack | None: ...

    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler


class AudioWorkletGlobalScope(WorkletGlobalScope):
    def registerProcessor(self, name: str, processorCtor: VoidFunction): ...

    currentFrame: int


class ErrorEvent(Event):
    message: str
    filename: str
    lineno: int
    colno: int


class HTMLAnchorElement(HTMLElement):
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


class PannerNode(AudioNode):
    panningModel: PanningModelType
    positionX: AudioParam
    positionY: AudioParam
    positionZ: AudioParam
    orientationX: AudioParam
    orientationY: AudioParam
    orientationZ: AudioParam
    distanceModel: DistanceModelType


class HTMLOptGroupElement(HTMLElement):
    disabled: bool
    label: str


class Coordinates: ...


class KeyframeEffect(AnimationEffect):
    target: Element | CSSPseudoElement | None
    iterationComposite: IterationCompositeOperation
    composite: CompositeOperation

    def setKeyframes(self, keyframes: object | None): ...


class Comment(CharacterData): ...


class SVGFEDropShadowElement(SVGElement):
    in1: SVGAnimatedString
    dx: SVGAnimatedNumber
    dy: SVGAnimatedNumber
    stdDeviationX: SVGAnimatedNumber
    stdDeviationY: SVGAnimatedNumber


class MediaQueryList(EventTarget):
    media: str
    matches: bool

    def addListener(self, listener: EventListener | None): ...

    def removeListener(self, listener: EventListener | None): ...

    onchange: EventHandler


class CanvasRenderingContext2D:
    canvas: HTMLCanvasElement | None

    def demote(self): ...


class CanvasGradient: ...


class CanvasPattern:
    def setTransform(self, matrix: SVGMatrix): ...


class TextMetrics: ...


class Path2D:
    def addPath(self, path: Path2D, transformation: SVGMatrix | None = None): ...


class SVGDescElement(SVGElement): ...


class PerformanceServerTiming:
    name: str
    duration: DOMHighResTimeStamp
    description: str

    def toJSON(self) -> object: ...


class HTMLProgressElement(HTMLElement):
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


class PushEvent(ExtendableEvent):
    data: PushMessageData | None


class SVGAnimateElement(SVGAnimationElement): ...


class CSSFontFaceRule(CSSRule):
    style: CSSStyleDeclaration


class SVGFEDisplacementMapElement(SVGElement):
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


class HTMLStyleElement(HTMLElement):
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


class Document(Node):
    implementation: DOMImplementation
    URL: str
    documentURI: str
    compatMode: str
    characterSet: str
    charset: str
    inputEncoding: str
    contentType: str
    doctype: DocumentType | None
    documentElement: Element | None

    def getElementsByTagName(self, localName: str) -> HTMLCollection: ...

    def getElementsByTagNameNS(self, namespace: str | None, localName: str) -> HTMLCollection: ...

    def getElementsByClassName(self, classNames: str) -> HTMLCollection: ...

    def getElementById(self, elementId: str) -> Element | None: ...

    def createElement(self, localName: str, options: ElementCreationOptions | str | None = None) -> Element: ...

    def createElementNS(self, namespace: str | None, qualifiedName: str,
                        options: ElementCreationOptions | str | None = None) -> Element: ...

    def createDocumentFragment(self) -> DocumentFragment: ...

    def createTextNode(self, data: str) -> Text: ...

    def createComment(self, data: str) -> Comment: ...

    def createProcessingInstruction(self, target: str, data: str) -> ProcessingInstruction: ...

    def importNode(self, node: Node, deep: bool | None = false) -> Node: ...

    def adoptNode(self, node: Node) -> Node: ...

    def createEvent(self, interface: str) -> Event: ...

    def createRange(self) -> Range: ...

    def createNodeIterator(self, root: Node, whatToShow: int | None = 0xFFFFFFFF,
                           filter: NodeFilter | None = None) -> NodeIterator: ...

    def createTreeWalker(self, root: Node, whatToShow: int | None = 0xFFFFFFFF,
                         filter: NodeFilter | None = None) -> TreeWalker: ...

    def createCDATASection(self, data: str) -> CDATASection: ...

    def createAttribute(self, name: str) -> Attr: ...

    def createAttributeNS(self, namespace: str | None, name: str) -> Attr: ...

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


class SVGPolygonElement(SVGGeometryElement): ...


class DelayNode(AudioNode):
    delayTime: AudioParam


class PromiseNativeHandler: ...


class MediaStreamTrackEvent(Event):
    track: MediaStreamTrack


class DeviceProximityEvent(Event): ...


class SVGLengthList:
    numberOfItems: int

    def clear(self): ...

    def initialize(self, newItem: SVGLength) -> SVGLength: ...

    def insertItemBefore(self, newItem: SVGLength, index: int) -> SVGLength: ...

    def replaceItem(self, newItem: SVGLength, index: int) -> SVGLength: ...

    def removeItem(self, index: int) -> SVGLength: ...

    def appendItem(self, newItem: SVGLength) -> SVGLength: ...


class AudioProcessingEvent(Event):
    inputBuffer: AudioBuffer
    outputBuffer: AudioBuffer


class Event:
    type: str
    target: EventTarget | None
    currentTarget: EventTarget | None
    eventPhase: int

    def stopPropagation(self): ...

    def stopImmediatePropagation(self): ...

    bubbles: bool
    cancelable: bool

    def preventDefault(self): ...

    defaultPrevented: bool
    defaultPreventedByChrome: bool
    defaultPreventedByContent: bool
    composed: bool
    isTrusted: bool
    timeStamp: DOMHighResTimeStamp

    def initEvent(self, type: str, bubbles: bool | None = false, cancelable: bool | None = false): ...

    cancelBubble: bool


class SVGGradientElement(SVGElement):
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


class Animation(EventTarget):
    id: str
    effect: AnimationEffect | None
    timeline: AnimationTimeline | None
    playState: AnimationPlayState
    pending: bool
    onfinish: EventHandler
    oncancel: EventHandler

    def cancel(self): ...

    def finish(self): ...

    def play(self): ...

    def pause(self): ...

    def reverse(self): ...

    isRunningOnCompositor: bool


class GamepadAxisMoveEvent(GamepadEvent):
    axis: int


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


class BroadcastChannel(EventTarget):
    name: str

    def close(self): ...

    onmessage: EventHandler
    onmessageerror: EventHandler


class SVGGeometryElement(SVGGraphicsElement):
    pathLength: SVGAnimatedNumber


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


class SVGTextPathElement(SVGTextContentElement):
    startOffset: SVGAnimatedLength
    method: SVGAnimatedEnumeration
    spacing: SVGAnimatedEnumeration


class XSLTProcessor:
    def importStylesheet(self, style: Node): ...

    def transformToFragment(self, source: Node, output: Document) -> DocumentFragment: ...

    def transformToDocument(self, source: Node) -> Document: ...

    def getParameter(self, namespaceURI: str, localName: str) -> nsIVariant | None: ...

    def removeParameter(self, namespaceURI: str, localName: str): ...

    def clearParameters(self): ...

    def reset(self): ...

    flags: int


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


class PushManagerImpl: ...


class PushManager: ...


class MediaCapabilitiesInfo:
    supported: bool
    smooth: bool
    powerEfficient: bool


class MediaCapabilities: ...


class PeerConnectionObserver:
    def onCreateOfferSuccess(self, offer: str): ...

    def onCreateOfferError(self, name: int, message: str): ...

    def onCreateAnswerSuccess(self, answer: str): ...

    def onCreateAnswerError(self, name: int, message: str): ...

    def onSetLocalDescriptionSuccess(self): ...

    def onSetRemoteDescriptionSuccess(self): ...

    def onSetLocalDescriptionError(self, name: int, message: str): ...

    def onSetRemoteDescriptionError(self, name: int, message: str): ...

    def onAddIceCandidateSuccess(self): ...

    def onAddIceCandidateError(self, name: int, message: str): ...

    def onIceCandidate(self, level: int, mid: str, candidate: str): ...

    def onGetStatsSuccess(self, report: RTCStatsReportInternal | None = None): ...

    def onGetStatsError(self, name: int, message: str): ...

    def notifyDataChannel(self, channel: RTCDataChannel): ...

    def onStateChange(self, state: PCObserverStateType): ...

    def onTransceiverNeeded(self, kind: str, transceiverImpl: TransceiverImpl): ...

    def onDTMFToneChange(self, track: MediaStreamTrack, tone: str): ...

    def onPacket(self, level: int, type: mozPacketDumpType, sending: bool, packet: ArrayBuffer): ...

    def syncTransceivers(self): ...


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


class DOMPointReadOnly:
    def toJSON(self) -> object: ...


class DOMPoint(DOMPointReadOnly): ...


class MediaStreamError:
    name: str
    message: str | None
    constraint: str | None


class SVGAnimatedNumber: ...


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


class SVGSymbolElement(SVGElement): ...


class FontFaceSetLoadEvent(Event): ...


class SVGViewElement(SVGElement): ...


class FileReaderSync:
    def readAsArrayBuffer(self, blob: Blob) -> ArrayBuffer: ...

    def readAsBinaryString(self, blob: Blob) -> str: ...

    def readAsText(self, blob: Blob, encoding: str | None = None) -> str: ...

    def readAsDataURL(self, blob: Blob) -> str: ...


class MediaRecorderErrorEvent(Event):
    error: DOMException


class TrackEvent(Event):
    track: VideoTrack | AudioTrack | TextTrack | None


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


class ReadableStreamDefaultReader:
    def releaseLock(self): ...


class ReadableStreamBYOBReader:
    def releaseLock(self): ...


class ReadableStreamDefaultController:
    def close(self): ...


class ReadableByteStreamController:
    byobRequest: ReadableStreamBYOBRequest | None

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
    def releaseLock(self): ...


class WritableStreamDefaultController:
    signal: AbortSignal


class TransformStream:
    readable: ReadableStream
    writable: WritableStream


class TransformStreamDefaultController:
    def terminate(self): ...


class ByteLengthQueuingStrategy:
    size: Function


class CountQueuingStrategy:
    size: Function


class HTMLModElement(HTMLElement):
    cite: str
    dateTime: str


class StyleSheetApplicableStateChangeEvent(Event):
    stylesheet: CSSStyleSheet | None
    applicable: bool


class PaymentRequestUpdateEvent(Event): ...


class SVGNumberList:
    numberOfItems: int

    def clear(self): ...

    def initialize(self, newItem: SVGNumber) -> SVGNumber: ...

    def insertItemBefore(self, newItem: SVGNumber, index: int) -> SVGNumber: ...

    def replaceItem(self, newItem: SVGNumber, index: int) -> SVGNumber: ...

    def removeItem(self, index: int) -> SVGNumber: ...

    def appendItem(self, newItem: SVGNumber) -> SVGNumber: ...


class RTCStatsReport: ...


class SpeechGrammarList:
    length: int


class CustomEvent(Event): ...


class GamepadButton:
    pressed: bool
    touched: bool


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


class SVGNumber: ...


class KeyboardEvent(UIEvent):
    charCode: int
    keyCode: int
    altKey: bool
    ctrlKey: bool
    shiftKey: bool
    metaKey: bool

    def getModifierState(self, key: str) -> bool: ...

    location: int
    repeat: bool
    isComposing: bool
    key: str
    code: str

    def initKeyboardEvent(self, typeArg: str, bubblesArg: bool | None = false, cancelableArg: bool | None = false,
                          viewArg: Window | None = None, keyArg: str | None = "", locationArg: int | None = 0,
                          ctrlKey: bool | None = false, altKey: bool | None = false, shiftKey: bool | None = false,
                          metaKey: bool | None = false): ...

    initDict: KeyboardEventInit


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


class SVGMarkerElement(SVGElement):
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


class DeviceLightEvent(Event): ...


class SVGElement(Element):
    id: str
    className: SVGAnimatedString
    dataset: DOMStringMap
    style: CSSStyleDeclaration
    ownerSVGElement: SVGSVGElement | None
    viewportElement: SVGElement | None
    tabIndex: int

    def focus(self): ...

    def blur(self): ...


class TouchEvent(UIEvent):
    touches: TouchList
    targetTouches: TouchList
    changedTouches: TouchList
    altKey: bool
    metaKey: bool
    ctrlKey: bool
    shiftKey: bool

    def initTouchEvent(self, type: str, canBubble: bool | None = false, cancelable: bool | None = false,
                       view: Window | None = None, detail: int | None = 0, ctrlKey: bool | None = false,
                       altKey: bool | None = false, shiftKey: bool | None = false, metaKey: bool | None = false,
                       touches: TouchList | None = None, targetTouches: TouchList | None = None,
                       changedTouches: TouchList | None = None): ...


class AudioParam: ...


class WorkerGlobalScope(EventTarget):
    self: WorkerGlobalScope
    location: WorkerLocation
    navigator: WorkerNavigator

    def importScripts(self, urls: str | None = None): ...

    onerror: OnErrorEventHandler
    onoffline: EventHandler
    ononline: EventHandler


class SVGFEFuncGElement(SVGComponentTransferFunctionElement): ...


class AudioBufferSourceNode(AudioScheduledSourceNode):
    buffer: AudioBuffer | None
    playbackRate: AudioParam
    detune: AudioParam
    loop: bool
    onended: EventHandler


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


class WheelEvent(MouseEvent):
    deltaMode: int


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


class DocumentType(Node):
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


class HiddenPluginEvent(Event):
    tag: PluginTag | None


class SVGAnimatedLengthList:
    baseVal: SVGLengthList
    animVal: SVGLengthList


class PerformanceObserverEntryList:
    def getEntries(self, filter: PerformanceEntryFilterOptions | None = None) -> PerformanceEntryList: ...

    def getEntriesByType(self, entryType: str) -> PerformanceEntryList: ...

    def getEntriesByName(self, name: str, entryType: str | None = None) -> PerformanceEntryList: ...


class SVGGraphicsElement(SVGElement):
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


class UserProximityEvent(Event):
    near: bool


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


class FontFace:
    family: str
    style: str
    weight: str
    stretch: str
    unicodeRange: str
    variant: str
    featureSettings: str
    variationSettings: str
    display: str
    status: FontFaceLoadStatus


class TCPServerSocket(EventTarget):
    localPort: int
    onconnect: EventHandler
    onerror: EventHandler

    def close(self): ...


class MediaKeys:
    keySystem: str

    def createSession(self, sessionType: MediaKeySessionType | None = "temporary") -> MediaKeySession: ...


class SVGAnimatedAngle:
    baseVal: SVGAngle
    animVal: SVGAngle


class MediaKeyMessageEvent(Event):
    messageType: MediaKeyMessageType
    message: ArrayBuffer


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

    def newPoseMove(self, index: int, orient: Float32Array, pos: Float32Array, angVelocity: Float32Array,
                    angAcceleration: Float32Array, linVelocity: Float32Array, linAcceleration: Float32Array): ...


class AbortSignal(EventTarget):
    aborted: bool
    onabort: EventHandler


class MediaRecorder(EventTarget):
    stream: MediaStream
    state: RecordingState
    mimeType: str
    ondataavailable: EventHandler
    onerror: EventHandler
    onstart: EventHandler
    onstop: EventHandler
    onwarning: EventHandler

    def start(self, timeSlice: int | None = None): ...

    def stop(self): ...

    def pause(self): ...

    def resume(self): ...

    def requestData(self): ...


class FileSystemFileEntry(FileSystemEntry):
    def file(self, successCallback: FileCallback, errorCallback: ErrorCallback | None = None): ...


class DragEvent(MouseEvent):
    dataTransfer: DataTransfer | None

    def initDragEvent(self, type: str, canBubble: bool | None = false, cancelable: bool | None = false,
                      aView: Window | None = None, aDetail: int | None = 0, aScreenX: int | None = 0,
                      aScreenY: int | None = 0, aClientX: int | None = 0, aClientY: int | None = 0,
                      aCtrlKey: bool | None = false, aAltKey: bool | None = false, aShiftKey: bool | None = false,
                      aMetaKey: bool | None = false, aButton: int | None = 0, aRelatedTarget: EventTarget | None = None,
                      aDataTransfer: DataTransfer | None = None): ...


class HTMLAreaElement(HTMLElement):
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


class EventTarget:
    def addEventListener(self, type: str, listener: EventListener,
                         options: AddEventListenerOptions | bool | None = None, wantsUntrusted: bool | None = None): ...

    def removeEventListener(self, type: str, listener: EventListener,
                            options: EventListenerOptions | bool | None = None): ...

    def dispatchEvent(self, event: Event) -> bool: ...


class PresentationConnectionList(EventTarget):
    onconnectionavailable: EventHandler


class SVGMPathElement(SVGElement): ...


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


class AnimationEvent(Event):
    animationName: str
    pseudoElement: str


class CSSTransition(Animation):
    transitionProperty: str


class HTMLUListElement(HTMLElement):
    compact: bool
    type: str


class DOMStringList:
    length: int

    def contains(self, string: str) -> bool: ...


class TCPServerSocketEvent(Event):
    socket: TCPSocket


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
    def matrixTransform(self, matrix: SVGMatrix) -> SVGPoint: ...


class AnimationEffect:
    def getTiming(self) -> EffectTiming: ...

    def getComputedTiming(self) -> ComputedEffectTiming: ...

    def updateTiming(self, timing: OptionalEffectTiming | None = None): ...


class FormData:
    def append(self, name: USVString, value: Blob, filename: USVString | None = None): ...

    def append(self, name: USVString, value: USVString): ...

    def delete(self, name: USVString): ...

    def get(self, name: USVString) -> FormDataEntryValue | None: ...

    def has(self, name: USVString) -> bool: ...

    def set(self, name: USVString, value: Blob, filename: USVString | None = None): ...

    def set(self, name: USVString, value: USVString): ...


class SpeechSynthesisUtterance(EventTarget):
    text: str
    lang: str
    voice: SpeechSynthesisVoice | None
    onstart: EventHandler
    onend: EventHandler
    onerror: EventHandler
    onpause: EventHandler
    onresume: EventHandler
    onmark: EventHandler
    onboundary: EventHandler
    chosenVoiceURI: str


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

    def getStartPositionOfChar(self, charnum: int) -> SVGPoint: ...

    def getEndPositionOfChar(self, charnum: int) -> SVGPoint: ...

    def getExtentOfChar(self, charnum: int) -> SVGRect: ...

    def getCharNumAtPosition(self, point: SVGPoint) -> int: ...

    def selectSubString(self, charnum: int, nchars: int): ...


class SpeechRecognitionAlternative:
    transcript: str


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


class RTCTrackEvent(Event):
    receiver: RTCRtpReceiver
    track: MediaStreamTrack
    transceiver: RTCRtpTransceiver


class OfflineAudioContext(BaseAudioContext):
    length: int
    oncomplete: EventHandler


class RTCPeerConnectionIceEvent(Event):
    candidate: RTCIceCandidate | None


class GamepadPose:
    hasOrientation: bool
    hasPosition: bool
    position: Float32Array
    linearVelocity: Float32Array
    linearAcceleration: Float32Array
    orientation: Float32Array
    angularVelocity: Float32Array
    angularAcceleration: Float32Array


class RTCDTMFToneChangeEvent(Event):
    tone: str


class HTMLBRElement(HTMLElement):
    clear: str


class U2F: ...


class IDBVersionChangeEvent(Event):
    oldVersion: int
    newVersion: int | None


class FuzzingFunctions: ...


class GamepadButtonEvent(GamepadEvent):
    button: int


class PresentationReceiver: ...


class PromiseRejectionEvent(Event): ...


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


class ChannelSplitterNode(AudioNode): ...


class SVGAnimateMotionElement(SVGAnimationElement): ...


class AbortController:
    signal: AbortSignal

    def abort(self): ...


class DataTransfer:
    dropEffect: str
    effectAllowed: str
    items: DataTransferItemList

    def setDragImage(self, image: Element, x: int, y: int): ...

    def getData(self, format: str) -> str: ...

    def setData(self, format: str, data: str): ...

    def clearData(self, format: str | None = None): ...

    files: FileList | None


class CaretPosition:
    offsetNode: Node | None
    offset: int

    def getClientRect(self) -> DOMRect | None: ...


class Worker(EventTarget):
    def terminate(self): ...

    onmessage: EventHandler
    onmessageerror: EventHandler


class ChromeWorker(Worker): ...


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


class HTMLBodyElement(HTMLElement):
    text: str
    link: str
    vLink: str
    aLink: str
    bgColor: str
    background: str


class TCPSocket(EventTarget):
    def upgradeToSecure(self): ...

    host: USVString
    port: int
    ssl: bool
    bufferedAmount: int

    def suspend(self): ...

    def resume(self): ...

    def close(self): ...

    def closeImmediately(self): ...

    def send(self, data: ByteString) -> bool: ...

    def send(self, data: ArrayBuffer, byteOffset: int | None = 0, byteLength: int | None = None) -> bool: ...

    readyState: TCPReadyState
    binaryType: TCPSocketBinaryType
    onopen: EventHandler
    ondrain: EventHandler
    ondata: EventHandler
    onerror: EventHandler
    onclose: EventHandler


class MessageEvent(Event):
    origin: USVString
    lastEventId: str
    source: MessageEventSource | None


class PageTransitionEvent(Event):
    persisted: bool
    inFrameSwap: bool


class VTTCue(TextTrackCue):
    region: VTTRegion | None
    vertical: DirectionSetting
    snapToLines: bool
    lineAlign: LineAlignSetting
    positionAlign: PositionAlignSetting
    align: AlignSetting
    text: str

    def getCueAsHTML(self) -> DocumentFragment: ...


class AudioWorkletProcessor:
    port: MessagePort


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


class URLSearchParams:
    def append(self, name: USVString, value: USVString): ...

    def delete(self, name: USVString): ...

    def get(self, name: USVString) -> USVString | None: ...

    def has(self, name: USVString) -> bool: ...

    def set(self, name: USVString, value: USVString): ...

    def sort(self): ...


class DeviceAcceleration: ...


class DeviceRotationRate: ...


class DeviceMotionEvent(Event):
    acceleration: DeviceAcceleration | None
    accelerationIncludingGravity: DeviceAcceleration | None
    rotationRate: DeviceRotationRate | None


class ProgressEvent(Event):
    lengthComputable: bool
    loaded: int
    total: int


class ExtendableMessageEvent(ExtendableEvent):
    origin: str
    lastEventId: str
    source: Client | ServiceWorker | MessagePort | None


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


class SVGRect: ...


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


class AudioBuffer:
    length: int
    numberOfChannels: int

    def getChannelData(self, channel: int) -> Float32Array: ...

    def copyFromChannel(self, destination: Float32Array, channelNumber: int, startInChannel: int | None = 0): ...

    def copyToChannel(self, source: Float32Array, channelNumber: int, startInChannel: int | None = 0): ...


class ChannelMergerNode(AudioNode): ...


class VideoTrack:
    id: str
    kind: str
    label: str
    language: str
    selected: bool
    sourceBuffer: SourceBuffer | None


class Permissions: ...


class UDPMessageEvent(Event):
    remoteAddress: str
    remotePort: int


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
    isEncrypted: bool
    paused: bool
    played: TimeRanges
    seekable: TimeRanges
    ended: bool
    autoplay: bool
    loop: bool

    def pause(self): ...

    controls: bool
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
    baseLayer: XRWebGLLayer | None


class XRFrame:
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
    gamepad: Gamepad | None


class XRInputSourceArray:
    length: int


class XRLayer(EventTarget): ...


class XRWebGLLayer(XRLayer):
    antialias: bool
    ignoreDepthValues: bool
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


class XRJointPose(XRPose): ...


class ImageCapture:
    track: MediaStreamTrack


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


class ResizeObserverSize: ...


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


class GPUDevice:
    onuncapturederror: EventHandler


class GPUBuffer:
    size: GPUSize64
    usage: GPUBufferUsageFlags
    mapState: GPUBufferMapState

    def getMappedRange(self, offset: GPUSize64 | None = 0, size: GPUSize64 | None = None) -> ArrayBuffer: ...

    def unmap(self): ...

    def destroy(self): ...


class GPUTexture:
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


class GPUTextureView: ...


class GPUExternalTexture:
    expired: bool


class GPUSampler: ...


class GPUBindGroupLayout: ...


class GPUBindGroup: ...


class GPUPipelineLayout: ...


class GPUShaderModule: ...


class GPUCompilationMessage:
    message: str
    type: GPUCompilationMessageType
    lineNum: int
    linePos: int
    offset: int
    length: int


class GPUCompilationInfo: ...


class GPUComputePipeline: ...


class GPURenderPipeline: ...


class GPUCommandBuffer: ...


class GPUCommandEncoder:
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


class GPUComputePassEncoder:
    def setPipeline(self, pipeline: GPUComputePipeline): ...

    def dispatchWorkgroups(self, workgroupCountX: GPUSize32, workgroupCountY: GPUSize32 | None = 1,
                           workgroupCountZ: GPUSize32 | None = 1): ...

    def dispatchWorkgroupsIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64): ...

    def end(self): ...


class GPURenderPassEncoder:
    def setScissorRect(self, x: GPUIntegerCoordinate, y: GPUIntegerCoordinate, width: GPUIntegerCoordinate,
                       height: GPUIntegerCoordinate): ...

    def setBlendConstant(self, color: GPUColor): ...

    def setStencilReference(self, reference: GPUStencilValue): ...

    def beginOcclusionQuery(self, queryIndex: GPUSize32): ...

    def endOcclusionQuery(self): ...

    def end(self): ...


class GPURenderBundle: ...


class GPURenderBundleEncoder:
    def finish(self, descriptor: GPURenderBundleDescriptor | None = {}) -> GPURenderBundle: ...


class GPUQueue:
    def writeBuffer(self, buffer: GPUBuffer, bufferOffset: GPUSize64, data: BufferSource,
                    dataOffset: GPUSize64 | None = 0, size: GPUSize64 | None = None): ...

    def writeTexture(self, destination: GPUImageCopyTexture, data: BufferSource, dataLayout: GPUImageDataLayout,
                     size: GPUExtent3D): ...

    def copyExternalImageToTexture(self, source: GPUImageCopyExternalImage, destination: GPUImageCopyTextureTagged,
                                   copySize: GPUExtent3D): ...


class GPUQuerySet:
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
    onchange: EventHandler
    selected: bool


class Bluetooth(EventTarget):
    onavailabilitychanged: EventHandler
    referringDevice: BluetoothDevice | None


class BluetoothPermissionResult(PermissionStatus): ...


class ValueEvent(Event): ...


class BluetoothDevice(EventTarget):
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


class BluetoothRemoteGATTService(EventTarget):
    device: BluetoothDevice
    uuid: UUID
    isPrimary: bool


class BluetoothRemoteGATTCharacteristic(EventTarget):
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


class PaymentRequest(EventTarget):
    id: str
    shippingAddress: PaymentAddress | None
    shippingOption: str | None
    shippingType: PaymentShippingType | None
    onshippingaddresschange: EventHandler
    onshippingoptionchange: EventHandler
    onpaymentmethodchange: EventHandler


class VRDisplayEvent(Event):
    display: VRDisplay
    reason: VRDisplayEventReason | None


document: Document
window: Window
navigator: Navigator
