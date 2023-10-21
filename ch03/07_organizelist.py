
numlist = []

for nums in range(1, 10):
    numlist.append(nums)
print(numlist)

#newlist = sorted(numlist)
newlist = numlist
print((sorted(numlist)).reverse())
print("Orginal: " + ','.join(str(e) for e in numlist))
print("Sorted: " + ','.join(str(e) for e in newlist))

numlist.sort(reverse=True)
print(numlist)

print(sorted(newlist))

#

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
cars.reverse()
print(cars)
