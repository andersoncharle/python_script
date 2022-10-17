#!/usr/bin/env python3

import subprocess

subprocess.call("sudo ifconfig eth1 down", shell=True)
subprocess.call("sudo ifconfig eth1 hw ether 10:20:30:40:50:80", shell=True)
subprocess.call("sudo ifconfig eth1 up", shell=True)
