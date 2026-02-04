from abc import ABC, abstractmethod
from datetime import datetime

# Abstract Base Class
class ParkingPass(ABC):
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

    @abstractmethod
    def calculate_fee(self, hours):
        pass


# Single Entry Pass
class SingleEntryPass(ParkingPass):
    def calculate_fee(self, hours):
        return hours * 5


# Monthly Pass
class MonthlyPass(ParkingPass):
    def calculate_fee(self, hours):
        return 100


# Parking System Class
class ParkingSystem:
    def __init__(self):
        self.active_vehicles = {}
        self.total_spaces = 300

    def vehicle_entry(self, vehicle_number):
        if len(self.active_vehicles) < self.total_spaces:
            self.active_vehicles[vehicle_number] = datetime.now()
            print("Vehicle Entered")
        else:
            print("Parking Full")

    def vehicle_exit(self, vehicle_number, pass_type):
        if vehicle_number in self.active_vehicles:
            entry_time = self.active_vehicles.pop(vehicle_number)
            hours = (datetime.now() - entry_time).seconds / 3600

            fee = pass_type.calculate_fee(hours)
            print("Parking Fee =", fee)
        else:
            print("Vehicle Not Found")


# Example Run
if __name__ == "__main__":
    system = ParkingSystem()

    system.vehicle_entry("ABC123")

    pass1 = SingleEntryPass("ABC123")
    system.vehicle_exit("ABC123", pass1)
