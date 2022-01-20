class Vehicle:
    def general_usage(self):
        print("General use: transportation")


class Car(Vehicle):  # inheritance
    def __init__(self):
        print("This is a car.")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Specific use: commute to work, vacation with family")


class Motorcycle(Vehicle):  # inheritance
    def __init__(self):
        print("This is a motorcycle.")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("Specific use: road trip, racing")


if __name__ == '__main__':
    c = Car()
    c.general_usage()
    c.specific_usage()

    print()

    m = Motorcycle()
    m.specific_usage()

    print()

    if isinstance(c, Car):
        print("We have a car object.")

    if issubclass(Car, Vehicle):
        print("Car is a subclass of Vehicle.")

