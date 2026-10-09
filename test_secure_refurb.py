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

if __name__ == "__main__":
    unittest.main()