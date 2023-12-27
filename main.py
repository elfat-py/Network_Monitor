#I am going try to create a networking progam which will be able to scan in the network
'''
Sniff Packets:
Command: sniff
Description: Initiates packet sniffing on the specified network interface.
Specify Interface:

Command: set interface [interface_name]
Description: Sets the network interface for packet sniffing.
Filter by Protocol:

Command: filter protocol [protocol_name]
Description: Filters captured packets based on a specific protocol.
Capture Packet Count:

Command: capture count [num_packets]
Description: Sets the maximum number of packets to capture before stopping.
Display Packet Details:

Command: packet details [packet_number]
Description: Displays detailed information about a captured packet.
Save Captured Packets:

Command: save packets [filename]
Description: Saves the captured packets to a specified file.
Perform Network Scan:

Command: scan [target]
Description: Initiates a network scan on the specified target using Nmap.
Analyze Pcap File:

Command: analyze file [filename]
Description: Reads and analyzes a pcap file using Pyshark.
Help:

Command: help
Description: Displays a list of available commands and their descriptions.
Exit Program:

Command: exit or quit
Description: Exits the network monitoring tool.


<I was thinking of making able to see what is the source and what is the destination so cliet server using wire
shark library, that would be one of my program options
https://www.youtube.com/watch?v=lb1Dw0elw0Q&ab_channel=VinsloevAcademy>
'''

import scapy.all as scapy
import os
import subprocess

class NetworkMonitor:
    def __init__(self):
        self.interface = None
        self.packets = []

    def set_interface(self, interface):
        self.interface = interface
        print(f"Interface set to {interface}")

    def sniff_packets(self, count=10):
        if not self.interface:
            print("Please set the interface first using 'set interface [interface_name]'")
            return

        print(f"Sniffing {count} packets on {self.interface}...")
        self.packets = scapy.sniff(iface=self.interface, store=True, count=count)

    def display_packet_details(self, packet_number):
        try:
            packet = self.packets[packet_number - 1]
            print(packet.show())
        except IndexError:
            print("Invalid packet number. Use 'sniff' command to capture packets.")

    def save_packets(self, filename):
        if not self.packets:
            print("No packets to save. Use 'sniff' command to capture packets.")
            return

        with open(filename, 'w') as file:
            for packet in self.packets:
                file.write(str(packet) + '\n')
        print(f"Packets saved to {filename}")

    def scan_network(self, target):
        print(f"Scanning network using Nmap on {target}...")
        subprocess.run(['nmap', target])

if __name__ == "__main__":
    monitor = NetworkMonitor()

    while True:
        command = input("Enter command: ").lower().split()

        if command[0] == 'set' and command[1] == 'interface':
            monitor.set_interface(command[2])

        elif command[0] == 'sniff':
            count = int(command[1]) if len(command) > 1 else 10
            monitor.sniff_packets(count)

        elif command[0] == 'packet' and command[1] == 'details':
            packet_number = int(command[2]) if len(command) > 2 else None
            monitor.display_packet_details(packet_number)

        elif command[0] == 'save' and command[1] == 'packets':
            filename = command[2] if len(command) > 2 else 'captured_packets.txt'
            monitor.save_packets(filename)

        elif command[0] == 'scan':
            target = command[1] if len(command) > 1 else None
            monitor.scan_network(target)

        elif command[0] == 'exit' or command[0] == 'quit':
            break

        else:
            print("Invalid command. Type 'help' for a list of commands.")
