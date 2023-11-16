from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.VoltageRatioInput import *
import traceback
import time

def onVoltageRatioInput1_SensorChange(self, sensorValue, sensorUnit):
	print("SensorValue: " + str(sensorValue))
	print("SensorUnit: " + str(sensorUnit.symbol))
	print("----------")

def onVoltageRatioInput1_Attach(self):
	print("Attach!")

def onVoltageRatioInput1_Detach(self):
	print("Detach!")

def onVoltageRatioInput1_Error(self, code, description):
	print("Code: " + ErrorEventCode.getName(code))
	print("Description: " + str(description))
	print("----------")

def main():
	try:
		voltageRatioInput1 = VoltageRatioInput()

		voltageRatioInput1.setDeviceSerialNumber(107414)
		voltageRatioInput1.setChannel(0)

		voltageRatioInput1.setOnSensorChangeHandler(onVoltageRatioInput1_SensorChange)
		voltageRatioInput1.setOnAttachHandler(onVoltageRatioInput1_Attach)
		voltageRatioInput1.setOnDetachHandler(onVoltageRatioInput1_Detach)
		voltageRatioInput1.setOnErrorHandler(onVoltageRatioInput1_Error)

		voltageRatioInput1.openWaitForAttachment(5000)

		voltageRatioInput1.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1101_SHARP_2Y0A21)

		time.sleep(5)

		voltageRatioInput1.close()

	except PhidgetException as ex:
		traceback.print_exc()
		print("")
		print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)


main()