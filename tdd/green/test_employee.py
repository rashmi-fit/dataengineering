"""
Employee class tests.
"""
import unittest

from employee import Employee

NAME: str = "Rashmi"
EMPLOYEE_ID: int = 12345


class TestEmployeeComputePayout(unittest.TestCase):
    """Test the compute_payout method of the Employee class."""

    def setUp(self):
        """Set up test fixtures."""
        self.Rashmi = Employee(name=NAME, employee_id=EMPLOYEE_ID)

    def test_employee_payout_returns_a_float(self):
        """Whether payout returns a float."""
        self.assertIsInstance(self.Rashmi.compute_payout(), float)

    def test_employee_payout_no_commission_no_hours(self):
        """Whether payout is correctly computed in case of no commission and no hours worked."""
        self.assertAlmostEqual(self.Rashmi.compute_payout(), 1000.0)

    def test_employee_payout_no_commission(self):
        """Whether payout is correctly computed in case of no commission and 10 hours worked."""
        self.Rashmi.hours_worked = 10.0
        self.assertAlmostEqual(self.Rashmi.compute_payout(), 2000.0)

    def test_employee_payout_with_commission(self):
        """
        Whether payout is correctly computed in case of
        10 contracts landed and 10 hours worked.
        """
        self.Rashmi.hours_worked = 10.0
        self.Rashmi.contracts_landed = 10
        self.assertAlmostEqual(self.Rashmi.compute_payout(), 3000.0)

    def test_employee_payout_commission_disabled(self):
        """
        Whether payout is correctly computed in case of
        10 contracts landed and 10 hours worked,
        but commission is disabled.
        """
        self.Rashmi.hours_worked = 10.0
        self.Rashmi.contracts_landed = 10
        self.Rashmi.has_commission = False
        self.assertAlmostEqual(self.Rashmi.compute_payout(), 2000.0)


if __name__ == "__main__":
    unittest.main()
