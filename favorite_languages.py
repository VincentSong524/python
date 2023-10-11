import my_tools

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favotite language is {language}.")

my_tools.line()

for name, language in favorite_languages.items():
    print(f"{name}'s favorite language is {language}.")

my_tools.line()

for name in favorite_languages.keys():
    print(name.title())

my_tools.line()

for name in favorite_languages:
    print(name.title())

my_tools.line()

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

my_tools.line()

for language in set(favorite_languages.values()):
    print(language)