import unittest
from types import SimpleNamespace
from unittest.mock import patch

from secure_refurb import check_disk_space

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

if __name__ == "__main__":
    unittest.main()