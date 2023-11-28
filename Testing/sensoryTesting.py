from pynput import keyboard
from pynput import mouse
from pynput.mouse import Controller 
import rcServo as servo 
import motor as motor

mouseSetPoint = Controller()
mouseSetPoint.position = (768, 448)

RCServo0_angle = []
RCServo1_angle = []

def on_press(key):
    try:
        # print('{0}'.format(key.char))
        if key.char == 'w':
            motor.main(1, 1, 1)
        elif key.char == 's':
            motor.main(-1, 1 ,1)
        elif key.char == 'a':
            motor.main(-1, -1 ,1)
        elif key.char == 'd':
            motor.main(-1, 1 ,-1)
        else:
            camera_controller(key, RCServo0_angle, RCServo1_angle)
    except AttributeError:
        # print('{0}'.format(key))
        pass

def camera_controller(key, RCServo0_angle, RCServo1_angle):
        if key.char == 'q':
            if servo.rcServo0.getPostition() < 180:
                RCServo0_angle.append(10)
                print(sum(RCServo0_angle))
            # servo.onRCServo0(sum(RCServo0_angle))
        if key.char == 'e':
                RCServo1_angle.append(10)
                servo.onRCServo1(sum(RCServo1_angle))
 

def on_release(key):
    # print('{0} released'.format(key))
    motor.close()
    if key == keyboard.Key.esc:
        return False
    

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listenerKeyboard:
    listenerKeyboard.join()


listenerKeyboard = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)


listenerKeyboard.start()


