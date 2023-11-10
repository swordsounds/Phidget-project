
from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
import time

#Declare any event handlers here. These will be called every time the associated event occurs.

def onVoltageChange(self, voltage):
	print("Voltage: " + str(voltage))

def onAttach(self):
	print("Attach!")

def onDetach(self):
	print("Detach!")

def main():
	#Create your Phidget channels
	voltageInput0 = VoltageInput()

	#Set addressing parameters to specify which channel to open (if any)
	voltageInput0.setDeviceSerialNumber(107414)

	#Assign any event handlers you need before calling open so that no events are missed.
	voltageInput0.setOnVoltageChangeHandler(onVoltageChange)
	voltageInput0.setOnAttachHandler(onAttach)
	voltageInput0.setOnDetachHandler(onDetach)

	#Open your Phidgets and wait for attachment
	voltageInput0.openWaitForAttachment(5000)

	#Do stuff with your Phidgets here or in your event handlers.

	time.sleep(5)

	#Close your Phidgets once the program is done.
	voltageInput0.close()

main()