import platform
import shutil
import json

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

report = {
    "operating_system": platform.system(),
    "processor_architecture": platform.machine(),
    "python_version": platform.python_version(),
    "disk_space": {
        "path": ".",
        "free_gib": round (free_gib, 1),
        "minimum_free_gib": minimum_free_gib,
        "passed": free_gib >= minimum_free_gib
    }
}

with open("report.json", "w", encoding="utf-8") as report_file:
    json.dump(report, report_file, indent=4)

print("Report generated and saved successfully.")