from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
import logging as lg

dcMotor0 = DCMotor()
dcMotor1 = DCMotor()

dcMotor0.setChannel(0)
dcMotor1.setChannel(1)



def main(multiplier, a, d):
	dcMotor0.openWaitForAttachment(1000)
	dcMotor1.openWaitForAttachment(1000)


	dcMotor0.setAcceleration(19.4)
	dcMotor1.setAcceleration(19.4)

	dcMotor0.setTargetVelocity(1 * multiplier * a)
	dcMotor1.setTargetVelocity(1 * multiplier * d)

def close():
	dcMotor0.close()
	dcMotor1.close()

if __name__ == "__main__":
	main()