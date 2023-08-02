from engine.engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        # super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000