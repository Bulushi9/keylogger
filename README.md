# Keylogger Project (Educational Use Only)

This project contains three versions of a simple keylogger implemented in Python, each with increasing functionality. These keyloggers are intended for educational purposes only to demonstrate basic techniques in data logging and Python automation.

## Project Structure

1. **keyloggerSimple.py** - Basic keylogger that captures keystrokes and saves them to a file.
2. **keyloggerWithTimestamp.py** - Enhanced keylogger that includes timestamps for each keystroke.
3. **keyloggerWithScreenshot.py** - Keylogger that captures keystrokes with timestamps and takes screenshots at set intervals.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Bulushi9/keylogger
   cd keylogger
   ```

2. **Install Dependencies**:
   ```bash
   pip install pynput
   ```

## Scripts Overview

### 1. Simple Keylogger (`keyloggerSimple.py`)

   - **Description**: This is a basic keylogger that captures every keystroke and logs it to a file called `keylog.txt`.
   - **Usage**: Run the script, and it will start logging keys until you stop it.
   - **How It Works**:
      - Captures keystrokes using `pynput`.
      - Logs each keystroke to `keylog.txt` in plain text.

   **Example Output in `keylog.txt`**:
   ```plaintext
   a
   b
   c
   [ENTER]
   d 
   ```

### 2. Keylogger with Timestamps (`keyloggerWithTimestamp.py`)

   - **Description**: This version includes timestamps for each keystroke, allowing you to track exactly when each key was pressed.
   - **Usage**: Run the script, and it will log each keystroke with a timestamp to a file named with the session’s start time, e.g., `keylog_2024-10-30_14-30-00.txt`.
   - **How It Works**:
      - Creates a timestamped filename for each session.
      - Logs each keystroke with the current time to make tracking easier.

   **Example Output in `keylog_YYYY-MM-DD_HH-MM-SS.txt`**:
   ```plaintext
    2024-10-30 14:30:01: a
    2024-10-30 14:30:02: b
    2024-10-30 14:30:03: [ENTER]
    2024-10-30 14:30:04: d 
   ```

### 3. Keylogger with Screenshots (`keyloggerWithScreenshot.py`)

   - **Description**: This version captures keystrokes with timestamps and takes screenshots every 60 seconds, saving each screenshot with a timestamped filename.
   - **Usage**: Run the script, and it will log keystrokes and take screenshots at intervals until you stop it.
   - **How It Works**:
      - Logs keystrokes as in the timestamped version.
      - Runs a background thread that captures and saves screenshots every 60 seconds.
      - Screenshots are saved as `screenshot_YYYY-MM-DD_HH-MM-SS.png`.

   **Example Output in `keylog_YYYY-MM-DD_HH-MM-SS.txt`**:
   ```plaintext
    2024-10-30 14:30:01: a
    2024-10-30 14:30:02: b
    2024-10-30 14:30:03: [ENTER]
    2024-10-30 14:30:04: d 
    ```
   
**Example Screenshot Filenames:**
- screenshot_2024-10-30_14-31-00.png
- screenshot_2024-10-30_14-32-00.png


## Usage
Stopping the Script: Each script can be stopped by pressing Ctrl + C in the terminal where it is running.

## Disclaimer
**This keylogger project is intended solely for educational purposes. Unauthorized use of keyloggers is illegal and unethical. Please use responsibly and ensure compliance with applicable laws.**

## Dependencies
- Python 3.x
- `pynput` library (install with `pip install pynput`)
- `pyautogui` library (for screenshots in keyloggerWithScreenshot.py)

## Future Enhancements
- Add encryption to the log files for secure storage.
- Implement a feature to periodically email logs to a specified address.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
