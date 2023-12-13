from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time

def onSensorChange(self, sensorValue, sensorUnit):
	print("SensorValue: " + str(sensorValue))
	print("SensorUnit: " + str(sensorUnit.symbol))
	print("----------")

def main():
	voltageRatioInput1 = VoltageRatioInput()

	voltageRatioInput1.setChannel(1)

	voltageRatioInput1.setOnSensorChangeHandler(onSensorChange)

	voltageRatioInput1.openWaitForAttachment(5000)

	voltageRatioInput1.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1124)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	voltageRatioInput1.close()

main()