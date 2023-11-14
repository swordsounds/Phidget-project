# from pynput.keyboard import Key, Listener
# from pynput.mouse import Listener
# from pynput import keyboard

# def on_click(x, y, button, pressed):
#     if pressed:
#         print("Mouse clicked.")

# def on_press(key):
#     print("key is pressed")




# key_listener = keyboard.Listener(on_press=on_press)
# key_listener.start()

# with Listener(on_click=on_click) as listener:
#     listener.join()

from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

from pynput import mouse

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()

# from pynput import mouse

# class MyException(Exception): pass

# def on_click(x, y, button, pressed):
#     if button == mouse.Button.left:
#         raise MyException(button)

# # Collect events until released
# with mouse.Listener(
#         on_click=on_click) as listener:
#     try:
#         listener.join()
#     except MyException as e:
#         print('{0} was clicked'.format(e.args[0]))