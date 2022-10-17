#!/usr/bin/env python3

import subprocess
from optparse import OptionParser


def get_arguments():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    return parser.parse_args()


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
