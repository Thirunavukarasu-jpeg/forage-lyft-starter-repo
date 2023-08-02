from tires.tire import Tire

class CarriganTires(Tire):
    def __init__(self,tire_wear: list) -> None:
        self.tire_wear_values = tire_wear
        self.tire_wear_threshold = 0.9
    def needs_service(self) -> bool:
        for tire_wear in self.tire_wear_values:
            if tire_wear >= self.tire_wear_threshold:
                return True
        return False