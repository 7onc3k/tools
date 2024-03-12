from pynput import mouse, keyboard
import pyautogui
import threading

# Globální proměnné
recording = False
recorded_actions = []
current_keys = set()  # Sada pro sledování současně stisknutých kláves

def on_click(x, y, button, pressed):
    if recording:
        recorded_actions.append(('mouse', x, y, button, pressed))

def on_press(key):
    global recording
    if key == keyboard.Key.esc:
        recording = not recording
        if recording:
            current_keys.clear()
            recorded_actions.clear()
            print("Recording started.")
        else:
            print("Recording stopped.")
    elif key == keyboard.KeyCode.from_char(';') and not recording:
        play_recorded_actions()
    elif recording:
        current_keys.add(key)
        recorded_actions.append(('key', tuple(current_keys), True))


def on_release(key):
    if recording:
        current_keys.discard(key)  # Používáme discard místo remove
        recorded_actions.append(('key', tuple(current_keys), False))


def play_recorded_actions():
    print("Playing back recorded actions.")
    for action in recorded_actions:
        if action[0] == 'mouse':
            _, x, y, button, pressed = action
            if pressed:
                pyautogui.mouseDown(x, y, button.name)
            else:
                pyautogui.mouseUp(x, y, button.name)
        elif action[0] == 'key':
            _, keys, pressed = action
            for key in keys:
                if pressed:
                    pyautogui.keyDown(key.char if hasattr(key, 'char') else key)
                else:
                    pyautogui.keyUp(key.char if hasattr(key, 'char') else key)

# Spuštění posluchačů
listener_mouse = mouse.Listener(on_click=on_click)
listener_keyboard = keyboard.Listener(on_press=on_press, on_release=on_release)

listener_mouse.start()
listener_keyboard.start()

listener_mouse.join()
listener_keyboard.join()
