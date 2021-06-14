import random

# random integer between 10 and 20 (both inclusive)
number = random.randint(10, 20)
print(number)

random_float = random.random()
print(random_float)

random_float_between_0_and_5 = random.random()*random.randint(0, 5)
print(random_float_between_0_and_5)