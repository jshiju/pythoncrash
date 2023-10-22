
def greet(name, age):
    print(f'Hello Mr., {name}. You are {age} years old!')

# types not making any difference !
def greet(name: str='Brad', age:int=20):
    print(f'Hello Mr., {name}. You are {age} years old!')

# you may get wierd output
def greet(name: str=20, age:int='Janie'):
    print(f'Hello Mr., {name}. You are {age} years old!')

greet('Leo')
greet(age=40, name='Nat')
greet()