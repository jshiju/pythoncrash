
# return needed
# def greet(name: str='Janie', age:int=20):
#    f'Hello Mr., {name}. You are {age} years old!'

# this works
# def greet(name: str='Janie', age:int=20):
#    return f'Hello Mr., {name}. You are {age} years old!'

# this works
# def greet(name: str='Janie', age:int=20) -> str:
#    return f'Hello Mr., {name}. You are {age} years old!'

# this too works!!
def greet(name: str='Janie', age:int=20) -> None:
    return f'Hello Mr., {name}. You are {age} years old!'

print(greet())
