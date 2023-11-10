from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.RCServo import *
import traceback
import time

#Declare any event handlers here. These will be called every time the associated event occurs.

def onRCServo0_Attach(self):
	print("Attach!")

def onRCServo0_Detach(self):
	print("Detach!")

def onRCServo0_Error(self, code, description):
	print("Code: " + ErrorEventCode.getName(code))
	print("Description: " + str(description))
	print("----------")

def main():
	try:
		Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")
		#Create your Phidget channels
		rcServo0 = RCServo()
		

		#Set addressing parameters to specify which channel to open (if any)
		rcServo0.setDeviceSerialNumber(302849)

		#Assign any event handlers you need before calling open so that no events are missed.
		rcServo0.setOnAttachHandler(onRCServo0_Attach)
		rcServo0.setOnDetachHandler(onRCServo0_Detach)
		rcServo0.setOnErrorHandler(onRCServo0_Error)
		rcServo0.setChannel(0)
		#Open your Phidgets and wait for attachment
		rcServo0.openWaitForAttachment(5000)

		#Do stuff with your Phidgets here or in your event handlers.
		rcServo0.setTargetPosition(90)
		rcServo0.setEngaged(True)

		time.sleep(5)

		#Close your Phidgets once the program is done.
		rcServo0.close()

	except PhidgetException as ex:
		#We will catch Phidget Exceptions here, and print the error informaiton.
		traceback.print_exc()
		print("")
		print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)


main()