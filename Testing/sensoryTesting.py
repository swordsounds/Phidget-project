from pynput import keyboard
from pynput import mouse
from pynput.mouse import Controller 
import rcServo as servo 
import motor as motor

mouseSetPoint = Controller()
mouseSetPoint.position = (768, 448)

angle = []

def on_press(key):
    print(sum(angle))
    try:
        # print('{0}'.format(key.char))
        if key.char == 'w':
            a = d = 1
            multiplier = 1
            motor.main(multiplier, a, d)
        elif key.char == 's':
            a = d = 1
            multiplier = -1
            motor.main(multiplier, a ,d)
        elif key.char == 'a':
            a = -1
            d = 1
            multiplier = -1
            motor.main(multiplier, a ,d)
        elif key.char == 'd':
            a = 1
            d = -1
            multiplier = -1
            motor.main(multiplier, a ,d)
        else:
            camera_controller(key, angle)
    except AttributeError:
        print('{0}'.format(key))

def camera_controller(key, angle):
    if servo.getPosition() == 0:
        if key.char == 'q':
            angle.append(10)
            # servo.main(sum(angle))
        elif key.char == 'e':
            if sum(angle) < 0:
                angle = 0
                # servo.main(sum(angle))
            angle.append(-10)
            # servo.main(sum(angle))
 



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


