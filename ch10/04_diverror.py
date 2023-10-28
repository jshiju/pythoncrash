try:
    print(5/0)
# except ZeroDivisionError:
except BaseException:
    print("You can't divide by zero!")