# Zero Division Runtime Error
try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")




try:
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")




try:
    print("My name is Chinaza")
    4/0
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This block always executes, regardless of errors.")