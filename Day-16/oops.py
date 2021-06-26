# attributes -  variables of a object
# methods -  functions that an object performs


# class - A Class in object oriented programming is a blueprint or prototype
#         that defines the variables and the methods (functions)

# object - An object in OOPS is a specimen of a class.
#          Software objects are often used to model real-world objects you find in everyday life


# turtle-graphics
from turtle import Turtle, Screen

timmy = Turtle()
# prints the object
# print(timmy)
# methods
# timmy.shape('turtle')
# timmy.color('SpringGreen')
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon_name", ['Pikachu', "chuchu"])
table.add_column("Type", ["Electric", "Hungry"])
print(table)
