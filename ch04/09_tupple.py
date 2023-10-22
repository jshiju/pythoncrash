dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# TypeError: 'tuple' object does not support item assignment
# dimensions[1] = 100


# tupple with one element
# mono = (10) - will be treated as integer within paranthesis
# TypeError: 'int' object is not subscriptable

mono = (10,)
print(mono[0])

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)



