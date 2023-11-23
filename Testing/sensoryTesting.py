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
    except AttributeError:
        print('{0} pressed'.format(key))

def on_release(key):
    # print('{0} released'.format(key))
    motor.close()
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
def on_move(x, y):
    print('Pointer:{0}'.format((x, y)))

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listenerKeyboard:
    listenerKeyboard.join()

with mouse.Listener(
        on_move=on_move) as listenerMouse:
    listenerMouse.join()

# ...or, in a non-blocking fashion:
listenerKeyboard = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)

listenerMouse = mouse.Listener(
    on_move=on_move)

listenerMouse.start()
listenerKeyboard.start()


