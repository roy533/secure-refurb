# secure-refurb
A Python tool used for checking Linux computer readiness and generating system reports.

## Current features

- Displays operating system, processor architecture, and Python version.
- Checks available disk space against a configurable threshold.
- Saves system information and disk-space result to 'report.json'.
- Rejects negative, infinite, and NaN minimum disk-space thresholds.
- Supports `--output` to choose the JSON report destination.
- Reports saving errors clearly and returns exit status 1 when saving fails.

## Running the tool

Requires Python 3.10 or newer. No additional packages are necessary.

```bash
python3 secure_refurb.py
```

The report is saved in the current working directory. Each run replaces the previous report.

Choose a report filename:
```bash
python3 secure_refurb.py --output my-report.json
```

Without `--output`, the report is saved as `report.json` in the current reporting directory. Each run replaces the destination file. The destination folder must already exist.

## Project status
*last updated: November 23, 2026*

**In development — working prototype**

SecureRefurb generates JSON reports containing system information, disk-space checks, and a Linux memory-capacity check.

All 18 automated tests passed on macOS and Ubuntu x86_64 on a physical ThinkPad T14 Gen 2. The ThinkPad reported 15.3 GiB of usable memory, passing the default 4 GiB minimum. It's JSON report was generated and parsed successfully.

Earlier validation in an Ubuntu ARM64 virtual machine in UTM passed the 14 tests available at the time.

The memory check reads Linux's `/proc/meminfo`. When memory information cannot be read, it reports an unknown result with an error explaination.

**Next milestone:** Add a firewall status check on Ubuntu. 

Additional readiness checks and HTML reports are planned.

See [ROADMAP.md](ROADMAP.md) for the development plan.

## Testing

Run the automated tests from the repository directory:

```bash
python3 -m unittest -v
```
## Ubuntu validation

Validated on October 29, 2026 using Ubuntu Server in UTM.

- Ubuntu: 24.04.5 LTS
- Architecture: ARM64 (`aarch64`)
- Python: 3.12.3
- Automated tests: all 14 passed
- Report: `ubuntu-report.json` generated and parsed successfully
- Disk check: passed with 51.9 GiB available against a 20 GiB minimum
- No code changes were required for this run.

## Physical hardware validation

Validated on November 17, 2026 using Ubuntu Desktop on a refurbished Lenovo ThinkPad T14 Gen 2 Intel.

- Hardware: Core-i5-1145G7, 16 GB RAM, 256 GB SSD
- Architecture: x86_64
- Python: 3.12.3
- Automated tests: all 14 passed
- Report: 'thinkpad-report.json' generated and parsed successfully
- Disk check: passed with 86.0 GiB available against a 20 GiB minimum

## Memory-capacity validation

Validated on November 23, 2026 using Ubuntu Desktop on a refurbished Lenovo ThinkPad T14 Gen 2 Intel.

- All 18 automated tests passed on macOS and Ubuntu.
- The ThinkPad reported 15.3 GiB of usable memory.
- The memory-capacity check passed against the default 4 GiB minimum.
- On macOS, the Linux memory check reports an unknown result with an explaination that it was because `/proc/meminfo` is unavailable. 