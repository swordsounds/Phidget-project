from pynput import keyboard
from pynput import mouse
from pynput.mouse import Controller 
import testingPlace as servo 
import motor as motor

mouseSetPoint = Controller()
mouseSetPoint.position = (768, 448)

def on_press(key):
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
            camera_controls()
    except AttributeError:
        print('{0} pressed'.format(key))


def camera_controls(key):
    if key.char == "Key.right":
        servo.main()
    elif key.char == "Key.left":
        servo.main()


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


