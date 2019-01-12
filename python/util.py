import threading
from networktables import NetworkTables
import serial
import serial.tools.list_ports
import sys

# Connect to Pynetworktables
def connectToNetworkTables(address):
    cond = threading.Condition()
    notified = [False]

    def connectionListener(connected, info):
        if(connected):
            print("Connected to NetworkTables at ", str(info.remote_ip) + ":" + str(info.remote_port))
        else:
            input("Could not connect to NetworkTables. Click enter to exit.")
            sys.exit()
        with cond:
            notified[0] = True
            cond.notify()

    NetworkTables.initialize(server=address)
    NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

    with cond:
        print("Waiting for NetworkTable Connection...")
        if not notified[0]:
            cond.wait()
    
    return NetworkTables.getTable("SmartDashboard")

def findArduinoDevice(pid = None):
    device = None
    ports = list(serial.tools.list_ports.comports(False))
    for port in ports:
        if ("Arduino" in port.description or "CH340" in port.description):
            if (not(pid == None) and (not(pid == port.pid))):
                continue
            device = port.device
            print("Identified ", device, " as Arduino device")
            break
    if device == None:
        input("Unable to identify Arduino device. Click enter to exit.")
        sys.exit()
    return device