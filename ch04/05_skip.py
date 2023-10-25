players = ['charles', 'martina', 'michael', 'florence', 'eli', 'smith', 'jane', 'rhode', 'jim']


print(players[0::2])

print(players[0:7:2])

print(players[-6::2])

# ValueError: slice step cannot be zero
# print(players[-6::0])

# no error on negative step
print(players[0:7:-2])