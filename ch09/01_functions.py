
# python doesn't support method overloading directly !!
def greet(name):
    print(f'Hello, {name}')

def greet(name, age):
    print(f'Hello Mr., {name}')

def greet(name):
    print(f'Hello, {name}')
greet('Roger', 10)