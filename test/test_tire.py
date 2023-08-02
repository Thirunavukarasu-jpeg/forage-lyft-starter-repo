import unittest
import datetime
from car_factory import CarFactory

class TestCarrigan(unittest.TestCase):
    def tire_need_to_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        car_factory = CarFactory()
        tire_wear_values = [0,0.4,0.6,0.9]
        car = car_factory.create_palindrome(today, last_service_date, current_mileage, last_service_mileage,tire_wear_values)
        self.assertTrue(car.needs_service())
    def tire_need_not_to_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        car_factory = CarFactory()
        tire_wear_values = [0,0.4,0.6,0.5]
        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage,tire_wear_values)
        self.assertFalse(car.needs_service())
class TestOctoprime(unittest.TestCase):
    def tire_need_to_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        car_factory = CarFactory()
        tire_wear_values = [1,0.4,0.9,0.9]
        car = car_factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage,tire_wear_values)
        self.assertTrue(car.needs_service())
    def tire_need_not_to_be_serviced(self):
        last_service_date = datetime.today().date()
        today = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        car_factory = CarFactory()
        tire_wear_values = [0,0.4,0.6,0.9]
        car = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage,tire_wear_values)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
