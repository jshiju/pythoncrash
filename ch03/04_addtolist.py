motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# append - list added as another 'item' in the initial list
bikes = ["ola", "ather"]
motorcycles.append(bikes)
print(motorcycles)

# extend - spread items and add to the initial list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.extend(bikes)
print(motorcycles)