#!/usr/bin/env python3

import subprocess

interface = "wlan0"
new_mac = "00:D4:K1:X9:5o:6B"
print(f"[+] Changing MAC address for {interface} to {new_mac}")
# subprocess.call("sudo ifconfig eth1 down", shell=True)
# subprocess.call("sudo ifconfig eth1 hw ether 10:20:30:40:50:80", shell=True)
# subprocess.call("sudo ifconfig eth1 up", shell=True)
