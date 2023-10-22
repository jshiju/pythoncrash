car = {'make': 'tata', 'model': 'nexon'}

# KeyError: 'type'
# car['type']

print(car.get('make'))
print(car.get('type'))

print(car.get('type','electric'))

if car.get('type') == None:
    print('Type info not avaiable')
