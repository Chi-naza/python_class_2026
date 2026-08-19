temperature = 5

is_male = True

if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")



if temperature > 30 and is_male:
    print("It's a hot day and you are a male")
elif temperature < 10 and is_male:
    print("It's a cold day and you are a male")
else:
    print("It's neither hot nor cold")



for i in range(5):
    print(i)