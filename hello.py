import requests

response = requests.get("https://api.github.com")

print("RESPONSE CODE:")
print(response.status_code)

name = "Chinaza"
age = 34

long_dash = "_" * 50

print(long_dash)

len(name)

is_logged_in = True

authenticated = 3 >= 4 and is_logged_in

print(f"AUTH - {authenticated}")

print(name.lower())
print(name.upper())
print(name.title())

# Hallo Python

sentence = "Hello Python, I am learning Python programming language"

print("Split:")
print(sentence.split(" "))

print(sentence.replace("Python", "JavaScript"))

print(sentence.find("Python"))

print(sentence.startswith("Python"))
print(sentence.endswith("language"))





