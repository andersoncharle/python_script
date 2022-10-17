#!/usr/bin/env python3

import subprocess
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="interface to change it's MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print(f"[+] Changing MAC address for {interface} to {new_mac}")


subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])
