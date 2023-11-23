from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.RCServo import *


import traceback
import time


rcServo0 = RCServo()
rcServo1 = RCServo()

def onRCServo0_Error(self, code, description):
	print("Code: " + ErrorEventCode.getName(code))
	print("Description: " + str(description))
	print("----------")


def main(angle):
	try:
		rcServo0.setDeviceSerialNumber(302849)
		rcServo1.setDeviceSerialNumber(302849)
		
		rcServo0.setOnErrorHandler(onRCServo0_Error)
		rcServo1.setOnErrorHandler(onRCServo0_Error)

		rcServo0.setChannel(0)
		rcServo1.setChannel(1)

		rcServo0.openWaitForAttachment(5000)
		rcServo1.openWaitForAttachment(5000)

		rcServo0.setTargetPosition(angle)
		rcServo1.setTargetPosition(angle)
		time.sleep(1)



	except PhidgetException as ex:
		traceback.print_exc()
		print("")
		print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)

def close():
	rcServo0.close()
	rcServo1.close()

if __name__ == "__main__":
	main()