class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model


    def fullName(self):
        return f'{self.brand} {self.model}'


my_car=Car("toyota","corolla")
tata=Car("tata","safari ")
print(tata.fullName())