from pynput.keyboard import Key, Listener

def on_press(key):
    print(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
