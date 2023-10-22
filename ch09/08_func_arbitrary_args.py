
def manyargs(*args):
    for arg in args:
        print(arg, end=' ')
    print('\n')

manyargs('jazz', 'pop')
manyargs('jazz', 'pop', 'soft')