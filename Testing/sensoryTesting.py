from pynput import keyboard
from pynput import mouse
from pynput.mouse import Controller 
import rcServo as servo 
import motor as motor
import cameraOperation as camera
import irDistance as distance_sensor
import threading
import logging as lg
from Phidget22.PhidgetException import *

# mouseSetPoint = Controller()
# mouseSetPoint.position = (768, 448)
lg.basicConfig(format='%(levelname)s: %(message)s', level=lg.DEBUG)

RCServo0_angle = 0
RCServo1_angle = 0

servo.main()
distance_sensor.main()

def on_press(key):
    try:
        if key.char == 'w':
            motor.main(1, 1, 1)
        elif key.char == 's':
            motor.main(-1, 1 ,1)
        elif key.char == 'a':
            motor.main(-1, -1 ,1)
        elif key.char == 'd':
            motor.main(-1, 1 ,-1)
        else:
            camera_controller(key)
    except AttributeError:
        pass

def camera_controller(key):
        global RCServo0_angle
        global RCServo1_angle

        if key.char == 'u':
            if RCServo0_angle == 180:
                lg.debug("== 180")
            else:    
                RCServo0_angle += 45
                servo.onRCServo0(RCServo0_angle) 
        elif key.char == 'j':
            if RCServo0_angle == 0:
                lg.debug("== 0")
                pass
            else:
                RCServo0_angle -= 45
                servo.onRCServo0(RCServo0_angle)
        
        elif key.char == 'k':
            if RCServo1_angle == 180:
                lg.debug("== 180")
            else:    
                RCServo1_angle += 45
                servo.onRCServo1(RCServo1_angle) 
        elif key.char == 'h':
            if RCServo1_angle == 0:
                lg.debug("== 0")
                pass
            else:
                RCServo1_angle -= 45
                servo.onRCServo1(RCServo1_angle)

        lg.info(RCServo0_angle)
        lg.info(RCServo1_angle)


def on_release(key):
    motor.close()
    if key == keyboard.Key.esc:
        return False

def cam():
    camera.main()

cam_thread = threading.Thread(target=cam)
cam_thread.start()


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listenerKeyboard:
    listenerKeyboard.join()


listenerKeyboard = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)


listenerKeyboard.start()
