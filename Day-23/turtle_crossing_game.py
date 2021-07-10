import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car()
    car_manager.move()
    score.update_scoreboard()

    # check if player reaches the top
    if player.ycor() > 280:
        score.increase_level()
        player.go_to_start()
        car_manager.level_up()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            score.game_over()
            game_is_on = False

screen.exitonclick()
