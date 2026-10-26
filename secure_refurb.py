import platform
import shutil
import json
import sys
import argparse
import math
def check_disk_space(path=".", minimum_free_gib=20):
    try:
        disk = shutil.disk_usage(path)
    except OSError as error:
       return {
           "path": path,
           "free_gib": None,
           "minimum_free_gib": minimum_free_gib,
           "passed": None,
           "error": str(error)
    }

    free_gib = disk.free / (1024 ** 3)

    return {
        "path": path,
        "free_gib": round(free_gib, 1),
        "minimum_free_gib": minimum_free_gib,
        "passed": free_gib >= minimum_free_gib,
        "error": None
    }

def non_negative_finite_gib(value):
    try:
        number = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("must be a number")

    if not math.isfinite(number) or number < 0:
        raise argparse.ArgumentTypeError("must be a finite non-negative number")
    return number

def main():
    parser = argparse.ArgumentParser(description="Check computer readiness and generate JSON report.")
    parser.add_argument("--path", default=".", help="Path to check disk space")
    parser.add_argument("--minimum-free-gib", type=non_negative_finite_gib, default=20, help="Minimum free disk space required in GiB")
    parser.add_argument(
        "--output", default="report.json", help="Output JSON report file name (default: report.json)"
    )
    args = parser.parse_args()

    print("SecureRefurb - System Information")
    print("Operating System:", platform.system())
    print("Processor architecture:", platform.machine())
    print("Python version:", platform.python_version())
    print("Python executable:", sys.executable)

    disk_result = check_disk_space(
        path=args.path,
        minimum_free_gib=args.minimum_free_gib
    )

    print(f"\nMinimum free disk space required: {disk_result['minimum_free_gib']} GiB")

    if disk_result["passed"] is None:
        print("Disk space check: UNABLE TO DETERMINE")
        print("Reason:", disk_result["error"])
    else:
        print(f"Free disk space: {disk_result['free_gib']:.1f} GiB")
        
        if disk_result["passed"]:
            print("Disk space check passed.")
        else:
            print("Disk space check failed. Please free up some space.")

    report = {
        "operating_system": platform.system(),
        "processor_architecture": platform.machine(),
        "python_version": platform.python_version(),
        "disk_space": disk_result
    }

    try:
        with open(args.output, "w", encoding="utf-8") as report_file:
            json.dump(report, report_file, indent=4)

    except OSError as error:
        print(f"Unable to save report to {args.output}: {error}", file=sys.stderr)
        return 1

    print(f"Report generated and saved successfully to {args.output}")
    return 0

if __name__ == "__main__":
    sys.exit(main())