# SecureRefurb Roadmap

SecureRefurb is a Python tool for assessing computer readiness and generating reports, inspired by my computer-refurbishment experience at Kramden Institute.

## First-release goal

Build an Ubuntu readiness checker with four to six read-only checks, JSON and HTML reports, automated tests, and a documented demonstration on physical hardware.

## Completed: inital prototype

- [x] Collect operating system, processor architecture, and Python information.
- [x] Check available disk space against a minimum threshold.
- [x] Generate a JSON report.
- [x] Separate program execution into main().
- [x] Add three automated disk-space tests.
- [x] Run successfully on macOS with Apple Silicon.

## Completed: reliable error handling

- [x] Handle missing paths and permission errors.
- [x] Report unavailable measurements as "unable to determine."
- [x] Include an explanation of each error in the report.
- [x] Add automated tests for error cases.
- [x] Confirm existing tests still pass.
- [x] Add a dedicated automated test for permission errors.

## Completed: command-line options

- [x] Allow users to select the disk path.
- [x] Allow users to set the minimum free space.
- [x] Validate minimum free space: accept finite, non-negative numbers.
- [x] Add automated tests for valid and invalid thresholds.
- [x] Provide command-line help.
- [x] Allow users to choose the report filename with '--output'.
- [x] Handle report-saving errors with a clear message.
- [x] Return exit status 1 when saving fails.
- [x] Add automated tests for custom report output and saving failures.
- [X] Test that running without '--output' creates 'report.json'.

## Completed: Ubuntu validation

- [X] Run the script and all 14 tests in an Ubuntu environment.
- [X] Collect Ubuntu distribution and version information. (Ubuntu 24.04.5 LTS, ARM64 (aarch64), and Python 3.12.3.)
- [X] Generate and successfully parse `ubuntu-report.json`.
- [X] Document the tested environment and any limitations in README.md.

Validation completed on October 29. 2026 in UTM. Physical hardware testing remains pending.

## Next: physical hardware and additional checks

- [ ] Run SecureRefurb on a spare or refurbished computer.
- [ ] Document the machine's hardware and test results.
- [ ] Add a memory-capacity check.
- [ ] Add a firewall-status check.
- [ ] Add selected SSH configuration checks.
- [ ] Include evidence, explanations, and tests for each check.

## First release: v0.1.0

- [ ] Generate a readable HTML report.
- [ ] Include a clearly labeled sample report.
- [ ] Document installation, usage, and limitations.
- [ ] Record a short demonstration on Ubuntu hardware.
- [ ] Publish a tagged release.

# Possible future work

These ideas are outside the first-release scope:

- Storage-health information
- Battery-health information
- Additional Linux distribution
- Support for Windows