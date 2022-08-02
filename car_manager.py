from turtle import Turtle

import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []


    def create_car(self):
        a = random.randint(1, 7)
        r = random.randint(0, 254)
        g = random.randint(0, 254)
        b = random.randint(0, 254)
        if a == 2:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(r, g, b)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(5)
