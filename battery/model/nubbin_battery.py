from battery.battery import Battery

from datetime import datetime,date

class NubbinBattery(Battery):
    def __init__(self,last_service_date: date,current_date: date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date
        self.service_frequency = 4
    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + self.service_frequency)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False