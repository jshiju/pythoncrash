
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# insert from back
motorcycles.insert(-2, 'harley')
print(motorcycles)

# invalid positive index always add to the last
motorcycles.insert(20, 'enfield')
print(motorcycles)

# invalid negative index always add as the first
motorcycles.insert(-10, 'bajaj')
print(motorcycles)