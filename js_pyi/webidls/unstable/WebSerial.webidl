[Exposed=Window, SecureContext]
partial interface Navigator {
  [SameObject] readonly attribute Serial serial;
};

[Exposed=DedicatedWorker, SecureContext]
partial interface WorkerNavigator {
  [SameObject] readonly attribute Serial serial;
};

[Exposed=(DedicatedWorker, Window), SecureContext]
interface Serial : EventTarget {
  attribute EventHandler onconnect;
  attribute EventHandler ondisconnect;
  Promise<sequence<SerialPort>> getPorts();
  [Exposed=Window] Promise<SerialPort> requestPort(optional SerialPortRequestOptions options = {});
};

dictionary SerialPortRequestOptions {
  sequence<SerialPortFilter> filters;
};

dictionary SerialPortFilter {
  unsigned short usbVendorId;
  unsigned short usbProductId;
};

[Exposed=(DedicatedWorker,Window), SecureContext]
interface SerialPort : EventTarget {
  attribute EventHandler onconnect;
  attribute EventHandler ondisconnect;
  readonly attribute ReadableStream readable;
  readonly attribute WritableStream writable;

  SerialPortInfo getInfo();

  Promise<undefined> open(SerialOptions options);
  Promise<undefined> setSignals(optional SerialOutputSignals signals = {});
  Promise<SerialInputSignals> getSignals();
  Promise<undefined> close();
  Promise<undefined> forget();
};

dictionary SerialPortInfo {
  unsigned short usbVendorId;
  unsigned short usbProductId;
};

dictionary SerialOptions {
  [EnforceRange] required unsigned long baudRate;
  [EnforceRange] octet dataBits = 8;
  [EnforceRange] octet stopBits = 1;
  ParityType parity = "none";
  [EnforceRange] unsigned long bufferSize = 255;
  FlowControlType flowControl = "none";
};

enum ParityType {
  "none",
  "even",
  "odd"
};

enum FlowControlType {
  "none",
  "hardware"
};

dictionary SerialOutputSignals {
  boolean dataTerminalReady;
  boolean requestToSend;
  boolean break;
};

dictionary SerialInputSignals {
  required boolean dataCarrierDetect;
  required boolean clearToSend;
  required boolean ringIndicator;
  required boolean dataSetReady;
};
