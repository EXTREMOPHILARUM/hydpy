class: center, middle

# hydpy.saurabhn.com

---

class: center, middle

# You can find me @EXTREMOPHILARUM

---
class: center, middle

# Sniffing your way through the network

---

# Here's the Agenda

1. What?
2. Why?
3. How to do it?
4. How can you be safe?

---
# What?

.center[![Trojan](https://www.greycampus.com/hubfs/Imported_Blog_Media/What%20is%20a%20Sniffing%20attack%20and%20How%20can%20you%20defend%20it.jpg)]

---
class: center, middle
# Why?

.center[![Trojan]()]

---
# ARP packets
- ARP packets are used to map IP addresses to MAC addresses
- There are two types of ARP packets
    - ARP request
    - ARP reply
- ARP request is used to find the MAC address of a host on the network
- ARP reply is used to reply to the ARP request

---
# ARP cache
- ARP cache is a table that stores the mapping of IP addresses to MAC addresses
---
# ARP cache poisoning
ARP poisoning is a technique used to intercept traffic between two hosts on the network. This is done by sending fake ARP replies to the hosts. The hosts will then start sending traffic to the attacker instead of the intended host.
---
class: center, middle

# Prerequisites
```bash
pip3 install scapy
```
---
# Step 1: Lets Sniff the default interface

```python
# sniff with default interface
from scapy.all import *
sniff(filter="port 80", prn=process_packet, store=False)
```

---
# How to perform ARP cache poisoning
- We will be using scapy to perform the same
- Scapy is a python library that allows us to send and receive packets
- We will be using the following code to perform the same
```python
from scapy.all import *
# send an ARP reply to the victim
send(ARP(op=2, pdst="victim_ip", hwdst="victim_mac", psrc="attacker_ip"))
# send an ARP reply to the gateway
send(ARP(op=2, pdst="gateway_ip", hwdst="gateway_mac", psrc="attacker_ip"))
```
- The above code will send an ARP reply to the victim and the gateway
- The victim will then start sending traffic to the attacker
- Similarly, the gateway will also start sending traffic to the attacker
- we can then sniff the traffic using the following code
```python
sniff(filter="port 80", prn=process_packet, store=False)
```
- The above code will sniff all the traffic on port 80
- We can then perform operations on the traffic
- Like, we can print the traffic to the console
- or can extract the data from the traffic like cookies, passwords, etc

---
# How to prevent ARP cache poisoning
- We can prevent ARP cache poisoning by monitoring the ARP cache and ARP traffic on the network.
- We can use the following code to monitor the ARP cache
```python
from scapy.all import *
# sniff for ARP packets
sniff(filter="arp", prn=process_packet, store=False)
```
- The above code will sniff all the ARP packets on the network
- We can then check if the ARP cache is poisoned or not
- As we know, ARP cache poisoning is done by sending fake ARP replies
- So, we can check if the ARP cache is poisoned by checking if the ARP cache has the IP address of the attacker
- If the ARP cache has the IP address of the attacker, then the ARP cache is poisoned
- We can then send an ARP reply to the victim and the gateway to remove the attacker from the ARP cache
- by using the following code
```python
from scapy.all import *
# send an ARP reply to the victim
send(ARP(op=2, pdst="victim_ip", hwdst="victim_mac", psrc="gateway_ip"))
# send an ARP reply to the gateway
send(ARP(op=2, pdst="gateway_ip", hwdst="gateway_mac", psrc="victim_ip"))
```
---
# Conclusion
- We have seen how to perform ARP cache poisoning
- We have also seen how to prevent ARP cache poisoning
- We now know how to sniff traffic on the network
- We can now perform operations on the traffic

---
class: center, middle

# Any questions?
