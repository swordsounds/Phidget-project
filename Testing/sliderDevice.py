from Phidget22.Phidget import *
from Phidget22.Devices.VoltageRatioInput import *
import time

def onSensorChange(self, sensorValue, sensorUnit):
	print("SensorValue: " + str(round(sensorValue, 2)))
	print("SensorUnit: " + str(sensorUnit.symbol))
	print("----------")

voltageRatioInput2 = VoltageRatioInput()

def main():
	voltageRatioInput2 = VoltageRatioInput()

	voltageRatioInput2.setChannel(2)

	voltageRatioInput2.setOnSensorChangeHandler(onSensorChange)

	voltageRatioInput2.openWaitForAttachment(5000)

	voltageRatioInput2.setSensorType(VoltageRatioSensorType.SENSOR_TYPE_1112)

	time.sleep(60)

	
def close():
	voltageRatioInput2.close()

main()