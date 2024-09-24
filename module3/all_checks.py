#!/usr/bin/env python3
  
import os
import sys

from check_free_space import check_reboot

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("Disk full.")
        sys.exit(1)

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
    checks=[
        (check_reboot , "pending reboot"),
        (check_reboot_full , "Root partition is full"),
    ]
    allOk = True
    for check, name in checks:
        if check():
            print(f"{name} detected.")  
            sys.exit(1)
            allOk = False
    if not allOk:
        sys.exit(1)  
    print('everything is ok')
    sys.exit(0) 

main()