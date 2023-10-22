
prompt = "\nWhat is your age? "

age = int(input(prompt))

# on cate error
# ValueError: invalid literal for int() with base 10: 'y6'

if age > 60:
    print("Yopu are old!")