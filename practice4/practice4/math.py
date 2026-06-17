import math
import random

# Built-in functions
print(min(5, 8, 2))
print(max(5, 8, 2))
print(abs(-15))
print(round(3.14159, 2))
print(pow(2, 5))

# math module
print(math.sqrt(81))
print(math.ceil(6.2))
print(math.floor(6.9))
print(math.sin(math.pi / 2))
print(math.cos(0))
print(math.pi)
print(math.e)

# random module
print(random.random())
print(random.randint(1, 100))

colors = ["red", "blue", "green"]

print(random.choice(colors))

random.shuffle(colors)

print(colors)