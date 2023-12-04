from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time

def onSensorChange(self, sensorValue, sensorUnit):
	print("SensorValue: " + str(sensorValue))
	print("SensorUnit: " + str(sensorUnit.symbol))
	print("----------")

voltageRatioInput0 = VoltageRatioInput()

def main():
	voltageRatioInput0.setOnSensorChangeHandler(onSensorChange)

	voltageRatioInput0.openWaitForAttachment(5000)

	voltageRatioInput0.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1101_SHARP_2Y0A21)

	time.sleep(60)

def close():
	voltageRatioInput0.close()

main()