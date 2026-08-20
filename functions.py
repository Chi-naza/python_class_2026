def sayHello(name):
    print("Hello, World! - ", name)
    

sayHello("Chinaza")

def addNumbers(a=1, b=3):
    return a + b

result = addNumbers()
print("With default values: ", result)

result = addNumbers(5, 10)
print("With positional values: ", result)

result = addNumbers(a=5, b=10)
print("With specified values: ", result)


def calculateArea(length, width):
    area = length * width
    return area

room_size = calculateArea(length=12, width = 26)
print("The area of the room is: ", room_size)


# Returning multiple values from a function

def smallFunction():
    numbers = [32, 8, 90, 44]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number


first, last = smallFunction()
print("The first number is: ", first)
print("The last number is: ", last)

