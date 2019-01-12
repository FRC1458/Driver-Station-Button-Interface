import serial
from time import sleep
from util import *

pid = None
server_address = "127.0.0.1"

buttons = {
    #     Button Path  Light Path
    "5": ("button5",   "light5")    # Testing
}

# Connect to NetworkTables and Arduino
table = connectToNetworkTables(server_address)        
ser = serial.Serial(findArduinoDevice(pid=pid))

### Lights

def setLight(pin, status):
    ser.write(bytes(str(pin) + ("1" if status else "0") + "\n", "ascii"))

def lightsTableChanged(source, key, value, param):
    pin = None
    for k in buttons.keys():
        if buttons[k][1] == key:
            pin = k
    if pin == None:
        return
    setLight(pin, value)

# Add Listeners to all of the button lights
for k in buttons.keys():
    table.addEntryListener(lightsTableChanged, True, buttons[k][1])

# Flash lights to give delay for serial to connect
for i in range(0, 15):
        for pin in buttons.keys():
            setLight(pin, True)
        sleep(0.1)
        for pin in buttons.keys():
            setLight(pin, False)
        sleep(0.1)
        
# Update lights to their perscribed values
for k in buttons.keys():
    lightsTableChanged("n/a", buttons[k][1], table.getBoolean(buttons[k][1], False), "")


### Buttons

print("Setup Completed.")

while(ser.isOpen()):
    sleep(0.01)
    b = ser.read(4).decode("ascii")
    pin = b[0]
    state = int(b[1])
    
    # Cycle if out of order
    if pin == b'\n' or pin == b'\r' or state == b'\n' or state == b'\r':
        ser.read()
        continue
    
    if(pin in buttons.keys() and table.containsKey(buttons[pin][0])):
        table.putBoolean(buttons[pin][0], False if state == 0 else True)

