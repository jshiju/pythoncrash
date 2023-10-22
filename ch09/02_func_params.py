
# def greet(name, age):
#    print(f'Hello Mr., {name}. You are {age} years old!')

# types not making any difference !
def greet(name: int, age: str):
    print(f'Hello Mr., {name}. You are {age} years old!')


greet('Leo', 38)
greet(age=40, name='Nat')