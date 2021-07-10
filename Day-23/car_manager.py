from turtle import Turtle
import random

COLORS = ["red", "orange", "pink", "green", "blue", "purple", "CornflowerBlue", "yellow", "IndianRed",
          "DeepSkyBlue", "LightSeaGreen",
          "SeaGreen"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-280, 280)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def level_up(self):
        self.move_speed += MOVE_INCREMENT
