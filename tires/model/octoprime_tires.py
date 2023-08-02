from tires.tire import Tire

class OctoprimeTires(Tire):
    def __init__(self,tire_wear: list) -> None:
        self.tire_wear_values = tire_wear
        self.tire_wear_threshold = 3
        
    def needs_service(self) -> bool:
        return sum(self.tire_wear_values) >= 3