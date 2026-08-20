import random


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method.")



class SquigglyLine:
    """A class representing a wavy, unpredictable line."""
    
    def __init__(self, color: str, initial_length: float):
        """Initialize the line with a color and a starting length."""
        self.color = color          # Public attribute
        self.length = initial_length # Public attribute
        self._is_straight = False    # Protected attribute (by convention)

    # Other dunder methods added below
    # Triggered automatically when you call print(object)
    def __str__(self):
        pattern = "~" * self.length
        return f"SquigglyLine object with pattern: {pattern}"

    # Triggered automatically when you call len(object)
    def __len__(self):
        pattern = "~" * self.length
        return len(pattern)
        
    def draw(self) -> str:
        """Return a text representation of the squiggly line."""
        visual = "~" * int(self.length)
        return f"Drawing a {self.color} squiggly line: {visual}"
    
    def wiggle(self) -> None:
        """Simulate the line shifting, which randomly changes its length."""
        change = random.choice([-2, -1, 1, 2])
        # Ensure length never drops below 1
        self.length = max(1.0, self.length + change)
        print(f"The line wiggled! New length: {self.length}")




# --- How to use the class ---

# 1. Instantiate (create) an object from the class
my_line = SquigglyLine(color="neon green", initial_length=15)

# 2. Access attributes
print(f"Line Color: {my_line.color}")

# 3. Call methods
print(my_line.draw())
my_line.wiggle()
print(my_line.draw())






class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"

# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)        # gpt-3.5-turbo
print(prod_config.model)       # gpt-4
print(prod_config.max_tokens)  # 1000





class Dog(Animal):
    def make_sound(self):
        print(self.name, "says woof!")

    def bark(self):
        print(self.name, "Bark! Bark!! Bark!!!")


dog = Dog(name="Buddy", species="Canine")

dog.make_sound()
dog.bark()




"""


Programming paradigms
Python supports multiple programming styles. The two main ones are:

1. Functional programming - Using functions to transform data
2. Object-oriented programming - Using classes to bundle data and behavior



When to use classes
Use classes when you need to:
1. Keep track of state between operations
2. Group related data and functions together
3. Create multiple instances with similar behavior
4. Model real-world objects or concepts
​
When to use functions
Use functions when you have:
1. Simple transformations (input → output)
2. Stateless operations
3. One-off calculations
4. Small scripts

"""