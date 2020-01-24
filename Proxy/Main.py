from proxy.printer_proxy import PrinterProxy

def startMain():
    p = PrinterProxy("Alice")
    print("Printer代理人の名前は現在({})です".format(p.getPrinterName()))
    p.myPrint("Nice to meet you")
    p.setPrinterName("Bob")
    print("Printer代理人の名前は現在({})です".format(p.getPrinterName()))
    p.myPrint("Hello, World")


if __name__ == '__main__':
    startMain()
