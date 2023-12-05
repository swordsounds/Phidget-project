from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import logging as lg
import time


voltageRatioInput0 = VoltageRatioInput()
voltageRatioInput1 = VoltageRatioInput()


def onSensorChange(self, sensorValue, sensorUnit):
	# print(f"SensorValue [{str(self.getChannel())}]: {str(sensorValue)} {str(sensorUnit.symbol)}\n")
	return

def main():

	voltageRatioInput0.setChannel(0)
	voltageRatioInput1.setChannel(1)

	voltageRatioInput0.setOnSensorChangeHandler(onSensorChange)
	voltageRatioInput1.setOnSensorChangeHandler(onSensorChange)

	voltageRatioInput0.openWaitForAttachment(5000)
	voltageRatioInput1.openWaitForAttachment(5000)

	voltageRatioInput0.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1101_SHARP_2Y0A21)
	voltageRatioInput1.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1101_SHARP_2Y0A21)

def close():
	voltageRatioInput0.close()
	voltageRatioInput1.close()

if __name__ == '__main_':
	main()