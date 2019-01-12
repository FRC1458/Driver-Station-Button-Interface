# Driver Station Button Interface

Contains the Arduino sketch and Python program used to connect driver station lights and buttons to [RobotPy NetworkTables](https://robotpy.readthedocs.io/projects/pynetworktables/en/stable/index.html "RobotPy NetworkTables").

## Setup
1. Use the Arduino IDE to upload `arduino_script.ino` to a Arduino compatible board.
	- Note: Many cheaper boards use the CH340 Serial Chipset. While this comes installed on many Linux distributions, it must be installed manually on Windows and Mac to enable serial communication. Drivers for this chipset can be downloaded from [this website](https://sparks.gogo.co.nz/ch340.html "this website").

2. Connect buttons and lights to the Arduino.
	- Buttons are connected to digital pins; LEDs are connected to analog pins.
	- Connect light/button pairs to the same number pin. (Ex. Pin 3 and Pin A3)
	- The buttons should short the digital pins to ground.
	- Use an approximately 220 Ohm resistor to connect the LEDs to the analog pins.

3. Configure `DriverStationButtonInterface.py`
	- Set the server address to `10.TE.AM.2` (Ex. `10.14.58.2`)
	- If you plan to connect multiple Arduinos to the driver station computer, make sure to set the PID (Product ID) variable as so that the program knows what Arduino to interact with.
		- The PID of a serial device can be found in Windows by opening the Device Manager, opening the list of COM ports, right clicking on the desired device, clicking Properties, going to the Details tab, and selecting the Hardware Ids dropdown.

## Running the Program
Right click on  `DriverStationButtonInterface.py` and select `Open with > Python`.