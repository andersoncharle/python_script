#!/usr/bin/env python3

import subprocess
from optparse import OptionParser


def get_arguments():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    (option, arguments) = parser.parse_args()
    if not option.interface:
        parser.error("[-] Please specify an interface,use --help for more info.")
    if not option.new_mac:
        parser.error("[-] Please specify a new mac,use --help for more info.")
    return option


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
