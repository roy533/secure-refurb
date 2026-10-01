import platform
import shutil
import json
import sys

def check_disk_space(path=".", minimum_free_gib=20):
    disk = shutil.disk_usage(path)
    free_gib = disk.free / (1024 ** 3)

    return {
        "path": path,
        "free_gib": round(free_gib, 1),
        "minimum_free_gib": minimum_free_gib,
        "passed": free_gib >= minimum_free_gib
    }

print("SecureRefurb - System Information")
print("Operating System:", platform.system())
print("Processor architecture:", platform.machine())
print("Python version:", platform.python_version())
print("Python executable:", sys.executable)

disk_result = check_disk_space()

print(f"\nFree disk space: {disk_result['free_gib']:.1f} GiB")
print(f"Minimum required disk space: {disk_result['minimum_free_gib']} GiB")

if disk_result["passed"]:
    print("Disk space check passed.")
else:
    print("Disk space check failed. Insufficient free space.")

report = {
    "operating_system": platform.system(),
    "processor_architecture": platform.machine(),
    "python_version": platform.python_version(),
    "disk_space": disk_result
}

with open("report.json", "w", encoding="utf-8") as report_file:
    json.dump(report, report_file, indent=4)

print("Report generated and saved successfully.")