import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreBoard = Scoreboard()

player.paint_finish_line()

screen.listen()
screen.onkey(player.walk, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.create_car()
    carManager.move_cars()

    if player.finish_check():
        player.go_start()
        carManager.level_up()
        scoreBoard.level_up()

        if scoreBoard.check_highscore():
            scoreBoard.write_score()

    for car in carManager.allCars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreBoard.write_score()
            scoreBoard.game_over()

screen.exitonclick()
