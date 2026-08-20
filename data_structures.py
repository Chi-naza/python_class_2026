## LISTS

my_list = [1, 2, 3, 4, 5]
my_second_list = ["China", "United States", "Germany", "France"]

print(my_list)
print(my_second_list)

my_second_list.append(4)
print(my_second_list)

my_second_list.insert(0, "Nigeria")
my_second_list.remove("Germany")
print(my_second_list)

last_item = my_second_list.pop() # remove and return the last
print("Last item removed:", last_item)

del my_second_list[0] # delete the first item
print(my_second_list)

numbers = [67, 8, 90, 1, 34, 56, 23, 78, 0, 12, 45, 89, 100]
print(numbers)
numbers.sort()
print(numbers)
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))
print("Count of 34:", numbers.count(34)) # return number of occurences
print("Index of 34:", numbers.index(34))

numbers.reverse()
print(numbers)

new_numbers = numbers.copy()
print("New numbers:", new_numbers)



## DICTIONARIES

person = {"name": "John", "age": 30, "city": "New York"}
print(person)
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

person["age"] = 31
person["country"] = "USA"
print(person)

person["is_male"] = True
print(person)

del person["age"]
print(person)

print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

person.update({"age": 32, "city": "Los Angeles", "email": "john@example.com"})
print("Updated person:", person)



## TUPLES
# Tuples are immutable, meaning they cannot be changed after creation.


empty_tuple = ()
print(empty_tuple)

colors = ("red", "green", "blue")
print(colors)

colors_list = list(colors)
print("Colors as list:", colors_list)

colors[0]
colors[0] = "yellow" # This will raise an error because tuples are immutable




## SETS
# Sets are unordered collections of unique elements.

num_sets = {1, 2, 3, 4, 5}
print(num_sets)

sec_set = set([4, 5, 6, 7, 8, "Hello", "Program", 4, 4, 7])
print(sec_set)

num_sets.add(6)
num_sets.remove(44) # error if not found
num_sets.discard(2) # no error if not found
print(num_sets)

if 3 in num_sets:
    print("3 is in the set")
