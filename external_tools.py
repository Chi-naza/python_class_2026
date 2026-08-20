
import math

from math import sqrt, pi

import random

import datetime

# Module -  a single python file.
# Package  - a directory or folder containing multiple modules

sqrt_of_16 = sqrt(16)
print("The square root of 16 is: ", sqrt_of_16)

circle_area = pi * (5 ** 2)
print("The area of the circle is: ", circle_area)



random_number = random.randint(1, 100)
print("A random number between 1 and 100 is: ", random_number)

choice = random.choice(["Ekene", "Joice", 890, True, "Lagos"])
print("A random choice from the list is: ", choice)


today = datetime.date.today()
print("Today's date is: ", today)



# Talking To the Operating System
import os

current_directory = os.getcwd()
print("The current working directory is: ", current_directory)




# Working with Pandas
import pandas as pd



# Generate a doc of all packages: pip freeze > requirements.txt
# When someone gets into the project they can run: pip install -r requirements.txt

# Install specific package: pip install package_name==version
