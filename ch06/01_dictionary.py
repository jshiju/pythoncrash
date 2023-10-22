# defining empty dict

car = {}
print(car)

car = {'make': 'tata', 'model': 'nexon'}
print(car)

car['cc'] = 1200
print(car)

del car['cc']
print(car)

car.update({'type': 'electric', 'battery': '12Kwh'})
print(car)

car['cc'] = 1200
print(car)

car.pop('battery')
print(car)

