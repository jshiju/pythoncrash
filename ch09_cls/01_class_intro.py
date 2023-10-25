class Vehicle:

    def __init__(self, make, year):
        self.make = make
        self.year = year

    def describe(self):
        return f"Vehicle: {self.make} of {self.year}"

def main():
    print("This is from main")
    v = Vehicle('suzuli', 2023)
    print(v.describe())

main()

