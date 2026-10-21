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

## Next: reliable error handling

- [x] Handle missing paths and permission errors.
- [x] Report unavailable measurements as "unable to determine."
- [x] Include an explanation of each error in the report.
- [x] Add automated tests for error cases.
- [x] Confirm existing tests still pass.
- [ ] Add a dedicated automated test for permission errors.

## Command-line options

- [ ] Allow users to select the disk path.
- [ ] Allow users to set the minimum free space.
- [ ] Allow users to choose the report filename.
- [ ] Validate inputs and provide command-line help.

## Ubuntu validation

- [ ] Run the script and tests in an Ubuntu environment.
- [ ] Collect Ubuntu distribution and version information.
- [ ] Document the tested environment and any limitations.

## Physical hardware and additional checks

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