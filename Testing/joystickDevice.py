from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time

def onSensorChange(self, sensorValue, sensorUnit):
	print("SensorValue: " + str(sensorValue))
	print("SensorUnit: " + str(sensorUnit.symbol))
	print("----------")

def main():
	voltageRatioInput3 = VoltageRatioInput()

	voltageRatioInput3.setChannel(3)

	voltageRatioInput3.setOnSensorChangeHandler(onSensorChange)

	voltageRatioInput3.openWaitForAttachment(5000)

	voltageRatioInput3.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1113)

	time.sleep(60)

	voltageRatioInput3.close()

main()