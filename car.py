class Car:
    def __init__(self, make, model, year,for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.for_sale = for_sale
    def drive(self):
        print(f"The car is driving {self.make} {self.model}.")
    def stop(self):
        print(f"The car {self.make} {self.model} has stopped.")