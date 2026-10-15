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

**In development — working prototype**

Currently tested on macOS with Apple Silicon. The tool collects
system information, checks available disk space, and generates
a JSON report.

Three automated unit tests cover sufficient disk space,
insufficient space, and the exact minimum threshold.

**Next milestone:** Handle disk-reading errors and report
unavailable measurements clearly.

Ubuntu validation, command-line options, additional readiness
checks, and HTML reports are planned in the future.

See [ROADMAP.md](ROADMAP.md) for the development plan.