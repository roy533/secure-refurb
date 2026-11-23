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

## Completed: physical hardware validation

- [X] Run SecureRefurb on a spare or refurbished computer.
- [X] Document the machine's hardware and test results.

Physical validation completed on November 17, 2026 on a refurbished ThinkPad T14 Gen 2 Intel running Ubuntu Desktop (x86_64). All 14 tests passed, and 'thinkpad-report.json' was generated and parsed successfully. See README.md for the results.

## Completed: Linux memory-capacity check

- [X] Read total memory from `/proc/meminfo`.
- [X] Compare memory against a default 4 GiB minimum.
- [X] Include the result in the JSON report.
- [X] Return an unknown result with an explaination when unavailable.
- [X] Pass all 18 automated tests on macOS and Ubuntu.
- [X] Validate in the physical ThinkPad: 15.3 GiB reported, check passed.

Completed on November 23, 2026. See README.md for validation details.

## Next: Firewall check
- [ ] Add an Ubuntu firewall-status check.
- [ ] Include its status and supporting evidence in the JSON report.
- [ ] Handle unavailable commands and permission errors.
- [ ] Add automated tests and validate on the ThinkPad. 

## Planned: Mac and ThinkPad development

- [ ] Simplify SSH access with a ThinkPad host alias.
- [ ] Run Ubuntu tests from the Mac and capture terminal output.
- [ ] Generate reports remotely and copy dated versions to the Mac.
- [ ] Document the commands and report-storage locations.
- [ ] Evaluate VS Code Remote SSH.
- [ ] Combine report generation and retrieval into one command.

## Planned: additional security checks
- [ ] Add selected SSH configuration checks.
- [ ] Include evidence, explainations, and tests for each check.

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