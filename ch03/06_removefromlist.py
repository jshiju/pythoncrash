
motorcycles = ['honda', 'yamaha', 'suzuki', 'harley', 'bajaj']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

del motorcycles[-2]
print(motorcycles)

# IndexError: list assignment index out of range
# del motorcycles[-8]

motorcycles.pop()
print(motorcycles)

motorcycles.pop()
print(motorcycles)
