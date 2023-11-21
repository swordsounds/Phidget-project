from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.RCServo import *


import traceback
import time

#Declare any event handlers here. These will be called every time the associated event occurs.
x = 0
def onRCServo0_Attach(self):
	print("Attach!")

def onRCServo0_Detach(self):
	print("Detach!")

def onRCServo0_Error(self, code, description):
	print("Code: " + ErrorEventCode.getName(code))
	print("Description: " + str(description))
	print("----------")
def thingIsOn(x, rcServo0):
	x += 45
	rcServo0.setTargetPosition(x)
	print(x)
	rcServo0.setEngaged(True)
	return x

def thingIsOn2(x, rcServo1):
	x += 45
	rcServo1.setTargetPosition(x)
	print(x)
	rcServo1.setEngaged(True)
	return x

def onRCServo0():
	
	try:
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
		thingIsOn(x, rcServo0)

		rcServo1 = RCServo()
		rcServo1.setDeviceSerialNumber(302849)

		#Assign any event handlers you need before calling open so that no events are missed.
	
		rcServo1.setOnAttachHandler(onRCServo0_Attach)
		rcServo1.setOnDetachHandler(onRCServo0_Detach)
		rcServo1.setOnErrorHandler(onRCServo0_Error)
		rcServo1.setChannel(1)
		#Open your Phidgets and wait for attachment
		rcServo1.openWaitForAttachment(5000)
		
		thingIsOn2(x, rcServo1)
		rcServo0.setTargetPosition(x)
		rcServo1.setTargetPosition(x)
		time.sleep(1)
		#Close your Phidgets once the program is done.
		rcServo0.close()
		rcServo1.close()

	except PhidgetException as ex:
		#We will catch Phidget Exceptions here, and print the error informaiton.
		traceback.print_exc()
		print("")
		print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)
