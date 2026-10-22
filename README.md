# secure-refurb
A Python tool used for checking Linux computer readiness and generating system reports.

## Current features

- Displays operating system, processor architecture, and Python version.
- Checks available disk space against a configurable threshold.
- Saves system information and disk-space result to 'report.json'.

## Running the tool

Requires Python 3.10 or newer. No additional packages are necessary.

```bash
python3 secure_refurb.py
```

The report is saved in the current working directory. Each run replaces the previous report.

## Project status
*last updated: October 21, 2026*

**In development — working prototype**

Currently tested on macOS with Apple Silicon. The tool collects system information, checks available disk space, and generates a JSON report.

Command-line options allow users to select the disk path with --path and set the minimum required free space with --minimum-free-gib.

Missing paths, permission errors, and other disk-reading errors are handled without crashing. Unavailable measurments are reported as "unable to determine", with an explaination included in the JSON report.

Six automated unit tests cover sufficient space, insufficient space, the exact minimum threshold, missing paths, permission errors, and general OS errors.

**Next milestone:** Validate command line inputs and allow users to choose the report filename.

Ubuntu validation, command-line options, additional readiness checks, and HTML reports are planned in the future.

See [ROADMAP.md](ROADMAP.md) for the development plan.

## Testing

Run the automated tests from the repository directory:

```bash
python3 -m unittest -v
```