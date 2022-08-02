import time
from turtle import Screen, Turtle
from car_manager import CarManager
from player import Player

screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)
car_manager = CarManager()

from scoreboard import Scoreboard
scoreboard = Scoreboard()
player = Player()



game_on = True
x = 1
while game_on:
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")
    time.sleep(0.1*x)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            game_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        print("Yay")
        scoreboard.increase_level()
        scoreboard.clear()
        scoreboard.update_level()
        x *= 0.6
        player.hideturtle()
        player = Player()

screen.exitonclick()
