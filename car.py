class Car:
    def __init__(self, make, model, year,for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.for_sale = for_sale
    def drive(self):
        print("The car is driving.")
    def stop(self):
        print("The car has stopped.")