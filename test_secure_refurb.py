import json
import subprocess
import sys
import tempfile
from pathlib import Path
import argparse
import unittest
from types import SimpleNamespace
from unittest.mock import patch
from secure_refurb import check_disk_space, non_negative_finite_gib

class TestCheckDiskSpace(unittest.TestCase):
    def test_sufficient_space_passes(self):
        fake_disk = SimpleNamespace(free=30 * (1024 ** 3))

        with patch("secure_refurb.shutil.disk_usage", return_value=fake_disk):
            result = check_disk_space(minimum_free_gib=20)

            self.assertTrue(result["passed"])
            self.assertEqual(result["free_gib"], 30.0)
            self.assertEqual(result["minimum_free_gib"], 20)

    def test_insufficient_space_fails(self):
        fake_disk = SimpleNamespace(free=10 * (1024 ** 3))

        with patch("secure_refurb.shutil.disk_usage", return_value=fake_disk):
            result = check_disk_space(minimum_free_gib=20)

            self.assertFalse(result["passed"])
            self.assertEqual(result["free_gib"], 10)

    def test_edge_case_exact_minimum(self):
        fake_disk = SimpleNamespace(free=20 * (1024 ** 3))

        with patch("secure_refurb.shutil.disk_usage", return_value=fake_disk):
            result = check_disk_space(minimum_free_gib=20)

            self.assertTrue(result["passed"])
            self.assertEqual(result["free_gib"], 20)

    def test_missing_path_returns_unknown(self):
        with patch(
            "secure_refurb.shutil.disk_usage",
            side_effect=FileNotFoundError("No such file or directory")
        ):
            result = check_disk_space(path="/missing-test-path")

        self.assertIsNone(result["passed"])
        self.assertIsNone(result["free_gib"])
        self.assertEqual(result["error"], "No such file or directory")
        self.assertEqual(result["path"], "/missing-test-path")

    def test_os_error_returns_unknown(self):
        with patch(
            "secure_refurb.shutil.disk_usage",
            side_effect=OSError("Disk error")
        ):
            result = check_disk_space(path="/error-test-path")

        self.assertIsNone(result["passed"])
        self.assertIsNone(result["free_gib"])
        self.assertEqual(result["error"], "Disk error")
        self.assertEqual(result["path"], "/error-test-path")

    def test_permission_error_returns_unknown(self):
        with patch(
            "secure_refurb.shutil.disk_usage",
            side_effect=PermissionError("Permission denied")
        ):
            result = check_disk_space(path="/restricted-test-path")

        self.assertIsNone(result["passed"])
        self.assertIsNone(result["free_gib"])
        self.assertEqual(result["error"], "Permission denied")
        self.assertEqual(result["path"], "/restricted-test-path")

class TestThresholdValidation(unittest.TestCase):
    def test_valid_threshold(self):
        for value, expected in [("0", 0.0), ("20", 20.0), ("2.5", 2.5)]:
            with self.subTest(value=value):
                self.assertEqual(non_negative_finite_gib(value), expected)

        def test_invalid_threshold_non_numeric(self):
            for value in ["-1", "inf", "-inf", "nan", "abc"]:
                with self.subTest(value=value):
                    with self.assertRaises(argparse.ArgumentTypeError):
                        non_negative_finite_gib(value)

    def test_invalid_threshold_non_numeric(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            non_negative_finite_gib("abc")

    def test_invalid_threshold_negative(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            non_negative_finite_gib("-5")

    def test_invalid_threshold_infinite(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            non_negative_finite_gib("inf")

    def test_invalid_threshold_nan(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            non_negative_finite_gib("nan")

class TestReportSaving(unittest.TestCase):
    def run_script(self, working_directory, *arguments):
        script = Path(__file__).resolve().with_name("secure_refurb.py")

        return subprocess.run(
            [sys.executable, str(script), *arguments],
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=10
        )

    def test_report_saved(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.run_script(folder)

            self.assertEqual(result.returncode, 0, result.stderr)

            report_file = Path(folder) / "report.json"
            self.assertTrue(report_file.is_file())

            with report_file.open(encoding="utf-8") as report_file:
                report = json.load(report_file)

            self.assertIn("disk_space", report)
            self.assertIn("operating_system", report)

    def test_save_failure_error(self):
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder) / "missing-folder" / "report.json"

            result = self.run_script(
                folder, "--output", str(destination)
            )

            self.assertEqual(result.returncode, 1)
            self.assertIn("Unable to save report", result.stderr)
            self.assertIn(str(destination), result.stderr)
            self.assertNotIn("Traceback", result.stderr)
            self.assertNotIn("Report saved successfully", result.stdout)
            self.assertFalse(destination.exists())

    def test_default_report_saved(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.run_script(folder)

            self.assertEqual(result.returncode, 0, result.stderr)

            report_file = Path(folder) / "report.json"
            self.assertTrue(report_file.is_file())

            with report_file.open(encoding="utf-8") as report_file:
                report = json.load(report_file)

            self.assertIn("disk_space", report)
            self.assertIn("operating_system", report)
            
if __name__ == "__main__":
    unittest.main()