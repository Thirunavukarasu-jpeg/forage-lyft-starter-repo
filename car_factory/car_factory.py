
from car import Car

from engine.model import capulet_engine,sternman_engine,willoughby_engine

from battery.model import nubbin_battery,spindler_battery

from datetime import date

class CarFactory():
    def create_calliope(self,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = capulet_engine.CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = spindler_battery.SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=engine,battery=battery)

    def create_glissade(self,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = willoughby_engine.WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = spindler_battery.SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=engine,battery=battery)
    
    def create_palindrome(self,current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=engine,battery=battery)
    
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = willoughby_engine.WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=engine,battery=battery)
    
    def create_thovex(self,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = capulet_engine.CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=engine,battery=battery)