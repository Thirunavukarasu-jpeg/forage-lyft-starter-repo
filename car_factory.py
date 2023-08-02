
from car import Car

from engine.model import capulet_engine,sternman_engine,willoughby_engine

from battery.model import nubbin_battery,spindler_battery

from tires.model import carrigan_tires, octoprime_tires

from datetime import date

class CarFactory():
    def create_calliope(self,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values: list) -> Car:
        engine = capulet_engine.CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = spindler_battery.SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        tire = carrigan_tires.CarriganTires(tire_wear_values)
        return Car(engine=engine,battery=battery,tire=tire)

    def create_glissade(self,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values: list) -> Car:
        engine = willoughby_engine.WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        tire = octoprime_tires.OctoprimeTires(tire_wear_values)
        battery = spindler_battery.SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=engine,battery=battery,tire=tire)
    
    def create_palindrome(self,current_date: date, last_service_date: date, warning_light_on: bool, tire_wear_values: list) -> Car:
        engine = sternman_engine.SternmanEngine(warning_light_on)
        battery = spindler_battery.SpindlerBattery(current_date=current_date,last_service_date=last_service_date)
        tire = carrigan_tires.CarriganTires(tire_wear_values)
        return Car(engine=engine,battery=battery,tire=tire)
    
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values: list) -> Car:
        engine = willoughby_engine.WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = nubbin_battery.NubbinBattery(current_date=current_date,last_service_date=last_service_date)
        tire = octoprime_tires.OctoprimeTires(tire_wear_values)
        return Car(engine=engine,battery=battery,tire=tire)
    
    def create_thovex(self,current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear_values: list) -> Car:
        engine = capulet_engine.CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        tire = octoprime_tires.OctoprimeTires(tire_wear_values)
        battery = nubbin_battery.NubbinBattery(current_date=current_date,last_service_date=last_service_date)
        return Car(engine=engine,battery=battery,tire=tire)