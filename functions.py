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