cars = {'honda', 'vw', 'bmw', 'benz', True, 1, 20, 20.0, 20.00000000000000005}
# True and '1' the same
print(cars)

# cars.add({'chevy'})
# TypeError: unhashable type: 'set'

cars.add('chevy')
cars.add('chevy')
print(cars)

cars.add(20.00006)
print(cars)

cars.add(20.0000000000000000006)
print(cars)
