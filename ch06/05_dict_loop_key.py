favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in favorite_languages.keys():
    print(name.title())

# default behaviour
for name in favorite_languages:
    print(name.title())

if 'sarah' in favorite_languages.keys():
    print('in learner list')
if 'matt' not in favorite_languages.keys():
    print('not in learner list')