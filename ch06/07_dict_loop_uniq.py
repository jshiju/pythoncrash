favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in sorted(set(favorite_languages.values())):
    print(f"{name.title()}, a top lang")
