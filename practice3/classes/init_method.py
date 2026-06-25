class Car:
    """Represents a car."""

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")

car = Car("Toyota", 2022)
car.display_info()