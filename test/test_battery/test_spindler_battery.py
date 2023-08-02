import unittest
from datetime import date,datetime

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.today().date()
        last_service_date = date.fromisoformat("2018-11-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.today().date()
        last_service_date = date.fromisoformat("2018-01-11")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
