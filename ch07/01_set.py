cars = {'honda', 'vw', 'bmw', 'benz'}

print(cars)

# TypeError: 'set' object is not subscriptable
# print(car [0])

for items in cars:
    print(items, end=' ')

cars.add('suzuki')
print(f'\n{len(cars)} : {cars}')

cars.pop()
cars.add('bmw')
print(f'{len(cars)} : {cars}')

