from serial.tools import list_ports
ports = list(list_ports.comports())
for i in ports:
    portproduct = str(i.product)
    portdevice = str(i.device)
    if "FT232R" in portproduct:
        print("port found:"+ portdevice)