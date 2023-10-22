cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if len(car) == 3:
        print(car.upper())
    else:
        print(car.title())


for e in (10,3,7,6):
    if e%2 != 0:
        print(f'Number {e} is odd')
    else:
        print(f'Number {e} is even')

