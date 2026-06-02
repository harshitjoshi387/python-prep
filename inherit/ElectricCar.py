class Car:

    def __init__(self,brand ,model):
        self.brand=brand
        self.model=model
    
    def fullName(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):

    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
    
        
tesla = ElectricCar("tesla","EV","100kwh")
print(tesla.fullName())