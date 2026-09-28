import platform
import shutil

print("SecureRefurb - System Information")
print("Operating System:", platform.system())
print("Processor architecture:", platform.machine())
print("Python version:", platform.python_version())

import sys
print("Python executable:", sys.executable)

disk = shutil.disk_usage(".")
free_gib = disk.free / (1024 ** 3)
minimum_free_gib = 20

print(f"\nFree disk space: {free_gib:.1f} GiB")
print(f"Minimum required disk space: {minimum_free_gib} GiB")

if free_gib >= minimum_free_gib:
    print("Disk space check passed.")
else:
    print("Disk space check failed. Insufficient free space.")