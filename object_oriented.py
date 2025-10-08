class Car:
    def __init__(self, make, model, year,for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.for_sale = for_sale

Car1 = Car("Toyota", "Corolla", 2020, True)
print(Car1.make) 
print(Car1.model)
print(Car1.year)
print(Car1.for_sale)