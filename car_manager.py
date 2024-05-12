from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []
        self.Repeater = 0
        self.carColumnInfo = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if (randint(1,4) == 3):
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)

            newCar.penup()
            newCar.color(choice(COLORS))

            randomY_position = randint(-10, 10) * 20
            newCar.goto(300, randomY_position)

            self.allCars.append(newCar)

    def move_cars(self):
        for car in self.allCars:
            car.backward(self.carSpeed)

    def level_up(self):
        self.carSpeed += MOVE_INCREMENT
