class Vehicle:

    def __init__(self, make, year):
        self.make = make
        self.year = year

    def describe(self):
        return f"Vehicle: {self.make} of {self.year}"


class Car(Vehicle):

    # use optional arguments with default value to simulate
    # constrcutor with multiple arguments
    def __init__(self, make, year, type=''):
        self.make = make
        self.year = year
        self.type = type

    def describe(self):
        return f"Car: {self.make} {self.type} of {self.year}"


def main():

    print("This is from main")
    v = Vehicle('hyndai', 2023) # using default argument value
    print(v.describe())

    print("This is from main")
    v = Car('suzuki', 2023) # using default argument value
    print(v.describe())

    v = Car('nexon', 2023, 'amt')
    print(v.describe())

main()

