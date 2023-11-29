from pynput import keyboard
from pynput import mouse
from pynput.mouse import Controller 
import rcServo as servo 
import motor as motor
import cameraOperation as camera
import threading

# mouseSetPoint = Controller()
# mouseSetPoint.position = (768, 448)

RCServo0_angle = []
RCServo1_angle = []

servo.main()

    
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
            camera_controller(key, RCServo0_angle, RCServo1_angle)
    except AttributeError:
        pass

def camera_controller(key, RCServo0_angle, RCServo1_angle):
        print(sum(RCServo0_angle))
        if sum(RCServo0_angle) <= 170 and sum(RCServo0_angle) >= 0: 
            if key.char == 'u':
                RCServo0_angle.append(10)
                servo.onRCServo0(sum(RCServo0_angle))
            elif key.char == 'j':
                RCServo0_angle.append(-10)
                servo.onRCServo0(sum(RCServo0_angle))
        elif sum(RCServo1_angle) < 170:
            if key.char == 'h':
                RCServo1_angle.append(-10)
                servo.onRCServo1(sum(RCServo1_angle))
            elif key.char == 'k':
                RCServo1_angle.append(10)
                servo.onRCServo1(sum(RCServo1_angle))


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
