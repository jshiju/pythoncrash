# defining empty dict

car = {}
print(car)

car = {'make': 'tata', 'model': 'nexon'}
print(car)

vehicle = car.copy()

if car == vehicle:
    print('Vehicle and Car the same')


vehicle.update({'type': 'electric'})
print(vehicle)

if car != vehicle:
    print('Vehicle and Car not the same')

vehicle.pop('type')
if car == vehicle:
    print('Vehicle and Car again the same')