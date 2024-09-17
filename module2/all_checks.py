#!/usr/bin/env python3
  
import os
import sys

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if disk_full():
	print("Disk full.")
	sys.exit(1)
    print("Everything ok.")
    sys.exit(0)

main()
