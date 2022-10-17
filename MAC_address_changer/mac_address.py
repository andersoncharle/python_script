#!/usr/bin/env python3

import subprocess

interface = input("Enter interface >> ")
new_mac = input("Enter new MAC >> ")
print(f"[+] Changing MAC address for {interface} to {new_mac}")

subprocess.call(f"sudo ifconfig {interface} down", shell=True)
subprocess.call(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True)
subprocess.call(f"sudo ifconfig {interface} up", shell=True)
