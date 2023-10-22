prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

meet = 5
# SyntaxError: invalid syntax
# meet++
meet += 1

nth = "st" if meet == 1 else "nd"
nth = "rd" if meet == 3 else nth
nth = "th" if meet > 3 else nth

print(f"Meeting {meet}{nth} time!")